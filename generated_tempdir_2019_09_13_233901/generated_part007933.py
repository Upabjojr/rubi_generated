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

class CommutativeMatcher145106(CommutativeMatcher):
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
        if CommutativeMatcher145106._instance is None:
            CommutativeMatcher145106._instance = CommutativeMatcher145106()
        return CommutativeMatcher145106._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 145105
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.0_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 145107
            if len(subjects) >= 1:
                tmp2 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.1', tmp2)
                except ValueError:
                    pass
                else:
                    pass
                    # State 145108
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
            # State 145193
            subst2 = Substitution(subst1)
            try:
                subst2.try_add_variable('i2.2.1.2', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 145194
                if len(subjects) >= 1:
                    tmp6 = subjects.popleft()
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.1', tmp6)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 145195
                        if len(subjects) == 0:
                            pass
                            # 1: x**n*b
                    subjects.appendleft(tmp6)
            if len(subjects) >= 1 and isinstance(subjects[0], Pow):
                tmp8 = subjects.popleft()
                subjects9 = deque(tmp8._args)
                # State 145196
                if len(subjects9) >= 1:
                    tmp10 = subjects9.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.1', tmp10)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 145197
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.2', 1)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 145198
                            if len(subjects9) == 0:
                                pass
                                # State 145199
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
                                # State 145198
                                if len(subjects9) == 0:
                                    pass
                                    # State 145199
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
                                # State 145251
                                if len(subjects9) == 0:
                                    pass
                                    # State 145252
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
                        # State 145500
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.3.0', S(0))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 145501
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i2.2.1.3.1.0', S(1))
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 145502
                                if len(subjects9) >= 1:
                                    tmp21 = subjects9.popleft()
                                    subst5 = Substitution(subst4)
                                    try:
                                        subst5.try_add_variable('i2.1', tmp21)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 145503
                                        if len(subjects9) == 0:
                                            pass
                                            # State 145504
                                            if len(subjects) == 0:
                                                pass
                                                # 3: b*f**(x*d + c)
                                    subjects9.appendleft(tmp21)
                            if len(subjects9) >= 1 and isinstance(subjects9[0], Mul):
                                tmp23 = subjects9.popleft()
                                associative1 = tmp23
                                associative_type1 = type(tmp23)
                                subjects24 = deque(tmp23._args)
                                matcher = CommutativeMatcher145506.get()
                                tmp25 = subjects24
                                subjects24 = []
                                for s in tmp25:
                                    matcher.add_subject(s)
                                for pattern_index, subst4 in matcher.match(tmp25, subst3):
                                    pass
                                    if pattern_index == 0:
                                        pass
                                        # State 145507
                                        if len(subjects9) == 0:
                                            pass
                                            # State 145508
                                            if len(subjects) == 0:
                                                pass
                                                # 3: b*f**(x*d + c)
                                subjects9.appendleft(tmp23)
                        if len(subjects9) >= 1 and isinstance(subjects9[0], Add):
                            tmp26 = subjects9.popleft()
                            associative1 = tmp26
                            associative_type1 = type(tmp26)
                            subjects27 = deque(tmp26._args)
                            matcher = CommutativeMatcher145510.get()
                            tmp28 = subjects27
                            subjects27 = []
                            for s in tmp28:
                                matcher.add_subject(s)
                            for pattern_index, subst3 in matcher.match(tmp28, subst2):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 145516
                                    if len(subjects9) == 0:
                                        pass
                                        # State 145517
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
            # State 147226
            if len(subjects) >= 1 and isinstance(subjects[0], tanh):
                tmp30 = subjects.popleft()
                subjects31 = deque(tmp30._args)
                # State 147227
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 147228
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.2.1.2.1.0', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 147229
                        if len(subjects31) >= 1:
                            tmp34 = subjects31.popleft()
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i2.2.1.0', tmp34)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 147230
                                if len(subjects31) == 0:
                                    pass
                                    # State 147231
                                    if len(subjects) == 0:
                                        pass
                                        # 4: d*tanh(x*b + a)
                            subjects31.appendleft(tmp34)
                    if len(subjects31) >= 1 and isinstance(subjects31[0], Mul):
                        tmp36 = subjects31.popleft()
                        associative1 = tmp36
                        associative_type1 = type(tmp36)
                        subjects37 = deque(tmp36._args)
                        matcher = CommutativeMatcher147233.get()
                        tmp38 = subjects37
                        subjects37 = []
                        for s in tmp38:
                            matcher.add_subject(s)
                        for pattern_index, subst3 in matcher.match(tmp38, subst2):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 147234
                                if len(subjects31) == 0:
                                    pass
                                    # State 147235
                                    if len(subjects) == 0:
                                        pass
                                        # 4: d*tanh(x*b + a)
                        subjects31.appendleft(tmp36)
                if len(subjects31) >= 1 and isinstance(subjects31[0], Add):
                    tmp39 = subjects31.popleft()
                    associative1 = tmp39
                    associative_type1 = type(tmp39)
                    subjects40 = deque(tmp39._args)
                    matcher = CommutativeMatcher147237.get()
                    tmp41 = subjects40
                    subjects40 = []
                    for s in tmp41:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp41, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 147243
                            if len(subjects31) == 0:
                                pass
                                # State 147244
                                if len(subjects) == 0:
                                    pass
                                    # 4: d*tanh(x*b + a)
                    subjects31.appendleft(tmp39)
                subjects.appendleft(tmp30)
            if len(subjects) >= 1 and isinstance(subjects[0], Pow):
                tmp42 = subjects.popleft()
                subjects43 = deque(tmp42._args)
                # State 147412
                if len(subjects43) >= 1 and isinstance(subjects43[0], tanh):
                    tmp44 = subjects43.popleft()
                    subjects45 = deque(tmp44._args)
                    # State 147413
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.3.0', S(0))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 147414
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.3.1.0', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 147415
                            if len(subjects45) >= 1:
                                tmp48 = subjects45.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.2.1.0', tmp48)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 147416
                                    if len(subjects45) == 0:
                                        pass
                                        # State 147417
                                        if len(subjects43) >= 1 and subjects43[0] == -1:
                                            tmp50 = subjects43.popleft()
                                            # State 147418
                                            if len(subjects43) == 0:
                                                pass
                                                # State 147419
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
                            matcher = CommutativeMatcher147421.get()
                            tmp53 = subjects52
                            subjects52 = []
                            for s in tmp53:
                                matcher.add_subject(s)
                            for pattern_index, subst3 in matcher.match(tmp53, subst2):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 147422
                                    if len(subjects45) == 0:
                                        pass
                                        # State 147423
                                        if len(subjects43) >= 1 and subjects43[0] == -1:
                                            tmp54 = subjects43.popleft()
                                            # State 147424
                                            if len(subjects43) == 0:
                                                pass
                                                # State 147425
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
                        matcher = CommutativeMatcher147427.get()
                        tmp57 = subjects56
                        subjects56 = []
                        for s in tmp57:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp57, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 147433
                                if len(subjects45) == 0:
                                    pass
                                    # State 147434
                                    if len(subjects43) >= 1 and subjects43[0] == -1:
                                        tmp58 = subjects43.popleft()
                                        # State 147435
                                        if len(subjects43) == 0:
                                            pass
                                            # State 147436
                                            if len(subjects) == 0:
                                                pass
                                                # 5: d/tanh(x*b + a)
                                        subjects43.appendleft(tmp58)
                        subjects45.appendleft(tmp55)
                    subjects43.appendleft(tmp44)
                if len(subjects43) >= 1 and isinstance(subjects43[0], tan):
                    tmp59 = subjects43.popleft()
                    subjects60 = deque(tmp59._args)
                    # State 148464
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.3.0', S(0))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 148465
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.3.1.0', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 148466
                            if len(subjects60) >= 1:
                                tmp63 = subjects60.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.2.1.0', tmp63)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 148467
                                    if len(subjects60) == 0:
                                        pass
                                        # State 148468
                                        if len(subjects43) >= 1 and subjects43[0] == -1:
                                            tmp65 = subjects43.popleft()
                                            # State 148469
                                            if len(subjects43) == 0:
                                                pass
                                                # State 148470
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
                            matcher = CommutativeMatcher148472.get()
                            tmp68 = subjects67
                            subjects67 = []
                            for s in tmp68:
                                matcher.add_subject(s)
                            for pattern_index, subst3 in matcher.match(tmp68, subst2):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 148473
                                    if len(subjects60) == 0:
                                        pass
                                        # State 148474
                                        if len(subjects43) >= 1 and subjects43[0] == -1:
                                            tmp69 = subjects43.popleft()
                                            # State 148475
                                            if len(subjects43) == 0:
                                                pass
                                                # State 148476
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
                        matcher = CommutativeMatcher148478.get()
                        tmp72 = subjects71
                        subjects71 = []
                        for s in tmp72:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp72, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 148484
                                if len(subjects60) == 0:
                                    pass
                                    # State 148485
                                    if len(subjects43) >= 1 and subjects43[0] == -1:
                                        tmp73 = subjects43.popleft()
                                        # State 148486
                                        if len(subjects43) == 0:
                                            pass
                                            # State 148487
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
                # State 148286
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 148287
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.2.1.2.1.0', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 148288
                        if len(subjects75) >= 1:
                            tmp78 = subjects75.popleft()
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i2.2.1.0', tmp78)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 148289
                                if len(subjects75) == 0:
                                    pass
                                    # State 148290
                                    if len(subjects) == 0:
                                        pass
                                        # 6: d*tan(x*f + e)
                            subjects75.appendleft(tmp78)
                    if len(subjects75) >= 1 and isinstance(subjects75[0], Mul):
                        tmp80 = subjects75.popleft()
                        associative1 = tmp80
                        associative_type1 = type(tmp80)
                        subjects81 = deque(tmp80._args)
                        matcher = CommutativeMatcher148292.get()
                        tmp82 = subjects81
                        subjects81 = []
                        for s in tmp82:
                            matcher.add_subject(s)
                        for pattern_index, subst3 in matcher.match(tmp82, subst2):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 148293
                                if len(subjects75) == 0:
                                    pass
                                    # State 148294
                                    if len(subjects) == 0:
                                        pass
                                        # 6: d*tan(x*f + e)
                        subjects75.appendleft(tmp80)
                if len(subjects75) >= 1 and isinstance(subjects75[0], Add):
                    tmp83 = subjects75.popleft()
                    associative1 = tmp83
                    associative_type1 = type(tmp83)
                    subjects84 = deque(tmp83._args)
                    matcher = CommutativeMatcher148296.get()
                    tmp85 = subjects84
                    subjects84 = []
                    for s in tmp85:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp85, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 148302
                            if len(subjects75) == 0:
                                pass
                                # State 148303
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
            matcher = CommutativeMatcher145110.get()
            tmp88 = subjects87
            subjects87 = []
            for s in tmp88:
                matcher.add_subject(s)
            for pattern_index, subst1 in matcher.match(tmp88, subst0):
                pass
                if pattern_index == 0:
                    pass
                    # State 145111
                    if len(subjects) == 0:
                        pass
                        # 0: g*x
                if pattern_index == 1:
                    pass
                    # State 145206
                    if len(subjects) == 0:
                        pass
                        # 1: x**n*b
                if pattern_index == 2:
                    pass
                    # State 145255
                    if len(subjects) == 0:
                        pass
                        # 2: x**n*b
                if pattern_index == 3:
                    pass
                    # State 145536
                    if len(subjects) == 0:
                        pass
                        # 3: b*f**(x*d + c)
                if pattern_index == 4:
                    pass
                    # State 147263
                    if len(subjects) == 0:
                        pass
                        # 4: d*tanh(x*b + a)
                if pattern_index == 5:
                    pass
                    # State 147461
                    if len(subjects) == 0:
                        pass
                        # 5: d/tanh(x*b + a)
                if pattern_index == 6:
                    pass
                    # State 148322
                    if len(subjects) == 0:
                        pass
                        # 6: d*tan(x*f + e)
                if pattern_index == 7:
                    pass
                    # State 148512
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
