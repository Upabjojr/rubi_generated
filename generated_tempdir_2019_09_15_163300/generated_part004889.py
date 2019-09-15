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


class CommutativeMatcher12627(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({0: 1}), [
      (VariableWithCount('i2.2.1.2.0_1', 1, 1, S(0)), Add)
]),
    1: (1, Multiset({1: 1}), [
      (VariableWithCount('i2.2.1.2.0', 1, 1, None), Add)
]),
    2: (2, Multiset({2: 1}), [
      (VariableWithCount('i2.2.1.2.0_1', 1, 1, S(0)), Add)
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
        if CommutativeMatcher12627._instance is None:
            CommutativeMatcher12627._instance = CommutativeMatcher12627()
        return CommutativeMatcher12627._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 12626
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.2.1.0_2', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 12628
            if len(subjects) >= 1:
                tmp2 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.1.0', tmp2)
                except ValueError:
                    pass
                else:
                    pass
                    # State 12629
                    if len(subjects) == 0:
                        pass
                        # 0: x*d
                        yield 0, subst2
                subjects.appendleft(tmp2)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.2.1.0', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 14003
            if len(subjects) >= 1 and isinstance(subjects[0], Pow):
                tmp5 = subjects.popleft()
                subjects6 = deque(tmp5._args)
                # State 14004
                if len(subjects6) >= 1:
                    tmp7 = subjects6.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.1', tmp7)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 14005
                        if len(subjects6) >= 1 and subjects6[0] == Integer(2):
                            tmp9 = subjects6.popleft()
                            # State 14006
                            if len(subjects6) == 0:
                                pass
                                # State 14007
                                if len(subjects) == 0:
                                    pass
                                    # 1: x**2*c
                                    yield 1, subst2
                            subjects6.appendleft(tmp9)
                    subjects6.appendleft(tmp7)
                subjects.appendleft(tmp5)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.2.1.0_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 151592
            subst2 = Substitution(subst1)
            try:
                subst2.try_add_variable('i2.2.1.2.1.2', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 151593
                if len(subjects) >= 1:
                    tmp12 = subjects.popleft()
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.2.1.2.1.1', tmp12)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 151594
                        if len(subjects) == 0:
                            pass
                            # 2: d*x**n
                            yield 2, subst3
                    subjects.appendleft(tmp12)
            if len(subjects) >= 1 and isinstance(subjects[0], Pow):
                tmp14 = subjects.popleft()
                subjects15 = deque(tmp14._args)
                # State 151595
                if len(subjects15) >= 1:
                    tmp16 = subjects15.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.2.1.1', tmp16)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 151596
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.2.1.2', 1)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 151597
                            if len(subjects15) == 0:
                                pass
                                # State 151598
                                if len(subjects) == 0:
                                    pass
                                    # 2: d*x**n
                                    yield 2, subst3
                        if len(subjects15) >= 1:
                            tmp19 = subjects15.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.2.1.2', tmp19)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 151597
                                if len(subjects15) == 0:
                                    pass
                                    # State 151598
                                    if len(subjects) == 0:
                                        pass
                                        # 2: d*x**n
                                        yield 2, subst3
                            subjects15.appendleft(tmp19)
                    subjects15.appendleft(tmp16)
                subjects.appendleft(tmp14)
        if len(subjects) >= 1 and isinstance(subjects[0], Mul):
            tmp21 = subjects.popleft()
            associative1 = tmp21
            associative_type1 = type(tmp21)
            subjects22 = deque(tmp21._args)
            matcher = CommutativeMatcher12631.get()
            tmp23 = subjects22
            subjects22 = []
            for s in tmp23:
                matcher.add_subject(s)
            for pattern_index, subst1 in matcher.match(tmp23, subst0):
                pass
                if pattern_index == 0:
                    pass
                    # State 12632
                    if len(subjects) == 0:
                        pass
                        # 0: x*d
                        yield 0, subst1
                if pattern_index == 1:
                    pass
                    # State 14012
                    if len(subjects) == 0:
                        pass
                        # 1: x**2*c
                        yield 1, subst1
                if pattern_index == 2:
                    pass
                    # State 151604
                    if len(subjects) == 0:
                        pass
                        # 2: d*x**n
                        yield 2, subst1
            subjects.appendleft(tmp21)
        return
        yield


from .generated_part004890 import *
from matchpy.matching.many_to_one import CommutativeMatcher
from collections import deque
from matchpy.utils import VariableWithCount
from multiset import Multiset