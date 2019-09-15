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


class CommutativeMatcher49164(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({0: 1}), [
      (VariableWithCount('i3.2.1.0', 1, 1, S(1)), Mul)
]),
    1: (1, Multiset({1: 1}), [
      (VariableWithCount('i3.2.1.0', 1, 1, S(1)), Mul)
]),
    2: (2, Multiset({2: 1}), [
      (VariableWithCount('i3.2.1.0', 1, 1, S(1)), Mul)
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
        if CommutativeMatcher49164._instance is None:
            CommutativeMatcher49164._instance = CommutativeMatcher49164()
        return CommutativeMatcher49164._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 49163
        if len(subjects) >= 1 and isinstance(subjects[0], Pow):
            tmp1 = subjects.popleft()
            subjects2 = deque(tmp1._args)
            # State 49165
            if len(subjects2) >= 1:
                tmp3 = subjects2.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i3.2.1.1', tmp3)
                except ValueError:
                    pass
                else:
                    pass
                    # State 49166
                    if len(subjects2) >= 1:
                        tmp5 = subjects2.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i3.2.1.2', tmp5)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 49167
                            if len(subjects2) == 0:
                                pass
                                # State 49168
                                if len(subjects) == 0:
                                    pass
                                    # 0: x**n
                                    yield 0, subst2
                        subjects2.appendleft(tmp5)
                subjects2.appendleft(tmp3)
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i3.2.1.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 51141
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i3.2.1.2.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 51142
                    if len(subjects2) >= 1:
                        tmp9 = subjects2.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i3.2.1.2.1.0', tmp9)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 51143
                            if len(subjects2) >= 1:
                                tmp11 = subjects2.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i3.2.1.2', tmp11)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 51144
                                    if len(subjects2) == 0:
                                        pass
                                        # State 51145
                                        if len(subjects) == 0:
                                            pass
                                            # 1: (d + x*e)**n
                                            yield 1, subst4
                                subjects2.appendleft(tmp11)
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i3.2.1.2', 1)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 51339
                                if len(subjects2) == 0:
                                    pass
                                    # State 51340
                                    if len(subjects) == 0:
                                        pass
                                        # 2: (d + x*e)**n
                                        yield 2, subst4
                            if len(subjects2) >= 1:
                                tmp14 = subjects2.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i3.2.1.2', tmp14)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 51339
                                    if len(subjects2) == 0:
                                        pass
                                        # State 51340
                                        if len(subjects) == 0:
                                            pass
                                            # 2: (d + x*e)**n
                                            yield 2, subst4
                                subjects2.appendleft(tmp14)
                        subjects2.appendleft(tmp9)
                if len(subjects2) >= 1 and isinstance(subjects2[0], Mul):
                    tmp16 = subjects2.popleft()
                    associative1 = tmp16
                    associative_type1 = type(tmp16)
                    subjects17 = deque(tmp16._args)
                    matcher = CommutativeMatcher51147.get()
                    tmp18 = subjects17
                    subjects17 = []
                    for s in tmp18:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp18, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 51148
                            if len(subjects2) >= 1:
                                tmp19 = []
                                tmp19.append(subjects2.popleft())
                                while True:
                                    if len(tmp19) > 1:
                                        tmp20 = create_operation_expression(associative1, tmp19)
                                    elif len(tmp19) == 1:
                                        tmp20 = tmp19[0]
                                    else:
                                        assert False, "Unreachable"
                                    subst3 = Substitution(subst2)
                                    try:
                                        subst3.try_add_variable('i3.2.1.2', tmp20)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 51149
                                        if len(subjects2) == 0:
                                            pass
                                            # State 51150
                                            if len(subjects) == 0:
                                                pass
                                                # 1: (d + x*e)**n
                                                yield 1, subst3
                                    if len(subjects2) == 0:
                                        break
                                    tmp19.append(subjects2.popleft())
                                subjects2.extendleft(reversed(tmp19))
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i3.2.1.2', 1)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 51341
                                if len(subjects2) == 0:
                                    pass
                                    # State 51342
                                    if len(subjects) == 0:
                                        pass
                                        # 2: (d + x*e)**n
                                        yield 2, subst3
                            if len(subjects2) >= 1:
                                tmp23 = []
                                tmp23.append(subjects2.popleft())
                                while True:
                                    if len(tmp23) > 1:
                                        tmp24 = create_operation_expression(associative1, tmp23)
                                    elif len(tmp23) == 1:
                                        tmp24 = tmp23[0]
                                    else:
                                        assert False, "Unreachable"
                                    subst3 = Substitution(subst2)
                                    try:
                                        subst3.try_add_variable('i3.2.1.2', tmp24)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 51341
                                        if len(subjects2) == 0:
                                            pass
                                            # State 51342
                                            if len(subjects) == 0:
                                                pass
                                                # 2: (d + x*e)**n
                                                yield 2, subst3
                                    if len(subjects2) == 0:
                                        break
                                    tmp23.append(subjects2.popleft())
                                subjects2.extendleft(reversed(tmp23))
                    subjects2.appendleft(tmp16)
            if len(subjects2) >= 1 and isinstance(subjects2[0], Add):
                tmp26 = subjects2.popleft()
                associative1 = tmp26
                associative_type1 = type(tmp26)
                subjects27 = deque(tmp26._args)
                matcher = CommutativeMatcher51152.get()
                tmp28 = subjects27
                subjects27 = []
                for s in tmp28:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp28, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 51158
                        if len(subjects2) >= 1:
                            tmp29 = []
                            tmp29.append(subjects2.popleft())
                            while True:
                                if len(tmp29) > 1:
                                    tmp30 = create_operation_expression(associative1, tmp29)
                                elif len(tmp29) == 1:
                                    tmp30 = tmp29[0]
                                else:
                                    assert False, "Unreachable"
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i3.2.1.2', tmp30)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 51159
                                    if len(subjects2) == 0:
                                        pass
                                        # State 51160
                                        if len(subjects) == 0:
                                            pass
                                            # 1: (d + x*e)**n
                                            yield 1, subst2
                                if len(subjects2) == 0:
                                    break
                                tmp29.append(subjects2.popleft())
                            subjects2.extendleft(reversed(tmp29))
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i3.2.1.2', 1)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 51343
                            if len(subjects2) == 0:
                                pass
                                # State 51344
                                if len(subjects) == 0:
                                    pass
                                    # 2: (d + x*e)**n
                                    yield 2, subst2
                        if len(subjects2) >= 1:
                            tmp33 = []
                            tmp33.append(subjects2.popleft())
                            while True:
                                if len(tmp33) > 1:
                                    tmp34 = create_operation_expression(associative1, tmp33)
                                elif len(tmp33) == 1:
                                    tmp34 = tmp33[0]
                                else:
                                    assert False, "Unreachable"
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i3.2.1.2', tmp34)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 51343
                                    if len(subjects2) == 0:
                                        pass
                                        # State 51344
                                        if len(subjects) == 0:
                                            pass
                                            # 2: (d + x*e)**n
                                            yield 2, subst2
                                if len(subjects2) == 0:
                                    break
                                tmp33.append(subjects2.popleft())
                            subjects2.extendleft(reversed(tmp33))
                subjects2.appendleft(tmp26)
            subjects.appendleft(tmp1)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i3.2.1.2', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 51324
            subst2 = Substitution(subst1)
            try:
                subst2.try_add_variable('i3.2.1.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 51325
                subst3 = Substitution(subst2)
                try:
                    subst3.try_add_variable('i3.2.1.2.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 51326
                    if len(subjects) >= 1:
                        tmp39 = subjects.popleft()
                        subst4 = Substitution(subst3)
                        try:
                            subst4.try_add_variable('i3.2.1.2.1.0', tmp39)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 51327
                            if len(subjects) == 0:
                                pass
                                # 2: (d + x*e)**n
                                yield 2, subst4
                        subjects.appendleft(tmp39)
                if len(subjects) >= 1 and isinstance(subjects[0], Mul):
                    tmp41 = subjects.popleft()
                    associative1 = tmp41
                    associative_type1 = type(tmp41)
                    subjects42 = deque(tmp41._args)
                    matcher = CommutativeMatcher51329.get()
                    tmp43 = subjects42
                    subjects42 = []
                    for s in tmp43:
                        matcher.add_subject(s)
                    for pattern_index, subst3 in matcher.match(tmp43, subst2):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 51330
                            if len(subjects) == 0:
                                pass
                                # 2: (d + x*e)**n
                                yield 2, subst3
                    subjects.appendleft(tmp41)
            if len(subjects) >= 1 and isinstance(subjects[0], Add):
                tmp44 = subjects.popleft()
                associative1 = tmp44
                associative_type1 = type(tmp44)
                subjects45 = deque(tmp44._args)
                matcher = CommutativeMatcher51332.get()
                tmp46 = subjects45
                subjects45 = []
                for s in tmp46:
                    matcher.add_subject(s)
                for pattern_index, subst2 in matcher.match(tmp46, subst1):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 51338
                        if len(subjects) == 0:
                            pass
                            # 2: (d + x*e)**n
                            yield 2, subst2
                subjects.appendleft(tmp44)
        return
        yield


from matchpy.matching.many_to_one import CommutativeMatcher
from .generated_part010176 import *
from .generated_part010179 import *
from collections import deque
from .generated_part010175 import *
from matchpy.utils import VariableWithCount
from multiset import Multiset
from .generated_part010178 import *