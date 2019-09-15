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


class CommutativeMatcher69594(CommutativeMatcher):
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
        if CommutativeMatcher69594._instance is None:
            CommutativeMatcher69594._instance = CommutativeMatcher69594()
        return CommutativeMatcher69594._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 69593
        if len(subjects) >= 1 and isinstance(subjects[0], sin):
            tmp1 = subjects.popleft()
            subjects2 = deque(tmp1._args)
            # State 69595
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 69596
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.2.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 69597
                    if len(subjects2) >= 1:
                        tmp5 = subjects2.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.2.2.1.0', tmp5)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 69598
                            if len(subjects2) == 0:
                                pass
                                # State 69599
                                if len(subjects) == 0:
                                    pass
                                    # 0: sin(c + x*d)
                                    yield 0, subst3
                        subjects2.appendleft(tmp5)
                if len(subjects2) >= 1 and isinstance(subjects2[0], Mul):
                    tmp7 = subjects2.popleft()
                    associative1 = tmp7
                    associative_type1 = type(tmp7)
                    subjects8 = deque(tmp7._args)
                    matcher = CommutativeMatcher69601.get()
                    tmp9 = subjects8
                    subjects8 = []
                    for s in tmp9:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp9, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 69602
                            if len(subjects2) == 0:
                                pass
                                # State 69603
                                if len(subjects) == 0:
                                    pass
                                    # 0: sin(c + x*d)
                                    yield 0, subst2
                    subjects2.appendleft(tmp7)
            if len(subjects2) >= 1 and isinstance(subjects2[0], Add):
                tmp10 = subjects2.popleft()
                associative1 = tmp10
                associative_type1 = type(tmp10)
                subjects11 = deque(tmp10._args)
                matcher = CommutativeMatcher69605.get()
                tmp12 = subjects11
                subjects11 = []
                for s in tmp12:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp12, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 69611
                        if len(subjects2) == 0:
                            pass
                            # State 69612
                            if len(subjects) == 0:
                                pass
                                # 0: sin(c + x*d)
                                yield 0, subst1
                subjects2.appendleft(tmp10)
            subjects.appendleft(tmp1)
        if len(subjects) >= 1 and isinstance(subjects[0], cos):
            tmp13 = subjects.popleft()
            subjects14 = deque(tmp13._args)
            # State 70049
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 70050
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.2.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 70051
                    if len(subjects14) >= 1:
                        tmp17 = subjects14.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.2.2.1.0', tmp17)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 70052
                            if len(subjects14) == 0:
                                pass
                                # State 70053
                                if len(subjects) == 0:
                                    pass
                                    # 1: cos(c + x*d)
                                    yield 1, subst3
                        subjects14.appendleft(tmp17)
                if len(subjects14) >= 1 and isinstance(subjects14[0], Mul):
                    tmp19 = subjects14.popleft()
                    associative1 = tmp19
                    associative_type1 = type(tmp19)
                    subjects20 = deque(tmp19._args)
                    matcher = CommutativeMatcher70055.get()
                    tmp21 = subjects20
                    subjects20 = []
                    for s in tmp21:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp21, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 70056
                            if len(subjects14) == 0:
                                pass
                                # State 70057
                                if len(subjects) == 0:
                                    pass
                                    # 1: cos(c + x*d)
                                    yield 1, subst2
                    subjects14.appendleft(tmp19)
            if len(subjects14) >= 1 and isinstance(subjects14[0], Add):
                tmp22 = subjects14.popleft()
                associative1 = tmp22
                associative_type1 = type(tmp22)
                subjects23 = deque(tmp22._args)
                matcher = CommutativeMatcher70059.get()
                tmp24 = subjects23
                subjects23 = []
                for s in tmp24:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp24, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 70065
                        if len(subjects14) == 0:
                            pass
                            # State 70066
                            if len(subjects) == 0:
                                pass
                                # 1: cos(c + x*d)
                                yield 1, subst1
                subjects14.appendleft(tmp22)
            subjects.appendleft(tmp13)
        if len(subjects) >= 1 and isinstance(subjects[0], tan):
            tmp25 = subjects.popleft()
            subjects26 = deque(tmp25._args)
            # State 85048
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 85049
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.2.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 85050
                    if len(subjects26) >= 1:
                        tmp29 = subjects26.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.2.2.1.0', tmp29)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 85051
                            if len(subjects26) == 0:
                                pass
                                # State 85052
                                if len(subjects) == 0:
                                    pass
                                    # 2: tan(c + x*d)
                                    yield 2, subst3
                        subjects26.appendleft(tmp29)
                if len(subjects26) >= 1 and isinstance(subjects26[0], Mul):
                    tmp31 = subjects26.popleft()
                    associative1 = tmp31
                    associative_type1 = type(tmp31)
                    subjects32 = deque(tmp31._args)
                    matcher = CommutativeMatcher85054.get()
                    tmp33 = subjects32
                    subjects32 = []
                    for s in tmp33:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp33, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 85055
                            if len(subjects26) == 0:
                                pass
                                # State 85056
                                if len(subjects) == 0:
                                    pass
                                    # 2: tan(c + x*d)
                                    yield 2, subst2
                    subjects26.appendleft(tmp31)
            if len(subjects26) >= 1 and isinstance(subjects26[0], Add):
                tmp34 = subjects26.popleft()
                associative1 = tmp34
                associative_type1 = type(tmp34)
                subjects35 = deque(tmp34._args)
                matcher = CommutativeMatcher85058.get()
                tmp36 = subjects35
                subjects35 = []
                for s in tmp36:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp36, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 85064
                        if len(subjects26) == 0:
                            pass
                            # State 85065
                            if len(subjects) == 0:
                                pass
                                # 2: tan(c + x*d)
                                yield 2, subst1
                subjects26.appendleft(tmp34)
            subjects.appendleft(tmp25)
        if len(subjects) >= 1 and isinstance(subjects[0], Pow):
            tmp37 = subjects.popleft()
            subjects38 = deque(tmp37._args)
            # State 85340
            if len(subjects38) >= 1 and isinstance(subjects38[0], tan):
                tmp39 = subjects38.popleft()
                subjects40 = deque(tmp39._args)
                # State 85341
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.1.2.3.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 85342
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.2.3.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 85343
                        if len(subjects40) >= 1:
                            tmp43 = subjects40.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.2.3.1.0', tmp43)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 85344
                                if len(subjects40) == 0:
                                    pass
                                    # State 85345
                                    if len(subjects38) >= 1 and subjects38[0] == Integer(-1):
                                        tmp45 = subjects38.popleft()
                                        # State 85346
                                        if len(subjects38) == 0:
                                            pass
                                            # State 85347
                                            if len(subjects) == 0:
                                                pass
                                                # 3: 1/tan(c + x*d)
                                                yield 3, subst3
                                        subjects38.appendleft(tmp45)
                            subjects40.appendleft(tmp43)
                    if len(subjects40) >= 1 and isinstance(subjects40[0], Mul):
                        tmp46 = subjects40.popleft()
                        associative1 = tmp46
                        associative_type1 = type(tmp46)
                        subjects47 = deque(tmp46._args)
                        matcher = CommutativeMatcher85349.get()
                        tmp48 = subjects47
                        subjects47 = []
                        for s in tmp48:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp48, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 85350
                                if len(subjects40) == 0:
                                    pass
                                    # State 85351
                                    if len(subjects38) >= 1 and subjects38[0] == Integer(-1):
                                        tmp49 = subjects38.popleft()
                                        # State 85352
                                        if len(subjects38) == 0:
                                            pass
                                            # State 85353
                                            if len(subjects) == 0:
                                                pass
                                                # 3: 1/tan(c + x*d)
                                                yield 3, subst2
                                        subjects38.appendleft(tmp49)
                        subjects40.appendleft(tmp46)
                if len(subjects40) >= 1 and isinstance(subjects40[0], Add):
                    tmp50 = subjects40.popleft()
                    associative1 = tmp50
                    associative_type1 = type(tmp50)
                    subjects51 = deque(tmp50._args)
                    matcher = CommutativeMatcher85355.get()
                    tmp52 = subjects51
                    subjects51 = []
                    for s in tmp52:
                        matcher.add_subject(s)
                    for pattern_index, subst1 in matcher.match(tmp52, subst0):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 85361
                            if len(subjects40) == 0:
                                pass
                                # State 85362
                                if len(subjects38) >= 1 and subjects38[0] == Integer(-1):
                                    tmp53 = subjects38.popleft()
                                    # State 85363
                                    if len(subjects38) == 0:
                                        pass
                                        # State 85364
                                        if len(subjects) == 0:
                                            pass
                                            # 3: 1/tan(c + x*d)
                                            yield 3, subst1
                                    subjects38.appendleft(tmp53)
                    subjects40.appendleft(tmp50)
                subjects38.appendleft(tmp39)
            subjects.appendleft(tmp37)
        return
        yield


from .generated_part001720 import *
from .generated_part001729 import *
from .generated_part001722 import *
from .generated_part001725 import *
from .generated_part001723 import *
from matchpy.matching.many_to_one import CommutativeMatcher
from .generated_part001726 import *
from .generated_part001719 import *
from collections import deque
from .generated_part001728 import *
from matchpy.utils import VariableWithCount
from multiset import Multiset