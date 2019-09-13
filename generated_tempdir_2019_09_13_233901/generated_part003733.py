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

class CommutativeMatcher3349(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({}), [
      (VariableWithCount('i2.2.0', 1, 1, None), Mul),
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul)
]),
    1: (1, Multiset({0: 1}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul)
]),
    2: (2, Multiset({1: 1}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul)
]),
    3: (3, Multiset({2: 1}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul)
]),
    4: (4, Multiset({3: 1}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul)
]),
    5: (5, Multiset({4: 1}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul)
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
        if CommutativeMatcher3349._instance is None:
            CommutativeMatcher3349._instance = CommutativeMatcher3349()
        return CommutativeMatcher3349._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 3348
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.2_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 7488
            if len(subjects) >= 1:
                tmp2 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.0_1', tmp2)
                except ValueError:
                    pass
                else:
                    pass
                    # State 7489
                    if len(subjects) == 0:
                        pass
                        # 0: x**n
                subjects.appendleft(tmp2)
        if len(subjects) >= 1 and isinstance(subjects[0], Pow):
            tmp4 = subjects.popleft()
            subjects5 = deque(tmp4._args)
            # State 7490
            if len(subjects5) >= 1:
                tmp6 = subjects5.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.0_1', tmp6)
                except ValueError:
                    pass
                else:
                    pass
                    # State 7491
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.2_1', 1)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 7492
                        if len(subjects5) == 0:
                            pass
                            # State 7493
                            if len(subjects) == 0:
                                pass
                                # 0: x**n
                    if len(subjects5) >= 1:
                        tmp9 = subjects5.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.1.2_1', tmp9)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 7492
                            if len(subjects5) == 0:
                                pass
                                # State 7493
                                if len(subjects) == 0:
                                    pass
                                    # 0: x**n
                        subjects5.appendleft(tmp9)
                subjects5.appendleft(tmp6)
            subjects.appendleft(tmp4)
        if len(subjects) >= 1 and isinstance(subjects[0], asin):
            tmp11 = subjects.popleft()
            subjects12 = deque(tmp11._args)
            # State 109019
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.0', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 109020
                if len(subjects12) >= 1:
                    tmp14 = subjects12.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.0', tmp14)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 109021
                        if len(subjects12) == 0:
                            pass
                            # State 109022
                            if len(subjects) == 0:
                                pass
                                # 1: asin(x*c)
                    subjects12.appendleft(tmp14)
            if len(subjects12) >= 1 and isinstance(subjects12[0], Mul):
                tmp16 = subjects12.popleft()
                associative1 = tmp16
                associative_type1 = type(tmp16)
                subjects17 = deque(tmp16._args)
                matcher = CommutativeMatcher109024.get()
                tmp18 = subjects17
                subjects17 = []
                for s in tmp18:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp18, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 109025
                        if len(subjects12) == 0:
                            pass
                            # State 109026
                            if len(subjects) == 0:
                                pass
                                # 1: asin(x*c)
                subjects12.appendleft(tmp16)
            subjects.appendleft(tmp11)
        if len(subjects) >= 1 and isinstance(subjects[0], acos):
            tmp19 = subjects.popleft()
            subjects20 = deque(tmp19._args)
            # State 109088
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.0', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 109089
                if len(subjects20) >= 1:
                    tmp22 = subjects20.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.0', tmp22)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 109090
                        if len(subjects20) == 0:
                            pass
                            # State 109091
                            if len(subjects) == 0:
                                pass
                                # 2: acos(x*c)
                    subjects20.appendleft(tmp22)
            if len(subjects20) >= 1 and isinstance(subjects20[0], Mul):
                tmp24 = subjects20.popleft()
                associative1 = tmp24
                associative_type1 = type(tmp24)
                subjects25 = deque(tmp24._args)
                matcher = CommutativeMatcher109093.get()
                tmp26 = subjects25
                subjects25 = []
                for s in tmp26:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp26, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 109094
                        if len(subjects20) == 0:
                            pass
                            # State 109095
                            if len(subjects) == 0:
                                pass
                                # 2: acos(x*c)
                subjects20.appendleft(tmp24)
            subjects.appendleft(tmp19)
        if len(subjects) >= 1 and isinstance(subjects[0], acosh):
            tmp27 = subjects.popleft()
            subjects28 = deque(tmp27._args)
            # State 138778
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.0', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 138779
                if len(subjects28) >= 1:
                    tmp30 = subjects28.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.0', tmp30)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 138780
                        if len(subjects28) == 0:
                            pass
                            # State 138781
                            if len(subjects) == 0:
                                pass
                                # 3: acosh(x*c)
                    subjects28.appendleft(tmp30)
            if len(subjects28) >= 1 and isinstance(subjects28[0], Mul):
                tmp32 = subjects28.popleft()
                associative1 = tmp32
                associative_type1 = type(tmp32)
                subjects33 = deque(tmp32._args)
                matcher = CommutativeMatcher138783.get()
                tmp34 = subjects33
                subjects33 = []
                for s in tmp34:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp34, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 138784
                        if len(subjects28) == 0:
                            pass
                            # State 138785
                            if len(subjects) == 0:
                                pass
                                # 3: acosh(x*c)
                subjects28.appendleft(tmp32)
            subjects.appendleft(tmp27)
        if len(subjects) >= 1 and isinstance(subjects[0], asinh):
            tmp35 = subjects.popleft()
            subjects36 = deque(tmp35._args)
            # State 138847
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.0', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 138848
                if len(subjects36) >= 1:
                    tmp38 = subjects36.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.0', tmp38)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 138849
                        if len(subjects36) == 0:
                            pass
                            # State 138850
                            if len(subjects) == 0:
                                pass
                                # 4: asinh(x*c)
                    subjects36.appendleft(tmp38)
            if len(subjects36) >= 1 and isinstance(subjects36[0], Mul):
                tmp40 = subjects36.popleft()
                associative1 = tmp40
                associative_type1 = type(tmp40)
                subjects41 = deque(tmp40._args)
                matcher = CommutativeMatcher138852.get()
                tmp42 = subjects41
                subjects41 = []
                for s in tmp42:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp42, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 138853
                        if len(subjects36) == 0:
                            pass
                            # State 138854
                            if len(subjects) == 0:
                                pass
                                # 4: asinh(x*c)
                subjects36.appendleft(tmp40)
            subjects.appendleft(tmp35)
        return
        yield


from matchpy.utils import VariableWithCount
from matchpy.matching.many_to_one import CommutativeMatcher
from multiset import Multiset
from collections import deque
