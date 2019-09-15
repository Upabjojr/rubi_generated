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


class CommutativeMatcher3222(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({}), [
      (VariableWithCount('i2.2.1.0', 1, 1, None), Mul),
      (VariableWithCount('i2.2.1.0_3', 1, 1, S(1)), Mul)
]),
    1: (1, Multiset({}), [
      (VariableWithCount('i2.2.1.0_2', 1, 1, S(1)), Mul),
      (VariableWithCount('i2.2.1.1', 1, 1, None), Mul)
]),
    2: (2, Multiset({}), [
      (VariableWithCount('i2.2.0', 1, 1, None), Mul),
      (VariableWithCount('i2.2.1.0_2', 1, 1, S(1)), Mul)
]),
    3: (3, Multiset({0: 1}), [
      (VariableWithCount('i2.2.1.0_2', 1, 1, S(1)), Mul)
]),
    4: (4, Multiset({}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul),
      (VariableWithCount('i2.2.3.1.1.0', 1, 1, None), Mul)
]),
    5: (5, Multiset({1: 1}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul)
]),
    6: (6, Multiset({2: 1}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul)
]),
    7: (7, Multiset({3: 1}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul)
]),
    8: (8, Multiset({4: 1}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul)
]),
    9: (9, Multiset({}), [
      (VariableWithCount('i2.2.1.0_2', 1, 1, S(1)), Mul),
      (VariableWithCount('i2.2.1.2.0', 1, 1, None), Mul)
]),
    10: (10, Multiset({}), [
      (VariableWithCount('i2.2.1.0_4', 1, 1, None), Mul),
      (VariableWithCount('i2.2.1.0_5', 1, 1, S(1)), Mul)
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
        if CommutativeMatcher3222._instance is None:
            CommutativeMatcher3222._instance = CommutativeMatcher3222()
        return CommutativeMatcher3222._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 3221
        if len(subjects) >= 1 and isinstance(subjects[0], Pow):
            tmp1 = subjects.popleft()
            subjects2 = deque(tmp1._args)
            # State 7800
            if len(subjects2) >= 1:
                tmp3 = subjects2.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.1.1_2', tmp3)
                except ValueError:
                    pass
                else:
                    pass
                    # State 7801
                    if len(subjects2) >= 1:
                        tmp5 = subjects2.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.1.2', tmp5)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 7802
                            if len(subjects2) == 0:
                                pass
                                # State 7803
                                if len(subjects) == 0:
                                    pass
                                    # 0: w**n
                                    yield 0, subst2
                        subjects2.appendleft(tmp5)
                subjects2.appendleft(tmp3)
            subjects.appendleft(tmp1)
        if len(subjects) >= 1 and isinstance(subjects[0], sin):
            tmp7 = subjects.popleft()
            subjects8 = deque(tmp7._args)
            # State 63029
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 63030
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.2.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 63031
                    if len(subjects8) >= 1:
                        tmp11 = subjects8.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.2.1.0', tmp11)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 63032
                            if len(subjects8) == 0:
                                pass
                                # State 63033
                                if len(subjects) == 0:
                                    pass
                                    # 1: sin(e + x*f)
                                    yield 1, subst3
                        subjects8.appendleft(tmp11)
                if len(subjects8) >= 1 and isinstance(subjects8[0], Mul):
                    tmp13 = subjects8.popleft()
                    associative1 = tmp13
                    associative_type1 = type(tmp13)
                    subjects14 = deque(tmp13._args)
                    matcher = CommutativeMatcher63035.get()
                    tmp15 = subjects14
                    subjects14 = []
                    for s in tmp15:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp15, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 63036
                            if len(subjects8) == 0:
                                pass
                                # State 63037
                                if len(subjects) == 0:
                                    pass
                                    # 1: sin(e + x*f)
                                    yield 1, subst2
                    subjects8.appendleft(tmp13)
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.3.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 63268
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.3.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 63269
                    if len(subjects8) >= 1:
                        tmp18 = subjects8.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.3.1.0', tmp18)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 63270
                            if len(subjects8) == 0:
                                pass
                                # State 63271
                                if len(subjects) == 0:
                                    pass
                                    # 3: sin(e + x*f)
                                    yield 3, subst3
                        subjects8.appendleft(tmp18)
                if len(subjects8) >= 1 and isinstance(subjects8[0], Mul):
                    tmp20 = subjects8.popleft()
                    associative1 = tmp20
                    associative_type1 = type(tmp20)
                    subjects21 = deque(tmp20._args)
                    matcher = CommutativeMatcher63273.get()
                    tmp22 = subjects21
                    subjects21 = []
                    for s in tmp22:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp22, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 63274
                            if len(subjects8) == 0:
                                pass
                                # State 63275
                                if len(subjects) == 0:
                                    pass
                                    # 3: sin(e + x*f)
                                    yield 3, subst2
                    subjects8.appendleft(tmp20)
            if len(subjects8) >= 1 and isinstance(subjects8[0], Add):
                tmp23 = subjects8.popleft()
                associative1 = tmp23
                associative_type1 = type(tmp23)
                subjects24 = deque(tmp23._args)
                matcher = CommutativeMatcher63039.get()
                tmp25 = subjects24
                subjects24 = []
                for s in tmp25:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp25, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 63045
                        if len(subjects8) == 0:
                            pass
                            # State 63046
                            if len(subjects) == 0:
                                pass
                                # 1: sin(e + x*f)
                                yield 1, subst1
                    if pattern_index == 1:
                        pass
                        # State 63279
                        if len(subjects8) == 0:
                            pass
                            # State 63280
                            if len(subjects) == 0:
                                pass
                                # 3: sin(e + x*f)
                                yield 3, subst1
                subjects8.appendleft(tmp23)
            subjects.appendleft(tmp7)
        if len(subjects) >= 1 and isinstance(subjects[0], cos):
            tmp26 = subjects.popleft()
            subjects27 = deque(tmp26._args)
            # State 63118
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 63119
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.2.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 63120
                    if len(subjects27) >= 1:
                        tmp30 = subjects27.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.2.1.0', tmp30)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 63121
                            if len(subjects27) == 0:
                                pass
                                # State 63122
                                if len(subjects) == 0:
                                    pass
                                    # 2: cos(e + x*f)
                                    yield 2, subst3
                        subjects27.appendleft(tmp30)
                if len(subjects27) >= 1 and isinstance(subjects27[0], Mul):
                    tmp32 = subjects27.popleft()
                    associative1 = tmp32
                    associative_type1 = type(tmp32)
                    subjects33 = deque(tmp32._args)
                    matcher = CommutativeMatcher63124.get()
                    tmp34 = subjects33
                    subjects33 = []
                    for s in tmp34:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp34, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 63125
                            if len(subjects27) == 0:
                                pass
                                # State 63126
                                if len(subjects) == 0:
                                    pass
                                    # 2: cos(e + x*f)
                                    yield 2, subst2
                    subjects27.appendleft(tmp32)
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.3.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 63444
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.3.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 63445
                    if len(subjects27) >= 1:
                        tmp37 = subjects27.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.3.1.0', tmp37)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 63446
                            if len(subjects27) == 0:
                                pass
                                # State 63447
                                if len(subjects) == 0:
                                    pass
                                    # 4: cos(e + x*f)
                                    yield 4, subst3
                        subjects27.appendleft(tmp37)
                if len(subjects27) >= 1 and isinstance(subjects27[0], Mul):
                    tmp39 = subjects27.popleft()
                    associative1 = tmp39
                    associative_type1 = type(tmp39)
                    subjects40 = deque(tmp39._args)
                    matcher = CommutativeMatcher63449.get()
                    tmp41 = subjects40
                    subjects40 = []
                    for s in tmp41:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp41, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 63450
                            if len(subjects27) == 0:
                                pass
                                # State 63451
                                if len(subjects) == 0:
                                    pass
                                    # 4: cos(e + x*f)
                                    yield 4, subst2
                    subjects27.appendleft(tmp39)
            if len(subjects27) >= 1 and isinstance(subjects27[0], Add):
                tmp42 = subjects27.popleft()
                associative1 = tmp42
                associative_type1 = type(tmp42)
                subjects43 = deque(tmp42._args)
                matcher = CommutativeMatcher63128.get()
                tmp44 = subjects43
                subjects43 = []
                for s in tmp44:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp44, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 63134
                        if len(subjects27) == 0:
                            pass
                            # State 63135
                            if len(subjects) == 0:
                                pass
                                # 2: cos(e + x*f)
                                yield 2, subst1
                    if pattern_index == 1:
                        pass
                        # State 63455
                        if len(subjects27) == 0:
                            pass
                            # State 63456
                            if len(subjects) == 0:
                                pass
                                # 4: cos(e + x*f)
                                yield 4, subst1
                subjects27.appendleft(tmp42)
            subjects.appendleft(tmp26)
        return
        yield


from .generated_part003721 import *
from .generated_part003726 import *
from .generated_part003725 import *
from .generated_part003722 import *
from matchpy.matching.many_to_one import CommutativeMatcher
from collections import deque
from .generated_part003727 import *
from .generated_part003723 import *
from matchpy.utils import VariableWithCount
from multiset import Multiset