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

class CommutativeMatcher145118(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({0: 1}), [
      (VariableWithCount('i2.2.0_1', 1, 1, None), Add)
]),
    1: (1, Multiset({1: 1}), [
      (VariableWithCount('i2.2.0', 1, 1, S(0)), Add)
]),
    2: (2, Multiset({2: 1}), [
      (VariableWithCount('i2.2.0', 1, 1, None), Add)
]),
    3: (3, Multiset({3: 1}), [
      (VariableWithCount('i2.2.0', 1, 1, S(0)), Add)
]),
    4: (4, Multiset({4: 1}), [
      (VariableWithCount('i2.2.0_1', 1, 1, S(0)), Add)
]),
    5: (5, Multiset({5: 1}), [
      (VariableWithCount('i2.2.0_1', 1, 1, S(0)), Add)
]),
    6: (6, Multiset({6: 1}), [
      (VariableWithCount('i2.2.0_1', 1, 1, S(0)), Add)
]),
    7: (7, Multiset({7: 1}), [
      (VariableWithCount('i2.2.0_1', 1, 1, S(0)), Add)
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
        if CommutativeMatcher145118._instance is None:
            CommutativeMatcher145118._instance = CommutativeMatcher145118()
        return CommutativeMatcher145118._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 145117
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.0_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 145119
            if len(subjects) >= 1:
                tmp2 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.1', tmp2)
                except ValueError:
                    pass
                else:
                    pass
                    # State 145120
                    if len(subjects) == 0:
                        pass
                        # 0: g*x
                subjects.appendleft(tmp2)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.0', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 145232
            subst2 = Substitution(subst1)
            try:
                subst2.try_add_variable('i2.2.1.2', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 145233
                if len(subjects) >= 1:
                    tmp6 = subjects.popleft()
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.1', tmp6)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 145234
                        if len(subjects) == 0:
                            pass
                            # 1: x**n*b
                    subjects.appendleft(tmp6)
            if len(subjects) >= 1 and isinstance(subjects[0], Pow):
                tmp8 = subjects.popleft()
                subjects9 = deque(tmp8._args)
                # State 145235
                if len(subjects9) >= 1:
                    tmp10 = subjects9.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.1', tmp10)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 145236
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.2', 1)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 145237
                            if len(subjects9) == 0:
                                pass
                                # State 145238
                                if len(subjects) == 0:
                                    pass
                                    # 1: x**n*b
                        if len(subjects9) >= 1:
                            tmp13 = subjects9.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.2', tmp13)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 145237
                                if len(subjects9) == 0:
                                    pass
                                    # State 145238
                                    if len(subjects) == 0:
                                        pass
                                        # 1: x**n*b
                            subjects9.appendleft(tmp13)
                        if len(subjects9) >= 1:
                            tmp15 = subjects9.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.2', tmp15)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 145261
                                if len(subjects9) == 0:
                                    pass
                                    # State 145262
                                    if len(subjects) == 0:
                                        pass
                                        # 2: x**n*b
                            subjects9.appendleft(tmp15)
                    subjects9.appendleft(tmp10)
                if len(subjects9) >= 1:
                    tmp17 = subjects9.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.1', tmp17)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 145583
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.3.0', S(0))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 145584
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i2.2.1.3.1.0', S(1))
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 145585
                                if len(subjects9) >= 1:
                                    tmp21 = subjects9.popleft()
                                    subst5 = Substitution(subst4)
                                    try:
                                        subst5.try_add_variable('i2.1', tmp21)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 145586
                                        if len(subjects9) == 0:
                                            pass
                                            # State 145587
                                            if len(subjects) == 0:
                                                pass
                                                # 3: b*f**(x*d + c)
                                    subjects9.appendleft(tmp21)
                            if len(subjects9) >= 1 and isinstance(subjects9[0], Mul):
                                tmp23 = subjects9.popleft()
                                associative1 = tmp23
                                associative_type1 = type(tmp23)
                                subjects24 = deque(tmp23._args)
                                matcher = CommutativeMatcher145589.get()
                                tmp25 = subjects24
                                subjects24 = []
                                for s in tmp25:
                                    matcher.add_subject(s)
                                for pattern_index, subst4 in matcher.match(tmp25, subst3):
                                    pass
                                    if pattern_index == 0:
                                        pass
                                        # State 145590
                                        if len(subjects9) == 0:
                                            pass
                                            # State 145591
                                            if len(subjects) == 0:
                                                pass
                                                # 3: b*f**(x*d + c)
                                subjects9.appendleft(tmp23)
                        if len(subjects9) >= 1 and isinstance(subjects9[0], Add):
                            tmp26 = subjects9.popleft()
                            associative1 = tmp26
                            associative_type1 = type(tmp26)
                            subjects27 = deque(tmp26._args)
                            matcher = CommutativeMatcher145593.get()
                            tmp28 = subjects27
                            subjects27 = []
                            for s in tmp28:
                                matcher.add_subject(s)
                            for pattern_index, subst3 in matcher.match(tmp28, subst2):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 145599
                                    if len(subjects9) == 0:
                                        pass
                                        # State 145600
                                        if len(subjects) == 0:
                                            pass
                                            # 3: b*f**(x*d + c)
                            subjects9.appendleft(tmp26)
                    subjects9.appendleft(tmp17)
                subjects.appendleft(tmp8)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.0_2', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 147314
            if len(subjects) >= 1 and isinstance(subjects[0], tanh):
                tmp30 = subjects.popleft()
                subjects31 = deque(tmp30._args)
                # State 147315
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 147316
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.2.1.2.1.0', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 147317
                        if len(subjects31) >= 1:
                            tmp34 = subjects31.popleft()
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i2.2.1.0', tmp34)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 147318
                                if len(subjects31) == 0:
                                    pass
                                    # State 147319
                                    if len(subjects) == 0:
                                        pass
                                        # 4: d*tanh(x*b + a)
                            subjects31.appendleft(tmp34)
                    if len(subjects31) >= 1 and isinstance(subjects31[0], Mul):
                        tmp36 = subjects31.popleft()
                        associative1 = tmp36
                        associative_type1 = type(tmp36)
                        subjects37 = deque(tmp36._args)
                        matcher = CommutativeMatcher147321.get()
                        tmp38 = subjects37
                        subjects37 = []
                        for s in tmp38:
                            matcher.add_subject(s)
                        for pattern_index, subst3 in matcher.match(tmp38, subst2):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 147322
                                if len(subjects31) == 0:
                                    pass
                                    # State 147323
                                    if len(subjects) == 0:
                                        pass
                                        # 4: d*tanh(x*b + a)
                        subjects31.appendleft(tmp36)
                if len(subjects31) >= 1 and isinstance(subjects31[0], Add):
                    tmp39 = subjects31.popleft()
                    associative1 = tmp39
                    associative_type1 = type(tmp39)
                    subjects40 = deque(tmp39._args)
                    matcher = CommutativeMatcher147325.get()
                    tmp41 = subjects40
                    subjects40 = []
                    for s in tmp41:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp41, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 147331
                            if len(subjects31) == 0:
                                pass
                                # State 147332
                                if len(subjects) == 0:
                                    pass
                                    # 4: d*tanh(x*b + a)
                    subjects31.appendleft(tmp39)
                subjects.appendleft(tmp30)
            if len(subjects) >= 1 and isinstance(subjects[0], Pow):
                tmp42 = subjects.popleft()
                subjects43 = deque(tmp42._args)
                # State 147522
                if len(subjects43) >= 1 and isinstance(subjects43[0], tanh):
                    tmp44 = subjects43.popleft()
                    subjects45 = deque(tmp44._args)
                    # State 147523
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.3.0', S(0))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 147524
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.3.1.0', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 147525
                            if len(subjects45) >= 1:
                                tmp48 = subjects45.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.2.1.0', tmp48)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 147526
                                    if len(subjects45) == 0:
                                        pass
                                        # State 147527
                                        if len(subjects43) >= 1 and subjects43[0] == -1:
                                            tmp50 = subjects43.popleft()
                                            # State 147528
                                            if len(subjects43) == 0:
                                                pass
                                                # State 147529
                                                if len(subjects) == 0:
                                                    pass
                                                    # 5: d/tanh(x*b + a)
                                            subjects43.appendleft(tmp50)
                                subjects45.appendleft(tmp48)
                        if len(subjects45) >= 1 and isinstance(subjects45[0], Mul):
                            tmp51 = subjects45.popleft()
                            associative1 = tmp51
                            associative_type1 = type(tmp51)
                            subjects52 = deque(tmp51._args)
                            matcher = CommutativeMatcher147531.get()
                            tmp53 = subjects52
                            subjects52 = []
                            for s in tmp53:
                                matcher.add_subject(s)
                            for pattern_index, subst3 in matcher.match(tmp53, subst2):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 147532
                                    if len(subjects45) == 0:
                                        pass
                                        # State 147533
                                        if len(subjects43) >= 1 and subjects43[0] == -1:
                                            tmp54 = subjects43.popleft()
                                            # State 147534
                                            if len(subjects43) == 0:
                                                pass
                                                # State 147535
                                                if len(subjects) == 0:
                                                    pass
                                                    # 5: d/tanh(x*b + a)
                                            subjects43.appendleft(tmp54)
                            subjects45.appendleft(tmp51)
                    if len(subjects45) >= 1 and isinstance(subjects45[0], Add):
                        tmp55 = subjects45.popleft()
                        associative1 = tmp55
                        associative_type1 = type(tmp55)
                        subjects56 = deque(tmp55._args)
                        matcher = CommutativeMatcher147537.get()
                        tmp57 = subjects56
                        subjects56 = []
                        for s in tmp57:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp57, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 147543
                                if len(subjects45) == 0:
                                    pass
                                    # State 147544
                                    if len(subjects43) >= 1 and subjects43[0] == -1:
                                        tmp58 = subjects43.popleft()
                                        # State 147545
                                        if len(subjects43) == 0:
                                            pass
                                            # State 147546
                                            if len(subjects) == 0:
                                                pass
                                                # 5: d/tanh(x*b + a)
                                        subjects43.appendleft(tmp58)
                        subjects45.appendleft(tmp55)
                    subjects43.appendleft(tmp44)
                if len(subjects43) >= 1 and isinstance(subjects43[0], tan):
                    tmp59 = subjects43.popleft()
                    subjects60 = deque(tmp59._args)
                    # State 148571
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.3.0', S(0))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 148572
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.3.1.0', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 148573
                            if len(subjects60) >= 1:
                                tmp63 = subjects60.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.2.1.0', tmp63)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 148574
                                    if len(subjects60) == 0:
                                        pass
                                        # State 148575
                                        if len(subjects43) >= 1 and subjects43[0] == -1:
                                            tmp65 = subjects43.popleft()
                                            # State 148576
                                            if len(subjects43) == 0:
                                                pass
                                                # State 148577
                                                if len(subjects) == 0:
                                                    pass
                                                    # 7: d/tan(x*e + d)
                                            subjects43.appendleft(tmp65)
                                subjects60.appendleft(tmp63)
                        if len(subjects60) >= 1 and isinstance(subjects60[0], Mul):
                            tmp66 = subjects60.popleft()
                            associative1 = tmp66
                            associative_type1 = type(tmp66)
                            subjects67 = deque(tmp66._args)
                            matcher = CommutativeMatcher148579.get()
                            tmp68 = subjects67
                            subjects67 = []
                            for s in tmp68:
                                matcher.add_subject(s)
                            for pattern_index, subst3 in matcher.match(tmp68, subst2):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 148580
                                    if len(subjects60) == 0:
                                        pass
                                        # State 148581
                                        if len(subjects43) >= 1 and subjects43[0] == -1:
                                            tmp69 = subjects43.popleft()
                                            # State 148582
                                            if len(subjects43) == 0:
                                                pass
                                                # State 148583
                                                if len(subjects) == 0:
                                                    pass
                                                    # 7: d/tan(x*e + d)
                                            subjects43.appendleft(tmp69)
                            subjects60.appendleft(tmp66)
                    if len(subjects60) >= 1 and isinstance(subjects60[0], Add):
                        tmp70 = subjects60.popleft()
                        associative1 = tmp70
                        associative_type1 = type(tmp70)
                        subjects71 = deque(tmp70._args)
                        matcher = CommutativeMatcher148585.get()
                        tmp72 = subjects71
                        subjects71 = []
                        for s in tmp72:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp72, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 148591
                                if len(subjects60) == 0:
                                    pass
                                    # State 148592
                                    if len(subjects43) >= 1 and subjects43[0] == -1:
                                        tmp73 = subjects43.popleft()
                                        # State 148593
                                        if len(subjects43) == 0:
                                            pass
                                            # State 148594
                                            if len(subjects) == 0:
                                                pass
                                                # 7: d/tan(x*e + d)
                                        subjects43.appendleft(tmp73)
                        subjects60.appendleft(tmp70)
                    subjects43.appendleft(tmp59)
                subjects.appendleft(tmp42)
            if len(subjects) >= 1 and isinstance(subjects[0], tan):
                tmp74 = subjects.popleft()
                subjects75 = deque(tmp74._args)
                # State 148369
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 148370
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.2.1.2.1.0', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 148371
                        if len(subjects75) >= 1:
                            tmp78 = subjects75.popleft()
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i2.2.1.0', tmp78)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 148372
                                if len(subjects75) == 0:
                                    pass
                                    # State 148373
                                    if len(subjects) == 0:
                                        pass
                                        # 6: d*tan(x*f + e)
                            subjects75.appendleft(tmp78)
                    if len(subjects75) >= 1 and isinstance(subjects75[0], Mul):
                        tmp80 = subjects75.popleft()
                        associative1 = tmp80
                        associative_type1 = type(tmp80)
                        subjects81 = deque(tmp80._args)
                        matcher = CommutativeMatcher148375.get()
                        tmp82 = subjects81
                        subjects81 = []
                        for s in tmp82:
                            matcher.add_subject(s)
                        for pattern_index, subst3 in matcher.match(tmp82, subst2):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 148376
                                if len(subjects75) == 0:
                                    pass
                                    # State 148377
                                    if len(subjects) == 0:
                                        pass
                                        # 6: d*tan(x*f + e)
                        subjects75.appendleft(tmp80)
                if len(subjects75) >= 1 and isinstance(subjects75[0], Add):
                    tmp83 = subjects75.popleft()
                    associative1 = tmp83
                    associative_type1 = type(tmp83)
                    subjects84 = deque(tmp83._args)
                    matcher = CommutativeMatcher148379.get()
                    tmp85 = subjects84
                    subjects84 = []
                    for s in tmp85:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp85, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 148385
                            if len(subjects75) == 0:
                                pass
                                # State 148386
                                if len(subjects) == 0:
                                    pass
                                    # 6: d*tan(x*f + e)
                    subjects75.appendleft(tmp83)
                subjects.appendleft(tmp74)
        if len(subjects) >= 1 and isinstance(subjects[0], Mul):
            tmp86 = subjects.popleft()
            associative1 = tmp86
            associative_type1 = type(tmp86)
            subjects87 = deque(tmp86._args)
            matcher = CommutativeMatcher145122.get()
            tmp88 = subjects87
            subjects87 = []
            for s in tmp88:
                matcher.add_subject(s)
            for pattern_index, subst1 in matcher.match(tmp88, subst0):
                pass
                if pattern_index == 0:
                    pass
                    # State 145123
                    if len(subjects) == 0:
                        pass
                        # 0: g*x
                if pattern_index == 1:
                    pass
                    # State 145245
                    if len(subjects) == 0:
                        pass
                        # 1: x**n*b
                if pattern_index == 2:
                    pass
                    # State 145265
                    if len(subjects) == 0:
                        pass
                        # 2: x**n*b
                if pattern_index == 3:
                    pass
                    # State 145619
                    if len(subjects) == 0:
                        pass
                        # 3: b*f**(x*d + c)
                if pattern_index == 4:
                    pass
                    # State 147351
                    if len(subjects) == 0:
                        pass
                        # 4: d*tanh(x*b + a)
                if pattern_index == 5:
                    pass
                    # State 147571
                    if len(subjects) == 0:
                        pass
                        # 5: d/tanh(x*b + a)
                if pattern_index == 6:
                    pass
                    # State 148405
                    if len(subjects) == 0:
                        pass
                        # 6: d*tan(x*f + e)
                if pattern_index == 7:
                    pass
                    # State 148619
                    if len(subjects) == 0:
                        pass
                        # 7: d/tan(x*e + d)
            subjects.appendleft(tmp86)
        return
        yield


from matchpy.utils import VariableWithCount
from matchpy.matching.many_to_one import CommutativeMatcher
from multiset import Multiset
from collections import deque
