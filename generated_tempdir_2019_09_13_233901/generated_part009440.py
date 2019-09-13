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

class CommutativeMatcher10089(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({0: 1}), [
      (VariableWithCount('i3.1.2.0', 1, 1, S(1)), Mul)
]),
    1: (1, Multiset({1: 1}), [
      (VariableWithCount('i3.1.2.0', 1, 1, S(1)), Mul)
]),
    2: (2, Multiset({2: 1}), [
      (VariableWithCount('i3.1.2.0', 1, 1, S(1)), Mul)
]),
    3: (3, Multiset({3: 1}), [
      (VariableWithCount('i3.1.2.0', 1, 1, S(1)), Mul)
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
        if CommutativeMatcher10089._instance is None:
            CommutativeMatcher10089._instance = CommutativeMatcher10089()
        return CommutativeMatcher10089._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 10088
        if len(subjects) >= 1 and isinstance(subjects[0], Pow):
            tmp1 = subjects.popleft()
            subjects2 = deque(tmp1._args)
            # State 10090
            if len(subjects2) >= 1:
                tmp3 = subjects2.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i3.1.2.1', tmp3)
                except ValueError:
                    pass
                else:
                    pass
                    # State 10091
                    if len(subjects2) >= 1:
                        tmp5 = subjects2.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i3.1.2.2', tmp5)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 10092
                            if len(subjects2) == 0:
                                pass
                                # State 10093
                                if len(subjects) == 0:
                                    pass
                                    # 0: x**n
                        subjects2.appendleft(tmp5)
                    if len(subjects2) >= 1 and subjects2[0] == -1:
                        tmp7 = subjects2.popleft()
                        # State 10622
                        if len(subjects2) == 0:
                            pass
                            # State 10623
                            if len(subjects) == 0:
                                pass
                                # 1: 1/x
                        subjects2.appendleft(tmp7)
                subjects2.appendleft(tmp3)
            if len(subjects2) >= 1 and isinstance(subjects2[0], tan):
                tmp8 = subjects2.popleft()
                subjects9 = deque(tmp8._args)
                # State 82277
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i3.1.2.3.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 82278
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i3.1.2.3.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 82279
                        if len(subjects9) >= 1:
                            tmp12 = subjects9.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i3.1.2.3.1.0', tmp12)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 82280
                                if len(subjects9) == 0:
                                    pass
                                    # State 82281
                                    if len(subjects2) >= 1 and subjects2[0] == -1:
                                        tmp14 = subjects2.popleft()
                                        # State 82282
                                        if len(subjects2) == 0:
                                            pass
                                            # State 82283
                                            if len(subjects) == 0:
                                                pass
                                                # 3: 1/tan(c + x*d)
                                        subjects2.appendleft(tmp14)
                            subjects9.appendleft(tmp12)
                    if len(subjects9) >= 1 and isinstance(subjects9[0], Mul):
                        tmp15 = subjects9.popleft()
                        associative1 = tmp15
                        associative_type1 = type(tmp15)
                        subjects16 = deque(tmp15._args)
                        matcher = CommutativeMatcher82285.get()
                        tmp17 = subjects16
                        subjects16 = []
                        for s in tmp17:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp17, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 82286
                                if len(subjects9) == 0:
                                    pass
                                    # State 82287
                                    if len(subjects2) >= 1 and subjects2[0] == -1:
                                        tmp18 = subjects2.popleft()
                                        # State 82288
                                        if len(subjects2) == 0:
                                            pass
                                            # State 82289
                                            if len(subjects) == 0:
                                                pass
                                                # 3: 1/tan(c + x*d)
                                        subjects2.appendleft(tmp18)
                        subjects9.appendleft(tmp15)
                if len(subjects9) >= 1 and isinstance(subjects9[0], Add):
                    tmp19 = subjects9.popleft()
                    associative1 = tmp19
                    associative_type1 = type(tmp19)
                    subjects20 = deque(tmp19._args)
                    matcher = CommutativeMatcher82291.get()
                    tmp21 = subjects20
                    subjects20 = []
                    for s in tmp21:
                        matcher.add_subject(s)
                    for pattern_index, subst1 in matcher.match(tmp21, subst0):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 82297
                            if len(subjects9) == 0:
                                pass
                                # State 82298
                                if len(subjects2) >= 1 and subjects2[0] == -1:
                                    tmp22 = subjects2.popleft()
                                    # State 82299
                                    if len(subjects2) == 0:
                                        pass
                                        # State 82300
                                        if len(subjects) == 0:
                                            pass
                                            # 3: 1/tan(c + x*d)
                                    subjects2.appendleft(tmp22)
                    subjects9.appendleft(tmp19)
                subjects2.appendleft(tmp8)
            subjects.appendleft(tmp1)
        if len(subjects) >= 1 and isinstance(subjects[0], tan):
            tmp23 = subjects.popleft()
            subjects24 = deque(tmp23._args)
            # State 82175
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i3.1.2.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 82176
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i3.1.2.2.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 82177
                    if len(subjects24) >= 1:
                        tmp27 = subjects24.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i3.1.2.2.1.0', tmp27)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 82178
                            if len(subjects24) == 0:
                                pass
                                # State 82179
                                if len(subjects) == 0:
                                    pass
                                    # 2: tan(c + x*d)
                        subjects24.appendleft(tmp27)
                if len(subjects24) >= 1 and isinstance(subjects24[0], Mul):
                    tmp29 = subjects24.popleft()
                    associative1 = tmp29
                    associative_type1 = type(tmp29)
                    subjects30 = deque(tmp29._args)
                    matcher = CommutativeMatcher82181.get()
                    tmp31 = subjects30
                    subjects30 = []
                    for s in tmp31:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp31, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 82182
                            if len(subjects24) == 0:
                                pass
                                # State 82183
                                if len(subjects) == 0:
                                    pass
                                    # 2: tan(c + x*d)
                    subjects24.appendleft(tmp29)
            if len(subjects24) >= 1 and isinstance(subjects24[0], Add):
                tmp32 = subjects24.popleft()
                associative1 = tmp32
                associative_type1 = type(tmp32)
                subjects33 = deque(tmp32._args)
                matcher = CommutativeMatcher82185.get()
                tmp34 = subjects33
                subjects33 = []
                for s in tmp34:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp34, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 82191
                        if len(subjects24) == 0:
                            pass
                            # State 82192
                            if len(subjects) == 0:
                                pass
                                # 2: tan(c + x*d)
                subjects24.appendleft(tmp32)
            subjects.appendleft(tmp23)
        return
        yield


from matchpy.utils import VariableWithCount
from matchpy.matching.many_to_one import CommutativeMatcher
from multiset import Multiset
from collections import deque
