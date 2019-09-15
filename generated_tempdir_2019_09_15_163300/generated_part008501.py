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


class CommutativeMatcher17009(CommutativeMatcher):
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
    4: (4, Multiset({4: 1}), [
      (VariableWithCount('i4.1.0', 1, 1, S(1)), Mul)
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
        if CommutativeMatcher17009._instance is None:
            CommutativeMatcher17009._instance = CommutativeMatcher17009()
        return CommutativeMatcher17009._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 17008
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i4.1.1.0', S(0))
        except ValueError:
            pass
        else:
            pass
            # State 17010
            subst2 = Substitution(subst1)
            try:
                subst2.try_add_variable('i4.1.1.1.0_1', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 17011
                if len(subjects) >= 1:
                    tmp3 = subjects.popleft()
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i4.1.1.1.0', tmp3)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 17012
                        if len(subjects) == 0:
                            pass
                            # 0: c + x*d /; (cons_f1101) and (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1115)
                            yield 0, subst3
                    subjects.appendleft(tmp3)
            if len(subjects) >= 1 and isinstance(subjects[0], Mul):
                tmp5 = subjects.popleft()
                associative1 = tmp5
                associative_type1 = type(tmp5)
                subjects6 = deque(tmp5._args)
                matcher = CommutativeMatcher17014.get()
                tmp7 = subjects6
                subjects6 = []
                for s in tmp7:
                    matcher.add_subject(s)
                for pattern_index, subst2 in matcher.match(tmp7, subst1):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 17015
                        if len(subjects) == 0:
                            pass
                            # 0: c + x*d /; (cons_f1101) and (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1115)
                            yield 0, subst2
                subjects.appendleft(tmp5)
        if len(subjects) >= 1 and isinstance(subjects[0], Add):
            tmp8 = subjects.popleft()
            associative1 = tmp8
            associative_type1 = type(tmp8)
            subjects9 = deque(tmp8._args)
            matcher = CommutativeMatcher17017.get()
            tmp10 = subjects9
            subjects9 = []
            for s in tmp10:
                matcher.add_subject(s)
            for pattern_index, subst1 in matcher.match(tmp10, subst0):
                pass
                if pattern_index == 0:
                    pass
                    # State 17023
                    if len(subjects) == 0:
                        pass
                        # 0: c + x*d /; (cons_f1101) and (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1115)
                        yield 0, subst1
            subjects.appendleft(tmp8)
        if len(subjects) >= 1 and isinstance(subjects[0], Pow):
            tmp11 = subjects.popleft()
            subjects12 = deque(tmp11._args)
            # State 17096
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i4.1.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 17097
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i4.1.2.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 17098
                    if len(subjects12) >= 1:
                        tmp15 = subjects12.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i4.1.2.1.0', tmp15)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 17099
                            if len(subjects12) >= 1 and subjects12[0] == Integer(2):
                                tmp17 = subjects12.popleft()
                                # State 17100
                                if len(subjects12) == 0:
                                    pass
                                    # State 17101
                                    if len(subjects) == 0:
                                        pass
                                        # 1: (c + x*d)**2 /; (cons_f1101) and (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29)
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
                                    # State 17187
                                    if len(subjects12) == 0:
                                        pass
                                        # State 17188
                                        if len(subjects) == 0:
                                            pass
                                            # 2: (c + x*d)**n /; (cons_f1101) and (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1116) and (cons_f198)
                                            yield 2, subst4
                                            # 3: (c + x*d)**n /; (cons_f1101) and (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1116) and (cons_f25)
                                            yield 3, subst4
                                            # 4: (c + x*d)**n /; (cons_f1101) and (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f1117)
                                            yield 4, subst4
                                subjects12.appendleft(tmp18)
                        subjects12.appendleft(tmp15)
                if len(subjects12) >= 1 and isinstance(subjects12[0], Mul):
                    tmp20 = subjects12.popleft()
                    associative1 = tmp20
                    associative_type1 = type(tmp20)
                    subjects21 = deque(tmp20._args)
                    matcher = CommutativeMatcher17103.get()
                    tmp22 = subjects21
                    subjects21 = []
                    for s in tmp22:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp22, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 17104
                            if len(subjects12) >= 1 and subjects12[0] == Integer(2):
                                tmp23 = subjects12.popleft()
                                # State 17105
                                if len(subjects12) == 0:
                                    pass
                                    # State 17106
                                    if len(subjects) == 0:
                                        pass
                                        # 1: (c + x*d)**2 /; (cons_f1101) and (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29)
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
                                        # State 17189
                                        if len(subjects12) == 0:
                                            pass
                                            # State 17190
                                            if len(subjects) == 0:
                                                pass
                                                # 2: (c + x*d)**n /; (cons_f1101) and (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1116) and (cons_f198)
                                                yield 2, subst3
                                                # 3: (c + x*d)**n /; (cons_f1101) and (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1116) and (cons_f25)
                                                yield 3, subst3
                                                # 4: (c + x*d)**n /; (cons_f1101) and (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f1117)
                                                yield 4, subst3
                                    if len(subjects12) == 0:
                                        break
                                    tmp24.append(subjects12.popleft())
                                subjects12.extendleft(reversed(tmp24))
                    subjects12.appendleft(tmp20)
            if len(subjects12) >= 1 and isinstance(subjects12[0], Add):
                tmp27 = subjects12.popleft()
                associative1 = tmp27
                associative_type1 = type(tmp27)
                subjects28 = deque(tmp27._args)
                matcher = CommutativeMatcher17108.get()
                tmp29 = subjects28
                subjects28 = []
                for s in tmp29:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp29, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 17114
                        if len(subjects12) >= 1 and subjects12[0] == Integer(2):
                            tmp30 = subjects12.popleft()
                            # State 17115
                            if len(subjects12) == 0:
                                pass
                                # State 17116
                                if len(subjects) == 0:
                                    pass
                                    # 1: (c + x*d)**2 /; (cons_f1101) and (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29)
                                    yield 1, subst1
                            subjects12.appendleft(tmp30)
                        if len(subjects12) >= 1:
                            tmp31 = []
                            tmp31.append(subjects12.popleft())
                            while True:
                                if len(tmp31) > 1:
                                    tmp32 = create_operation_expression(associative1, tmp31)
                                elif len(tmp31) == 1:
                                    tmp32 = tmp31[0]
                                else:
                                    assert False, "Unreachable"
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i4.1.2', tmp32)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 17191
                                    if len(subjects12) == 0:
                                        pass
                                        # State 17192
                                        if len(subjects) == 0:
                                            pass
                                            # 2: (c + x*d)**n /; (cons_f1101) and (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1116) and (cons_f198)
                                            yield 2, subst2
                                            # 3: (c + x*d)**n /; (cons_f1101) and (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1116) and (cons_f25)
                                            yield 3, subst2
                                            # 4: (c + x*d)**n /; (cons_f1101) and (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f1117)
                                            yield 4, subst2
                                if len(subjects12) == 0:
                                    break
                                tmp31.append(subjects12.popleft())
                            subjects12.extendleft(reversed(tmp31))
                subjects12.appendleft(tmp27)
            subjects.appendleft(tmp11)
        return
        yield


from .generated_part008503 import *
from matchpy.matching.many_to_one import CommutativeMatcher
from collections import deque
from .generated_part008506 import *
from .generated_part008502 import *
from matchpy.utils import VariableWithCount
from multiset import Multiset
from .generated_part008505 import *