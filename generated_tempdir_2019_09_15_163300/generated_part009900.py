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


class CommutativeMatcher89909(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({}), [
      (VariableWithCount('i5.1.0', 1, 1, None), Mul),
      (VariableWithCount('i5.1.0_1', 1, 1, S(1)), Mul)
]),
    1: (1, Multiset({0: 1}), [
      (VariableWithCount('i5.1.0', 1, 1, S(1)), Mul)
]),
    2: (2, Multiset({1: 1}), [
      (VariableWithCount('i5.1.0', 1, 1, S(1)), Mul)
]),
    3: (3, Multiset({2: 1}), [
      (VariableWithCount('i5.1.0', 1, 1, S(1)), Mul)
]),
    4: (4, Multiset({3: 1}), [
      (VariableWithCount('i5.1.0', 1, 1, S(1)), Mul)
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
        if CommutativeMatcher89909._instance is None:
            CommutativeMatcher89909._instance = CommutativeMatcher89909()
        return CommutativeMatcher89909._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 89908
        if len(subjects) >= 1 and isinstance(subjects[0], log):
            tmp1 = subjects.popleft()
            subjects2 = deque(tmp1._args)
            # State 105762
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i5.1.2.0', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 105763
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i5.1.2.2', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 105764
                    if len(subjects2) >= 1:
                        tmp5 = subjects2.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i5.1.2.1', tmp5)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 105765
                            if len(subjects2) == 0:
                                pass
                                # State 105766
                                if len(subjects) == 0:
                                    pass
                                    # 0: log(c*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f1721)
                                    yield 0, subst3
                                    # 1: log(c*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f1723)
                                    yield 1, subst3
                                    # 2: log(c*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f1713)
                                    yield 2, subst3
                                    # 3: log(c*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f1713)
                                    yield 3, subst3
                        subjects2.appendleft(tmp5)
                if len(subjects2) >= 1 and isinstance(subjects2[0], Pow):
                    tmp7 = subjects2.popleft()
                    subjects8 = deque(tmp7._args)
                    # State 105767
                    if len(subjects8) >= 1:
                        tmp9 = subjects8.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i5.1.2.1', tmp9)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 105768
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i5.1.2.2', 1)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 105769
                                if len(subjects8) == 0:
                                    pass
                                    # State 105770
                                    if len(subjects2) == 0:
                                        pass
                                        # State 105771
                                        if len(subjects) == 0:
                                            pass
                                            # 0: log(c*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f1721)
                                            yield 0, subst3
                                            # 1: log(c*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f1723)
                                            yield 1, subst3
                                            # 2: log(c*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f1713)
                                            yield 2, subst3
                                            # 3: log(c*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f1713)
                                            yield 3, subst3
                            if len(subjects8) >= 1:
                                tmp12 = subjects8.popleft()
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i5.1.2.2', tmp12)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 105769
                                    if len(subjects8) == 0:
                                        pass
                                        # State 105770
                                        if len(subjects2) == 0:
                                            pass
                                            # State 105771
                                            if len(subjects) == 0:
                                                pass
                                                # 0: log(c*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f1721)
                                                yield 0, subst3
                                                # 1: log(c*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f1723)
                                                yield 1, subst3
                                                # 2: log(c*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f1713)
                                                yield 2, subst3
                                                # 3: log(c*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f1713)
                                                yield 3, subst3
                                subjects8.appendleft(tmp12)
                        subjects8.appendleft(tmp9)
                    subjects2.appendleft(tmp7)
            if len(subjects2) >= 1 and isinstance(subjects2[0], Mul):
                tmp14 = subjects2.popleft()
                associative1 = tmp14
                associative_type1 = type(tmp14)
                subjects15 = deque(tmp14._args)
                matcher = CommutativeMatcher105773.get()
                tmp16 = subjects15
                subjects15 = []
                for s in tmp16:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp16, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 105780
                        if len(subjects2) == 0:
                            pass
                            # State 105781
                            if len(subjects) == 0:
                                pass
                                # 0: log(c*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f1721)
                                yield 0, subst1
                                # 1: log(c*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f1723)
                                yield 1, subst1
                                # 2: log(c*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f1713)
                                yield 2, subst1
                                # 3: log(c*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f1713)
                                yield 3, subst1
                subjects2.appendleft(tmp14)
            subjects.appendleft(tmp1)
        return
        yield


from matchpy.matching.many_to_one import CommutativeMatcher
from collections import deque
from .generated_part009901 import *
from matchpy.utils import VariableWithCount
from multiset import Multiset