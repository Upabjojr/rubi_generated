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

class CommutativeMatcher69868(CommutativeMatcher):
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
        if CommutativeMatcher69868._instance is None:
            CommutativeMatcher69868._instance = CommutativeMatcher69868()
        return CommutativeMatcher69868._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 69867
        if len(subjects) >= 1 and isinstance(subjects[0], sin):
            tmp1 = subjects.popleft()
            subjects2 = deque(tmp1._args)
            # State 69869
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 69870
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.2.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 69871
                    if len(subjects2) >= 1:
                        tmp5 = subjects2.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.2.2.1.0', tmp5)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 69872
                            if len(subjects2) == 0:
                                pass
                                # State 69873
                                if len(subjects) == 0:
                                    pass
                                    # 0: sin(c + x*d)
                        subjects2.appendleft(tmp5)
                if len(subjects2) >= 1 and isinstance(subjects2[0], Mul):
                    tmp7 = subjects2.popleft()
                    associative1 = tmp7
                    associative_type1 = type(tmp7)
                    subjects8 = deque(tmp7._args)
                    matcher = CommutativeMatcher69875.get()
                    tmp9 = subjects8
                    subjects8 = []
                    for s in tmp9:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp9, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 69876
                            if len(subjects2) == 0:
                                pass
                                # State 69877
                                if len(subjects) == 0:
                                    pass
                                    # 0: sin(c + x*d)
                    subjects2.appendleft(tmp7)
            if len(subjects2) >= 1 and isinstance(subjects2[0], Add):
                tmp10 = subjects2.popleft()
                associative1 = tmp10
                associative_type1 = type(tmp10)
                subjects11 = deque(tmp10._args)
                matcher = CommutativeMatcher69879.get()
                tmp12 = subjects11
                subjects11 = []
                for s in tmp12:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp12, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 69885
                        if len(subjects2) == 0:
                            pass
                            # State 69886
                            if len(subjects) == 0:
                                pass
                                # 0: sin(c + x*d)
                subjects2.appendleft(tmp10)
            subjects.appendleft(tmp1)
        if len(subjects) >= 1 and isinstance(subjects[0], cos):
            tmp13 = subjects.popleft()
            subjects14 = deque(tmp13._args)
            # State 70314
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 70315
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.2.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 70316
                    if len(subjects14) >= 1:
                        tmp17 = subjects14.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.2.2.1.0', tmp17)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 70317
                            if len(subjects14) == 0:
                                pass
                                # State 70318
                                if len(subjects) == 0:
                                    pass
                                    # 1: cos(c + x*d)
                        subjects14.appendleft(tmp17)
                if len(subjects14) >= 1 and isinstance(subjects14[0], Mul):
                    tmp19 = subjects14.popleft()
                    associative1 = tmp19
                    associative_type1 = type(tmp19)
                    subjects20 = deque(tmp19._args)
                    matcher = CommutativeMatcher70320.get()
                    tmp21 = subjects20
                    subjects20 = []
                    for s in tmp21:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp21, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 70321
                            if len(subjects14) == 0:
                                pass
                                # State 70322
                                if len(subjects) == 0:
                                    pass
                                    # 1: cos(c + x*d)
                    subjects14.appendleft(tmp19)
            if len(subjects14) >= 1 and isinstance(subjects14[0], Add):
                tmp22 = subjects14.popleft()
                associative1 = tmp22
                associative_type1 = type(tmp22)
                subjects23 = deque(tmp22._args)
                matcher = CommutativeMatcher70324.get()
                tmp24 = subjects23
                subjects23 = []
                for s in tmp24:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp24, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 70330
                        if len(subjects14) == 0:
                            pass
                            # State 70331
                            if len(subjects) == 0:
                                pass
                                # 1: cos(c + x*d)
                subjects14.appendleft(tmp22)
            subjects.appendleft(tmp13)
        if len(subjects) >= 1 and isinstance(subjects[0], tan):
            tmp25 = subjects.popleft()
            subjects26 = deque(tmp25._args)
            # State 84097
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 84098
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.2.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 84099
                    if len(subjects26) >= 1:
                        tmp29 = subjects26.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.2.2.1.0', tmp29)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 84100
                            if len(subjects26) == 0:
                                pass
                                # State 84101
                                if len(subjects) == 0:
                                    pass
                                    # 2: tan(c + x*d)
                        subjects26.appendleft(tmp29)
                if len(subjects26) >= 1 and isinstance(subjects26[0], Mul):
                    tmp31 = subjects26.popleft()
                    associative1 = tmp31
                    associative_type1 = type(tmp31)
                    subjects32 = deque(tmp31._args)
                    matcher = CommutativeMatcher84103.get()
                    tmp33 = subjects32
                    subjects32 = []
                    for s in tmp33:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp33, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 84104
                            if len(subjects26) == 0:
                                pass
                                # State 84105
                                if len(subjects) == 0:
                                    pass
                                    # 2: tan(c + x*d)
                    subjects26.appendleft(tmp31)
            if len(subjects26) >= 1 and isinstance(subjects26[0], Add):
                tmp34 = subjects26.popleft()
                associative1 = tmp34
                associative_type1 = type(tmp34)
                subjects35 = deque(tmp34._args)
                matcher = CommutativeMatcher84107.get()
                tmp36 = subjects35
                subjects35 = []
                for s in tmp36:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp36, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 84113
                        if len(subjects26) == 0:
                            pass
                            # State 84114
                            if len(subjects) == 0:
                                pass
                                # 2: tan(c + x*d)
                subjects26.appendleft(tmp34)
            subjects.appendleft(tmp25)
        if len(subjects) >= 1 and isinstance(subjects[0], Pow):
            tmp37 = subjects.popleft()
            subjects38 = deque(tmp37._args)
            # State 84343
            if len(subjects38) >= 1 and isinstance(subjects38[0], tan):
                tmp39 = subjects38.popleft()
                subjects40 = deque(tmp39._args)
                # State 84344
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.1.2.3.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 84345
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.2.3.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 84346
                        if len(subjects40) >= 1:
                            tmp43 = subjects40.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.2.3.1.0', tmp43)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 84347
                                if len(subjects40) == 0:
                                    pass
                                    # State 84348
                                    if len(subjects38) >= 1 and subjects38[0] == -1:
                                        tmp45 = subjects38.popleft()
                                        # State 84349
                                        if len(subjects38) == 0:
                                            pass
                                            # State 84350
                                            if len(subjects) == 0:
                                                pass
                                                # 3: 1/tan(c + x*d)
                                        subjects38.appendleft(tmp45)
                            subjects40.appendleft(tmp43)
                    if len(subjects40) >= 1 and isinstance(subjects40[0], Mul):
                        tmp46 = subjects40.popleft()
                        associative1 = tmp46
                        associative_type1 = type(tmp46)
                        subjects47 = deque(tmp46._args)
                        matcher = CommutativeMatcher84352.get()
                        tmp48 = subjects47
                        subjects47 = []
                        for s in tmp48:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp48, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 84353
                                if len(subjects40) == 0:
                                    pass
                                    # State 84354
                                    if len(subjects38) >= 1 and subjects38[0] == -1:
                                        tmp49 = subjects38.popleft()
                                        # State 84355
                                        if len(subjects38) == 0:
                                            pass
                                            # State 84356
                                            if len(subjects) == 0:
                                                pass
                                                # 3: 1/tan(c + x*d)
                                        subjects38.appendleft(tmp49)
                        subjects40.appendleft(tmp46)
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.4.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 86117
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.4.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 86118
                        if len(subjects40) >= 1:
                            tmp52 = subjects40.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.4.1.0', tmp52)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 86119
                                if len(subjects40) == 0:
                                    pass
                                    # State 86120
                                    if len(subjects38) >= 1 and subjects38[0] == -1:
                                        tmp54 = subjects38.popleft()
                                        # State 86121
                                        if len(subjects38) == 0:
                                            pass
                                            # State 86122
                                            if len(subjects) == 0:
                                                pass
                                                # 4: 1/tan(e + x*f)
                                        subjects38.appendleft(tmp54)
                            subjects40.appendleft(tmp52)
                    if len(subjects40) >= 1 and isinstance(subjects40[0], Mul):
                        tmp55 = subjects40.popleft()
                        associative1 = tmp55
                        associative_type1 = type(tmp55)
                        subjects56 = deque(tmp55._args)
                        matcher = CommutativeMatcher86124.get()
                        tmp57 = subjects56
                        subjects56 = []
                        for s in tmp57:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp57, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 86125
                                if len(subjects40) == 0:
                                    pass
                                    # State 86126
                                    if len(subjects38) >= 1 and subjects38[0] == -1:
                                        tmp58 = subjects38.popleft()
                                        # State 86127
                                        if len(subjects38) == 0:
                                            pass
                                            # State 86128
                                            if len(subjects) == 0:
                                                pass
                                                # 4: 1/tan(e + x*f)
                                        subjects38.appendleft(tmp58)
                        subjects40.appendleft(tmp55)
                if len(subjects40) >= 1 and isinstance(subjects40[0], Add):
                    tmp59 = subjects40.popleft()
                    associative1 = tmp59
                    associative_type1 = type(tmp59)
                    subjects60 = deque(tmp59._args)
                    matcher = CommutativeMatcher84358.get()
                    tmp61 = subjects60
                    subjects60 = []
                    for s in tmp61:
                        matcher.add_subject(s)
                    for pattern_index, subst1 in matcher.match(tmp61, subst0):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 84364
                            if len(subjects40) == 0:
                                pass
                                # State 84365
                                if len(subjects38) >= 1 and subjects38[0] == -1:
                                    tmp62 = subjects38.popleft()
                                    # State 84366
                                    if len(subjects38) == 0:
                                        pass
                                        # State 84367
                                        if len(subjects) == 0:
                                            pass
                                            # 3: 1/tan(c + x*d)
                                    subjects38.appendleft(tmp62)
                        if pattern_index == 1:
                            pass
                            # State 86132
                            if len(subjects40) == 0:
                                pass
                                # State 86133
                                if len(subjects38) >= 1 and subjects38[0] == -1:
                                    tmp63 = subjects38.popleft()
                                    # State 86134
                                    if len(subjects38) == 0:
                                        pass
                                        # State 86135
                                        if len(subjects) == 0:
                                            pass
                                            # 4: 1/tan(e + x*f)
                                    subjects38.appendleft(tmp63)
                    subjects40.appendleft(tmp59)
                subjects38.appendleft(tmp39)
            subjects.appendleft(tmp37)
        return
        yield


from matchpy.utils import VariableWithCount
from matchpy.matching.many_to_one import CommutativeMatcher
from multiset import Multiset
from collections import deque
