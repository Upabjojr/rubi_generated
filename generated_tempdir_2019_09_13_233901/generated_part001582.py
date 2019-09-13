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

class CommutativeMatcher47144(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({0: 1, 1: 1}), [
      (VariableWithCount('i4.2.0', 1, 1, S(1)), Mul)
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
        if CommutativeMatcher47144._instance is None:
            CommutativeMatcher47144._instance = CommutativeMatcher47144()
        return CommutativeMatcher47144._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 47143
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i4.2.2', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 47145
            subst2 = Substitution(subst1)
            try:
                subst2.try_add_variable('i4.2.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 47146
                subst3 = Substitution(subst2)
                try:
                    subst3.try_add_variable('i4.2.2.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 47147
                    if len(subjects) >= 1:
                        tmp4 = subjects.popleft()
                        subst4 = Substitution(subst3)
                        try:
                            subst4.try_add_variable('i4.2.2.1.0', tmp4)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 47148
                            if len(subjects) == 0:
                                pass
                                # 0: (a + x*b)**n1
                        subjects.appendleft(tmp4)
                if len(subjects) >= 1 and isinstance(subjects[0], Mul):
                    tmp6 = subjects.popleft()
                    associative1 = tmp6
                    associative_type1 = type(tmp6)
                    subjects7 = deque(tmp6._args)
                    matcher = CommutativeMatcher47150.get()
                    tmp8 = subjects7
                    subjects7 = []
                    for s in tmp8:
                        matcher.add_subject(s)
                    for pattern_index, subst3 in matcher.match(tmp8, subst2):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 47151
                            if len(subjects) == 0:
                                pass
                                # 0: (a + x*b)**n1
                    subjects.appendleft(tmp6)
            if len(subjects) >= 1 and isinstance(subjects[0], Add):
                tmp9 = subjects.popleft()
                associative1 = tmp9
                associative_type1 = type(tmp9)
                subjects10 = deque(tmp9._args)
                matcher = CommutativeMatcher47153.get()
                tmp11 = subjects10
                subjects10 = []
                for s in tmp11:
                    matcher.add_subject(s)
                for pattern_index, subst2 in matcher.match(tmp11, subst1):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 47159
                        if len(subjects) == 0:
                            pass
                            # 0: (a + x*b)**n1
                subjects.appendleft(tmp9)
        if len(subjects) >= 1 and isinstance(subjects[0], Pow):
            tmp12 = subjects.popleft()
            subjects13 = deque(tmp12._args)
            # State 47160
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i4.2.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 47161
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i4.2.2.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 47162
                    if len(subjects13) >= 1:
                        tmp16 = subjects13.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i4.2.2.1.0', tmp16)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 47163
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i4.2.2', 1)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 47164
                                if len(subjects13) == 0:
                                    pass
                                    # State 47165
                                    if len(subjects) == 0:
                                        pass
                                        # 0: (a + x*b)**n1
                            if len(subjects13) >= 1:
                                tmp19 = subjects13.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i4.2.2', tmp19)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 47164
                                    if len(subjects13) == 0:
                                        pass
                                        # State 47165
                                        if len(subjects) == 0:
                                            pass
                                            # 0: (a + x*b)**n1
                                subjects13.appendleft(tmp19)
                        subjects13.appendleft(tmp16)
                if len(subjects13) >= 1 and isinstance(subjects13[0], Mul):
                    tmp21 = subjects13.popleft()
                    associative1 = tmp21
                    associative_type1 = type(tmp21)
                    subjects22 = deque(tmp21._args)
                    matcher = CommutativeMatcher47167.get()
                    tmp23 = subjects22
                    subjects22 = []
                    for s in tmp23:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp23, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 47168
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i4.2.2', 1)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 47169
                                if len(subjects13) == 0:
                                    pass
                                    # State 47170
                                    if len(subjects) == 0:
                                        pass
                                        # 0: (a + x*b)**n1
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
                                    subst3 = Substitution(subst2)
                                    try:
                                        subst3.try_add_variable('i4.2.2', tmp26)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 47169
                                        if len(subjects13) == 0:
                                            pass
                                            # State 47170
                                            if len(subjects) == 0:
                                                pass
                                                # 0: (a + x*b)**n1
                                    if len(subjects13) == 0:
                                        break
                                    tmp25.append(subjects13.popleft())
                                subjects13.extendleft(reversed(tmp25))
                    subjects13.appendleft(tmp21)
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i4.2.2.0_1', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 47181
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i4.2.2.1.0_2', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 47182
                    if len(subjects13) >= 1:
                        tmp30 = subjects13.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i4.2.2.1.0', tmp30)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 47183
                            if len(subjects13) >= 1:
                                tmp32 = subjects13.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i4.2.2_1', tmp32)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 47184
                                    if len(subjects13) == 0:
                                        pass
                                        # State 47185
                                        if len(subjects) == 0:
                                            pass
                                            # 1: (c + x*d)**n2
                                subjects13.appendleft(tmp32)
                        subjects13.appendleft(tmp30)
                if len(subjects13) >= 1 and isinstance(subjects13[0], Mul):
                    tmp34 = subjects13.popleft()
                    associative1 = tmp34
                    associative_type1 = type(tmp34)
                    subjects35 = deque(tmp34._args)
                    matcher = CommutativeMatcher47187.get()
                    tmp36 = subjects35
                    subjects35 = []
                    for s in tmp36:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp36, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 47188
                            if len(subjects13) >= 1:
                                tmp37 = []
                                tmp37.append(subjects13.popleft())
                                while True:
                                    if len(tmp37) > 1:
                                        tmp38 = create_operation_expression(associative1, tmp37)
                                    elif len(tmp37) == 1:
                                        tmp38 = tmp37[0]
                                    else:
                                        assert False, "Unreachable"
                                    subst3 = Substitution(subst2)
                                    try:
                                        subst3.try_add_variable('i4.2.2_1', tmp38)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 47189
                                        if len(subjects13) == 0:
                                            pass
                                            # State 47190
                                            if len(subjects) == 0:
                                                pass
                                                # 1: (c + x*d)**n2
                                    if len(subjects13) == 0:
                                        break
                                    tmp37.append(subjects13.popleft())
                                subjects13.extendleft(reversed(tmp37))
                    subjects13.appendleft(tmp34)
            if len(subjects13) >= 1 and isinstance(subjects13[0], Add):
                tmp40 = subjects13.popleft()
                associative1 = tmp40
                associative_type1 = type(tmp40)
                subjects41 = deque(tmp40._args)
                matcher = CommutativeMatcher47172.get()
                tmp42 = subjects41
                subjects41 = []
                for s in tmp42:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp42, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 47178
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i4.2.2', 1)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 47179
                            if len(subjects13) == 0:
                                pass
                                # State 47180
                                if len(subjects) == 0:
                                    pass
                                    # 0: (a + x*b)**n1
                        if len(subjects13) >= 1:
                            tmp44 = []
                            tmp44.append(subjects13.popleft())
                            while True:
                                if len(tmp44) > 1:
                                    tmp45 = create_operation_expression(associative1, tmp44)
                                elif len(tmp44) == 1:
                                    tmp45 = tmp44[0]
                                else:
                                    assert False, "Unreachable"
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i4.2.2', tmp45)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 47179
                                    if len(subjects13) == 0:
                                        pass
                                        # State 47180
                                        if len(subjects) == 0:
                                            pass
                                            # 0: (a + x*b)**n1
                                if len(subjects13) == 0:
                                    break
                                tmp44.append(subjects13.popleft())
                            subjects13.extendleft(reversed(tmp44))
                    if pattern_index == 1:
                        pass
                        # State 47194
                        if len(subjects13) >= 1:
                            tmp47 = []
                            tmp47.append(subjects13.popleft())
                            while True:
                                if len(tmp47) > 1:
                                    tmp48 = create_operation_expression(associative1, tmp47)
                                elif len(tmp47) == 1:
                                    tmp48 = tmp47[0]
                                else:
                                    assert False, "Unreachable"
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i4.2.2_1', tmp48)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 47195
                                    if len(subjects13) == 0:
                                        pass
                                        # State 47196
                                        if len(subjects) == 0:
                                            pass
                                            # 1: (c + x*d)**n2
                                if len(subjects13) == 0:
                                    break
                                tmp47.append(subjects13.popleft())
                            subjects13.extendleft(reversed(tmp47))
                subjects13.appendleft(tmp40)
            subjects.appendleft(tmp12)
        return
        yield


from matchpy.utils import VariableWithCount
from matchpy.matching.many_to_one import CommutativeMatcher
from multiset import Multiset
from collections import deque
