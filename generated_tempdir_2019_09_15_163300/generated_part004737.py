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


class CommutativeMatcher58351(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({0: 1}), [
      (VariableWithCount('i2.2.1.2.0', 1, 1, S(0)), Add)
]),
    1: (1, Multiset({1: 1}), [
      (VariableWithCount('i2.2.2.0', 1, 1, S(0)), Add)
]),
    2: (2, Multiset({2: 1}), [
      (VariableWithCount('i2.2.3.0', 1, 1, S(0)), Add)
]),
    3: (3, Multiset({3: 1}), [
      (VariableWithCount('i2.2.2.2.0', 1, 1, S(0)), Add)
]),
    4: (4, Multiset({4: 1}), [
      (VariableWithCount('i2.2.1.2.0', 1, 1, S(0)), Add)
]),
    5: (5, Multiset({5: 1}), [
      (VariableWithCount('i2.2.1.2.0', 1, 1, S(0)), Add)
]),
    6: (6, Multiset({6: 1}), [
      (VariableWithCount('i2.2.1.2.0', 1, 1, S(0)), Add)
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
        if CommutativeMatcher58351._instance is None:
            CommutativeMatcher58351._instance = CommutativeMatcher58351()
        return CommutativeMatcher58351._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 58350
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.2.1.0_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 58352
            if len(subjects) >= 1:
                tmp2 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.1.0', tmp2)
                except ValueError:
                    pass
                else:
                    pass
                    # State 58353
                    if len(subjects) == 0:
                        pass
                        # 0: x*d
                        yield 0, subst2
                subjects.appendleft(tmp2)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.2.1.0_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 58633
            if len(subjects) >= 1:
                tmp5 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.2.1.0', tmp5)
                except ValueError:
                    pass
                else:
                    pass
                    # State 58634
                    if len(subjects) == 0:
                        pass
                        # 1: x*f
                        yield 1, subst2
                subjects.appendleft(tmp5)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.3.1.0_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 59055
            if len(subjects) >= 1:
                tmp8 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.3.1.0', tmp8)
                except ValueError:
                    pass
                else:
                    pass
                    # State 59056
                    if len(subjects) == 0:
                        pass
                        # 2: x*f
                        yield 2, subst2
                subjects.appendleft(tmp8)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.2.2.1.0_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 61561
            if len(subjects) >= 1:
                tmp11 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.2.2.1.0', tmp11)
                except ValueError:
                    pass
                else:
                    pass
                    # State 61562
                    if len(subjects) == 0:
                        pass
                        # 3: x*f
                        yield 3, subst2
                subjects.appendleft(tmp11)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.2.1.0', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 73800
            if len(subjects) >= 1 and isinstance(subjects[0], Pow):
                tmp14 = subjects.popleft()
                subjects15 = deque(tmp14._args)
                # State 73801
                if len(subjects15) >= 1:
                    tmp16 = subjects15.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.2.1.1', tmp16)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 73802
                        if len(subjects15) >= 1:
                            tmp18 = subjects15.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.2.1.2', tmp18)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 73803
                                if len(subjects15) == 0:
                                    pass
                                    # State 73804
                                    if len(subjects) == 0:
                                        pass
                                        # 4: d*x**n
                                        yield 4, subst3
                            subjects15.appendleft(tmp18)
                    subjects15.appendleft(tmp16)
                if len(subjects15) >= 1:
                    tmp20 = subjects15.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.0_1', tmp20)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 74248
                        if len(subjects15) >= 1:
                            tmp22 = subjects15.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.2.1.2', tmp22)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 74249
                                if len(subjects15) == 0:
                                    pass
                                    # State 74250
                                    if len(subjects) == 0:
                                        pass
                                        # 5: x**n*d
                                        yield 5, subst3
                            subjects15.appendleft(tmp22)
                    subjects15.appendleft(tmp20)
                if len(subjects15) >= 1:
                    tmp24 = subjects15.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.0', tmp24)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 74822
                        if len(subjects15) >= 1:
                            tmp26 = subjects15.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.2.1.2', tmp26)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 74823
                                if len(subjects15) == 0:
                                    pass
                                    # State 74824
                                    if len(subjects) == 0:
                                        pass
                                        # 6: x**n*d
                                        yield 6, subst3
                            subjects15.appendleft(tmp26)
                    subjects15.appendleft(tmp24)
                subjects.appendleft(tmp14)
        if len(subjects) >= 1 and isinstance(subjects[0], Mul):
            tmp28 = subjects.popleft()
            associative1 = tmp28
            associative_type1 = type(tmp28)
            subjects29 = deque(tmp28._args)
            matcher = CommutativeMatcher58355.get()
            tmp30 = subjects29
            subjects29 = []
            for s in tmp30:
                matcher.add_subject(s)
            for pattern_index, subst1 in matcher.match(tmp30, subst0):
                pass
                if pattern_index == 0:
                    pass
                    # State 58356
                    if len(subjects) == 0:
                        pass
                        # 0: x*d
                        yield 0, subst1
                if pattern_index == 1:
                    pass
                    # State 58635
                    if len(subjects) == 0:
                        pass
                        # 1: x*f
                        yield 1, subst1
                if pattern_index == 2:
                    pass
                    # State 59057
                    if len(subjects) == 0:
                        pass
                        # 2: x*f
                        yield 2, subst1
                if pattern_index == 3:
                    pass
                    # State 61563
                    if len(subjects) == 0:
                        pass
                        # 3: x*f
                        yield 3, subst1
                if pattern_index == 4:
                    pass
                    # State 73809
                    if len(subjects) == 0:
                        pass
                        # 4: d*x**n
                        yield 4, subst1
                if pattern_index == 5:
                    pass
                    # State 74254
                    if len(subjects) == 0:
                        pass
                        # 5: x**n*d
                        yield 5, subst1
                if pattern_index == 6:
                    pass
                    # State 74828
                    if len(subjects) == 0:
                        pass
                        # 6: x**n*d
                        yield 6, subst1
            subjects.appendleft(tmp28)
        return
        yield


from matchpy.matching.many_to_one import CommutativeMatcher
from collections import deque
from matchpy.utils import VariableWithCount
from multiset import Multiset
from .generated_part004738 import *