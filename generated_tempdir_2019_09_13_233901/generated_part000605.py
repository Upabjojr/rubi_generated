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

class CommutativeMatcher42551(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({0: 1}), [
      (VariableWithCount('i2.2.1.2.2.0', 1, 1, S(1)), Mul)
]),
    1: (1, Multiset({1: 1}), [
      (VariableWithCount('i2.2.1.2.2.0', 1, 1, S(1)), Mul)
]),
    2: (2, Multiset({2: 1}), [
      (VariableWithCount('i2.2.1.2.2.0', 1, 1, S(1)), Mul)
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
        if CommutativeMatcher42551._instance is None:
            CommutativeMatcher42551._instance = CommutativeMatcher42551()
        return CommutativeMatcher42551._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 42550
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.2.2.2', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 42552
            if len(subjects) >= 1 and isinstance(subjects[0], Add):
                tmp2 = subjects.popleft()
                associative1 = tmp2
                associative_type1 = type(tmp2)
                subjects3 = deque(tmp2._args)
                matcher = CommutativeMatcher42554.get()
                tmp4 = subjects3
                subjects3 = []
                for s in tmp4:
                    matcher.add_subject(s)
                for pattern_index, subst2 in matcher.match(tmp4, subst1):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 42570
                        if len(subjects) == 0:
                            pass
                            # 0: (e + f*x + g*x**2)**p
                    if pattern_index == 1:
                        pass
                        # State 54630
                        if len(subjects) == 0:
                            pass
                            # 2: (e + x*f)**p
                subjects.appendleft(tmp2)
            if len(subjects) >= 1:
                tmp5 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.2.1', tmp5)
                except ValueError:
                    pass
                else:
                    pass
                    # State 45237
                    if len(subjects) == 0:
                        pass
                        # 1: v**p
                subjects.appendleft(tmp5)
            subst2 = Substitution(subst1)
            try:
                subst2.try_add_variable('i2.2.1.2.2.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 54622
                subst3 = Substitution(subst2)
                try:
                    subst3.try_add_variable('i2.2.1.2.2.2.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 54623
                    if len(subjects) >= 1:
                        tmp9 = subjects.popleft()
                        subst4 = Substitution(subst3)
                        try:
                            subst4.try_add_variable('i2.2.1.2.2.2.1.0', tmp9)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 54624
                            if len(subjects) == 0:
                                pass
                                # 2: (e + x*f)**p
                        subjects.appendleft(tmp9)
                if len(subjects) >= 1 and isinstance(subjects[0], Mul):
                    tmp11 = subjects.popleft()
                    associative1 = tmp11
                    associative_type1 = type(tmp11)
                    subjects12 = deque(tmp11._args)
                    matcher = CommutativeMatcher54626.get()
                    tmp13 = subjects12
                    subjects12 = []
                    for s in tmp13:
                        matcher.add_subject(s)
                    for pattern_index, subst3 in matcher.match(tmp13, subst2):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 54627
                            if len(subjects) == 0:
                                pass
                                # 2: (e + x*f)**p
                    subjects.appendleft(tmp11)
        if len(subjects) >= 1 and isinstance(subjects[0], Pow):
            tmp14 = subjects.popleft()
            subjects15 = deque(tmp14._args)
            # State 42571
            if len(subjects15) >= 1 and isinstance(subjects15[0], Add):
                tmp16 = subjects15.popleft()
                associative1 = tmp16
                associative_type1 = type(tmp16)
                subjects17 = deque(tmp16._args)
                matcher = CommutativeMatcher42573.get()
                tmp18 = subjects17
                subjects17 = []
                for s in tmp18:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp18, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 42589
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.1.2.2.2', 1)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 42590
                            if len(subjects15) == 0:
                                pass
                                # State 42591
                                if len(subjects) == 0:
                                    pass
                                    # 0: (e + f*x + g*x**2)**p
                        if len(subjects15) >= 1:
                            tmp20 = []
                            tmp20.append(subjects15.popleft())
                            while True:
                                if len(tmp20) > 1:
                                    tmp21 = create_operation_expression(associative1, tmp20)
                                elif len(tmp20) == 1:
                                    tmp21 = tmp20[0]
                                else:
                                    assert False, "Unreachable"
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i2.2.1.2.2.2', tmp21)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 42590
                                    if len(subjects15) == 0:
                                        pass
                                        # State 42591
                                        if len(subjects) == 0:
                                            pass
                                            # 0: (e + f*x + g*x**2)**p
                                if len(subjects15) == 0:
                                    break
                                tmp20.append(subjects15.popleft())
                            subjects15.extendleft(reversed(tmp20))
                    if pattern_index == 1:
                        pass
                        # State 54643
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.1.2.2.2', 1)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 54644
                            if len(subjects15) == 0:
                                pass
                                # State 54645
                                if len(subjects) == 0:
                                    pass
                                    # 2: (e + x*f)**p
                        if len(subjects15) >= 1:
                            tmp24 = []
                            tmp24.append(subjects15.popleft())
                            while True:
                                if len(tmp24) > 1:
                                    tmp25 = create_operation_expression(associative1, tmp24)
                                elif len(tmp24) == 1:
                                    tmp25 = tmp24[0]
                                else:
                                    assert False, "Unreachable"
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i2.2.1.2.2.2', tmp25)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 54644
                                    if len(subjects15) == 0:
                                        pass
                                        # State 54645
                                        if len(subjects) == 0:
                                            pass
                                            # 2: (e + x*f)**p
                                if len(subjects15) == 0:
                                    break
                                tmp24.append(subjects15.popleft())
                            subjects15.extendleft(reversed(tmp24))
                subjects15.appendleft(tmp16)
            if len(subjects15) >= 1:
                tmp27 = subjects15.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.1.2.2.1', tmp27)
                except ValueError:
                    pass
                else:
                    pass
                    # State 45238
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.2.2.2', 1)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 45239
                        if len(subjects15) == 0:
                            pass
                            # State 45240
                            if len(subjects) == 0:
                                pass
                                # 1: v**p
                    if len(subjects15) >= 1:
                        tmp30 = subjects15.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.1.2.2.2', tmp30)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 45239
                            if len(subjects15) == 0:
                                pass
                                # State 45240
                                if len(subjects) == 0:
                                    pass
                                    # 1: v**p
                        subjects15.appendleft(tmp30)
                subjects15.appendleft(tmp27)
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.2.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 54631
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.2.2.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 54632
                    if len(subjects15) >= 1:
                        tmp34 = subjects15.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.2.2.2.1.0', tmp34)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 54633
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i2.2.1.2.2.2', 1)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 54634
                                if len(subjects15) == 0:
                                    pass
                                    # State 54635
                                    if len(subjects) == 0:
                                        pass
                                        # 2: (e + x*f)**p
                            if len(subjects15) >= 1:
                                tmp37 = subjects15.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.2.1.2.2.2', tmp37)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 54634
                                    if len(subjects15) == 0:
                                        pass
                                        # State 54635
                                        if len(subjects) == 0:
                                            pass
                                            # 2: (e + x*f)**p
                                subjects15.appendleft(tmp37)
                        subjects15.appendleft(tmp34)
                if len(subjects15) >= 1 and isinstance(subjects15[0], Mul):
                    tmp39 = subjects15.popleft()
                    associative1 = tmp39
                    associative_type1 = type(tmp39)
                    subjects40 = deque(tmp39._args)
                    matcher = CommutativeMatcher54637.get()
                    tmp41 = subjects40
                    subjects40 = []
                    for s in tmp41:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp41, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 54638
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.2.2.2', 1)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 54639
                                if len(subjects15) == 0:
                                    pass
                                    # State 54640
                                    if len(subjects) == 0:
                                        pass
                                        # 2: (e + x*f)**p
                            if len(subjects15) >= 1:
                                tmp43 = []
                                tmp43.append(subjects15.popleft())
                                while True:
                                    if len(tmp43) > 1:
                                        tmp44 = create_operation_expression(associative1, tmp43)
                                    elif len(tmp43) == 1:
                                        tmp44 = tmp43[0]
                                    else:
                                        assert False, "Unreachable"
                                    subst3 = Substitution(subst2)
                                    try:
                                        subst3.try_add_variable('i2.2.1.2.2.2', tmp44)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 54639
                                        if len(subjects15) == 0:
                                            pass
                                            # State 54640
                                            if len(subjects) == 0:
                                                pass
                                                # 2: (e + x*f)**p
                                    if len(subjects15) == 0:
                                        break
                                    tmp43.append(subjects15.popleft())
                                subjects15.extendleft(reversed(tmp43))
                    subjects15.appendleft(tmp39)
            subjects.appendleft(tmp14)
        return
        yield


from matchpy.utils import VariableWithCount
from matchpy.matching.many_to_one import CommutativeMatcher
from multiset import Multiset
from collections import deque
