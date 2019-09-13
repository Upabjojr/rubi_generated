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

class CommutativeMatcher125353(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({0: 1}), [
      (VariableWithCount('i2.3.0', 1, 1, S(0)), Add)
]),
    1: (1, Multiset({1: 1}), [
      (VariableWithCount('i2.3.0', 1, 1, S(0)), Add)
]),
    2: (2, Multiset({2: 1}), [
      (VariableWithCount('i2.2.1.2.0', 1, 1, S(0)), Add)
]),
    3: (3, Multiset({3: 1}), [
      (VariableWithCount('i2.3.0_1', 1, 1, S(0)), Add)
]),
    4: (4, Multiset({4: 1}), [
      (VariableWithCount('i2.3.0', 1, 1, S(0)), Add)
]),
    5: (5, Multiset({5: 1}), [
      (VariableWithCount('i2.3.0', 1, 1, S(0)), Add)
]),
    6: (6, Multiset({6: 1}), [
      (VariableWithCount('i2.3.0', 1, 1, S(0)), Add)
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
        if CommutativeMatcher125353._instance is None:
            CommutativeMatcher125353._instance = CommutativeMatcher125353()
        return CommutativeMatcher125353._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 125352
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.3.1.0', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 125354
            subst2 = Substitution(subst1)
            try:
                subst2.try_add_variable('i2.3.1.2', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 125355
                if len(subjects) >= 1:
                    tmp3 = subjects.popleft()
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.1', tmp3)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 125356
                        if len(subjects) == 0:
                            pass
                            # 0: x**n*b
                    subjects.appendleft(tmp3)
            if len(subjects) >= 1:
                tmp5 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.0', tmp5)
                except ValueError:
                    pass
                else:
                    pass
                    # State 131947
                    if len(subjects) == 0:
                        pass
                        # 1: x*b
                subjects.appendleft(tmp5)
            if len(subjects) >= 1 and isinstance(subjects[0], Pow):
                tmp7 = subjects.popleft()
                subjects8 = deque(tmp7._args)
                # State 125357
                if len(subjects8) >= 1:
                    tmp9 = subjects8.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.1', tmp9)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 125358
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.3.1.2', 1)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 125359
                            if len(subjects8) == 0:
                                pass
                                # State 125360
                                if len(subjects) == 0:
                                    pass
                                    # 0: x**n*b
                        if len(subjects8) >= 1:
                            tmp12 = subjects8.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.3.1.2', tmp12)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 125359
                                if len(subjects8) == 0:
                                    pass
                                    # State 125360
                                    if len(subjects) == 0:
                                        pass
                                        # 0: x**n*b
                            subjects8.appendleft(tmp12)
                    subjects8.appendleft(tmp9)
                if len(subjects8) >= 1 and isinstance(subjects8[0], Add):
                    tmp14 = subjects8.popleft()
                    associative1 = tmp14
                    associative_type1 = type(tmp14)
                    subjects15 = deque(tmp14._args)
                    matcher = CommutativeMatcher136947.get()
                    tmp16 = subjects15
                    subjects15 = []
                    for s in tmp16:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp16, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 136953
                            if len(subjects8) >= 1:
                                tmp17 = []
                                tmp17.append(subjects8.popleft())
                                while True:
                                    if len(tmp17) > 1:
                                        tmp18 = create_operation_expression(associative1, tmp17)
                                    elif len(tmp17) == 1:
                                        tmp18 = tmp17[0]
                                    else:
                                        assert False, "Unreachable"
                                    subst3 = Substitution(subst2)
                                    try:
                                        subst3.try_add_variable('i2.3.1.2', tmp18)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 136954
                                        if len(subjects8) == 0:
                                            pass
                                            # State 136955
                                            if len(subjects) == 0:
                                                pass
                                                # 5: b*(x*d + c)**n
                                    if len(subjects8) == 0:
                                        break
                                    tmp17.append(subjects8.popleft())
                                subjects8.extendleft(reversed(tmp17))
                    subjects8.appendleft(tmp14)
                subjects.appendleft(tmp7)
            if len(subjects) >= 1 and isinstance(subjects[0], log):
                tmp20 = subjects.popleft()
                subjects21 = deque(tmp20._args)
                # State 134312
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.3.1.2.0', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 134313
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.3.1.2.2', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 134314
                        if len(subjects21) >= 1:
                            tmp24 = subjects21.popleft()
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i2.1', tmp24)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 134315
                                if len(subjects21) == 0:
                                    pass
                                    # State 134316
                                    if len(subjects) == 0:
                                        pass
                                        # 4: b*log(x**n*c)
                            subjects21.appendleft(tmp24)
                    if len(subjects21) >= 1 and isinstance(subjects21[0], Pow):
                        tmp26 = subjects21.popleft()
                        subjects27 = deque(tmp26._args)
                        # State 134317
                        if len(subjects27) >= 1:
                            tmp28 = subjects27.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.1', tmp28)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 134318
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.3.1.2.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 134319
                                    if len(subjects27) == 0:
                                        pass
                                        # State 134320
                                        if len(subjects21) == 0:
                                            pass
                                            # State 134321
                                            if len(subjects) == 0:
                                                pass
                                                # 4: b*log(x**n*c)
                                if len(subjects27) >= 1:
                                    tmp31 = subjects27.popleft()
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i2.3.1.2.2', tmp31)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 134319
                                        if len(subjects27) == 0:
                                            pass
                                            # State 134320
                                            if len(subjects21) == 0:
                                                pass
                                                # State 134321
                                                if len(subjects) == 0:
                                                    pass
                                                    # 4: b*log(x**n*c)
                                    subjects27.appendleft(tmp31)
                            subjects27.appendleft(tmp28)
                        subjects21.appendleft(tmp26)
                if len(subjects21) >= 1 and isinstance(subjects21[0], Mul):
                    tmp33 = subjects21.popleft()
                    associative1 = tmp33
                    associative_type1 = type(tmp33)
                    subjects34 = deque(tmp33._args)
                    matcher = CommutativeMatcher134323.get()
                    tmp35 = subjects34
                    subjects34 = []
                    for s in tmp35:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp35, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 134330
                            if len(subjects21) == 0:
                                pass
                                # State 134331
                                if len(subjects) == 0:
                                    pass
                                    # 4: b*log(x**n*c)
                    subjects21.appendleft(tmp33)
                subjects.appendleft(tmp20)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.2.1.0_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 132755
            if len(subjects) >= 1:
                tmp37 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.1.0', tmp37)
                except ValueError:
                    pass
                else:
                    pass
                    # State 132756
                    if len(subjects) == 0:
                        pass
                        # 2: x*d
                subjects.appendleft(tmp37)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.3.1.0_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 132880
            if len(subjects) >= 1:
                tmp40 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.3.1.1.0', tmp40)
                except ValueError:
                    pass
                else:
                    pass
                    # State 132881
                    if len(subjects) == 0:
                        pass
                        # 3: e*x
                subjects.appendleft(tmp40)
            if len(subjects) >= 1:
                tmp42 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.3.1.0', tmp42)
                except ValueError:
                    pass
                else:
                    pass
                    # State 137524
                    if len(subjects) == 0:
                        pass
                        # 6: x*e
                subjects.appendleft(tmp42)
        if len(subjects) >= 1 and isinstance(subjects[0], Mul):
            tmp44 = subjects.popleft()
            associative1 = tmp44
            associative_type1 = type(tmp44)
            subjects45 = deque(tmp44._args)
            matcher = CommutativeMatcher125362.get()
            tmp46 = subjects45
            subjects45 = []
            for s in tmp46:
                matcher.add_subject(s)
            for pattern_index, subst1 in matcher.match(tmp46, subst0):
                pass
                if pattern_index == 0:
                    pass
                    # State 125369
                    if len(subjects) == 0:
                        pass
                        # 0: x**n*b
                if pattern_index == 1:
                    pass
                    # State 131948
                    if len(subjects) == 0:
                        pass
                        # 1: x*b
                if pattern_index == 2:
                    pass
                    # State 132757
                    if len(subjects) == 0:
                        pass
                        # 2: x*d
                if pattern_index == 3:
                    pass
                    # State 132882
                    if len(subjects) == 0:
                        pass
                        # 3: e*x
                if pattern_index == 4:
                    pass
                    # State 134352
                    if len(subjects) == 0:
                        pass
                        # 4: b*log(x**n*c)
                if pattern_index == 5:
                    pass
                    # State 136966
                    if len(subjects) == 0:
                        pass
                        # 5: b*(x*d + c)**n
                if pattern_index == 6:
                    pass
                    # State 137525
                    if len(subjects) == 0:
                        pass
                        # 6: x*e
            subjects.appendleft(tmp44)
        return
        yield


from matchpy.utils import VariableWithCount
from matchpy.matching.many_to_one import CommutativeMatcher
from multiset import Multiset
from collections import deque
