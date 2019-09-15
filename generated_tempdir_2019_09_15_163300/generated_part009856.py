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


class CommutativeMatcher3827(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({0: 1}), [
      (VariableWithCount('i3.2.0', 1, 1, S(0)), Add)
]),
    1: (1, Multiset({1: 1}), [
      (VariableWithCount('i3.2.0_1', 1, 1, S(0)), Add)
]),
    2: (2, Multiset({2: 1}), [
      (VariableWithCount('i3.2.0_2', 1, 1, S(0)), Add)
]),
    3: (3, Multiset({3: 1}), [
      (VariableWithCount('i3.2.0_3', 1, 1, S(0)), Add)
]),
    4: (4, Multiset({4: 1}), [
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
        if CommutativeMatcher3827._instance is None:
            CommutativeMatcher3827._instance = CommutativeMatcher3827()
        return CommutativeMatcher3827._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 3826
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i3.2.1.0_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 3828
            if len(subjects) >= 1:
                tmp2 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i3.2.1.0', tmp2)
                except ValueError:
                    pass
                else:
                    pass
                    # State 3829
                    if len(subjects) == 0:
                        pass
                        # 0: x*b
                        yield 0, subst2
                subjects.appendleft(tmp2)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i3.2.1.0_2', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 3846
            if len(subjects) >= 1:
                tmp5 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i3.2.1.0', tmp5)
                except ValueError:
                    pass
                else:
                    pass
                    # State 3847
                    if len(subjects) == 0:
                        pass
                        # 1: x*d
                        yield 1, subst2
                subjects.appendleft(tmp5)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i3.2.1.0_3', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 3862
            if len(subjects) >= 1:
                tmp8 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i3.2.1.0', tmp8)
                except ValueError:
                    pass
                else:
                    pass
                    # State 3863
                    if len(subjects) == 0:
                        pass
                        # 2: x*f
                        yield 2, subst2
                subjects.appendleft(tmp8)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i3.2.1.0_4', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 3878
            if len(subjects) >= 1:
                tmp11 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i3.2.1.0', tmp11)
                except ValueError:
                    pass
                else:
                    pass
                    # State 3879
                    if len(subjects) == 0:
                        pass
                        # 3: x*h
                        yield 3, subst2
                subjects.appendleft(tmp11)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i3.2.1.0', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 10517
            subst2 = Substitution(subst1)
            try:
                subst2.try_add_variable('i3.2.1.2', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 10518
                if len(subjects) >= 1:
                    tmp15 = subjects.popleft()
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i3.2.1.1', tmp15)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 10519
                        if len(subjects) == 0:
                            pass
                            # 4: d*x**n
                            yield 4, subst3
                    subjects.appendleft(tmp15)
            if len(subjects) >= 1 and isinstance(subjects[0], Pow):
                tmp17 = subjects.popleft()
                subjects18 = deque(tmp17._args)
                # State 10520
                if len(subjects18) >= 1:
                    tmp19 = subjects18.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i3.2.1.1', tmp19)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 10521
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i3.2.1.2', 1)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 10522
                            if len(subjects18) == 0:
                                pass
                                # State 10523
                                if len(subjects) == 0:
                                    pass
                                    # 4: d*x**n
                                    yield 4, subst3
                        if len(subjects18) >= 1:
                            tmp22 = subjects18.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i3.2.1.2', tmp22)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 10522
                                if len(subjects18) == 0:
                                    pass
                                    # State 10523
                                    if len(subjects) == 0:
                                        pass
                                        # 4: d*x**n
                                        yield 4, subst3
                            subjects18.appendleft(tmp22)
                    subjects18.appendleft(tmp19)
                subjects.appendleft(tmp17)
        if len(subjects) >= 1 and isinstance(subjects[0], Mul):
            tmp24 = subjects.popleft()
            associative1 = tmp24
            associative_type1 = type(tmp24)
            subjects25 = deque(tmp24._args)
            matcher = CommutativeMatcher3831.get()
            tmp26 = subjects25
            subjects25 = []
            for s in tmp26:
                matcher.add_subject(s)
            for pattern_index, subst1 in matcher.match(tmp26, subst0):
                pass
                if pattern_index == 0:
                    pass
                    # State 3832
                    if len(subjects) == 0:
                        pass
                        # 0: x*b
                        yield 0, subst1
                if pattern_index == 1:
                    pass
                    # State 3848
                    if len(subjects) == 0:
                        pass
                        # 1: x*d
                        yield 1, subst1
                if pattern_index == 2:
                    pass
                    # State 3864
                    if len(subjects) == 0:
                        pass
                        # 2: x*f
                        yield 2, subst1
                if pattern_index == 3:
                    pass
                    # State 3880
                    if len(subjects) == 0:
                        pass
                        # 3: x*h
                        yield 3, subst1
                if pattern_index == 4:
                    pass
                    # State 10530
                    if len(subjects) == 0:
                        pass
                        # 4: d*x**n
                        yield 4, subst1
            subjects.appendleft(tmp24)
        return
        yield


from matchpy.matching.many_to_one import CommutativeMatcher
from collections import deque
from .generated_part009857 import *
from matchpy.utils import VariableWithCount
from multiset import Multiset