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


class CommutativeMatcher58908(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({0: 1}), [
      (VariableWithCount('i2.2.2.0', 1, 1, S(0)), Add)
]),
    1: (1, Multiset({1: 1}), [
      (VariableWithCount('i2.2.3.0', 1, 1, S(0)), Add)
]),
    2: (2, Multiset({2: 1}), [
      (VariableWithCount('i2.2.1.2.0', 1, 1, S(0)), Add)
]),
    3: (3, Multiset({3: 1}), [
      (VariableWithCount('i2.2.2.2.0', 1, 1, S(0)), Add)
]),
    4: (4, Multiset({4: 1}), [
      (VariableWithCount('i2.2.1.3.0', 1, 1, S(0)), Add)
]),
    5: (5, Multiset({5: 1}), [
      (VariableWithCount('i2.2.1.2.0', 1, 1, S(0)), Add)
]),
    6: (6, Multiset({6: 1}), [
      (VariableWithCount('i2.2.1.2.0', 1, 1, S(0)), Add)
]),
    7: (7, Multiset({7: 1}), [
      (VariableWithCount('i2.2.1.2.0', 1, 1, S(0)), Add)
]),
    8: (8, Multiset({8: 1}), [
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
        if CommutativeMatcher58908._instance is None:
            CommutativeMatcher58908._instance = CommutativeMatcher58908()
        return CommutativeMatcher58908._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 58907
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.2.1.0_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 58909
            if len(subjects) >= 1:
                tmp2 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.2.1.0', tmp2)
                except ValueError:
                    pass
                else:
                    pass
                    # State 58910
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
            # State 59101
            if len(subjects) >= 1:
                tmp5 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.3.1.0', tmp5)
                except ValueError:
                    pass
                else:
                    pass
                    # State 59102
                    if len(subjects) == 0:
                        pass
                        # 1: x*f
                        yield 1, subst2
                subjects.appendleft(tmp5)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.2.1.0_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 60241
            if len(subjects) >= 1:
                tmp8 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.1.0', tmp8)
                except ValueError:
                    pass
                else:
                    pass
                    # State 60242
                    if len(subjects) == 0:
                        pass
                        # 2: x*d
                        yield 2, subst2
                subjects.appendleft(tmp8)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.2.2.1.0_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 61740
            if len(subjects) >= 1:
                tmp11 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.2.2.1.0', tmp11)
                except ValueError:
                    pass
                else:
                    pass
                    # State 61741
                    if len(subjects) == 0:
                        pass
                        # 3: x*f
                        yield 3, subst2
                subjects.appendleft(tmp11)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.3.1.0_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 62101
            if len(subjects) >= 1:
                tmp14 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.3.1.0', tmp14)
                except ValueError:
                    pass
                else:
                    pass
                    # State 62102
                    if len(subjects) == 0:
                        pass
                        # 4: x*f
                        yield 4, subst2
                subjects.appendleft(tmp14)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.2.1.0', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 74386
            if len(subjects) >= 1 and isinstance(subjects[0], Pow):
                tmp17 = subjects.popleft()
                subjects18 = deque(tmp17._args)
                # State 74387
                if len(subjects18) >= 1:
                    tmp19 = subjects18.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.0_1', tmp19)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 74388
                        if len(subjects18) >= 1:
                            tmp21 = subjects18.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.2.1.2', tmp21)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 74389
                                if len(subjects18) == 0:
                                    pass
                                    # State 74390
                                    if len(subjects) == 0:
                                        pass
                                        # 5: x**n*d
                                        yield 5, subst3
                            subjects18.appendleft(tmp21)
                    subjects18.appendleft(tmp19)
                if len(subjects18) >= 1:
                    tmp23 = subjects18.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.0', tmp23)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 74920
                        if len(subjects18) >= 1:
                            tmp25 = subjects18.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.2.1.2', tmp25)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 74921
                                if len(subjects18) == 0:
                                    pass
                                    # State 74922
                                    if len(subjects) == 0:
                                        pass
                                        # 6: x**n*d
                                        yield 6, subst3
                            subjects18.appendleft(tmp25)
                    subjects18.appendleft(tmp23)
                if len(subjects18) >= 1:
                    tmp27 = subjects18.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.2.1.1', tmp27)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 75307
                        if len(subjects18) >= 1:
                            tmp29 = subjects18.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.2.1.2', tmp29)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 75308
                                if len(subjects18) == 0:
                                    pass
                                    # State 75309
                                    if len(subjects) == 0:
                                        pass
                                        # 7: d*x**n
                                        yield 7, subst3
                            subjects18.appendleft(tmp29)
                    subjects18.appendleft(tmp27)
                subjects.appendleft(tmp17)
            if len(subjects) >= 1:
                tmp31 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.0', tmp31)
                except ValueError:
                    pass
                else:
                    pass
                    # State 107259
                    if len(subjects) == 0:
                        pass
                        # 8: x*d
                        yield 8, subst2
                subjects.appendleft(tmp31)
        if len(subjects) >= 1 and isinstance(subjects[0], Mul):
            tmp33 = subjects.popleft()
            associative1 = tmp33
            associative_type1 = type(tmp33)
            subjects34 = deque(tmp33._args)
            matcher = CommutativeMatcher58912.get()
            tmp35 = subjects34
            subjects34 = []
            for s in tmp35:
                matcher.add_subject(s)
            for pattern_index, subst1 in matcher.match(tmp35, subst0):
                pass
                if pattern_index == 0:
                    pass
                    # State 58913
                    if len(subjects) == 0:
                        pass
                        # 0: x*f
                        yield 0, subst1
                if pattern_index == 1:
                    pass
                    # State 59103
                    if len(subjects) == 0:
                        pass
                        # 1: x*f
                        yield 1, subst1
                if pattern_index == 2:
                    pass
                    # State 60243
                    if len(subjects) == 0:
                        pass
                        # 2: x*d
                        yield 2, subst1
                if pattern_index == 3:
                    pass
                    # State 61742
                    if len(subjects) == 0:
                        pass
                        # 3: x*f
                        yield 3, subst1
                if pattern_index == 4:
                    pass
                    # State 62103
                    if len(subjects) == 0:
                        pass
                        # 4: x*f
                        yield 4, subst1
                if pattern_index == 5:
                    pass
                    # State 74395
                    if len(subjects) == 0:
                        pass
                        # 5: x**n*d
                        yield 5, subst1
                if pattern_index == 6:
                    pass
                    # State 74926
                    if len(subjects) == 0:
                        pass
                        # 6: x**n*d
                        yield 6, subst1
                if pattern_index == 7:
                    pass
                    # State 75313
                    if len(subjects) == 0:
                        pass
                        # 7: d*x**n
                        yield 7, subst1
                if pattern_index == 8:
                    pass
                    # State 107260
                    if len(subjects) == 0:
                        pass
                        # 8: x*d
                        yield 8, subst1
            subjects.appendleft(tmp33)
        return
        yield


from .generated_part003665 import *
from matchpy.matching.many_to_one import CommutativeMatcher
from collections import deque
from matchpy.utils import VariableWithCount
from multiset import Multiset