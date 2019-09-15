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


class CommutativeMatcher89883(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({0: 1}), [
      (VariableWithCount('i5.0', 1, 1, S(0)), Add)
]),
    1: (1, Multiset({1: 1}), [
      (VariableWithCount('i5.0', 1, 1, S(0)), Add)
]),
    2: (2, Multiset({2: 1}), [
      (VariableWithCount('i5.0', 1, 1, S(0)), Add)
]),
    3: (3, Multiset({3: 1}), [
      (VariableWithCount('i5.0', 1, 1, S(0)), Add)
]),
    4: (4, Multiset({4: 1}), [
      (VariableWithCount('i5.0', 1, 1, S(0)), Add)
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
        if CommutativeMatcher89883._instance is None:
            CommutativeMatcher89883._instance = CommutativeMatcher89883()
        return CommutativeMatcher89883._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 89882
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i5.1.0_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 89884
            if len(subjects) >= 1:
                tmp2 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i5.1.0', tmp2)
                except ValueError:
                    pass
                else:
                    pass
                    # State 89885
                    if len(subjects) == 0:
                        pass
                        # 0: x*d /; (cons_f8) and (cons_f29)
                        yield 0, subst2
                subjects.appendleft(tmp2)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i5.1.0', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 105670
            if len(subjects) >= 1 and isinstance(subjects[0], log):
                tmp5 = subjects.popleft()
                subjects6 = deque(tmp5._args)
                # State 105671
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i5.1.2.0', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 105672
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i5.1.2.2', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 105673
                        if len(subjects6) >= 1:
                            tmp9 = subjects6.popleft()
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i5.1.2.1', tmp9)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 105674
                                if len(subjects6) == 0:
                                    pass
                                    # State 105675
                                    if len(subjects) == 0:
                                        pass
                                        # 1: b*log(c*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f1721)
                                        yield 1, subst4
                                        # 2: b*log(c*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f1723)
                                        yield 2, subst4
                                        # 3: b*log(c*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f1713)
                                        yield 3, subst4
                                        # 4: b*log(c*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f1713)
                                        yield 4, subst4
                            subjects6.appendleft(tmp9)
                    if len(subjects6) >= 1 and isinstance(subjects6[0], Pow):
                        tmp11 = subjects6.popleft()
                        subjects12 = deque(tmp11._args)
                        # State 105676
                        if len(subjects12) >= 1:
                            tmp13 = subjects12.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i5.1.2.1', tmp13)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 105677
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i5.1.2.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 105678
                                    if len(subjects12) == 0:
                                        pass
                                        # State 105679
                                        if len(subjects6) == 0:
                                            pass
                                            # State 105680
                                            if len(subjects) == 0:
                                                pass
                                                # 1: b*log(c*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f1721)
                                                yield 1, subst4
                                                # 2: b*log(c*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f1723)
                                                yield 2, subst4
                                                # 3: b*log(c*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f1713)
                                                yield 3, subst4
                                                # 4: b*log(c*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f1713)
                                                yield 4, subst4
                                if len(subjects12) >= 1:
                                    tmp16 = subjects12.popleft()
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i5.1.2.2', tmp16)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 105678
                                        if len(subjects12) == 0:
                                            pass
                                            # State 105679
                                            if len(subjects6) == 0:
                                                pass
                                                # State 105680
                                                if len(subjects) == 0:
                                                    pass
                                                    # 1: b*log(c*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f1721)
                                                    yield 1, subst4
                                                    # 2: b*log(c*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f1723)
                                                    yield 2, subst4
                                                    # 3: b*log(c*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f1713)
                                                    yield 3, subst4
                                                    # 4: b*log(c*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f1713)
                                                    yield 4, subst4
                                    subjects12.appendleft(tmp16)
                            subjects12.appendleft(tmp13)
                        subjects6.appendleft(tmp11)
                if len(subjects6) >= 1 and isinstance(subjects6[0], Mul):
                    tmp18 = subjects6.popleft()
                    associative1 = tmp18
                    associative_type1 = type(tmp18)
                    subjects19 = deque(tmp18._args)
                    matcher = CommutativeMatcher105682.get()
                    tmp20 = subjects19
                    subjects19 = []
                    for s in tmp20:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp20, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 105689
                            if len(subjects6) == 0:
                                pass
                                # State 105690
                                if len(subjects) == 0:
                                    pass
                                    # 1: b*log(c*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f1721)
                                    yield 1, subst2
                                    # 2: b*log(c*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f1723)
                                    yield 2, subst2
                                    # 3: b*log(c*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f1713)
                                    yield 3, subst2
                                    # 4: b*log(c*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f1713)
                                    yield 4, subst2
                    subjects6.appendleft(tmp18)
                subjects.appendleft(tmp5)
        if len(subjects) >= 1 and isinstance(subjects[0], Mul):
            tmp21 = subjects.popleft()
            associative1 = tmp21
            associative_type1 = type(tmp21)
            subjects22 = deque(tmp21._args)
            matcher = CommutativeMatcher89887.get()
            tmp23 = subjects22
            subjects22 = []
            for s in tmp23:
                matcher.add_subject(s)
            for pattern_index, subst1 in matcher.match(tmp23, subst0):
                pass
                if pattern_index == 0:
                    pass
                    # State 89888
                    if len(subjects) == 0:
                        pass
                        # 0: x*d /; (cons_f8) and (cons_f29)
                        yield 0, subst1
                if pattern_index == 1:
                    pass
                    # State 105711
                    if len(subjects) == 0:
                        pass
                        # 1: b*log(c*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f1721)
                        yield 1, subst1
                        # 2: b*log(c*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f1723)
                        yield 2, subst1
                        # 3: b*log(c*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f1713)
                        yield 3, subst1
                        # 4: b*log(c*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f1713)
                        yield 4, subst1
            subjects.appendleft(tmp21)
        return
        yield


from matchpy.matching.many_to_one import CommutativeMatcher
from collections import deque
from .generated_part009897 import *
from .generated_part009896 import *
from matchpy.utils import VariableWithCount
from multiset import Multiset