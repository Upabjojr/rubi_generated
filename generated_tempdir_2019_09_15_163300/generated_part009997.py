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


class CommutativeMatcher57788(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({}), [
      (VariableWithCount('i4.1.0', 1, 1, None), Mul),
      (VariableWithCount('i4.1.0_1', 1, 1, S(1)), Mul)
]),
    1: (1, Multiset({0: 1}), [
      (VariableWithCount('i4.1.0', 1, 1, S(1)), Mul)
]),
    2: (2, Multiset({}), [
      (VariableWithCount('i4.1.0_1', 1, 1, S(1)), Mul),
      (VariableWithCount('i4.1.1', 1, 1, None), Mul)
]),
    3: (3, Multiset({1: 1}), [
      (VariableWithCount('i4.1.0', 1, 1, S(1)), Mul)
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
        if CommutativeMatcher57788._instance is None:
            CommutativeMatcher57788._instance = CommutativeMatcher57788()
        return CommutativeMatcher57788._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 57787
        if len(subjects) >= 1 and isinstance(subjects[0], Pow):
            tmp1 = subjects.popleft()
            subjects2 = deque(tmp1._args)
            # State 75655
            if len(subjects2) >= 1:
                tmp3 = subjects2.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i4.1.1', tmp3)
                except ValueError:
                    pass
                else:
                    pass
                    # State 75656
                    if len(subjects2) >= 1 and subjects2[0] == Integer(2):
                        tmp5 = subjects2.popleft()
                        # State 75657
                        if len(subjects2) == 0:
                            pass
                            # State 75658
                            if len(subjects) == 0:
                                pass
                                # 0: x**2
                                yield 0, subst1
                        subjects2.appendleft(tmp5)
                subjects2.appendleft(tmp3)
            subjects.appendleft(tmp1)
        if len(subjects) >= 1 and isinstance(subjects[0], log):
            tmp6 = subjects.popleft()
            subjects7 = deque(tmp6._args)
            # State 104224
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i4.1.2.0', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 104225
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i4.1.2.2', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 104226
                    if len(subjects7) >= 1:
                        tmp10 = subjects7.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i4.1.2.1', tmp10)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 104227
                            if len(subjects7) == 0:
                                pass
                                # State 104228
                                if len(subjects) == 0:
                                    pass
                                    # 1: log(c*x**n)
                                    yield 1, subst3
                        subjects7.appendleft(tmp10)
                if len(subjects7) >= 1 and isinstance(subjects7[0], Pow):
                    tmp12 = subjects7.popleft()
                    subjects13 = deque(tmp12._args)
                    # State 104229
                    if len(subjects13) >= 1:
                        tmp14 = subjects13.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i4.1.2.1', tmp14)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 104230
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i4.1.2.2', 1)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 104231
                                if len(subjects13) == 0:
                                    pass
                                    # State 104232
                                    if len(subjects7) == 0:
                                        pass
                                        # State 104233
                                        if len(subjects) == 0:
                                            pass
                                            # 1: log(c*x**n)
                                            yield 1, subst3
                            if len(subjects13) >= 1:
                                tmp17 = subjects13.popleft()
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i4.1.2.2', tmp17)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 104231
                                    if len(subjects13) == 0:
                                        pass
                                        # State 104232
                                        if len(subjects7) == 0:
                                            pass
                                            # State 104233
                                            if len(subjects) == 0:
                                                pass
                                                # 1: log(c*x**n)
                                                yield 1, subst3
                                subjects13.appendleft(tmp17)
                        subjects13.appendleft(tmp14)
                    subjects7.appendleft(tmp12)
            if len(subjects7) >= 1 and isinstance(subjects7[0], Mul):
                tmp19 = subjects7.popleft()
                associative1 = tmp19
                associative_type1 = type(tmp19)
                subjects20 = deque(tmp19._args)
                matcher = CommutativeMatcher104235.get()
                tmp21 = subjects20
                subjects20 = []
                for s in tmp21:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp21, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 104242
                        if len(subjects7) == 0:
                            pass
                            # State 104243
                            if len(subjects) == 0:
                                pass
                                # 1: log(c*x**n)
                                yield 1, subst1
                subjects7.appendleft(tmp19)
            subjects.appendleft(tmp6)
        return
        yield


from .generated_part009998 import *
from matchpy.matching.many_to_one import CommutativeMatcher
from collections import deque
from matchpy.utils import VariableWithCount
from multiset import Multiset