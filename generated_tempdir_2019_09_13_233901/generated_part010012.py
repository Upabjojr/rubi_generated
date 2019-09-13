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

class CommutativeMatcher57814(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({0: 1}), [
      (VariableWithCount('i4.0', 1, 1, S(0)), Add)
]),
    1: (1, Multiset({1: 1}), [
      (VariableWithCount('i4.0', 1, 1, S(0)), Add)
]),
    2: (2, Multiset({2: 1, 3: 1}), [
      (VariableWithCount('i4.0', 1, 1, S(0)), Add)
]),
    3: (3, Multiset({4: 1}), [
      (VariableWithCount('i4.0', 1, 1, S(0)), Add)
]),
    4: (4, Multiset({5: 1}), [
      (VariableWithCount('i4.0', 1, 1, S(0)), Add)
]),
    5: (5, Multiset({6: 1}), [
      (VariableWithCount('i4.0', 1, 1, S(0)), Add)
]),
    6: (6, Multiset({7: 1}), [
      (VariableWithCount('i4.0', 1, 1, S(0)), Add)
]),
    7: (7, Multiset({8: 1}), [
      (VariableWithCount('i4.0', 1, 1, S(0)), Add)
]),
    8: (8, Multiset({9: 1}), [
      (VariableWithCount('i4.0', 1, 1, S(0)), Add)
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
        if CommutativeMatcher57814._instance is None:
            CommutativeMatcher57814._instance = CommutativeMatcher57814()
        return CommutativeMatcher57814._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 57813
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i4.1.0_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 57815
            if len(subjects) >= 1:
                tmp2 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i4.1.0', tmp2)
                except ValueError:
                    pass
                else:
                    pass
                    # State 57816
                    if len(subjects) == 0:
                        pass
                        # 0: x*b /; (cons_f8) and (cons_f29)
                        # 1: x*b /; (cons_f8) and (cons_f29) and (cons_f1263)
                subjects.appendleft(tmp2)
            if len(subjects) >= 1:
                tmp4 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i4.1.1', tmp4)
                except ValueError:
                    pass
                else:
                    pass
                    # State 75678
                    if len(subjects) == 0:
                        pass
                        # 3: b*x /; (cons_f2) and (cons_f3) and (cons_f8)
                subjects.appendleft(tmp4)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i4.1.0', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 75668
            if len(subjects) >= 1 and isinstance(subjects[0], Pow):
                tmp7 = subjects.popleft()
                subjects8 = deque(tmp7._args)
                # State 75669
                if len(subjects8) >= 1:
                    tmp9 = subjects8.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i4.1.1', tmp9)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 75670
                        if len(subjects8) >= 1 and subjects8[0] == 2:
                            tmp11 = subjects8.popleft()
                            # State 75671
                            if len(subjects8) == 0:
                                pass
                                # State 75672
                                if len(subjects) == 0:
                                    pass
                                    # 2: c*x**2 /; (cons_f2) and (cons_f3) and (cons_f8)
                            subjects8.appendleft(tmp11)
                    subjects8.appendleft(tmp9)
                subjects.appendleft(tmp7)
            if len(subjects) >= 1 and isinstance(subjects[0], log):
                tmp12 = subjects.popleft()
                subjects13 = deque(tmp12._args)
                # State 104313
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i4.1.2.0', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 104314
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i4.1.2.2', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 104315
                        if len(subjects13) >= 1:
                            tmp16 = subjects13.popleft()
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i4.1.2.1', tmp16)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 104316
                                if len(subjects13) == 0:
                                    pass
                                    # State 104317
                                    if len(subjects) == 0:
                                        pass
                                        # 4: b*log(c*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f1710)
                                        # 5: b*log(c*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f1711)
                                        # 6: b*log(c*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f1713)
                                        # 7: b*log(c*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f1714)
                                        # 8: b*log(c*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f1713)
                                        # 9: b*log(c*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f1720)
                            subjects13.appendleft(tmp16)
                    if len(subjects13) >= 1 and isinstance(subjects13[0], Pow):
                        tmp18 = subjects13.popleft()
                        subjects19 = deque(tmp18._args)
                        # State 104318
                        if len(subjects19) >= 1:
                            tmp20 = subjects19.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i4.1.2.1', tmp20)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 104319
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i4.1.2.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 104320
                                    if len(subjects19) == 0:
                                        pass
                                        # State 104321
                                        if len(subjects13) == 0:
                                            pass
                                            # State 104322
                                            if len(subjects) == 0:
                                                pass
                                                # 4: b*log(c*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f1710)
                                                # 5: b*log(c*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f1711)
                                                # 6: b*log(c*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f1713)
                                                # 7: b*log(c*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f1714)
                                                # 8: b*log(c*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f1713)
                                                # 9: b*log(c*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f1720)
                                if len(subjects19) >= 1:
                                    tmp23 = subjects19.popleft()
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i4.1.2.2', tmp23)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 104320
                                        if len(subjects19) == 0:
                                            pass
                                            # State 104321
                                            if len(subjects13) == 0:
                                                pass
                                                # State 104322
                                                if len(subjects) == 0:
                                                    pass
                                                    # 4: b*log(c*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f1710)
                                                    # 5: b*log(c*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f1711)
                                                    # 6: b*log(c*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f1713)
                                                    # 7: b*log(c*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f1714)
                                                    # 8: b*log(c*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f1713)
                                                    # 9: b*log(c*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f1720)
                                    subjects19.appendleft(tmp23)
                            subjects19.appendleft(tmp20)
                        subjects13.appendleft(tmp18)
                if len(subjects13) >= 1 and isinstance(subjects13[0], Mul):
                    tmp25 = subjects13.popleft()
                    associative1 = tmp25
                    associative_type1 = type(tmp25)
                    subjects26 = deque(tmp25._args)
                    matcher = CommutativeMatcher104324.get()
                    tmp27 = subjects26
                    subjects26 = []
                    for s in tmp27:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp27, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 104331
                            if len(subjects13) == 0:
                                pass
                                # State 104332
                                if len(subjects) == 0:
                                    pass
                                    # 4: b*log(c*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f1710)
                                    # 5: b*log(c*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f1711)
                                    # 6: b*log(c*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f1713)
                                    # 7: b*log(c*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f1714)
                                    # 8: b*log(c*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f1713)
                                    # 9: b*log(c*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f1720)
                    subjects13.appendleft(tmp25)
                subjects.appendleft(tmp12)
        if len(subjects) >= 1 and isinstance(subjects[0], Mul):
            tmp28 = subjects.popleft()
            associative1 = tmp28
            associative_type1 = type(tmp28)
            subjects29 = deque(tmp28._args)
            matcher = CommutativeMatcher57818.get()
            tmp30 = subjects29
            subjects29 = []
            for s in tmp30:
                matcher.add_subject(s)
            for pattern_index, subst1 in matcher.match(tmp30, subst0):
                pass
                if pattern_index == 0:
                    pass
                    # State 57819
                    if len(subjects) == 0:
                        pass
                        # 0: x*b /; (cons_f8) and (cons_f29)
                        # 1: x*b /; (cons_f8) and (cons_f29) and (cons_f1263)
                if pattern_index == 1:
                    pass
                    # State 75677
                    if len(subjects) == 0:
                        pass
                        # 2: c*x**2 /; (cons_f2) and (cons_f3) and (cons_f8)
                if pattern_index == 2:
                    pass
                    # State 75679
                    if len(subjects) == 0:
                        pass
                        # 3: b*x /; (cons_f2) and (cons_f3) and (cons_f8)
                if pattern_index == 3:
                    pass
                    # State 104353
                    if len(subjects) == 0:
                        pass
                        # 4: b*log(c*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f1710)
                        # 5: b*log(c*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f1711)
                        # 6: b*log(c*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f1713)
                        # 7: b*log(c*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f1714)
                        # 8: b*log(c*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f1713)
                        # 9: b*log(c*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f1720)
            subjects.appendleft(tmp28)
        return
        yield


from matchpy.utils import VariableWithCount
from matchpy.matching.many_to_one import CommutativeMatcher
from multiset import Multiset
from collections import deque
