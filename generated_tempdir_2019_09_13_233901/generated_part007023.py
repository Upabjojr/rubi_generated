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

class CommutativeMatcher121782(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({}), [
      (VariableWithCount('i2.2.1.0', 1, 1, None), Mul),
      (VariableWithCount('i2.3.1.0', 1, 1, S(1)), Mul)
]),
    1: (1, Multiset({0: 1}), [
      (VariableWithCount('i2.3.1.0', 1, 1, S(1)), Mul)
]),
    2: (2, Multiset({1: 1}), [
      (VariableWithCount('i2.3.1.0', 1, 1, S(1)), Mul)
]),
    3: (3, Multiset({}), [
      (VariableWithCount('i2.3.1.0', 1, 1, None), Mul),
      (VariableWithCount('i2.3.1.0_1', 1, 1, S(1)), Mul)
]),
    4: (4, Multiset({2: 1}), [
      (VariableWithCount('i2.3.1.0', 1, 1, S(1)), Mul)
]),
    5: (5, Multiset({3: 1}), [
      (VariableWithCount('i2.3.1.0', 1, 1, S(1)), Mul)
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
        if CommutativeMatcher121782._instance is None:
            CommutativeMatcher121782._instance = CommutativeMatcher121782()
        return CommutativeMatcher121782._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 121781
        if len(subjects) >= 1 and isinstance(subjects[0], Pow):
            tmp1 = subjects.popleft()
            subjects2 = deque(tmp1._args)
            # State 124561
            if len(subjects2) >= 1:
                tmp3 = subjects2.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.3.1.1', tmp3)
                except ValueError:
                    pass
                else:
                    pass
                    # State 124562
                    if len(subjects2) >= 1:
                        tmp5 = subjects2.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.3.1.2', tmp5)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 124563
                            if len(subjects2) == 0:
                                pass
                                # State 124564
                                if len(subjects) == 0:
                                    pass
                                    # 0: x**n
                        subjects2.appendleft(tmp5)
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.3.1.2', 1)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 125493
                        if len(subjects2) == 0:
                            pass
                            # State 125494
                            if len(subjects) == 0:
                                pass
                                # 1: x**n
                    if len(subjects2) >= 1:
                        tmp8 = subjects2.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.3.1.2', tmp8)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 125493
                            if len(subjects2) == 0:
                                pass
                                # State 125494
                                if len(subjects) == 0:
                                    pass
                                    # 1: x**n
                        subjects2.appendleft(tmp8)
                subjects2.appendleft(tmp3)
            if len(subjects2) >= 1 and isinstance(subjects2[0], Add):
                tmp10 = subjects2.popleft()
                associative1 = tmp10
                associative_type1 = type(tmp10)
                subjects11 = deque(tmp10._args)
                matcher = CommutativeMatcher137084.get()
                tmp12 = subjects11
                subjects11 = []
                for s in tmp12:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp12, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 137090
                        if len(subjects2) >= 1:
                            tmp13 = []
                            tmp13.append(subjects2.popleft())
                            while True:
                                if len(tmp13) > 1:
                                    tmp14 = create_operation_expression(associative1, tmp13)
                                elif len(tmp13) == 1:
                                    tmp14 = tmp13[0]
                                else:
                                    assert False, "Unreachable"
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i2.3.1.2', tmp14)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 137091
                                    if len(subjects2) == 0:
                                        pass
                                        # State 137092
                                        if len(subjects) == 0:
                                            pass
                                            # 3: (x*d + c)**n
                                if len(subjects2) == 0:
                                    break
                                tmp13.append(subjects2.popleft())
                            subjects2.extendleft(reversed(tmp13))
                subjects2.appendleft(tmp10)
            subjects.appendleft(tmp1)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.3.1.2', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 125491
            if len(subjects) >= 1:
                tmp17 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.3.1.1', tmp17)
                except ValueError:
                    pass
                else:
                    pass
                    # State 125492
                    if len(subjects) == 0:
                        pass
                        # 1: x**n
                subjects.appendleft(tmp17)
        if len(subjects) >= 1 and isinstance(subjects[0], log):
            tmp19 = subjects.popleft()
            subjects20 = deque(tmp19._args)
            # State 134195
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.3.1.2.0', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 134196
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.3.1.2.2', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 134197
                    if len(subjects20) >= 1:
                        tmp23 = subjects20.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.3.1.2.1', tmp23)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 134198
                            if len(subjects20) == 0:
                                pass
                                # State 134199
                                if len(subjects) == 0:
                                    pass
                                    # 2: log(c*x**n)
                        subjects20.appendleft(tmp23)
                if len(subjects20) >= 1 and isinstance(subjects20[0], Pow):
                    tmp25 = subjects20.popleft()
                    subjects26 = deque(tmp25._args)
                    # State 134200
                    if len(subjects26) >= 1:
                        tmp27 = subjects26.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.3.1.2.1', tmp27)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 134201
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.3.1.2.2', 1)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 134202
                                if len(subjects26) == 0:
                                    pass
                                    # State 134203
                                    if len(subjects20) == 0:
                                        pass
                                        # State 134204
                                        if len(subjects) == 0:
                                            pass
                                            # 2: log(c*x**n)
                            if len(subjects26) >= 1:
                                tmp30 = subjects26.popleft()
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i2.3.1.2.2', tmp30)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 134202
                                    if len(subjects26) == 0:
                                        pass
                                        # State 134203
                                        if len(subjects20) == 0:
                                            pass
                                            # State 134204
                                            if len(subjects) == 0:
                                                pass
                                                # 2: log(c*x**n)
                                subjects26.appendleft(tmp30)
                        subjects26.appendleft(tmp27)
                    subjects20.appendleft(tmp25)
            if len(subjects20) >= 1 and isinstance(subjects20[0], Mul):
                tmp32 = subjects20.popleft()
                associative1 = tmp32
                associative_type1 = type(tmp32)
                subjects33 = deque(tmp32._args)
                matcher = CommutativeMatcher134206.get()
                tmp34 = subjects33
                subjects33 = []
                for s in tmp34:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp34, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 134213
                        if len(subjects20) == 0:
                            pass
                            # State 134214
                            if len(subjects) == 0:
                                pass
                                # 2: log(c*x**n)
                subjects20.appendleft(tmp32)
            subjects.appendleft(tmp19)
        return
        yield


from matchpy.utils import VariableWithCount
from matchpy.matching.many_to_one import CommutativeMatcher
from multiset import Multiset
from collections import deque
