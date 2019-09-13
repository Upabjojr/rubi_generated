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

class CommutativeMatcher11766(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({0: 1}), [
      (VariableWithCount('i2.2.1.2.0', 1, 1, None), Add)
]),
    1: (1, Multiset({0: 1}), [
      (VariableWithCount('i2.2.1.2.0', 1, 1, S(0)), Add)
]),
    2: (2, Multiset({1: 1}), [
      (VariableWithCount('i2.2.1.2.0', 1, 1, S(0)), Add)
]),
    3: (3, Multiset({2: 1, 3: 1}), [
      (VariableWithCount('i2.2.1.2.0', 1, 1, S(0)), Add)
]),
    4: (4, Multiset({2: 1}), [
      (VariableWithCount('i2.2.1.2.0', 1, 1, S(0)), Add)
]),
    5: (5, Multiset({2: 1}), [
      (VariableWithCount('i2.2.1.2.0', 1, 1, None), Add)
]),
    6: (6, Multiset({1: 1}), [
      (VariableWithCount('i2.2.1.2.0', 1, 1, None), Add)
]),
    7: (7, Multiset({4: 1}), [
      (VariableWithCount('i2.2.1.2.0', 1, 1, None), Add)
]),
    8: (8, Multiset({5: 1}), [
      (VariableWithCount('i2.2.1.2.0', 1, 1, None), Add)
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
        if CommutativeMatcher11766._instance is None:
            CommutativeMatcher11766._instance = CommutativeMatcher11766()
        return CommutativeMatcher11766._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 11765
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.2.1.0_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 11767
            if len(subjects) >= 1:
                tmp2 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.1.0', tmp2)
                except ValueError:
                    pass
                else:
                    pass
                    # State 11768
                    if len(subjects) == 0:
                        pass
                        # 0: x*d
                subjects.appendleft(tmp2)
            if len(subjects) >= 1:
                tmp4 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.1.1', tmp4)
                except ValueError:
                    pass
                else:
                    pass
                    # State 12946
                    if len(subjects) == 0:
                        pass
                        # 3: b*x
                subjects.appendleft(tmp4)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.2.1.0', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 12789
            subst2 = Substitution(subst1)
            try:
                subst2.try_add_variable('i2.2.1.2.1.2', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 12790
                if len(subjects) >= 1:
                    tmp8 = subjects.popleft()
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.2.1.2.1.1', tmp8)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 12791
                        if len(subjects) == 0:
                            pass
                            # 1: b*x**p
                    subjects.appendleft(tmp8)
            if len(subjects) >= 1 and isinstance(subjects[0], Pow):
                tmp10 = subjects.popleft()
                subjects11 = deque(tmp10._args)
                # State 12792
                if len(subjects11) >= 1:
                    tmp12 = subjects11.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.2.1.1', tmp12)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 12793
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.2.1.2', 1)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 12794
                            if len(subjects11) == 0:
                                pass
                                # State 12795
                                if len(subjects) == 0:
                                    pass
                                    # 1: b*x**p
                        if len(subjects11) >= 1:
                            tmp15 = subjects11.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.2.1.2', tmp15)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 12794
                                if len(subjects11) == 0:
                                    pass
                                    # State 12795
                                    if len(subjects) == 0:
                                        pass
                                        # 1: b*x**p
                            subjects11.appendleft(tmp15)
                        if len(subjects11) >= 1:
                            tmp17 = subjects11.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.2.1.2', tmp17)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 14338
                                if len(subjects11) == 0:
                                    pass
                                    # State 14339
                                    if len(subjects) == 0:
                                        pass
                                        # 5: b*x**n
                            subjects11.appendleft(tmp17)
                        if len(subjects11) >= 1 and subjects11[0] == 2:
                            tmp19 = subjects11.popleft()
                            # State 12941
                            if len(subjects11) == 0:
                                pass
                                # State 12942
                                if len(subjects) == 0:
                                    pass
                                    # 2: c*x**2
                            subjects11.appendleft(tmp19)
                        if len(subjects11) >= 1 and subjects11[0] == 4:
                            tmp20 = subjects11.popleft()
                            # State 14213
                            if len(subjects11) == 0:
                                pass
                                # State 14214
                                if len(subjects) == 0:
                                    pass
                                    # 4: b*x**4
                            subjects11.appendleft(tmp20)
                    subjects11.appendleft(tmp12)
                subjects.appendleft(tmp10)
        if len(subjects) >= 1 and isinstance(subjects[0], Mul):
            tmp21 = subjects.popleft()
            associative1 = tmp21
            associative_type1 = type(tmp21)
            subjects22 = deque(tmp21._args)
            matcher = CommutativeMatcher11770.get()
            tmp23 = subjects22
            subjects22 = []
            for s in tmp23:
                matcher.add_subject(s)
            for pattern_index, subst1 in matcher.match(tmp23, subst0):
                pass
                if pattern_index == 0:
                    pass
                    # State 11771
                    if len(subjects) == 0:
                        pass
                        # 0: x*d
                if pattern_index == 1:
                    pass
                    # State 12802
                    if len(subjects) == 0:
                        pass
                        # 1: b*x**p
                if pattern_index == 2:
                    pass
                    # State 12945
                    if len(subjects) == 0:
                        pass
                        # 2: c*x**2
                if pattern_index == 3:
                    pass
                    # State 12947
                    if len(subjects) == 0:
                        pass
                        # 3: b*x
                if pattern_index == 4:
                    pass
                    # State 14217
                    if len(subjects) == 0:
                        pass
                        # 4: b*x**4
                if pattern_index == 5:
                    pass
                    # State 14342
                    if len(subjects) == 0:
                        pass
                        # 5: b*x**n
            subjects.appendleft(tmp21)
        return
        yield


from matchpy.utils import VariableWithCount
from matchpy.matching.many_to_one import CommutativeMatcher
from multiset import Multiset
from collections import deque
