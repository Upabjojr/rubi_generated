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


class CommutativeMatcher118098(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({0: 1}), [
      (VariableWithCount('i2.2.1.0_2', 1, 1, S(1)), Mul)
]),
    1: (1, Multiset({1: 1}), [
      (VariableWithCount('i2.2.1.0_2', 1, 1, S(1)), Mul)
]),
    2: (2, Multiset({2: 1}), [
      (VariableWithCount('i2.2.1.0_2', 1, 1, S(1)), Mul)
]),
    3: (3, Multiset({3: 1}), [
      (VariableWithCount('i2.2.1.0_2', 1, 1, S(1)), Mul)
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
        if CommutativeMatcher118098._instance is None:
            CommutativeMatcher118098._instance = CommutativeMatcher118098()
        return CommutativeMatcher118098._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 118097
        if len(subjects) >= 1 and isinstance(subjects[0], tan):
            tmp1 = subjects.popleft()
            subjects2 = deque(tmp1._args)
            # State 118099
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 118100
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.1.0', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 118101
                    if len(subjects2) >= 1:
                        tmp5 = subjects2.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.0', tmp5)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 118102
                            if len(subjects2) == 0:
                                pass
                                # State 118103
                                if len(subjects) == 0:
                                    pass
                                    # 0: tan(x*f + e)
                                    yield 0, subst3
                        subjects2.appendleft(tmp5)
                if len(subjects2) >= 1 and isinstance(subjects2[0], Mul):
                    tmp7 = subjects2.popleft()
                    associative1 = tmp7
                    associative_type1 = type(tmp7)
                    subjects8 = deque(tmp7._args)
                    matcher = CommutativeMatcher118105.get()
                    tmp9 = subjects8
                    subjects8 = []
                    for s in tmp9:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp9, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 118106
                            if len(subjects2) == 0:
                                pass
                                # State 118107
                                if len(subjects) == 0:
                                    pass
                                    # 0: tan(x*f + e)
                                    yield 0, subst2
                    subjects2.appendleft(tmp7)
            if len(subjects2) >= 1 and isinstance(subjects2[0], Add):
                tmp10 = subjects2.popleft()
                associative1 = tmp10
                associative_type1 = type(tmp10)
                subjects11 = deque(tmp10._args)
                matcher = CommutativeMatcher118109.get()
                tmp12 = subjects11
                subjects11 = []
                for s in tmp12:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp12, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 118115
                        if len(subjects2) == 0:
                            pass
                            # State 118116
                            if len(subjects) == 0:
                                pass
                                # 0: tan(x*f + e)
                                yield 0, subst1
                subjects2.appendleft(tmp10)
            subjects.appendleft(tmp1)
        if len(subjects) >= 1 and isinstance(subjects[0], Pow):
            tmp13 = subjects.popleft()
            subjects14 = deque(tmp13._args)
            # State 118300
            if len(subjects14) >= 1 and isinstance(subjects14[0], tan):
                tmp15 = subjects14.popleft()
                subjects16 = deque(tmp15._args)
                # State 118301
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.1.3.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 118302
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.3.1.0', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 118303
                        if len(subjects16) >= 1:
                            tmp19 = subjects16.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.0', tmp19)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 118304
                                if len(subjects16) == 0:
                                    pass
                                    # State 118305
                                    if len(subjects14) >= 1 and subjects14[0] == Integer(-1):
                                        tmp21 = subjects14.popleft()
                                        # State 118306
                                        if len(subjects14) == 0:
                                            pass
                                            # State 118307
                                            if len(subjects) == 0:
                                                pass
                                                # 1: 1/tan(x*e + d)
                                                yield 1, subst3
                                        subjects14.appendleft(tmp21)
                            subjects16.appendleft(tmp19)
                    if len(subjects16) >= 1 and isinstance(subjects16[0], Mul):
                        tmp22 = subjects16.popleft()
                        associative1 = tmp22
                        associative_type1 = type(tmp22)
                        subjects23 = deque(tmp22._args)
                        matcher = CommutativeMatcher118309.get()
                        tmp24 = subjects23
                        subjects23 = []
                        for s in tmp24:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp24, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 118310
                                if len(subjects16) == 0:
                                    pass
                                    # State 118311
                                    if len(subjects14) >= 1 and subjects14[0] == Integer(-1):
                                        tmp25 = subjects14.popleft()
                                        # State 118312
                                        if len(subjects14) == 0:
                                            pass
                                            # State 118313
                                            if len(subjects) == 0:
                                                pass
                                                # 1: 1/tan(x*e + d)
                                                yield 1, subst2
                                        subjects14.appendleft(tmp25)
                        subjects16.appendleft(tmp22)
                if len(subjects16) >= 1 and isinstance(subjects16[0], Add):
                    tmp26 = subjects16.popleft()
                    associative1 = tmp26
                    associative_type1 = type(tmp26)
                    subjects27 = deque(tmp26._args)
                    matcher = CommutativeMatcher118315.get()
                    tmp28 = subjects27
                    subjects27 = []
                    for s in tmp28:
                        matcher.add_subject(s)
                    for pattern_index, subst1 in matcher.match(tmp28, subst0):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 118321
                            if len(subjects16) == 0:
                                pass
                                # State 118322
                                if len(subjects14) >= 1 and subjects14[0] == Integer(-1):
                                    tmp29 = subjects14.popleft()
                                    # State 118323
                                    if len(subjects14) == 0:
                                        pass
                                        # State 118324
                                        if len(subjects) == 0:
                                            pass
                                            # 1: 1/tan(x*e + d)
                                            yield 1, subst1
                                    subjects14.appendleft(tmp29)
                    subjects16.appendleft(tmp26)
                subjects14.appendleft(tmp15)
            if len(subjects14) >= 1 and isinstance(subjects14[0], tanh):
                tmp30 = subjects14.popleft()
                subjects31 = deque(tmp30._args)
                # State 119350
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.1.3.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 119351
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.3.1.0', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 119352
                        if len(subjects31) >= 1:
                            tmp34 = subjects31.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.0', tmp34)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 119353
                                if len(subjects31) == 0:
                                    pass
                                    # State 119354
                                    if len(subjects14) >= 1 and subjects14[0] == Integer(-1):
                                        tmp36 = subjects14.popleft()
                                        # State 119355
                                        if len(subjects14) == 0:
                                            pass
                                            # State 119356
                                            if len(subjects) == 0:
                                                pass
                                                # 3: 1/tanh(x*b + a)
                                                yield 3, subst3
                                        subjects14.appendleft(tmp36)
                            subjects31.appendleft(tmp34)
                    if len(subjects31) >= 1 and isinstance(subjects31[0], Mul):
                        tmp37 = subjects31.popleft()
                        associative1 = tmp37
                        associative_type1 = type(tmp37)
                        subjects38 = deque(tmp37._args)
                        matcher = CommutativeMatcher119358.get()
                        tmp39 = subjects38
                        subjects38 = []
                        for s in tmp39:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp39, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 119359
                                if len(subjects31) == 0:
                                    pass
                                    # State 119360
                                    if len(subjects14) >= 1 and subjects14[0] == Integer(-1):
                                        tmp40 = subjects14.popleft()
                                        # State 119361
                                        if len(subjects14) == 0:
                                            pass
                                            # State 119362
                                            if len(subjects) == 0:
                                                pass
                                                # 3: 1/tanh(x*b + a)
                                                yield 3, subst2
                                        subjects14.appendleft(tmp40)
                        subjects31.appendleft(tmp37)
                if len(subjects31) >= 1 and isinstance(subjects31[0], Add):
                    tmp41 = subjects31.popleft()
                    associative1 = tmp41
                    associative_type1 = type(tmp41)
                    subjects42 = deque(tmp41._args)
                    matcher = CommutativeMatcher119364.get()
                    tmp43 = subjects42
                    subjects42 = []
                    for s in tmp43:
                        matcher.add_subject(s)
                    for pattern_index, subst1 in matcher.match(tmp43, subst0):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 119370
                            if len(subjects31) == 0:
                                pass
                                # State 119371
                                if len(subjects14) >= 1 and subjects14[0] == Integer(-1):
                                    tmp44 = subjects14.popleft()
                                    # State 119372
                                    if len(subjects14) == 0:
                                        pass
                                        # State 119373
                                        if len(subjects) == 0:
                                            pass
                                            # 3: 1/tanh(x*b + a)
                                            yield 3, subst1
                                    subjects14.appendleft(tmp44)
                    subjects31.appendleft(tmp41)
                subjects14.appendleft(tmp30)
            subjects.appendleft(tmp13)
        if len(subjects) >= 1 and isinstance(subjects[0], tanh):
            tmp45 = subjects.popleft()
            subjects46 = deque(tmp45._args)
            # State 119154
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 119155
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.1.0', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 119156
                    if len(subjects46) >= 1:
                        tmp49 = subjects46.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.0', tmp49)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 119157
                            if len(subjects46) == 0:
                                pass
                                # State 119158
                                if len(subjects) == 0:
                                    pass
                                    # 2: tanh(x*b + a)
                                    yield 2, subst3
                        subjects46.appendleft(tmp49)
                if len(subjects46) >= 1 and isinstance(subjects46[0], Mul):
                    tmp51 = subjects46.popleft()
                    associative1 = tmp51
                    associative_type1 = type(tmp51)
                    subjects52 = deque(tmp51._args)
                    matcher = CommutativeMatcher119160.get()
                    tmp53 = subjects52
                    subjects52 = []
                    for s in tmp53:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp53, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 119161
                            if len(subjects46) == 0:
                                pass
                                # State 119162
                                if len(subjects) == 0:
                                    pass
                                    # 2: tanh(x*b + a)
                                    yield 2, subst2
                    subjects46.appendleft(tmp51)
            if len(subjects46) >= 1 and isinstance(subjects46[0], Add):
                tmp54 = subjects46.popleft()
                associative1 = tmp54
                associative_type1 = type(tmp54)
                subjects55 = deque(tmp54._args)
                matcher = CommutativeMatcher119164.get()
                tmp56 = subjects55
                subjects55 = []
                for s in tmp56:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp56, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 119170
                        if len(subjects46) == 0:
                            pass
                            # State 119171
                            if len(subjects) == 0:
                                pass
                                # 2: tanh(x*b + a)
                                yield 2, subst1
                subjects46.appendleft(tmp54)
            subjects.appendleft(tmp45)
        return
        yield


from .generated_part007849 import *
from .generated_part007859 import *
from .generated_part007853 import *
from matchpy.matching.many_to_one import CommutativeMatcher
from .generated_part007852 import *
from .generated_part007855 import *
from .generated_part007850 import *
from .generated_part007858 import *
from collections import deque
from matchpy.utils import VariableWithCount
from multiset import Multiset
from .generated_part007856 import *