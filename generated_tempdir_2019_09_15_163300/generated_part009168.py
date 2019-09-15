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


class CommutativeMatcher110396(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({0: 1}), [
      (VariableWithCount('i3.1.2.0', 1, 1, None), Add)
]),
    1: (1, Multiset({1: 1, 2: 1}), [
      
]),
    2: (2, Multiset({3: 1, 2: 1}), [
      
]),
    3: (3, Multiset({4: 1}), [
      (VariableWithCount('i3.1.2.0', 1, 1, None), Add)
])
}
    subjects = {}
    subjects_by_id = {}
    bipartite = BipartiteGraph()
    associative = Add
    max_optional_count = 0
    anonymous_patterns = {1, 3}

    def __init__(self):
        self.add_subject(None)

    @staticmethod
    def get():
        if CommutativeMatcher110396._instance is None:
            CommutativeMatcher110396._instance = CommutativeMatcher110396()
        return CommutativeMatcher110396._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 110395
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i3.1.2.1.0_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 110397
            if len(subjects) >= 1:
                tmp2 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i3.1.2.1.0', tmp2)
                except ValueError:
                    pass
                else:
                    pass
                    # State 110398
                    if len(subjects) == 0:
                        pass
                        # 0: x*d /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f1275)
                        yield 0, subst2
                subjects.appendleft(tmp2)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i3.1.2.1.0', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 110737
            if len(subjects) >= 1 and isinstance(subjects[0], Pow):
                tmp5 = subjects.popleft()
                subjects6 = deque(tmp5._args)
                # State 110738
                if len(subjects6) >= 1:
                    tmp7 = subjects6.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i3.1.2.1.1', tmp7)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 110739
                        if len(subjects6) >= 1 and subjects6[0] == Integer(2):
                            tmp9 = subjects6.popleft()
                            # State 110740
                            if len(subjects6) == 0:
                                pass
                                # State 110741
                                if len(subjects) == 0:
                                    pass
                                    # 2: d*x**2 /; (cons_f2) and (cons_f3) and (cons_f29) and (cons_f1767)
                                    yield 2, subst2
                                    # 4: d*x**2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29)
                                    yield 4, subst2
                            subjects6.appendleft(tmp9)
                    subjects6.appendleft(tmp7)
                subjects.appendleft(tmp5)
        if len(subjects) >= 1 and isinstance(subjects[0], Mul):
            tmp10 = subjects.popleft()
            associative1 = tmp10
            associative_type1 = type(tmp10)
            subjects11 = deque(tmp10._args)
            matcher = CommutativeMatcher110400.get()
            tmp12 = subjects11
            subjects11 = []
            for s in tmp12:
                matcher.add_subject(s)
            for pattern_index, subst1 in matcher.match(tmp12, subst0):
                pass
                if pattern_index == 0:
                    pass
                    # State 110401
                    if len(subjects) == 0:
                        pass
                        # 0: x*d /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f1275)
                        yield 0, subst1
                if pattern_index == 1:
                    pass
                    # State 110746
                    if len(subjects) == 0:
                        pass
                        # 2: d*x**2 /; (cons_f2) and (cons_f3) and (cons_f29) and (cons_f1767)
                        yield 2, subst1
                        # 4: d*x**2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29)
                        yield 4, subst1
            subjects.appendleft(tmp10)
        if len(subjects) >= 1 and subjects[0] == Integer(1):
            tmp13 = subjects.popleft()
            # State 110736
            if len(subjects) == 0:
                pass
                # 1: 1
                yield 1, subst0
            subjects.appendleft(tmp13)
        if len(subjects) >= 1 and subjects[0] == Integer(-1):
            tmp14 = subjects.popleft()
            # State 110803
            if len(subjects) == 0:
                pass
                # 3: -1
                yield 3, subst0
            subjects.appendleft(tmp14)
        return
        yield


from matchpy.matching.many_to_one import CommutativeMatcher
from collections import deque
from .generated_part009169 import *
from matchpy.utils import VariableWithCount
from multiset import Multiset