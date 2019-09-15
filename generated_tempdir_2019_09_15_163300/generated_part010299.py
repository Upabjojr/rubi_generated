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


class CommutativeMatcher57970(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({0: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    1: (1, Multiset({1: 1}), [
      (VariableWithCount('i3.0', 1, 1, None), Add)
]),
    2: (2, Multiset({2: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    3: (3, Multiset({3: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    4: (4, Multiset({4: 1, 5: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    5: (5, Multiset({6: 1, 7: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    6: (6, Multiset({8: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
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
        if CommutativeMatcher57970._instance is None:
            CommutativeMatcher57970._instance = CommutativeMatcher57970()
        return CommutativeMatcher57970._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 57969
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i3.1.0_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 57971
            if len(subjects) >= 1:
                tmp2 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i3.1.0', tmp2)
                except ValueError:
                    pass
                else:
                    pass
                    # State 57972
                    if len(subjects) == 0:
                        pass
                        # 0: x*b /; (cons_f8) and (cons_f8) and (cons_f1264)
                        yield 0, subst2
                subjects.appendleft(tmp2)
            if len(subjects) >= 1:
                tmp4 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i3.1.1', tmp4)
                except ValueError:
                    pass
                else:
                    pass
                    # State 75636
                    if len(subjects) == 0:
                        pass
                        # 5: b*x /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f47)
                        yield 5, subst2
                        # 7: b*x /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f228)
                        yield 7, subst2
                subjects.appendleft(tmp4)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i3.1.0', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 72573
            if len(subjects) >= 1 and isinstance(subjects[0], Pow):
                tmp7 = subjects.popleft()
                subjects8 = deque(tmp7._args)
                # State 72574
                if len(subjects8) >= 1:
                    tmp9 = subjects8.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i3.1.1', tmp9)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 72575
                        if len(subjects8) >= 1 and subjects8[0] == Integer(2):
                            tmp11 = subjects8.popleft()
                            # State 72576
                            if len(subjects8) == 0:
                                pass
                                # State 72577
                                if len(subjects) == 0:
                                    pass
                                    # 1: d*x**2 /; (cons_f8) and (cons_f29) and (cons_f1263)
                                    yield 1, subst2
                                    # 4: d*x**2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f47)
                                    yield 4, subst2
                                    # 6: d*x**2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f228)
                                    yield 6, subst2
                            subjects8.appendleft(tmp11)
                        if len(subjects8) >= 1:
                            tmp12 = subjects8.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i3.1.2', tmp12)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 72628
                                if len(subjects8) == 0:
                                    pass
                                    # State 72629
                                    if len(subjects) == 0:
                                        pass
                                        # 2: d*x**n /; (cons_f8) and (cons_f29) and (cons_f87) and (cons_f746)
                                        yield 2, subst3
                                        # 3: d*x**n /; (cons_f8) and (cons_f29) and (cons_f4) and (cons_f1500)
                                        yield 3, subst3
                            subjects8.appendleft(tmp12)
                    subjects8.appendleft(tmp9)
                subjects.appendleft(tmp7)
            if len(subjects) >= 1 and isinstance(subjects[0], log):
                tmp14 = subjects.popleft()
                subjects15 = deque(tmp14._args)
                # State 104779
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i3.1.2.0', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 104780
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i3.1.2.2', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 104781
                        if len(subjects15) >= 1:
                            tmp18 = subjects15.popleft()
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i3.1.2.1', tmp18)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 104782
                                if len(subjects15) == 0:
                                    pass
                                    # State 104783
                                    if len(subjects) == 0:
                                        pass
                                        # 8: b*log(c*RFx**p) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f1712)
                                        yield 8, subst4
                            subjects15.appendleft(tmp18)
                    if len(subjects15) >= 1 and isinstance(subjects15[0], Pow):
                        tmp20 = subjects15.popleft()
                        subjects21 = deque(tmp20._args)
                        # State 104784
                        if len(subjects21) >= 1:
                            tmp22 = subjects21.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i3.1.2.1', tmp22)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 104785
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i3.1.2.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 104786
                                    if len(subjects21) == 0:
                                        pass
                                        # State 104787
                                        if len(subjects15) == 0:
                                            pass
                                            # State 104788
                                            if len(subjects) == 0:
                                                pass
                                                # 8: b*log(c*RFx**p) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f1712)
                                                yield 8, subst4
                                if len(subjects21) >= 1:
                                    tmp25 = subjects21.popleft()
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i3.1.2.2', tmp25)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 104786
                                        if len(subjects21) == 0:
                                            pass
                                            # State 104787
                                            if len(subjects15) == 0:
                                                pass
                                                # State 104788
                                                if len(subjects) == 0:
                                                    pass
                                                    # 8: b*log(c*RFx**p) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f1712)
                                                    yield 8, subst4
                                    subjects21.appendleft(tmp25)
                            subjects21.appendleft(tmp22)
                        subjects15.appendleft(tmp20)
                if len(subjects15) >= 1 and isinstance(subjects15[0], Mul):
                    tmp27 = subjects15.popleft()
                    associative1 = tmp27
                    associative_type1 = type(tmp27)
                    subjects28 = deque(tmp27._args)
                    matcher = CommutativeMatcher104790.get()
                    tmp29 = subjects28
                    subjects28 = []
                    for s in tmp29:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp29, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 104797
                            if len(subjects15) == 0:
                                pass
                                # State 104798
                                if len(subjects) == 0:
                                    pass
                                    # 8: b*log(c*RFx**p) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f1712)
                                    yield 8, subst2
                    subjects15.appendleft(tmp27)
                subjects.appendleft(tmp14)
        if len(subjects) >= 1 and isinstance(subjects[0], Mul):
            tmp30 = subjects.popleft()
            associative1 = tmp30
            associative_type1 = type(tmp30)
            subjects31 = deque(tmp30._args)
            matcher = CommutativeMatcher57974.get()
            tmp32 = subjects31
            subjects31 = []
            for s in tmp32:
                matcher.add_subject(s)
            for pattern_index, subst1 in matcher.match(tmp32, subst0):
                pass
                if pattern_index == 0:
                    pass
                    # State 57975
                    if len(subjects) == 0:
                        pass
                        # 0: x*b /; (cons_f8) and (cons_f8) and (cons_f1264)
                        yield 0, subst1
                if pattern_index == 1:
                    pass
                    # State 72582
                    if len(subjects) == 0:
                        pass
                        # 1: d*x**2 /; (cons_f8) and (cons_f29) and (cons_f1263)
                        yield 1, subst1
                        # 4: d*x**2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f47)
                        yield 4, subst1
                        # 6: d*x**2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f228)
                        yield 6, subst1
                if pattern_index == 2:
                    pass
                    # State 72632
                    if len(subjects) == 0:
                        pass
                        # 2: d*x**n /; (cons_f8) and (cons_f29) and (cons_f87) and (cons_f746)
                        yield 2, subst1
                        # 3: d*x**n /; (cons_f8) and (cons_f29) and (cons_f4) and (cons_f1500)
                        yield 3, subst1
                if pattern_index == 3:
                    pass
                    # State 75637
                    if len(subjects) == 0:
                        pass
                        # 5: b*x /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f47)
                        yield 5, subst1
                        # 7: b*x /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f228)
                        yield 7, subst1
                if pattern_index == 4:
                    pass
                    # State 104819
                    if len(subjects) == 0:
                        pass
                        # 8: b*log(c*RFx**p) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f1712)
                        yield 8, subst1
            subjects.appendleft(tmp30)
        return
        yield


from .generated_part010300 import *
from .generated_part010301 import *
from matchpy.matching.many_to_one import CommutativeMatcher
from collections import deque
from matchpy.utils import VariableWithCount
from multiset import Multiset