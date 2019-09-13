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

class CommutativeMatcher65667(CommutativeMatcher):
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
        if CommutativeMatcher65667._instance is None:
            CommutativeMatcher65667._instance = CommutativeMatcher65667()
        return CommutativeMatcher65667._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 65666
        if len(subjects) >= 1 and isinstance(subjects[0], Pow):
            tmp1 = subjects.popleft()
            subjects2 = deque(tmp1._args)
            # State 74616
            if len(subjects2) >= 1:
                tmp3 = subjects2.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.1', tmp3)
                except ValueError:
                    pass
                else:
                    pass
                    # State 74617
                    if len(subjects2) >= 1:
                        tmp5 = subjects2.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.3.1.2', tmp5)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 74618
                            if len(subjects2) == 0:
                                pass
                                # State 74619
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
                        # State 75466
                        if len(subjects2) == 0:
                            pass
                            # State 75467
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
                            # State 75466
                            if len(subjects2) == 0:
                                pass
                                # State 75467
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
                matcher = CommutativeMatcher107349.get()
                tmp12 = subjects11
                subjects11 = []
                for s in tmp12:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp12, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 107355
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
                                    # State 107356
                                    if len(subjects2) == 0:
                                        pass
                                        # State 107357
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
            # State 75464
            if len(subjects) >= 1:
                tmp17 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.1', tmp17)
                except ValueError:
                    pass
                else:
                    pass
                    # State 75465
                    if len(subjects) == 0:
                        pass
                        # 1: x**n
                subjects.appendleft(tmp17)
        if len(subjects) >= 1 and isinstance(subjects[0], log):
            tmp19 = subjects.popleft()
            subjects20 = deque(tmp19._args)
            # State 104967
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.3.1.2.0', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 104968
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.3.1.2.2', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 104969
                    if len(subjects20) >= 1:
                        tmp23 = subjects20.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.1', tmp23)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 104970
                            if len(subjects20) == 0:
                                pass
                                # State 104971
                                if len(subjects) == 0:
                                    pass
                                    # 2: log(x**n*c)
                        subjects20.appendleft(tmp23)
                if len(subjects20) >= 1 and isinstance(subjects20[0], Pow):
                    tmp25 = subjects20.popleft()
                    subjects26 = deque(tmp25._args)
                    # State 104972
                    if len(subjects26) >= 1:
                        tmp27 = subjects26.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.1', tmp27)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 104973
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.3.1.2.2', 1)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 104974
                                if len(subjects26) == 0:
                                    pass
                                    # State 104975
                                    if len(subjects20) == 0:
                                        pass
                                        # State 104976
                                        if len(subjects) == 0:
                                            pass
                                            # 2: log(x**n*c)
                            if len(subjects26) >= 1:
                                tmp30 = subjects26.popleft()
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i2.3.1.2.2', tmp30)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 104974
                                    if len(subjects26) == 0:
                                        pass
                                        # State 104975
                                        if len(subjects20) == 0:
                                            pass
                                            # State 104976
                                            if len(subjects) == 0:
                                                pass
                                                # 2: log(x**n*c)
                                subjects26.appendleft(tmp30)
                        subjects26.appendleft(tmp27)
                    subjects20.appendleft(tmp25)
            if len(subjects20) >= 1 and isinstance(subjects20[0], Mul):
                tmp32 = subjects20.popleft()
                associative1 = tmp32
                associative_type1 = type(tmp32)
                subjects33 = deque(tmp32._args)
                matcher = CommutativeMatcher104978.get()
                tmp34 = subjects33
                subjects33 = []
                for s in tmp34:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp34, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 104985
                        if len(subjects20) == 0:
                            pass
                            # State 104986
                            if len(subjects) == 0:
                                pass
                                # 2: log(x**n*c)
                subjects20.appendleft(tmp32)
            subjects.appendleft(tmp19)
        return
        yield


from matchpy.utils import VariableWithCount
from matchpy.matching.many_to_one import CommutativeMatcher
from multiset import Multiset
from collections import deque
