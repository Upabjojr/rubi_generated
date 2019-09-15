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


class CommutativeMatcher11005(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({0: 1}), [
      (VariableWithCount('i2.2.1.2.0', 1, 1, S(1)), Mul)
]),
    1: (1, Multiset({1: 1}), [
      (VariableWithCount('i2.2.1.2.0', 1, 1, S(1)), Mul)
]),
    2: (2, Multiset({2: 1}), [
      (VariableWithCount('i2.2.1.2.0', 1, 1, S(1)), Mul)
]),
    3: (3, Multiset({3: 1}), [
      (VariableWithCount('i2.2.1.2.0', 1, 1, S(1)), Mul)
]),
    4: (4, Multiset({4: 1}), [
      (VariableWithCount('i2.2.1.2.0', 1, 1, S(1)), Mul)
]),
    5: (5, Multiset({5: 1}), [
      (VariableWithCount('i2.2.1.2.0', 1, 1, S(1)), Mul)
]),
    6: (6, Multiset({6: 1}), [
      (VariableWithCount('i2.2.1.2.0', 1, 1, S(1)), Mul)
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
        if CommutativeMatcher11005._instance is None:
            CommutativeMatcher11005._instance = CommutativeMatcher11005()
        return CommutativeMatcher11005._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 11004
        if len(subjects) >= 1 and isinstance(subjects[0], Pow):
            tmp1 = subjects.popleft()
            subjects2 = deque(tmp1._args)
            # State 11006
            if len(subjects2) >= 1:
                tmp3 = subjects2.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.1.2.1', tmp3)
                except ValueError:
                    pass
                else:
                    pass
                    # State 11007
                    if len(subjects2) >= 1 and subjects2[0] == Integer(-1):
                        tmp5 = subjects2.popleft()
                        # State 11008
                        if len(subjects2) == 0:
                            pass
                            # State 11009
                            if len(subjects) == 0:
                                pass
                                # 0: 1/x
                                yield 0, subst1
                        subjects2.appendleft(tmp5)
                subjects2.appendleft(tmp3)
            if len(subjects2) >= 1 and isinstance(subjects2[0], tan):
                tmp6 = subjects2.popleft()
                subjects7 = deque(tmp6._args)
                # State 85591
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.1.2.3.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 85592
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.2.3.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 85593
                        if len(subjects7) >= 1:
                            tmp10 = subjects7.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.2.3.1.0', tmp10)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 85594
                                if len(subjects7) == 0:
                                    pass
                                    # State 85595
                                    if len(subjects2) >= 1 and subjects2[0] == Integer(-1):
                                        tmp12 = subjects2.popleft()
                                        # State 85596
                                        if len(subjects2) == 0:
                                            pass
                                            # State 85597
                                            if len(subjects) == 0:
                                                pass
                                                # 6: 1/tan(c + x*d)
                                                yield 6, subst3
                                        subjects2.appendleft(tmp12)
                            subjects7.appendleft(tmp10)
                    if len(subjects7) >= 1 and isinstance(subjects7[0], Mul):
                        tmp13 = subjects7.popleft()
                        associative1 = tmp13
                        associative_type1 = type(tmp13)
                        subjects14 = deque(tmp13._args)
                        matcher = CommutativeMatcher85599.get()
                        tmp15 = subjects14
                        subjects14 = []
                        for s in tmp15:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp15, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 85600
                                if len(subjects7) == 0:
                                    pass
                                    # State 85601
                                    if len(subjects2) >= 1 and subjects2[0] == Integer(-1):
                                        tmp16 = subjects2.popleft()
                                        # State 85602
                                        if len(subjects2) == 0:
                                            pass
                                            # State 85603
                                            if len(subjects) == 0:
                                                pass
                                                # 6: 1/tan(c + x*d)
                                                yield 6, subst2
                                        subjects2.appendleft(tmp16)
                        subjects7.appendleft(tmp13)
                if len(subjects7) >= 1 and isinstance(subjects7[0], Add):
                    tmp17 = subjects7.popleft()
                    associative1 = tmp17
                    associative_type1 = type(tmp17)
                    subjects18 = deque(tmp17._args)
                    matcher = CommutativeMatcher85605.get()
                    tmp19 = subjects18
                    subjects18 = []
                    for s in tmp19:
                        matcher.add_subject(s)
                    for pattern_index, subst1 in matcher.match(tmp19, subst0):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 85611
                            if len(subjects7) == 0:
                                pass
                                # State 85612
                                if len(subjects2) >= 1 and subjects2[0] == Integer(-1):
                                    tmp20 = subjects2.popleft()
                                    # State 85613
                                    if len(subjects2) == 0:
                                        pass
                                        # State 85614
                                        if len(subjects) == 0:
                                            pass
                                            # 6: 1/tan(c + x*d)
                                            yield 6, subst1
                                    subjects2.appendleft(tmp20)
                    subjects7.appendleft(tmp17)
                subjects2.appendleft(tmp6)
            subjects.appendleft(tmp1)
        if len(subjects) >= 1 and isinstance(subjects[0], sin):
            tmp21 = subjects.popleft()
            subjects22 = deque(tmp21._args)
            # State 69732
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 69733
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.2.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 69734
                    if len(subjects22) >= 1:
                        tmp25 = subjects22.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.2.2.1.0', tmp25)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 69735
                            if len(subjects22) == 0:
                                pass
                                # State 69736
                                if len(subjects) == 0:
                                    pass
                                    # 1: sin(c + x*d)
                                    yield 1, subst3
                        subjects22.appendleft(tmp25)
                if len(subjects22) >= 1 and isinstance(subjects22[0], Mul):
                    tmp27 = subjects22.popleft()
                    associative1 = tmp27
                    associative_type1 = type(tmp27)
                    subjects28 = deque(tmp27._args)
                    matcher = CommutativeMatcher69738.get()
                    tmp29 = subjects28
                    subjects28 = []
                    for s in tmp29:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp29, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 69739
                            if len(subjects22) == 0:
                                pass
                                # State 69740
                                if len(subjects) == 0:
                                    pass
                                    # 1: sin(c + x*d)
                                    yield 1, subst2
                    subjects22.appendleft(tmp27)
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.4.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 71374
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.4.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 71375
                    if len(subjects22) >= 1:
                        tmp32 = subjects22.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.4.1.0', tmp32)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 71376
                            if len(subjects22) == 0:
                                pass
                                # State 71377
                                if len(subjects) == 0:
                                    pass
                                    # 4: sin(e + x*f)
                                    yield 4, subst3
                        subjects22.appendleft(tmp32)
                if len(subjects22) >= 1 and isinstance(subjects22[0], Mul):
                    tmp34 = subjects22.popleft()
                    associative1 = tmp34
                    associative_type1 = type(tmp34)
                    subjects35 = deque(tmp34._args)
                    matcher = CommutativeMatcher71379.get()
                    tmp36 = subjects35
                    subjects35 = []
                    for s in tmp36:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp36, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 71380
                            if len(subjects22) == 0:
                                pass
                                # State 71381
                                if len(subjects) == 0:
                                    pass
                                    # 4: sin(e + x*f)
                                    yield 4, subst2
                    subjects22.appendleft(tmp34)
            if len(subjects22) >= 1 and isinstance(subjects22[0], Add):
                tmp37 = subjects22.popleft()
                associative1 = tmp37
                associative_type1 = type(tmp37)
                subjects38 = deque(tmp37._args)
                matcher = CommutativeMatcher69742.get()
                tmp39 = subjects38
                subjects38 = []
                for s in tmp39:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp39, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 69748
                        if len(subjects22) == 0:
                            pass
                            # State 69749
                            if len(subjects) == 0:
                                pass
                                # 1: sin(c + x*d)
                                yield 1, subst1
                    if pattern_index == 1:
                        pass
                        # State 71385
                        if len(subjects22) == 0:
                            pass
                            # State 71386
                            if len(subjects) == 0:
                                pass
                                # 4: sin(e + x*f)
                                yield 4, subst1
                subjects22.appendleft(tmp37)
            subjects.appendleft(tmp21)
        if len(subjects) >= 1 and isinstance(subjects[0], cos):
            tmp40 = subjects.popleft()
            subjects41 = deque(tmp40._args)
            # State 70183
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 70184
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.2.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 70185
                    if len(subjects41) >= 1:
                        tmp44 = subjects41.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.2.2.1.0', tmp44)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 70186
                            if len(subjects41) == 0:
                                pass
                                # State 70187
                                if len(subjects) == 0:
                                    pass
                                    # 2: cos(c + x*d)
                                    yield 2, subst3
                        subjects41.appendleft(tmp44)
                if len(subjects41) >= 1 and isinstance(subjects41[0], Mul):
                    tmp46 = subjects41.popleft()
                    associative1 = tmp46
                    associative_type1 = type(tmp46)
                    subjects47 = deque(tmp46._args)
                    matcher = CommutativeMatcher70189.get()
                    tmp48 = subjects47
                    subjects47 = []
                    for s in tmp48:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp48, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 70190
                            if len(subjects41) == 0:
                                pass
                                # State 70191
                                if len(subjects) == 0:
                                    pass
                                    # 2: cos(c + x*d)
                                    yield 2, subst2
                    subjects41.appendleft(tmp46)
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.4.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 70839
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.4.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 70840
                    if len(subjects41) >= 1:
                        tmp51 = subjects41.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.4.1.0', tmp51)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 70841
                            if len(subjects41) == 0:
                                pass
                                # State 70842
                                if len(subjects) == 0:
                                    pass
                                    # 3: cos(e + x*f)
                                    yield 3, subst3
                        subjects41.appendleft(tmp51)
                if len(subjects41) >= 1 and isinstance(subjects41[0], Mul):
                    tmp53 = subjects41.popleft()
                    associative1 = tmp53
                    associative_type1 = type(tmp53)
                    subjects54 = deque(tmp53._args)
                    matcher = CommutativeMatcher70844.get()
                    tmp55 = subjects54
                    subjects54 = []
                    for s in tmp55:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp55, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 70845
                            if len(subjects41) == 0:
                                pass
                                # State 70846
                                if len(subjects) == 0:
                                    pass
                                    # 3: cos(e + x*f)
                                    yield 3, subst2
                    subjects41.appendleft(tmp53)
            if len(subjects41) >= 1 and isinstance(subjects41[0], Add):
                tmp56 = subjects41.popleft()
                associative1 = tmp56
                associative_type1 = type(tmp56)
                subjects57 = deque(tmp56._args)
                matcher = CommutativeMatcher70193.get()
                tmp58 = subjects57
                subjects57 = []
                for s in tmp58:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp58, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 70199
                        if len(subjects41) == 0:
                            pass
                            # State 70200
                            if len(subjects) == 0:
                                pass
                                # 2: cos(c + x*d)
                                yield 2, subst1
                    if pattern_index == 1:
                        pass
                        # State 70850
                        if len(subjects41) == 0:
                            pass
                            # State 70851
                            if len(subjects) == 0:
                                pass
                                # 3: cos(e + x*f)
                                yield 3, subst1
                subjects41.appendleft(tmp56)
            subjects.appendleft(tmp40)
        if len(subjects) >= 1 and isinstance(subjects[0], tan):
            tmp59 = subjects.popleft()
            subjects60 = deque(tmp59._args)
            # State 85236
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 85237
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.2.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 85238
                    if len(subjects60) >= 1:
                        tmp63 = subjects60.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.2.2.1.0', tmp63)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 85239
                            if len(subjects60) == 0:
                                pass
                                # State 85240
                                if len(subjects) == 0:
                                    pass
                                    # 5: tan(c + x*d)
                                    yield 5, subst3
                        subjects60.appendleft(tmp63)
                if len(subjects60) >= 1 and isinstance(subjects60[0], Mul):
                    tmp65 = subjects60.popleft()
                    associative1 = tmp65
                    associative_type1 = type(tmp65)
                    subjects66 = deque(tmp65._args)
                    matcher = CommutativeMatcher85242.get()
                    tmp67 = subjects66
                    subjects66 = []
                    for s in tmp67:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp67, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 85243
                            if len(subjects60) == 0:
                                pass
                                # State 85244
                                if len(subjects) == 0:
                                    pass
                                    # 5: tan(c + x*d)
                                    yield 5, subst2
                    subjects60.appendleft(tmp65)
            if len(subjects60) >= 1 and isinstance(subjects60[0], Add):
                tmp68 = subjects60.popleft()
                associative1 = tmp68
                associative_type1 = type(tmp68)
                subjects69 = deque(tmp68._args)
                matcher = CommutativeMatcher85246.get()
                tmp70 = subjects69
                subjects69 = []
                for s in tmp70:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp70, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 85252
                        if len(subjects60) == 0:
                            pass
                            # State 85253
                            if len(subjects) == 0:
                                pass
                                # 5: tan(c + x*d)
                                yield 5, subst1
                subjects60.appendleft(tmp68)
            subjects.appendleft(tmp59)
        return
        yield


from .generated_part002079 import *
from .generated_part002081 import *
from .generated_part002085 import *
from .generated_part002077 import *
from matchpy.matching.many_to_one import CommutativeMatcher
from .generated_part002076 import *
from .generated_part002087 import *
from collections import deque
from .generated_part002084 import *
from .generated_part002088 import *
from .generated_part002080 import *
from matchpy.utils import VariableWithCount
from multiset import Multiset
from .generated_part002083 import *