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


class CommutativeMatcher20924(CommutativeMatcher):
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
]),
    9: (9, Multiset({9: 1}), [
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
        if CommutativeMatcher20924._instance is None:
            CommutativeMatcher20924._instance = CommutativeMatcher20924()
        return CommutativeMatcher20924._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 20923
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.2.2', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 20925
            subst2 = Substitution(subst1)
            try:
                subst2.try_add_variable('i2.2.1.2.2.0', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 20926
                subst3 = Substitution(subst2)
                try:
                    subst3.try_add_variable('i2.2.1.2.2.2', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 20927
                    subst4 = Substitution(subst3)
                    try:
                        subst4.try_add_variable('i2.2.1.2.2.2.0', S(0))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 20928
                        subst5 = Substitution(subst4)
                        try:
                            subst5.try_add_variable('i2.2.1.2.2.2.1.0_1', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 20929
                            if len(subjects) >= 1:
                                tmp6 = subjects.popleft()
                                subst6 = Substitution(subst5)
                                try:
                                    subst6.try_add_variable('i2.2.1.2.2.2.1.0', tmp6)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 20930
                                    if len(subjects) == 0:
                                        pass
                                        # 0: (d*(e + x*f)**p)**q
                                        yield 0, subst6
                                subjects.appendleft(tmp6)
                        subst5 = Substitution(subst4)
                        try:
                            subst5.try_add_variable('i2.2.1.2.2.2.1.0', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 34997
                            if len(subjects) >= 1 and isinstance(subjects[0], Pow):
                                tmp9 = subjects.popleft()
                                subjects10 = deque(tmp9._args)
                                # State 34998
                                if len(subjects10) >= 1:
                                    tmp11 = subjects10.popleft()
                                    subst6 = Substitution(subst5)
                                    try:
                                        subst6.try_add_variable('i2.2.1.2.2.2.1.1', tmp11)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 34999
                                        if len(subjects10) >= 1:
                                            tmp13 = subjects10.popleft()
                                            subst7 = Substitution(subst6)
                                            try:
                                                subst7.try_add_variable('i2.2.1.2.2.2.1.2', tmp13)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 35000
                                                if len(subjects10) == 0:
                                                    pass
                                                    # State 35001
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 5: (d*(e + f*x**m)**p)**q
                                                        yield 5, subst7
                                            subjects10.appendleft(tmp13)
                                    subjects10.appendleft(tmp11)
                                subjects.appendleft(tmp9)
                        if len(subjects) >= 1 and isinstance(subjects[0], Mul):
                            tmp15 = subjects.popleft()
                            associative1 = tmp15
                            associative_type1 = type(tmp15)
                            subjects16 = deque(tmp15._args)
                            matcher = CommutativeMatcher20932.get()
                            tmp17 = subjects16
                            subjects16 = []
                            for s in tmp17:
                                matcher.add_subject(s)
                            for pattern_index, subst5 in matcher.match(tmp17, subst4):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 20933
                                    if len(subjects) == 0:
                                        pass
                                        # 0: (d*(e + x*f)**p)**q
                                        yield 0, subst5
                                if pattern_index == 1:
                                    pass
                                    # State 35006
                                    if len(subjects) == 0:
                                        pass
                                        # 5: (d*(e + f*x**m)**p)**q
                                        yield 5, subst5
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
                            # State 45627
                            if len(subjects) == 0:
                                pass
                                # 7: (d*v**p)**q
                                yield 7, subst4
                        subjects.appendleft(tmp18)
                    if len(subjects) >= 1 and isinstance(subjects[0], Add):
                        tmp20 = subjects.popleft()
                        associative1 = tmp20
                        associative_type1 = type(tmp20)
                        subjects21 = deque(tmp20._args)
                        matcher = CommutativeMatcher20935.get()
                        tmp22 = subjects21
                        subjects21 = []
                        for s in tmp22:
                            matcher.add_subject(s)
                        for pattern_index, subst4 in matcher.match(tmp22, subst3):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 20941
                                if len(subjects) == 0:
                                    pass
                                    # 0: (d*(e + x*f)**p)**q
                                    yield 0, subst4
                            if pattern_index == 1:
                                pass
                                # State 29299
                                if len(subjects) == 0:
                                    pass
                                    # 3: (d*(e + f*x**m)**p)**q
                                    yield 3, subst4
                            if pattern_index == 2:
                                pass
                                # State 35007
                                if len(subjects) == 0:
                                    pass
                                    # 5: (d*(e + f*x**m)**p)**q
                                    yield 5, subst4
                            if pattern_index == 3:
                                pass
                                # State 44295
                                if len(subjects) == 0:
                                    pass
                                    # 6: (d*(e + f*x + g*x**2)**p)**q
                                    yield 6, subst4
                        subjects.appendleft(tmp20)
                    if len(subjects) >= 1 and isinstance(subjects[0], Mul):
                        tmp23 = subjects.popleft()
                        associative1 = tmp23
                        associative_type1 = type(tmp23)
                        subjects24 = deque(tmp23._args)
                        matcher = CommutativeMatcher32128.get()
                        tmp25 = subjects24
                        subjects24 = []
                        for s in tmp25:
                            matcher.add_subject(s)
                        for pattern_index, subst4 in matcher.match(tmp25, subst3):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 32152
                                if len(subjects) == 0:
                                    pass
                                    # 4: (d*(x**m*(f + e*x**r))**p)**q
                                    yield 4, subst4
                        subjects.appendleft(tmp23)
                if len(subjects) >= 1 and isinstance(subjects[0], Pow):
                    tmp26 = subjects.popleft()
                    subjects27 = deque(tmp26._args)
                    # State 20942
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.2.1.2.2.2.0', S(0))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 20943
                        subst4 = Substitution(subst3)
                        try:
                            subst4.try_add_variable('i2.2.1.2.2.2.1.0_1', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 20944
                            if len(subjects27) >= 1:
                                tmp30 = subjects27.popleft()
                                subst5 = Substitution(subst4)
                                try:
                                    subst5.try_add_variable('i2.2.1.2.2.2.1.0', tmp30)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 20945
                                    subst6 = Substitution(subst5)
                                    try:
                                        subst6.try_add_variable('i2.2.1.2.2.2', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 20946
                                        if len(subjects27) == 0:
                                            pass
                                            # State 20947
                                            if len(subjects) == 0:
                                                pass
                                                # 0: (d*(e + x*f)**p)**q
                                                yield 0, subst6
                                    if len(subjects27) >= 1:
                                        tmp33 = subjects27.popleft()
                                        subst6 = Substitution(subst5)
                                        try:
                                            subst6.try_add_variable('i2.2.1.2.2.2', tmp33)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 20946
                                            if len(subjects27) == 0:
                                                pass
                                                # State 20947
                                                if len(subjects) == 0:
                                                    pass
                                                    # 0: (d*(e + x*f)**p)**q
                                                    yield 0, subst6
                                        subjects27.appendleft(tmp33)
                                subjects27.appendleft(tmp30)
                        subst4 = Substitution(subst3)
                        try:
                            subst4.try_add_variable('i2.2.1.2.2.2.1.0', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 35008
                            if len(subjects27) >= 1 and isinstance(subjects27[0], Pow):
                                tmp36 = subjects27.popleft()
                                subjects37 = deque(tmp36._args)
                                # State 35009
                                if len(subjects37) >= 1:
                                    tmp38 = subjects37.popleft()
                                    subst5 = Substitution(subst4)
                                    try:
                                        subst5.try_add_variable('i2.2.1.2.2.2.1.1', tmp38)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 35010
                                        if len(subjects37) >= 1:
                                            tmp40 = subjects37.popleft()
                                            subst6 = Substitution(subst5)
                                            try:
                                                subst6.try_add_variable('i2.2.1.2.2.2.1.2', tmp40)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 35011
                                                if len(subjects37) == 0:
                                                    pass
                                                    # State 35012
                                                    subst7 = Substitution(subst6)
                                                    try:
                                                        subst7.try_add_variable('i2.2.1.2.2.2', 1)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 35013
                                                        if len(subjects27) == 0:
                                                            pass
                                                            # State 35014
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 5: (d*(e + f*x**m)**p)**q
                                                                yield 5, subst7
                                                    if len(subjects27) >= 1:
                                                        tmp43 = subjects27.popleft()
                                                        subst7 = Substitution(subst6)
                                                        try:
                                                            subst7.try_add_variable('i2.2.1.2.2.2', tmp43)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            # State 35013
                                                            if len(subjects27) == 0:
                                                                pass
                                                                # State 35014
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 5: (d*(e + f*x**m)**p)**q
                                                                    yield 5, subst7
                                                        subjects27.appendleft(tmp43)
                                            subjects37.appendleft(tmp40)
                                    subjects37.appendleft(tmp38)
                                subjects27.appendleft(tmp36)
                        if len(subjects27) >= 1 and isinstance(subjects27[0], Mul):
                            tmp45 = subjects27.popleft()
                            associative1 = tmp45
                            associative_type1 = type(tmp45)
                            subjects46 = deque(tmp45._args)
                            matcher = CommutativeMatcher20949.get()
                            tmp47 = subjects46
                            subjects46 = []
                            for s in tmp47:
                                matcher.add_subject(s)
                            for pattern_index, subst4 in matcher.match(tmp47, subst3):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 20950
                                    subst5 = Substitution(subst4)
                                    try:
                                        subst5.try_add_variable('i2.2.1.2.2.2', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 20951
                                        if len(subjects27) == 0:
                                            pass
                                            # State 20952
                                            if len(subjects) == 0:
                                                pass
                                                # 0: (d*(e + x*f)**p)**q
                                                yield 0, subst5
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
                                                # State 20951
                                                if len(subjects27) == 0:
                                                    pass
                                                    # State 20952
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 0: (d*(e + x*f)**p)**q
                                                        yield 0, subst5
                                            if len(subjects27) == 0:
                                                break
                                            tmp49.append(subjects27.popleft())
                                        subjects27.extendleft(reversed(tmp49))
                                if pattern_index == 1:
                                    pass
                                    # State 35019
                                    subst5 = Substitution(subst4)
                                    try:
                                        subst5.try_add_variable('i2.2.1.2.2.2', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 35020
                                        if len(subjects27) == 0:
                                            pass
                                            # State 35021
                                            if len(subjects) == 0:
                                                pass
                                                # 5: (d*(e + f*x**m)**p)**q
                                                yield 5, subst5
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
                                                # State 35020
                                                if len(subjects27) == 0:
                                                    pass
                                                    # State 35021
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 5: (d*(e + f*x**m)**p)**q
                                                        yield 5, subst5
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
                            # State 25689
                            if len(subjects27) >= 1:
                                tmp58 = subjects27.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.2.1.2.2.2', tmp58)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 25690
                                    if len(subjects27) == 0:
                                        pass
                                        # State 25691
                                        if len(subjects) == 0:
                                            pass
                                            # 1: (d*v**p)**q
                                            yield 1, subst4
                                subjects27.appendleft(tmp58)
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i2.2.1.2.2.2', 1)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 45628
                                if len(subjects27) == 0:
                                    pass
                                    # State 45629
                                    if len(subjects) == 0:
                                        pass
                                        # 7: (d*v**p)**q
                                        yield 7, subst4
                            if len(subjects27) >= 1:
                                tmp61 = subjects27.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.2.1.2.2.2', tmp61)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 45628
                                    if len(subjects27) == 0:
                                        pass
                                        # State 45629
                                        if len(subjects) == 0:
                                            pass
                                            # 7: (d*v**p)**q
                                            yield 7, subst4
                                subjects27.appendleft(tmp61)
                        subjects27.appendleft(tmp56)
                    if len(subjects27) >= 1 and isinstance(subjects27[0], Add):
                        tmp63 = subjects27.popleft()
                        associative1 = tmp63
                        associative_type1 = type(tmp63)
                        subjects64 = deque(tmp63._args)
                        matcher = CommutativeMatcher20954.get()
                        tmp65 = subjects64
                        subjects64 = []
                        for s in tmp65:
                            matcher.add_subject(s)
                        for pattern_index, subst3 in matcher.match(tmp65, subst2):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 20960
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.2.1.2.2.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 20961
                                    if len(subjects27) == 0:
                                        pass
                                        # State 20962
                                        if len(subjects) == 0:
                                            pass
                                            # 0: (d*(e + x*f)**p)**q
                                            yield 0, subst4
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
                                            # State 20961
                                            if len(subjects27) == 0:
                                                pass
                                                # State 20962
                                                if len(subjects) == 0:
                                                    pass
                                                    # 0: (d*(e + x*f)**p)**q
                                                    yield 0, subst4
                                        if len(subjects27) == 0:
                                            break
                                        tmp67.append(subjects27.popleft())
                                    subjects27.extendleft(reversed(tmp67))
                            if pattern_index == 1:
                                pass
                                # State 29310
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.2.1.2.2.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 29311
                                    if len(subjects27) == 0:
                                        pass
                                        # State 29312
                                        if len(subjects) == 0:
                                            pass
                                            # 3: (d*(e + f*x**m)**p)**q
                                            yield 3, subst4
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
                                            # State 29311
                                            if len(subjects27) == 0:
                                                pass
                                                # State 29312
                                                if len(subjects) == 0:
                                                    pass
                                                    # 3: (d*(e + f*x**m)**p)**q
                                                    yield 3, subst4
                                        if len(subjects27) == 0:
                                            break
                                        tmp71.append(subjects27.popleft())
                                    subjects27.extendleft(reversed(tmp71))
                            if pattern_index == 2:
                                pass
                                # State 35022
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.2.1.2.2.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 35023
                                    if len(subjects27) == 0:
                                        pass
                                        # State 35024
                                        if len(subjects) == 0:
                                            pass
                                            # 5: (d*(e + f*x**m)**p)**q
                                            yield 5, subst4
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
                                            # State 35023
                                            if len(subjects27) == 0:
                                                pass
                                                # State 35024
                                                if len(subjects) == 0:
                                                    pass
                                                    # 5: (d*(e + f*x**m)**p)**q
                                                    yield 5, subst4
                                        if len(subjects27) == 0:
                                            break
                                        tmp75.append(subjects27.popleft())
                                    subjects27.extendleft(reversed(tmp75))
                            if pattern_index == 3:
                                pass
                                # State 44303
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.2.1.2.2.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 44304
                                    if len(subjects27) == 0:
                                        pass
                                        # State 44305
                                        if len(subjects) == 0:
                                            pass
                                            # 6: (d*(e + f*x + g*x**2)**p)**q
                                            yield 6, subst4
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
                                            # State 44304
                                            if len(subjects27) == 0:
                                                pass
                                                # State 44305
                                                if len(subjects) == 0:
                                                    pass
                                                    # 6: (d*(e + f*x + g*x**2)**p)**q
                                                    yield 6, subst4
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
                        matcher = CommutativeMatcher32154.get()
                        tmp84 = subjects83
                        subjects83 = []
                        for s in tmp84:
                            matcher.add_subject(s)
                        for pattern_index, subst3 in matcher.match(tmp84, subst2):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 32178
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.2.1.2.2.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 32179
                                    if len(subjects27) == 0:
                                        pass
                                        # State 32180
                                        if len(subjects) == 0:
                                            pass
                                            # 4: (d*(x**m*(f + e*x**r))**p)**q
                                            yield 4, subst4
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
                                            # State 32179
                                            if len(subjects27) == 0:
                                                pass
                                                # State 32180
                                                if len(subjects) == 0:
                                                    pass
                                                    # 4: (d*(x**m*(f + e*x**r))**p)**q
                                                    yield 4, subst4
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
                    # State 53274
                    if len(subjects) == 0:
                        pass
                        # 9: RFx**p
                        yield 9, subst2
                subjects.appendleft(tmp89)
            if len(subjects) >= 1 and isinstance(subjects[0], Mul):
                tmp91 = subjects.popleft()
                associative1 = tmp91
                associative_type1 = type(tmp91)
                subjects92 = deque(tmp91._args)
                matcher = CommutativeMatcher20964.get()
                tmp93 = subjects92
                subjects92 = []
                for s in tmp93:
                    matcher.add_subject(s)
                for pattern_index, subst2 in matcher.match(tmp93, subst1):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 21001
                        if len(subjects) == 0:
                            pass
                            # 0: (d*(e + x*f)**p)**q
                            yield 0, subst2
                    if pattern_index == 1:
                        pass
                        # State 25695
                        if len(subjects) == 0:
                            pass
                            # 1: (d*v**p)**q
                            yield 1, subst2
                    if pattern_index == 2:
                        pass
                        # State 29337
                        if len(subjects) == 0:
                            pass
                            # 3: (d*(e + f*x**m)**p)**q
                            yield 3, subst2
                    if pattern_index == 3:
                        pass
                        # State 32235
                        if len(subjects) == 0:
                            pass
                            # 4: (d*(x**m*(f + e*x**r))**p)**q
                            yield 4, subst2
                    if pattern_index == 4:
                        pass
                        # State 35053
                        if len(subjects) == 0:
                            pass
                            # 5: (d*(e + f*x**m)**p)**q
                            yield 5, subst2
                    if pattern_index == 5:
                        pass
                        # State 44324
                        if len(subjects) == 0:
                            pass
                            # 6: (d*(e + f*x + g*x**2)**p)**q
                            yield 6, subst2
                    if pattern_index == 6:
                        pass
                        # State 45633
                        if len(subjects) == 0:
                            pass
                            # 7: (d*v**p)**q
                            yield 7, subst2
                subjects.appendleft(tmp91)
            if len(subjects) >= 1 and isinstance(subjects[0], Add):
                tmp94 = subjects.popleft()
                associative1 = tmp94
                associative_type1 = type(tmp94)
                subjects95 = deque(tmp94._args)
                matcher = CommutativeMatcher50848.get()
                tmp96 = subjects95
                subjects95 = []
                for s in tmp96:
                    matcher.add_subject(s)
                for pattern_index, subst2 in matcher.match(tmp96, subst1):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 50861
                        if len(subjects) == 0:
                            pass
                            # 8: (d + e*x**2)**p
                            yield 8, subst2
                subjects.appendleft(tmp94)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.2.1.0', S(0))
        except ValueError:
            pass
        else:
            pass
            # State 26157
            subst2 = Substitution(subst1)
            try:
                subst2.try_add_variable('i2.2.1.2.1.1.0_1', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 26158
                if len(subjects) >= 1:
                    tmp99 = subjects.popleft()
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.2.1.2.1.1.0', tmp99)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 26159
                        if len(subjects) == 0:
                            pass
                            # 2: e + x*f
                            yield 2, subst3
                    subjects.appendleft(tmp99)
            if len(subjects) >= 1 and isinstance(subjects[0], Mul):
                tmp101 = subjects.popleft()
                associative1 = tmp101
                associative_type1 = type(tmp101)
                subjects102 = deque(tmp101._args)
                matcher = CommutativeMatcher26161.get()
                tmp103 = subjects102
                subjects102 = []
                for s in tmp103:
                    matcher.add_subject(s)
                for pattern_index, subst2 in matcher.match(tmp103, subst1):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 26162
                        if len(subjects) == 0:
                            pass
                            # 2: e + x*f
                            yield 2, subst2
                subjects.appendleft(tmp101)
        if len(subjects) >= 1 and isinstance(subjects[0], Pow):
            tmp104 = subjects.popleft()
            subjects105 = deque(tmp104._args)
            # State 21002
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.2.0', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 21003
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.2.2', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 21004
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.2.1.2.2.2.0', S(0))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 21005
                        subst4 = Substitution(subst3)
                        try:
                            subst4.try_add_variable('i2.2.1.2.2.2.1.0_1', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 21006
                            if len(subjects105) >= 1:
                                tmp110 = subjects105.popleft()
                                subst5 = Substitution(subst4)
                                try:
                                    subst5.try_add_variable('i2.2.1.2.2.2.1.0', tmp110)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 21007
                                    subst6 = Substitution(subst5)
                                    try:
                                        subst6.try_add_variable('i2.2.1.2.2', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 21008
                                        if len(subjects105) == 0:
                                            pass
                                            # State 21009
                                            if len(subjects) == 0:
                                                pass
                                                # 0: (d*(e + x*f)**p)**q
                                                yield 0, subst6
                                    if len(subjects105) >= 1:
                                        tmp113 = subjects105.popleft()
                                        subst6 = Substitution(subst5)
                                        try:
                                            subst6.try_add_variable('i2.2.1.2.2', tmp113)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 21008
                                            if len(subjects105) == 0:
                                                pass
                                                # State 21009
                                                if len(subjects) == 0:
                                                    pass
                                                    # 0: (d*(e + x*f)**p)**q
                                                    yield 0, subst6
                                        subjects105.appendleft(tmp113)
                                subjects105.appendleft(tmp110)
                        subst4 = Substitution(subst3)
                        try:
                            subst4.try_add_variable('i2.2.1.2.2.2.1.0', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 35054
                            if len(subjects105) >= 1 and isinstance(subjects105[0], Pow):
                                tmp116 = subjects105.popleft()
                                subjects117 = deque(tmp116._args)
                                # State 35055
                                if len(subjects117) >= 1:
                                    tmp118 = subjects117.popleft()
                                    subst5 = Substitution(subst4)
                                    try:
                                        subst5.try_add_variable('i2.2.1.2.2.2.1.1', tmp118)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 35056
                                        if len(subjects117) >= 1:
                                            tmp120 = subjects117.popleft()
                                            subst6 = Substitution(subst5)
                                            try:
                                                subst6.try_add_variable('i2.2.1.2.2.2.1.2', tmp120)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 35057
                                                if len(subjects117) == 0:
                                                    pass
                                                    # State 35058
                                                    subst7 = Substitution(subst6)
                                                    try:
                                                        subst7.try_add_variable('i2.2.1.2.2', 1)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 35059
                                                        if len(subjects105) == 0:
                                                            pass
                                                            # State 35060
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 5: (d*(e + f*x**m)**p)**q
                                                                yield 5, subst7
                                                    if len(subjects105) >= 1:
                                                        tmp123 = subjects105.popleft()
                                                        subst7 = Substitution(subst6)
                                                        try:
                                                            subst7.try_add_variable('i2.2.1.2.2', tmp123)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            # State 35059
                                                            if len(subjects105) == 0:
                                                                pass
                                                                # State 35060
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 5: (d*(e + f*x**m)**p)**q
                                                                    yield 5, subst7
                                                        subjects105.appendleft(tmp123)
                                            subjects117.appendleft(tmp120)
                                    subjects117.appendleft(tmp118)
                                subjects105.appendleft(tmp116)
                        if len(subjects105) >= 1 and isinstance(subjects105[0], Mul):
                            tmp125 = subjects105.popleft()
                            associative1 = tmp125
                            associative_type1 = type(tmp125)
                            subjects126 = deque(tmp125._args)
                            matcher = CommutativeMatcher21011.get()
                            tmp127 = subjects126
                            subjects126 = []
                            for s in tmp127:
                                matcher.add_subject(s)
                            for pattern_index, subst4 in matcher.match(tmp127, subst3):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 21012
                                    subst5 = Substitution(subst4)
                                    try:
                                        subst5.try_add_variable('i2.2.1.2.2', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 21013
                                        if len(subjects105) == 0:
                                            pass
                                            # State 21014
                                            if len(subjects) == 0:
                                                pass
                                                # 0: (d*(e + x*f)**p)**q
                                                yield 0, subst5
                                    if len(subjects105) >= 1:
                                        tmp129 = []
                                        tmp129.append(subjects105.popleft())
                                        while True:
                                            if len(tmp129) > 1:
                                                tmp130 = create_operation_expression(associative1, tmp129)
                                            elif len(tmp129) == 1:
                                                tmp130 = tmp129[0]
                                            else:
                                                assert False, "Unreachable"
                                            subst5 = Substitution(subst4)
                                            try:
                                                subst5.try_add_variable('i2.2.1.2.2', tmp130)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 21013
                                                if len(subjects105) == 0:
                                                    pass
                                                    # State 21014
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 0: (d*(e + x*f)**p)**q
                                                        yield 0, subst5
                                            if len(subjects105) == 0:
                                                break
                                            tmp129.append(subjects105.popleft())
                                        subjects105.extendleft(reversed(tmp129))
                                if pattern_index == 1:
                                    pass
                                    # State 35065
                                    subst5 = Substitution(subst4)
                                    try:
                                        subst5.try_add_variable('i2.2.1.2.2', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 35066
                                        if len(subjects105) == 0:
                                            pass
                                            # State 35067
                                            if len(subjects) == 0:
                                                pass
                                                # 5: (d*(e + f*x**m)**p)**q
                                                yield 5, subst5
                                    if len(subjects105) >= 1:
                                        tmp133 = []
                                        tmp133.append(subjects105.popleft())
                                        while True:
                                            if len(tmp133) > 1:
                                                tmp134 = create_operation_expression(associative1, tmp133)
                                            elif len(tmp133) == 1:
                                                tmp134 = tmp133[0]
                                            else:
                                                assert False, "Unreachable"
                                            subst5 = Substitution(subst4)
                                            try:
                                                subst5.try_add_variable('i2.2.1.2.2', tmp134)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 35066
                                                if len(subjects105) == 0:
                                                    pass
                                                    # State 35067
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 5: (d*(e + f*x**m)**p)**q
                                                        yield 5, subst5
                                            if len(subjects105) == 0:
                                                break
                                            tmp133.append(subjects105.popleft())
                                        subjects105.extendleft(reversed(tmp133))
                            subjects105.appendleft(tmp125)
                    if len(subjects105) >= 1:
                        tmp136 = subjects105.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.2.2.1', tmp136)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 45634
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i2.2.1.2.2', 1)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 45635
                                if len(subjects105) == 0:
                                    pass
                                    # State 45636
                                    if len(subjects) == 0:
                                        pass
                                        # 7: (d*v**p)**q
                                        yield 7, subst4
                            if len(subjects105) >= 1:
                                tmp139 = subjects105.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.2.1.2.2', tmp139)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 45635
                                    if len(subjects105) == 0:
                                        pass
                                        # State 45636
                                        if len(subjects) == 0:
                                            pass
                                            # 7: (d*v**p)**q
                                            yield 7, subst4
                                subjects105.appendleft(tmp139)
                        subjects105.appendleft(tmp136)
                    if len(subjects105) >= 1 and isinstance(subjects105[0], Add):
                        tmp141 = subjects105.popleft()
                        associative1 = tmp141
                        associative_type1 = type(tmp141)
                        subjects142 = deque(tmp141._args)
                        matcher = CommutativeMatcher21016.get()
                        tmp143 = subjects142
                        subjects142 = []
                        for s in tmp143:
                            matcher.add_subject(s)
                        for pattern_index, subst3 in matcher.match(tmp143, subst2):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 21022
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.2.1.2.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 21023
                                    if len(subjects105) == 0:
                                        pass
                                        # State 21024
                                        if len(subjects) == 0:
                                            pass
                                            # 0: (d*(e + x*f)**p)**q
                                            yield 0, subst4
                                if len(subjects105) >= 1:
                                    tmp145 = []
                                    tmp145.append(subjects105.popleft())
                                    while True:
                                        if len(tmp145) > 1:
                                            tmp146 = create_operation_expression(associative1, tmp145)
                                        elif len(tmp145) == 1:
                                            tmp146 = tmp145[0]
                                        else:
                                            assert False, "Unreachable"
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.2.1.2.2', tmp146)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 21023
                                            if len(subjects105) == 0:
                                                pass
                                                # State 21024
                                                if len(subjects) == 0:
                                                    pass
                                                    # 0: (d*(e + x*f)**p)**q
                                                    yield 0, subst4
                                        if len(subjects105) == 0:
                                            break
                                        tmp145.append(subjects105.popleft())
                                    subjects105.extendleft(reversed(tmp145))
                            if pattern_index == 1:
                                pass
                                # State 29348
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.2.1.2.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 29349
                                    if len(subjects105) == 0:
                                        pass
                                        # State 29350
                                        if len(subjects) == 0:
                                            pass
                                            # 3: (d*(e + f*x**m)**p)**q
                                            yield 3, subst4
                                if len(subjects105) >= 1:
                                    tmp149 = []
                                    tmp149.append(subjects105.popleft())
                                    while True:
                                        if len(tmp149) > 1:
                                            tmp150 = create_operation_expression(associative1, tmp149)
                                        elif len(tmp149) == 1:
                                            tmp150 = tmp149[0]
                                        else:
                                            assert False, "Unreachable"
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.2.1.2.2', tmp150)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 29349
                                            if len(subjects105) == 0:
                                                pass
                                                # State 29350
                                                if len(subjects) == 0:
                                                    pass
                                                    # 3: (d*(e + f*x**m)**p)**q
                                                    yield 3, subst4
                                        if len(subjects105) == 0:
                                            break
                                        tmp149.append(subjects105.popleft())
                                    subjects105.extendleft(reversed(tmp149))
                            if pattern_index == 2:
                                pass
                                # State 35068
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.2.1.2.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 35069
                                    if len(subjects105) == 0:
                                        pass
                                        # State 35070
                                        if len(subjects) == 0:
                                            pass
                                            # 5: (d*(e + f*x**m)**p)**q
                                            yield 5, subst4
                                if len(subjects105) >= 1:
                                    tmp153 = []
                                    tmp153.append(subjects105.popleft())
                                    while True:
                                        if len(tmp153) > 1:
                                            tmp154 = create_operation_expression(associative1, tmp153)
                                        elif len(tmp153) == 1:
                                            tmp154 = tmp153[0]
                                        else:
                                            assert False, "Unreachable"
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.2.1.2.2', tmp154)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 35069
                                            if len(subjects105) == 0:
                                                pass
                                                # State 35070
                                                if len(subjects) == 0:
                                                    pass
                                                    # 5: (d*(e + f*x**m)**p)**q
                                                    yield 5, subst4
                                        if len(subjects105) == 0:
                                            break
                                        tmp153.append(subjects105.popleft())
                                    subjects105.extendleft(reversed(tmp153))
                            if pattern_index == 3:
                                pass
                                # State 44332
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.2.1.2.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 44333
                                    if len(subjects105) == 0:
                                        pass
                                        # State 44334
                                        if len(subjects) == 0:
                                            pass
                                            # 6: (d*(e + f*x + g*x**2)**p)**q
                                            yield 6, subst4
                                if len(subjects105) >= 1:
                                    tmp157 = []
                                    tmp157.append(subjects105.popleft())
                                    while True:
                                        if len(tmp157) > 1:
                                            tmp158 = create_operation_expression(associative1, tmp157)
                                        elif len(tmp157) == 1:
                                            tmp158 = tmp157[0]
                                        else:
                                            assert False, "Unreachable"
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.2.1.2.2', tmp158)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 44333
                                            if len(subjects105) == 0:
                                                pass
                                                # State 44334
                                                if len(subjects) == 0:
                                                    pass
                                                    # 6: (d*(e + f*x + g*x**2)**p)**q
                                                    yield 6, subst4
                                        if len(subjects105) == 0:
                                            break
                                        tmp157.append(subjects105.popleft())
                                    subjects105.extendleft(reversed(tmp157))
                        subjects105.appendleft(tmp141)
                    if len(subjects105) >= 1 and isinstance(subjects105[0], Mul):
                        tmp160 = subjects105.popleft()
                        associative1 = tmp160
                        associative_type1 = type(tmp160)
                        subjects161 = deque(tmp160._args)
                        matcher = CommutativeMatcher32237.get()
                        tmp162 = subjects161
                        subjects161 = []
                        for s in tmp162:
                            matcher.add_subject(s)
                        for pattern_index, subst3 in matcher.match(tmp162, subst2):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 32261
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.2.1.2.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 32262
                                    if len(subjects105) == 0:
                                        pass
                                        # State 32263
                                        if len(subjects) == 0:
                                            pass
                                            # 4: (d*(x**m*(f + e*x**r))**p)**q
                                            yield 4, subst4
                                if len(subjects105) >= 1:
                                    tmp164 = []
                                    tmp164.append(subjects105.popleft())
                                    while True:
                                        if len(tmp164) > 1:
                                            tmp165 = create_operation_expression(associative1, tmp164)
                                        elif len(tmp164) == 1:
                                            tmp165 = tmp164[0]
                                        else:
                                            assert False, "Unreachable"
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.2.1.2.2', tmp165)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 32262
                                            if len(subjects105) == 0:
                                                pass
                                                # State 32263
                                                if len(subjects) == 0:
                                                    pass
                                                    # 4: (d*(x**m*(f + e*x**r))**p)**q
                                                    yield 4, subst4
                                        if len(subjects105) == 0:
                                            break
                                        tmp164.append(subjects105.popleft())
                                    subjects105.extendleft(reversed(tmp164))
                        subjects105.appendleft(tmp160)
                if len(subjects105) >= 1 and isinstance(subjects105[0], Pow):
                    tmp167 = subjects105.popleft()
                    subjects168 = deque(tmp167._args)
                    # State 21025
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.2.2.2.0', S(0))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 21026
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.2.2.2.1.0_1', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 21027
                            if len(subjects168) >= 1:
                                tmp171 = subjects168.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.2.1.2.2.2.1.0', tmp171)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 21028
                                    subst5 = Substitution(subst4)
                                    try:
                                        subst5.try_add_variable('i2.2.1.2.2.2', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 21029
                                        if len(subjects168) == 0:
                                            pass
                                            # State 21030
                                            subst6 = Substitution(subst5)
                                            try:
                                                subst6.try_add_variable('i2.2.1.2.2', 1)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 21031
                                                if len(subjects105) == 0:
                                                    pass
                                                    # State 21032
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 0: (d*(e + x*f)**p)**q
                                                        yield 0, subst6
                                            if len(subjects105) >= 1:
                                                tmp175 = subjects105.popleft()
                                                subst6 = Substitution(subst5)
                                                try:
                                                    subst6.try_add_variable('i2.2.1.2.2', tmp175)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 21031
                                                    if len(subjects105) == 0:
                                                        pass
                                                        # State 21032
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 0: (d*(e + x*f)**p)**q
                                                            yield 0, subst6
                                                subjects105.appendleft(tmp175)
                                    if len(subjects168) >= 1:
                                        tmp177 = subjects168.popleft()
                                        subst5 = Substitution(subst4)
                                        try:
                                            subst5.try_add_variable('i2.2.1.2.2.2', tmp177)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 21029
                                            if len(subjects168) == 0:
                                                pass
                                                # State 21030
                                                subst6 = Substitution(subst5)
                                                try:
                                                    subst6.try_add_variable('i2.2.1.2.2', 1)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 21031
                                                    if len(subjects105) == 0:
                                                        pass
                                                        # State 21032
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 0: (d*(e + x*f)**p)**q
                                                            yield 0, subst6
                                                if len(subjects105) >= 1:
                                                    tmp180 = subjects105.popleft()
                                                    subst6 = Substitution(subst5)
                                                    try:
                                                        subst6.try_add_variable('i2.2.1.2.2', tmp180)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 21031
                                                        if len(subjects105) == 0:
                                                            pass
                                                            # State 21032
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 0: (d*(e + x*f)**p)**q
                                                                yield 0, subst6
                                                    subjects105.appendleft(tmp180)
                                        subjects168.appendleft(tmp177)
                                subjects168.appendleft(tmp171)
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.2.2.2.1.0', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 35071
                            if len(subjects168) >= 1 and isinstance(subjects168[0], Pow):
                                tmp183 = subjects168.popleft()
                                subjects184 = deque(tmp183._args)
                                # State 35072
                                if len(subjects184) >= 1:
                                    tmp185 = subjects184.popleft()
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i2.2.1.2.2.2.1.1', tmp185)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 35073
                                        if len(subjects184) >= 1:
                                            tmp187 = subjects184.popleft()
                                            subst5 = Substitution(subst4)
                                            try:
                                                subst5.try_add_variable('i2.2.1.2.2.2.1.2', tmp187)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 35074
                                                if len(subjects184) == 0:
                                                    pass
                                                    # State 35075
                                                    subst6 = Substitution(subst5)
                                                    try:
                                                        subst6.try_add_variable('i2.2.1.2.2.2', 1)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 35076
                                                        if len(subjects168) == 0:
                                                            pass
                                                            # State 35077
                                                            subst7 = Substitution(subst6)
                                                            try:
                                                                subst7.try_add_variable('i2.2.1.2.2', 1)
                                                            except ValueError:
                                                                pass
                                                            else:
                                                                pass
                                                                # State 35078
                                                                if len(subjects105) == 0:
                                                                    pass
                                                                    # State 35079
                                                                    if len(subjects) == 0:
                                                                        pass
                                                                        # 5: (d*(e + f*x**m)**p)**q
                                                                        yield 5, subst7
                                                            if len(subjects105) >= 1:
                                                                tmp191 = subjects105.popleft()
                                                                subst7 = Substitution(subst6)
                                                                try:
                                                                    subst7.try_add_variable('i2.2.1.2.2', tmp191)
                                                                except ValueError:
                                                                    pass
                                                                else:
                                                                    pass
                                                                    # State 35078
                                                                    if len(subjects105) == 0:
                                                                        pass
                                                                        # State 35079
                                                                        if len(subjects) == 0:
                                                                            pass
                                                                            # 5: (d*(e + f*x**m)**p)**q
                                                                            yield 5, subst7
                                                                subjects105.appendleft(tmp191)
                                                    if len(subjects168) >= 1:
                                                        tmp193 = subjects168.popleft()
                                                        subst6 = Substitution(subst5)
                                                        try:
                                                            subst6.try_add_variable('i2.2.1.2.2.2', tmp193)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            # State 35076
                                                            if len(subjects168) == 0:
                                                                pass
                                                                # State 35077
                                                                subst7 = Substitution(subst6)
                                                                try:
                                                                    subst7.try_add_variable('i2.2.1.2.2', 1)
                                                                except ValueError:
                                                                    pass
                                                                else:
                                                                    pass
                                                                    # State 35078
                                                                    if len(subjects105) == 0:
                                                                        pass
                                                                        # State 35079
                                                                        if len(subjects) == 0:
                                                                            pass
                                                                            # 5: (d*(e + f*x**m)**p)**q
                                                                            yield 5, subst7
                                                                if len(subjects105) >= 1:
                                                                    tmp196 = subjects105.popleft()
                                                                    subst7 = Substitution(subst6)
                                                                    try:
                                                                        subst7.try_add_variable('i2.2.1.2.2', tmp196)
                                                                    except ValueError:
                                                                        pass
                                                                    else:
                                                                        pass
                                                                        # State 35078
                                                                        if len(subjects105) == 0:
                                                                            pass
                                                                            # State 35079
                                                                            if len(subjects) == 0:
                                                                                pass
                                                                                # 5: (d*(e + f*x**m)**p)**q
                                                                                yield 5, subst7
                                                                    subjects105.appendleft(tmp196)
                                                        subjects168.appendleft(tmp193)
                                            subjects184.appendleft(tmp187)
                                    subjects184.appendleft(tmp185)
                                subjects168.appendleft(tmp183)
                        if len(subjects168) >= 1 and isinstance(subjects168[0], Mul):
                            tmp198 = subjects168.popleft()
                            associative1 = tmp198
                            associative_type1 = type(tmp198)
                            subjects199 = deque(tmp198._args)
                            matcher = CommutativeMatcher21034.get()
                            tmp200 = subjects199
                            subjects199 = []
                            for s in tmp200:
                                matcher.add_subject(s)
                            for pattern_index, subst3 in matcher.match(tmp200, subst2):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 21035
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i2.2.1.2.2.2', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 21036
                                        if len(subjects168) == 0:
                                            pass
                                            # State 21037
                                            subst5 = Substitution(subst4)
                                            try:
                                                subst5.try_add_variable('i2.2.1.2.2', 1)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 21038
                                                if len(subjects105) == 0:
                                                    pass
                                                    # State 21039
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 0: (d*(e + x*f)**p)**q
                                                        yield 0, subst5
                                            if len(subjects105) >= 1:
                                                tmp203 = subjects105.popleft()
                                                subst5 = Substitution(subst4)
                                                try:
                                                    subst5.try_add_variable('i2.2.1.2.2', tmp203)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 21038
                                                    if len(subjects105) == 0:
                                                        pass
                                                        # State 21039
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 0: (d*(e + x*f)**p)**q
                                                            yield 0, subst5
                                                subjects105.appendleft(tmp203)
                                    if len(subjects168) >= 1:
                                        tmp205 = []
                                        tmp205.append(subjects168.popleft())
                                        while True:
                                            if len(tmp205) > 1:
                                                tmp206 = create_operation_expression(associative1, tmp205)
                                            elif len(tmp205) == 1:
                                                tmp206 = tmp205[0]
                                            else:
                                                assert False, "Unreachable"
                                            subst4 = Substitution(subst3)
                                            try:
                                                subst4.try_add_variable('i2.2.1.2.2.2', tmp206)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 21036
                                                if len(subjects168) == 0:
                                                    pass
                                                    # State 21037
                                                    subst5 = Substitution(subst4)
                                                    try:
                                                        subst5.try_add_variable('i2.2.1.2.2', 1)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 21038
                                                        if len(subjects105) == 0:
                                                            pass
                                                            # State 21039
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 0: (d*(e + x*f)**p)**q
                                                                yield 0, subst5
                                                    if len(subjects105) >= 1:
                                                        tmp209 = subjects105.popleft()
                                                        subst5 = Substitution(subst4)
                                                        try:
                                                            subst5.try_add_variable('i2.2.1.2.2', tmp209)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            # State 21038
                                                            if len(subjects105) == 0:
                                                                pass
                                                                # State 21039
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 0: (d*(e + x*f)**p)**q
                                                                    yield 0, subst5
                                                        subjects105.appendleft(tmp209)
                                            if len(subjects168) == 0:
                                                break
                                            tmp205.append(subjects168.popleft())
                                        subjects168.extendleft(reversed(tmp205))
                                if pattern_index == 1:
                                    pass
                                    # State 35084
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i2.2.1.2.2.2', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 35085
                                        if len(subjects168) == 0:
                                            pass
                                            # State 35086
                                            subst5 = Substitution(subst4)
                                            try:
                                                subst5.try_add_variable('i2.2.1.2.2', 1)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 35087
                                                if len(subjects105) == 0:
                                                    pass
                                                    # State 35088
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 5: (d*(e + f*x**m)**p)**q
                                                        yield 5, subst5
                                            if len(subjects105) >= 1:
                                                tmp213 = subjects105.popleft()
                                                subst5 = Substitution(subst4)
                                                try:
                                                    subst5.try_add_variable('i2.2.1.2.2', tmp213)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 35087
                                                    if len(subjects105) == 0:
                                                        pass
                                                        # State 35088
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 5: (d*(e + f*x**m)**p)**q
                                                            yield 5, subst5
                                                subjects105.appendleft(tmp213)
                                    if len(subjects168) >= 1:
                                        tmp215 = []
                                        tmp215.append(subjects168.popleft())
                                        while True:
                                            if len(tmp215) > 1:
                                                tmp216 = create_operation_expression(associative1, tmp215)
                                            elif len(tmp215) == 1:
                                                tmp216 = tmp215[0]
                                            else:
                                                assert False, "Unreachable"
                                            subst4 = Substitution(subst3)
                                            try:
                                                subst4.try_add_variable('i2.2.1.2.2.2', tmp216)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 35085
                                                if len(subjects168) == 0:
                                                    pass
                                                    # State 35086
                                                    subst5 = Substitution(subst4)
                                                    try:
                                                        subst5.try_add_variable('i2.2.1.2.2', 1)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 35087
                                                        if len(subjects105) == 0:
                                                            pass
                                                            # State 35088
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 5: (d*(e + f*x**m)**p)**q
                                                                yield 5, subst5
                                                    if len(subjects105) >= 1:
                                                        tmp219 = subjects105.popleft()
                                                        subst5 = Substitution(subst4)
                                                        try:
                                                            subst5.try_add_variable('i2.2.1.2.2', tmp219)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            # State 35087
                                                            if len(subjects105) == 0:
                                                                pass
                                                                # State 35088
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 5: (d*(e + f*x**m)**p)**q
                                                                    yield 5, subst5
                                                        subjects105.appendleft(tmp219)
                                            if len(subjects168) == 0:
                                                break
                                            tmp215.append(subjects168.popleft())
                                        subjects168.extendleft(reversed(tmp215))
                            subjects168.appendleft(tmp198)
                    if len(subjects168) >= 1:
                        tmp221 = subjects168.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.1.2.2.1', tmp221)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 25696
                            if len(subjects168) >= 1:
                                tmp223 = subjects168.popleft()
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i2.2.1.2.2.2', tmp223)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 25697
                                    if len(subjects168) == 0:
                                        pass
                                        # State 25698
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.2.1.2.2', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 25699
                                            if len(subjects105) == 0:
                                                pass
                                                # State 25700
                                                if len(subjects) == 0:
                                                    pass
                                                    # 1: (d*v**p)**q
                                                    yield 1, subst4
                                        if len(subjects105) >= 1:
                                            tmp226 = subjects105.popleft()
                                            subst4 = Substitution(subst3)
                                            try:
                                                subst4.try_add_variable('i2.2.1.2.2', tmp226)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 25699
                                                if len(subjects105) == 0:
                                                    pass
                                                    # State 25700
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 1: (d*v**p)**q
                                                        yield 1, subst4
                                            subjects105.appendleft(tmp226)
                                subjects168.appendleft(tmp223)
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.2.2.2', 1)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 45637
                                if len(subjects168) == 0:
                                    pass
                                    # State 45638
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i2.2.1.2.2', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 45639
                                        if len(subjects105) == 0:
                                            pass
                                            # State 45640
                                            if len(subjects) == 0:
                                                pass
                                                # 7: (d*v**p)**q
                                                yield 7, subst4
                                    if len(subjects105) >= 1:
                                        tmp230 = subjects105.popleft()
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.2.1.2.2', tmp230)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 45639
                                            if len(subjects105) == 0:
                                                pass
                                                # State 45640
                                                if len(subjects) == 0:
                                                    pass
                                                    # 7: (d*v**p)**q
                                                    yield 7, subst4
                                        subjects105.appendleft(tmp230)
                            if len(subjects168) >= 1:
                                tmp232 = subjects168.popleft()
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i2.2.1.2.2.2', tmp232)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 45637
                                    if len(subjects168) == 0:
                                        pass
                                        # State 45638
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.2.1.2.2', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 45639
                                            if len(subjects105) == 0:
                                                pass
                                                # State 45640
                                                if len(subjects) == 0:
                                                    pass
                                                    # 7: (d*v**p)**q
                                                    yield 7, subst4
                                        if len(subjects105) >= 1:
                                            tmp235 = subjects105.popleft()
                                            subst4 = Substitution(subst3)
                                            try:
                                                subst4.try_add_variable('i2.2.1.2.2', tmp235)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 45639
                                                if len(subjects105) == 0:
                                                    pass
                                                    # State 45640
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 7: (d*v**p)**q
                                                        yield 7, subst4
                                            subjects105.appendleft(tmp235)
                                subjects168.appendleft(tmp232)
                        subjects168.appendleft(tmp221)
                    if len(subjects168) >= 1 and isinstance(subjects168[0], Add):
                        tmp237 = subjects168.popleft()
                        associative1 = tmp237
                        associative_type1 = type(tmp237)
                        subjects238 = deque(tmp237._args)
                        matcher = CommutativeMatcher21041.get()
                        tmp239 = subjects238
                        subjects238 = []
                        for s in tmp239:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp239, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 21047
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i2.2.1.2.2.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 21048
                                    if len(subjects168) == 0:
                                        pass
                                        # State 21049
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.2.1.2.2', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 21050
                                            if len(subjects105) == 0:
                                                pass
                                                # State 21051
                                                if len(subjects) == 0:
                                                    pass
                                                    # 0: (d*(e + x*f)**p)**q
                                                    yield 0, subst4
                                        if len(subjects105) >= 1:
                                            tmp242 = subjects105.popleft()
                                            subst4 = Substitution(subst3)
                                            try:
                                                subst4.try_add_variable('i2.2.1.2.2', tmp242)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 21050
                                                if len(subjects105) == 0:
                                                    pass
                                                    # State 21051
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 0: (d*(e + x*f)**p)**q
                                                        yield 0, subst4
                                            subjects105.appendleft(tmp242)
                                if len(subjects168) >= 1:
                                    tmp244 = []
                                    tmp244.append(subjects168.popleft())
                                    while True:
                                        if len(tmp244) > 1:
                                            tmp245 = create_operation_expression(associative1, tmp244)
                                        elif len(tmp244) == 1:
                                            tmp245 = tmp244[0]
                                        else:
                                            assert False, "Unreachable"
                                        subst3 = Substitution(subst2)
                                        try:
                                            subst3.try_add_variable('i2.2.1.2.2.2', tmp245)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 21048
                                            if len(subjects168) == 0:
                                                pass
                                                # State 21049
                                                subst4 = Substitution(subst3)
                                                try:
                                                    subst4.try_add_variable('i2.2.1.2.2', 1)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 21050
                                                    if len(subjects105) == 0:
                                                        pass
                                                        # State 21051
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 0: (d*(e + x*f)**p)**q
                                                            yield 0, subst4
                                                if len(subjects105) >= 1:
                                                    tmp248 = subjects105.popleft()
                                                    subst4 = Substitution(subst3)
                                                    try:
                                                        subst4.try_add_variable('i2.2.1.2.2', tmp248)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 21050
                                                        if len(subjects105) == 0:
                                                            pass
                                                            # State 21051
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 0: (d*(e + x*f)**p)**q
                                                                yield 0, subst4
                                                    subjects105.appendleft(tmp248)
                                        if len(subjects168) == 0:
                                            break
                                        tmp244.append(subjects168.popleft())
                                    subjects168.extendleft(reversed(tmp244))
                            if pattern_index == 1:
                                pass
                                # State 29361
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i2.2.1.2.2.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 29362
                                    if len(subjects168) == 0:
                                        pass
                                        # State 29363
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.2.1.2.2', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 29364
                                            if len(subjects105) == 0:
                                                pass
                                                # State 29365
                                                if len(subjects) == 0:
                                                    pass
                                                    # 3: (d*(e + f*x**m)**p)**q
                                                    yield 3, subst4
                                        if len(subjects105) >= 1:
                                            tmp252 = subjects105.popleft()
                                            subst4 = Substitution(subst3)
                                            try:
                                                subst4.try_add_variable('i2.2.1.2.2', tmp252)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 29364
                                                if len(subjects105) == 0:
                                                    pass
                                                    # State 29365
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 3: (d*(e + f*x**m)**p)**q
                                                        yield 3, subst4
                                            subjects105.appendleft(tmp252)
                                if len(subjects168) >= 1:
                                    tmp254 = []
                                    tmp254.append(subjects168.popleft())
                                    while True:
                                        if len(tmp254) > 1:
                                            tmp255 = create_operation_expression(associative1, tmp254)
                                        elif len(tmp254) == 1:
                                            tmp255 = tmp254[0]
                                        else:
                                            assert False, "Unreachable"
                                        subst3 = Substitution(subst2)
                                        try:
                                            subst3.try_add_variable('i2.2.1.2.2.2', tmp255)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 29362
                                            if len(subjects168) == 0:
                                                pass
                                                # State 29363
                                                subst4 = Substitution(subst3)
                                                try:
                                                    subst4.try_add_variable('i2.2.1.2.2', 1)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 29364
                                                    if len(subjects105) == 0:
                                                        pass
                                                        # State 29365
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 3: (d*(e + f*x**m)**p)**q
                                                            yield 3, subst4
                                                if len(subjects105) >= 1:
                                                    tmp258 = subjects105.popleft()
                                                    subst4 = Substitution(subst3)
                                                    try:
                                                        subst4.try_add_variable('i2.2.1.2.2', tmp258)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 29364
                                                        if len(subjects105) == 0:
                                                            pass
                                                            # State 29365
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 3: (d*(e + f*x**m)**p)**q
                                                                yield 3, subst4
                                                    subjects105.appendleft(tmp258)
                                        if len(subjects168) == 0:
                                            break
                                        tmp254.append(subjects168.popleft())
                                    subjects168.extendleft(reversed(tmp254))
                            if pattern_index == 2:
                                pass
                                # State 35089
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i2.2.1.2.2.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 35090
                                    if len(subjects168) == 0:
                                        pass
                                        # State 35091
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.2.1.2.2', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 35092
                                            if len(subjects105) == 0:
                                                pass
                                                # State 35093
                                                if len(subjects) == 0:
                                                    pass
                                                    # 5: (d*(e + f*x**m)**p)**q
                                                    yield 5, subst4
                                        if len(subjects105) >= 1:
                                            tmp262 = subjects105.popleft()
                                            subst4 = Substitution(subst3)
                                            try:
                                                subst4.try_add_variable('i2.2.1.2.2', tmp262)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 35092
                                                if len(subjects105) == 0:
                                                    pass
                                                    # State 35093
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 5: (d*(e + f*x**m)**p)**q
                                                        yield 5, subst4
                                            subjects105.appendleft(tmp262)
                                if len(subjects168) >= 1:
                                    tmp264 = []
                                    tmp264.append(subjects168.popleft())
                                    while True:
                                        if len(tmp264) > 1:
                                            tmp265 = create_operation_expression(associative1, tmp264)
                                        elif len(tmp264) == 1:
                                            tmp265 = tmp264[0]
                                        else:
                                            assert False, "Unreachable"
                                        subst3 = Substitution(subst2)
                                        try:
                                            subst3.try_add_variable('i2.2.1.2.2.2', tmp265)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 35090
                                            if len(subjects168) == 0:
                                                pass
                                                # State 35091
                                                subst4 = Substitution(subst3)
                                                try:
                                                    subst4.try_add_variable('i2.2.1.2.2', 1)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 35092
                                                    if len(subjects105) == 0:
                                                        pass
                                                        # State 35093
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 5: (d*(e + f*x**m)**p)**q
                                                            yield 5, subst4
                                                if len(subjects105) >= 1:
                                                    tmp268 = subjects105.popleft()
                                                    subst4 = Substitution(subst3)
                                                    try:
                                                        subst4.try_add_variable('i2.2.1.2.2', tmp268)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 35092
                                                        if len(subjects105) == 0:
                                                            pass
                                                            # State 35093
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 5: (d*(e + f*x**m)**p)**q
                                                                yield 5, subst4
                                                    subjects105.appendleft(tmp268)
                                        if len(subjects168) == 0:
                                            break
                                        tmp264.append(subjects168.popleft())
                                    subjects168.extendleft(reversed(tmp264))
                            if pattern_index == 3:
                                pass
                                # State 44342
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i2.2.1.2.2.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 44343
                                    if len(subjects168) == 0:
                                        pass
                                        # State 44344
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.2.1.2.2', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 44345
                                            if len(subjects105) == 0:
                                                pass
                                                # State 44346
                                                if len(subjects) == 0:
                                                    pass
                                                    # 6: (d*(e + f*x + g*x**2)**p)**q
                                                    yield 6, subst4
                                        if len(subjects105) >= 1:
                                            tmp272 = subjects105.popleft()
                                            subst4 = Substitution(subst3)
                                            try:
                                                subst4.try_add_variable('i2.2.1.2.2', tmp272)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 44345
                                                if len(subjects105) == 0:
                                                    pass
                                                    # State 44346
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 6: (d*(e + f*x + g*x**2)**p)**q
                                                        yield 6, subst4
                                            subjects105.appendleft(tmp272)
                                if len(subjects168) >= 1:
                                    tmp274 = []
                                    tmp274.append(subjects168.popleft())
                                    while True:
                                        if len(tmp274) > 1:
                                            tmp275 = create_operation_expression(associative1, tmp274)
                                        elif len(tmp274) == 1:
                                            tmp275 = tmp274[0]
                                        else:
                                            assert False, "Unreachable"
                                        subst3 = Substitution(subst2)
                                        try:
                                            subst3.try_add_variable('i2.2.1.2.2.2', tmp275)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 44343
                                            if len(subjects168) == 0:
                                                pass
                                                # State 44344
                                                subst4 = Substitution(subst3)
                                                try:
                                                    subst4.try_add_variable('i2.2.1.2.2', 1)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 44345
                                                    if len(subjects105) == 0:
                                                        pass
                                                        # State 44346
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 6: (d*(e + f*x + g*x**2)**p)**q
                                                            yield 6, subst4
                                                if len(subjects105) >= 1:
                                                    tmp278 = subjects105.popleft()
                                                    subst4 = Substitution(subst3)
                                                    try:
                                                        subst4.try_add_variable('i2.2.1.2.2', tmp278)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 44345
                                                        if len(subjects105) == 0:
                                                            pass
                                                            # State 44346
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 6: (d*(e + f*x + g*x**2)**p)**q
                                                                yield 6, subst4
                                                    subjects105.appendleft(tmp278)
                                        if len(subjects168) == 0:
                                            break
                                        tmp274.append(subjects168.popleft())
                                    subjects168.extendleft(reversed(tmp274))
                        subjects168.appendleft(tmp237)
                    if len(subjects168) >= 1 and isinstance(subjects168[0], Mul):
                        tmp280 = subjects168.popleft()
                        associative1 = tmp280
                        associative_type1 = type(tmp280)
                        subjects281 = deque(tmp280._args)
                        matcher = CommutativeMatcher32265.get()
                        tmp282 = subjects281
                        subjects281 = []
                        for s in tmp282:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp282, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 32289
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i2.2.1.2.2.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 32290
                                    if len(subjects168) == 0:
                                        pass
                                        # State 32291
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.2.1.2.2', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 32292
                                            if len(subjects105) == 0:
                                                pass
                                                # State 32293
                                                if len(subjects) == 0:
                                                    pass
                                                    # 4: (d*(x**m*(f + e*x**r))**p)**q
                                                    yield 4, subst4
                                        if len(subjects105) >= 1:
                                            tmp285 = subjects105.popleft()
                                            subst4 = Substitution(subst3)
                                            try:
                                                subst4.try_add_variable('i2.2.1.2.2', tmp285)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 32292
                                                if len(subjects105) == 0:
                                                    pass
                                                    # State 32293
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 4: (d*(x**m*(f + e*x**r))**p)**q
                                                        yield 4, subst4
                                            subjects105.appendleft(tmp285)
                                if len(subjects168) >= 1:
                                    tmp287 = []
                                    tmp287.append(subjects168.popleft())
                                    while True:
                                        if len(tmp287) > 1:
                                            tmp288 = create_operation_expression(associative1, tmp287)
                                        elif len(tmp287) == 1:
                                            tmp288 = tmp287[0]
                                        else:
                                            assert False, "Unreachable"
                                        subst3 = Substitution(subst2)
                                        try:
                                            subst3.try_add_variable('i2.2.1.2.2.2', tmp288)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 32290
                                            if len(subjects168) == 0:
                                                pass
                                                # State 32291
                                                subst4 = Substitution(subst3)
                                                try:
                                                    subst4.try_add_variable('i2.2.1.2.2', 1)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 32292
                                                    if len(subjects105) == 0:
                                                        pass
                                                        # State 32293
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 4: (d*(x**m*(f + e*x**r))**p)**q
                                                            yield 4, subst4
                                                if len(subjects105) >= 1:
                                                    tmp291 = subjects105.popleft()
                                                    subst4 = Substitution(subst3)
                                                    try:
                                                        subst4.try_add_variable('i2.2.1.2.2', tmp291)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 32292
                                                        if len(subjects105) == 0:
                                                            pass
                                                            # State 32293
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 4: (d*(x**m*(f + e*x**r))**p)**q
                                                                yield 4, subst4
                                                    subjects105.appendleft(tmp291)
                                        if len(subjects168) == 0:
                                            break
                                        tmp287.append(subjects168.popleft())
                                    subjects168.extendleft(reversed(tmp287))
                        subjects168.appendleft(tmp280)
                    subjects105.appendleft(tmp167)
            if len(subjects105) >= 1:
                tmp293 = subjects105.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.1.2.1', tmp293)
                except ValueError:
                    pass
                else:
                    pass
                    # State 53275
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.2.2', 1)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 53276
                        if len(subjects105) == 0:
                            pass
                            # State 53277
                            if len(subjects) == 0:
                                pass
                                # 9: RFx**p
                                yield 9, subst2
                    if len(subjects105) >= 1:
                        tmp296 = subjects105.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.1.2.2', tmp296)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 53276
                            if len(subjects105) == 0:
                                pass
                                # State 53277
                                if len(subjects) == 0:
                                    pass
                                    # 9: RFx**p
                                    yield 9, subst2
                        subjects105.appendleft(tmp296)
                subjects105.appendleft(tmp293)
            if len(subjects105) >= 1 and isinstance(subjects105[0], Mul):
                tmp298 = subjects105.popleft()
                associative1 = tmp298
                associative_type1 = type(tmp298)
                subjects299 = deque(tmp298._args)
                matcher = CommutativeMatcher21053.get()
                tmp300 = subjects299
                subjects299 = []
                for s in tmp300:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp300, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 21090
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.1.2.2', 1)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 21091
                            if len(subjects105) == 0:
                                pass
                                # State 21092
                                if len(subjects) == 0:
                                    pass
                                    # 0: (d*(e + x*f)**p)**q
                                    yield 0, subst2
                        if len(subjects105) >= 1:
                            tmp302 = []
                            tmp302.append(subjects105.popleft())
                            while True:
                                if len(tmp302) > 1:
                                    tmp303 = create_operation_expression(associative1, tmp302)
                                elif len(tmp302) == 1:
                                    tmp303 = tmp302[0]
                                else:
                                    assert False, "Unreachable"
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i2.2.1.2.2', tmp303)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 21091
                                    if len(subjects105) == 0:
                                        pass
                                        # State 21092
                                        if len(subjects) == 0:
                                            pass
                                            # 0: (d*(e + x*f)**p)**q
                                            yield 0, subst2
                                if len(subjects105) == 0:
                                    break
                                tmp302.append(subjects105.popleft())
                            subjects105.extendleft(reversed(tmp302))
                    if pattern_index == 1:
                        pass
                        # State 25704
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.1.2.2', 1)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 25705
                            if len(subjects105) == 0:
                                pass
                                # State 25706
                                if len(subjects) == 0:
                                    pass
                                    # 1: (d*v**p)**q
                                    yield 1, subst2
                        if len(subjects105) >= 1:
                            tmp306 = []
                            tmp306.append(subjects105.popleft())
                            while True:
                                if len(tmp306) > 1:
                                    tmp307 = create_operation_expression(associative1, tmp306)
                                elif len(tmp306) == 1:
                                    tmp307 = tmp306[0]
                                else:
                                    assert False, "Unreachable"
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i2.2.1.2.2', tmp307)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 25705
                                    if len(subjects105) == 0:
                                        pass
                                        # State 25706
                                        if len(subjects) == 0:
                                            pass
                                            # 1: (d*v**p)**q
                                            yield 1, subst2
                                if len(subjects105) == 0:
                                    break
                                tmp306.append(subjects105.popleft())
                            subjects105.extendleft(reversed(tmp306))
                    if pattern_index == 2:
                        pass
                        # State 29390
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.1.2.2', 1)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 29391
                            if len(subjects105) == 0:
                                pass
                                # State 29392
                                if len(subjects) == 0:
                                    pass
                                    # 3: (d*(e + f*x**m)**p)**q
                                    yield 3, subst2
                        if len(subjects105) >= 1:
                            tmp310 = []
                            tmp310.append(subjects105.popleft())
                            while True:
                                if len(tmp310) > 1:
                                    tmp311 = create_operation_expression(associative1, tmp310)
                                elif len(tmp310) == 1:
                                    tmp311 = tmp310[0]
                                else:
                                    assert False, "Unreachable"
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i2.2.1.2.2', tmp311)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 29391
                                    if len(subjects105) == 0:
                                        pass
                                        # State 29392
                                        if len(subjects) == 0:
                                            pass
                                            # 3: (d*(e + f*x**m)**p)**q
                                            yield 3, subst2
                                if len(subjects105) == 0:
                                    break
                                tmp310.append(subjects105.popleft())
                            subjects105.extendleft(reversed(tmp310))
                    if pattern_index == 3:
                        pass
                        # State 32348
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.1.2.2', 1)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 32349
                            if len(subjects105) == 0:
                                pass
                                # State 32350
                                if len(subjects) == 0:
                                    pass
                                    # 4: (d*(x**m*(f + e*x**r))**p)**q
                                    yield 4, subst2
                        if len(subjects105) >= 1:
                            tmp314 = []
                            tmp314.append(subjects105.popleft())
                            while True:
                                if len(tmp314) > 1:
                                    tmp315 = create_operation_expression(associative1, tmp314)
                                elif len(tmp314) == 1:
                                    tmp315 = tmp314[0]
                                else:
                                    assert False, "Unreachable"
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i2.2.1.2.2', tmp315)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 32349
                                    if len(subjects105) == 0:
                                        pass
                                        # State 32350
                                        if len(subjects) == 0:
                                            pass
                                            # 4: (d*(x**m*(f + e*x**r))**p)**q
                                            yield 4, subst2
                                if len(subjects105) == 0:
                                    break
                                tmp314.append(subjects105.popleft())
                            subjects105.extendleft(reversed(tmp314))
                    if pattern_index == 4:
                        pass
                        # State 35122
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.1.2.2', 1)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 35123
                            if len(subjects105) == 0:
                                pass
                                # State 35124
                                if len(subjects) == 0:
                                    pass
                                    # 5: (d*(e + f*x**m)**p)**q
                                    yield 5, subst2
                        if len(subjects105) >= 1:
                            tmp318 = []
                            tmp318.append(subjects105.popleft())
                            while True:
                                if len(tmp318) > 1:
                                    tmp319 = create_operation_expression(associative1, tmp318)
                                elif len(tmp318) == 1:
                                    tmp319 = tmp318[0]
                                else:
                                    assert False, "Unreachable"
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i2.2.1.2.2', tmp319)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 35123
                                    if len(subjects105) == 0:
                                        pass
                                        # State 35124
                                        if len(subjects) == 0:
                                            pass
                                            # 5: (d*(e + f*x**m)**p)**q
                                            yield 5, subst2
                                if len(subjects105) == 0:
                                    break
                                tmp318.append(subjects105.popleft())
                            subjects105.extendleft(reversed(tmp318))
                    if pattern_index == 5:
                        pass
                        # State 44365
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.1.2.2', 1)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 44366
                            if len(subjects105) == 0:
                                pass
                                # State 44367
                                if len(subjects) == 0:
                                    pass
                                    # 6: (d*(e + f*x + g*x**2)**p)**q
                                    yield 6, subst2
                        if len(subjects105) >= 1:
                            tmp322 = []
                            tmp322.append(subjects105.popleft())
                            while True:
                                if len(tmp322) > 1:
                                    tmp323 = create_operation_expression(associative1, tmp322)
                                elif len(tmp322) == 1:
                                    tmp323 = tmp322[0]
                                else:
                                    assert False, "Unreachable"
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i2.2.1.2.2', tmp323)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 44366
                                    if len(subjects105) == 0:
                                        pass
                                        # State 44367
                                        if len(subjects) == 0:
                                            pass
                                            # 6: (d*(e + f*x + g*x**2)**p)**q
                                            yield 6, subst2
                                if len(subjects105) == 0:
                                    break
                                tmp322.append(subjects105.popleft())
                            subjects105.extendleft(reversed(tmp322))
                    if pattern_index == 6:
                        pass
                        # State 45644
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.1.2.2', 1)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 45645
                            if len(subjects105) == 0:
                                pass
                                # State 45646
                                if len(subjects) == 0:
                                    pass
                                    # 7: (d*v**p)**q
                                    yield 7, subst2
                        if len(subjects105) >= 1:
                            tmp326 = []
                            tmp326.append(subjects105.popleft())
                            while True:
                                if len(tmp326) > 1:
                                    tmp327 = create_operation_expression(associative1, tmp326)
                                elif len(tmp326) == 1:
                                    tmp327 = tmp326[0]
                                else:
                                    assert False, "Unreachable"
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i2.2.1.2.2', tmp327)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 45645
                                    if len(subjects105) == 0:
                                        pass
                                        # State 45646
                                        if len(subjects) == 0:
                                            pass
                                            # 7: (d*v**p)**q
                                            yield 7, subst2
                                if len(subjects105) == 0:
                                    break
                                tmp326.append(subjects105.popleft())
                            subjects105.extendleft(reversed(tmp326))
                subjects105.appendleft(tmp298)
            if len(subjects105) >= 1 and isinstance(subjects105[0], Add):
                tmp329 = subjects105.popleft()
                associative1 = tmp329
                associative_type1 = type(tmp329)
                subjects330 = deque(tmp329._args)
                matcher = CommutativeMatcher50863.get()
                tmp331 = subjects330
                subjects330 = []
                for s in tmp331:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp331, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 50876
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.1.2.2', 1)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 50877
                            if len(subjects105) == 0:
                                pass
                                # State 50878
                                if len(subjects) == 0:
                                    pass
                                    # 8: (d + e*x**2)**p
                                    yield 8, subst2
                        if len(subjects105) >= 1:
                            tmp333 = []
                            tmp333.append(subjects105.popleft())
                            while True:
                                if len(tmp333) > 1:
                                    tmp334 = create_operation_expression(associative1, tmp333)
                                elif len(tmp333) == 1:
                                    tmp334 = tmp333[0]
                                else:
                                    assert False, "Unreachable"
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i2.2.1.2.2', tmp334)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 50877
                                    if len(subjects105) == 0:
                                        pass
                                        # State 50878
                                        if len(subjects) == 0:
                                            pass
                                            # 8: (d + e*x**2)**p
                                            yield 8, subst2
                                if len(subjects105) == 0:
                                    break
                                tmp333.append(subjects105.popleft())
                            subjects105.extendleft(reversed(tmp333))
                subjects105.appendleft(tmp329)
            subjects.appendleft(tmp104)
        if len(subjects) >= 1 and isinstance(subjects[0], Add):
            tmp336 = subjects.popleft()
            associative1 = tmp336
            associative_type1 = type(tmp336)
            subjects337 = deque(tmp336._args)
            matcher = CommutativeMatcher26164.get()
            tmp338 = subjects337
            subjects337 = []
            for s in tmp338:
                matcher.add_subject(s)
            for pattern_index, subst1 in matcher.match(tmp338, subst0):
                pass
                if pattern_index == 0:
                    pass
                    # State 26170
                    if len(subjects) == 0:
                        pass
                        # 2: e + x*f
                        yield 2, subst1
            subjects.appendleft(tmp336)
        return
        yield


from .generated_part005578 import *
from .generated_part005584 import *
from .generated_part005579 import *
from .generated_part005609 import *
from .generated_part005597 import *
from .generated_part005606 import *
from .generated_part005573 import *
from .generated_part005607 import *
from collections import deque
from .generated_part005625 import *
from .generated_part005627 import *
from matchpy.utils import VariableWithCount
from .generated_part005581 import *
from .generated_part005572 import *
from .generated_part005603 import *
from multiset import Multiset
from .generated_part005600 import *
from matchpy.matching.many_to_one import CommutativeMatcher
from .generated_part005575 import *
from .generated_part005601 import *
from .generated_part005612 import *
from .generated_part005599 import *