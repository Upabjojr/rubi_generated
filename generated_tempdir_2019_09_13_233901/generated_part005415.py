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

class CommutativeMatcher58369(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({0: 1}), [
      (VariableWithCount('i2.2.1.2.0', 1, 1, S(0)), Add)
]),
    1: (1, Multiset({1: 1}), [
      (VariableWithCount('i2.2.2.0', 1, 1, S(0)), Add)
]),
    2: (2, Multiset({2: 1}), [
      (VariableWithCount('i2.2.3.0', 1, 1, S(0)), Add)
]),
    3: (3, Multiset({3: 1}), [
      (VariableWithCount('i2.2.2.2.0', 1, 1, S(0)), Add)
]),
    4: (4, Multiset({4: 1}), [
      (VariableWithCount('i2.2.1.3.0', 1, 1, S(0)), Add)
]),
    5: (5, Multiset({5: 1}), [
      (VariableWithCount('i2.4.0', 1, 1, S(0)), Add)
]),
    6: (6, Multiset({6: 1}), [
      (VariableWithCount('i2.2.1.2.0', 1, 1, S(0)), Add)
]),
    7: (7, Multiset({7: 1}), [
      (VariableWithCount('i2.2.1.2.0', 1, 1, S(0)), Add)
]),
    8: (8, Multiset({8: 1}), [
      (VariableWithCount('i2.2.1.2.0', 1, 1, S(0)), Add)
]),
    9: (9, Multiset({9: 1}), [
      (VariableWithCount('i2.2.1.2.0', 1, 1, S(0)), Add)
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
        if CommutativeMatcher58369._instance is None:
            CommutativeMatcher58369._instance = CommutativeMatcher58369()
        return CommutativeMatcher58369._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 58368
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.2.1.0_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 58370
            if len(subjects) >= 1:
                tmp2 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.1.0', tmp2)
                except ValueError:
                    pass
                else:
                    pass
                    # State 58371
                    if len(subjects) == 0:
                        pass
                        # 0: x*d
                subjects.appendleft(tmp2)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.2.1.0_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 58646
            if len(subjects) >= 1:
                tmp5 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.2.1.0', tmp5)
                except ValueError:
                    pass
                else:
                    pass
                    # State 58647
                    if len(subjects) == 0:
                        pass
                        # 1: x*f
                subjects.appendleft(tmp5)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.3.1.0_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 59068
            if len(subjects) >= 1:
                tmp8 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.3.1.0', tmp8)
                except ValueError:
                    pass
                else:
                    pass
                    # State 59069
                    if len(subjects) == 0:
                        pass
                        # 2: x*f
                subjects.appendleft(tmp8)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.2.2.1.0_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 61574
            if len(subjects) >= 1:
                tmp11 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.2.2.1.0', tmp11)
                except ValueError:
                    pass
                else:
                    pass
                    # State 61575
                    if len(subjects) == 0:
                        pass
                        # 3: x*f
                subjects.appendleft(tmp11)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.3.1.0_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 61966
            if len(subjects) >= 1:
                tmp14 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.3.1.0', tmp14)
                except ValueError:
                    pass
                else:
                    pass
                    # State 61967
                    if len(subjects) == 0:
                        pass
                        # 4: x*f
                subjects.appendleft(tmp14)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.4.1.0_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 64740
            if len(subjects) >= 1:
                tmp17 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.4.1.0', tmp17)
                except ValueError:
                    pass
                else:
                    pass
                    # State 64741
                    if len(subjects) == 0:
                        pass
                        # 5: x*f
                subjects.appendleft(tmp17)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.2.1.0', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 72191
            if len(subjects) >= 1:
                tmp20 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.0', tmp20)
                except ValueError:
                    pass
                else:
                    pass
                    # State 72192
                    if len(subjects) == 0:
                        pass
                        # 6: x*f
                subjects.appendleft(tmp20)
            if len(subjects) >= 1 and isinstance(subjects[0], Pow):
                tmp22 = subjects.popleft()
                subjects23 = deque(tmp22._args)
                # State 73823
                if len(subjects23) >= 1:
                    tmp24 = subjects23.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.2.1.1', tmp24)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 73824
                        if len(subjects23) >= 1:
                            tmp26 = subjects23.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.2.1.2', tmp26)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 73825
                                if len(subjects23) == 0:
                                    pass
                                    # State 73826
                                    if len(subjects) == 0:
                                        pass
                                        # 7: d*x**n
                            subjects23.appendleft(tmp26)
                    subjects23.appendleft(tmp24)
                if len(subjects23) >= 1:
                    tmp28 = subjects23.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.0_1', tmp28)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 74266
                        if len(subjects23) >= 1:
                            tmp30 = subjects23.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.2.1.2', tmp30)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 74267
                                if len(subjects23) == 0:
                                    pass
                                    # State 74268
                                    if len(subjects) == 0:
                                        pass
                                        # 8: x**n*d
                            subjects23.appendleft(tmp30)
                    subjects23.appendleft(tmp28)
                if len(subjects23) >= 1:
                    tmp32 = subjects23.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.0', tmp32)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 74840
                        if len(subjects23) >= 1:
                            tmp34 = subjects23.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.2.1.2', tmp34)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 74841
                                if len(subjects23) == 0:
                                    pass
                                    # State 74842
                                    if len(subjects) == 0:
                                        pass
                                        # 9: x**n*d
                            subjects23.appendleft(tmp34)
                    subjects23.appendleft(tmp32)
                subjects.appendleft(tmp22)
        if len(subjects) >= 1 and isinstance(subjects[0], Mul):
            tmp36 = subjects.popleft()
            associative1 = tmp36
            associative_type1 = type(tmp36)
            subjects37 = deque(tmp36._args)
            matcher = CommutativeMatcher58373.get()
            tmp38 = subjects37
            subjects37 = []
            for s in tmp38:
                matcher.add_subject(s)
            for pattern_index, subst1 in matcher.match(tmp38, subst0):
                pass
                if pattern_index == 0:
                    pass
                    # State 58374
                    if len(subjects) == 0:
                        pass
                        # 0: x*d
                if pattern_index == 1:
                    pass
                    # State 58648
                    if len(subjects) == 0:
                        pass
                        # 1: x*f
                if pattern_index == 2:
                    pass
                    # State 59070
                    if len(subjects) == 0:
                        pass
                        # 2: x*f
                if pattern_index == 3:
                    pass
                    # State 61576
                    if len(subjects) == 0:
                        pass
                        # 3: x*f
                if pattern_index == 4:
                    pass
                    # State 61968
                    if len(subjects) == 0:
                        pass
                        # 4: x*f
                if pattern_index == 5:
                    pass
                    # State 64742
                    if len(subjects) == 0:
                        pass
                        # 5: x*f
                if pattern_index == 6:
                    pass
                    # State 72193
                    if len(subjects) == 0:
                        pass
                        # 6: x*f
                if pattern_index == 7:
                    pass
                    # State 73831
                    if len(subjects) == 0:
                        pass
                        # 7: d*x**n
                if pattern_index == 8:
                    pass
                    # State 74272
                    if len(subjects) == 0:
                        pass
                        # 8: x**n*d
                if pattern_index == 9:
                    pass
                    # State 74846
                    if len(subjects) == 0:
                        pass
                        # 9: x**n*d
            subjects.appendleft(tmp36)
        return
        yield


from matchpy.utils import VariableWithCount
from matchpy.matching.many_to_one import CommutativeMatcher
from multiset import Multiset
from collections import deque
