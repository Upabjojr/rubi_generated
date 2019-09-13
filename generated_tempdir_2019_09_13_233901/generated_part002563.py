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

class CommutativeMatcher22371(CommutativeMatcher):
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
]),
    7: (7, Multiset({7: 1}), [
      (VariableWithCount('i2.2.1.2.0', 1, 1, S(1)), Mul)
]),
    8: (8, Multiset({8: 1}), [
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
        if CommutativeMatcher22371._instance is None:
            CommutativeMatcher22371._instance = CommutativeMatcher22371()
        return CommutativeMatcher22371._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 22370
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.2.2', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 22372
            subst2 = Substitution(subst1)
            try:
                subst2.try_add_variable('i2.2.1.2.2.0', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 22373
                subst3 = Substitution(subst2)
                try:
                    subst3.try_add_variable('i2.2.1.2.2.2', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 22374
                    subst4 = Substitution(subst3)
                    try:
                        subst4.try_add_variable('i2.2.1.2.2.2.0', S(0))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 22375
                        subst5 = Substitution(subst4)
                        try:
                            subst5.try_add_variable('i2.2.1.2.2.2.1.0_1', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 22376
                            if len(subjects) >= 1:
                                tmp6 = subjects.popleft()
                                subst6 = Substitution(subst5)
                                try:
                                    subst6.try_add_variable('i2.2.1.2.2.2.1.0', tmp6)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 22377
                                    if len(subjects) == 0:
                                        pass
                                        # 0: (d*(e + x*f)**p)**q
                                subjects.appendleft(tmp6)
                        subst5 = Substitution(subst4)
                        try:
                            subst5.try_add_variable('i2.2.1.2.2.2.1.0', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 33878
                            if len(subjects) >= 1 and isinstance(subjects[0], Pow):
                                tmp9 = subjects.popleft()
                                subjects10 = deque(tmp9._args)
                                # State 33879
                                if len(subjects10) >= 1:
                                    tmp11 = subjects10.popleft()
                                    subst6 = Substitution(subst5)
                                    try:
                                        subst6.try_add_variable('i2.2.1.2.2.2.1.1', tmp11)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 33880
                                        if len(subjects10) >= 1:
                                            tmp13 = subjects10.popleft()
                                            subst7 = Substitution(subst6)
                                            try:
                                                subst7.try_add_variable('i2.2.1.2.2.2.1.2', tmp13)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 33881
                                                if len(subjects10) == 0:
                                                    pass
                                                    # State 33882
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 5: (d*(e + f*x**m)**p)**q
                                            subjects10.appendleft(tmp13)
                                    subjects10.appendleft(tmp11)
                                subjects.appendleft(tmp9)
                        if len(subjects) >= 1 and isinstance(subjects[0], Mul):
                            tmp15 = subjects.popleft()
                            associative1 = tmp15
                            associative_type1 = type(tmp15)
                            subjects16 = deque(tmp15._args)
                            matcher = CommutativeMatcher22379.get()
                            tmp17 = subjects16
                            subjects16 = []
                            for s in tmp17:
                                matcher.add_subject(s)
                            for pattern_index, subst5 in matcher.match(tmp17, subst4):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 22380
                                    if len(subjects) == 0:
                                        pass
                                        # 0: (d*(e + x*f)**p)**q
                                if pattern_index == 1:
                                    pass
                                    # State 33887
                                    if len(subjects) == 0:
                                        pass
                                        # 5: (d*(e + f*x**m)**p)**q
                            subjects.appendleft(tmp15)
                    if len(subjects) >= 1:
                        tmp18 = subjects.popleft()
                        subst4 = Substitution(subst3)
                        try:
                            subst4.try_add_variable('i2.2.1.2.2.1', tmp18)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 45420
                            if len(subjects) == 0:
                                pass
                                # 7: (d*v**p)**q
                        subjects.appendleft(tmp18)
                    if len(subjects) >= 1 and isinstance(subjects[0], Add):
                        tmp20 = subjects.popleft()
                        associative1 = tmp20
                        associative_type1 = type(tmp20)
                        subjects21 = deque(tmp20._args)
                        matcher = CommutativeMatcher22382.get()
                        tmp22 = subjects21
                        subjects21 = []
                        for s in tmp22:
                            matcher.add_subject(s)
                        for pattern_index, subst4 in matcher.match(tmp22, subst3):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 22388
                                if len(subjects) == 0:
                                    pass
                                    # 0: (d*(e + x*f)**p)**q
                            if pattern_index == 1:
                                pass
                                # State 28420
                                if len(subjects) == 0:
                                    pass
                                    # 3: (d*(e + f*x**m)**p)**q
                            if pattern_index == 2:
                                pass
                                # State 33888
                                if len(subjects) == 0:
                                    pass
                                    # 5: (d*(e + f*x**m)**p)**q
                            if pattern_index == 3:
                                pass
                                # State 43608
                                if len(subjects) == 0:
                                    pass
                                    # 6: (d*(e + f*x + g*x**2)**p)**q
                        subjects.appendleft(tmp20)
                    if len(subjects) >= 1 and isinstance(subjects[0], Mul):
                        tmp23 = subjects.popleft()
                        associative1 = tmp23
                        associative_type1 = type(tmp23)
                        subjects24 = deque(tmp23._args)
                        matcher = CommutativeMatcher30289.get()
                        tmp25 = subjects24
                        subjects24 = []
                        for s in tmp25:
                            matcher.add_subject(s)
                        for pattern_index, subst4 in matcher.match(tmp25, subst3):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 30313
                                if len(subjects) == 0:
                                    pass
                                    # 4: (d*(x**m*(f + e*x**r))**p)**q
                        subjects.appendleft(tmp23)
                if len(subjects) >= 1 and isinstance(subjects[0], Pow):
                    tmp26 = subjects.popleft()
                    subjects27 = deque(tmp26._args)
                    # State 22389
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.2.1.2.2.2.0', S(0))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 22390
                        subst4 = Substitution(subst3)
                        try:
                            subst4.try_add_variable('i2.2.1.2.2.2.1.0_1', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 22391
                            if len(subjects27) >= 1:
                                tmp30 = subjects27.popleft()
                                subst5 = Substitution(subst4)
                                try:
                                    subst5.try_add_variable('i2.2.1.2.2.2.1.0', tmp30)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 22392
                                    subst6 = Substitution(subst5)
                                    try:
                                        subst6.try_add_variable('i2.2.1.2.2.2', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 22393
                                        if len(subjects27) == 0:
                                            pass
                                            # State 22394
                                            if len(subjects) == 0:
                                                pass
                                                # 0: (d*(e + x*f)**p)**q
                                    if len(subjects27) >= 1:
                                        tmp33 = subjects27.popleft()
                                        subst6 = Substitution(subst5)
                                        try:
                                            subst6.try_add_variable('i2.2.1.2.2.2', tmp33)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 22393
                                            if len(subjects27) == 0:
                                                pass
                                                # State 22394
                                                if len(subjects) == 0:
                                                    pass
                                                    # 0: (d*(e + x*f)**p)**q
                                        subjects27.appendleft(tmp33)
                                subjects27.appendleft(tmp30)
                        subst4 = Substitution(subst3)
                        try:
                            subst4.try_add_variable('i2.2.1.2.2.2.1.0', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 33889
                            if len(subjects27) >= 1 and isinstance(subjects27[0], Pow):
                                tmp36 = subjects27.popleft()
                                subjects37 = deque(tmp36._args)
                                # State 33890
                                if len(subjects37) >= 1:
                                    tmp38 = subjects37.popleft()
                                    subst5 = Substitution(subst4)
                                    try:
                                        subst5.try_add_variable('i2.2.1.2.2.2.1.1', tmp38)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 33891
                                        if len(subjects37) >= 1:
                                            tmp40 = subjects37.popleft()
                                            subst6 = Substitution(subst5)
                                            try:
                                                subst6.try_add_variable('i2.2.1.2.2.2.1.2', tmp40)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 33892
                                                if len(subjects37) == 0:
                                                    pass
                                                    # State 33893
                                                    subst7 = Substitution(subst6)
                                                    try:
                                                        subst7.try_add_variable('i2.2.1.2.2.2', 1)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 33894
                                                        if len(subjects27) == 0:
                                                            pass
                                                            # State 33895
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 5: (d*(e + f*x**m)**p)**q
                                                    if len(subjects27) >= 1:
                                                        tmp43 = subjects27.popleft()
                                                        subst7 = Substitution(subst6)
                                                        try:
                                                            subst7.try_add_variable('i2.2.1.2.2.2', tmp43)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            # State 33894
                                                            if len(subjects27) == 0:
                                                                pass
                                                                # State 33895
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 5: (d*(e + f*x**m)**p)**q
                                                        subjects27.appendleft(tmp43)
                                            subjects37.appendleft(tmp40)
                                    subjects37.appendleft(tmp38)
                                subjects27.appendleft(tmp36)
                        if len(subjects27) >= 1 and isinstance(subjects27[0], Mul):
                            tmp45 = subjects27.popleft()
                            associative1 = tmp45
                            associative_type1 = type(tmp45)
                            subjects46 = deque(tmp45._args)
                            matcher = CommutativeMatcher22396.get()
                            tmp47 = subjects46
                            subjects46 = []
                            for s in tmp47:
                                matcher.add_subject(s)
                            for pattern_index, subst4 in matcher.match(tmp47, subst3):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 22397
                                    subst5 = Substitution(subst4)
                                    try:
                                        subst5.try_add_variable('i2.2.1.2.2.2', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 22398
                                        if len(subjects27) == 0:
                                            pass
                                            # State 22399
                                            if len(subjects) == 0:
                                                pass
                                                # 0: (d*(e + x*f)**p)**q
                                    if len(subjects27) >= 1:
                                        tmp49 = []
                                        tmp49.append(subjects27.popleft())
                                        while True:
                                            if len(tmp49) > 1:
                                                tmp50 = create_operation_expression(associative1, tmp49)
                                            elif len(tmp49) == 1:
                                                tmp50 = tmp49[0]
                                            else:
                                                assert False, "Unreachable"
                                            subst5 = Substitution(subst4)
                                            try:
                                                subst5.try_add_variable('i2.2.1.2.2.2', tmp50)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 22398
                                                if len(subjects27) == 0:
                                                    pass
                                                    # State 22399
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 0: (d*(e + x*f)**p)**q
                                            if len(subjects27) == 0:
                                                break
                                            tmp49.append(subjects27.popleft())
                                        subjects27.extendleft(reversed(tmp49))
                                if pattern_index == 1:
                                    pass
                                    # State 33900
                                    subst5 = Substitution(subst4)
                                    try:
                                        subst5.try_add_variable('i2.2.1.2.2.2', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 33901
                                        if len(subjects27) == 0:
                                            pass
                                            # State 33902
                                            if len(subjects) == 0:
                                                pass
                                                # 5: (d*(e + f*x**m)**p)**q
                                    if len(subjects27) >= 1:
                                        tmp53 = []
                                        tmp53.append(subjects27.popleft())
                                        while True:
                                            if len(tmp53) > 1:
                                                tmp54 = create_operation_expression(associative1, tmp53)
                                            elif len(tmp53) == 1:
                                                tmp54 = tmp53[0]
                                            else:
                                                assert False, "Unreachable"
                                            subst5 = Substitution(subst4)
                                            try:
                                                subst5.try_add_variable('i2.2.1.2.2.2', tmp54)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 33901
                                                if len(subjects27) == 0:
                                                    pass
                                                    # State 33902
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 5: (d*(e + f*x**m)**p)**q
                                            if len(subjects27) == 0:
                                                break
                                            tmp53.append(subjects27.popleft())
                                        subjects27.extendleft(reversed(tmp53))
                            subjects27.appendleft(tmp45)
                    if len(subjects27) >= 1:
                        tmp56 = subjects27.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.2.2.1', tmp56)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 25510
                            if len(subjects27) >= 1:
                                tmp58 = subjects27.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.2.1.2.2.2', tmp58)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 25511
                                    if len(subjects27) == 0:
                                        pass
                                        # State 25512
                                        if len(subjects) == 0:
                                            pass
                                            # 1: (d*v**p)**q
                                subjects27.appendleft(tmp58)
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i2.2.1.2.2.2', 1)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 45421
                                if len(subjects27) == 0:
                                    pass
                                    # State 45422
                                    if len(subjects) == 0:
                                        pass
                                        # 7: (d*v**p)**q
                            if len(subjects27) >= 1:
                                tmp61 = subjects27.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.2.1.2.2.2', tmp61)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 45421
                                    if len(subjects27) == 0:
                                        pass
                                        # State 45422
                                        if len(subjects) == 0:
                                            pass
                                            # 7: (d*v**p)**q
                                subjects27.appendleft(tmp61)
                        subjects27.appendleft(tmp56)
                    if len(subjects27) >= 1 and isinstance(subjects27[0], Add):
                        tmp63 = subjects27.popleft()
                        associative1 = tmp63
                        associative_type1 = type(tmp63)
                        subjects64 = deque(tmp63._args)
                        matcher = CommutativeMatcher22401.get()
                        tmp65 = subjects64
                        subjects64 = []
                        for s in tmp65:
                            matcher.add_subject(s)
                        for pattern_index, subst3 in matcher.match(tmp65, subst2):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 22407
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.2.1.2.2.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 22408
                                    if len(subjects27) == 0:
                                        pass
                                        # State 22409
                                        if len(subjects) == 0:
                                            pass
                                            # 0: (d*(e + x*f)**p)**q
                                if len(subjects27) >= 1:
                                    tmp67 = []
                                    tmp67.append(subjects27.popleft())
                                    while True:
                                        if len(tmp67) > 1:
                                            tmp68 = create_operation_expression(associative1, tmp67)
                                        elif len(tmp67) == 1:
                                            tmp68 = tmp67[0]
                                        else:
                                            assert False, "Unreachable"
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.2.1.2.2.2', tmp68)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 22408
                                            if len(subjects27) == 0:
                                                pass
                                                # State 22409
                                                if len(subjects) == 0:
                                                    pass
                                                    # 0: (d*(e + x*f)**p)**q
                                        if len(subjects27) == 0:
                                            break
                                        tmp67.append(subjects27.popleft())
                                    subjects27.extendleft(reversed(tmp67))
                            if pattern_index == 1:
                                pass
                                # State 28431
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.2.1.2.2.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 28432
                                    if len(subjects27) == 0:
                                        pass
                                        # State 28433
                                        if len(subjects) == 0:
                                            pass
                                            # 3: (d*(e + f*x**m)**p)**q
                                if len(subjects27) >= 1:
                                    tmp71 = []
                                    tmp71.append(subjects27.popleft())
                                    while True:
                                        if len(tmp71) > 1:
                                            tmp72 = create_operation_expression(associative1, tmp71)
                                        elif len(tmp71) == 1:
                                            tmp72 = tmp71[0]
                                        else:
                                            assert False, "Unreachable"
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.2.1.2.2.2', tmp72)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 28432
                                            if len(subjects27) == 0:
                                                pass
                                                # State 28433
                                                if len(subjects) == 0:
                                                    pass
                                                    # 3: (d*(e + f*x**m)**p)**q
                                        if len(subjects27) == 0:
                                            break
                                        tmp71.append(subjects27.popleft())
                                    subjects27.extendleft(reversed(tmp71))
                            if pattern_index == 2:
                                pass
                                # State 33903
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.2.1.2.2.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 33904
                                    if len(subjects27) == 0:
                                        pass
                                        # State 33905
                                        if len(subjects) == 0:
                                            pass
                                            # 5: (d*(e + f*x**m)**p)**q
                                if len(subjects27) >= 1:
                                    tmp75 = []
                                    tmp75.append(subjects27.popleft())
                                    while True:
                                        if len(tmp75) > 1:
                                            tmp76 = create_operation_expression(associative1, tmp75)
                                        elif len(tmp75) == 1:
                                            tmp76 = tmp75[0]
                                        else:
                                            assert False, "Unreachable"
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.2.1.2.2.2', tmp76)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 33904
                                            if len(subjects27) == 0:
                                                pass
                                                # State 33905
                                                if len(subjects) == 0:
                                                    pass
                                                    # 5: (d*(e + f*x**m)**p)**q
                                        if len(subjects27) == 0:
                                            break
                                        tmp75.append(subjects27.popleft())
                                    subjects27.extendleft(reversed(tmp75))
                            if pattern_index == 3:
                                pass
                                # State 43616
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.2.1.2.2.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 43617
                                    if len(subjects27) == 0:
                                        pass
                                        # State 43618
                                        if len(subjects) == 0:
                                            pass
                                            # 6: (d*(e + f*x + g*x**2)**p)**q
                                if len(subjects27) >= 1:
                                    tmp79 = []
                                    tmp79.append(subjects27.popleft())
                                    while True:
                                        if len(tmp79) > 1:
                                            tmp80 = create_operation_expression(associative1, tmp79)
                                        elif len(tmp79) == 1:
                                            tmp80 = tmp79[0]
                                        else:
                                            assert False, "Unreachable"
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.2.1.2.2.2', tmp80)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 43617
                                            if len(subjects27) == 0:
                                                pass
                                                # State 43618
                                                if len(subjects) == 0:
                                                    pass
                                                    # 6: (d*(e + f*x + g*x**2)**p)**q
                                        if len(subjects27) == 0:
                                            break
                                        tmp79.append(subjects27.popleft())
                                    subjects27.extendleft(reversed(tmp79))
                        subjects27.appendleft(tmp63)
                    if len(subjects27) >= 1 and isinstance(subjects27[0], Mul):
                        tmp82 = subjects27.popleft()
                        associative1 = tmp82
                        associative_type1 = type(tmp82)
                        subjects83 = deque(tmp82._args)
                        matcher = CommutativeMatcher30315.get()
                        tmp84 = subjects83
                        subjects83 = []
                        for s in tmp84:
                            matcher.add_subject(s)
                        for pattern_index, subst3 in matcher.match(tmp84, subst2):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 30339
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.2.1.2.2.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 30340
                                    if len(subjects27) == 0:
                                        pass
                                        # State 30341
                                        if len(subjects) == 0:
                                            pass
                                            # 4: (d*(x**m*(f + e*x**r))**p)**q
                                if len(subjects27) >= 1:
                                    tmp86 = []
                                    tmp86.append(subjects27.popleft())
                                    while True:
                                        if len(tmp86) > 1:
                                            tmp87 = create_operation_expression(associative1, tmp86)
                                        elif len(tmp86) == 1:
                                            tmp87 = tmp86[0]
                                        else:
                                            assert False, "Unreachable"
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.2.1.2.2.2', tmp87)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 30340
                                            if len(subjects27) == 0:
                                                pass
                                                # State 30341
                                                if len(subjects) == 0:
                                                    pass
                                                    # 4: (d*(x**m*(f + e*x**r))**p)**q
                                        if len(subjects27) == 0:
                                            break
                                        tmp86.append(subjects27.popleft())
                                    subjects27.extendleft(reversed(tmp86))
                        subjects27.appendleft(tmp82)
                    subjects.appendleft(tmp26)
            if len(subjects) >= 1:
                tmp89 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.1', tmp89)
                except ValueError:
                    pass
                else:
                    pass
                    # State 53219
                    if len(subjects) == 0:
                        pass
                        # 8: RFx**p
                subjects.appendleft(tmp89)
            if len(subjects) >= 1 and isinstance(subjects[0], Mul):
                tmp91 = subjects.popleft()
                associative1 = tmp91
                associative_type1 = type(tmp91)
                subjects92 = deque(tmp91._args)
                matcher = CommutativeMatcher22411.get()
                tmp93 = subjects92
                subjects92 = []
                for s in tmp93:
                    matcher.add_subject(s)
                for pattern_index, subst2 in matcher.match(tmp93, subst1):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 22448
                        if len(subjects) == 0:
                            pass
                            # 0: (d*(e + x*f)**p)**q
                    if pattern_index == 1:
                        pass
                        # State 25516
                        if len(subjects) == 0:
                            pass
                            # 1: (d*v**p)**q
                    if pattern_index == 2:
                        pass
                        # State 28458
                        if len(subjects) == 0:
                            pass
                            # 3: (d*(e + f*x**m)**p)**q
                    if pattern_index == 3:
                        pass
                        # State 30396
                        if len(subjects) == 0:
                            pass
                            # 4: (d*(x**m*(f + e*x**r))**p)**q
                    if pattern_index == 4:
                        pass
                        # State 33934
                        if len(subjects) == 0:
                            pass
                            # 5: (d*(e + f*x**m)**p)**q
                    if pattern_index == 5:
                        pass
                        # State 43637
                        if len(subjects) == 0:
                            pass
                            # 6: (d*(e + f*x + g*x**2)**p)**q
                    if pattern_index == 6:
                        pass
                        # State 45426
                        if len(subjects) == 0:
                            pass
                            # 7: (d*v**p)**q
                subjects.appendleft(tmp91)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.2.1.0', S(0))
        except ValueError:
            pass
        else:
            pass
            # State 26016
            subst2 = Substitution(subst1)
            try:
                subst2.try_add_variable('i2.2.1.2.1.1.0_1', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 26017
                if len(subjects) >= 1:
                    tmp96 = subjects.popleft()
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.2.1.2.1.1.0', tmp96)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 26018
                        if len(subjects) == 0:
                            pass
                            # 2: e + x*f
                    subjects.appendleft(tmp96)
            if len(subjects) >= 1 and isinstance(subjects[0], Mul):
                tmp98 = subjects.popleft()
                associative1 = tmp98
                associative_type1 = type(tmp98)
                subjects99 = deque(tmp98._args)
                matcher = CommutativeMatcher26020.get()
                tmp100 = subjects99
                subjects99 = []
                for s in tmp100:
                    matcher.add_subject(s)
                for pattern_index, subst2 in matcher.match(tmp100, subst1):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 26021
                        if len(subjects) == 0:
                            pass
                            # 2: e + x*f
                subjects.appendleft(tmp98)
        if len(subjects) >= 1 and isinstance(subjects[0], Pow):
            tmp101 = subjects.popleft()
            subjects102 = deque(tmp101._args)
            # State 22449
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.2.0', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 22450
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.2.2', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 22451
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.2.1.2.2.2.0', S(0))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 22452
                        subst4 = Substitution(subst3)
                        try:
                            subst4.try_add_variable('i2.2.1.2.2.2.1.0_1', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 22453
                            if len(subjects102) >= 1:
                                tmp107 = subjects102.popleft()
                                subst5 = Substitution(subst4)
                                try:
                                    subst5.try_add_variable('i2.2.1.2.2.2.1.0', tmp107)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 22454
                                    subst6 = Substitution(subst5)
                                    try:
                                        subst6.try_add_variable('i2.2.1.2.2', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 22455
                                        if len(subjects102) == 0:
                                            pass
                                            # State 22456
                                            if len(subjects) == 0:
                                                pass
                                                # 0: (d*(e + x*f)**p)**q
                                    if len(subjects102) >= 1:
                                        tmp110 = subjects102.popleft()
                                        subst6 = Substitution(subst5)
                                        try:
                                            subst6.try_add_variable('i2.2.1.2.2', tmp110)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 22455
                                            if len(subjects102) == 0:
                                                pass
                                                # State 22456
                                                if len(subjects) == 0:
                                                    pass
                                                    # 0: (d*(e + x*f)**p)**q
                                        subjects102.appendleft(tmp110)
                                subjects102.appendleft(tmp107)
                        subst4 = Substitution(subst3)
                        try:
                            subst4.try_add_variable('i2.2.1.2.2.2.1.0', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 33935
                            if len(subjects102) >= 1 and isinstance(subjects102[0], Pow):
                                tmp113 = subjects102.popleft()
                                subjects114 = deque(tmp113._args)
                                # State 33936
                                if len(subjects114) >= 1:
                                    tmp115 = subjects114.popleft()
                                    subst5 = Substitution(subst4)
                                    try:
                                        subst5.try_add_variable('i2.2.1.2.2.2.1.1', tmp115)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 33937
                                        if len(subjects114) >= 1:
                                            tmp117 = subjects114.popleft()
                                            subst6 = Substitution(subst5)
                                            try:
                                                subst6.try_add_variable('i2.2.1.2.2.2.1.2', tmp117)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 33938
                                                if len(subjects114) == 0:
                                                    pass
                                                    # State 33939
                                                    subst7 = Substitution(subst6)
                                                    try:
                                                        subst7.try_add_variable('i2.2.1.2.2', 1)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 33940
                                                        if len(subjects102) == 0:
                                                            pass
                                                            # State 33941
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 5: (d*(e + f*x**m)**p)**q
                                                    if len(subjects102) >= 1:
                                                        tmp120 = subjects102.popleft()
                                                        subst7 = Substitution(subst6)
                                                        try:
                                                            subst7.try_add_variable('i2.2.1.2.2', tmp120)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            # State 33940
                                                            if len(subjects102) == 0:
                                                                pass
                                                                # State 33941
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 5: (d*(e + f*x**m)**p)**q
                                                        subjects102.appendleft(tmp120)
                                            subjects114.appendleft(tmp117)
                                    subjects114.appendleft(tmp115)
                                subjects102.appendleft(tmp113)
                        if len(subjects102) >= 1 and isinstance(subjects102[0], Mul):
                            tmp122 = subjects102.popleft()
                            associative1 = tmp122
                            associative_type1 = type(tmp122)
                            subjects123 = deque(tmp122._args)
                            matcher = CommutativeMatcher22458.get()
                            tmp124 = subjects123
                            subjects123 = []
                            for s in tmp124:
                                matcher.add_subject(s)
                            for pattern_index, subst4 in matcher.match(tmp124, subst3):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 22459
                                    subst5 = Substitution(subst4)
                                    try:
                                        subst5.try_add_variable('i2.2.1.2.2', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 22460
                                        if len(subjects102) == 0:
                                            pass
                                            # State 22461
                                            if len(subjects) == 0:
                                                pass
                                                # 0: (d*(e + x*f)**p)**q
                                    if len(subjects102) >= 1:
                                        tmp126 = []
                                        tmp126.append(subjects102.popleft())
                                        while True:
                                            if len(tmp126) > 1:
                                                tmp127 = create_operation_expression(associative1, tmp126)
                                            elif len(tmp126) == 1:
                                                tmp127 = tmp126[0]
                                            else:
                                                assert False, "Unreachable"
                                            subst5 = Substitution(subst4)
                                            try:
                                                subst5.try_add_variable('i2.2.1.2.2', tmp127)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 22460
                                                if len(subjects102) == 0:
                                                    pass
                                                    # State 22461
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 0: (d*(e + x*f)**p)**q
                                            if len(subjects102) == 0:
                                                break
                                            tmp126.append(subjects102.popleft())
                                        subjects102.extendleft(reversed(tmp126))
                                if pattern_index == 1:
                                    pass
                                    # State 33946
                                    subst5 = Substitution(subst4)
                                    try:
                                        subst5.try_add_variable('i2.2.1.2.2', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 33947
                                        if len(subjects102) == 0:
                                            pass
                                            # State 33948
                                            if len(subjects) == 0:
                                                pass
                                                # 5: (d*(e + f*x**m)**p)**q
                                    if len(subjects102) >= 1:
                                        tmp130 = []
                                        tmp130.append(subjects102.popleft())
                                        while True:
                                            if len(tmp130) > 1:
                                                tmp131 = create_operation_expression(associative1, tmp130)
                                            elif len(tmp130) == 1:
                                                tmp131 = tmp130[0]
                                            else:
                                                assert False, "Unreachable"
                                            subst5 = Substitution(subst4)
                                            try:
                                                subst5.try_add_variable('i2.2.1.2.2', tmp131)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 33947
                                                if len(subjects102) == 0:
                                                    pass
                                                    # State 33948
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 5: (d*(e + f*x**m)**p)**q
                                            if len(subjects102) == 0:
                                                break
                                            tmp130.append(subjects102.popleft())
                                        subjects102.extendleft(reversed(tmp130))
                            subjects102.appendleft(tmp122)
                    if len(subjects102) >= 1:
                        tmp133 = subjects102.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.2.2.1', tmp133)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 45427
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i2.2.1.2.2', 1)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 45428
                                if len(subjects102) == 0:
                                    pass
                                    # State 45429
                                    if len(subjects) == 0:
                                        pass
                                        # 7: (d*v**p)**q
                            if len(subjects102) >= 1:
                                tmp136 = subjects102.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.2.1.2.2', tmp136)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 45428
                                    if len(subjects102) == 0:
                                        pass
                                        # State 45429
                                        if len(subjects) == 0:
                                            pass
                                            # 7: (d*v**p)**q
                                subjects102.appendleft(tmp136)
                        subjects102.appendleft(tmp133)
                    if len(subjects102) >= 1 and isinstance(subjects102[0], Add):
                        tmp138 = subjects102.popleft()
                        associative1 = tmp138
                        associative_type1 = type(tmp138)
                        subjects139 = deque(tmp138._args)
                        matcher = CommutativeMatcher22463.get()
                        tmp140 = subjects139
                        subjects139 = []
                        for s in tmp140:
                            matcher.add_subject(s)
                        for pattern_index, subst3 in matcher.match(tmp140, subst2):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 22469
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.2.1.2.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 22470
                                    if len(subjects102) == 0:
                                        pass
                                        # State 22471
                                        if len(subjects) == 0:
                                            pass
                                            # 0: (d*(e + x*f)**p)**q
                                if len(subjects102) >= 1:
                                    tmp142 = []
                                    tmp142.append(subjects102.popleft())
                                    while True:
                                        if len(tmp142) > 1:
                                            tmp143 = create_operation_expression(associative1, tmp142)
                                        elif len(tmp142) == 1:
                                            tmp143 = tmp142[0]
                                        else:
                                            assert False, "Unreachable"
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.2.1.2.2', tmp143)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 22470
                                            if len(subjects102) == 0:
                                                pass
                                                # State 22471
                                                if len(subjects) == 0:
                                                    pass
                                                    # 0: (d*(e + x*f)**p)**q
                                        if len(subjects102) == 0:
                                            break
                                        tmp142.append(subjects102.popleft())
                                    subjects102.extendleft(reversed(tmp142))
                            if pattern_index == 1:
                                pass
                                # State 28469
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.2.1.2.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 28470
                                    if len(subjects102) == 0:
                                        pass
                                        # State 28471
                                        if len(subjects) == 0:
                                            pass
                                            # 3: (d*(e + f*x**m)**p)**q
                                if len(subjects102) >= 1:
                                    tmp146 = []
                                    tmp146.append(subjects102.popleft())
                                    while True:
                                        if len(tmp146) > 1:
                                            tmp147 = create_operation_expression(associative1, tmp146)
                                        elif len(tmp146) == 1:
                                            tmp147 = tmp146[0]
                                        else:
                                            assert False, "Unreachable"
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.2.1.2.2', tmp147)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 28470
                                            if len(subjects102) == 0:
                                                pass
                                                # State 28471
                                                if len(subjects) == 0:
                                                    pass
                                                    # 3: (d*(e + f*x**m)**p)**q
                                        if len(subjects102) == 0:
                                            break
                                        tmp146.append(subjects102.popleft())
                                    subjects102.extendleft(reversed(tmp146))
                            if pattern_index == 2:
                                pass
                                # State 33949
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.2.1.2.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 33950
                                    if len(subjects102) == 0:
                                        pass
                                        # State 33951
                                        if len(subjects) == 0:
                                            pass
                                            # 5: (d*(e + f*x**m)**p)**q
                                if len(subjects102) >= 1:
                                    tmp150 = []
                                    tmp150.append(subjects102.popleft())
                                    while True:
                                        if len(tmp150) > 1:
                                            tmp151 = create_operation_expression(associative1, tmp150)
                                        elif len(tmp150) == 1:
                                            tmp151 = tmp150[0]
                                        else:
                                            assert False, "Unreachable"
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.2.1.2.2', tmp151)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 33950
                                            if len(subjects102) == 0:
                                                pass
                                                # State 33951
                                                if len(subjects) == 0:
                                                    pass
                                                    # 5: (d*(e + f*x**m)**p)**q
                                        if len(subjects102) == 0:
                                            break
                                        tmp150.append(subjects102.popleft())
                                    subjects102.extendleft(reversed(tmp150))
                            if pattern_index == 3:
                                pass
                                # State 43645
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.2.1.2.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 43646
                                    if len(subjects102) == 0:
                                        pass
                                        # State 43647
                                        if len(subjects) == 0:
                                            pass
                                            # 6: (d*(e + f*x + g*x**2)**p)**q
                                if len(subjects102) >= 1:
                                    tmp154 = []
                                    tmp154.append(subjects102.popleft())
                                    while True:
                                        if len(tmp154) > 1:
                                            tmp155 = create_operation_expression(associative1, tmp154)
                                        elif len(tmp154) == 1:
                                            tmp155 = tmp154[0]
                                        else:
                                            assert False, "Unreachable"
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.2.1.2.2', tmp155)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 43646
                                            if len(subjects102) == 0:
                                                pass
                                                # State 43647
                                                if len(subjects) == 0:
                                                    pass
                                                    # 6: (d*(e + f*x + g*x**2)**p)**q
                                        if len(subjects102) == 0:
                                            break
                                        tmp154.append(subjects102.popleft())
                                    subjects102.extendleft(reversed(tmp154))
                        subjects102.appendleft(tmp138)
                    if len(subjects102) >= 1 and isinstance(subjects102[0], Mul):
                        tmp157 = subjects102.popleft()
                        associative1 = tmp157
                        associative_type1 = type(tmp157)
                        subjects158 = deque(tmp157._args)
                        matcher = CommutativeMatcher30398.get()
                        tmp159 = subjects158
                        subjects158 = []
                        for s in tmp159:
                            matcher.add_subject(s)
                        for pattern_index, subst3 in matcher.match(tmp159, subst2):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 30422
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.2.1.2.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 30423
                                    if len(subjects102) == 0:
                                        pass
                                        # State 30424
                                        if len(subjects) == 0:
                                            pass
                                            # 4: (d*(x**m*(f + e*x**r))**p)**q
                                if len(subjects102) >= 1:
                                    tmp161 = []
                                    tmp161.append(subjects102.popleft())
                                    while True:
                                        if len(tmp161) > 1:
                                            tmp162 = create_operation_expression(associative1, tmp161)
                                        elif len(tmp161) == 1:
                                            tmp162 = tmp161[0]
                                        else:
                                            assert False, "Unreachable"
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.2.1.2.2', tmp162)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 30423
                                            if len(subjects102) == 0:
                                                pass
                                                # State 30424
                                                if len(subjects) == 0:
                                                    pass
                                                    # 4: (d*(x**m*(f + e*x**r))**p)**q
                                        if len(subjects102) == 0:
                                            break
                                        tmp161.append(subjects102.popleft())
                                    subjects102.extendleft(reversed(tmp161))
                        subjects102.appendleft(tmp157)
                if len(subjects102) >= 1 and isinstance(subjects102[0], Pow):
                    tmp164 = subjects102.popleft()
                    subjects165 = deque(tmp164._args)
                    # State 22472
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.2.2.2.0', S(0))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 22473
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.2.2.2.1.0_1', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 22474
                            if len(subjects165) >= 1:
                                tmp168 = subjects165.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.2.1.2.2.2.1.0', tmp168)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 22475
                                    subst5 = Substitution(subst4)
                                    try:
                                        subst5.try_add_variable('i2.2.1.2.2.2', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 22476
                                        if len(subjects165) == 0:
                                            pass
                                            # State 22477
                                            subst6 = Substitution(subst5)
                                            try:
                                                subst6.try_add_variable('i2.2.1.2.2', 1)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 22478
                                                if len(subjects102) == 0:
                                                    pass
                                                    # State 22479
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 0: (d*(e + x*f)**p)**q
                                            if len(subjects102) >= 1:
                                                tmp172 = subjects102.popleft()
                                                subst6 = Substitution(subst5)
                                                try:
                                                    subst6.try_add_variable('i2.2.1.2.2', tmp172)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 22478
                                                    if len(subjects102) == 0:
                                                        pass
                                                        # State 22479
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 0: (d*(e + x*f)**p)**q
                                                subjects102.appendleft(tmp172)
                                    if len(subjects165) >= 1:
                                        tmp174 = subjects165.popleft()
                                        subst5 = Substitution(subst4)
                                        try:
                                            subst5.try_add_variable('i2.2.1.2.2.2', tmp174)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 22476
                                            if len(subjects165) == 0:
                                                pass
                                                # State 22477
                                                subst6 = Substitution(subst5)
                                                try:
                                                    subst6.try_add_variable('i2.2.1.2.2', 1)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 22478
                                                    if len(subjects102) == 0:
                                                        pass
                                                        # State 22479
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 0: (d*(e + x*f)**p)**q
                                                if len(subjects102) >= 1:
                                                    tmp177 = subjects102.popleft()
                                                    subst6 = Substitution(subst5)
                                                    try:
                                                        subst6.try_add_variable('i2.2.1.2.2', tmp177)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 22478
                                                        if len(subjects102) == 0:
                                                            pass
                                                            # State 22479
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 0: (d*(e + x*f)**p)**q
                                                    subjects102.appendleft(tmp177)
                                        subjects165.appendleft(tmp174)
                                subjects165.appendleft(tmp168)
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.2.2.2.1.0', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 33952
                            if len(subjects165) >= 1 and isinstance(subjects165[0], Pow):
                                tmp180 = subjects165.popleft()
                                subjects181 = deque(tmp180._args)
                                # State 33953
                                if len(subjects181) >= 1:
                                    tmp182 = subjects181.popleft()
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i2.2.1.2.2.2.1.1', tmp182)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 33954
                                        if len(subjects181) >= 1:
                                            tmp184 = subjects181.popleft()
                                            subst5 = Substitution(subst4)
                                            try:
                                                subst5.try_add_variable('i2.2.1.2.2.2.1.2', tmp184)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 33955
                                                if len(subjects181) == 0:
                                                    pass
                                                    # State 33956
                                                    subst6 = Substitution(subst5)
                                                    try:
                                                        subst6.try_add_variable('i2.2.1.2.2.2', 1)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 33957
                                                        if len(subjects165) == 0:
                                                            pass
                                                            # State 33958
                                                            subst7 = Substitution(subst6)
                                                            try:
                                                                subst7.try_add_variable('i2.2.1.2.2', 1)
                                                            except ValueError:
                                                                pass
                                                            else:
                                                                pass
                                                                # State 33959
                                                                if len(subjects102) == 0:
                                                                    pass
                                                                    # State 33960
                                                                    if len(subjects) == 0:
                                                                        pass
                                                                        # 5: (d*(e + f*x**m)**p)**q
                                                            if len(subjects102) >= 1:
                                                                tmp188 = subjects102.popleft()
                                                                subst7 = Substitution(subst6)
                                                                try:
                                                                    subst7.try_add_variable('i2.2.1.2.2', tmp188)
                                                                except ValueError:
                                                                    pass
                                                                else:
                                                                    pass
                                                                    # State 33959
                                                                    if len(subjects102) == 0:
                                                                        pass
                                                                        # State 33960
                                                                        if len(subjects) == 0:
                                                                            pass
                                                                            # 5: (d*(e + f*x**m)**p)**q
                                                                subjects102.appendleft(tmp188)
                                                    if len(subjects165) >= 1:
                                                        tmp190 = subjects165.popleft()
                                                        subst6 = Substitution(subst5)
                                                        try:
                                                            subst6.try_add_variable('i2.2.1.2.2.2', tmp190)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            # State 33957
                                                            if len(subjects165) == 0:
                                                                pass
                                                                # State 33958
                                                                subst7 = Substitution(subst6)
                                                                try:
                                                                    subst7.try_add_variable('i2.2.1.2.2', 1)
                                                                except ValueError:
                                                                    pass
                                                                else:
                                                                    pass
                                                                    # State 33959
                                                                    if len(subjects102) == 0:
                                                                        pass
                                                                        # State 33960
                                                                        if len(subjects) == 0:
                                                                            pass
                                                                            # 5: (d*(e + f*x**m)**p)**q
                                                                if len(subjects102) >= 1:
                                                                    tmp193 = subjects102.popleft()
                                                                    subst7 = Substitution(subst6)
                                                                    try:
                                                                        subst7.try_add_variable('i2.2.1.2.2', tmp193)
                                                                    except ValueError:
                                                                        pass
                                                                    else:
                                                                        pass
                                                                        # State 33959
                                                                        if len(subjects102) == 0:
                                                                            pass
                                                                            # State 33960
                                                                            if len(subjects) == 0:
                                                                                pass
                                                                                # 5: (d*(e + f*x**m)**p)**q
                                                                    subjects102.appendleft(tmp193)
                                                        subjects165.appendleft(tmp190)
                                            subjects181.appendleft(tmp184)
                                    subjects181.appendleft(tmp182)
                                subjects165.appendleft(tmp180)
                        if len(subjects165) >= 1 and isinstance(subjects165[0], Mul):
                            tmp195 = subjects165.popleft()
                            associative1 = tmp195
                            associative_type1 = type(tmp195)
                            subjects196 = deque(tmp195._args)
                            matcher = CommutativeMatcher22481.get()
                            tmp197 = subjects196
                            subjects196 = []
                            for s in tmp197:
                                matcher.add_subject(s)
                            for pattern_index, subst3 in matcher.match(tmp197, subst2):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 22482
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i2.2.1.2.2.2', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 22483
                                        if len(subjects165) == 0:
                                            pass
                                            # State 22484
                                            subst5 = Substitution(subst4)
                                            try:
                                                subst5.try_add_variable('i2.2.1.2.2', 1)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 22485
                                                if len(subjects102) == 0:
                                                    pass
                                                    # State 22486
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 0: (d*(e + x*f)**p)**q
                                            if len(subjects102) >= 1:
                                                tmp200 = subjects102.popleft()
                                                subst5 = Substitution(subst4)
                                                try:
                                                    subst5.try_add_variable('i2.2.1.2.2', tmp200)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 22485
                                                    if len(subjects102) == 0:
                                                        pass
                                                        # State 22486
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 0: (d*(e + x*f)**p)**q
                                                subjects102.appendleft(tmp200)
                                    if len(subjects165) >= 1:
                                        tmp202 = []
                                        tmp202.append(subjects165.popleft())
                                        while True:
                                            if len(tmp202) > 1:
                                                tmp203 = create_operation_expression(associative1, tmp202)
                                            elif len(tmp202) == 1:
                                                tmp203 = tmp202[0]
                                            else:
                                                assert False, "Unreachable"
                                            subst4 = Substitution(subst3)
                                            try:
                                                subst4.try_add_variable('i2.2.1.2.2.2', tmp203)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 22483
                                                if len(subjects165) == 0:
                                                    pass
                                                    # State 22484
                                                    subst5 = Substitution(subst4)
                                                    try:
                                                        subst5.try_add_variable('i2.2.1.2.2', 1)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 22485
                                                        if len(subjects102) == 0:
                                                            pass
                                                            # State 22486
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 0: (d*(e + x*f)**p)**q
                                                    if len(subjects102) >= 1:
                                                        tmp206 = subjects102.popleft()
                                                        subst5 = Substitution(subst4)
                                                        try:
                                                            subst5.try_add_variable('i2.2.1.2.2', tmp206)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            # State 22485
                                                            if len(subjects102) == 0:
                                                                pass
                                                                # State 22486
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 0: (d*(e + x*f)**p)**q
                                                        subjects102.appendleft(tmp206)
                                            if len(subjects165) == 0:
                                                break
                                            tmp202.append(subjects165.popleft())
                                        subjects165.extendleft(reversed(tmp202))
                                if pattern_index == 1:
                                    pass
                                    # State 33965
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i2.2.1.2.2.2', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 33966
                                        if len(subjects165) == 0:
                                            pass
                                            # State 33967
                                            subst5 = Substitution(subst4)
                                            try:
                                                subst5.try_add_variable('i2.2.1.2.2', 1)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 33968
                                                if len(subjects102) == 0:
                                                    pass
                                                    # State 33969
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 5: (d*(e + f*x**m)**p)**q
                                            if len(subjects102) >= 1:
                                                tmp210 = subjects102.popleft()
                                                subst5 = Substitution(subst4)
                                                try:
                                                    subst5.try_add_variable('i2.2.1.2.2', tmp210)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 33968
                                                    if len(subjects102) == 0:
                                                        pass
                                                        # State 33969
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 5: (d*(e + f*x**m)**p)**q
                                                subjects102.appendleft(tmp210)
                                    if len(subjects165) >= 1:
                                        tmp212 = []
                                        tmp212.append(subjects165.popleft())
                                        while True:
                                            if len(tmp212) > 1:
                                                tmp213 = create_operation_expression(associative1, tmp212)
                                            elif len(tmp212) == 1:
                                                tmp213 = tmp212[0]
                                            else:
                                                assert False, "Unreachable"
                                            subst4 = Substitution(subst3)
                                            try:
                                                subst4.try_add_variable('i2.2.1.2.2.2', tmp213)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 33966
                                                if len(subjects165) == 0:
                                                    pass
                                                    # State 33967
                                                    subst5 = Substitution(subst4)
                                                    try:
                                                        subst5.try_add_variable('i2.2.1.2.2', 1)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 33968
                                                        if len(subjects102) == 0:
                                                            pass
                                                            # State 33969
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 5: (d*(e + f*x**m)**p)**q
                                                    if len(subjects102) >= 1:
                                                        tmp216 = subjects102.popleft()
                                                        subst5 = Substitution(subst4)
                                                        try:
                                                            subst5.try_add_variable('i2.2.1.2.2', tmp216)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            # State 33968
                                                            if len(subjects102) == 0:
                                                                pass
                                                                # State 33969
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 5: (d*(e + f*x**m)**p)**q
                                                        subjects102.appendleft(tmp216)
                                            if len(subjects165) == 0:
                                                break
                                            tmp212.append(subjects165.popleft())
                                        subjects165.extendleft(reversed(tmp212))
                            subjects165.appendleft(tmp195)
                    if len(subjects165) >= 1:
                        tmp218 = subjects165.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.1.2.2.1', tmp218)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 25517
                            if len(subjects165) >= 1:
                                tmp220 = subjects165.popleft()
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i2.2.1.2.2.2', tmp220)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 25518
                                    if len(subjects165) == 0:
                                        pass
                                        # State 25519
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.2.1.2.2', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 25520
                                            if len(subjects102) == 0:
                                                pass
                                                # State 25521
                                                if len(subjects) == 0:
                                                    pass
                                                    # 1: (d*v**p)**q
                                        if len(subjects102) >= 1:
                                            tmp223 = subjects102.popleft()
                                            subst4 = Substitution(subst3)
                                            try:
                                                subst4.try_add_variable('i2.2.1.2.2', tmp223)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 25520
                                                if len(subjects102) == 0:
                                                    pass
                                                    # State 25521
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 1: (d*v**p)**q
                                            subjects102.appendleft(tmp223)
                                subjects165.appendleft(tmp220)
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.2.2.2', 1)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 45430
                                if len(subjects165) == 0:
                                    pass
                                    # State 45431
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i2.2.1.2.2', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 45432
                                        if len(subjects102) == 0:
                                            pass
                                            # State 45433
                                            if len(subjects) == 0:
                                                pass
                                                # 7: (d*v**p)**q
                                    if len(subjects102) >= 1:
                                        tmp227 = subjects102.popleft()
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.2.1.2.2', tmp227)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 45432
                                            if len(subjects102) == 0:
                                                pass
                                                # State 45433
                                                if len(subjects) == 0:
                                                    pass
                                                    # 7: (d*v**p)**q
                                        subjects102.appendleft(tmp227)
                            if len(subjects165) >= 1:
                                tmp229 = subjects165.popleft()
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i2.2.1.2.2.2', tmp229)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 45430
                                    if len(subjects165) == 0:
                                        pass
                                        # State 45431
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.2.1.2.2', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 45432
                                            if len(subjects102) == 0:
                                                pass
                                                # State 45433
                                                if len(subjects) == 0:
                                                    pass
                                                    # 7: (d*v**p)**q
                                        if len(subjects102) >= 1:
                                            tmp232 = subjects102.popleft()
                                            subst4 = Substitution(subst3)
                                            try:
                                                subst4.try_add_variable('i2.2.1.2.2', tmp232)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 45432
                                                if len(subjects102) == 0:
                                                    pass
                                                    # State 45433
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 7: (d*v**p)**q
                                            subjects102.appendleft(tmp232)
                                subjects165.appendleft(tmp229)
                        subjects165.appendleft(tmp218)
                    if len(subjects165) >= 1 and isinstance(subjects165[0], Add):
                        tmp234 = subjects165.popleft()
                        associative1 = tmp234
                        associative_type1 = type(tmp234)
                        subjects235 = deque(tmp234._args)
                        matcher = CommutativeMatcher22488.get()
                        tmp236 = subjects235
                        subjects235 = []
                        for s in tmp236:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp236, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 22494
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i2.2.1.2.2.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 22495
                                    if len(subjects165) == 0:
                                        pass
                                        # State 22496
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.2.1.2.2', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 22497
                                            if len(subjects102) == 0:
                                                pass
                                                # State 22498
                                                if len(subjects) == 0:
                                                    pass
                                                    # 0: (d*(e + x*f)**p)**q
                                        if len(subjects102) >= 1:
                                            tmp239 = subjects102.popleft()
                                            subst4 = Substitution(subst3)
                                            try:
                                                subst4.try_add_variable('i2.2.1.2.2', tmp239)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 22497
                                                if len(subjects102) == 0:
                                                    pass
                                                    # State 22498
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 0: (d*(e + x*f)**p)**q
                                            subjects102.appendleft(tmp239)
                                if len(subjects165) >= 1:
                                    tmp241 = []
                                    tmp241.append(subjects165.popleft())
                                    while True:
                                        if len(tmp241) > 1:
                                            tmp242 = create_operation_expression(associative1, tmp241)
                                        elif len(tmp241) == 1:
                                            tmp242 = tmp241[0]
                                        else:
                                            assert False, "Unreachable"
                                        subst3 = Substitution(subst2)
                                        try:
                                            subst3.try_add_variable('i2.2.1.2.2.2', tmp242)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 22495
                                            if len(subjects165) == 0:
                                                pass
                                                # State 22496
                                                subst4 = Substitution(subst3)
                                                try:
                                                    subst4.try_add_variable('i2.2.1.2.2', 1)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 22497
                                                    if len(subjects102) == 0:
                                                        pass
                                                        # State 22498
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 0: (d*(e + x*f)**p)**q
                                                if len(subjects102) >= 1:
                                                    tmp245 = subjects102.popleft()
                                                    subst4 = Substitution(subst3)
                                                    try:
                                                        subst4.try_add_variable('i2.2.1.2.2', tmp245)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 22497
                                                        if len(subjects102) == 0:
                                                            pass
                                                            # State 22498
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 0: (d*(e + x*f)**p)**q
                                                    subjects102.appendleft(tmp245)
                                        if len(subjects165) == 0:
                                            break
                                        tmp241.append(subjects165.popleft())
                                    subjects165.extendleft(reversed(tmp241))
                            if pattern_index == 1:
                                pass
                                # State 28482
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i2.2.1.2.2.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 28483
                                    if len(subjects165) == 0:
                                        pass
                                        # State 28484
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.2.1.2.2', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 28485
                                            if len(subjects102) == 0:
                                                pass
                                                # State 28486
                                                if len(subjects) == 0:
                                                    pass
                                                    # 3: (d*(e + f*x**m)**p)**q
                                        if len(subjects102) >= 1:
                                            tmp249 = subjects102.popleft()
                                            subst4 = Substitution(subst3)
                                            try:
                                                subst4.try_add_variable('i2.2.1.2.2', tmp249)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 28485
                                                if len(subjects102) == 0:
                                                    pass
                                                    # State 28486
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 3: (d*(e + f*x**m)**p)**q
                                            subjects102.appendleft(tmp249)
                                if len(subjects165) >= 1:
                                    tmp251 = []
                                    tmp251.append(subjects165.popleft())
                                    while True:
                                        if len(tmp251) > 1:
                                            tmp252 = create_operation_expression(associative1, tmp251)
                                        elif len(tmp251) == 1:
                                            tmp252 = tmp251[0]
                                        else:
                                            assert False, "Unreachable"
                                        subst3 = Substitution(subst2)
                                        try:
                                            subst3.try_add_variable('i2.2.1.2.2.2', tmp252)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 28483
                                            if len(subjects165) == 0:
                                                pass
                                                # State 28484
                                                subst4 = Substitution(subst3)
                                                try:
                                                    subst4.try_add_variable('i2.2.1.2.2', 1)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 28485
                                                    if len(subjects102) == 0:
                                                        pass
                                                        # State 28486
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 3: (d*(e + f*x**m)**p)**q
                                                if len(subjects102) >= 1:
                                                    tmp255 = subjects102.popleft()
                                                    subst4 = Substitution(subst3)
                                                    try:
                                                        subst4.try_add_variable('i2.2.1.2.2', tmp255)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 28485
                                                        if len(subjects102) == 0:
                                                            pass
                                                            # State 28486
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 3: (d*(e + f*x**m)**p)**q
                                                    subjects102.appendleft(tmp255)
                                        if len(subjects165) == 0:
                                            break
                                        tmp251.append(subjects165.popleft())
                                    subjects165.extendleft(reversed(tmp251))
                            if pattern_index == 2:
                                pass
                                # State 33970
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i2.2.1.2.2.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 33971
                                    if len(subjects165) == 0:
                                        pass
                                        # State 33972
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.2.1.2.2', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 33973
                                            if len(subjects102) == 0:
                                                pass
                                                # State 33974
                                                if len(subjects) == 0:
                                                    pass
                                                    # 5: (d*(e + f*x**m)**p)**q
                                        if len(subjects102) >= 1:
                                            tmp259 = subjects102.popleft()
                                            subst4 = Substitution(subst3)
                                            try:
                                                subst4.try_add_variable('i2.2.1.2.2', tmp259)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 33973
                                                if len(subjects102) == 0:
                                                    pass
                                                    # State 33974
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 5: (d*(e + f*x**m)**p)**q
                                            subjects102.appendleft(tmp259)
                                if len(subjects165) >= 1:
                                    tmp261 = []
                                    tmp261.append(subjects165.popleft())
                                    while True:
                                        if len(tmp261) > 1:
                                            tmp262 = create_operation_expression(associative1, tmp261)
                                        elif len(tmp261) == 1:
                                            tmp262 = tmp261[0]
                                        else:
                                            assert False, "Unreachable"
                                        subst3 = Substitution(subst2)
                                        try:
                                            subst3.try_add_variable('i2.2.1.2.2.2', tmp262)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 33971
                                            if len(subjects165) == 0:
                                                pass
                                                # State 33972
                                                subst4 = Substitution(subst3)
                                                try:
                                                    subst4.try_add_variable('i2.2.1.2.2', 1)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 33973
                                                    if len(subjects102) == 0:
                                                        pass
                                                        # State 33974
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 5: (d*(e + f*x**m)**p)**q
                                                if len(subjects102) >= 1:
                                                    tmp265 = subjects102.popleft()
                                                    subst4 = Substitution(subst3)
                                                    try:
                                                        subst4.try_add_variable('i2.2.1.2.2', tmp265)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 33973
                                                        if len(subjects102) == 0:
                                                            pass
                                                            # State 33974
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 5: (d*(e + f*x**m)**p)**q
                                                    subjects102.appendleft(tmp265)
                                        if len(subjects165) == 0:
                                            break
                                        tmp261.append(subjects165.popleft())
                                    subjects165.extendleft(reversed(tmp261))
                            if pattern_index == 3:
                                pass
                                # State 43655
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i2.2.1.2.2.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 43656
                                    if len(subjects165) == 0:
                                        pass
                                        # State 43657
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.2.1.2.2', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 43658
                                            if len(subjects102) == 0:
                                                pass
                                                # State 43659
                                                if len(subjects) == 0:
                                                    pass
                                                    # 6: (d*(e + f*x + g*x**2)**p)**q
                                        if len(subjects102) >= 1:
                                            tmp269 = subjects102.popleft()
                                            subst4 = Substitution(subst3)
                                            try:
                                                subst4.try_add_variable('i2.2.1.2.2', tmp269)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 43658
                                                if len(subjects102) == 0:
                                                    pass
                                                    # State 43659
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 6: (d*(e + f*x + g*x**2)**p)**q
                                            subjects102.appendleft(tmp269)
                                if len(subjects165) >= 1:
                                    tmp271 = []
                                    tmp271.append(subjects165.popleft())
                                    while True:
                                        if len(tmp271) > 1:
                                            tmp272 = create_operation_expression(associative1, tmp271)
                                        elif len(tmp271) == 1:
                                            tmp272 = tmp271[0]
                                        else:
                                            assert False, "Unreachable"
                                        subst3 = Substitution(subst2)
                                        try:
                                            subst3.try_add_variable('i2.2.1.2.2.2', tmp272)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 43656
                                            if len(subjects165) == 0:
                                                pass
                                                # State 43657
                                                subst4 = Substitution(subst3)
                                                try:
                                                    subst4.try_add_variable('i2.2.1.2.2', 1)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 43658
                                                    if len(subjects102) == 0:
                                                        pass
                                                        # State 43659
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 6: (d*(e + f*x + g*x**2)**p)**q
                                                if len(subjects102) >= 1:
                                                    tmp275 = subjects102.popleft()
                                                    subst4 = Substitution(subst3)
                                                    try:
                                                        subst4.try_add_variable('i2.2.1.2.2', tmp275)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 43658
                                                        if len(subjects102) == 0:
                                                            pass
                                                            # State 43659
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 6: (d*(e + f*x + g*x**2)**p)**q
                                                    subjects102.appendleft(tmp275)
                                        if len(subjects165) == 0:
                                            break
                                        tmp271.append(subjects165.popleft())
                                    subjects165.extendleft(reversed(tmp271))
                        subjects165.appendleft(tmp234)
                    if len(subjects165) >= 1 and isinstance(subjects165[0], Mul):
                        tmp277 = subjects165.popleft()
                        associative1 = tmp277
                        associative_type1 = type(tmp277)
                        subjects278 = deque(tmp277._args)
                        matcher = CommutativeMatcher30426.get()
                        tmp279 = subjects278
                        subjects278 = []
                        for s in tmp279:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp279, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 30450
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i2.2.1.2.2.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 30451
                                    if len(subjects165) == 0:
                                        pass
                                        # State 30452
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.2.1.2.2', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 30453
                                            if len(subjects102) == 0:
                                                pass
                                                # State 30454
                                                if len(subjects) == 0:
                                                    pass
                                                    # 4: (d*(x**m*(f + e*x**r))**p)**q
                                        if len(subjects102) >= 1:
                                            tmp282 = subjects102.popleft()
                                            subst4 = Substitution(subst3)
                                            try:
                                                subst4.try_add_variable('i2.2.1.2.2', tmp282)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 30453
                                                if len(subjects102) == 0:
                                                    pass
                                                    # State 30454
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 4: (d*(x**m*(f + e*x**r))**p)**q
                                            subjects102.appendleft(tmp282)
                                if len(subjects165) >= 1:
                                    tmp284 = []
                                    tmp284.append(subjects165.popleft())
                                    while True:
                                        if len(tmp284) > 1:
                                            tmp285 = create_operation_expression(associative1, tmp284)
                                        elif len(tmp284) == 1:
                                            tmp285 = tmp284[0]
                                        else:
                                            assert False, "Unreachable"
                                        subst3 = Substitution(subst2)
                                        try:
                                            subst3.try_add_variable('i2.2.1.2.2.2', tmp285)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 30451
                                            if len(subjects165) == 0:
                                                pass
                                                # State 30452
                                                subst4 = Substitution(subst3)
                                                try:
                                                    subst4.try_add_variable('i2.2.1.2.2', 1)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 30453
                                                    if len(subjects102) == 0:
                                                        pass
                                                        # State 30454
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 4: (d*(x**m*(f + e*x**r))**p)**q
                                                if len(subjects102) >= 1:
                                                    tmp288 = subjects102.popleft()
                                                    subst4 = Substitution(subst3)
                                                    try:
                                                        subst4.try_add_variable('i2.2.1.2.2', tmp288)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 30453
                                                        if len(subjects102) == 0:
                                                            pass
                                                            # State 30454
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 4: (d*(x**m*(f + e*x**r))**p)**q
                                                    subjects102.appendleft(tmp288)
                                        if len(subjects165) == 0:
                                            break
                                        tmp284.append(subjects165.popleft())
                                    subjects165.extendleft(reversed(tmp284))
                        subjects165.appendleft(tmp277)
                    subjects102.appendleft(tmp164)
            if len(subjects102) >= 1:
                tmp290 = subjects102.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.1.2.1', tmp290)
                except ValueError:
                    pass
                else:
                    pass
                    # State 53220
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.2.2', 1)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 53221
                        if len(subjects102) == 0:
                            pass
                            # State 53222
                            if len(subjects) == 0:
                                pass
                                # 8: RFx**p
                    if len(subjects102) >= 1:
                        tmp293 = subjects102.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.1.2.2', tmp293)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 53221
                            if len(subjects102) == 0:
                                pass
                                # State 53222
                                if len(subjects) == 0:
                                    pass
                                    # 8: RFx**p
                        subjects102.appendleft(tmp293)
                subjects102.appendleft(tmp290)
            if len(subjects102) >= 1 and isinstance(subjects102[0], Mul):
                tmp295 = subjects102.popleft()
                associative1 = tmp295
                associative_type1 = type(tmp295)
                subjects296 = deque(tmp295._args)
                matcher = CommutativeMatcher22500.get()
                tmp297 = subjects296
                subjects296 = []
                for s in tmp297:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp297, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 22537
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.1.2.2', 1)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 22538
                            if len(subjects102) == 0:
                                pass
                                # State 22539
                                if len(subjects) == 0:
                                    pass
                                    # 0: (d*(e + x*f)**p)**q
                        if len(subjects102) >= 1:
                            tmp299 = []
                            tmp299.append(subjects102.popleft())
                            while True:
                                if len(tmp299) > 1:
                                    tmp300 = create_operation_expression(associative1, tmp299)
                                elif len(tmp299) == 1:
                                    tmp300 = tmp299[0]
                                else:
                                    assert False, "Unreachable"
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i2.2.1.2.2', tmp300)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 22538
                                    if len(subjects102) == 0:
                                        pass
                                        # State 22539
                                        if len(subjects) == 0:
                                            pass
                                            # 0: (d*(e + x*f)**p)**q
                                if len(subjects102) == 0:
                                    break
                                tmp299.append(subjects102.popleft())
                            subjects102.extendleft(reversed(tmp299))
                    if pattern_index == 1:
                        pass
                        # State 25525
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.1.2.2', 1)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 25526
                            if len(subjects102) == 0:
                                pass
                                # State 25527
                                if len(subjects) == 0:
                                    pass
                                    # 1: (d*v**p)**q
                        if len(subjects102) >= 1:
                            tmp303 = []
                            tmp303.append(subjects102.popleft())
                            while True:
                                if len(tmp303) > 1:
                                    tmp304 = create_operation_expression(associative1, tmp303)
                                elif len(tmp303) == 1:
                                    tmp304 = tmp303[0]
                                else:
                                    assert False, "Unreachable"
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i2.2.1.2.2', tmp304)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 25526
                                    if len(subjects102) == 0:
                                        pass
                                        # State 25527
                                        if len(subjects) == 0:
                                            pass
                                            # 1: (d*v**p)**q
                                if len(subjects102) == 0:
                                    break
                                tmp303.append(subjects102.popleft())
                            subjects102.extendleft(reversed(tmp303))
                    if pattern_index == 2:
                        pass
                        # State 28511
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.1.2.2', 1)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 28512
                            if len(subjects102) == 0:
                                pass
                                # State 28513
                                if len(subjects) == 0:
                                    pass
                                    # 3: (d*(e + f*x**m)**p)**q
                        if len(subjects102) >= 1:
                            tmp307 = []
                            tmp307.append(subjects102.popleft())
                            while True:
                                if len(tmp307) > 1:
                                    tmp308 = create_operation_expression(associative1, tmp307)
                                elif len(tmp307) == 1:
                                    tmp308 = tmp307[0]
                                else:
                                    assert False, "Unreachable"
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i2.2.1.2.2', tmp308)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 28512
                                    if len(subjects102) == 0:
                                        pass
                                        # State 28513
                                        if len(subjects) == 0:
                                            pass
                                            # 3: (d*(e + f*x**m)**p)**q
                                if len(subjects102) == 0:
                                    break
                                tmp307.append(subjects102.popleft())
                            subjects102.extendleft(reversed(tmp307))
                    if pattern_index == 3:
                        pass
                        # State 30509
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.1.2.2', 1)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 30510
                            if len(subjects102) == 0:
                                pass
                                # State 30511
                                if len(subjects) == 0:
                                    pass
                                    # 4: (d*(x**m*(f + e*x**r))**p)**q
                        if len(subjects102) >= 1:
                            tmp311 = []
                            tmp311.append(subjects102.popleft())
                            while True:
                                if len(tmp311) > 1:
                                    tmp312 = create_operation_expression(associative1, tmp311)
                                elif len(tmp311) == 1:
                                    tmp312 = tmp311[0]
                                else:
                                    assert False, "Unreachable"
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i2.2.1.2.2', tmp312)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 30510
                                    if len(subjects102) == 0:
                                        pass
                                        # State 30511
                                        if len(subjects) == 0:
                                            pass
                                            # 4: (d*(x**m*(f + e*x**r))**p)**q
                                if len(subjects102) == 0:
                                    break
                                tmp311.append(subjects102.popleft())
                            subjects102.extendleft(reversed(tmp311))
                    if pattern_index == 4:
                        pass
                        # State 34003
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.1.2.2', 1)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 34004
                            if len(subjects102) == 0:
                                pass
                                # State 34005
                                if len(subjects) == 0:
                                    pass
                                    # 5: (d*(e + f*x**m)**p)**q
                        if len(subjects102) >= 1:
                            tmp315 = []
                            tmp315.append(subjects102.popleft())
                            while True:
                                if len(tmp315) > 1:
                                    tmp316 = create_operation_expression(associative1, tmp315)
                                elif len(tmp315) == 1:
                                    tmp316 = tmp315[0]
                                else:
                                    assert False, "Unreachable"
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i2.2.1.2.2', tmp316)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 34004
                                    if len(subjects102) == 0:
                                        pass
                                        # State 34005
                                        if len(subjects) == 0:
                                            pass
                                            # 5: (d*(e + f*x**m)**p)**q
                                if len(subjects102) == 0:
                                    break
                                tmp315.append(subjects102.popleft())
                            subjects102.extendleft(reversed(tmp315))
                    if pattern_index == 5:
                        pass
                        # State 43678
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.1.2.2', 1)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 43679
                            if len(subjects102) == 0:
                                pass
                                # State 43680
                                if len(subjects) == 0:
                                    pass
                                    # 6: (d*(e + f*x + g*x**2)**p)**q
                        if len(subjects102) >= 1:
                            tmp319 = []
                            tmp319.append(subjects102.popleft())
                            while True:
                                if len(tmp319) > 1:
                                    tmp320 = create_operation_expression(associative1, tmp319)
                                elif len(tmp319) == 1:
                                    tmp320 = tmp319[0]
                                else:
                                    assert False, "Unreachable"
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i2.2.1.2.2', tmp320)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 43679
                                    if len(subjects102) == 0:
                                        pass
                                        # State 43680
                                        if len(subjects) == 0:
                                            pass
                                            # 6: (d*(e + f*x + g*x**2)**p)**q
                                if len(subjects102) == 0:
                                    break
                                tmp319.append(subjects102.popleft())
                            subjects102.extendleft(reversed(tmp319))
                    if pattern_index == 6:
                        pass
                        # State 45437
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.1.2.2', 1)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 45438
                            if len(subjects102) == 0:
                                pass
                                # State 45439
                                if len(subjects) == 0:
                                    pass
                                    # 7: (d*v**p)**q
                        if len(subjects102) >= 1:
                            tmp323 = []
                            tmp323.append(subjects102.popleft())
                            while True:
                                if len(tmp323) > 1:
                                    tmp324 = create_operation_expression(associative1, tmp323)
                                elif len(tmp323) == 1:
                                    tmp324 = tmp323[0]
                                else:
                                    assert False, "Unreachable"
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i2.2.1.2.2', tmp324)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 45438
                                    if len(subjects102) == 0:
                                        pass
                                        # State 45439
                                        if len(subjects) == 0:
                                            pass
                                            # 7: (d*v**p)**q
                                if len(subjects102) == 0:
                                    break
                                tmp323.append(subjects102.popleft())
                            subjects102.extendleft(reversed(tmp323))
                subjects102.appendleft(tmp295)
            subjects.appendleft(tmp101)
        if len(subjects) >= 1 and isinstance(subjects[0], Add):
            tmp326 = subjects.popleft()
            associative1 = tmp326
            associative_type1 = type(tmp326)
            subjects327 = deque(tmp326._args)
            matcher = CommutativeMatcher26023.get()
            tmp328 = subjects327
            subjects327 = []
            for s in tmp328:
                matcher.add_subject(s)
            for pattern_index, subst1 in matcher.match(tmp328, subst0):
                pass
                if pattern_index == 0:
                    pass
                    # State 26029
                    if len(subjects) == 0:
                        pass
                        # 2: e + x*f
            subjects.appendleft(tmp326)
        return
        yield


from matchpy.utils import VariableWithCount
from matchpy.matching.many_to_one import CommutativeMatcher
from multiset import Multiset
from collections import deque
