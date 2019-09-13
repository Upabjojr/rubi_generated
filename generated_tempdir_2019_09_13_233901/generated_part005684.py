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

class CommutativeMatcher151235(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({0: 1, 1: 1}), [
      (VariableWithCount('i2.2.1.3.0', 1, 1, S(1)), Mul)
]),
    1: (1, Multiset({2: 1, 3: 1}), [
      (VariableWithCount('i2.2.1.3.0', 1, 1, S(1)), Mul)
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
        if CommutativeMatcher151235._instance is None:
            CommutativeMatcher151235._instance = CommutativeMatcher151235()
        return CommutativeMatcher151235._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 151234
        if len(subjects) >= 1 and isinstance(subjects[0], Pow):
            tmp1 = subjects.popleft()
            subjects2 = deque(tmp1._args)
            # State 151236
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.3.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 151237
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.3.2.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 151238
                    if len(subjects2) >= 1:
                        tmp5 = subjects2.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.3.2.1.0', tmp5)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 151239
                            if len(subjects2) >= 1 and subjects2[0] == 1/2:
                                tmp7 = subjects2.popleft()
                                # State 151240
                                if len(subjects2) == 0:
                                    pass
                                    # State 151241
                                    if len(subjects) == 0:
                                        pass
                                        # 0: sqrt(d + x*e)
                                subjects2.appendleft(tmp7)
                        subjects2.appendleft(tmp5)
                if len(subjects2) >= 1 and isinstance(subjects2[0], Mul):
                    tmp8 = subjects2.popleft()
                    associative1 = tmp8
                    associative_type1 = type(tmp8)
                    subjects9 = deque(tmp8._args)
                    matcher = CommutativeMatcher151243.get()
                    tmp10 = subjects9
                    subjects9 = []
                    for s in tmp10:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp10, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 151244
                            if len(subjects2) >= 1 and subjects2[0] == 1/2:
                                tmp11 = subjects2.popleft()
                                # State 151245
                                if len(subjects2) == 0:
                                    pass
                                    # State 151246
                                    if len(subjects) == 0:
                                        pass
                                        # 0: sqrt(d + x*e)
                                subjects2.appendleft(tmp11)
                    subjects2.appendleft(tmp8)
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.3.2.0_1', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 151257
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.3.2.1.0_2', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 151258
                    if len(subjects2) >= 1:
                        tmp14 = subjects2.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.3.2.1.0', tmp14)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 151259
                            if len(subjects2) >= 1 and subjects2[0] == -1/2:
                                tmp16 = subjects2.popleft()
                                # State 151260
                                if len(subjects2) == 0:
                                    pass
                                    # State 151261
                                    if len(subjects) == 0:
                                        pass
                                        # 1: 1/sqrt(f + x*g)
                                subjects2.appendleft(tmp16)
                        subjects2.appendleft(tmp14)
                if len(subjects2) >= 1 and isinstance(subjects2[0], Mul):
                    tmp17 = subjects2.popleft()
                    associative1 = tmp17
                    associative_type1 = type(tmp17)
                    subjects18 = deque(tmp17._args)
                    matcher = CommutativeMatcher151263.get()
                    tmp19 = subjects18
                    subjects18 = []
                    for s in tmp19:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp19, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 151264
                            if len(subjects2) >= 1 and subjects2[0] == -1/2:
                                tmp20 = subjects2.popleft()
                                # State 151265
                                if len(subjects2) == 0:
                                    pass
                                    # State 151266
                                    if len(subjects) == 0:
                                        pass
                                        # 1: 1/sqrt(f + x*g)
                                subjects2.appendleft(tmp20)
                    subjects2.appendleft(tmp17)
            if len(subjects2) >= 1 and isinstance(subjects2[0], Add):
                tmp21 = subjects2.popleft()
                associative1 = tmp21
                associative_type1 = type(tmp21)
                subjects22 = deque(tmp21._args)
                matcher = CommutativeMatcher151248.get()
                tmp23 = subjects22
                subjects22 = []
                for s in tmp23:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp23, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 151254
                        if len(subjects2) >= 1 and subjects2[0] == 1/2:
                            tmp24 = subjects2.popleft()
                            # State 151255
                            if len(subjects2) == 0:
                                pass
                                # State 151256
                                if len(subjects) == 0:
                                    pass
                                    # 0: sqrt(d + x*e)
                            subjects2.appendleft(tmp24)
                    if pattern_index == 1:
                        pass
                        # State 151270
                        if len(subjects2) >= 1 and subjects2[0] == -1/2:
                            tmp25 = subjects2.popleft()
                            # State 151271
                            if len(subjects2) == 0:
                                pass
                                # State 151272
                                if len(subjects) == 0:
                                    pass
                                    # 1: 1/sqrt(f + x*g)
                            subjects2.appendleft(tmp25)
                    if pattern_index == 2:
                        pass
                        # State 151426
                        if len(subjects2) >= 1 and subjects2[0] == 1/2:
                            tmp26 = subjects2.popleft()
                            # State 151427
                            if len(subjects2) == 0:
                                pass
                                # State 151428
                                if len(subjects) == 0:
                                    pass
                                    # 2: sqrt(x*e + 1)
                            subjects2.appendleft(tmp26)
                    if pattern_index == 3:
                        pass
                        # State 151429
                        if len(subjects2) >= 1 and subjects2[0] == -1/2:
                            tmp27 = subjects2.popleft()
                            # State 151430
                            if len(subjects2) == 0:
                                pass
                                # State 151431
                                if len(subjects) == 0:
                                    pass
                                    # 3: 1/sqrt(x*g + 1)
                            subjects2.appendleft(tmp27)
                subjects2.appendleft(tmp21)
            subjects.appendleft(tmp1)
        return
        yield


from matchpy.utils import VariableWithCount
from matchpy.matching.many_to_one import CommutativeMatcher
from multiset import Multiset
from collections import deque
