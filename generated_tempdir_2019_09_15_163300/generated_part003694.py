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


class CommutativeMatcher6480(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({}), [
      (VariableWithCount('i2.2.0_1', 1, 1, S(1)), Mul),
      (VariableWithCount('i2.2.1', 1, 1, None), Mul)
]),
    1: (1, Multiset({}), [
      (VariableWithCount('i2.2.0_1', 1, 1, None), Mul),
      (VariableWithCount('i2.2.1', 1, 1, None), Mul)
]),
    2: (2, Multiset({0: 1}), [
      (VariableWithCount('i2.2.0_1', 1, 1, S(1)), Mul)
]),
    3: (3, Multiset({1: 1}), [
      (VariableWithCount('i2.2.0_1', 1, 1, S(1)), Mul)
]),
    4: (4, Multiset({2: 1}), [
      (VariableWithCount('i2.2.0_1', 1, 1, S(1)), Mul)
]),
    5: (5, Multiset({3: 1}), [
      (VariableWithCount('i2.2.0_1', 1, 1, S(1)), Mul)
]),
    6: (6, Multiset({4: 1}), [
      (VariableWithCount('i2.2.0_1', 1, 1, S(1)), Mul)
]),
    7: (7, Multiset({5: 1}), [
      (VariableWithCount('i2.2.0_1', 1, 1, S(1)), Mul)
]),
    8: (8, Multiset({6: 1}), [
      (VariableWithCount('i2.2.0_1', 1, 1, S(1)), Mul)
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
        if CommutativeMatcher6480._instance is None:
            CommutativeMatcher6480._instance = CommutativeMatcher6480()
        return CommutativeMatcher6480._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 6479
        if len(subjects) >= 1 and isinstance(subjects[0], sin):
            tmp1 = subjects.popleft()
            subjects2 = deque(tmp1._args)
            # State 57042
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 57043
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.2.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 57044
                    if len(subjects2) >= 1:
                        tmp5 = subjects2.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.2.1.0', tmp5)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 57045
                            if len(subjects2) == 0:
                                pass
                                # State 57046
                                if len(subjects) == 0:
                                    pass
                                    # 0: sin(e + x*f)
                                    yield 0, subst3
                        subjects2.appendleft(tmp5)
                if len(subjects2) >= 1 and isinstance(subjects2[0], Mul):
                    tmp7 = subjects2.popleft()
                    associative1 = tmp7
                    associative_type1 = type(tmp7)
                    subjects8 = deque(tmp7._args)
                    matcher = CommutativeMatcher57048.get()
                    tmp9 = subjects8
                    subjects8 = []
                    for s in tmp9:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp9, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 57049
                            if len(subjects2) == 0:
                                pass
                                # State 57050
                                if len(subjects) == 0:
                                    pass
                                    # 0: sin(e + x*f)
                                    yield 0, subst2
                    subjects2.appendleft(tmp7)
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.3.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 57466
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.3.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 57467
                    if len(subjects2) >= 1:
                        tmp12 = subjects2.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.3.1.0', tmp12)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 57468
                            if len(subjects2) == 0:
                                pass
                                # State 57469
                                if len(subjects) == 0:
                                    pass
                                    # 1: sin(e + x*f)
                                    yield 1, subst3
                        subjects2.appendleft(tmp12)
                if len(subjects2) >= 1 and isinstance(subjects2[0], Mul):
                    tmp14 = subjects2.popleft()
                    associative1 = tmp14
                    associative_type1 = type(tmp14)
                    subjects15 = deque(tmp14._args)
                    matcher = CommutativeMatcher57471.get()
                    tmp16 = subjects15
                    subjects15 = []
                    for s in tmp16:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp16, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 57472
                            if len(subjects2) == 0:
                                pass
                                # State 57473
                                if len(subjects) == 0:
                                    pass
                                    # 1: sin(e + x*f)
                                    yield 1, subst2
                    subjects2.appendleft(tmp14)
            if len(subjects2) >= 1 and isinstance(subjects2[0], Add):
                tmp17 = subjects2.popleft()
                associative1 = tmp17
                associative_type1 = type(tmp17)
                subjects18 = deque(tmp17._args)
                matcher = CommutativeMatcher57052.get()
                tmp19 = subjects18
                subjects18 = []
                for s in tmp19:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp19, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 57058
                        if len(subjects2) == 0:
                            pass
                            # State 57059
                            if len(subjects) == 0:
                                pass
                                # 0: sin(e + x*f)
                                yield 0, subst1
                    if pattern_index == 1:
                        pass
                        # State 57477
                        if len(subjects2) == 0:
                            pass
                            # State 57478
                            if len(subjects) == 0:
                                pass
                                # 1: sin(e + x*f)
                                yield 1, subst1
                subjects2.appendleft(tmp17)
            subjects.appendleft(tmp1)
        if len(subjects) >= 1 and isinstance(subjects[0], cos):
            tmp20 = subjects.popleft()
            subjects21 = deque(tmp20._args)
            # State 57642
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.3.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 57643
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.3.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 57644
                    if len(subjects21) >= 1:
                        tmp24 = subjects21.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.3.1.0', tmp24)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 57645
                            if len(subjects21) == 0:
                                pass
                                # State 57646
                                if len(subjects) == 0:
                                    pass
                                    # 2: cos(e + x*f)
                                    yield 2, subst3
                        subjects21.appendleft(tmp24)
                if len(subjects21) >= 1 and isinstance(subjects21[0], Mul):
                    tmp26 = subjects21.popleft()
                    associative1 = tmp26
                    associative_type1 = type(tmp26)
                    subjects27 = deque(tmp26._args)
                    matcher = CommutativeMatcher57648.get()
                    tmp28 = subjects27
                    subjects27 = []
                    for s in tmp28:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp28, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 57649
                            if len(subjects21) == 0:
                                pass
                                # State 57650
                                if len(subjects) == 0:
                                    pass
                                    # 2: cos(e + x*f)
                                    yield 2, subst2
                    subjects21.appendleft(tmp26)
            if len(subjects21) >= 1 and isinstance(subjects21[0], Add):
                tmp29 = subjects21.popleft()
                associative1 = tmp29
                associative_type1 = type(tmp29)
                subjects30 = deque(tmp29._args)
                matcher = CommutativeMatcher57652.get()
                tmp31 = subjects30
                subjects30 = []
                for s in tmp31:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp31, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 57658
                        if len(subjects21) == 0:
                            pass
                            # State 57659
                            if len(subjects) == 0:
                                pass
                                # 2: cos(e + x*f)
                                yield 2, subst1
                subjects21.appendleft(tmp29)
            subjects.appendleft(tmp20)
        if len(subjects) >= 1 and isinstance(subjects[0], tan):
            tmp32 = subjects.popleft()
            subjects33 = deque(tmp32._args)
            # State 76040
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 76041
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.2.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 76042
                    if len(subjects33) >= 1:
                        tmp36 = subjects33.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.2.1.0', tmp36)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 76043
                            if len(subjects33) == 0:
                                pass
                                # State 76044
                                if len(subjects) == 0:
                                    pass
                                    # 3: tan(e + x*f)
                                    yield 3, subst3
                        subjects33.appendleft(tmp36)
                if len(subjects33) >= 1 and isinstance(subjects33[0], Mul):
                    tmp38 = subjects33.popleft()
                    associative1 = tmp38
                    associative_type1 = type(tmp38)
                    subjects39 = deque(tmp38._args)
                    matcher = CommutativeMatcher76046.get()
                    tmp40 = subjects39
                    subjects39 = []
                    for s in tmp40:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp40, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 76047
                            if len(subjects33) == 0:
                                pass
                                # State 76048
                                if len(subjects) == 0:
                                    pass
                                    # 3: tan(e + x*f)
                                    yield 3, subst2
                    subjects33.appendleft(tmp38)
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.3.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 76242
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.3.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 76243
                    if len(subjects33) >= 1:
                        tmp43 = subjects33.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.3.1.0', tmp43)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 76244
                            if len(subjects33) == 0:
                                pass
                                # State 76245
                                if len(subjects) == 0:
                                    pass
                                    # 4: tan(e + x*f)
                                    yield 4, subst3
                        subjects33.appendleft(tmp43)
                if len(subjects33) >= 1 and isinstance(subjects33[0], Mul):
                    tmp45 = subjects33.popleft()
                    associative1 = tmp45
                    associative_type1 = type(tmp45)
                    subjects46 = deque(tmp45._args)
                    matcher = CommutativeMatcher76247.get()
                    tmp47 = subjects46
                    subjects46 = []
                    for s in tmp47:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp47, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 76248
                            if len(subjects33) == 0:
                                pass
                                # State 76249
                                if len(subjects) == 0:
                                    pass
                                    # 4: tan(e + x*f)
                                    yield 4, subst2
                    subjects33.appendleft(tmp45)
            if len(subjects33) >= 1 and isinstance(subjects33[0], Add):
                tmp48 = subjects33.popleft()
                associative1 = tmp48
                associative_type1 = type(tmp48)
                subjects49 = deque(tmp48._args)
                matcher = CommutativeMatcher76050.get()
                tmp50 = subjects49
                subjects49 = []
                for s in tmp50:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp50, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 76056
                        if len(subjects33) == 0:
                            pass
                            # State 76057
                            if len(subjects) == 0:
                                pass
                                # 3: tan(e + x*f)
                                yield 3, subst1
                    if pattern_index == 1:
                        pass
                        # State 76253
                        if len(subjects33) == 0:
                            pass
                            # State 76254
                            if len(subjects) == 0:
                                pass
                                # 4: tan(e + x*f)
                                yield 4, subst1
                subjects33.appendleft(tmp48)
            subjects.appendleft(tmp32)
        if len(subjects) >= 1 and isinstance(subjects[0], Pow):
            tmp51 = subjects.popleft()
            subjects52 = deque(tmp51._args)
            # State 76292
            if len(subjects52) >= 1 and isinstance(subjects52[0], tan):
                tmp53 = subjects52.popleft()
                subjects54 = deque(tmp53._args)
                # State 76293
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.3.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 76294
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.3.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 76295
                        if len(subjects54) >= 1:
                            tmp57 = subjects54.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.3.1.0', tmp57)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 76296
                                if len(subjects54) == 0:
                                    pass
                                    # State 76297
                                    if len(subjects52) >= 1 and subjects52[0] == Integer(-1):
                                        tmp59 = subjects52.popleft()
                                        # State 76298
                                        if len(subjects52) == 0:
                                            pass
                                            # State 76299
                                            if len(subjects) == 0:
                                                pass
                                                # 5: 1/tan(e + x*f)
                                                yield 5, subst3
                                        subjects52.appendleft(tmp59)
                            subjects54.appendleft(tmp57)
                    if len(subjects54) >= 1 and isinstance(subjects54[0], Mul):
                        tmp60 = subjects54.popleft()
                        associative1 = tmp60
                        associative_type1 = type(tmp60)
                        subjects61 = deque(tmp60._args)
                        matcher = CommutativeMatcher76301.get()
                        tmp62 = subjects61
                        subjects61 = []
                        for s in tmp62:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp62, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 76302
                                if len(subjects54) == 0:
                                    pass
                                    # State 76303
                                    if len(subjects52) >= 1 and subjects52[0] == Integer(-1):
                                        tmp63 = subjects52.popleft()
                                        # State 76304
                                        if len(subjects52) == 0:
                                            pass
                                            # State 76305
                                            if len(subjects) == 0:
                                                pass
                                                # 5: 1/tan(e + x*f)
                                                yield 5, subst2
                                        subjects52.appendleft(tmp63)
                        subjects54.appendleft(tmp60)
                if len(subjects54) >= 1 and isinstance(subjects54[0], Add):
                    tmp64 = subjects54.popleft()
                    associative1 = tmp64
                    associative_type1 = type(tmp64)
                    subjects65 = deque(tmp64._args)
                    matcher = CommutativeMatcher76307.get()
                    tmp66 = subjects65
                    subjects65 = []
                    for s in tmp66:
                        matcher.add_subject(s)
                    for pattern_index, subst1 in matcher.match(tmp66, subst0):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 76313
                            if len(subjects54) == 0:
                                pass
                                # State 76314
                                if len(subjects52) >= 1 and subjects52[0] == Integer(-1):
                                    tmp67 = subjects52.popleft()
                                    # State 76315
                                    if len(subjects52) == 0:
                                        pass
                                        # State 76316
                                        if len(subjects) == 0:
                                            pass
                                            # 5: 1/tan(e + x*f)
                                            yield 5, subst1
                                    subjects52.appendleft(tmp67)
                    subjects54.appendleft(tmp64)
                subjects52.appendleft(tmp53)
            if len(subjects52) >= 1 and isinstance(subjects52[0], sin):
                tmp68 = subjects52.popleft()
                subjects69 = deque(tmp68._args)
                # State 89813
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.3.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 89814
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.3.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 89815
                        if len(subjects69) >= 1:
                            tmp72 = subjects69.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.3.1.0', tmp72)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 89816
                                if len(subjects69) == 0:
                                    pass
                                    # State 89817
                                    if len(subjects52) >= 1 and subjects52[0] == Integer(-1):
                                        tmp74 = subjects52.popleft()
                                        # State 89818
                                        if len(subjects52) == 0:
                                            pass
                                            # State 89819
                                            if len(subjects) == 0:
                                                pass
                                                # 6: 1/sin(e + x*f)
                                                yield 6, subst3
                                        subjects52.appendleft(tmp74)
                            subjects69.appendleft(tmp72)
                    if len(subjects69) >= 1 and isinstance(subjects69[0], Mul):
                        tmp75 = subjects69.popleft()
                        associative1 = tmp75
                        associative_type1 = type(tmp75)
                        subjects76 = deque(tmp75._args)
                        matcher = CommutativeMatcher89821.get()
                        tmp77 = subjects76
                        subjects76 = []
                        for s in tmp77:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp77, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 89822
                                if len(subjects69) == 0:
                                    pass
                                    # State 89823
                                    if len(subjects52) >= 1 and subjects52[0] == Integer(-1):
                                        tmp78 = subjects52.popleft()
                                        # State 89824
                                        if len(subjects52) == 0:
                                            pass
                                            # State 89825
                                            if len(subjects) == 0:
                                                pass
                                                # 6: 1/sin(e + x*f)
                                                yield 6, subst2
                                        subjects52.appendleft(tmp78)
                        subjects69.appendleft(tmp75)
                if len(subjects69) >= 1 and isinstance(subjects69[0], Add):
                    tmp79 = subjects69.popleft()
                    associative1 = tmp79
                    associative_type1 = type(tmp79)
                    subjects80 = deque(tmp79._args)
                    matcher = CommutativeMatcher89827.get()
                    tmp81 = subjects80
                    subjects80 = []
                    for s in tmp81:
                        matcher.add_subject(s)
                    for pattern_index, subst1 in matcher.match(tmp81, subst0):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 89833
                            if len(subjects69) == 0:
                                pass
                                # State 89834
                                if len(subjects52) >= 1 and subjects52[0] == Integer(-1):
                                    tmp82 = subjects52.popleft()
                                    # State 89835
                                    if len(subjects52) == 0:
                                        pass
                                        # State 89836
                                        if len(subjects) == 0:
                                            pass
                                            # 6: 1/sin(e + x*f)
                                            yield 6, subst1
                                    subjects52.appendleft(tmp82)
                    subjects69.appendleft(tmp79)
                subjects52.appendleft(tmp68)
            subjects.appendleft(tmp51)
        return
        yield


from .generated_part003697 import *
from .generated_part003700 import *
from .generated_part003707 import *
from .generated_part003709 import *
from .generated_part003702 import *
from .generated_part003704 import *
from matchpy.matching.many_to_one import CommutativeMatcher
from .generated_part003706 import *
from .generated_part003695 import *
from .generated_part003710 import *
from collections import deque
from .generated_part003696 import *
from .generated_part003699 import *
from .generated_part003703 import *
from matchpy.utils import VariableWithCount
from multiset import Multiset