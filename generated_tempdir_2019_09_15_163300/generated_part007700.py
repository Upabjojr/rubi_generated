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


class CommutativeMatcher56288(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({}), [
      (VariableWithCount('i2.2.1.0', 1, 1, None), Mul),
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul)
]),
    1: (1, Multiset({}), [
      (VariableWithCount('i2.1', 1, 1, None), Mul),
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    2: (2, Multiset({0: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    3: (3, Multiset({}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul),
      (VariableWithCount('i2.3.1.0', 1, 1, None), Mul)
]),
    4: (4, Multiset({}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul),
      (VariableWithCount('i2.3.1.1.0', 1, 1, None), Mul)
]),
    5: (5, Multiset({1: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
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
        if CommutativeMatcher56288._instance is None:
            CommutativeMatcher56288._instance = CommutativeMatcher56288()
        return CommutativeMatcher56288._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 56287
        if len(subjects) >= 1 and isinstance(subjects[0], Pow):
            tmp1 = subjects.popleft()
            subjects2 = deque(tmp1._args)
            # State 74532
            if len(subjects2) >= 1:
                tmp3 = subjects2.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.1', tmp3)
                except ValueError:
                    pass
                else:
                    pass
                    # State 74533
                    if len(subjects2) >= 1:
                        tmp5 = subjects2.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.1.2', tmp5)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 74534
                            if len(subjects2) == 0:
                                pass
                                # State 74535
                                if len(subjects) == 0:
                                    pass
                                    # 0: x**n
                                    yield 0, subst2
                        subjects2.appendleft(tmp5)
                subjects2.appendleft(tmp3)
            subjects.appendleft(tmp1)
        if len(subjects) >= 1 and isinstance(subjects[0], log):
            tmp7 = subjects.popleft()
            subjects8 = deque(tmp7._args)
            # State 105460
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.0', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 105461
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.2', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 105462
                    if len(subjects8) >= 1:
                        tmp11 = subjects8.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.1', tmp11)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 105463
                            if len(subjects8) == 0:
                                pass
                                # State 105464
                                if len(subjects) == 0:
                                    pass
                                    # 1: log(x**n*c)
                                    yield 1, subst3
                        subjects8.appendleft(tmp11)
                if len(subjects8) >= 1 and isinstance(subjects8[0], Pow):
                    tmp13 = subjects8.popleft()
                    subjects14 = deque(tmp13._args)
                    # State 105465
                    if len(subjects14) >= 1:
                        tmp15 = subjects14.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.1', tmp15)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 105466
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.2.2', 1)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 105467
                                if len(subjects14) == 0:
                                    pass
                                    # State 105468
                                    if len(subjects8) == 0:
                                        pass
                                        # State 105469
                                        if len(subjects) == 0:
                                            pass
                                            # 1: log(x**n*c)
                                            yield 1, subst3
                            if len(subjects14) >= 1:
                                tmp18 = subjects14.popleft()
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i2.2.1.2.2', tmp18)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 105467
                                    if len(subjects14) == 0:
                                        pass
                                        # State 105468
                                        if len(subjects8) == 0:
                                            pass
                                            # State 105469
                                            if len(subjects) == 0:
                                                pass
                                                # 1: log(x**n*c)
                                                yield 1, subst3
                                subjects14.appendleft(tmp18)
                        subjects14.appendleft(tmp15)
                    subjects8.appendleft(tmp13)
            if len(subjects8) >= 1 and isinstance(subjects8[0], Mul):
                tmp20 = subjects8.popleft()
                associative1 = tmp20
                associative_type1 = type(tmp20)
                subjects21 = deque(tmp20._args)
                matcher = CommutativeMatcher105471.get()
                tmp22 = subjects21
                subjects21 = []
                for s in tmp22:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp22, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 105478
                        if len(subjects8) == 0:
                            pass
                            # State 105479
                            if len(subjects) == 0:
                                pass
                                # 1: log(x**n*c)
                                yield 1, subst1
                subjects8.appendleft(tmp20)
            subjects.appendleft(tmp7)
        return
        yield


from matchpy.matching.many_to_one import CommutativeMatcher
from collections import deque
from .generated_part007701 import *
from matchpy.utils import VariableWithCount
from multiset import Multiset