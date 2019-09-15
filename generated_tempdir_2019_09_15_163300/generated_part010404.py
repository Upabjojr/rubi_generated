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


class CommutativeMatcher115944(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({0: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    1: (1, Multiset({1: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    2: (2, Multiset({2: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    3: (3, Multiset({3: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    4: (4, Multiset({4: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    5: (5, Multiset({5: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
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
        if CommutativeMatcher115944._instance is None:
            CommutativeMatcher115944._instance = CommutativeMatcher115944()
        return CommutativeMatcher115944._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 115943
        if len(subjects) >= 1 and isinstance(subjects[0], Pow):
            tmp1 = subjects.popleft()
            subjects2 = deque(tmp1._args)
            # State 115945
            if len(subjects2) >= 1:
                tmp3 = subjects2.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i3.1.1', tmp3)
                except ValueError:
                    pass
                else:
                    pass
                    # State 115946
                    if len(subjects2) >= 1:
                        tmp5 = subjects2.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i3.1.2', tmp5)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 115947
                            if len(subjects2) == 0:
                                pass
                                # State 115948
                                if len(subjects) == 0:
                                    pass
                                    # 0: x**n
                                    yield 0, subst2
                        subjects2.appendleft(tmp5)
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i3.1.3.0', S(0))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 116190
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i3.1.3.1.0_1', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 116191
                            if len(subjects2) >= 1:
                                tmp9 = subjects2.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i3.1.3.1.0', tmp9)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 116192
                                    if len(subjects2) == 0:
                                        pass
                                        # State 116193
                                        if len(subjects) == 0:
                                            pass
                                            # 1: F**(c + x*d)
                                            yield 1, subst4
                                subjects2.appendleft(tmp9)
                        if len(subjects2) >= 1 and isinstance(subjects2[0], Mul):
                            tmp11 = subjects2.popleft()
                            associative1 = tmp11
                            associative_type1 = type(tmp11)
                            subjects12 = deque(tmp11._args)
                            matcher = CommutativeMatcher116195.get()
                            tmp13 = subjects12
                            subjects12 = []
                            for s in tmp13:
                                matcher.add_subject(s)
                            for pattern_index, subst3 in matcher.match(tmp13, subst2):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 116196
                                    if len(subjects2) == 0:
                                        pass
                                        # State 116197
                                        if len(subjects) == 0:
                                            pass
                                            # 1: F**(c + x*d)
                                            yield 1, subst3
                            subjects2.appendleft(tmp11)
                    if len(subjects2) >= 1 and isinstance(subjects2[0], Add):
                        tmp14 = subjects2.popleft()
                        associative1 = tmp14
                        associative_type1 = type(tmp14)
                        subjects15 = deque(tmp14._args)
                        matcher = CommutativeMatcher116199.get()
                        tmp16 = subjects15
                        subjects15 = []
                        for s in tmp16:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp16, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 116205
                                if len(subjects2) == 0:
                                    pass
                                    # State 116206
                                    if len(subjects) == 0:
                                        pass
                                        # 1: F**(c + x*d)
                                        yield 1, subst2
                        subjects2.appendleft(tmp14)
                subjects2.appendleft(tmp3)
            if len(subjects2) >= 1 and isinstance(subjects2[0], tan):
                tmp17 = subjects2.popleft()
                subjects18 = deque(tmp17._args)
                # State 117941
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i3.1.3.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 117942
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i3.1.3.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 117943
                        if len(subjects18) >= 1:
                            tmp21 = subjects18.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i3.1.3.1.0', tmp21)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 117944
                                if len(subjects18) == 0:
                                    pass
                                    # State 117945
                                    if len(subjects2) >= 1 and subjects2[0] == Integer(-1):
                                        tmp23 = subjects2.popleft()
                                        # State 117946
                                        if len(subjects2) == 0:
                                            pass
                                            # State 117947
                                            if len(subjects) == 0:
                                                pass
                                                # 3: 1/tan(d + x*e)
                                                yield 3, subst3
                                        subjects2.appendleft(tmp23)
                            subjects18.appendleft(tmp21)
                    if len(subjects18) >= 1 and isinstance(subjects18[0], Mul):
                        tmp24 = subjects18.popleft()
                        associative1 = tmp24
                        associative_type1 = type(tmp24)
                        subjects25 = deque(tmp24._args)
                        matcher = CommutativeMatcher117949.get()
                        tmp26 = subjects25
                        subjects25 = []
                        for s in tmp26:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp26, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 117950
                                if len(subjects18) == 0:
                                    pass
                                    # State 117951
                                    if len(subjects2) >= 1 and subjects2[0] == Integer(-1):
                                        tmp27 = subjects2.popleft()
                                        # State 117952
                                        if len(subjects2) == 0:
                                            pass
                                            # State 117953
                                            if len(subjects) == 0:
                                                pass
                                                # 3: 1/tan(d + x*e)
                                                yield 3, subst2
                                        subjects2.appendleft(tmp27)
                        subjects18.appendleft(tmp24)
                if len(subjects18) >= 1 and isinstance(subjects18[0], Add):
                    tmp28 = subjects18.popleft()
                    associative1 = tmp28
                    associative_type1 = type(tmp28)
                    subjects29 = deque(tmp28._args)
                    matcher = CommutativeMatcher117955.get()
                    tmp30 = subjects29
                    subjects29 = []
                    for s in tmp30:
                        matcher.add_subject(s)
                    for pattern_index, subst1 in matcher.match(tmp30, subst0):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 117961
                            if len(subjects18) == 0:
                                pass
                                # State 117962
                                if len(subjects2) >= 1 and subjects2[0] == Integer(-1):
                                    tmp31 = subjects2.popleft()
                                    # State 117963
                                    if len(subjects2) == 0:
                                        pass
                                        # State 117964
                                        if len(subjects) == 0:
                                            pass
                                            # 3: 1/tan(d + x*e)
                                            yield 3, subst1
                                    subjects2.appendleft(tmp31)
                    subjects18.appendleft(tmp28)
                subjects2.appendleft(tmp17)
            if len(subjects2) >= 1 and isinstance(subjects2[0], tanh):
                tmp32 = subjects2.popleft()
                subjects33 = deque(tmp32._args)
                # State 119005
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i3.1.3.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 119006
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i3.1.3.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 119007
                        if len(subjects33) >= 1:
                            tmp36 = subjects33.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i3.1.3.1.0', tmp36)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 119008
                                if len(subjects33) == 0:
                                    pass
                                    # State 119009
                                    if len(subjects2) >= 1 and subjects2[0] == Integer(-1):
                                        tmp38 = subjects2.popleft()
                                        # State 119010
                                        if len(subjects2) == 0:
                                            pass
                                            # State 119011
                                            if len(subjects) == 0:
                                                pass
                                                # 5: 1/tanh(c + x*d)
                                                yield 5, subst3
                                        subjects2.appendleft(tmp38)
                            subjects33.appendleft(tmp36)
                    if len(subjects33) >= 1 and isinstance(subjects33[0], Mul):
                        tmp39 = subjects33.popleft()
                        associative1 = tmp39
                        associative_type1 = type(tmp39)
                        subjects40 = deque(tmp39._args)
                        matcher = CommutativeMatcher119013.get()
                        tmp41 = subjects40
                        subjects40 = []
                        for s in tmp41:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp41, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 119014
                                if len(subjects33) == 0:
                                    pass
                                    # State 119015
                                    if len(subjects2) >= 1 and subjects2[0] == Integer(-1):
                                        tmp42 = subjects2.popleft()
                                        # State 119016
                                        if len(subjects2) == 0:
                                            pass
                                            # State 119017
                                            if len(subjects) == 0:
                                                pass
                                                # 5: 1/tanh(c + x*d)
                                                yield 5, subst2
                                        subjects2.appendleft(tmp42)
                        subjects33.appendleft(tmp39)
                if len(subjects33) >= 1 and isinstance(subjects33[0], Add):
                    tmp43 = subjects33.popleft()
                    associative1 = tmp43
                    associative_type1 = type(tmp43)
                    subjects44 = deque(tmp43._args)
                    matcher = CommutativeMatcher119019.get()
                    tmp45 = subjects44
                    subjects44 = []
                    for s in tmp45:
                        matcher.add_subject(s)
                    for pattern_index, subst1 in matcher.match(tmp45, subst0):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 119025
                            if len(subjects33) == 0:
                                pass
                                # State 119026
                                if len(subjects2) >= 1 and subjects2[0] == Integer(-1):
                                    tmp46 = subjects2.popleft()
                                    # State 119027
                                    if len(subjects2) == 0:
                                        pass
                                        # State 119028
                                        if len(subjects) == 0:
                                            pass
                                            # 5: 1/tanh(c + x*d)
                                            yield 5, subst1
                                    subjects2.appendleft(tmp46)
                    subjects33.appendleft(tmp43)
                subjects2.appendleft(tmp32)
            subjects.appendleft(tmp1)
        if len(subjects) >= 1 and isinstance(subjects[0], tan):
            tmp47 = subjects.popleft()
            subjects48 = deque(tmp47._args)
            # State 117719
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i3.1.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 117720
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i3.1.2.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 117721
                    if len(subjects48) >= 1:
                        tmp51 = subjects48.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i3.1.2.1.0', tmp51)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 117722
                            if len(subjects48) == 0:
                                pass
                                # State 117723
                                if len(subjects) == 0:
                                    pass
                                    # 2: tan(c + x*d)
                                    yield 2, subst3
                        subjects48.appendleft(tmp51)
                if len(subjects48) >= 1 and isinstance(subjects48[0], Mul):
                    tmp53 = subjects48.popleft()
                    associative1 = tmp53
                    associative_type1 = type(tmp53)
                    subjects54 = deque(tmp53._args)
                    matcher = CommutativeMatcher117725.get()
                    tmp55 = subjects54
                    subjects54 = []
                    for s in tmp55:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp55, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 117726
                            if len(subjects48) == 0:
                                pass
                                # State 117727
                                if len(subjects) == 0:
                                    pass
                                    # 2: tan(c + x*d)
                                    yield 2, subst2
                    subjects48.appendleft(tmp53)
            if len(subjects48) >= 1 and isinstance(subjects48[0], Add):
                tmp56 = subjects48.popleft()
                associative1 = tmp56
                associative_type1 = type(tmp56)
                subjects57 = deque(tmp56._args)
                matcher = CommutativeMatcher117729.get()
                tmp58 = subjects57
                subjects57 = []
                for s in tmp58:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp58, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 117735
                        if len(subjects48) == 0:
                            pass
                            # State 117736
                            if len(subjects) == 0:
                                pass
                                # 2: tan(c + x*d)
                                yield 2, subst1
                subjects48.appendleft(tmp56)
            subjects.appendleft(tmp47)
        if len(subjects) >= 1 and isinstance(subjects[0], tanh):
            tmp59 = subjects.popleft()
            subjects60 = deque(tmp59._args)
            # State 118783
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i3.1.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 118784
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i3.1.2.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 118785
                    if len(subjects60) >= 1:
                        tmp63 = subjects60.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i3.1.2.1.0', tmp63)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 118786
                            if len(subjects60) == 0:
                                pass
                                # State 118787
                                if len(subjects) == 0:
                                    pass
                                    # 4: tanh(a + x*d)
                                    yield 4, subst3
                        subjects60.appendleft(tmp63)
                if len(subjects60) >= 1 and isinstance(subjects60[0], Mul):
                    tmp65 = subjects60.popleft()
                    associative1 = tmp65
                    associative_type1 = type(tmp65)
                    subjects66 = deque(tmp65._args)
                    matcher = CommutativeMatcher118789.get()
                    tmp67 = subjects66
                    subjects66 = []
                    for s in tmp67:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp67, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 118790
                            if len(subjects60) == 0:
                                pass
                                # State 118791
                                if len(subjects) == 0:
                                    pass
                                    # 4: tanh(a + x*d)
                                    yield 4, subst2
                    subjects60.appendleft(tmp65)
            if len(subjects60) >= 1 and isinstance(subjects60[0], Add):
                tmp68 = subjects60.popleft()
                associative1 = tmp68
                associative_type1 = type(tmp68)
                subjects69 = deque(tmp68._args)
                matcher = CommutativeMatcher118793.get()
                tmp70 = subjects69
                subjects69 = []
                for s in tmp70:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp70, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 118799
                        if len(subjects60) == 0:
                            pass
                            # State 118800
                            if len(subjects) == 0:
                                pass
                                # 4: tanh(a + x*d)
                                yield 4, subst1
                subjects60.appendleft(tmp68)
            subjects.appendleft(tmp59)
        return
        yield


from .generated_part010411 import *
from .generated_part010417 import *
from .generated_part010418 import *
from .generated_part010414 import *
from .generated_part010405 import *
from matchpy.matching.many_to_one import CommutativeMatcher
from .generated_part010415 import *
from .generated_part010406 import *
from collections import deque
from .generated_part010412 import *
from .generated_part010409 import *
from matchpy.utils import VariableWithCount
from multiset import Multiset
from .generated_part010408 import *