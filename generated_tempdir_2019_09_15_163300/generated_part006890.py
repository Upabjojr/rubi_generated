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


class CommutativeMatcher65742(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({}), [
      (VariableWithCount('i2.3.1.0', 1, 1, None), Mul),
      (VariableWithCount('i2.3.1.0_1', 1, 1, S(1)), Mul)
]),
    1: (1, Multiset({}), [
      (VariableWithCount('i2.2.1.0', 1, 1, None), Mul),
      (VariableWithCount('i2.3.1.0', 1, 1, S(1)), Mul)
]),
    2: (2, Multiset({0: 1}), [
      (VariableWithCount('i2.3.1.0', 1, 1, S(1)), Mul)
]),
    3: (3, Multiset({1: 1}), [
      (VariableWithCount('i2.3.1.0', 1, 1, S(1)), Mul)
]),
    4: (4, Multiset({}), [
      (VariableWithCount('i2.2.2.1.0', 1, 1, None), Mul),
      (VariableWithCount('i2.3.1.0', 1, 1, S(1)), Mul)
]),
    5: (5, Multiset({2: 1}), [
      (VariableWithCount('i2.3.1.0', 1, 1, S(1)), Mul)
]),
    6: (6, Multiset({3: 1}), [
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
        if CommutativeMatcher65742._instance is None:
            CommutativeMatcher65742._instance = CommutativeMatcher65742()
        return CommutativeMatcher65742._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 65741
        if len(subjects) >= 1 and isinstance(subjects[0], Pow):
            tmp1 = subjects.popleft()
            subjects2 = deque(tmp1._args)
            # State 74647
            if len(subjects2) >= 1:
                tmp3 = subjects2.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.3.1.1', tmp3)
                except ValueError:
                    pass
                else:
                    pass
                    # State 74648
                    if len(subjects2) >= 1:
                        tmp5 = subjects2.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.3.1.2', tmp5)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 74649
                            if len(subjects2) == 0:
                                pass
                                # State 74650
                                if len(subjects) == 0:
                                    pass
                                    # 0: x**n
                                    yield 0, subst2
                        subjects2.appendleft(tmp5)
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.3.1.2', 1)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 75567
                        if len(subjects2) == 0:
                            pass
                            # State 75568
                            if len(subjects) == 0:
                                pass
                                # 1: x**n
                                yield 1, subst2
                    if len(subjects2) >= 1:
                        tmp8 = subjects2.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.3.1.2', tmp8)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 75567
                            if len(subjects2) == 0:
                                pass
                                # State 75568
                                if len(subjects) == 0:
                                    pass
                                    # 1: x**n
                                    yield 1, subst2
                        subjects2.appendleft(tmp8)
                subjects2.appendleft(tmp3)
            if len(subjects2) >= 1 and isinstance(subjects2[0], Add):
                tmp10 = subjects2.popleft()
                associative1 = tmp10
                associative_type1 = type(tmp10)
                subjects11 = deque(tmp10._args)
                matcher = CommutativeMatcher107450.get()
                tmp12 = subjects11
                subjects11 = []
                for s in tmp12:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp12, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 107456
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
                                    # State 107457
                                    if len(subjects2) == 0:
                                        pass
                                        # State 107458
                                        if len(subjects) == 0:
                                            pass
                                            # 3: (x*d + c)**n
                                            yield 3, subst2
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
            # State 75565
            if len(subjects) >= 1:
                tmp17 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.3.1.1', tmp17)
                except ValueError:
                    pass
                else:
                    pass
                    # State 75566
                    if len(subjects) == 0:
                        pass
                        # 1: x**n
                        yield 1, subst2
                subjects.appendleft(tmp17)
        if len(subjects) >= 1 and isinstance(subjects[0], log):
            tmp19 = subjects.popleft()
            subjects20 = deque(tmp19._args)
            # State 105068
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.3.1.2.0', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 105069
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.3.1.2.2', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 105070
                    if len(subjects20) >= 1:
                        tmp23 = subjects20.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.3.1.2.1', tmp23)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 105071
                            if len(subjects20) == 0:
                                pass
                                # State 105072
                                if len(subjects) == 0:
                                    pass
                                    # 2: log(c*x**n)
                                    yield 2, subst3
                        subjects20.appendleft(tmp23)
                if len(subjects20) >= 1 and isinstance(subjects20[0], Pow):
                    tmp25 = subjects20.popleft()
                    subjects26 = deque(tmp25._args)
                    # State 105073
                    if len(subjects26) >= 1:
                        tmp27 = subjects26.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.3.1.2.1', tmp27)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 105074
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.3.1.2.2', 1)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 105075
                                if len(subjects26) == 0:
                                    pass
                                    # State 105076
                                    if len(subjects20) == 0:
                                        pass
                                        # State 105077
                                        if len(subjects) == 0:
                                            pass
                                            # 2: log(c*x**n)
                                            yield 2, subst3
                            if len(subjects26) >= 1:
                                tmp30 = subjects26.popleft()
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i2.3.1.2.2', tmp30)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 105075
                                    if len(subjects26) == 0:
                                        pass
                                        # State 105076
                                        if len(subjects20) == 0:
                                            pass
                                            # State 105077
                                            if len(subjects) == 0:
                                                pass
                                                # 2: log(c*x**n)
                                                yield 2, subst3
                                subjects26.appendleft(tmp30)
                        subjects26.appendleft(tmp27)
                    subjects20.appendleft(tmp25)
            if len(subjects20) >= 1 and isinstance(subjects20[0], Mul):
                tmp32 = subjects20.popleft()
                associative1 = tmp32
                associative_type1 = type(tmp32)
                subjects33 = deque(tmp32._args)
                matcher = CommutativeMatcher105079.get()
                tmp34 = subjects33
                subjects33 = []
                for s in tmp34:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp34, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 105086
                        if len(subjects20) == 0:
                            pass
                            # State 105087
                            if len(subjects) == 0:
                                pass
                                # 2: log(c*x**n)
                                yield 2, subst1
                subjects20.appendleft(tmp32)
            subjects.appendleft(tmp19)
        return
        yield


from .generated_part006891 import *
from matchpy.matching.many_to_one import CommutativeMatcher
from .generated_part006893 import *
from collections import deque
from matchpy.utils import VariableWithCount
from multiset import Multiset