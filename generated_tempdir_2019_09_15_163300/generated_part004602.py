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


class CommutativeMatcher77707(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({0: 1}), [
      (VariableWithCount('i2.4.0', 1, 1, S(0)), Add)
]),
    1: (1, Multiset({1: 1}), [
      (VariableWithCount('i2.2.3.0', 1, 1, S(0)), Add)
]),
    2: (2, Multiset({2: 1}), [
      (VariableWithCount('i2.2.1.3.0', 1, 1, S(0)), Add)
]),
    3: (3, Multiset({3: 1}), [
      (VariableWithCount('i2.2.2.0', 1, 1, S(0)), Add)
]),
    4: (4, Multiset({4: 1}), [
      (VariableWithCount('i2.2.2.3.0', 1, 1, S(0)), Add)
]),
    5: (5, Multiset({5: 1}), [
      (VariableWithCount('i2.2.4.0', 1, 1, S(0)), Add)
]),
    6: (6, Multiset({6: 1}), [
      (VariableWithCount('i2.2.1.3.0', 1, 1, S(0)), Add)
]),
    7: (7, Multiset({7: 1}), [
      (VariableWithCount('i2.2.1.3.0', 1, 1, S(0)), Add)
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
        if CommutativeMatcher77707._instance is None:
            CommutativeMatcher77707._instance = CommutativeMatcher77707()
        return CommutativeMatcher77707._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 77706
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.4.1.0_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 77708
            if len(subjects) >= 1:
                tmp2 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.4.1.0', tmp2)
                except ValueError:
                    pass
                else:
                    pass
                    # State 77709
                    if len(subjects) == 0:
                        pass
                        # 0: x*f
                        yield 0, subst2
                subjects.appendleft(tmp2)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.3.1.0_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 77769
            if len(subjects) >= 1:
                tmp5 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.3.1.0', tmp5)
                except ValueError:
                    pass
                else:
                    pass
                    # State 77770
                    if len(subjects) == 0:
                        pass
                        # 1: x*f
                        yield 1, subst2
                subjects.appendleft(tmp5)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.3.1.0_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 77847
            if len(subjects) >= 1:
                tmp8 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.3.1.0', tmp8)
                except ValueError:
                    pass
                else:
                    pass
                    # State 77848
                    if len(subjects) == 0:
                        pass
                        # 2: x*f
                        yield 2, subst2
                subjects.appendleft(tmp8)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.2.1.0_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 78216
            if len(subjects) >= 1:
                tmp11 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.2.1.0', tmp11)
                except ValueError:
                    pass
                else:
                    pass
                    # State 78217
                    if len(subjects) == 0:
                        pass
                        # 3: x*f
                        yield 3, subst2
                subjects.appendleft(tmp11)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.2.3.1.0_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 80426
            if len(subjects) >= 1:
                tmp14 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.2.3.1.0', tmp14)
                except ValueError:
                    pass
                else:
                    pass
                    # State 80427
                    if len(subjects) == 0:
                        pass
                        # 4: x*f
                        yield 4, subst2
                subjects.appendleft(tmp14)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.4.1.0_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 80874
            if len(subjects) >= 1:
                tmp17 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.4.1.0', tmp17)
                except ValueError:
                    pass
                else:
                    pass
                    # State 80875
                    if len(subjects) == 0:
                        pass
                        # 5: x*f
                        yield 5, subst2
                subjects.appendleft(tmp17)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.3.1.0', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 88352
            if len(subjects) >= 1 and isinstance(subjects[0], Pow):
                tmp20 = subjects.popleft()
                subjects21 = deque(tmp20._args)
                # State 88353
                if len(subjects21) >= 1:
                    tmp22 = subjects21.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.3.1.1', tmp22)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 88354
                        if len(subjects21) >= 1:
                            tmp24 = subjects21.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.3.1.2', tmp24)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 88355
                                if len(subjects21) == 0:
                                    pass
                                    # State 88356
                                    if len(subjects) == 0:
                                        pass
                                        # 6: d*x**n
                                        yield 6, subst3
                            subjects21.appendleft(tmp24)
                    subjects21.appendleft(tmp22)
                if len(subjects21) >= 1:
                    tmp26 = subjects21.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.0_1', tmp26)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 88925
                        if len(subjects21) >= 1:
                            tmp28 = subjects21.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.3.1.2', tmp28)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 88926
                                if len(subjects21) == 0:
                                    pass
                                    # State 88927
                                    if len(subjects) == 0:
                                        pass
                                        # 7: x**n*d
                                        yield 7, subst3
                            subjects21.appendleft(tmp28)
                    subjects21.appendleft(tmp26)
                subjects.appendleft(tmp20)
        if len(subjects) >= 1 and isinstance(subjects[0], Mul):
            tmp30 = subjects.popleft()
            associative1 = tmp30
            associative_type1 = type(tmp30)
            subjects31 = deque(tmp30._args)
            matcher = CommutativeMatcher77711.get()
            tmp32 = subjects31
            subjects31 = []
            for s in tmp32:
                matcher.add_subject(s)
            for pattern_index, subst1 in matcher.match(tmp32, subst0):
                pass
                if pattern_index == 0:
                    pass
                    # State 77712
                    if len(subjects) == 0:
                        pass
                        # 0: x*f
                        yield 0, subst1
                if pattern_index == 1:
                    pass
                    # State 77771
                    if len(subjects) == 0:
                        pass
                        # 1: x*f
                        yield 1, subst1
                if pattern_index == 2:
                    pass
                    # State 77849
                    if len(subjects) == 0:
                        pass
                        # 2: x*f
                        yield 2, subst1
                if pattern_index == 3:
                    pass
                    # State 78218
                    if len(subjects) == 0:
                        pass
                        # 3: x*f
                        yield 3, subst1
                if pattern_index == 4:
                    pass
                    # State 80428
                    if len(subjects) == 0:
                        pass
                        # 4: x*f
                        yield 4, subst1
                if pattern_index == 5:
                    pass
                    # State 80876
                    if len(subjects) == 0:
                        pass
                        # 5: x*f
                        yield 5, subst1
                if pattern_index == 6:
                    pass
                    # State 88361
                    if len(subjects) == 0:
                        pass
                        # 6: d*x**n
                        yield 6, subst1
                if pattern_index == 7:
                    pass
                    # State 88931
                    if len(subjects) == 0:
                        pass
                        # 7: x**n*d
                        yield 7, subst1
            subjects.appendleft(tmp30)
        return
        yield


from matchpy.matching.many_to_one import CommutativeMatcher
from collections import deque
from .generated_part004603 import *
from matchpy.utils import VariableWithCount
from multiset import Multiset