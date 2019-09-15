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


class CommutativeMatcher58482(CommutativeMatcher):
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
      (VariableWithCount('i2.4.0', 1, 1, S(0)), Add)
]),
    4: (4, Multiset({4: 1}), [
      (VariableWithCount('i2.2.2.2.0', 1, 1, S(0)), Add)
]),
    5: (5, Multiset({5: 1}), [
      (VariableWithCount('i2.2.1.3.0', 1, 1, S(0)), Add)
]),
    6: (6, Multiset({6: 1}), [
      (VariableWithCount('i2.2.1.2.0', 1, 1, S(0)), Add)
]),
    7: (7, Multiset({7: 1}), [
      (VariableWithCount('i2.2.1.2.0', 1, 1, S(0)), Add)
]),
    8: (8, Multiset({8: 1}), [
      (VariableWithCount('i2.2.1.2.0', 1, 1, S(0)), Add)
]),
    9: (9, Multiset({9: 1}), [
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
        if CommutativeMatcher58482._instance is None:
            CommutativeMatcher58482._instance = CommutativeMatcher58482()
        return CommutativeMatcher58482._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 58481
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.2.1.0_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 58483
            if len(subjects) >= 1:
                tmp2 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.1.0', tmp2)
                except ValueError:
                    pass
                else:
                    pass
                    # State 58484
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
            # State 58679
            if len(subjects) >= 1:
                tmp5 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.2.1.0', tmp5)
                except ValueError:
                    pass
                else:
                    pass
                    # State 58680
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
            # State 59129
            if len(subjects) >= 1:
                tmp8 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.3.1.0', tmp8)
                except ValueError:
                    pass
                else:
                    pass
                    # State 59130
                    if len(subjects) == 0:
                        pass
                        # 2: x*f
                        yield 2, subst2
                subjects.appendleft(tmp8)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.4.1.0_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 59487
            if len(subjects) >= 1:
                tmp11 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.4.1.0', tmp11)
                except ValueError:
                    pass
                else:
                    pass
                    # State 59488
                    if len(subjects) == 0:
                        pass
                        # 3: x*f
                        yield 3, subst2
                subjects.appendleft(tmp11)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.2.2.1.0_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 61803
            if len(subjects) >= 1:
                tmp14 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.2.2.1.0', tmp14)
                except ValueError:
                    pass
                else:
                    pass
                    # State 61804
                    if len(subjects) == 0:
                        pass
                        # 4: x*f
                        yield 4, subst2
                subjects.appendleft(tmp14)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.3.1.0_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 62129
            if len(subjects) >= 1:
                tmp17 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.3.1.0', tmp17)
                except ValueError:
                    pass
                else:
                    pass
                    # State 62130
                    if len(subjects) == 0:
                        pass
                        # 5: x*f
                        yield 5, subst2
                subjects.appendleft(tmp17)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.2.1.0', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 74036
            if len(subjects) >= 1 and isinstance(subjects[0], Pow):
                tmp20 = subjects.popleft()
                subjects21 = deque(tmp20._args)
                # State 74037
                if len(subjects21) >= 1:
                    tmp22 = subjects21.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.2.1.1', tmp22)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 74038
                        if len(subjects21) >= 1:
                            tmp24 = subjects21.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.2.1.2', tmp24)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 74039
                                if len(subjects21) == 0:
                                    pass
                                    # State 74040
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
                        # State 74495
                        if len(subjects21) >= 1:
                            tmp28 = subjects21.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.2.1.2', tmp28)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 74496
                                if len(subjects21) == 0:
                                    pass
                                    # State 74497
                                    if len(subjects) == 0:
                                        pass
                                        # 7: x**n*d
                                        yield 7, subst3
                            subjects21.appendleft(tmp28)
                    subjects21.appendleft(tmp26)
                if len(subjects21) >= 1:
                    tmp30 = subjects21.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.0', tmp30)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 75003
                        if len(subjects21) >= 1:
                            tmp32 = subjects21.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.2.1.2', tmp32)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 75004
                                if len(subjects21) == 0:
                                    pass
                                    # State 75005
                                    if len(subjects) == 0:
                                        pass
                                        # 8: x**n*d
                                        yield 8, subst3
                            subjects21.appendleft(tmp32)
                    subjects21.appendleft(tmp30)
                subjects.appendleft(tmp20)
            if len(subjects) >= 1:
                tmp34 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.0', tmp34)
                except ValueError:
                    pass
                else:
                    pass
                    # State 107269
                    if len(subjects) == 0:
                        pass
                        # 9: x*d
                        yield 9, subst2
                subjects.appendleft(tmp34)
        if len(subjects) >= 1 and isinstance(subjects[0], Mul):
            tmp36 = subjects.popleft()
            associative1 = tmp36
            associative_type1 = type(tmp36)
            subjects37 = deque(tmp36._args)
            matcher = CommutativeMatcher58486.get()
            tmp38 = subjects37
            subjects37 = []
            for s in tmp38:
                matcher.add_subject(s)
            for pattern_index, subst1 in matcher.match(tmp38, subst0):
                pass
                if pattern_index == 0:
                    pass
                    # State 58487
                    if len(subjects) == 0:
                        pass
                        # 0: x*d
                        yield 0, subst1
                if pattern_index == 1:
                    pass
                    # State 58681
                    if len(subjects) == 0:
                        pass
                        # 1: x*f
                        yield 1, subst1
                if pattern_index == 2:
                    pass
                    # State 59131
                    if len(subjects) == 0:
                        pass
                        # 2: x*f
                        yield 2, subst1
                if pattern_index == 3:
                    pass
                    # State 59489
                    if len(subjects) == 0:
                        pass
                        # 3: x*f
                        yield 3, subst1
                if pattern_index == 4:
                    pass
                    # State 61805
                    if len(subjects) == 0:
                        pass
                        # 4: x*f
                        yield 4, subst1
                if pattern_index == 5:
                    pass
                    # State 62131
                    if len(subjects) == 0:
                        pass
                        # 5: x*f
                        yield 5, subst1
                if pattern_index == 6:
                    pass
                    # State 74045
                    if len(subjects) == 0:
                        pass
                        # 6: d*x**n
                        yield 6, subst1
                if pattern_index == 7:
                    pass
                    # State 74501
                    if len(subjects) == 0:
                        pass
                        # 7: x**n*d
                        yield 7, subst1
                if pattern_index == 8:
                    pass
                    # State 75009
                    if len(subjects) == 0:
                        pass
                        # 8: x**n*d
                        yield 8, subst1
                if pattern_index == 9:
                    pass
                    # State 107270
                    if len(subjects) == 0:
                        pass
                        # 9: x*d
                        yield 9, subst1
            subjects.appendleft(tmp36)
        return
        yield


from matchpy.matching.many_to_one import CommutativeMatcher
from collections import deque
from .generated_part005424 import *
from matchpy.utils import VariableWithCount
from multiset import Multiset