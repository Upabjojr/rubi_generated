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

class CommutativeMatcher20279(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({0: 1}), [
      (VariableWithCount('i3.1.2.0', 1, 1, S(1)), Mul)
]),
    1: (1, Multiset({1: 1}), [
      (VariableWithCount('i3.1.2.0', 1, 1, S(1)), Mul)
]),
    2: (2, Multiset({2: 1}), [
      (VariableWithCount('i3.1.2.0', 1, 1, S(1)), Mul)
]),
    3: (3, Multiset({3: 1}), [
      (VariableWithCount('i3.1.2.0', 1, 1, S(1)), Mul)
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
        if CommutativeMatcher20279._instance is None:
            CommutativeMatcher20279._instance = CommutativeMatcher20279()
        return CommutativeMatcher20279._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 20278
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i3.1.2.2', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 20280
            subst2 = Substitution(subst1)
            try:
                subst2.try_add_variable('i3.1.2.2.0', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 20281
                subst3 = Substitution(subst2)
                try:
                    subst3.try_add_variable('i3.1.2.2.2', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 20282
                    subst4 = Substitution(subst3)
                    try:
                        subst4.try_add_variable('i3.1.2.2.2.0', S(0))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 20283
                        subst5 = Substitution(subst4)
                        try:
                            subst5.try_add_variable('i3.1.2.2.2.1.0_1', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 20284
                            if len(subjects) >= 1:
                                tmp6 = subjects.popleft()
                                subst6 = Substitution(subst5)
                                try:
                                    subst6.try_add_variable('i3.1.2.2.2.1.0', tmp6)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 20285
                                    if len(subjects) == 0:
                                        pass
                                        # 0: (d*(e + x*f)**p)**q
                                subjects.appendleft(tmp6)
                        if len(subjects) >= 1 and isinstance(subjects[0], Mul):
                            tmp8 = subjects.popleft()
                            associative1 = tmp8
                            associative_type1 = type(tmp8)
                            subjects9 = deque(tmp8._args)
                            matcher = CommutativeMatcher20287.get()
                            tmp10 = subjects9
                            subjects9 = []
                            for s in tmp10:
                                matcher.add_subject(s)
                            for pattern_index, subst5 in matcher.match(tmp10, subst4):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 20288
                                    if len(subjects) == 0:
                                        pass
                                        # 0: (d*(e + x*f)**p)**q
                            subjects.appendleft(tmp8)
                    if len(subjects) >= 1 and isinstance(subjects[0], Add):
                        tmp11 = subjects.popleft()
                        associative1 = tmp11
                        associative_type1 = type(tmp11)
                        subjects12 = deque(tmp11._args)
                        matcher = CommutativeMatcher20290.get()
                        tmp13 = subjects12
                        subjects12 = []
                        for s in tmp13:
                            matcher.add_subject(s)
                        for pattern_index, subst4 in matcher.match(tmp13, subst3):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 20296
                                if len(subjects) == 0:
                                    pass
                                    # 0: (d*(e + x*f)**p)**q
                        subjects.appendleft(tmp11)
                if len(subjects) >= 1 and isinstance(subjects[0], Pow):
                    tmp14 = subjects.popleft()
                    subjects15 = deque(tmp14._args)
                    # State 20297
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i3.1.2.2.2.0', S(0))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 20298
                        subst4 = Substitution(subst3)
                        try:
                            subst4.try_add_variable('i3.1.2.2.2.1.0_1', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 20299
                            if len(subjects15) >= 1:
                                tmp18 = subjects15.popleft()
                                subst5 = Substitution(subst4)
                                try:
                                    subst5.try_add_variable('i3.1.2.2.2.1.0', tmp18)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 20300
                                    subst6 = Substitution(subst5)
                                    try:
                                        subst6.try_add_variable('i3.1.2.2.2', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 20301
                                        if len(subjects15) == 0:
                                            pass
                                            # State 20302
                                            if len(subjects) == 0:
                                                pass
                                                # 0: (d*(e + x*f)**p)**q
                                    if len(subjects15) >= 1:
                                        tmp21 = subjects15.popleft()
                                        subst6 = Substitution(subst5)
                                        try:
                                            subst6.try_add_variable('i3.1.2.2.2', tmp21)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 20301
                                            if len(subjects15) == 0:
                                                pass
                                                # State 20302
                                                if len(subjects) == 0:
                                                    pass
                                                    # 0: (d*(e + x*f)**p)**q
                                        subjects15.appendleft(tmp21)
                                subjects15.appendleft(tmp18)
                        if len(subjects15) >= 1 and isinstance(subjects15[0], Mul):
                            tmp23 = subjects15.popleft()
                            associative1 = tmp23
                            associative_type1 = type(tmp23)
                            subjects24 = deque(tmp23._args)
                            matcher = CommutativeMatcher20304.get()
                            tmp25 = subjects24
                            subjects24 = []
                            for s in tmp25:
                                matcher.add_subject(s)
                            for pattern_index, subst4 in matcher.match(tmp25, subst3):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 20305
                                    subst5 = Substitution(subst4)
                                    try:
                                        subst5.try_add_variable('i3.1.2.2.2', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 20306
                                        if len(subjects15) == 0:
                                            pass
                                            # State 20307
                                            if len(subjects) == 0:
                                                pass
                                                # 0: (d*(e + x*f)**p)**q
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
                                                subst5.try_add_variable('i3.1.2.2.2', tmp28)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 20306
                                                if len(subjects15) == 0:
                                                    pass
                                                    # State 20307
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 0: (d*(e + x*f)**p)**q
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
                        matcher = CommutativeMatcher20309.get()
                        tmp32 = subjects31
                        subjects31 = []
                        for s in tmp32:
                            matcher.add_subject(s)
                        for pattern_index, subst3 in matcher.match(tmp32, subst2):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 20315
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i3.1.2.2.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 20316
                                    if len(subjects15) == 0:
                                        pass
                                        # State 20317
                                        if len(subjects) == 0:
                                            pass
                                            # 0: (d*(e + x*f)**p)**q
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
                                            subst4.try_add_variable('i3.1.2.2.2', tmp35)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 20316
                                            if len(subjects15) == 0:
                                                pass
                                                # State 20317
                                                if len(subjects) == 0:
                                                    pass
                                                    # 0: (d*(e + x*f)**p)**q
                                        if len(subjects15) == 0:
                                            break
                                        tmp34.append(subjects15.popleft())
                                    subjects15.extendleft(reversed(tmp34))
                        subjects15.appendleft(tmp30)
                    subjects.appendleft(tmp14)
            if len(subjects) >= 1:
                tmp37 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i3.1.2.1', tmp37)
                except ValueError:
                    pass
                else:
                    pass
                    # State 53201
                    if len(subjects) == 0:
                        pass
                        # 3: RFx**p
                subjects.appendleft(tmp37)
            if len(subjects) >= 1 and isinstance(subjects[0], Mul):
                tmp39 = subjects.popleft()
                associative1 = tmp39
                associative_type1 = type(tmp39)
                subjects40 = deque(tmp39._args)
                matcher = CommutativeMatcher20319.get()
                tmp41 = subjects40
                subjects40 = []
                for s in tmp41:
                    matcher.add_subject(s)
                for pattern_index, subst2 in matcher.match(tmp41, subst1):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 20356
                        if len(subjects) == 0:
                            pass
                            # 0: (d*(e + x*f)**p)**q
                subjects.appendleft(tmp39)
            if len(subjects) >= 1 and isinstance(subjects[0], Add):
                tmp42 = subjects.popleft()
                associative1 = tmp42
                associative_type1 = type(tmp42)
                subjects43 = deque(tmp42._args)
                matcher = CommutativeMatcher50770.get()
                tmp44 = subjects43
                subjects43 = []
                for s in tmp44:
                    matcher.add_subject(s)
                for pattern_index, subst2 in matcher.match(tmp44, subst1):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 50783
                        if len(subjects) == 0:
                            pass
                            # 1: (d + e*x**2)**p
                    if pattern_index == 1:
                        pass
                        # State 53028
                        if len(subjects) == 0:
                            pass
                            # 2: (d + e/(f + x*g))**p
                subjects.appendleft(tmp42)
        if len(subjects) >= 1 and isinstance(subjects[0], Pow):
            tmp45 = subjects.popleft()
            subjects46 = deque(tmp45._args)
            # State 20357
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i3.1.2.2.0', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 20358
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i3.1.2.2.2', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 20359
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i3.1.2.2.2.0', S(0))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 20360
                        subst4 = Substitution(subst3)
                        try:
                            subst4.try_add_variable('i3.1.2.2.2.1.0_1', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 20361
                            if len(subjects46) >= 1:
                                tmp51 = subjects46.popleft()
                                subst5 = Substitution(subst4)
                                try:
                                    subst5.try_add_variable('i3.1.2.2.2.1.0', tmp51)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 20362
                                    subst6 = Substitution(subst5)
                                    try:
                                        subst6.try_add_variable('i3.1.2.2', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 20363
                                        if len(subjects46) == 0:
                                            pass
                                            # State 20364
                                            if len(subjects) == 0:
                                                pass
                                                # 0: (d*(e + x*f)**p)**q
                                    if len(subjects46) >= 1:
                                        tmp54 = subjects46.popleft()
                                        subst6 = Substitution(subst5)
                                        try:
                                            subst6.try_add_variable('i3.1.2.2', tmp54)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 20363
                                            if len(subjects46) == 0:
                                                pass
                                                # State 20364
                                                if len(subjects) == 0:
                                                    pass
                                                    # 0: (d*(e + x*f)**p)**q
                                        subjects46.appendleft(tmp54)
                                subjects46.appendleft(tmp51)
                        if len(subjects46) >= 1 and isinstance(subjects46[0], Mul):
                            tmp56 = subjects46.popleft()
                            associative1 = tmp56
                            associative_type1 = type(tmp56)
                            subjects57 = deque(tmp56._args)
                            matcher = CommutativeMatcher20366.get()
                            tmp58 = subjects57
                            subjects57 = []
                            for s in tmp58:
                                matcher.add_subject(s)
                            for pattern_index, subst4 in matcher.match(tmp58, subst3):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 20367
                                    subst5 = Substitution(subst4)
                                    try:
                                        subst5.try_add_variable('i3.1.2.2', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 20368
                                        if len(subjects46) == 0:
                                            pass
                                            # State 20369
                                            if len(subjects) == 0:
                                                pass
                                                # 0: (d*(e + x*f)**p)**q
                                    if len(subjects46) >= 1:
                                        tmp60 = []
                                        tmp60.append(subjects46.popleft())
                                        while True:
                                            if len(tmp60) > 1:
                                                tmp61 = create_operation_expression(associative1, tmp60)
                                            elif len(tmp60) == 1:
                                                tmp61 = tmp60[0]
                                            else:
                                                assert False, "Unreachable"
                                            subst5 = Substitution(subst4)
                                            try:
                                                subst5.try_add_variable('i3.1.2.2', tmp61)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 20368
                                                if len(subjects46) == 0:
                                                    pass
                                                    # State 20369
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 0: (d*(e + x*f)**p)**q
                                            if len(subjects46) == 0:
                                                break
                                            tmp60.append(subjects46.popleft())
                                        subjects46.extendleft(reversed(tmp60))
                            subjects46.appendleft(tmp56)
                    if len(subjects46) >= 1 and isinstance(subjects46[0], Add):
                        tmp63 = subjects46.popleft()
                        associative1 = tmp63
                        associative_type1 = type(tmp63)
                        subjects64 = deque(tmp63._args)
                        matcher = CommutativeMatcher20371.get()
                        tmp65 = subjects64
                        subjects64 = []
                        for s in tmp65:
                            matcher.add_subject(s)
                        for pattern_index, subst3 in matcher.match(tmp65, subst2):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 20377
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i3.1.2.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 20378
                                    if len(subjects46) == 0:
                                        pass
                                        # State 20379
                                        if len(subjects) == 0:
                                            pass
                                            # 0: (d*(e + x*f)**p)**q
                                if len(subjects46) >= 1:
                                    tmp67 = []
                                    tmp67.append(subjects46.popleft())
                                    while True:
                                        if len(tmp67) > 1:
                                            tmp68 = create_operation_expression(associative1, tmp67)
                                        elif len(tmp67) == 1:
                                            tmp68 = tmp67[0]
                                        else:
                                            assert False, "Unreachable"
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i3.1.2.2', tmp68)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 20378
                                            if len(subjects46) == 0:
                                                pass
                                                # State 20379
                                                if len(subjects) == 0:
                                                    pass
                                                    # 0: (d*(e + x*f)**p)**q
                                        if len(subjects46) == 0:
                                            break
                                        tmp67.append(subjects46.popleft())
                                    subjects46.extendleft(reversed(tmp67))
                        subjects46.appendleft(tmp63)
                if len(subjects46) >= 1 and isinstance(subjects46[0], Pow):
                    tmp70 = subjects46.popleft()
                    subjects71 = deque(tmp70._args)
                    # State 20380
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i3.1.2.2.2.0', S(0))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 20381
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i3.1.2.2.2.1.0_1', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 20382
                            if len(subjects71) >= 1:
                                tmp74 = subjects71.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i3.1.2.2.2.1.0', tmp74)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 20383
                                    subst5 = Substitution(subst4)
                                    try:
                                        subst5.try_add_variable('i3.1.2.2.2', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 20384
                                        if len(subjects71) == 0:
                                            pass
                                            # State 20385
                                            subst6 = Substitution(subst5)
                                            try:
                                                subst6.try_add_variable('i3.1.2.2', 1)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 20386
                                                if len(subjects46) == 0:
                                                    pass
                                                    # State 20387
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 0: (d*(e + x*f)**p)**q
                                            if len(subjects46) >= 1:
                                                tmp78 = subjects46.popleft()
                                                subst6 = Substitution(subst5)
                                                try:
                                                    subst6.try_add_variable('i3.1.2.2', tmp78)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 20386
                                                    if len(subjects46) == 0:
                                                        pass
                                                        # State 20387
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 0: (d*(e + x*f)**p)**q
                                                subjects46.appendleft(tmp78)
                                    if len(subjects71) >= 1:
                                        tmp80 = subjects71.popleft()
                                        subst5 = Substitution(subst4)
                                        try:
                                            subst5.try_add_variable('i3.1.2.2.2', tmp80)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 20384
                                            if len(subjects71) == 0:
                                                pass
                                                # State 20385
                                                subst6 = Substitution(subst5)
                                                try:
                                                    subst6.try_add_variable('i3.1.2.2', 1)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 20386
                                                    if len(subjects46) == 0:
                                                        pass
                                                        # State 20387
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 0: (d*(e + x*f)**p)**q
                                                if len(subjects46) >= 1:
                                                    tmp83 = subjects46.popleft()
                                                    subst6 = Substitution(subst5)
                                                    try:
                                                        subst6.try_add_variable('i3.1.2.2', tmp83)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 20386
                                                        if len(subjects46) == 0:
                                                            pass
                                                            # State 20387
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 0: (d*(e + x*f)**p)**q
                                                    subjects46.appendleft(tmp83)
                                        subjects71.appendleft(tmp80)
                                subjects71.appendleft(tmp74)
                        if len(subjects71) >= 1 and isinstance(subjects71[0], Mul):
                            tmp85 = subjects71.popleft()
                            associative1 = tmp85
                            associative_type1 = type(tmp85)
                            subjects86 = deque(tmp85._args)
                            matcher = CommutativeMatcher20389.get()
                            tmp87 = subjects86
                            subjects86 = []
                            for s in tmp87:
                                matcher.add_subject(s)
                            for pattern_index, subst3 in matcher.match(tmp87, subst2):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 20390
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i3.1.2.2.2', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 20391
                                        if len(subjects71) == 0:
                                            pass
                                            # State 20392
                                            subst5 = Substitution(subst4)
                                            try:
                                                subst5.try_add_variable('i3.1.2.2', 1)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 20393
                                                if len(subjects46) == 0:
                                                    pass
                                                    # State 20394
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 0: (d*(e + x*f)**p)**q
                                            if len(subjects46) >= 1:
                                                tmp90 = subjects46.popleft()
                                                subst5 = Substitution(subst4)
                                                try:
                                                    subst5.try_add_variable('i3.1.2.2', tmp90)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 20393
                                                    if len(subjects46) == 0:
                                                        pass
                                                        # State 20394
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 0: (d*(e + x*f)**p)**q
                                                subjects46.appendleft(tmp90)
                                    if len(subjects71) >= 1:
                                        tmp92 = []
                                        tmp92.append(subjects71.popleft())
                                        while True:
                                            if len(tmp92) > 1:
                                                tmp93 = create_operation_expression(associative1, tmp92)
                                            elif len(tmp92) == 1:
                                                tmp93 = tmp92[0]
                                            else:
                                                assert False, "Unreachable"
                                            subst4 = Substitution(subst3)
                                            try:
                                                subst4.try_add_variable('i3.1.2.2.2', tmp93)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 20391
                                                if len(subjects71) == 0:
                                                    pass
                                                    # State 20392
                                                    subst5 = Substitution(subst4)
                                                    try:
                                                        subst5.try_add_variable('i3.1.2.2', 1)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 20393
                                                        if len(subjects46) == 0:
                                                            pass
                                                            # State 20394
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 0: (d*(e + x*f)**p)**q
                                                    if len(subjects46) >= 1:
                                                        tmp96 = subjects46.popleft()
                                                        subst5 = Substitution(subst4)
                                                        try:
                                                            subst5.try_add_variable('i3.1.2.2', tmp96)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            # State 20393
                                                            if len(subjects46) == 0:
                                                                pass
                                                                # State 20394
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 0: (d*(e + x*f)**p)**q
                                                        subjects46.appendleft(tmp96)
                                            if len(subjects71) == 0:
                                                break
                                            tmp92.append(subjects71.popleft())
                                        subjects71.extendleft(reversed(tmp92))
                            subjects71.appendleft(tmp85)
                    if len(subjects71) >= 1 and isinstance(subjects71[0], Add):
                        tmp98 = subjects71.popleft()
                        associative1 = tmp98
                        associative_type1 = type(tmp98)
                        subjects99 = deque(tmp98._args)
                        matcher = CommutativeMatcher20396.get()
                        tmp100 = subjects99
                        subjects99 = []
                        for s in tmp100:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp100, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 20402
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i3.1.2.2.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 20403
                                    if len(subjects71) == 0:
                                        pass
                                        # State 20404
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i3.1.2.2', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 20405
                                            if len(subjects46) == 0:
                                                pass
                                                # State 20406
                                                if len(subjects) == 0:
                                                    pass
                                                    # 0: (d*(e + x*f)**p)**q
                                        if len(subjects46) >= 1:
                                            tmp103 = subjects46.popleft()
                                            subst4 = Substitution(subst3)
                                            try:
                                                subst4.try_add_variable('i3.1.2.2', tmp103)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 20405
                                                if len(subjects46) == 0:
                                                    pass
                                                    # State 20406
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 0: (d*(e + x*f)**p)**q
                                            subjects46.appendleft(tmp103)
                                if len(subjects71) >= 1:
                                    tmp105 = []
                                    tmp105.append(subjects71.popleft())
                                    while True:
                                        if len(tmp105) > 1:
                                            tmp106 = create_operation_expression(associative1, tmp105)
                                        elif len(tmp105) == 1:
                                            tmp106 = tmp105[0]
                                        else:
                                            assert False, "Unreachable"
                                        subst3 = Substitution(subst2)
                                        try:
                                            subst3.try_add_variable('i3.1.2.2.2', tmp106)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 20403
                                            if len(subjects71) == 0:
                                                pass
                                                # State 20404
                                                subst4 = Substitution(subst3)
                                                try:
                                                    subst4.try_add_variable('i3.1.2.2', 1)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 20405
                                                    if len(subjects46) == 0:
                                                        pass
                                                        # State 20406
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 0: (d*(e + x*f)**p)**q
                                                if len(subjects46) >= 1:
                                                    tmp109 = subjects46.popleft()
                                                    subst4 = Substitution(subst3)
                                                    try:
                                                        subst4.try_add_variable('i3.1.2.2', tmp109)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 20405
                                                        if len(subjects46) == 0:
                                                            pass
                                                            # State 20406
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 0: (d*(e + x*f)**p)**q
                                                    subjects46.appendleft(tmp109)
                                        if len(subjects71) == 0:
                                            break
                                        tmp105.append(subjects71.popleft())
                                    subjects71.extendleft(reversed(tmp105))
                        subjects71.appendleft(tmp98)
                    subjects46.appendleft(tmp70)
            if len(subjects46) >= 1:
                tmp111 = subjects46.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i3.1.2.1', tmp111)
                except ValueError:
                    pass
                else:
                    pass
                    # State 53202
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i3.1.2.2', 1)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 53203
                        if len(subjects46) == 0:
                            pass
                            # State 53204
                            if len(subjects) == 0:
                                pass
                                # 3: RFx**p
                    if len(subjects46) >= 1:
                        tmp114 = subjects46.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i3.1.2.2', tmp114)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 53203
                            if len(subjects46) == 0:
                                pass
                                # State 53204
                                if len(subjects) == 0:
                                    pass
                                    # 3: RFx**p
                        subjects46.appendleft(tmp114)
                subjects46.appendleft(tmp111)
            if len(subjects46) >= 1 and isinstance(subjects46[0], Mul):
                tmp116 = subjects46.popleft()
                associative1 = tmp116
                associative_type1 = type(tmp116)
                subjects117 = deque(tmp116._args)
                matcher = CommutativeMatcher20408.get()
                tmp118 = subjects117
                subjects117 = []
                for s in tmp118:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp118, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 20445
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i3.1.2.2', 1)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 20446
                            if len(subjects46) == 0:
                                pass
                                # State 20447
                                if len(subjects) == 0:
                                    pass
                                    # 0: (d*(e + x*f)**p)**q
                        if len(subjects46) >= 1:
                            tmp120 = []
                            tmp120.append(subjects46.popleft())
                            while True:
                                if len(tmp120) > 1:
                                    tmp121 = create_operation_expression(associative1, tmp120)
                                elif len(tmp120) == 1:
                                    tmp121 = tmp120[0]
                                else:
                                    assert False, "Unreachable"
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i3.1.2.2', tmp121)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 20446
                                    if len(subjects46) == 0:
                                        pass
                                        # State 20447
                                        if len(subjects) == 0:
                                            pass
                                            # 0: (d*(e + x*f)**p)**q
                                if len(subjects46) == 0:
                                    break
                                tmp120.append(subjects46.popleft())
                            subjects46.extendleft(reversed(tmp120))
                subjects46.appendleft(tmp116)
            if len(subjects46) >= 1 and isinstance(subjects46[0], Add):
                tmp123 = subjects46.popleft()
                associative1 = tmp123
                associative_type1 = type(tmp123)
                subjects124 = deque(tmp123._args)
                matcher = CommutativeMatcher50785.get()
                tmp125 = subjects124
                subjects124 = []
                for s in tmp125:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp125, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 50798
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i3.1.2.2', 1)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 50799
                            if len(subjects46) == 0:
                                pass
                                # State 50800
                                if len(subjects) == 0:
                                    pass
                                    # 1: (d + e*x**2)**p
                        if len(subjects46) >= 1:
                            tmp127 = []
                            tmp127.append(subjects46.popleft())
                            while True:
                                if len(tmp127) > 1:
                                    tmp128 = create_operation_expression(associative1, tmp127)
                                elif len(tmp127) == 1:
                                    tmp128 = tmp127[0]
                                else:
                                    assert False, "Unreachable"
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i3.1.2.2', tmp128)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 50799
                                    if len(subjects46) == 0:
                                        pass
                                        # State 50800
                                        if len(subjects) == 0:
                                            pass
                                            # 1: (d + e*x**2)**p
                                if len(subjects46) == 0:
                                    break
                                tmp127.append(subjects46.popleft())
                            subjects46.extendleft(reversed(tmp127))
                    if pattern_index == 1:
                        pass
                        # State 53070
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i3.1.2.2', 1)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 53071
                            if len(subjects46) == 0:
                                pass
                                # State 53072
                                if len(subjects) == 0:
                                    pass
                                    # 2: (d + e/(f + x*g))**p
                        if len(subjects46) >= 1:
                            tmp131 = []
                            tmp131.append(subjects46.popleft())
                            while True:
                                if len(tmp131) > 1:
                                    tmp132 = create_operation_expression(associative1, tmp131)
                                elif len(tmp131) == 1:
                                    tmp132 = tmp131[0]
                                else:
                                    assert False, "Unreachable"
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i3.1.2.2', tmp132)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 53071
                                    if len(subjects46) == 0:
                                        pass
                                        # State 53072
                                        if len(subjects) == 0:
                                            pass
                                            # 2: (d + e/(f + x*g))**p
                                if len(subjects46) == 0:
                                    break
                                tmp131.append(subjects46.popleft())
                            subjects46.extendleft(reversed(tmp131))
                subjects46.appendleft(tmp123)
            subjects.appendleft(tmp45)
        return
        yield


from matchpy.utils import VariableWithCount
from matchpy.matching.many_to_one import CommutativeMatcher
from multiset import Multiset
from collections import deque
