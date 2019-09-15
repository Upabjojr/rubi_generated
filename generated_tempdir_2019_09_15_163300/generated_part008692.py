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


class CommutativeMatcher17046(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({0: 1}), [
      (VariableWithCount('i4.1.0', 1, 1, S(1)), Mul)
]),
    1: (1, Multiset({1: 1}), [
      (VariableWithCount('i4.1.0', 1, 1, S(1)), Mul)
]),
    2: (2, Multiset({2: 1}), [
      (VariableWithCount('i4.1.0', 1, 1, S(1)), Mul)
]),
    3: (3, Multiset({3: 1}), [
      (VariableWithCount('i4.1.0', 1, 1, S(1)), Mul)
]),
    4: (4, Multiset({}), [
      (VariableWithCount('i4.1.0_1', 1, 1, S(1)), Mul),
      (VariableWithCount('i4.1.1', 1, 1, None), Mul)
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
        if CommutativeMatcher17046._instance is None:
            CommutativeMatcher17046._instance = CommutativeMatcher17046()
        return CommutativeMatcher17046._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 17045
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i4.1.1.0', S(0))
        except ValueError:
            pass
        else:
            pass
            # State 17047
            subst2 = Substitution(subst1)
            try:
                subst2.try_add_variable('i4.1.1.1.0_1', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 17048
                if len(subjects) >= 1:
                    tmp3 = subjects.popleft()
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i4.1.1.1.0', tmp3)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 17049
                        if len(subjects) == 0:
                            pass
                            # 0: c + x*d
                            yield 0, subst3
                    subjects.appendleft(tmp3)
            if len(subjects) >= 1 and isinstance(subjects[0], Mul):
                tmp5 = subjects.popleft()
                associative1 = tmp5
                associative_type1 = type(tmp5)
                subjects6 = deque(tmp5._args)
                matcher = CommutativeMatcher17051.get()
                tmp7 = subjects6
                subjects6 = []
                for s in tmp7:
                    matcher.add_subject(s)
                for pattern_index, subst2 in matcher.match(tmp7, subst1):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 17052
                        if len(subjects) == 0:
                            pass
                            # 0: c + x*d
                            yield 0, subst2
                subjects.appendleft(tmp5)
        if len(subjects) >= 1 and isinstance(subjects[0], Add):
            tmp8 = subjects.popleft()
            associative1 = tmp8
            associative_type1 = type(tmp8)
            subjects9 = deque(tmp8._args)
            matcher = CommutativeMatcher17054.get()
            tmp10 = subjects9
            subjects9 = []
            for s in tmp10:
                matcher.add_subject(s)
            for pattern_index, subst1 in matcher.match(tmp10, subst0):
                pass
                if pattern_index == 0:
                    pass
                    # State 17060
                    if len(subjects) == 0:
                        pass
                        # 0: c + x*d
                        yield 0, subst1
            subjects.appendleft(tmp8)
        if len(subjects) >= 1 and isinstance(subjects[0], Pow):
            tmp11 = subjects.popleft()
            subjects12 = deque(tmp11._args)
            # State 17142
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i4.1.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 17143
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i4.1.2.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 17144
                    if len(subjects12) >= 1:
                        tmp15 = subjects12.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i4.1.2.1.0', tmp15)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 17145
                            if len(subjects12) >= 1 and subjects12[0] == Integer(2):
                                tmp17 = subjects12.popleft()
                                # State 17146
                                if len(subjects12) == 0:
                                    pass
                                    # State 17147
                                    if len(subjects) == 0:
                                        pass
                                        # 1: (c + x*d)**2
                                        yield 1, subst3
                                subjects12.appendleft(tmp17)
                            if len(subjects12) >= 1:
                                tmp18 = subjects12.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i4.1.2', tmp18)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 17203
                                    if len(subjects12) == 0:
                                        pass
                                        # State 17204
                                        if len(subjects) == 0:
                                            pass
                                            # 2: (c + x*d)**n
                                            yield 2, subst4
                                subjects12.appendleft(tmp18)
                        subjects12.appendleft(tmp15)
                if len(subjects12) >= 1 and isinstance(subjects12[0], Mul):
                    tmp20 = subjects12.popleft()
                    associative1 = tmp20
                    associative_type1 = type(tmp20)
                    subjects21 = deque(tmp20._args)
                    matcher = CommutativeMatcher17149.get()
                    tmp22 = subjects21
                    subjects21 = []
                    for s in tmp22:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp22, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 17150
                            if len(subjects12) >= 1 and subjects12[0] == Integer(2):
                                tmp23 = subjects12.popleft()
                                # State 17151
                                if len(subjects12) == 0:
                                    pass
                                    # State 17152
                                    if len(subjects) == 0:
                                        pass
                                        # 1: (c + x*d)**2
                                        yield 1, subst2
                                subjects12.appendleft(tmp23)
                            if len(subjects12) >= 1:
                                tmp24 = []
                                tmp24.append(subjects12.popleft())
                                while True:
                                    if len(tmp24) > 1:
                                        tmp25 = create_operation_expression(associative1, tmp24)
                                    elif len(tmp24) == 1:
                                        tmp25 = tmp24[0]
                                    else:
                                        assert False, "Unreachable"
                                    subst3 = Substitution(subst2)
                                    try:
                                        subst3.try_add_variable('i4.1.2', tmp25)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 17205
                                        if len(subjects12) == 0:
                                            pass
                                            # State 17206
                                            if len(subjects) == 0:
                                                pass
                                                # 2: (c + x*d)**n
                                                yield 2, subst3
                                    if len(subjects12) == 0:
                                        break
                                    tmp24.append(subjects12.popleft())
                                subjects12.extendleft(reversed(tmp24))
                    subjects12.appendleft(tmp20)
            if len(subjects12) >= 1:
                tmp27 = subjects12.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i4.1.1', tmp27)
                except ValueError:
                    pass
                else:
                    pass
                    # State 17677
                    if len(subjects12) >= 1 and subjects12[0] == Integer(2):
                        tmp29 = subjects12.popleft()
                        # State 17678
                        if len(subjects12) == 0:
                            pass
                            # State 17679
                            if len(subjects) == 0:
                                pass
                                # 3: x**2
                                yield 3, subst1
                        subjects12.appendleft(tmp29)
                subjects12.appendleft(tmp27)
            if len(subjects12) >= 1 and isinstance(subjects12[0], Add):
                tmp30 = subjects12.popleft()
                associative1 = tmp30
                associative_type1 = type(tmp30)
                subjects31 = deque(tmp30._args)
                matcher = CommutativeMatcher17154.get()
                tmp32 = subjects31
                subjects31 = []
                for s in tmp32:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp32, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 17160
                        if len(subjects12) >= 1 and subjects12[0] == Integer(2):
                            tmp33 = subjects12.popleft()
                            # State 17161
                            if len(subjects12) == 0:
                                pass
                                # State 17162
                                if len(subjects) == 0:
                                    pass
                                    # 1: (c + x*d)**2
                                    yield 1, subst1
                            subjects12.appendleft(tmp33)
                        if len(subjects12) >= 1:
                            tmp34 = []
                            tmp34.append(subjects12.popleft())
                            while True:
                                if len(tmp34) > 1:
                                    tmp35 = create_operation_expression(associative1, tmp34)
                                elif len(tmp34) == 1:
                                    tmp35 = tmp34[0]
                                else:
                                    assert False, "Unreachable"
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i4.1.2', tmp35)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 17207
                                    if len(subjects12) == 0:
                                        pass
                                        # State 17208
                                        if len(subjects) == 0:
                                            pass
                                            # 2: (c + x*d)**n
                                            yield 2, subst2
                                if len(subjects12) == 0:
                                    break
                                tmp34.append(subjects12.popleft())
                            subjects12.extendleft(reversed(tmp34))
                subjects12.appendleft(tmp30)
            subjects.appendleft(tmp11)
        return
        yield


from .generated_part008693 import *
from matchpy.matching.many_to_one import CommutativeMatcher
from collections import deque
from .generated_part008696 import *
from .generated_part008697 import *
from matchpy.utils import VariableWithCount
from multiset import Multiset
from .generated_part008694 import *