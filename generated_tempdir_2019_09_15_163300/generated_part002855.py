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


class CommutativeMatcher3303(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({}), [
      (VariableWithCount('i2.2.1.0', 1, 1, None), Mul),
      (VariableWithCount('i2.2.1.0_2', 1, 1, S(1)), Mul)
]),
    1: (1, Multiset({}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul),
      (VariableWithCount('i2.2.1.1', 1, 1, None), Mul)
]),
    2: (2, Multiset({0: 1}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul)
]),
    3: (3, Multiset({}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul),
      (VariableWithCount('i2.2.1.4.1.1.0', 1, 1, None), Mul)
]),
    4: (4, Multiset({}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul),
      (VariableWithCount('i2.2.1.2.2.2.1.0', 1, 1, None), Mul)
]),
    5: (5, Multiset({}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul),
      (VariableWithCount('i2.2.1.2.1.0', 1, 1, None), Mul)
]),
    6: (6, Multiset({}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul),
      (VariableWithCount('i2.2.1.3.1.0', 1, 1, None), Mul)
]),
    7: (7, Multiset({1: 1}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul)
]),
    8: (8, Multiset({2: 1}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul)
]),
    9: (9, Multiset({3: 1}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul)
]),
    10: (10, Multiset({4: 1}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul)
]),
    11: (11, Multiset({5: 1}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul)
]),
    12: (12, Multiset({6: 1}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul)
]),
    13: (13, Multiset({7: 1}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul)
]),
    14: (14, Multiset({8: 1}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul)
]),
    15: (15, Multiset({9: 1, 10: 1}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, None), Mul),
      (VariableWithCount('i2.2.1.0_2', 1, 1, S(1)), Mul),
      (VariableWithCount('i2.2.1.0_3', 1, 1, S(1)), Mul)
])
}
    subjects = {}
    subjects_by_id = {}
    bipartite = BipartiteGraph()
    associative = Mul
    max_optional_count = 2
    anonymous_patterns = set()

    def __init__(self):
        self.add_subject(None)

    @staticmethod
    def get():
        if CommutativeMatcher3303._instance is None:
            CommutativeMatcher3303._instance = CommutativeMatcher3303()
        return CommutativeMatcher3303._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 3302
        if len(subjects) >= 1 and isinstance(subjects[0], Pow):
            tmp1 = subjects.popleft()
            subjects2 = deque(tmp1._args)
            # State 6363
            if len(subjects2) >= 1:
                tmp3 = subjects2.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.1.1', tmp3)
                except ValueError:
                    pass
                else:
                    pass
                    # State 6364
                    if len(subjects2) >= 1:
                        tmp5 = subjects2.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.1.2', tmp5)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 6365
                            if len(subjects2) == 0:
                                pass
                                # State 6366
                                if len(subjects) == 0:
                                    pass
                                    # 0: x**j
                                    yield 0, subst2
                        subjects2.appendleft(tmp5)
                subjects2.appendleft(tmp3)
            if len(subjects2) >= 1 and isinstance(subjects2[0], Add):
                tmp7 = subjects2.popleft()
                associative1 = tmp7
                associative_type1 = type(tmp7)
                subjects8 = deque(tmp7._args)
                matcher = CommutativeMatcher150960.get()
                tmp9 = subjects8
                subjects8 = []
                for s in tmp9:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp9, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 150967
                        if len(subjects2) >= 1 and subjects2[0] == Rational(1, 2):
                            tmp10 = subjects2.popleft()
                            # State 150968
                            if len(subjects2) == 0:
                                pass
                                # State 150969
                                if len(subjects) == 0:
                                    pass
                                    # 9: sqrt(x*e + 1)
                                    yield 9, subst1
                            subjects2.appendleft(tmp10)
                    if pattern_index == 1:
                        pass
                        # State 150973
                        if len(subjects2) >= 1 and subjects2[0] == Rational(-1, 2):
                            tmp11 = subjects2.popleft()
                            # State 150974
                            if len(subjects2) == 0:
                                pass
                                # State 150975
                                if len(subjects) == 0:
                                    pass
                                    # 10: 1/sqrt(x*g + 1)
                                    yield 10, subst1
                            subjects2.appendleft(tmp11)
                subjects2.appendleft(tmp7)
            subjects.appendleft(tmp1)
        if len(subjects) >= 1 and isinstance(subjects[0], asin):
            tmp12 = subjects.popleft()
            subjects13 = deque(tmp12._args)
            # State 108651
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.0', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 108652
                if len(subjects13) >= 1:
                    tmp15 = subjects13.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.1', tmp15)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 108653
                        if len(subjects13) == 0:
                            pass
                            # State 108654
                            if len(subjects) == 0:
                                pass
                                # 1: asin(x*c)
                                yield 1, subst2
                    subjects13.appendleft(tmp15)
            if len(subjects13) >= 1 and isinstance(subjects13[0], Mul):
                tmp17 = subjects13.popleft()
                associative1 = tmp17
                associative_type1 = type(tmp17)
                subjects18 = deque(tmp17._args)
                matcher = CommutativeMatcher108656.get()
                tmp19 = subjects18
                subjects18 = []
                for s in tmp19:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp19, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 108657
                        if len(subjects13) == 0:
                            pass
                            # State 108658
                            if len(subjects) == 0:
                                pass
                                # 1: asin(x*c)
                                yield 1, subst1
                subjects13.appendleft(tmp17)
            subjects.appendleft(tmp12)
        if len(subjects) >= 1 and isinstance(subjects[0], acos):
            tmp20 = subjects.popleft()
            subjects21 = deque(tmp20._args)
            # State 108694
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.0', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 108695
                if len(subjects21) >= 1:
                    tmp23 = subjects21.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.1', tmp23)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 108696
                        if len(subjects21) == 0:
                            pass
                            # State 108697
                            if len(subjects) == 0:
                                pass
                                # 2: acos(x*c)
                                yield 2, subst2
                    subjects21.appendleft(tmp23)
            if len(subjects21) >= 1 and isinstance(subjects21[0], Mul):
                tmp25 = subjects21.popleft()
                associative1 = tmp25
                associative_type1 = type(tmp25)
                subjects26 = deque(tmp25._args)
                matcher = CommutativeMatcher108699.get()
                tmp27 = subjects26
                subjects26 = []
                for s in tmp27:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp27, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 108700
                        if len(subjects21) == 0:
                            pass
                            # State 108701
                            if len(subjects) == 0:
                                pass
                                # 2: acos(x*c)
                                yield 2, subst1
                subjects21.appendleft(tmp25)
            subjects.appendleft(tmp20)
        if len(subjects) >= 1 and isinstance(subjects[0], atan):
            tmp28 = subjects.popleft()
            subjects29 = deque(tmp28._args)
            # State 113320
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.0', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 113321
                if len(subjects29) >= 1:
                    tmp31 = subjects29.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.1', tmp31)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 113322
                        if len(subjects29) == 0:
                            pass
                            # State 113323
                            if len(subjects) == 0:
                                pass
                                # 3: atan(x*c)
                                yield 3, subst2
                    subjects29.appendleft(tmp31)
            if len(subjects29) >= 1 and isinstance(subjects29[0], Mul):
                tmp33 = subjects29.popleft()
                associative1 = tmp33
                associative_type1 = type(tmp33)
                subjects34 = deque(tmp33._args)
                matcher = CommutativeMatcher113325.get()
                tmp35 = subjects34
                subjects34 = []
                for s in tmp35:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp35, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 113326
                        if len(subjects29) == 0:
                            pass
                            # State 113327
                            if len(subjects) == 0:
                                pass
                                # 3: atan(x*c)
                                yield 3, subst1
                subjects29.appendleft(tmp33)
            subjects.appendleft(tmp28)
        if len(subjects) >= 1 and isinstance(subjects[0], acot):
            tmp36 = subjects.popleft()
            subjects37 = deque(tmp36._args)
            # State 113363
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.0', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 113364
                if len(subjects37) >= 1:
                    tmp39 = subjects37.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.1', tmp39)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 113365
                        if len(subjects37) == 0:
                            pass
                            # State 113366
                            if len(subjects) == 0:
                                pass
                                # 4: acot(x*c)
                                yield 4, subst2
                    subjects37.appendleft(tmp39)
            if len(subjects37) >= 1 and isinstance(subjects37[0], Mul):
                tmp41 = subjects37.popleft()
                associative1 = tmp41
                associative_type1 = type(tmp41)
                subjects42 = deque(tmp41._args)
                matcher = CommutativeMatcher113368.get()
                tmp43 = subjects42
                subjects42 = []
                for s in tmp43:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp43, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 113369
                        if len(subjects37) == 0:
                            pass
                            # State 113370
                            if len(subjects) == 0:
                                pass
                                # 4: acot(x*c)
                                yield 4, subst1
                subjects37.appendleft(tmp41)
            subjects.appendleft(tmp36)
        if len(subjects) >= 1 and isinstance(subjects[0], asinh):
            tmp44 = subjects.popleft()
            subjects45 = deque(tmp44._args)
            # State 138357
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.0', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 138358
                if len(subjects45) >= 1:
                    tmp47 = subjects45.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.1', tmp47)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 138359
                        if len(subjects45) == 0:
                            pass
                            # State 138360
                            if len(subjects) == 0:
                                pass
                                # 5: asinh(x*c)
                                yield 5, subst2
                    subjects45.appendleft(tmp47)
            if len(subjects45) >= 1 and isinstance(subjects45[0], Mul):
                tmp49 = subjects45.popleft()
                associative1 = tmp49
                associative_type1 = type(tmp49)
                subjects50 = deque(tmp49._args)
                matcher = CommutativeMatcher138362.get()
                tmp51 = subjects50
                subjects50 = []
                for s in tmp51:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp51, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 138363
                        if len(subjects45) == 0:
                            pass
                            # State 138364
                            if len(subjects) == 0:
                                pass
                                # 5: asinh(x*c)
                                yield 5, subst1
                subjects45.appendleft(tmp49)
            subjects.appendleft(tmp44)
        if len(subjects) >= 1 and isinstance(subjects[0], acosh):
            tmp52 = subjects.popleft()
            subjects53 = deque(tmp52._args)
            # State 138641
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.0', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 138642
                if len(subjects53) >= 1:
                    tmp55 = subjects53.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.1', tmp55)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 138643
                        if len(subjects53) == 0:
                            pass
                            # State 138644
                            if len(subjects) == 0:
                                pass
                                # 6: acosh(x*c)
                                yield 6, subst2
                    subjects53.appendleft(tmp55)
            if len(subjects53) >= 1 and isinstance(subjects53[0], Mul):
                tmp57 = subjects53.popleft()
                associative1 = tmp57
                associative_type1 = type(tmp57)
                subjects58 = deque(tmp57._args)
                matcher = CommutativeMatcher138646.get()
                tmp59 = subjects58
                subjects58 = []
                for s in tmp59:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp59, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 138647
                        if len(subjects53) == 0:
                            pass
                            # State 138648
                            if len(subjects) == 0:
                                pass
                                # 6: acosh(x*c)
                                yield 6, subst1
                subjects53.appendleft(tmp57)
            subjects.appendleft(tmp52)
        if len(subjects) >= 1 and isinstance(subjects[0], atanh):
            tmp60 = subjects.popleft()
            subjects61 = deque(tmp60._args)
            # State 142945
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.0', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 142946
                if len(subjects61) >= 1:
                    tmp63 = subjects61.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.1', tmp63)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 142947
                        if len(subjects61) == 0:
                            pass
                            # State 142948
                            if len(subjects) == 0:
                                pass
                                # 7: atanh(x*c)
                                yield 7, subst2
                    subjects61.appendleft(tmp63)
            if len(subjects61) >= 1 and isinstance(subjects61[0], Mul):
                tmp65 = subjects61.popleft()
                associative1 = tmp65
                associative_type1 = type(tmp65)
                subjects66 = deque(tmp65._args)
                matcher = CommutativeMatcher142950.get()
                tmp67 = subjects66
                subjects66 = []
                for s in tmp67:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp67, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 142951
                        if len(subjects61) == 0:
                            pass
                            # State 142952
                            if len(subjects) == 0:
                                pass
                                # 7: atanh(x*c)
                                yield 7, subst1
                subjects61.appendleft(tmp65)
            subjects.appendleft(tmp60)
        if len(subjects) >= 1 and isinstance(subjects[0], acoth):
            tmp68 = subjects.popleft()
            subjects69 = deque(tmp68._args)
            # State 142988
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.0', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 142989
                if len(subjects69) >= 1:
                    tmp71 = subjects69.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.1', tmp71)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 142990
                        if len(subjects69) == 0:
                            pass
                            # State 142991
                            if len(subjects) == 0:
                                pass
                                # 8: acoth(x*c)
                                yield 8, subst2
                    subjects69.appendleft(tmp71)
            if len(subjects69) >= 1 and isinstance(subjects69[0], Mul):
                tmp73 = subjects69.popleft()
                associative1 = tmp73
                associative_type1 = type(tmp73)
                subjects74 = deque(tmp73._args)
                matcher = CommutativeMatcher142993.get()
                tmp75 = subjects74
                subjects74 = []
                for s in tmp75:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp75, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 142994
                        if len(subjects69) == 0:
                            pass
                            # State 142995
                            if len(subjects) == 0:
                                pass
                                # 8: acoth(x*c)
                                yield 8, subst1
                subjects69.appendleft(tmp73)
            subjects.appendleft(tmp68)
        return
        yield


from .generated_part002856 import *
from .generated_part002863 import *
from .generated_part002861 import *
from .generated_part002862 import *
from matchpy.matching.many_to_one import CommutativeMatcher
from .generated_part002859 import *
from .generated_part002864 import *
from collections import deque
from .generated_part002865 import *
from .generated_part002860 import *
from .generated_part002858 import *
from matchpy.utils import VariableWithCount
from multiset import Multiset