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

class CommutativeMatcher115899(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({0: 1}), [
      (VariableWithCount('i2.2.0_1', 1, 1, None), Add)
]),
    1: (1, Multiset({1: 1}), [
      (VariableWithCount('i2.2.0', 1, 1, S(0)), Add)
]),
    2: (2, Multiset({1: 1}), [
      (VariableWithCount('i2.2.0', 1, 1, None), Add)
]),
    3: (3, Multiset({2: 1}), [
      (VariableWithCount('i2.2.0', 1, 1, S(0)), Add)
]),
    4: (4, Multiset({3: 1}), [
      (VariableWithCount('i2.2.0', 1, 1, None), Add)
]),
    5: (5, Multiset({4: 1}), [
      (VariableWithCount('i2.2.0_1', 1, 1, S(0)), Add)
]),
    6: (6, Multiset({5: 1}), [
      (VariableWithCount('i2.2.0_1', 1, 1, S(0)), Add)
]),
    7: (7, Multiset({6: 1}), [
      (VariableWithCount('i2.2.0_1', 1, 1, S(0)), Add)
]),
    8: (8, Multiset({7: 1}), [
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
        if CommutativeMatcher115899._instance is None:
            CommutativeMatcher115899._instance = CommutativeMatcher115899()
        return CommutativeMatcher115899._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 115898
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.0_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 115900
            if len(subjects) >= 1:
                tmp2 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.1', tmp2)
                except ValueError:
                    pass
                else:
                    pass
                    # State 115901
                    if len(subjects) == 0:
                        pass
                        # 0: d*x
                subjects.appendleft(tmp2)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.0', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 115999
            if len(subjects) >= 1 and isinstance(subjects[0], Pow):
                tmp5 = subjects.popleft()
                subjects6 = deque(tmp5._args)
                # State 116000
                if len(subjects6) >= 1:
                    tmp7 = subjects6.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.1', tmp7)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 116001
                        if len(subjects6) >= 1:
                            tmp9 = subjects6.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.2', tmp9)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 116002
                                if len(subjects6) == 0:
                                    pass
                                    # State 116003
                                    if len(subjects) == 0:
                                        pass
                                        # 1: x**n*b
                            subjects6.appendleft(tmp9)
                    subjects6.appendleft(tmp7)
                if len(subjects6) >= 1:
                    tmp11 = subjects6.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.1', tmp11)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 116336
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.3.0', S(0))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 116337
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i2.2.1.3.1.0', S(1))
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 116338
                                if len(subjects6) >= 1:
                                    tmp15 = subjects6.popleft()
                                    subst5 = Substitution(subst4)
                                    try:
                                        subst5.try_add_variable('i2.1', tmp15)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 116339
                                        if len(subjects6) == 0:
                                            pass
                                            # State 116340
                                            if len(subjects) == 0:
                                                pass
                                                # 2: b*f**(x*d + c)
                                    subjects6.appendleft(tmp15)
                            if len(subjects6) >= 1 and isinstance(subjects6[0], Mul):
                                tmp17 = subjects6.popleft()
                                associative1 = tmp17
                                associative_type1 = type(tmp17)
                                subjects18 = deque(tmp17._args)
                                matcher = CommutativeMatcher116342.get()
                                tmp19 = subjects18
                                subjects18 = []
                                for s in tmp19:
                                    matcher.add_subject(s)
                                for pattern_index, subst4 in matcher.match(tmp19, subst3):
                                    pass
                                    if pattern_index == 0:
                                        pass
                                        # State 116343
                                        if len(subjects6) == 0:
                                            pass
                                            # State 116344
                                            if len(subjects) == 0:
                                                pass
                                                # 2: b*f**(x*d + c)
                                subjects6.appendleft(tmp17)
                        if len(subjects6) >= 1 and isinstance(subjects6[0], Add):
                            tmp20 = subjects6.popleft()
                            associative1 = tmp20
                            associative_type1 = type(tmp20)
                            subjects21 = deque(tmp20._args)
                            matcher = CommutativeMatcher116346.get()
                            tmp22 = subjects21
                            subjects21 = []
                            for s in tmp22:
                                matcher.add_subject(s)
                            for pattern_index, subst3 in matcher.match(tmp22, subst2):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 116352
                                    if len(subjects6) == 0:
                                        pass
                                        # State 116353
                                        if len(subjects) == 0:
                                            pass
                                            # 2: b*f**(x*d + c)
                            subjects6.appendleft(tmp20)
                        if len(subjects6) >= 1 and subjects6[0] == 1/2:
                            tmp23 = subjects6.popleft()
                            # State 117546
                            if len(subjects6) == 0:
                                pass
                                # State 117547
                                if len(subjects) == 0:
                                    pass
                                    # 3: s*sqrt(w)
                            subjects6.appendleft(tmp23)
                    subjects6.appendleft(tmp11)
                subjects.appendleft(tmp5)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.0_2', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 118119
            if len(subjects) >= 1 and isinstance(subjects[0], tan):
                tmp25 = subjects.popleft()
                subjects26 = deque(tmp25._args)
                # State 118120
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 118121
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.2.1.2.1.0', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 118122
                        if len(subjects26) >= 1:
                            tmp29 = subjects26.popleft()
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i2.2.1.0', tmp29)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 118123
                                if len(subjects26) == 0:
                                    pass
                                    # State 118124
                                    if len(subjects) == 0:
                                        pass
                                        # 4: d*tan(x*f + e)
                            subjects26.appendleft(tmp29)
                    if len(subjects26) >= 1 and isinstance(subjects26[0], Mul):
                        tmp31 = subjects26.popleft()
                        associative1 = tmp31
                        associative_type1 = type(tmp31)
                        subjects32 = deque(tmp31._args)
                        matcher = CommutativeMatcher118126.get()
                        tmp33 = subjects32
                        subjects32 = []
                        for s in tmp33:
                            matcher.add_subject(s)
                        for pattern_index, subst3 in matcher.match(tmp33, subst2):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 118127
                                if len(subjects26) == 0:
                                    pass
                                    # State 118128
                                    if len(subjects) == 0:
                                        pass
                                        # 4: d*tan(x*f + e)
                        subjects26.appendleft(tmp31)
                if len(subjects26) >= 1 and isinstance(subjects26[0], Add):
                    tmp34 = subjects26.popleft()
                    associative1 = tmp34
                    associative_type1 = type(tmp34)
                    subjects35 = deque(tmp34._args)
                    matcher = CommutativeMatcher118130.get()
                    tmp36 = subjects35
                    subjects35 = []
                    for s in tmp36:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp36, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 118136
                            if len(subjects26) == 0:
                                pass
                                # State 118137
                                if len(subjects) == 0:
                                    pass
                                    # 4: d*tan(x*f + e)
                    subjects26.appendleft(tmp34)
                subjects.appendleft(tmp25)
            if len(subjects) >= 1 and isinstance(subjects[0], Pow):
                tmp37 = subjects.popleft()
                subjects38 = deque(tmp37._args)
                # State 118327
                if len(subjects38) >= 1 and isinstance(subjects38[0], tan):
                    tmp39 = subjects38.popleft()
                    subjects40 = deque(tmp39._args)
                    # State 118328
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.3.0', S(0))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 118329
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.3.1.0', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 118330
                            if len(subjects40) >= 1:
                                tmp43 = subjects40.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.2.1.0', tmp43)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 118331
                                    if len(subjects40) == 0:
                                        pass
                                        # State 118332
                                        if len(subjects38) >= 1 and subjects38[0] == -1:
                                            tmp45 = subjects38.popleft()
                                            # State 118333
                                            if len(subjects38) == 0:
                                                pass
                                                # State 118334
                                                if len(subjects) == 0:
                                                    pass
                                                    # 5: d/tan(x*e + d)
                                            subjects38.appendleft(tmp45)
                                subjects40.appendleft(tmp43)
                        if len(subjects40) >= 1 and isinstance(subjects40[0], Mul):
                            tmp46 = subjects40.popleft()
                            associative1 = tmp46
                            associative_type1 = type(tmp46)
                            subjects47 = deque(tmp46._args)
                            matcher = CommutativeMatcher118336.get()
                            tmp48 = subjects47
                            subjects47 = []
                            for s in tmp48:
                                matcher.add_subject(s)
                            for pattern_index, subst3 in matcher.match(tmp48, subst2):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 118337
                                    if len(subjects40) == 0:
                                        pass
                                        # State 118338
                                        if len(subjects38) >= 1 and subjects38[0] == -1:
                                            tmp49 = subjects38.popleft()
                                            # State 118339
                                            if len(subjects38) == 0:
                                                pass
                                                # State 118340
                                                if len(subjects) == 0:
                                                    pass
                                                    # 5: d/tan(x*e + d)
                                            subjects38.appendleft(tmp49)
                            subjects40.appendleft(tmp46)
                    if len(subjects40) >= 1 and isinstance(subjects40[0], Add):
                        tmp50 = subjects40.popleft()
                        associative1 = tmp50
                        associative_type1 = type(tmp50)
                        subjects51 = deque(tmp50._args)
                        matcher = CommutativeMatcher118342.get()
                        tmp52 = subjects51
                        subjects51 = []
                        for s in tmp52:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp52, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 118348
                                if len(subjects40) == 0:
                                    pass
                                    # State 118349
                                    if len(subjects38) >= 1 and subjects38[0] == -1:
                                        tmp53 = subjects38.popleft()
                                        # State 118350
                                        if len(subjects38) == 0:
                                            pass
                                            # State 118351
                                            if len(subjects) == 0:
                                                pass
                                                # 5: d/tan(x*e + d)
                                        subjects38.appendleft(tmp53)
                        subjects40.appendleft(tmp50)
                    subjects38.appendleft(tmp39)
                if len(subjects38) >= 1 and isinstance(subjects38[0], tanh):
                    tmp54 = subjects38.popleft()
                    subjects55 = deque(tmp54._args)
                    # State 119376
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.3.0', S(0))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 119377
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.3.1.0', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 119378
                            if len(subjects55) >= 1:
                                tmp58 = subjects55.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.2.1.0', tmp58)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 119379
                                    if len(subjects55) == 0:
                                        pass
                                        # State 119380
                                        if len(subjects38) >= 1 and subjects38[0] == -1:
                                            tmp60 = subjects38.popleft()
                                            # State 119381
                                            if len(subjects38) == 0:
                                                pass
                                                # State 119382
                                                if len(subjects) == 0:
                                                    pass
                                                    # 7: d/tanh(x*b + a)
                                            subjects38.appendleft(tmp60)
                                subjects55.appendleft(tmp58)
                        if len(subjects55) >= 1 and isinstance(subjects55[0], Mul):
                            tmp61 = subjects55.popleft()
                            associative1 = tmp61
                            associative_type1 = type(tmp61)
                            subjects62 = deque(tmp61._args)
                            matcher = CommutativeMatcher119384.get()
                            tmp63 = subjects62
                            subjects62 = []
                            for s in tmp63:
                                matcher.add_subject(s)
                            for pattern_index, subst3 in matcher.match(tmp63, subst2):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 119385
                                    if len(subjects55) == 0:
                                        pass
                                        # State 119386
                                        if len(subjects38) >= 1 and subjects38[0] == -1:
                                            tmp64 = subjects38.popleft()
                                            # State 119387
                                            if len(subjects38) == 0:
                                                pass
                                                # State 119388
                                                if len(subjects) == 0:
                                                    pass
                                                    # 7: d/tanh(x*b + a)
                                            subjects38.appendleft(tmp64)
                            subjects55.appendleft(tmp61)
                    if len(subjects55) >= 1 and isinstance(subjects55[0], Add):
                        tmp65 = subjects55.popleft()
                        associative1 = tmp65
                        associative_type1 = type(tmp65)
                        subjects66 = deque(tmp65._args)
                        matcher = CommutativeMatcher119390.get()
                        tmp67 = subjects66
                        subjects66 = []
                        for s in tmp67:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp67, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 119396
                                if len(subjects55) == 0:
                                    pass
                                    # State 119397
                                    if len(subjects38) >= 1 and subjects38[0] == -1:
                                        tmp68 = subjects38.popleft()
                                        # State 119398
                                        if len(subjects38) == 0:
                                            pass
                                            # State 119399
                                            if len(subjects) == 0:
                                                pass
                                                # 7: d/tanh(x*b + a)
                                        subjects38.appendleft(tmp68)
                        subjects55.appendleft(tmp65)
                    subjects38.appendleft(tmp54)
                subjects.appendleft(tmp37)
            if len(subjects) >= 1 and isinstance(subjects[0], tanh):
                tmp69 = subjects.popleft()
                subjects70 = deque(tmp69._args)
                # State 119174
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 119175
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.2.1.2.1.0', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 119176
                        if len(subjects70) >= 1:
                            tmp73 = subjects70.popleft()
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i2.2.1.0', tmp73)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 119177
                                if len(subjects70) == 0:
                                    pass
                                    # State 119178
                                    if len(subjects) == 0:
                                        pass
                                        # 6: d*tanh(x*b + a)
                            subjects70.appendleft(tmp73)
                    if len(subjects70) >= 1 and isinstance(subjects70[0], Mul):
                        tmp75 = subjects70.popleft()
                        associative1 = tmp75
                        associative_type1 = type(tmp75)
                        subjects76 = deque(tmp75._args)
                        matcher = CommutativeMatcher119180.get()
                        tmp77 = subjects76
                        subjects76 = []
                        for s in tmp77:
                            matcher.add_subject(s)
                        for pattern_index, subst3 in matcher.match(tmp77, subst2):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 119181
                                if len(subjects70) == 0:
                                    pass
                                    # State 119182
                                    if len(subjects) == 0:
                                        pass
                                        # 6: d*tanh(x*b + a)
                        subjects70.appendleft(tmp75)
                if len(subjects70) >= 1 and isinstance(subjects70[0], Add):
                    tmp78 = subjects70.popleft()
                    associative1 = tmp78
                    associative_type1 = type(tmp78)
                    subjects79 = deque(tmp78._args)
                    matcher = CommutativeMatcher119184.get()
                    tmp80 = subjects79
                    subjects79 = []
                    for s in tmp80:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp80, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 119190
                            if len(subjects70) == 0:
                                pass
                                # State 119191
                                if len(subjects) == 0:
                                    pass
                                    # 6: d*tanh(x*b + a)
                    subjects70.appendleft(tmp78)
                subjects.appendleft(tmp69)
        if len(subjects) >= 1 and isinstance(subjects[0], Mul):
            tmp81 = subjects.popleft()
            associative1 = tmp81
            associative_type1 = type(tmp81)
            subjects82 = deque(tmp81._args)
            matcher = CommutativeMatcher115903.get()
            tmp83 = subjects82
            subjects82 = []
            for s in tmp83:
                matcher.add_subject(s)
            for pattern_index, subst1 in matcher.match(tmp83, subst0):
                pass
                if pattern_index == 0:
                    pass
                    # State 115904
                    if len(subjects) == 0:
                        pass
                        # 0: d*x
                if pattern_index == 1:
                    pass
                    # State 116008
                    if len(subjects) == 0:
                        pass
                        # 1: x**n*b
                if pattern_index == 2:
                    pass
                    # State 116372
                    if len(subjects) == 0:
                        pass
                        # 2: b*f**(x*d + c)
                if pattern_index == 3:
                    pass
                    # State 117550
                    if len(subjects) == 0:
                        pass
                        # 3: s*sqrt(w)
                if pattern_index == 4:
                    pass
                    # State 118156
                    if len(subjects) == 0:
                        pass
                        # 4: d*tan(x*f + e)
                if pattern_index == 5:
                    pass
                    # State 118376
                    if len(subjects) == 0:
                        pass
                        # 5: d/tan(x*e + d)
                if pattern_index == 6:
                    pass
                    # State 119210
                    if len(subjects) == 0:
                        pass
                        # 6: d*tanh(x*b + a)
                if pattern_index == 7:
                    pass
                    # State 119424
                    if len(subjects) == 0:
                        pass
                        # 7: d/tanh(x*b + a)
            subjects.appendleft(tmp81)
        return
        yield


from matchpy.utils import VariableWithCount
from matchpy.matching.many_to_one import CommutativeMatcher
from multiset import Multiset
from collections import deque
