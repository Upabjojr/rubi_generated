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


class CommutativeMatcher18788(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({0: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(1)), Mul)
]),
    1: (1, Multiset({1: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(1)), Mul)
]),
    2: (2, Multiset({2: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(1)), Mul)
]),
    3: (3, Multiset({3: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(1)), Mul)
]),
    4: (4, Multiset({4: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(1)), Mul)
]),
    5: (5, Multiset({5: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(1)), Mul)
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
        if CommutativeMatcher18788._instance is None:
            CommutativeMatcher18788._instance = CommutativeMatcher18788()
        return CommutativeMatcher18788._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 18787
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i3.2', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 18789
            subst2 = Substitution(subst1)
            try:
                subst2.try_add_variable('i3.2.0', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 18790
                subst3 = Substitution(subst2)
                try:
                    subst3.try_add_variable('i3.2.2', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 18791
                    subst4 = Substitution(subst3)
                    try:
                        subst4.try_add_variable('i3.2.2.0', S(0))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 18792
                        subst5 = Substitution(subst4)
                        try:
                            subst5.try_add_variable('i3.2.2.1.0_1', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 18793
                            if len(subjects) >= 1:
                                tmp6 = subjects.popleft()
                                subst6 = Substitution(subst5)
                                try:
                                    subst6.try_add_variable('i3.2.2.1.0', tmp6)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 18794
                                    if len(subjects) == 0:
                                        pass
                                        # 0: (d*(e + x*f)**p)**q /; (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f1158)
                                        yield 0, subst6
                                subjects.appendleft(tmp6)
                        if len(subjects) >= 1 and isinstance(subjects[0], Mul):
                            tmp8 = subjects.popleft()
                            associative1 = tmp8
                            associative_type1 = type(tmp8)
                            subjects9 = deque(tmp8._args)
                            matcher = CommutativeMatcher18796.get()
                            tmp10 = subjects9
                            subjects9 = []
                            for s in tmp10:
                                matcher.add_subject(s)
                            for pattern_index, subst5 in matcher.match(tmp10, subst4):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 18797
                                    if len(subjects) == 0:
                                        pass
                                        # 0: (d*(e + x*f)**p)**q /; (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f1158)
                                        yield 0, subst5
                            subjects.appendleft(tmp8)
                    if len(subjects) >= 1 and isinstance(subjects[0], Add):
                        tmp11 = subjects.popleft()
                        associative1 = tmp11
                        associative_type1 = type(tmp11)
                        subjects12 = deque(tmp11._args)
                        matcher = CommutativeMatcher18799.get()
                        tmp13 = subjects12
                        subjects12 = []
                        for s in tmp13:
                            matcher.add_subject(s)
                        for pattern_index, subst4 in matcher.match(tmp13, subst3):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 18805
                                if len(subjects) == 0:
                                    pass
                                    # 0: (d*(e + x*f)**p)**q /; (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f1158)
                                    yield 0, subst4
                        subjects.appendleft(tmp11)
                if len(subjects) >= 1 and isinstance(subjects[0], Pow):
                    tmp14 = subjects.popleft()
                    subjects15 = deque(tmp14._args)
                    # State 18806
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i3.2.2.0', S(0))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 18807
                        subst4 = Substitution(subst3)
                        try:
                            subst4.try_add_variable('i3.2.2.1.0_1', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 18808
                            if len(subjects15) >= 1:
                                tmp18 = subjects15.popleft()
                                subst5 = Substitution(subst4)
                                try:
                                    subst5.try_add_variable('i3.2.2.1.0', tmp18)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 18809
                                    subst6 = Substitution(subst5)
                                    try:
                                        subst6.try_add_variable('i3.2.2', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 18810
                                        if len(subjects15) == 0:
                                            pass
                                            # State 18811
                                            if len(subjects) == 0:
                                                pass
                                                # 0: (d*(e + x*f)**p)**q /; (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f1158)
                                                yield 0, subst6
                                    if len(subjects15) >= 1:
                                        tmp21 = subjects15.popleft()
                                        subst6 = Substitution(subst5)
                                        try:
                                            subst6.try_add_variable('i3.2.2', tmp21)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 18810
                                            if len(subjects15) == 0:
                                                pass
                                                # State 18811
                                                if len(subjects) == 0:
                                                    pass
                                                    # 0: (d*(e + x*f)**p)**q /; (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f1158)
                                                    yield 0, subst6
                                        subjects15.appendleft(tmp21)
                                subjects15.appendleft(tmp18)
                        if len(subjects15) >= 1 and isinstance(subjects15[0], Mul):
                            tmp23 = subjects15.popleft()
                            associative1 = tmp23
                            associative_type1 = type(tmp23)
                            subjects24 = deque(tmp23._args)
                            matcher = CommutativeMatcher18813.get()
                            tmp25 = subjects24
                            subjects24 = []
                            for s in tmp25:
                                matcher.add_subject(s)
                            for pattern_index, subst4 in matcher.match(tmp25, subst3):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 18814
                                    subst5 = Substitution(subst4)
                                    try:
                                        subst5.try_add_variable('i3.2.2', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 18815
                                        if len(subjects15) == 0:
                                            pass
                                            # State 18816
                                            if len(subjects) == 0:
                                                pass
                                                # 0: (d*(e + x*f)**p)**q /; (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f1158)
                                                yield 0, subst5
                                    if len(subjects15) >= 1:
                                        tmp27 = []
                                        tmp27.append(subjects15.popleft())
                                        while True:
                                            if len(tmp27) > 1:
                                                tmp28 = create_operation_expression(associative1, tmp27)
                                            elif len(tmp27) == 1:
                                                tmp28 = tmp27[0]
                                            else:
                                                assert False, "Unreachable"
                                            subst5 = Substitution(subst4)
                                            try:
                                                subst5.try_add_variable('i3.2.2', tmp28)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 18815
                                                if len(subjects15) == 0:
                                                    pass
                                                    # State 18816
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 0: (d*(e + x*f)**p)**q /; (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f1158)
                                                        yield 0, subst5
                                            if len(subjects15) == 0:
                                                break
                                            tmp27.append(subjects15.popleft())
                                        subjects15.extendleft(reversed(tmp27))
                            subjects15.appendleft(tmp23)
                    if len(subjects15) >= 1 and isinstance(subjects15[0], Add):
                        tmp30 = subjects15.popleft()
                        associative1 = tmp30
                        associative_type1 = type(tmp30)
                        subjects31 = deque(tmp30._args)
                        matcher = CommutativeMatcher18818.get()
                        tmp32 = subjects31
                        subjects31 = []
                        for s in tmp32:
                            matcher.add_subject(s)
                        for pattern_index, subst3 in matcher.match(tmp32, subst2):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 18824
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i3.2.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 18825
                                    if len(subjects15) == 0:
                                        pass
                                        # State 18826
                                        if len(subjects) == 0:
                                            pass
                                            # 0: (d*(e + x*f)**p)**q /; (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f1158)
                                            yield 0, subst4
                                if len(subjects15) >= 1:
                                    tmp34 = []
                                    tmp34.append(subjects15.popleft())
                                    while True:
                                        if len(tmp34) > 1:
                                            tmp35 = create_operation_expression(associative1, tmp34)
                                        elif len(tmp34) == 1:
                                            tmp35 = tmp34[0]
                                        else:
                                            assert False, "Unreachable"
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i3.2.2', tmp35)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 18825
                                            if len(subjects15) == 0:
                                                pass
                                                # State 18826
                                                if len(subjects) == 0:
                                                    pass
                                                    # 0: (d*(e + x*f)**p)**q /; (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f1158)
                                                    yield 0, subst4
                                        if len(subjects15) == 0:
                                            break
                                        tmp34.append(subjects15.popleft())
                                    subjects15.extendleft(reversed(tmp34))
                        subjects15.appendleft(tmp30)
                    subjects.appendleft(tmp14)
            subst2 = Substitution(subst1)
            try:
                subst2.try_add_variable('i3.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 49217
                subst3 = Substitution(subst2)
                try:
                    subst3.try_add_variable('i3.2.1.0', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 49218
                    if len(subjects) >= 1 and isinstance(subjects[0], Pow):
                        tmp39 = subjects.popleft()
                        subjects40 = deque(tmp39._args)
                        # State 49219
                        if len(subjects40) >= 1:
                            tmp41 = subjects40.popleft()
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i3.2.1.1', tmp41)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 49220
                                if len(subjects40) >= 1:
                                    tmp43 = subjects40.popleft()
                                    subst5 = Substitution(subst4)
                                    try:
                                        subst5.try_add_variable('i3.2.1.2', tmp43)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 49221
                                        if len(subjects40) == 0:
                                            pass
                                            # State 49222
                                            if len(subjects) == 0:
                                                pass
                                                # 1: (a + b*x**n)**p /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f808)
                                                yield 1, subst5
                                    subjects40.appendleft(tmp43)
                            subjects40.appendleft(tmp41)
                        subjects.appendleft(tmp39)
                if len(subjects) >= 1 and isinstance(subjects[0], Mul):
                    tmp45 = subjects.popleft()
                    associative1 = tmp45
                    associative_type1 = type(tmp45)
                    subjects46 = deque(tmp45._args)
                    matcher = CommutativeMatcher49224.get()
                    tmp47 = subjects46
                    subjects46 = []
                    for s in tmp47:
                        matcher.add_subject(s)
                    for pattern_index, subst3 in matcher.match(tmp47, subst2):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 49229
                            if len(subjects) == 0:
                                pass
                                # 1: (a + b*x**n)**p /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f808)
                                yield 1, subst3
                    subjects.appendleft(tmp45)
            if len(subjects) >= 1:
                tmp48 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i3.1', tmp48)
                except ValueError:
                    pass
                else:
                    pass
                    # State 49293
                    if len(subjects) == 0:
                        pass
                        # 2: v**p /; (cons_f5) and (cons_f842) and (cons_f1227)
                        yield 2, subst2
                subjects.appendleft(tmp48)
            if len(subjects) >= 1 and isinstance(subjects[0], Mul):
                tmp50 = subjects.popleft()
                associative1 = tmp50
                associative_type1 = type(tmp50)
                subjects51 = deque(tmp50._args)
                matcher = CommutativeMatcher18828.get()
                tmp52 = subjects51
                subjects51 = []
                for s in tmp52:
                    matcher.add_subject(s)
                for pattern_index, subst2 in matcher.match(tmp52, subst1):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 18865
                        if len(subjects) == 0:
                            pass
                            # 0: (d*(e + x*f)**p)**q /; (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f1158)
                            yield 0, subst2
                subjects.appendleft(tmp50)
            if len(subjects) >= 1 and isinstance(subjects[0], Add):
                tmp53 = subjects.popleft()
                associative1 = tmp53
                associative_type1 = type(tmp53)
                subjects54 = deque(tmp53._args)
                matcher = CommutativeMatcher49231.get()
                tmp55 = subjects54
                subjects54 = []
                for s in tmp55:
                    matcher.add_subject(s)
                for pattern_index, subst2 in matcher.match(tmp55, subst1):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 49244
                        if len(subjects) == 0:
                            pass
                            # 1: (a + b*x**n)**p /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f808)
                            yield 1, subst2
                    if pattern_index == 1:
                        pass
                        # State 51254
                        if len(subjects) == 0:
                            pass
                            # 3: (a + b*(d + x*e)**n)**p /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f5) and (cons_f89) and (cons_f465)
                            yield 3, subst2
                    if pattern_index == 2:
                        pass
                        # State 51442
                        if len(subjects) == 0:
                            pass
                            # 4: (a + b*(d + x*e)**n)**p /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f5) and (cons_f1233)
                            yield 4, subst2
                subjects.appendleft(tmp53)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i3.3', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 53871
            if len(subjects) >= 1 and isinstance(subjects[0], log):
                tmp57 = subjects.popleft()
                subjects58 = deque(tmp57._args)
                # State 53872
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i3.3.0', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 53873
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i3.3.2', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 53874
                        if len(subjects58) >= 1:
                            tmp61 = subjects58.popleft()
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i3.3.1', tmp61)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 53875
                                if len(subjects58) == 0:
                                    pass
                                    # State 53876
                                    if len(subjects) == 0:
                                        pass
                                        # 5: log(b*x**n)**p /; (cons_f2) and (cons_f3) and (cons_f4) and (cons_f5) and (cons_f1246)
                                        yield 5, subst4
                            subjects58.appendleft(tmp61)
                    if len(subjects58) >= 1 and isinstance(subjects58[0], Pow):
                        tmp63 = subjects58.popleft()
                        subjects64 = deque(tmp63._args)
                        # State 53877
                        if len(subjects64) >= 1:
                            tmp65 = subjects64.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i3.3.1', tmp65)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 53878
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i3.3.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 53879
                                    if len(subjects64) == 0:
                                        pass
                                        # State 53880
                                        if len(subjects58) == 0:
                                            pass
                                            # State 53881
                                            if len(subjects) == 0:
                                                pass
                                                # 5: log(b*x**n)**p /; (cons_f2) and (cons_f3) and (cons_f4) and (cons_f5) and (cons_f1246)
                                                yield 5, subst4
                                if len(subjects64) >= 1:
                                    tmp68 = subjects64.popleft()
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i3.3.2', tmp68)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 53879
                                        if len(subjects64) == 0:
                                            pass
                                            # State 53880
                                            if len(subjects58) == 0:
                                                pass
                                                # State 53881
                                                if len(subjects) == 0:
                                                    pass
                                                    # 5: log(b*x**n)**p /; (cons_f2) and (cons_f3) and (cons_f4) and (cons_f5) and (cons_f1246)
                                                    yield 5, subst4
                                    subjects64.appendleft(tmp68)
                            subjects64.appendleft(tmp65)
                        subjects58.appendleft(tmp63)
                if len(subjects58) >= 1 and isinstance(subjects58[0], Mul):
                    tmp70 = subjects58.popleft()
                    associative1 = tmp70
                    associative_type1 = type(tmp70)
                    subjects71 = deque(tmp70._args)
                    matcher = CommutativeMatcher53883.get()
                    tmp72 = subjects71
                    subjects71 = []
                    for s in tmp72:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp72, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 53890
                            if len(subjects58) == 0:
                                pass
                                # State 53891
                                if len(subjects) == 0:
                                    pass
                                    # 5: log(b*x**n)**p /; (cons_f2) and (cons_f3) and (cons_f4) and (cons_f5) and (cons_f1246)
                                    yield 5, subst2
                    subjects58.appendleft(tmp70)
                subjects.appendleft(tmp57)
        if len(subjects) >= 1 and isinstance(subjects[0], Pow):
            tmp73 = subjects.popleft()
            subjects74 = deque(tmp73._args)
            # State 18866
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i3.2.0', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 18867
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i3.2.2', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 18868
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i3.2.2.0', S(0))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 18869
                        subst4 = Substitution(subst3)
                        try:
                            subst4.try_add_variable('i3.2.2.1.0_1', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 18870
                            if len(subjects74) >= 1:
                                tmp79 = subjects74.popleft()
                                subst5 = Substitution(subst4)
                                try:
                                    subst5.try_add_variable('i3.2.2.1.0', tmp79)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 18871
                                    subst6 = Substitution(subst5)
                                    try:
                                        subst6.try_add_variable('i3.2', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 18872
                                        if len(subjects74) == 0:
                                            pass
                                            # State 18873
                                            if len(subjects) == 0:
                                                pass
                                                # 0: (d*(e + x*f)**p)**q /; (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f1158)
                                                yield 0, subst6
                                    if len(subjects74) >= 1:
                                        tmp82 = subjects74.popleft()
                                        subst6 = Substitution(subst5)
                                        try:
                                            subst6.try_add_variable('i3.2', tmp82)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 18872
                                            if len(subjects74) == 0:
                                                pass
                                                # State 18873
                                                if len(subjects) == 0:
                                                    pass
                                                    # 0: (d*(e + x*f)**p)**q /; (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f1158)
                                                    yield 0, subst6
                                        subjects74.appendleft(tmp82)
                                subjects74.appendleft(tmp79)
                        if len(subjects74) >= 1 and isinstance(subjects74[0], Mul):
                            tmp84 = subjects74.popleft()
                            associative1 = tmp84
                            associative_type1 = type(tmp84)
                            subjects85 = deque(tmp84._args)
                            matcher = CommutativeMatcher18875.get()
                            tmp86 = subjects85
                            subjects85 = []
                            for s in tmp86:
                                matcher.add_subject(s)
                            for pattern_index, subst4 in matcher.match(tmp86, subst3):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 18876
                                    subst5 = Substitution(subst4)
                                    try:
                                        subst5.try_add_variable('i3.2', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 18877
                                        if len(subjects74) == 0:
                                            pass
                                            # State 18878
                                            if len(subjects) == 0:
                                                pass
                                                # 0: (d*(e + x*f)**p)**q /; (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f1158)
                                                yield 0, subst5
                                    if len(subjects74) >= 1:
                                        tmp88 = []
                                        tmp88.append(subjects74.popleft())
                                        while True:
                                            if len(tmp88) > 1:
                                                tmp89 = create_operation_expression(associative1, tmp88)
                                            elif len(tmp88) == 1:
                                                tmp89 = tmp88[0]
                                            else:
                                                assert False, "Unreachable"
                                            subst5 = Substitution(subst4)
                                            try:
                                                subst5.try_add_variable('i3.2', tmp89)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 18877
                                                if len(subjects74) == 0:
                                                    pass
                                                    # State 18878
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 0: (d*(e + x*f)**p)**q /; (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f1158)
                                                        yield 0, subst5
                                            if len(subjects74) == 0:
                                                break
                                            tmp88.append(subjects74.popleft())
                                        subjects74.extendleft(reversed(tmp88))
                            subjects74.appendleft(tmp84)
                    if len(subjects74) >= 1 and isinstance(subjects74[0], Add):
                        tmp91 = subjects74.popleft()
                        associative1 = tmp91
                        associative_type1 = type(tmp91)
                        subjects92 = deque(tmp91._args)
                        matcher = CommutativeMatcher18880.get()
                        tmp93 = subjects92
                        subjects92 = []
                        for s in tmp93:
                            matcher.add_subject(s)
                        for pattern_index, subst3 in matcher.match(tmp93, subst2):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 18886
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i3.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 18887
                                    if len(subjects74) == 0:
                                        pass
                                        # State 18888
                                        if len(subjects) == 0:
                                            pass
                                            # 0: (d*(e + x*f)**p)**q /; (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f1158)
                                            yield 0, subst4
                                if len(subjects74) >= 1:
                                    tmp95 = []
                                    tmp95.append(subjects74.popleft())
                                    while True:
                                        if len(tmp95) > 1:
                                            tmp96 = create_operation_expression(associative1, tmp95)
                                        elif len(tmp95) == 1:
                                            tmp96 = tmp95[0]
                                        else:
                                            assert False, "Unreachable"
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i3.2', tmp96)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 18887
                                            if len(subjects74) == 0:
                                                pass
                                                # State 18888
                                                if len(subjects) == 0:
                                                    pass
                                                    # 0: (d*(e + x*f)**p)**q /; (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f1158)
                                                    yield 0, subst4
                                        if len(subjects74) == 0:
                                            break
                                        tmp95.append(subjects74.popleft())
                                    subjects74.extendleft(reversed(tmp95))
                        subjects74.appendleft(tmp91)
                if len(subjects74) >= 1 and isinstance(subjects74[0], Pow):
                    tmp98 = subjects74.popleft()
                    subjects99 = deque(tmp98._args)
                    # State 18889
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i3.2.2.0', S(0))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 18890
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i3.2.2.1.0_1', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 18891
                            if len(subjects99) >= 1:
                                tmp102 = subjects99.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i3.2.2.1.0', tmp102)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 18892
                                    subst5 = Substitution(subst4)
                                    try:
                                        subst5.try_add_variable('i3.2.2', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 18893
                                        if len(subjects99) == 0:
                                            pass
                                            # State 18894
                                            subst6 = Substitution(subst5)
                                            try:
                                                subst6.try_add_variable('i3.2', 1)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 18895
                                                if len(subjects74) == 0:
                                                    pass
                                                    # State 18896
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 0: (d*(e + x*f)**p)**q /; (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f1158)
                                                        yield 0, subst6
                                            if len(subjects74) >= 1:
                                                tmp106 = subjects74.popleft()
                                                subst6 = Substitution(subst5)
                                                try:
                                                    subst6.try_add_variable('i3.2', tmp106)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 18895
                                                    if len(subjects74) == 0:
                                                        pass
                                                        # State 18896
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 0: (d*(e + x*f)**p)**q /; (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f1158)
                                                            yield 0, subst6
                                                subjects74.appendleft(tmp106)
                                    if len(subjects99) >= 1:
                                        tmp108 = subjects99.popleft()
                                        subst5 = Substitution(subst4)
                                        try:
                                            subst5.try_add_variable('i3.2.2', tmp108)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 18893
                                            if len(subjects99) == 0:
                                                pass
                                                # State 18894
                                                subst6 = Substitution(subst5)
                                                try:
                                                    subst6.try_add_variable('i3.2', 1)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 18895
                                                    if len(subjects74) == 0:
                                                        pass
                                                        # State 18896
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 0: (d*(e + x*f)**p)**q /; (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f1158)
                                                            yield 0, subst6
                                                if len(subjects74) >= 1:
                                                    tmp111 = subjects74.popleft()
                                                    subst6 = Substitution(subst5)
                                                    try:
                                                        subst6.try_add_variable('i3.2', tmp111)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 18895
                                                        if len(subjects74) == 0:
                                                            pass
                                                            # State 18896
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 0: (d*(e + x*f)**p)**q /; (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f1158)
                                                                yield 0, subst6
                                                    subjects74.appendleft(tmp111)
                                        subjects99.appendleft(tmp108)
                                subjects99.appendleft(tmp102)
                        if len(subjects99) >= 1 and isinstance(subjects99[0], Mul):
                            tmp113 = subjects99.popleft()
                            associative1 = tmp113
                            associative_type1 = type(tmp113)
                            subjects114 = deque(tmp113._args)
                            matcher = CommutativeMatcher18898.get()
                            tmp115 = subjects114
                            subjects114 = []
                            for s in tmp115:
                                matcher.add_subject(s)
                            for pattern_index, subst3 in matcher.match(tmp115, subst2):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 18899
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i3.2.2', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 18900
                                        if len(subjects99) == 0:
                                            pass
                                            # State 18901
                                            subst5 = Substitution(subst4)
                                            try:
                                                subst5.try_add_variable('i3.2', 1)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 18902
                                                if len(subjects74) == 0:
                                                    pass
                                                    # State 18903
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 0: (d*(e + x*f)**p)**q /; (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f1158)
                                                        yield 0, subst5
                                            if len(subjects74) >= 1:
                                                tmp118 = subjects74.popleft()
                                                subst5 = Substitution(subst4)
                                                try:
                                                    subst5.try_add_variable('i3.2', tmp118)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 18902
                                                    if len(subjects74) == 0:
                                                        pass
                                                        # State 18903
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 0: (d*(e + x*f)**p)**q /; (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f1158)
                                                            yield 0, subst5
                                                subjects74.appendleft(tmp118)
                                    if len(subjects99) >= 1:
                                        tmp120 = []
                                        tmp120.append(subjects99.popleft())
                                        while True:
                                            if len(tmp120) > 1:
                                                tmp121 = create_operation_expression(associative1, tmp120)
                                            elif len(tmp120) == 1:
                                                tmp121 = tmp120[0]
                                            else:
                                                assert False, "Unreachable"
                                            subst4 = Substitution(subst3)
                                            try:
                                                subst4.try_add_variable('i3.2.2', tmp121)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 18900
                                                if len(subjects99) == 0:
                                                    pass
                                                    # State 18901
                                                    subst5 = Substitution(subst4)
                                                    try:
                                                        subst5.try_add_variable('i3.2', 1)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 18902
                                                        if len(subjects74) == 0:
                                                            pass
                                                            # State 18903
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 0: (d*(e + x*f)**p)**q /; (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f1158)
                                                                yield 0, subst5
                                                    if len(subjects74) >= 1:
                                                        tmp124 = subjects74.popleft()
                                                        subst5 = Substitution(subst4)
                                                        try:
                                                            subst5.try_add_variable('i3.2', tmp124)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            # State 18902
                                                            if len(subjects74) == 0:
                                                                pass
                                                                # State 18903
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 0: (d*(e + x*f)**p)**q /; (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f1158)
                                                                    yield 0, subst5
                                                        subjects74.appendleft(tmp124)
                                            if len(subjects99) == 0:
                                                break
                                            tmp120.append(subjects99.popleft())
                                        subjects99.extendleft(reversed(tmp120))
                            subjects99.appendleft(tmp113)
                    if len(subjects99) >= 1 and isinstance(subjects99[0], Add):
                        tmp126 = subjects99.popleft()
                        associative1 = tmp126
                        associative_type1 = type(tmp126)
                        subjects127 = deque(tmp126._args)
                        matcher = CommutativeMatcher18905.get()
                        tmp128 = subjects127
                        subjects127 = []
                        for s in tmp128:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp128, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 18911
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i3.2.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 18912
                                    if len(subjects99) == 0:
                                        pass
                                        # State 18913
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i3.2', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 18914
                                            if len(subjects74) == 0:
                                                pass
                                                # State 18915
                                                if len(subjects) == 0:
                                                    pass
                                                    # 0: (d*(e + x*f)**p)**q /; (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f1158)
                                                    yield 0, subst4
                                        if len(subjects74) >= 1:
                                            tmp131 = subjects74.popleft()
                                            subst4 = Substitution(subst3)
                                            try:
                                                subst4.try_add_variable('i3.2', tmp131)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 18914
                                                if len(subjects74) == 0:
                                                    pass
                                                    # State 18915
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 0: (d*(e + x*f)**p)**q /; (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f1158)
                                                        yield 0, subst4
                                            subjects74.appendleft(tmp131)
                                if len(subjects99) >= 1:
                                    tmp133 = []
                                    tmp133.append(subjects99.popleft())
                                    while True:
                                        if len(tmp133) > 1:
                                            tmp134 = create_operation_expression(associative1, tmp133)
                                        elif len(tmp133) == 1:
                                            tmp134 = tmp133[0]
                                        else:
                                            assert False, "Unreachable"
                                        subst3 = Substitution(subst2)
                                        try:
                                            subst3.try_add_variable('i3.2.2', tmp134)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 18912
                                            if len(subjects99) == 0:
                                                pass
                                                # State 18913
                                                subst4 = Substitution(subst3)
                                                try:
                                                    subst4.try_add_variable('i3.2', 1)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 18914
                                                    if len(subjects74) == 0:
                                                        pass
                                                        # State 18915
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 0: (d*(e + x*f)**p)**q /; (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f1158)
                                                            yield 0, subst4
                                                if len(subjects74) >= 1:
                                                    tmp137 = subjects74.popleft()
                                                    subst4 = Substitution(subst3)
                                                    try:
                                                        subst4.try_add_variable('i3.2', tmp137)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 18914
                                                        if len(subjects74) == 0:
                                                            pass
                                                            # State 18915
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 0: (d*(e + x*f)**p)**q /; (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f1158)
                                                                yield 0, subst4
                                                    subjects74.appendleft(tmp137)
                                        if len(subjects99) == 0:
                                            break
                                        tmp133.append(subjects99.popleft())
                                    subjects99.extendleft(reversed(tmp133))
                        subjects99.appendleft(tmp126)
                    subjects74.appendleft(tmp98)
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i3.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 49245
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i3.2.1.0', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 49246
                    if len(subjects74) >= 1 and isinstance(subjects74[0], Pow):
                        tmp141 = subjects74.popleft()
                        subjects142 = deque(tmp141._args)
                        # State 49247
                        if len(subjects142) >= 1:
                            tmp143 = subjects142.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i3.2.1.1', tmp143)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 49248
                                if len(subjects142) >= 1:
                                    tmp145 = subjects142.popleft()
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i3.2.1.2', tmp145)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 49249
                                        if len(subjects142) == 0:
                                            pass
                                            # State 49250
                                            subst5 = Substitution(subst4)
                                            try:
                                                subst5.try_add_variable('i3.2', 1)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 49251
                                                if len(subjects74) == 0:
                                                    pass
                                                    # State 49252
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 1: (a + b*x**n)**p /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f808)
                                                        yield 1, subst5
                                            if len(subjects74) >= 1:
                                                tmp148 = subjects74.popleft()
                                                subst5 = Substitution(subst4)
                                                try:
                                                    subst5.try_add_variable('i3.2', tmp148)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 49251
                                                    if len(subjects74) == 0:
                                                        pass
                                                        # State 49252
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 1: (a + b*x**n)**p /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f808)
                                                            yield 1, subst5
                                                subjects74.appendleft(tmp148)
                                    subjects142.appendleft(tmp145)
                            subjects142.appendleft(tmp143)
                        subjects74.appendleft(tmp141)
                if len(subjects74) >= 1 and isinstance(subjects74[0], Mul):
                    tmp150 = subjects74.popleft()
                    associative1 = tmp150
                    associative_type1 = type(tmp150)
                    subjects151 = deque(tmp150._args)
                    matcher = CommutativeMatcher49254.get()
                    tmp152 = subjects151
                    subjects151 = []
                    for s in tmp152:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp152, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 49259
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i3.2', 1)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 49260
                                if len(subjects74) == 0:
                                    pass
                                    # State 49261
                                    if len(subjects) == 0:
                                        pass
                                        # 1: (a + b*x**n)**p /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f808)
                                        yield 1, subst3
                            if len(subjects74) >= 1:
                                tmp154 = []
                                tmp154.append(subjects74.popleft())
                                while True:
                                    if len(tmp154) > 1:
                                        tmp155 = create_operation_expression(associative1, tmp154)
                                    elif len(tmp154) == 1:
                                        tmp155 = tmp154[0]
                                    else:
                                        assert False, "Unreachable"
                                    subst3 = Substitution(subst2)
                                    try:
                                        subst3.try_add_variable('i3.2', tmp155)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 49260
                                        if len(subjects74) == 0:
                                            pass
                                            # State 49261
                                            if len(subjects) == 0:
                                                pass
                                                # 1: (a + b*x**n)**p /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f808)
                                                yield 1, subst3
                                    if len(subjects74) == 0:
                                        break
                                    tmp154.append(subjects74.popleft())
                                subjects74.extendleft(reversed(tmp154))
                    subjects74.appendleft(tmp150)
            if len(subjects74) >= 1:
                tmp157 = subjects74.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i3.1', tmp157)
                except ValueError:
                    pass
                else:
                    pass
                    # State 49294
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i3.2', 1)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 49295
                        if len(subjects74) == 0:
                            pass
                            # State 49296
                            if len(subjects) == 0:
                                pass
                                # 2: v**p /; (cons_f5) and (cons_f842) and (cons_f1227)
                                yield 2, subst2
                    if len(subjects74) >= 1:
                        tmp160 = subjects74.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i3.2', tmp160)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 49295
                            if len(subjects74) == 0:
                                pass
                                # State 49296
                                if len(subjects) == 0:
                                    pass
                                    # 2: v**p /; (cons_f5) and (cons_f842) and (cons_f1227)
                                    yield 2, subst2
                        subjects74.appendleft(tmp160)
                subjects74.appendleft(tmp157)
            if len(subjects74) >= 1 and isinstance(subjects74[0], Mul):
                tmp162 = subjects74.popleft()
                associative1 = tmp162
                associative_type1 = type(tmp162)
                subjects163 = deque(tmp162._args)
                matcher = CommutativeMatcher18917.get()
                tmp164 = subjects163
                subjects163 = []
                for s in tmp164:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp164, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 18954
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i3.2', 1)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 18955
                            if len(subjects74) == 0:
                                pass
                                # State 18956
                                if len(subjects) == 0:
                                    pass
                                    # 0: (d*(e + x*f)**p)**q /; (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f1158)
                                    yield 0, subst2
                        if len(subjects74) >= 1:
                            tmp166 = []
                            tmp166.append(subjects74.popleft())
                            while True:
                                if len(tmp166) > 1:
                                    tmp167 = create_operation_expression(associative1, tmp166)
                                elif len(tmp166) == 1:
                                    tmp167 = tmp166[0]
                                else:
                                    assert False, "Unreachable"
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i3.2', tmp167)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 18955
                                    if len(subjects74) == 0:
                                        pass
                                        # State 18956
                                        if len(subjects) == 0:
                                            pass
                                            # 0: (d*(e + x*f)**p)**q /; (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f1158)
                                            yield 0, subst2
                                if len(subjects74) == 0:
                                    break
                                tmp166.append(subjects74.popleft())
                            subjects74.extendleft(reversed(tmp166))
                subjects74.appendleft(tmp162)
            if len(subjects74) >= 1 and isinstance(subjects74[0], Add):
                tmp169 = subjects74.popleft()
                associative1 = tmp169
                associative_type1 = type(tmp169)
                subjects170 = deque(tmp169._args)
                matcher = CommutativeMatcher49263.get()
                tmp171 = subjects170
                subjects170 = []
                for s in tmp171:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp171, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 49276
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i3.2', 1)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 49277
                            if len(subjects74) == 0:
                                pass
                                # State 49278
                                if len(subjects) == 0:
                                    pass
                                    # 1: (a + b*x**n)**p /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f808)
                                    yield 1, subst2
                        if len(subjects74) >= 1:
                            tmp173 = []
                            tmp173.append(subjects74.popleft())
                            while True:
                                if len(tmp173) > 1:
                                    tmp174 = create_operation_expression(associative1, tmp173)
                                elif len(tmp173) == 1:
                                    tmp174 = tmp173[0]
                                else:
                                    assert False, "Unreachable"
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i3.2', tmp174)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 49277
                                    if len(subjects74) == 0:
                                        pass
                                        # State 49278
                                        if len(subjects) == 0:
                                            pass
                                            # 1: (a + b*x**n)**p /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f808)
                                            yield 1, subst2
                                if len(subjects74) == 0:
                                    break
                                tmp173.append(subjects74.popleft())
                            subjects74.extendleft(reversed(tmp173))
                    if pattern_index == 1:
                        pass
                        # State 51296
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i3.2', 1)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 51297
                            if len(subjects74) == 0:
                                pass
                                # State 51298
                                if len(subjects) == 0:
                                    pass
                                    # 3: (a + b*(d + x*e)**n)**p /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f5) and (cons_f89) and (cons_f465)
                                    yield 3, subst2
                        if len(subjects74) >= 1:
                            tmp177 = []
                            tmp177.append(subjects74.popleft())
                            while True:
                                if len(tmp177) > 1:
                                    tmp178 = create_operation_expression(associative1, tmp177)
                                elif len(tmp177) == 1:
                                    tmp178 = tmp177[0]
                                else:
                                    assert False, "Unreachable"
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i3.2', tmp178)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 51297
                                    if len(subjects74) == 0:
                                        pass
                                        # State 51298
                                        if len(subjects) == 0:
                                            pass
                                            # 3: (a + b*(d + x*e)**n)**p /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f5) and (cons_f89) and (cons_f465)
                                            yield 3, subst2
                                if len(subjects74) == 0:
                                    break
                                tmp177.append(subjects74.popleft())
                            subjects74.extendleft(reversed(tmp177))
                    if pattern_index == 2:
                        pass
                        # State 51486
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i3.2', 1)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 51487
                            if len(subjects74) == 0:
                                pass
                                # State 51488
                                if len(subjects) == 0:
                                    pass
                                    # 4: (a + b*(d + x*e)**n)**p /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f5) and (cons_f1233)
                                    yield 4, subst2
                        if len(subjects74) >= 1:
                            tmp181 = []
                            tmp181.append(subjects74.popleft())
                            while True:
                                if len(tmp181) > 1:
                                    tmp182 = create_operation_expression(associative1, tmp181)
                                elif len(tmp181) == 1:
                                    tmp182 = tmp181[0]
                                else:
                                    assert False, "Unreachable"
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i3.2', tmp182)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 51487
                                    if len(subjects74) == 0:
                                        pass
                                        # State 51488
                                        if len(subjects) == 0:
                                            pass
                                            # 4: (a + b*(d + x*e)**n)**p /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f5) and (cons_f1233)
                                            yield 4, subst2
                                if len(subjects74) == 0:
                                    break
                                tmp181.append(subjects74.popleft())
                            subjects74.extendleft(reversed(tmp181))
                subjects74.appendleft(tmp169)
            if len(subjects74) >= 1 and isinstance(subjects74[0], log):
                tmp184 = subjects74.popleft()
                subjects185 = deque(tmp184._args)
                # State 53892
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i3.3.0', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 53893
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i3.3.2', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 53894
                        if len(subjects185) >= 1:
                            tmp188 = subjects185.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i3.3.1', tmp188)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 53895
                                if len(subjects185) == 0:
                                    pass
                                    # State 53896
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i3.3', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 53897
                                        if len(subjects74) == 0:
                                            pass
                                            # State 53898
                                            if len(subjects) == 0:
                                                pass
                                                # 5: log(b*x**n)**p /; (cons_f2) and (cons_f3) and (cons_f4) and (cons_f5) and (cons_f1246)
                                                yield 5, subst4
                                    if len(subjects74) >= 1:
                                        tmp191 = subjects74.popleft()
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i3.3', tmp191)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 53897
                                            if len(subjects74) == 0:
                                                pass
                                                # State 53898
                                                if len(subjects) == 0:
                                                    pass
                                                    # 5: log(b*x**n)**p /; (cons_f2) and (cons_f3) and (cons_f4) and (cons_f5) and (cons_f1246)
                                                    yield 5, subst4
                                        subjects74.appendleft(tmp191)
                            subjects185.appendleft(tmp188)
                    if len(subjects185) >= 1 and isinstance(subjects185[0], Pow):
                        tmp193 = subjects185.popleft()
                        subjects194 = deque(tmp193._args)
                        # State 53899
                        if len(subjects194) >= 1:
                            tmp195 = subjects194.popleft()
                            subst2 = Substitution(subst1)
                            try:
                                subst2.try_add_variable('i3.3.1', tmp195)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 53900
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i3.3.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 53901
                                    if len(subjects194) == 0:
                                        pass
                                        # State 53902
                                        if len(subjects185) == 0:
                                            pass
                                            # State 53903
                                            subst4 = Substitution(subst3)
                                            try:
                                                subst4.try_add_variable('i3.3', 1)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 53904
                                                if len(subjects74) == 0:
                                                    pass
                                                    # State 53905
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 5: log(b*x**n)**p /; (cons_f2) and (cons_f3) and (cons_f4) and (cons_f5) and (cons_f1246)
                                                        yield 5, subst4
                                            if len(subjects74) >= 1:
                                                tmp199 = subjects74.popleft()
                                                subst4 = Substitution(subst3)
                                                try:
                                                    subst4.try_add_variable('i3.3', tmp199)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 53904
                                                    if len(subjects74) == 0:
                                                        pass
                                                        # State 53905
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 5: log(b*x**n)**p /; (cons_f2) and (cons_f3) and (cons_f4) and (cons_f5) and (cons_f1246)
                                                            yield 5, subst4
                                                subjects74.appendleft(tmp199)
                                if len(subjects194) >= 1:
                                    tmp201 = subjects194.popleft()
                                    subst3 = Substitution(subst2)
                                    try:
                                        subst3.try_add_variable('i3.3.2', tmp201)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 53901
                                        if len(subjects194) == 0:
                                            pass
                                            # State 53902
                                            if len(subjects185) == 0:
                                                pass
                                                # State 53903
                                                subst4 = Substitution(subst3)
                                                try:
                                                    subst4.try_add_variable('i3.3', 1)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 53904
                                                    if len(subjects74) == 0:
                                                        pass
                                                        # State 53905
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 5: log(b*x**n)**p /; (cons_f2) and (cons_f3) and (cons_f4) and (cons_f5) and (cons_f1246)
                                                            yield 5, subst4
                                                if len(subjects74) >= 1:
                                                    tmp204 = subjects74.popleft()
                                                    subst4 = Substitution(subst3)
                                                    try:
                                                        subst4.try_add_variable('i3.3', tmp204)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 53904
                                                        if len(subjects74) == 0:
                                                            pass
                                                            # State 53905
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 5: log(b*x**n)**p /; (cons_f2) and (cons_f3) and (cons_f4) and (cons_f5) and (cons_f1246)
                                                                yield 5, subst4
                                                    subjects74.appendleft(tmp204)
                                    subjects194.appendleft(tmp201)
                            subjects194.appendleft(tmp195)
                        subjects185.appendleft(tmp193)
                if len(subjects185) >= 1 and isinstance(subjects185[0], Mul):
                    tmp206 = subjects185.popleft()
                    associative1 = tmp206
                    associative_type1 = type(tmp206)
                    subjects207 = deque(tmp206._args)
                    matcher = CommutativeMatcher53907.get()
                    tmp208 = subjects207
                    subjects207 = []
                    for s in tmp208:
                        matcher.add_subject(s)
                    for pattern_index, subst1 in matcher.match(tmp208, subst0):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 53914
                            if len(subjects185) == 0:
                                pass
                                # State 53915
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i3.3', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 53916
                                    if len(subjects74) == 0:
                                        pass
                                        # State 53917
                                        if len(subjects) == 0:
                                            pass
                                            # 5: log(b*x**n)**p /; (cons_f2) and (cons_f3) and (cons_f4) and (cons_f5) and (cons_f1246)
                                            yield 5, subst2
                                if len(subjects74) >= 1:
                                    tmp210 = subjects74.popleft()
                                    subst2 = Substitution(subst1)
                                    try:
                                        subst2.try_add_variable('i3.3', tmp210)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 53916
                                        if len(subjects74) == 0:
                                            pass
                                            # State 53917
                                            if len(subjects) == 0:
                                                pass
                                                # 5: log(b*x**n)**p /; (cons_f2) and (cons_f3) and (cons_f4) and (cons_f5) and (cons_f1246)
                                                yield 5, subst2
                                    subjects74.appendleft(tmp210)
                    subjects185.appendleft(tmp206)
                subjects74.appendleft(tmp184)
            subjects.appendleft(tmp73)
        return
        yield


from .generated_part010245 import *
from .generated_part010248 import *
from .generated_part010269 import *
from .generated_part010226 import *
from .generated_part010247 import *
from .generated_part010215 import *
from .generated_part010213 import *
from .generated_part010244 import *
from collections import deque
from matchpy.utils import VariableWithCount
from .generated_part010219 import *
from .generated_part010212 import *
from .generated_part010242 import *
from .generated_part010255 import *
from .generated_part010218 import *
from .generated_part010241 import *
from multiset import Multiset
from .generated_part010240 import *
from matchpy.matching.many_to_one import CommutativeMatcher
from .generated_part010216 import *