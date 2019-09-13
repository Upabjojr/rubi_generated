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

class CommutativeMatcher2303(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({0: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    1: (1, Multiset({1: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    2: (2, Multiset({2: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    3: (3, Multiset({3: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    4: (4, Multiset({4: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    5: (5, Multiset({5: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    6: (6, Multiset({6: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
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
        if CommutativeMatcher2303._instance is None:
            CommutativeMatcher2303._instance = CommutativeMatcher2303()
        return CommutativeMatcher2303._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 2302
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.2', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 2304
            if len(subjects) >= 1:
                tmp2 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.1', tmp2)
                except ValueError:
                    pass
                else:
                    pass
                    # State 2305
                    if len(subjects) == 0:
                        pass
                        # 0: x**n /; (cons_f2) and (cons_f3) and (cons_f4) and (cons_f5)
                subjects.appendleft(tmp2)
        if len(subjects) >= 1 and isinstance(subjects[0], Pow):
            tmp4 = subjects.popleft()
            subjects5 = deque(tmp4._args)
            # State 2306
            if len(subjects5) >= 1:
                tmp6 = subjects5.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.1.1', tmp6)
                except ValueError:
                    pass
                else:
                    pass
                    # State 2307
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.2', 1)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 2308
                        if len(subjects5) == 0:
                            pass
                            # State 2309
                            if len(subjects) == 0:
                                pass
                                # 0: x**n /; (cons_f2) and (cons_f3) and (cons_f4) and (cons_f5)
                    if len(subjects5) >= 1:
                        tmp9 = subjects5.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.1.2', tmp9)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 2308
                            if len(subjects5) == 0:
                                pass
                                # State 2309
                                if len(subjects) == 0:
                                    pass
                                    # 0: x**n /; (cons_f2) and (cons_f3) and (cons_f4) and (cons_f5)
                        subjects5.appendleft(tmp9)
                subjects5.appendleft(tmp6)
            subjects.appendleft(tmp4)
        if len(subjects) >= 1 and isinstance(subjects[0], log):
            tmp11 = subjects.popleft()
            subjects12 = deque(tmp11._args)
            # State 40921
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.0', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 40922
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.2', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 40923
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.2.1.2.2.0', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 40924
                        subst4 = Substitution(subst3)
                        try:
                            subst4.try_add_variable('i2.2.1.2.2.2', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 40925
                            if len(subjects12) >= 1 and isinstance(subjects12[0], Add):
                                tmp17 = subjects12.popleft()
                                associative1 = tmp17
                                associative_type1 = type(tmp17)
                                subjects18 = deque(tmp17._args)
                                matcher = CommutativeMatcher40927.get()
                                tmp19 = subjects18
                                subjects18 = []
                                for s in tmp19:
                                    matcher.add_subject(s)
                                for pattern_index, subst5 in matcher.match(tmp19, subst4):
                                    pass
                                    if pattern_index == 0:
                                        pass
                                        # State 40943
                                        if len(subjects12) == 0:
                                            pass
                                            # State 40944
                                            if len(subjects) == 0:
                                                pass
                                                # 1: log(c*(d*(e + f*x + g*x**2)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f210) and (cons_f52) and (cons_f4) and (cons_f1201) and (cons_f40)
                                subjects12.appendleft(tmp17)
                            if len(subjects12) >= 1:
                                tmp20 = subjects12.popleft()
                                subst5 = Substitution(subst4)
                                try:
                                    subst5.try_add_variable('i2.2.1.2.2.1', tmp20)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 44956
                                    if len(subjects12) == 0:
                                        pass
                                        # State 44957
                                        if len(subjects) == 0:
                                            pass
                                            # 2: log(c*(d*v**p)**q) /; (cons_f8) and (cons_f29) and (cons_f5) and (cons_f52) and (cons_f554) and (cons_f1202)
                                subjects12.appendleft(tmp20)
                        if len(subjects12) >= 1 and isinstance(subjects12[0], Pow):
                            tmp22 = subjects12.popleft()
                            subjects23 = deque(tmp22._args)
                            # State 40945
                            if len(subjects23) >= 1 and isinstance(subjects23[0], Add):
                                tmp24 = subjects23.popleft()
                                associative1 = tmp24
                                associative_type1 = type(tmp24)
                                subjects25 = deque(tmp24._args)
                                matcher = CommutativeMatcher40947.get()
                                tmp26 = subjects25
                                subjects25 = []
                                for s in tmp26:
                                    matcher.add_subject(s)
                                for pattern_index, subst4 in matcher.match(tmp26, subst3):
                                    pass
                                    if pattern_index == 0:
                                        pass
                                        # State 40963
                                        subst5 = Substitution(subst4)
                                        try:
                                            subst5.try_add_variable('i2.2.1.2.2.2', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 40964
                                            if len(subjects23) == 0:
                                                pass
                                                # State 40965
                                                if len(subjects12) == 0:
                                                    pass
                                                    # State 40966
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 1: log(c*(d*(e + f*x + g*x**2)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f210) and (cons_f52) and (cons_f4) and (cons_f1201) and (cons_f40)
                                        if len(subjects23) >= 1:
                                            tmp28 = []
                                            tmp28.append(subjects23.popleft())
                                            while True:
                                                if len(tmp28) > 1:
                                                    tmp29 = create_operation_expression(associative1, tmp28)
                                                elif len(tmp28) == 1:
                                                    tmp29 = tmp28[0]
                                                else:
                                                    assert False, "Unreachable"
                                                subst5 = Substitution(subst4)
                                                try:
                                                    subst5.try_add_variable('i2.2.1.2.2.2', tmp29)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 40964
                                                    if len(subjects23) == 0:
                                                        pass
                                                        # State 40965
                                                        if len(subjects12) == 0:
                                                            pass
                                                            # State 40966
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 1: log(c*(d*(e + f*x + g*x**2)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f210) and (cons_f52) and (cons_f4) and (cons_f1201) and (cons_f40)
                                                if len(subjects23) == 0:
                                                    break
                                                tmp28.append(subjects23.popleft())
                                            subjects23.extendleft(reversed(tmp28))
                                subjects23.appendleft(tmp24)
                            if len(subjects23) >= 1:
                                tmp31 = subjects23.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.2.1.2.2.1', tmp31)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 44958
                                    subst5 = Substitution(subst4)
                                    try:
                                        subst5.try_add_variable('i2.2.1.2.2.2', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 44959
                                        if len(subjects23) == 0:
                                            pass
                                            # State 44960
                                            if len(subjects12) == 0:
                                                pass
                                                # State 44961
                                                if len(subjects) == 0:
                                                    pass
                                                    # 2: log(c*(d*v**p)**q) /; (cons_f8) and (cons_f29) and (cons_f5) and (cons_f52) and (cons_f554) and (cons_f1202)
                                    if len(subjects23) >= 1:
                                        tmp34 = subjects23.popleft()
                                        subst5 = Substitution(subst4)
                                        try:
                                            subst5.try_add_variable('i2.2.1.2.2.2', tmp34)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 44959
                                            if len(subjects23) == 0:
                                                pass
                                                # State 44960
                                                if len(subjects12) == 0:
                                                    pass
                                                    # State 44961
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 2: log(c*(d*v**p)**q) /; (cons_f8) and (cons_f29) and (cons_f5) and (cons_f52) and (cons_f554) and (cons_f1202)
                                        subjects23.appendleft(tmp34)
                                subjects23.appendleft(tmp31)
                            subjects12.appendleft(tmp22)
                    if len(subjects12) >= 1 and isinstance(subjects12[0], Mul):
                        tmp36 = subjects12.popleft()
                        associative1 = tmp36
                        associative_type1 = type(tmp36)
                        subjects37 = deque(tmp36._args)
                        matcher = CommutativeMatcher40968.get()
                        tmp38 = subjects37
                        subjects37 = []
                        for s in tmp38:
                            matcher.add_subject(s)
                        for pattern_index, subst3 in matcher.match(tmp38, subst2):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 41009
                                if len(subjects12) == 0:
                                    pass
                                    # State 41010
                                    if len(subjects) == 0:
                                        pass
                                        # 1: log(c*(d*(e + f*x + g*x**2)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f210) and (cons_f52) and (cons_f4) and (cons_f1201) and (cons_f40)
                            if pattern_index == 1:
                                pass
                                # State 44966
                                if len(subjects12) == 0:
                                    pass
                                    # State 44967
                                    if len(subjects) == 0:
                                        pass
                                        # 2: log(c*(d*v**p)**q) /; (cons_f8) and (cons_f29) and (cons_f5) and (cons_f52) and (cons_f554) and (cons_f1202)
                        subjects12.appendleft(tmp36)
                if len(subjects12) >= 1 and isinstance(subjects12[0], Pow):
                    tmp39 = subjects12.popleft()
                    subjects40 = deque(tmp39._args)
                    # State 41011
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.2.2.0', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 41012
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.2.2.2', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 41013
                            if len(subjects40) >= 1 and isinstance(subjects40[0], Add):
                                tmp43 = subjects40.popleft()
                                associative1 = tmp43
                                associative_type1 = type(tmp43)
                                subjects44 = deque(tmp43._args)
                                matcher = CommutativeMatcher41015.get()
                                tmp45 = subjects44
                                subjects44 = []
                                for s in tmp45:
                                    matcher.add_subject(s)
                                for pattern_index, subst4 in matcher.match(tmp45, subst3):
                                    pass
                                    if pattern_index == 0:
                                        pass
                                        # State 41031
                                        subst5 = Substitution(subst4)
                                        try:
                                            subst5.try_add_variable('i2.2.1.2.2', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 41032
                                            if len(subjects40) == 0:
                                                pass
                                                # State 41033
                                                if len(subjects12) == 0:
                                                    pass
                                                    # State 41034
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 1: log(c*(d*(e + f*x + g*x**2)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f210) and (cons_f52) and (cons_f4) and (cons_f1201) and (cons_f40)
                                        if len(subjects40) >= 1:
                                            tmp47 = []
                                            tmp47.append(subjects40.popleft())
                                            while True:
                                                if len(tmp47) > 1:
                                                    tmp48 = create_operation_expression(associative1, tmp47)
                                                elif len(tmp47) == 1:
                                                    tmp48 = tmp47[0]
                                                else:
                                                    assert False, "Unreachable"
                                                subst5 = Substitution(subst4)
                                                try:
                                                    subst5.try_add_variable('i2.2.1.2.2', tmp48)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 41032
                                                    if len(subjects40) == 0:
                                                        pass
                                                        # State 41033
                                                        if len(subjects12) == 0:
                                                            pass
                                                            # State 41034
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 1: log(c*(d*(e + f*x + g*x**2)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f210) and (cons_f52) and (cons_f4) and (cons_f1201) and (cons_f40)
                                                if len(subjects40) == 0:
                                                    break
                                                tmp47.append(subjects40.popleft())
                                            subjects40.extendleft(reversed(tmp47))
                                subjects40.appendleft(tmp43)
                            if len(subjects40) >= 1:
                                tmp50 = subjects40.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.2.1.2.2.1', tmp50)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 44968
                                    subst5 = Substitution(subst4)
                                    try:
                                        subst5.try_add_variable('i2.2.1.2.2', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 44969
                                        if len(subjects40) == 0:
                                            pass
                                            # State 44970
                                            if len(subjects12) == 0:
                                                pass
                                                # State 44971
                                                if len(subjects) == 0:
                                                    pass
                                                    # 2: log(c*(d*v**p)**q) /; (cons_f8) and (cons_f29) and (cons_f5) and (cons_f52) and (cons_f554) and (cons_f1202)
                                    if len(subjects40) >= 1:
                                        tmp53 = subjects40.popleft()
                                        subst5 = Substitution(subst4)
                                        try:
                                            subst5.try_add_variable('i2.2.1.2.2', tmp53)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 44969
                                            if len(subjects40) == 0:
                                                pass
                                                # State 44970
                                                if len(subjects12) == 0:
                                                    pass
                                                    # State 44971
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 2: log(c*(d*v**p)**q) /; (cons_f8) and (cons_f29) and (cons_f5) and (cons_f52) and (cons_f554) and (cons_f1202)
                                        subjects40.appendleft(tmp53)
                                subjects40.appendleft(tmp50)
                        if len(subjects40) >= 1 and isinstance(subjects40[0], Pow):
                            tmp55 = subjects40.popleft()
                            subjects56 = deque(tmp55._args)
                            # State 41035
                            if len(subjects56) >= 1 and isinstance(subjects56[0], Add):
                                tmp57 = subjects56.popleft()
                                associative1 = tmp57
                                associative_type1 = type(tmp57)
                                subjects58 = deque(tmp57._args)
                                matcher = CommutativeMatcher41037.get()
                                tmp59 = subjects58
                                subjects58 = []
                                for s in tmp59:
                                    matcher.add_subject(s)
                                for pattern_index, subst3 in matcher.match(tmp59, subst2):
                                    pass
                                    if pattern_index == 0:
                                        pass
                                        # State 41053
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.2.1.2.2.2', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 41054
                                            if len(subjects56) == 0:
                                                pass
                                                # State 41055
                                                subst5 = Substitution(subst4)
                                                try:
                                                    subst5.try_add_variable('i2.2.1.2.2', 1)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 41056
                                                    if len(subjects40) == 0:
                                                        pass
                                                        # State 41057
                                                        if len(subjects12) == 0:
                                                            pass
                                                            # State 41058
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 1: log(c*(d*(e + f*x + g*x**2)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f210) and (cons_f52) and (cons_f4) and (cons_f1201) and (cons_f40)
                                                if len(subjects40) >= 1:
                                                    tmp62 = subjects40.popleft()
                                                    subst5 = Substitution(subst4)
                                                    try:
                                                        subst5.try_add_variable('i2.2.1.2.2', tmp62)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 41056
                                                        if len(subjects40) == 0:
                                                            pass
                                                            # State 41057
                                                            if len(subjects12) == 0:
                                                                pass
                                                                # State 41058
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 1: log(c*(d*(e + f*x + g*x**2)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f210) and (cons_f52) and (cons_f4) and (cons_f1201) and (cons_f40)
                                                    subjects40.appendleft(tmp62)
                                        if len(subjects56) >= 1:
                                            tmp64 = []
                                            tmp64.append(subjects56.popleft())
                                            while True:
                                                if len(tmp64) > 1:
                                                    tmp65 = create_operation_expression(associative1, tmp64)
                                                elif len(tmp64) == 1:
                                                    tmp65 = tmp64[0]
                                                else:
                                                    assert False, "Unreachable"
                                                subst4 = Substitution(subst3)
                                                try:
                                                    subst4.try_add_variable('i2.2.1.2.2.2', tmp65)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 41054
                                                    if len(subjects56) == 0:
                                                        pass
                                                        # State 41055
                                                        subst5 = Substitution(subst4)
                                                        try:
                                                            subst5.try_add_variable('i2.2.1.2.2', 1)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            # State 41056
                                                            if len(subjects40) == 0:
                                                                pass
                                                                # State 41057
                                                                if len(subjects12) == 0:
                                                                    pass
                                                                    # State 41058
                                                                    if len(subjects) == 0:
                                                                        pass
                                                                        # 1: log(c*(d*(e + f*x + g*x**2)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f210) and (cons_f52) and (cons_f4) and (cons_f1201) and (cons_f40)
                                                        if len(subjects40) >= 1:
                                                            tmp68 = subjects40.popleft()
                                                            subst5 = Substitution(subst4)
                                                            try:
                                                                subst5.try_add_variable('i2.2.1.2.2', tmp68)
                                                            except ValueError:
                                                                pass
                                                            else:
                                                                pass
                                                                # State 41056
                                                                if len(subjects40) == 0:
                                                                    pass
                                                                    # State 41057
                                                                    if len(subjects12) == 0:
                                                                        pass
                                                                        # State 41058
                                                                        if len(subjects) == 0:
                                                                            pass
                                                                            # 1: log(c*(d*(e + f*x + g*x**2)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f210) and (cons_f52) and (cons_f4) and (cons_f1201) and (cons_f40)
                                                            subjects40.appendleft(tmp68)
                                                if len(subjects56) == 0:
                                                    break
                                                tmp64.append(subjects56.popleft())
                                            subjects56.extendleft(reversed(tmp64))
                                subjects56.appendleft(tmp57)
                            if len(subjects56) >= 1:
                                tmp70 = subjects56.popleft()
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i2.2.1.2.2.1', tmp70)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 44972
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i2.2.1.2.2.2', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 44973
                                        if len(subjects56) == 0:
                                            pass
                                            # State 44974
                                            subst5 = Substitution(subst4)
                                            try:
                                                subst5.try_add_variable('i2.2.1.2.2', 1)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 44975
                                                if len(subjects40) == 0:
                                                    pass
                                                    # State 44976
                                                    if len(subjects12) == 0:
                                                        pass
                                                        # State 44977
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 2: log(c*(d*v**p)**q) /; (cons_f8) and (cons_f29) and (cons_f5) and (cons_f52) and (cons_f554) and (cons_f1202)
                                            if len(subjects40) >= 1:
                                                tmp74 = subjects40.popleft()
                                                subst5 = Substitution(subst4)
                                                try:
                                                    subst5.try_add_variable('i2.2.1.2.2', tmp74)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 44975
                                                    if len(subjects40) == 0:
                                                        pass
                                                        # State 44976
                                                        if len(subjects12) == 0:
                                                            pass
                                                            # State 44977
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 2: log(c*(d*v**p)**q) /; (cons_f8) and (cons_f29) and (cons_f5) and (cons_f52) and (cons_f554) and (cons_f1202)
                                                subjects40.appendleft(tmp74)
                                    if len(subjects56) >= 1:
                                        tmp76 = subjects56.popleft()
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.2.1.2.2.2', tmp76)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 44973
                                            if len(subjects56) == 0:
                                                pass
                                                # State 44974
                                                subst5 = Substitution(subst4)
                                                try:
                                                    subst5.try_add_variable('i2.2.1.2.2', 1)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 44975
                                                    if len(subjects40) == 0:
                                                        pass
                                                        # State 44976
                                                        if len(subjects12) == 0:
                                                            pass
                                                            # State 44977
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 2: log(c*(d*v**p)**q) /; (cons_f8) and (cons_f29) and (cons_f5) and (cons_f52) and (cons_f554) and (cons_f1202)
                                                if len(subjects40) >= 1:
                                                    tmp79 = subjects40.popleft()
                                                    subst5 = Substitution(subst4)
                                                    try:
                                                        subst5.try_add_variable('i2.2.1.2.2', tmp79)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 44975
                                                        if len(subjects40) == 0:
                                                            pass
                                                            # State 44976
                                                            if len(subjects12) == 0:
                                                                pass
                                                                # State 44977
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 2: log(c*(d*v**p)**q) /; (cons_f8) and (cons_f29) and (cons_f5) and (cons_f52) and (cons_f554) and (cons_f1202)
                                                    subjects40.appendleft(tmp79)
                                        subjects56.appendleft(tmp76)
                                subjects56.appendleft(tmp70)
                            subjects40.appendleft(tmp55)
                    if len(subjects40) >= 1 and isinstance(subjects40[0], Mul):
                        tmp81 = subjects40.popleft()
                        associative1 = tmp81
                        associative_type1 = type(tmp81)
                        subjects82 = deque(tmp81._args)
                        matcher = CommutativeMatcher41060.get()
                        tmp83 = subjects82
                        subjects82 = []
                        for s in tmp83:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp83, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 41101
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i2.2.1.2.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 41102
                                    if len(subjects40) == 0:
                                        pass
                                        # State 41103
                                        if len(subjects12) == 0:
                                            pass
                                            # State 41104
                                            if len(subjects) == 0:
                                                pass
                                                # 1: log(c*(d*(e + f*x + g*x**2)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f210) and (cons_f52) and (cons_f4) and (cons_f1201) and (cons_f40)
                                if len(subjects40) >= 1:
                                    tmp85 = []
                                    tmp85.append(subjects40.popleft())
                                    while True:
                                        if len(tmp85) > 1:
                                            tmp86 = create_operation_expression(associative1, tmp85)
                                        elif len(tmp85) == 1:
                                            tmp86 = tmp85[0]
                                        else:
                                            assert False, "Unreachable"
                                        subst3 = Substitution(subst2)
                                        try:
                                            subst3.try_add_variable('i2.2.1.2.2', tmp86)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 41102
                                            if len(subjects40) == 0:
                                                pass
                                                # State 41103
                                                if len(subjects12) == 0:
                                                    pass
                                                    # State 41104
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 1: log(c*(d*(e + f*x + g*x**2)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f210) and (cons_f52) and (cons_f4) and (cons_f1201) and (cons_f40)
                                        if len(subjects40) == 0:
                                            break
                                        tmp85.append(subjects40.popleft())
                                    subjects40.extendleft(reversed(tmp85))
                            if pattern_index == 1:
                                pass
                                # State 44982
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i2.2.1.2.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 44983
                                    if len(subjects40) == 0:
                                        pass
                                        # State 44984
                                        if len(subjects12) == 0:
                                            pass
                                            # State 44985
                                            if len(subjects) == 0:
                                                pass
                                                # 2: log(c*(d*v**p)**q) /; (cons_f8) and (cons_f29) and (cons_f5) and (cons_f52) and (cons_f554) and (cons_f1202)
                                if len(subjects40) >= 1:
                                    tmp89 = []
                                    tmp89.append(subjects40.popleft())
                                    while True:
                                        if len(tmp89) > 1:
                                            tmp90 = create_operation_expression(associative1, tmp89)
                                        elif len(tmp89) == 1:
                                            tmp90 = tmp89[0]
                                        else:
                                            assert False, "Unreachable"
                                        subst3 = Substitution(subst2)
                                        try:
                                            subst3.try_add_variable('i2.2.1.2.2', tmp90)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 44983
                                            if len(subjects40) == 0:
                                                pass
                                                # State 44984
                                                if len(subjects12) == 0:
                                                    pass
                                                    # State 44985
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 2: log(c*(d*v**p)**q) /; (cons_f8) and (cons_f29) and (cons_f5) and (cons_f52) and (cons_f554) and (cons_f1202)
                                        if len(subjects40) == 0:
                                            break
                                        tmp89.append(subjects40.popleft())
                                    subjects40.extendleft(reversed(tmp89))
                        subjects40.appendleft(tmp81)
                    subjects12.appendleft(tmp39)
            if len(subjects12) >= 1 and isinstance(subjects12[0], Mul):
                tmp92 = subjects12.popleft()
                associative1 = tmp92
                associative_type1 = type(tmp92)
                subjects93 = deque(tmp92._args)
                matcher = CommutativeMatcher41106.get()
                tmp94 = subjects93
                subjects93 = []
                for s in tmp94:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp94, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 41283
                        if len(subjects12) == 0:
                            pass
                            # State 41284
                            if len(subjects) == 0:
                                pass
                                # 1: log(c*(d*(e + f*x + g*x**2)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f210) and (cons_f52) and (cons_f4) and (cons_f1201) and (cons_f40)
                    if pattern_index == 1:
                        pass
                        # State 45010
                        if len(subjects12) == 0:
                            pass
                            # State 45011
                            if len(subjects) == 0:
                                pass
                                # 2: log(c*(d*v**p)**q) /; (cons_f8) and (cons_f29) and (cons_f5) and (cons_f52) and (cons_f554) and (cons_f1202)
                subjects12.appendleft(tmp92)
            subjects.appendleft(tmp11)
        if len(subjects) >= 1 and isinstance(subjects[0], asin):
            tmp95 = subjects.popleft()
            subjects96 = deque(tmp95._args)
            # State 110072
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.0_1', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 110073
                if len(subjects96) >= 1:
                    tmp98 = subjects96.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.2.0', tmp98)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 110074
                        if len(subjects96) == 0:
                            pass
                            # State 110075
                            if len(subjects) == 0:
                                pass
                                # 3: asin(x*c) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f1581)
                    subjects96.appendleft(tmp98)
            if len(subjects96) >= 1 and isinstance(subjects96[0], Mul):
                tmp100 = subjects96.popleft()
                associative1 = tmp100
                associative_type1 = type(tmp100)
                subjects101 = deque(tmp100._args)
                matcher = CommutativeMatcher110077.get()
                tmp102 = subjects101
                subjects101 = []
                for s in tmp102:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp102, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 110078
                        if len(subjects96) == 0:
                            pass
                            # State 110079
                            if len(subjects) == 0:
                                pass
                                # 3: asin(x*c) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f1581)
                subjects96.appendleft(tmp100)
            subjects.appendleft(tmp95)
        if len(subjects) >= 1 and isinstance(subjects[0], acos):
            tmp103 = subjects.popleft()
            subjects104 = deque(tmp103._args)
            # State 110169
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.0_1', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 110170
                if len(subjects104) >= 1:
                    tmp106 = subjects104.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.2.0', tmp106)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 110171
                        if len(subjects104) == 0:
                            pass
                            # State 110172
                            if len(subjects) == 0:
                                pass
                                # 4: acos(x*c) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f1581)
                    subjects104.appendleft(tmp106)
            if len(subjects104) >= 1 and isinstance(subjects104[0], Mul):
                tmp108 = subjects104.popleft()
                associative1 = tmp108
                associative_type1 = type(tmp108)
                subjects109 = deque(tmp108._args)
                matcher = CommutativeMatcher110174.get()
                tmp110 = subjects109
                subjects109 = []
                for s in tmp110:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp110, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 110175
                        if len(subjects104) == 0:
                            pass
                            # State 110176
                            if len(subjects) == 0:
                                pass
                                # 4: acos(x*c) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f1581)
                subjects104.appendleft(tmp108)
            subjects.appendleft(tmp103)
        if len(subjects) >= 1 and isinstance(subjects[0], asinh):
            tmp111 = subjects.popleft()
            subjects112 = deque(tmp111._args)
            # State 139807
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.0_1', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 139808
                if len(subjects112) >= 1:
                    tmp114 = subjects112.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.2.0', tmp114)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 139809
                        if len(subjects112) == 0:
                            pass
                            # State 139810
                            if len(subjects) == 0:
                                pass
                                # 5: asinh(x*c) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f1581)
                    subjects112.appendleft(tmp114)
            if len(subjects112) >= 1 and isinstance(subjects112[0], Mul):
                tmp116 = subjects112.popleft()
                associative1 = tmp116
                associative_type1 = type(tmp116)
                subjects117 = deque(tmp116._args)
                matcher = CommutativeMatcher139812.get()
                tmp118 = subjects117
                subjects117 = []
                for s in tmp118:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp118, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 139813
                        if len(subjects112) == 0:
                            pass
                            # State 139814
                            if len(subjects) == 0:
                                pass
                                # 5: asinh(x*c) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f1581)
                subjects112.appendleft(tmp116)
            subjects.appendleft(tmp111)
        if len(subjects) >= 1 and isinstance(subjects[0], acosh):
            tmp119 = subjects.popleft()
            subjects120 = deque(tmp119._args)
            # State 139904
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.0_1', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 139905
                if len(subjects120) >= 1:
                    tmp122 = subjects120.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.2.0', tmp122)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 139906
                        if len(subjects120) == 0:
                            pass
                            # State 139907
                            if len(subjects) == 0:
                                pass
                                # 6: acosh(x*c) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f1581)
                    subjects120.appendleft(tmp122)
            if len(subjects120) >= 1 and isinstance(subjects120[0], Mul):
                tmp124 = subjects120.popleft()
                associative1 = tmp124
                associative_type1 = type(tmp124)
                subjects125 = deque(tmp124._args)
                matcher = CommutativeMatcher139909.get()
                tmp126 = subjects125
                subjects125 = []
                for s in tmp126:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp126, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 139910
                        if len(subjects120) == 0:
                            pass
                            # State 139911
                            if len(subjects) == 0:
                                pass
                                # 6: acosh(x*c) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f1581)
                subjects120.appendleft(tmp124)
            subjects.appendleft(tmp119)
        return
        yield


from matchpy.utils import VariableWithCount
from matchpy.matching.many_to_one import CommutativeMatcher
from multiset import Multiset
from collections import deque
