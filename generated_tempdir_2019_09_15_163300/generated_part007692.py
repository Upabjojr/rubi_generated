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


class CommutativeMatcher55929(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({0: 1}), [
      (VariableWithCount('i2.2.0_2', 1, 1, S(1)), Mul)
]),
    1: (1, Multiset({1: 1}), [
      (VariableWithCount('i2.2.0_1', 1, 1, S(1)), Mul)
]),
    2: (2, Multiset({2: 1}), [
      (VariableWithCount('i2.2.0', 1, 1, S(1)), Mul)
]),
    3: (3, Multiset({3: 1}), [
      (VariableWithCount('i2.2.0', 1, 1, S(1)), Mul),
      (VariableWithCount('i2.3.0', 1, 1, None), Mul)
]),
    4: (4, Multiset({3: 1, 4: 1}), [
      (VariableWithCount('i2.2.0', 1, 1, S(1)), Mul)
]),
    5: (5, Multiset({3: 1, 5: 1}), [
      (VariableWithCount('i2.2.0', 1, 1, S(1)), Mul)
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
        if CommutativeMatcher55929._instance is None:
            CommutativeMatcher55929._instance = CommutativeMatcher55929()
        return CommutativeMatcher55929._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 55928
        if len(subjects) >= 1 and isinstance(subjects[0], Pow):
            tmp1 = subjects.popleft()
            subjects2 = deque(tmp1._args)
            # State 55930
            if len(subjects2) >= 1:
                tmp3 = subjects2.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.0', tmp3)
                except ValueError:
                    pass
                else:
                    pass
                    # State 55931
                    if len(subjects2) >= 1 and subjects2[0] == Integer(2):
                        tmp5 = subjects2.popleft()
                        # State 55932
                        if len(subjects2) == 0:
                            pass
                            # State 55933
                            if len(subjects) == 0:
                                pass
                                # 0: v**2
                                yield 0, subst1
                        subjects2.appendleft(tmp5)
                subjects2.appendleft(tmp3)
            if len(subjects2) >= 1:
                tmp6 = subjects2.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.1', tmp6)
                except ValueError:
                    pass
                else:
                    pass
                    # State 55968
                    if len(subjects2) >= 1 and subjects2[0] == Integer(2):
                        tmp8 = subjects2.popleft()
                        # State 55969
                        if len(subjects2) == 0:
                            pass
                            # State 55970
                            if len(subjects) == 0:
                                pass
                                # 1: x**2
                                yield 1, subst1
                        subjects2.appendleft(tmp8)
                    if len(subjects2) >= 1:
                        tmp9 = subjects2.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.2', tmp9)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 73587
                            if len(subjects2) == 0:
                                pass
                                # State 73588
                                if len(subjects) == 0:
                                    pass
                                    # 2: x**n
                                    yield 2, subst2
                        subjects2.appendleft(tmp9)
                subjects2.appendleft(tmp6)
            if len(subjects2) >= 1:
                tmp11 = subjects2.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.3.0', tmp11)
                except ValueError:
                    pass
                else:
                    pass
                    # State 106780
                    if len(subjects2) >= 1:
                        tmp13 = subjects2.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.2', tmp13)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 106781
                            if len(subjects2) == 0:
                                pass
                                # State 106782
                                if len(subjects) == 0:
                                    pass
                                    # 4: x**n
                                    yield 4, subst2
                        subjects2.appendleft(tmp13)
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.2', 1)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 106798
                        if len(subjects2) == 0:
                            pass
                            # State 106799
                            if len(subjects) == 0:
                                pass
                                # 5: x**n
                                yield 5, subst2
                    if len(subjects2) >= 1:
                        tmp16 = subjects2.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.2', tmp16)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 106798
                            if len(subjects2) == 0:
                                pass
                                # State 106799
                                if len(subjects) == 0:
                                    pass
                                    # 5: x**n
                                    yield 5, subst2
                        subjects2.appendleft(tmp16)
                subjects2.appendleft(tmp11)
            if len(subjects2) >= 1 and isinstance(subjects2[0], log):
                tmp18 = subjects2.popleft()
                subjects19 = deque(tmp18._args)
                # State 106737
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.3.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 106738
                    if len(subjects19) >= 1:
                        tmp21 = subjects19.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.3.0', tmp21)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 106739
                            if len(subjects19) == 0:
                                pass
                                # State 106740
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i2.3', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 106741
                                    if len(subjects2) == 0:
                                        pass
                                        # State 106742
                                        if len(subjects) == 0:
                                            pass
                                            # 3: log(v*c)**p
                                            yield 3, subst3
                                if len(subjects2) >= 1:
                                    tmp24 = subjects2.popleft()
                                    subst3 = Substitution(subst2)
                                    try:
                                        subst3.try_add_variable('i2.3', tmp24)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 106741
                                        if len(subjects2) == 0:
                                            pass
                                            # State 106742
                                            if len(subjects) == 0:
                                                pass
                                                # 3: log(v*c)**p
                                                yield 3, subst3
                                    subjects2.appendleft(tmp24)
                        subjects19.appendleft(tmp21)
                if len(subjects19) >= 1 and isinstance(subjects19[0], Mul):
                    tmp26 = subjects19.popleft()
                    associative1 = tmp26
                    associative_type1 = type(tmp26)
                    subjects27 = deque(tmp26._args)
                    matcher = CommutativeMatcher106744.get()
                    tmp28 = subjects27
                    subjects27 = []
                    for s in tmp28:
                        matcher.add_subject(s)
                    for pattern_index, subst1 in matcher.match(tmp28, subst0):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 106745
                            if len(subjects19) == 0:
                                pass
                                # State 106746
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i2.3', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 106747
                                    if len(subjects2) == 0:
                                        pass
                                        # State 106748
                                        if len(subjects) == 0:
                                            pass
                                            # 3: log(v*c)**p
                                            yield 3, subst2
                                if len(subjects2) >= 1:
                                    tmp30 = subjects2.popleft()
                                    subst2 = Substitution(subst1)
                                    try:
                                        subst2.try_add_variable('i2.3', tmp30)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 106747
                                        if len(subjects2) == 0:
                                            pass
                                            # State 106748
                                            if len(subjects) == 0:
                                                pass
                                                # 3: log(v*c)**p
                                                yield 3, subst2
                                    subjects2.appendleft(tmp30)
                    subjects19.appendleft(tmp26)
                subjects2.appendleft(tmp18)
            subjects.appendleft(tmp1)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.3', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 106728
            if len(subjects) >= 1 and isinstance(subjects[0], log):
                tmp33 = subjects.popleft()
                subjects34 = deque(tmp33._args)
                # State 106729
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.3.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 106730
                    if len(subjects34) >= 1:
                        tmp36 = subjects34.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.3.0', tmp36)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 106731
                            if len(subjects34) == 0:
                                pass
                                # State 106732
                                if len(subjects) == 0:
                                    pass
                                    # 3: log(v*c)**p
                                    yield 3, subst3
                        subjects34.appendleft(tmp36)
                if len(subjects34) >= 1 and isinstance(subjects34[0], Mul):
                    tmp38 = subjects34.popleft()
                    associative1 = tmp38
                    associative_type1 = type(tmp38)
                    subjects39 = deque(tmp38._args)
                    matcher = CommutativeMatcher106734.get()
                    tmp40 = subjects39
                    subjects39 = []
                    for s in tmp40:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp40, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 106735
                            if len(subjects34) == 0:
                                pass
                                # State 106736
                                if len(subjects) == 0:
                                    pass
                                    # 3: log(v*c)**p
                                    yield 3, subst2
                    subjects34.appendleft(tmp38)
                subjects.appendleft(tmp33)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.2', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 106796
            if len(subjects) >= 1:
                tmp42 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.3.0', tmp42)
                except ValueError:
                    pass
                else:
                    pass
                    # State 106797
                    if len(subjects) == 0:
                        pass
                        # 5: x**n
                        yield 5, subst2
                subjects.appendleft(tmp42)
        return
        yield


from matchpy.matching.many_to_one import CommutativeMatcher
from .generated_part007694 import *
from collections import deque
from matchpy.utils import VariableWithCount
from multiset import Multiset
from .generated_part007693 import *