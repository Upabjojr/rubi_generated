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


class CommutativeMatcher63172(CommutativeMatcher):
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
      (VariableWithCount('i2.2.1.2.0', 1, 1, S(0)), Add)
]),
    4: (4, Multiset({4: 1}), [
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
        if CommutativeMatcher63172._instance is None:
            CommutativeMatcher63172._instance = CommutativeMatcher63172()
        return CommutativeMatcher63172._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 63171
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.2.1.0_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 63173
            if len(subjects) >= 1:
                tmp2 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.2.1.0', tmp2)
                except ValueError:
                    pass
                else:
                    pass
                    # State 63174
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
            # State 63513
            if len(subjects) >= 1:
                tmp5 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.3.1.0', tmp5)
                except ValueError:
                    pass
                else:
                    pass
                    # State 63514
                    if len(subjects) == 0:
                        pass
                        # 1: x*f
                        yield 1, subst2
                subjects.appendleft(tmp5)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.2.1.0', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 74453
            if len(subjects) >= 1 and isinstance(subjects[0], Pow):
                tmp8 = subjects.popleft()
                subjects9 = deque(tmp8._args)
                # State 74454
                if len(subjects9) >= 1:
                    tmp10 = subjects9.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.0_1', tmp10)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 74455
                        if len(subjects9) >= 1:
                            tmp12 = subjects9.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.2.1.2', tmp12)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 74456
                                if len(subjects9) == 0:
                                    pass
                                    # State 74457
                                    if len(subjects) == 0:
                                        pass
                                        # 2: x**n*d
                                        yield 2, subst3
                            subjects9.appendleft(tmp12)
                    subjects9.appendleft(tmp10)
                if len(subjects9) >= 1:
                    tmp14 = subjects9.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.0', tmp14)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 74964
                        if len(subjects9) >= 1:
                            tmp16 = subjects9.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.2.1.2', tmp16)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 74965
                                if len(subjects9) == 0:
                                    pass
                                    # State 74966
                                    if len(subjects) == 0:
                                        pass
                                        # 3: x**n*d
                                        yield 3, subst3
                            subjects9.appendleft(tmp16)
                    subjects9.appendleft(tmp14)
                if len(subjects9) >= 1:
                    tmp18 = subjects9.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.2.1.1', tmp18)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 75351
                        if len(subjects9) >= 1:
                            tmp20 = subjects9.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.2.1.2', tmp20)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 75352
                                if len(subjects9) == 0:
                                    pass
                                    # State 75353
                                    if len(subjects) == 0:
                                        pass
                                        # 4: d*x**n
                                        yield 4, subst3
                            subjects9.appendleft(tmp20)
                    subjects9.appendleft(tmp18)
                subjects.appendleft(tmp8)
        if len(subjects) >= 1 and isinstance(subjects[0], Mul):
            tmp22 = subjects.popleft()
            associative1 = tmp22
            associative_type1 = type(tmp22)
            subjects23 = deque(tmp22._args)
            matcher = CommutativeMatcher63176.get()
            tmp24 = subjects23
            subjects23 = []
            for s in tmp24:
                matcher.add_subject(s)
            for pattern_index, subst1 in matcher.match(tmp24, subst0):
                pass
                if pattern_index == 0:
                    pass
                    # State 63177
                    if len(subjects) == 0:
                        pass
                        # 0: x*f
                        yield 0, subst1
                if pattern_index == 1:
                    pass
                    # State 63515
                    if len(subjects) == 0:
                        pass
                        # 1: x*f
                        yield 1, subst1
                if pattern_index == 2:
                    pass
                    # State 74462
                    if len(subjects) == 0:
                        pass
                        # 2: x**n*d
                        yield 2, subst1
                if pattern_index == 3:
                    pass
                    # State 74970
                    if len(subjects) == 0:
                        pass
                        # 3: x**n*d
                        yield 3, subst1
                if pattern_index == 4:
                    pass
                    # State 75357
                    if len(subjects) == 0:
                        pass
                        # 4: d*x**n
                        yield 4, subst1
            subjects.appendleft(tmp22)
        return
        yield


from matchpy.matching.many_to_one import CommutativeMatcher
from collections import deque
from matchpy.utils import VariableWithCount
from multiset import Multiset
from .generated_part006392 import *