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


class CommutativeMatcher115887(CommutativeMatcher):
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
        if CommutativeMatcher115887._instance is None:
            CommutativeMatcher115887._instance = CommutativeMatcher115887()
        return CommutativeMatcher115887._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 115886
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.0_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 115888
            if len(subjects) >= 1:
                tmp2 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.1', tmp2)
                except ValueError:
                    pass
                else:
                    pass
                    # State 115889
                    if len(subjects) == 0:
                        pass
                        # 0: d*x
                        yield 0, subst2
                subjects.appendleft(tmp2)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.0', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 115969
            if len(subjects) >= 1 and isinstance(subjects[0], Pow):
                tmp5 = subjects.popleft()
                subjects6 = deque(tmp5._args)
                # State 115970
                if len(subjects6) >= 1:
                    tmp7 = subjects6.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.1', tmp7)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 115971
                        if len(subjects6) >= 1:
                            tmp9 = subjects6.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.2', tmp9)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 115972
                                if len(subjects6) == 0:
                                    pass
                                    # State 115973
                                    if len(subjects) == 0:
                                        pass
                                        # 1: x**n*b
                                        yield 1, subst3
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
                        # State 116253
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.3.0', S(0))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 116254
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i2.2.1.3.1.0', S(1))
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 116255
                                if len(subjects6) >= 1:
                                    tmp15 = subjects6.popleft()
                                    subst5 = Substitution(subst4)
                                    try:
                                        subst5.try_add_variable('i2.1', tmp15)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 116256
                                        if len(subjects6) == 0:
                                            pass
                                            # State 116257
                                            if len(subjects) == 0:
                                                pass
                                                # 2: b*f**(x*d + c)
                                                yield 2, subst5
                                    subjects6.appendleft(tmp15)
                            if len(subjects6) >= 1 and isinstance(subjects6[0], Mul):
                                tmp17 = subjects6.popleft()
                                associative1 = tmp17
                                associative_type1 = type(tmp17)
                                subjects18 = deque(tmp17._args)
                                matcher = CommutativeMatcher116259.get()
                                tmp19 = subjects18
                                subjects18 = []
                                for s in tmp19:
                                    matcher.add_subject(s)
                                for pattern_index, subst4 in matcher.match(tmp19, subst3):
                                    pass
                                    if pattern_index == 0:
                                        pass
                                        # State 116260
                                        if len(subjects6) == 0:
                                            pass
                                            # State 116261
                                            if len(subjects) == 0:
                                                pass
                                                # 2: b*f**(x*d + c)
                                                yield 2, subst4
                                subjects6.appendleft(tmp17)
                        if len(subjects6) >= 1 and isinstance(subjects6[0], Add):
                            tmp20 = subjects6.popleft()
                            associative1 = tmp20
                            associative_type1 = type(tmp20)
                            subjects21 = deque(tmp20._args)
                            matcher = CommutativeMatcher116263.get()
                            tmp22 = subjects21
                            subjects21 = []
                            for s in tmp22:
                                matcher.add_subject(s)
                            for pattern_index, subst3 in matcher.match(tmp22, subst2):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 116269
                                    if len(subjects6) == 0:
                                        pass
                                        # State 116270
                                        if len(subjects) == 0:
                                            pass
                                            # 2: b*f**(x*d + c)
                                            yield 2, subst3
                            subjects6.appendleft(tmp20)
                        if len(subjects6) >= 1 and subjects6[0] == Rational(1, 2):
                            tmp23 = subjects6.popleft()
                            # State 117517
                            if len(subjects6) == 0:
                                pass
                                # State 117518
                                if len(subjects) == 0:
                                    pass
                                    # 3: s*sqrt(w)
                                    yield 3, subst2
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
            # State 118031
            if len(subjects) >= 1 and isinstance(subjects[0], tan):
                tmp25 = subjects.popleft()
                subjects26 = deque(tmp25._args)
                # State 118032
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 118033
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.2.1.2.1.0', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 118034
                        if len(subjects26) >= 1:
                            tmp29 = subjects26.popleft()
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i2.2.1.0', tmp29)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 118035
                                if len(subjects26) == 0:
                                    pass
                                    # State 118036
                                    if len(subjects) == 0:
                                        pass
                                        # 4: d*tan(x*f + e)
                                        yield 4, subst4
                            subjects26.appendleft(tmp29)
                    if len(subjects26) >= 1 and isinstance(subjects26[0], Mul):
                        tmp31 = subjects26.popleft()
                        associative1 = tmp31
                        associative_type1 = type(tmp31)
                        subjects32 = deque(tmp31._args)
                        matcher = CommutativeMatcher118038.get()
                        tmp33 = subjects32
                        subjects32 = []
                        for s in tmp33:
                            matcher.add_subject(s)
                        for pattern_index, subst3 in matcher.match(tmp33, subst2):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 118039
                                if len(subjects26) == 0:
                                    pass
                                    # State 118040
                                    if len(subjects) == 0:
                                        pass
                                        # 4: d*tan(x*f + e)
                                        yield 4, subst3
                        subjects26.appendleft(tmp31)
                if len(subjects26) >= 1 and isinstance(subjects26[0], Add):
                    tmp34 = subjects26.popleft()
                    associative1 = tmp34
                    associative_type1 = type(tmp34)
                    subjects35 = deque(tmp34._args)
                    matcher = CommutativeMatcher118042.get()
                    tmp36 = subjects35
                    subjects35 = []
                    for s in tmp36:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp36, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 118048
                            if len(subjects26) == 0:
                                pass
                                # State 118049
                                if len(subjects) == 0:
                                    pass
                                    # 4: d*tan(x*f + e)
                                    yield 4, subst2
                    subjects26.appendleft(tmp34)
                subjects.appendleft(tmp25)
            if len(subjects) >= 1 and isinstance(subjects[0], Pow):
                tmp37 = subjects.popleft()
                subjects38 = deque(tmp37._args)
                # State 118217
                if len(subjects38) >= 1 and isinstance(subjects38[0], tan):
                    tmp39 = subjects38.popleft()
                    subjects40 = deque(tmp39._args)
                    # State 118218
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.3.0', S(0))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 118219
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.3.1.0', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 118220
                            if len(subjects40) >= 1:
                                tmp43 = subjects40.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.2.1.0', tmp43)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 118221
                                    if len(subjects40) == 0:
                                        pass
                                        # State 118222
                                        if len(subjects38) >= 1 and subjects38[0] == Integer(-1):
                                            tmp45 = subjects38.popleft()
                                            # State 118223
                                            if len(subjects38) == 0:
                                                pass
                                                # State 118224
                                                if len(subjects) == 0:
                                                    pass
                                                    # 5: d/tan(x*e + d)
                                                    yield 5, subst4
                                            subjects38.appendleft(tmp45)
                                subjects40.appendleft(tmp43)
                        if len(subjects40) >= 1 and isinstance(subjects40[0], Mul):
                            tmp46 = subjects40.popleft()
                            associative1 = tmp46
                            associative_type1 = type(tmp46)
                            subjects47 = deque(tmp46._args)
                            matcher = CommutativeMatcher118226.get()
                            tmp48 = subjects47
                            subjects47 = []
                            for s in tmp48:
                                matcher.add_subject(s)
                            for pattern_index, subst3 in matcher.match(tmp48, subst2):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 118227
                                    if len(subjects40) == 0:
                                        pass
                                        # State 118228
                                        if len(subjects38) >= 1 and subjects38[0] == Integer(-1):
                                            tmp49 = subjects38.popleft()
                                            # State 118229
                                            if len(subjects38) == 0:
                                                pass
                                                # State 118230
                                                if len(subjects) == 0:
                                                    pass
                                                    # 5: d/tan(x*e + d)
                                                    yield 5, subst3
                                            subjects38.appendleft(tmp49)
                            subjects40.appendleft(tmp46)
                    if len(subjects40) >= 1 and isinstance(subjects40[0], Add):
                        tmp50 = subjects40.popleft()
                        associative1 = tmp50
                        associative_type1 = type(tmp50)
                        subjects51 = deque(tmp50._args)
                        matcher = CommutativeMatcher118232.get()
                        tmp52 = subjects51
                        subjects51 = []
                        for s in tmp52:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp52, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 118238
                                if len(subjects40) == 0:
                                    pass
                                    # State 118239
                                    if len(subjects38) >= 1 and subjects38[0] == Integer(-1):
                                        tmp53 = subjects38.popleft()
                                        # State 118240
                                        if len(subjects38) == 0:
                                            pass
                                            # State 118241
                                            if len(subjects) == 0:
                                                pass
                                                # 5: d/tan(x*e + d)
                                                yield 5, subst2
                                        subjects38.appendleft(tmp53)
                        subjects40.appendleft(tmp50)
                    subjects38.appendleft(tmp39)
                if len(subjects38) >= 1 and isinstance(subjects38[0], tanh):
                    tmp54 = subjects38.popleft()
                    subjects55 = deque(tmp54._args)
                    # State 119269
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.3.0', S(0))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 119270
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.3.1.0', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 119271
                            if len(subjects55) >= 1:
                                tmp58 = subjects55.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.2.1.0', tmp58)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 119272
                                    if len(subjects55) == 0:
                                        pass
                                        # State 119273
                                        if len(subjects38) >= 1 and subjects38[0] == Integer(-1):
                                            tmp60 = subjects38.popleft()
                                            # State 119274
                                            if len(subjects38) == 0:
                                                pass
                                                # State 119275
                                                if len(subjects) == 0:
                                                    pass
                                                    # 7: d/tanh(x*b + a)
                                                    yield 7, subst4
                                            subjects38.appendleft(tmp60)
                                subjects55.appendleft(tmp58)
                        if len(subjects55) >= 1 and isinstance(subjects55[0], Mul):
                            tmp61 = subjects55.popleft()
                            associative1 = tmp61
                            associative_type1 = type(tmp61)
                            subjects62 = deque(tmp61._args)
                            matcher = CommutativeMatcher119277.get()
                            tmp63 = subjects62
                            subjects62 = []
                            for s in tmp63:
                                matcher.add_subject(s)
                            for pattern_index, subst3 in matcher.match(tmp63, subst2):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 119278
                                    if len(subjects55) == 0:
                                        pass
                                        # State 119279
                                        if len(subjects38) >= 1 and subjects38[0] == Integer(-1):
                                            tmp64 = subjects38.popleft()
                                            # State 119280
                                            if len(subjects38) == 0:
                                                pass
                                                # State 119281
                                                if len(subjects) == 0:
                                                    pass
                                                    # 7: d/tanh(x*b + a)
                                                    yield 7, subst3
                                            subjects38.appendleft(tmp64)
                            subjects55.appendleft(tmp61)
                    if len(subjects55) >= 1 and isinstance(subjects55[0], Add):
                        tmp65 = subjects55.popleft()
                        associative1 = tmp65
                        associative_type1 = type(tmp65)
                        subjects66 = deque(tmp65._args)
                        matcher = CommutativeMatcher119283.get()
                        tmp67 = subjects66
                        subjects66 = []
                        for s in tmp67:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp67, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 119289
                                if len(subjects55) == 0:
                                    pass
                                    # State 119290
                                    if len(subjects38) >= 1 and subjects38[0] == Integer(-1):
                                        tmp68 = subjects38.popleft()
                                        # State 119291
                                        if len(subjects38) == 0:
                                            pass
                                            # State 119292
                                            if len(subjects) == 0:
                                                pass
                                                # 7: d/tanh(x*b + a)
                                                yield 7, subst2
                                        subjects38.appendleft(tmp68)
                        subjects55.appendleft(tmp65)
                    subjects38.appendleft(tmp54)
                subjects.appendleft(tmp37)
            if len(subjects) >= 1 and isinstance(subjects[0], tanh):
                tmp69 = subjects.popleft()
                subjects70 = deque(tmp69._args)
                # State 119091
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 119092
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.2.1.2.1.0', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 119093
                        if len(subjects70) >= 1:
                            tmp73 = subjects70.popleft()
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i2.2.1.0', tmp73)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 119094
                                if len(subjects70) == 0:
                                    pass
                                    # State 119095
                                    if len(subjects) == 0:
                                        pass
                                        # 6: d*tanh(x*b + a)
                                        yield 6, subst4
                            subjects70.appendleft(tmp73)
                    if len(subjects70) >= 1 and isinstance(subjects70[0], Mul):
                        tmp75 = subjects70.popleft()
                        associative1 = tmp75
                        associative_type1 = type(tmp75)
                        subjects76 = deque(tmp75._args)
                        matcher = CommutativeMatcher119097.get()
                        tmp77 = subjects76
                        subjects76 = []
                        for s in tmp77:
                            matcher.add_subject(s)
                        for pattern_index, subst3 in matcher.match(tmp77, subst2):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 119098
                                if len(subjects70) == 0:
                                    pass
                                    # State 119099
                                    if len(subjects) == 0:
                                        pass
                                        # 6: d*tanh(x*b + a)
                                        yield 6, subst3
                        subjects70.appendleft(tmp75)
                if len(subjects70) >= 1 and isinstance(subjects70[0], Add):
                    tmp78 = subjects70.popleft()
                    associative1 = tmp78
                    associative_type1 = type(tmp78)
                    subjects79 = deque(tmp78._args)
                    matcher = CommutativeMatcher119101.get()
                    tmp80 = subjects79
                    subjects79 = []
                    for s in tmp80:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp80, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 119107
                            if len(subjects70) == 0:
                                pass
                                # State 119108
                                if len(subjects) == 0:
                                    pass
                                    # 6: d*tanh(x*b + a)
                                    yield 6, subst2
                    subjects70.appendleft(tmp78)
                subjects.appendleft(tmp69)
        if len(subjects) >= 1 and isinstance(subjects[0], Mul):
            tmp81 = subjects.popleft()
            associative1 = tmp81
            associative_type1 = type(tmp81)
            subjects82 = deque(tmp81._args)
            matcher = CommutativeMatcher115891.get()
            tmp83 = subjects82
            subjects82 = []
            for s in tmp83:
                matcher.add_subject(s)
            for pattern_index, subst1 in matcher.match(tmp83, subst0):
                pass
                if pattern_index == 0:
                    pass
                    # State 115892
                    if len(subjects) == 0:
                        pass
                        # 0: d*x
                        yield 0, subst1
                if pattern_index == 1:
                    pass
                    # State 115978
                    if len(subjects) == 0:
                        pass
                        # 1: x**n*b
                        yield 1, subst1
                if pattern_index == 2:
                    pass
                    # State 116289
                    if len(subjects) == 0:
                        pass
                        # 2: b*f**(x*d + c)
                        yield 2, subst1
                if pattern_index == 3:
                    pass
                    # State 117521
                    if len(subjects) == 0:
                        pass
                        # 3: s*sqrt(w)
                        yield 3, subst1
                if pattern_index == 4:
                    pass
                    # State 118068
                    if len(subjects) == 0:
                        pass
                        # 4: d*tan(x*f + e)
                        yield 4, subst1
                if pattern_index == 5:
                    pass
                    # State 118266
                    if len(subjects) == 0:
                        pass
                        # 5: d/tan(x*e + d)
                        yield 5, subst1
                if pattern_index == 6:
                    pass
                    # State 119127
                    if len(subjects) == 0:
                        pass
                        # 6: d*tanh(x*b + a)
                        yield 6, subst1
                if pattern_index == 7:
                    pass
                    # State 119317
                    if len(subjects) == 0:
                        pass
                        # 7: d/tanh(x*b + a)
                        yield 7, subst1
            subjects.appendleft(tmp81)
        return
        yield


from .generated_part007804 import *
from .generated_part007795 import *
from .generated_part007802 import *
from .generated_part007807 import *
from .generated_part007792 import *
from matchpy.matching.many_to_one import CommutativeMatcher
from .generated_part007798 import *
from .generated_part007793 import *
from .generated_part007799 import *
from .generated_part007801 import *
from collections import deque
from .generated_part007796 import *
from matchpy.utils import VariableWithCount
from multiset import Multiset
from .generated_part007805 import *