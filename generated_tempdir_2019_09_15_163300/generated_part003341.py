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


class CommutativeMatcher109230(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({0: 1}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul)
]),
    1: (1, Multiset({1: 1}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul)
]),
    2: (2, Multiset({2: 1}), [
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
        if CommutativeMatcher109230._instance is None:
            CommutativeMatcher109230._instance = CommutativeMatcher109230()
        return CommutativeMatcher109230._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 109229
        if len(subjects) >= 1 and isinstance(subjects[0], asin):
            tmp1 = subjects.popleft()
            subjects2 = deque(tmp1._args)
            # State 109231
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.0', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 109232
                if len(subjects2) >= 1:
                    tmp4 = subjects2.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.0', tmp4)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 109233
                        if len(subjects2) == 0:
                            pass
                            # State 109234
                            if len(subjects) == 0:
                                pass
                                # 0: asin(x*c)
                                yield 0, subst2
                    subjects2.appendleft(tmp4)
            if len(subjects2) >= 1 and isinstance(subjects2[0], Mul):
                tmp6 = subjects2.popleft()
                associative1 = tmp6
                associative_type1 = type(tmp6)
                subjects7 = deque(tmp6._args)
                matcher = CommutativeMatcher109236.get()
                tmp8 = subjects7
                subjects7 = []
                for s in tmp8:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp8, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 109237
                        if len(subjects2) == 0:
                            pass
                            # State 109238
                            if len(subjects) == 0:
                                pass
                                # 0: asin(x*c)
                                yield 0, subst1
                subjects2.appendleft(tmp6)
            subjects.appendleft(tmp1)
        if len(subjects) >= 1 and isinstance(subjects[0], acos):
            tmp9 = subjects.popleft()
            subjects10 = deque(tmp9._args)
            # State 109265
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.0', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 109266
                if len(subjects10) >= 1:
                    tmp12 = subjects10.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.0', tmp12)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 109267
                        if len(subjects10) == 0:
                            pass
                            # State 109268
                            if len(subjects) == 0:
                                pass
                                # 1: acos(x*c)
                                yield 1, subst2
                    subjects10.appendleft(tmp12)
            if len(subjects10) >= 1 and isinstance(subjects10[0], Mul):
                tmp14 = subjects10.popleft()
                associative1 = tmp14
                associative_type1 = type(tmp14)
                subjects15 = deque(tmp14._args)
                matcher = CommutativeMatcher109270.get()
                tmp16 = subjects15
                subjects15 = []
                for s in tmp16:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp16, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 109271
                        if len(subjects10) == 0:
                            pass
                            # State 109272
                            if len(subjects) == 0:
                                pass
                                # 1: acos(x*c)
                                yield 1, subst1
                subjects10.appendleft(tmp14)
            subjects.appendleft(tmp9)
        if len(subjects) >= 1 and isinstance(subjects[0], asinh):
            tmp17 = subjects.popleft()
            subjects18 = deque(tmp17._args)
            # State 139020
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.0', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 139021
                if len(subjects18) >= 1:
                    tmp20 = subjects18.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.0', tmp20)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 139022
                        if len(subjects18) == 0:
                            pass
                            # State 139023
                            if len(subjects) == 0:
                                pass
                                # 2: asinh(x*c)
                                yield 2, subst2
                    subjects18.appendleft(tmp20)
            if len(subjects18) >= 1 and isinstance(subjects18[0], Mul):
                tmp22 = subjects18.popleft()
                associative1 = tmp22
                associative_type1 = type(tmp22)
                subjects23 = deque(tmp22._args)
                matcher = CommutativeMatcher139025.get()
                tmp24 = subjects23
                subjects23 = []
                for s in tmp24:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp24, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 139026
                        if len(subjects18) == 0:
                            pass
                            # State 139027
                            if len(subjects) == 0:
                                pass
                                # 2: asinh(x*c)
                                yield 2, subst1
                subjects18.appendleft(tmp22)
            subjects.appendleft(tmp17)
        return
        yield


from .generated_part003343 import *
from .generated_part003344 import *
from matchpy.matching.many_to_one import CommutativeMatcher
from .generated_part003342 import *
from collections import deque
from matchpy.utils import VariableWithCount
from multiset import Multiset