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

class CommutativeMatcher18323(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({0: 1}), [
      (VariableWithCount('i3.0', 1, 1, None), Add)
]),
    1: (1, Multiset({1: 1, 2: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    2: (2, Multiset({3: 1, 4: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
])
}
    subjects = {}
    subjects_by_id = {}
    bipartite = BipartiteGraph()
    associative = Add
    max_optional_count = 1
    anonymous_patterns = set()

    def __init__(self):
        self.add_subject(None)

    @staticmethod
    def get():
        if CommutativeMatcher18323._instance is None:
            CommutativeMatcher18323._instance = CommutativeMatcher18323()
        return CommutativeMatcher18323._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 18322
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i3.1.0', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 18324
            subst2 = Substitution(subst1)
            try:
                subst2.try_add_variable('i3.1.4', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 18325
                if len(subjects) >= 1 and isinstance(subjects[0], Pow):
                    tmp3 = subjects.popleft()
                    subjects4 = deque(tmp3._args)
                    # State 18326
                    if len(subjects4) >= 1:
                        tmp5 = subjects4.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i3.1.2', tmp5)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 18327
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i3.1.4.0', S(1))
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 18328
                                subst5 = Substitution(subst4)
                                try:
                                    subst5.try_add_variable('i3.1.4.1.0', S(0))
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 18329
                                    subst6 = Substitution(subst5)
                                    try:
                                        subst6.try_add_variable('i3.1.4.1.1.0_1', S(1))
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 18330
                                        if len(subjects4) >= 1:
                                            tmp10 = subjects4.popleft()
                                            subst7 = Substitution(subst6)
                                            try:
                                                subst7.try_add_variable('i3.1.4.1.1.0', tmp10)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 18331
                                                if len(subjects4) == 0:
                                                    pass
                                                    # State 18332
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 0: b*(F**(e*(c + x*d)))**n /; (cons_f1101) and (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4)
                                            subjects4.appendleft(tmp10)
                                    if len(subjects4) >= 1 and isinstance(subjects4[0], Mul):
                                        tmp12 = subjects4.popleft()
                                        associative1 = tmp12
                                        associative_type1 = type(tmp12)
                                        subjects13 = deque(tmp12._args)
                                        matcher = CommutativeMatcher18334.get()
                                        tmp14 = subjects13
                                        subjects13 = []
                                        for s in tmp14:
                                            matcher.add_subject(s)
                                        for pattern_index, subst6 in matcher.match(tmp14, subst5):
                                            pass
                                            if pattern_index == 0:
                                                pass
                                                # State 18335
                                                if len(subjects4) == 0:
                                                    pass
                                                    # State 18336
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 0: b*(F**(e*(c + x*d)))**n /; (cons_f1101) and (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4)
                                        subjects4.appendleft(tmp12)
                                if len(subjects4) >= 1 and isinstance(subjects4[0], Add):
                                    tmp15 = subjects4.popleft()
                                    associative1 = tmp15
                                    associative_type1 = type(tmp15)
                                    subjects16 = deque(tmp15._args)
                                    matcher = CommutativeMatcher18338.get()
                                    tmp17 = subjects16
                                    subjects16 = []
                                    for s in tmp17:
                                        matcher.add_subject(s)
                                    for pattern_index, subst5 in matcher.match(tmp17, subst4):
                                        pass
                                        if pattern_index == 0:
                                            pass
                                            # State 18344
                                            if len(subjects4) == 0:
                                                pass
                                                # State 18345
                                                if len(subjects) == 0:
                                                    pass
                                                    # 0: b*(F**(e*(c + x*d)))**n /; (cons_f1101) and (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4)
                                    subjects4.appendleft(tmp15)
                            if len(subjects4) >= 1 and isinstance(subjects4[0], Mul):
                                tmp18 = subjects4.popleft()
                                associative1 = tmp18
                                associative_type1 = type(tmp18)
                                subjects19 = deque(tmp18._args)
                                matcher = CommutativeMatcher18347.get()
                                tmp20 = subjects19
                                subjects19 = []
                                for s in tmp20:
                                    matcher.add_subject(s)
                                for pattern_index, subst4 in matcher.match(tmp20, subst3):
                                    pass
                                    if pattern_index == 0:
                                        pass
                                        # State 18362
                                        if len(subjects4) == 0:
                                            pass
                                            # State 18363
                                            if len(subjects) == 0:
                                                pass
                                                # 0: b*(F**(e*(c + x*d)))**n /; (cons_f1101) and (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4)
                                subjects4.appendleft(tmp18)
                        subjects4.appendleft(tmp5)
                    subjects.appendleft(tmp3)
            if len(subjects) >= 1 and isinstance(subjects[0], Pow):
                tmp21 = subjects.popleft()
                subjects22 = deque(tmp21._args)
                # State 18364
                if len(subjects22) >= 1 and isinstance(subjects22[0], Pow):
                    tmp23 = subjects22.popleft()
                    subjects24 = deque(tmp23._args)
                    # State 18365
                    if len(subjects24) >= 1:
                        tmp25 = subjects24.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i3.1.2', tmp25)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 18366
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i3.1.4.0', S(1))
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 18367
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i3.1.4.1.0', S(0))
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 18368
                                    subst5 = Substitution(subst4)
                                    try:
                                        subst5.try_add_variable('i3.1.4.1.1.0_1', S(1))
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 18369
                                        if len(subjects24) >= 1:
                                            tmp30 = subjects24.popleft()
                                            subst6 = Substitution(subst5)
                                            try:
                                                subst6.try_add_variable('i3.1.4.1.1.0', tmp30)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 18370
                                                if len(subjects24) == 0:
                                                    pass
                                                    # State 18371
                                                    subst7 = Substitution(subst6)
                                                    try:
                                                        subst7.try_add_variable('i3.1.4', 1)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 18372
                                                        if len(subjects22) == 0:
                                                            pass
                                                            # State 18373
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 0: b*(F**(e*(c + x*d)))**n /; (cons_f1101) and (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4)
                                                    if len(subjects22) >= 1:
                                                        tmp33 = subjects22.popleft()
                                                        subst7 = Substitution(subst6)
                                                        try:
                                                            subst7.try_add_variable('i3.1.4', tmp33)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            # State 18372
                                                            if len(subjects22) == 0:
                                                                pass
                                                                # State 18373
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 0: b*(F**(e*(c + x*d)))**n /; (cons_f1101) and (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4)
                                                        subjects22.appendleft(tmp33)
                                            subjects24.appendleft(tmp30)
                                    if len(subjects24) >= 1 and isinstance(subjects24[0], Mul):
                                        tmp35 = subjects24.popleft()
                                        associative1 = tmp35
                                        associative_type1 = type(tmp35)
                                        subjects36 = deque(tmp35._args)
                                        matcher = CommutativeMatcher18375.get()
                                        tmp37 = subjects36
                                        subjects36 = []
                                        for s in tmp37:
                                            matcher.add_subject(s)
                                        for pattern_index, subst5 in matcher.match(tmp37, subst4):
                                            pass
                                            if pattern_index == 0:
                                                pass
                                                # State 18376
                                                if len(subjects24) == 0:
                                                    pass
                                                    # State 18377
                                                    subst6 = Substitution(subst5)
                                                    try:
                                                        subst6.try_add_variable('i3.1.4', 1)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 18378
                                                        if len(subjects22) == 0:
                                                            pass
                                                            # State 18379
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 0: b*(F**(e*(c + x*d)))**n /; (cons_f1101) and (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4)
                                                    if len(subjects22) >= 1:
                                                        tmp39 = subjects22.popleft()
                                                        subst6 = Substitution(subst5)
                                                        try:
                                                            subst6.try_add_variable('i3.1.4', tmp39)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            # State 18378
                                                            if len(subjects22) == 0:
                                                                pass
                                                                # State 18379
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 0: b*(F**(e*(c + x*d)))**n /; (cons_f1101) and (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4)
                                                        subjects22.appendleft(tmp39)
                                        subjects24.appendleft(tmp35)
                                if len(subjects24) >= 1 and isinstance(subjects24[0], Add):
                                    tmp41 = subjects24.popleft()
                                    associative1 = tmp41
                                    associative_type1 = type(tmp41)
                                    subjects42 = deque(tmp41._args)
                                    matcher = CommutativeMatcher18381.get()
                                    tmp43 = subjects42
                                    subjects42 = []
                                    for s in tmp43:
                                        matcher.add_subject(s)
                                    for pattern_index, subst4 in matcher.match(tmp43, subst3):
                                        pass
                                        if pattern_index == 0:
                                            pass
                                            # State 18387
                                            if len(subjects24) == 0:
                                                pass
                                                # State 18388
                                                subst5 = Substitution(subst4)
                                                try:
                                                    subst5.try_add_variable('i3.1.4', 1)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 18389
                                                    if len(subjects22) == 0:
                                                        pass
                                                        # State 18390
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 0: b*(F**(e*(c + x*d)))**n /; (cons_f1101) and (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4)
                                                if len(subjects22) >= 1:
                                                    tmp45 = subjects22.popleft()
                                                    subst5 = Substitution(subst4)
                                                    try:
                                                        subst5.try_add_variable('i3.1.4', tmp45)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 18389
                                                        if len(subjects22) == 0:
                                                            pass
                                                            # State 18390
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 0: b*(F**(e*(c + x*d)))**n /; (cons_f1101) and (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4)
                                                    subjects22.appendleft(tmp45)
                                    subjects24.appendleft(tmp41)
                            if len(subjects24) >= 1 and isinstance(subjects24[0], Mul):
                                tmp47 = subjects24.popleft()
                                associative1 = tmp47
                                associative_type1 = type(tmp47)
                                subjects48 = deque(tmp47._args)
                                matcher = CommutativeMatcher18392.get()
                                tmp49 = subjects48
                                subjects48 = []
                                for s in tmp49:
                                    matcher.add_subject(s)
                                for pattern_index, subst3 in matcher.match(tmp49, subst2):
                                    pass
                                    if pattern_index == 0:
                                        pass
                                        # State 18407
                                        if len(subjects24) == 0:
                                            pass
                                            # State 18408
                                            subst4 = Substitution(subst3)
                                            try:
                                                subst4.try_add_variable('i3.1.4', 1)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 18409
                                                if len(subjects22) == 0:
                                                    pass
                                                    # State 18410
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 0: b*(F**(e*(c + x*d)))**n /; (cons_f1101) and (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4)
                                            if len(subjects22) >= 1:
                                                tmp51 = subjects22.popleft()
                                                subst4 = Substitution(subst3)
                                                try:
                                                    subst4.try_add_variable('i3.1.4', tmp51)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 18409
                                                    if len(subjects22) == 0:
                                                        pass
                                                        # State 18410
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 0: b*(F**(e*(c + x*d)))**n /; (cons_f1101) and (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4)
                                                subjects22.appendleft(tmp51)
                                subjects24.appendleft(tmp47)
                        subjects24.appendleft(tmp25)
                    subjects22.appendleft(tmp23)
                if len(subjects22) >= 1 and isinstance(subjects22[0], Add):
                    tmp53 = subjects22.popleft()
                    associative1 = tmp53
                    associative_type1 = type(tmp53)
                    subjects54 = deque(tmp53._args)
                    matcher = CommutativeMatcher53559.get()
                    tmp55 = subjects54
                    subjects54 = []
                    for s in tmp55:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp55, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 53575
                            if len(subjects22) >= 1 and subjects22[0] == 1/2:
                                tmp56 = subjects22.popleft()
                                # State 53576
                                if len(subjects22) == 0:
                                    pass
                                    # State 53577
                                    if len(subjects) == 0:
                                        pass
                                        # 1: f*sqrt(a + b*x + c*x**2) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f1057)
                                subjects22.appendleft(tmp56)
                        if pattern_index == 1:
                            pass
                            # State 53623
                            if len(subjects22) >= 1 and subjects22[0] == 1/2:
                                tmp57 = subjects22.popleft()
                                # State 53624
                                if len(subjects22) == 0:
                                    pass
                                    # State 53625
                                    if len(subjects) == 0:
                                        pass
                                        # 3: f*sqrt(a + c*x**2) /; (cons_f2) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f1057)
                                subjects22.appendleft(tmp57)
                    subjects22.appendleft(tmp53)
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i3.1.2.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 53606
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i3.1.2.1.0', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 53607
                        if len(subjects22) >= 1 and isinstance(subjects22[0], Pow):
                            tmp60 = subjects22.popleft()
                            subjects61 = deque(tmp60._args)
                            # State 53608
                            if len(subjects61) >= 1:
                                tmp62 = subjects61.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i3.1.2.1.1', tmp62)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 53609
                                    if len(subjects61) >= 1 and subjects61[0] == 2:
                                        tmp64 = subjects61.popleft()
                                        # State 53610
                                        if len(subjects61) == 0:
                                            pass
                                            # State 53611
                                            if len(subjects22) >= 1 and subjects22[0] == 1/2:
                                                tmp65 = subjects22.popleft()
                                                # State 53612
                                                if len(subjects22) == 0:
                                                    pass
                                                    # State 53613
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 3: f*sqrt(a + c*x**2) /; (cons_f2) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f1057)
                                                subjects22.appendleft(tmp65)
                                        subjects61.appendleft(tmp64)
                                subjects61.appendleft(tmp62)
                            subjects22.appendleft(tmp60)
                    if len(subjects22) >= 1 and isinstance(subjects22[0], Mul):
                        tmp66 = subjects22.popleft()
                        associative1 = tmp66
                        associative_type1 = type(tmp66)
                        subjects67 = deque(tmp66._args)
                        matcher = CommutativeMatcher53615.get()
                        tmp68 = subjects67
                        subjects67 = []
                        for s in tmp68:
                            matcher.add_subject(s)
                        for pattern_index, subst3 in matcher.match(tmp68, subst2):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 53620
                                if len(subjects22) >= 1 and subjects22[0] == 1/2:
                                    tmp69 = subjects22.popleft()
                                    # State 53621
                                    if len(subjects22) == 0:
                                        pass
                                        # State 53622
                                        if len(subjects) == 0:
                                            pass
                                            # 3: f*sqrt(a + c*x**2) /; (cons_f2) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f1057)
                                    subjects22.appendleft(tmp69)
                        subjects22.appendleft(tmp66)
                subjects.appendleft(tmp21)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i3.1.0_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 53599
            if len(subjects) >= 1:
                tmp71 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i3.1.2.1.1', tmp71)
                except ValueError:
                    pass
                else:
                    pass
                    # State 53600
                    if len(subjects) == 0:
                        pass
                        # 2: e*x /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f1057)
                        # 4: e*x /; (cons_f2) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f1057)
                subjects.appendleft(tmp71)
        if len(subjects) >= 1 and isinstance(subjects[0], Mul):
            tmp73 = subjects.popleft()
            associative1 = tmp73
            associative_type1 = type(tmp73)
            subjects74 = deque(tmp73._args)
            matcher = CommutativeMatcher18412.get()
            tmp75 = subjects74
            subjects74 = []
            for s in tmp75:
                matcher.add_subject(s)
            for pattern_index, subst1 in matcher.match(tmp75, subst0):
                pass
                if pattern_index == 0:
                    pass
                    # State 18499
                    if len(subjects) == 0:
                        pass
                        # 0: b*(F**(e*(c + x*d)))**n /; (cons_f1101) and (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4)
                if pattern_index == 1:
                    pass
                    # State 53598
                    if len(subjects) == 0:
                        pass
                        # 1: f*sqrt(a + b*x + c*x**2) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f1057)
                if pattern_index == 2:
                    pass
                    # State 53601
                    if len(subjects) == 0:
                        pass
                        # 2: e*x /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f1057)
                        # 4: e*x /; (cons_f2) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f1057)
                if pattern_index == 3:
                    pass
                    # State 53646
                    if len(subjects) == 0:
                        pass
                        # 3: f*sqrt(a + c*x**2) /; (cons_f2) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f1057)
            subjects.appendleft(tmp73)
        return
        yield


from matchpy.utils import VariableWithCount
from matchpy.matching.many_to_one import CommutativeMatcher
from multiset import Multiset
from collections import deque
