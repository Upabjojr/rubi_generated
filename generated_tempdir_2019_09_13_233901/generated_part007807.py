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

class CommutativeMatcher115891(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul),
      (VariableWithCount('i2.2.1.1', 1, 1, None), Mul)
]),
    1: (1, Multiset({0: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    2: (2, Multiset({1: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    3: (3, Multiset({2: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    4: (4, Multiset({3: 1}), [
      (VariableWithCount('i2.2.1.0_2', 1, 1, S(1)), Mul)
]),
    5: (5, Multiset({4: 1}), [
      (VariableWithCount('i2.2.1.0_2', 1, 1, S(1)), Mul)
]),
    6: (6, Multiset({5: 1}), [
      (VariableWithCount('i2.2.1.0_2', 1, 1, S(1)), Mul)
]),
    7: (7, Multiset({6: 1}), [
      (VariableWithCount('i2.2.1.0_2', 1, 1, S(1)), Mul)
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
        if CommutativeMatcher115891._instance is None:
            CommutativeMatcher115891._instance = CommutativeMatcher115891()
        return CommutativeMatcher115891._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 115890
        if len(subjects) >= 1 and isinstance(subjects[0], Pow):
            tmp1 = subjects.popleft()
            subjects2 = deque(tmp1._args)
            # State 115974
            if len(subjects2) >= 1:
                tmp3 = subjects2.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.1', tmp3)
                except ValueError:
                    pass
                else:
                    pass
                    # State 115975
                    if len(subjects2) >= 1:
                        tmp5 = subjects2.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.1.2', tmp5)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 115976
                            if len(subjects2) == 0:
                                pass
                                # State 115977
                                if len(subjects) == 0:
                                    pass
                                    # 0: x**n
                        subjects2.appendleft(tmp5)
                subjects2.appendleft(tmp3)
            if len(subjects2) >= 1:
                tmp7 = subjects2.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.1.1', tmp7)
                except ValueError:
                    pass
                else:
                    pass
                    # State 116271
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.3.0', S(0))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 116272
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.3.1.0', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 116273
                            if len(subjects2) >= 1:
                                tmp11 = subjects2.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.1', tmp11)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 116274
                                    if len(subjects2) == 0:
                                        pass
                                        # State 116275
                                        if len(subjects) == 0:
                                            pass
                                            # 1: f**(x*d + c)
                                subjects2.appendleft(tmp11)
                        if len(subjects2) >= 1 and isinstance(subjects2[0], Mul):
                            tmp13 = subjects2.popleft()
                            associative1 = tmp13
                            associative_type1 = type(tmp13)
                            subjects14 = deque(tmp13._args)
                            matcher = CommutativeMatcher116277.get()
                            tmp15 = subjects14
                            subjects14 = []
                            for s in tmp15:
                                matcher.add_subject(s)
                            for pattern_index, subst3 in matcher.match(tmp15, subst2):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 116278
                                    if len(subjects2) == 0:
                                        pass
                                        # State 116279
                                        if len(subjects) == 0:
                                            pass
                                            # 1: f**(x*d + c)
                            subjects2.appendleft(tmp13)
                    if len(subjects2) >= 1 and isinstance(subjects2[0], Add):
                        tmp16 = subjects2.popleft()
                        associative1 = tmp16
                        associative_type1 = type(tmp16)
                        subjects17 = deque(tmp16._args)
                        matcher = CommutativeMatcher116281.get()
                        tmp18 = subjects17
                        subjects17 = []
                        for s in tmp18:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp18, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 116287
                                if len(subjects2) == 0:
                                    pass
                                    # State 116288
                                    if len(subjects) == 0:
                                        pass
                                        # 1: f**(x*d + c)
                        subjects2.appendleft(tmp16)
                    if len(subjects2) >= 1 and subjects2[0] == 1/2:
                        tmp19 = subjects2.popleft()
                        # State 117519
                        if len(subjects2) == 0:
                            pass
                            # State 117520
                            if len(subjects) == 0:
                                pass
                                # 2: sqrt(w)
                        subjects2.appendleft(tmp19)
                subjects2.appendleft(tmp7)
            if len(subjects2) >= 1 and isinstance(subjects2[0], tan):
                tmp20 = subjects2.popleft()
                subjects21 = deque(tmp20._args)
                # State 118242
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.1.3.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 118243
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.3.1.0', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 118244
                        if len(subjects21) >= 1:
                            tmp24 = subjects21.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.0', tmp24)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 118245
                                if len(subjects21) == 0:
                                    pass
                                    # State 118246
                                    if len(subjects2) >= 1 and subjects2[0] == -1:
                                        tmp26 = subjects2.popleft()
                                        # State 118247
                                        if len(subjects2) == 0:
                                            pass
                                            # State 118248
                                            if len(subjects) == 0:
                                                pass
                                                # 4: 1/tan(x*e + d)
                                        subjects2.appendleft(tmp26)
                            subjects21.appendleft(tmp24)
                    if len(subjects21) >= 1 and isinstance(subjects21[0], Mul):
                        tmp27 = subjects21.popleft()
                        associative1 = tmp27
                        associative_type1 = type(tmp27)
                        subjects28 = deque(tmp27._args)
                        matcher = CommutativeMatcher118250.get()
                        tmp29 = subjects28
                        subjects28 = []
                        for s in tmp29:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp29, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 118251
                                if len(subjects21) == 0:
                                    pass
                                    # State 118252
                                    if len(subjects2) >= 1 and subjects2[0] == -1:
                                        tmp30 = subjects2.popleft()
                                        # State 118253
                                        if len(subjects2) == 0:
                                            pass
                                            # State 118254
                                            if len(subjects) == 0:
                                                pass
                                                # 4: 1/tan(x*e + d)
                                        subjects2.appendleft(tmp30)
                        subjects21.appendleft(tmp27)
                if len(subjects21) >= 1 and isinstance(subjects21[0], Add):
                    tmp31 = subjects21.popleft()
                    associative1 = tmp31
                    associative_type1 = type(tmp31)
                    subjects32 = deque(tmp31._args)
                    matcher = CommutativeMatcher118256.get()
                    tmp33 = subjects32
                    subjects32 = []
                    for s in tmp33:
                        matcher.add_subject(s)
                    for pattern_index, subst1 in matcher.match(tmp33, subst0):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 118262
                            if len(subjects21) == 0:
                                pass
                                # State 118263
                                if len(subjects2) >= 1 and subjects2[0] == -1:
                                    tmp34 = subjects2.popleft()
                                    # State 118264
                                    if len(subjects2) == 0:
                                        pass
                                        # State 118265
                                        if len(subjects) == 0:
                                            pass
                                            # 4: 1/tan(x*e + d)
                                    subjects2.appendleft(tmp34)
                    subjects21.appendleft(tmp31)
                subjects2.appendleft(tmp20)
            if len(subjects2) >= 1 and isinstance(subjects2[0], tanh):
                tmp35 = subjects2.popleft()
                subjects36 = deque(tmp35._args)
                # State 119293
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.1.3.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 119294
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.3.1.0', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 119295
                        if len(subjects36) >= 1:
                            tmp39 = subjects36.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.0', tmp39)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 119296
                                if len(subjects36) == 0:
                                    pass
                                    # State 119297
                                    if len(subjects2) >= 1 and subjects2[0] == -1:
                                        tmp41 = subjects2.popleft()
                                        # State 119298
                                        if len(subjects2) == 0:
                                            pass
                                            # State 119299
                                            if len(subjects) == 0:
                                                pass
                                                # 6: 1/tanh(x*b + a)
                                        subjects2.appendleft(tmp41)
                            subjects36.appendleft(tmp39)
                    if len(subjects36) >= 1 and isinstance(subjects36[0], Mul):
                        tmp42 = subjects36.popleft()
                        associative1 = tmp42
                        associative_type1 = type(tmp42)
                        subjects43 = deque(tmp42._args)
                        matcher = CommutativeMatcher119301.get()
                        tmp44 = subjects43
                        subjects43 = []
                        for s in tmp44:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp44, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 119302
                                if len(subjects36) == 0:
                                    pass
                                    # State 119303
                                    if len(subjects2) >= 1 and subjects2[0] == -1:
                                        tmp45 = subjects2.popleft()
                                        # State 119304
                                        if len(subjects2) == 0:
                                            pass
                                            # State 119305
                                            if len(subjects) == 0:
                                                pass
                                                # 6: 1/tanh(x*b + a)
                                        subjects2.appendleft(tmp45)
                        subjects36.appendleft(tmp42)
                if len(subjects36) >= 1 and isinstance(subjects36[0], Add):
                    tmp46 = subjects36.popleft()
                    associative1 = tmp46
                    associative_type1 = type(tmp46)
                    subjects47 = deque(tmp46._args)
                    matcher = CommutativeMatcher119307.get()
                    tmp48 = subjects47
                    subjects47 = []
                    for s in tmp48:
                        matcher.add_subject(s)
                    for pattern_index, subst1 in matcher.match(tmp48, subst0):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 119313
                            if len(subjects36) == 0:
                                pass
                                # State 119314
                                if len(subjects2) >= 1 and subjects2[0] == -1:
                                    tmp49 = subjects2.popleft()
                                    # State 119315
                                    if len(subjects2) == 0:
                                        pass
                                        # State 119316
                                        if len(subjects) == 0:
                                            pass
                                            # 6: 1/tanh(x*b + a)
                                    subjects2.appendleft(tmp49)
                    subjects36.appendleft(tmp46)
                subjects2.appendleft(tmp35)
            subjects.appendleft(tmp1)
        if len(subjects) >= 1 and isinstance(subjects[0], tan):
            tmp50 = subjects.popleft()
            subjects51 = deque(tmp50._args)
            # State 118050
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 118051
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.1.0', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 118052
                    if len(subjects51) >= 1:
                        tmp54 = subjects51.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.0', tmp54)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 118053
                            if len(subjects51) == 0:
                                pass
                                # State 118054
                                if len(subjects) == 0:
                                    pass
                                    # 3: tan(x*f + e)
                        subjects51.appendleft(tmp54)
                if len(subjects51) >= 1 and isinstance(subjects51[0], Mul):
                    tmp56 = subjects51.popleft()
                    associative1 = tmp56
                    associative_type1 = type(tmp56)
                    subjects57 = deque(tmp56._args)
                    matcher = CommutativeMatcher118056.get()
                    tmp58 = subjects57
                    subjects57 = []
                    for s in tmp58:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp58, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 118057
                            if len(subjects51) == 0:
                                pass
                                # State 118058
                                if len(subjects) == 0:
                                    pass
                                    # 3: tan(x*f + e)
                    subjects51.appendleft(tmp56)
            if len(subjects51) >= 1 and isinstance(subjects51[0], Add):
                tmp59 = subjects51.popleft()
                associative1 = tmp59
                associative_type1 = type(tmp59)
                subjects60 = deque(tmp59._args)
                matcher = CommutativeMatcher118060.get()
                tmp61 = subjects60
                subjects60 = []
                for s in tmp61:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp61, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 118066
                        if len(subjects51) == 0:
                            pass
                            # State 118067
                            if len(subjects) == 0:
                                pass
                                # 3: tan(x*f + e)
                subjects51.appendleft(tmp59)
            subjects.appendleft(tmp50)
        if len(subjects) >= 1 and isinstance(subjects[0], tanh):
            tmp62 = subjects.popleft()
            subjects63 = deque(tmp62._args)
            # State 119109
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 119110
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.1.0', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 119111
                    if len(subjects63) >= 1:
                        tmp66 = subjects63.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.0', tmp66)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 119112
                            if len(subjects63) == 0:
                                pass
                                # State 119113
                                if len(subjects) == 0:
                                    pass
                                    # 5: tanh(x*b + a)
                        subjects63.appendleft(tmp66)
                if len(subjects63) >= 1 and isinstance(subjects63[0], Mul):
                    tmp68 = subjects63.popleft()
                    associative1 = tmp68
                    associative_type1 = type(tmp68)
                    subjects69 = deque(tmp68._args)
                    matcher = CommutativeMatcher119115.get()
                    tmp70 = subjects69
                    subjects69 = []
                    for s in tmp70:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp70, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 119116
                            if len(subjects63) == 0:
                                pass
                                # State 119117
                                if len(subjects) == 0:
                                    pass
                                    # 5: tanh(x*b + a)
                    subjects63.appendleft(tmp68)
            if len(subjects63) >= 1 and isinstance(subjects63[0], Add):
                tmp71 = subjects63.popleft()
                associative1 = tmp71
                associative_type1 = type(tmp71)
                subjects72 = deque(tmp71._args)
                matcher = CommutativeMatcher119119.get()
                tmp73 = subjects72
                subjects72 = []
                for s in tmp73:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp73, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 119125
                        if len(subjects63) == 0:
                            pass
                            # State 119126
                            if len(subjects) == 0:
                                pass
                                # 5: tanh(x*b + a)
                subjects63.appendleft(tmp71)
            subjects.appendleft(tmp62)
        return
        yield


from matchpy.utils import VariableWithCount
from matchpy.matching.many_to_one import CommutativeMatcher
from multiset import Multiset
from collections import deque
