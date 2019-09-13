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

class CommutativeMatcher37996(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({0: 1}), [
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
        if CommutativeMatcher37996._instance is None:
            CommutativeMatcher37996._instance = CommutativeMatcher37996()
        return CommutativeMatcher37996._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 37995
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.2.2', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 37997
            subst2 = Substitution(subst1)
            try:
                subst2.try_add_variable('i2.2.1.2.2.0', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 37998
                subst3 = Substitution(subst2)
                try:
                    subst3.try_add_variable('i2.2.1.2.2.2', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 37999
                    subst4 = Substitution(subst3)
                    try:
                        subst4.try_add_variable('i2.2.1.2.2.2.0', S(0))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 38000
                        subst5 = Substitution(subst4)
                        try:
                            subst5.try_add_variable('i2.2.1.2.2.2.1.0', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 38001
                            if len(subjects) >= 1 and isinstance(subjects[0], Pow):
                                tmp6 = subjects.popleft()
                                subjects7 = deque(tmp6._args)
                                # State 38002
                                if len(subjects7) >= 1:
                                    tmp8 = subjects7.popleft()
                                    subst6 = Substitution(subst5)
                                    try:
                                        subst6.try_add_variable('i2.2.1.1', tmp8)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 38003
                                        if len(subjects7) >= 1:
                                            tmp10 = subjects7.popleft()
                                            subst7 = Substitution(subst6)
                                            try:
                                                subst7.try_add_variable('i2.2.1.2', tmp10)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 38004
                                                if len(subjects7) == 0:
                                                    pass
                                                    # State 38005
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 0: (d*(x**j*f + e)**p)**q
                                            subjects7.appendleft(tmp10)
                                    subjects7.appendleft(tmp8)
                                subjects.appendleft(tmp6)
                        if len(subjects) >= 1 and isinstance(subjects[0], Mul):
                            tmp12 = subjects.popleft()
                            associative1 = tmp12
                            associative_type1 = type(tmp12)
                            subjects13 = deque(tmp12._args)
                            matcher = CommutativeMatcher38007.get()
                            tmp14 = subjects13
                            subjects13 = []
                            for s in tmp14:
                                matcher.add_subject(s)
                            for pattern_index, subst5 in matcher.match(tmp14, subst4):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 38012
                                    if len(subjects) == 0:
                                        pass
                                        # 0: (d*(x**j*f + e)**p)**q
                            subjects.appendleft(tmp12)
                    if len(subjects) >= 1 and isinstance(subjects[0], Add):
                        tmp15 = subjects.popleft()
                        associative1 = tmp15
                        associative_type1 = type(tmp15)
                        subjects16 = deque(tmp15._args)
                        matcher = CommutativeMatcher38014.get()
                        tmp17 = subjects16
                        subjects16 = []
                        for s in tmp17:
                            matcher.add_subject(s)
                        for pattern_index, subst4 in matcher.match(tmp17, subst3):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 38027
                                if len(subjects) == 0:
                                    pass
                                    # 0: (d*(x**j*f + e)**p)**q
                        subjects.appendleft(tmp15)
                if len(subjects) >= 1 and isinstance(subjects[0], Pow):
                    tmp18 = subjects.popleft()
                    subjects19 = deque(tmp18._args)
                    # State 38028
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.2.1.2.2.2.0', S(0))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 38029
                        subst4 = Substitution(subst3)
                        try:
                            subst4.try_add_variable('i2.2.1.2.2.2.1.0', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 38030
                            if len(subjects19) >= 1 and isinstance(subjects19[0], Pow):
                                tmp22 = subjects19.popleft()
                                subjects23 = deque(tmp22._args)
                                # State 38031
                                if len(subjects23) >= 1:
                                    tmp24 = subjects23.popleft()
                                    subst5 = Substitution(subst4)
                                    try:
                                        subst5.try_add_variable('i2.2.1.1', tmp24)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 38032
                                        if len(subjects23) >= 1:
                                            tmp26 = subjects23.popleft()
                                            subst6 = Substitution(subst5)
                                            try:
                                                subst6.try_add_variable('i2.2.1.2', tmp26)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 38033
                                                if len(subjects23) == 0:
                                                    pass
                                                    # State 38034
                                                    subst7 = Substitution(subst6)
                                                    try:
                                                        subst7.try_add_variable('i2.2.1.2.2.2', 1)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 38035
                                                        if len(subjects19) == 0:
                                                            pass
                                                            # State 38036
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 0: (d*(x**j*f + e)**p)**q
                                                    if len(subjects19) >= 1:
                                                        tmp29 = subjects19.popleft()
                                                        subst7 = Substitution(subst6)
                                                        try:
                                                            subst7.try_add_variable('i2.2.1.2.2.2', tmp29)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            # State 38035
                                                            if len(subjects19) == 0:
                                                                pass
                                                                # State 38036
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 0: (d*(x**j*f + e)**p)**q
                                                        subjects19.appendleft(tmp29)
                                            subjects23.appendleft(tmp26)
                                    subjects23.appendleft(tmp24)
                                subjects19.appendleft(tmp22)
                        if len(subjects19) >= 1 and isinstance(subjects19[0], Mul):
                            tmp31 = subjects19.popleft()
                            associative1 = tmp31
                            associative_type1 = type(tmp31)
                            subjects32 = deque(tmp31._args)
                            matcher = CommutativeMatcher38038.get()
                            tmp33 = subjects32
                            subjects32 = []
                            for s in tmp33:
                                matcher.add_subject(s)
                            for pattern_index, subst4 in matcher.match(tmp33, subst3):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 38043
                                    subst5 = Substitution(subst4)
                                    try:
                                        subst5.try_add_variable('i2.2.1.2.2.2', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 38044
                                        if len(subjects19) == 0:
                                            pass
                                            # State 38045
                                            if len(subjects) == 0:
                                                pass
                                                # 0: (d*(x**j*f + e)**p)**q
                                    if len(subjects19) >= 1:
                                        tmp35 = []
                                        tmp35.append(subjects19.popleft())
                                        while True:
                                            if len(tmp35) > 1:
                                                tmp36 = create_operation_expression(associative1, tmp35)
                                            elif len(tmp35) == 1:
                                                tmp36 = tmp35[0]
                                            else:
                                                assert False, "Unreachable"
                                            subst5 = Substitution(subst4)
                                            try:
                                                subst5.try_add_variable('i2.2.1.2.2.2', tmp36)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 38044
                                                if len(subjects19) == 0:
                                                    pass
                                                    # State 38045
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 0: (d*(x**j*f + e)**p)**q
                                            if len(subjects19) == 0:
                                                break
                                            tmp35.append(subjects19.popleft())
                                        subjects19.extendleft(reversed(tmp35))
                            subjects19.appendleft(tmp31)
                    if len(subjects19) >= 1 and isinstance(subjects19[0], Add):
                        tmp38 = subjects19.popleft()
                        associative1 = tmp38
                        associative_type1 = type(tmp38)
                        subjects39 = deque(tmp38._args)
                        matcher = CommutativeMatcher38047.get()
                        tmp40 = subjects39
                        subjects39 = []
                        for s in tmp40:
                            matcher.add_subject(s)
                        for pattern_index, subst3 in matcher.match(tmp40, subst2):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 38060
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.2.1.2.2.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 38061
                                    if len(subjects19) == 0:
                                        pass
                                        # State 38062
                                        if len(subjects) == 0:
                                            pass
                                            # 0: (d*(x**j*f + e)**p)**q
                                if len(subjects19) >= 1:
                                    tmp42 = []
                                    tmp42.append(subjects19.popleft())
                                    while True:
                                        if len(tmp42) > 1:
                                            tmp43 = create_operation_expression(associative1, tmp42)
                                        elif len(tmp42) == 1:
                                            tmp43 = tmp42[0]
                                        else:
                                            assert False, "Unreachable"
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.2.1.2.2.2', tmp43)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 38061
                                            if len(subjects19) == 0:
                                                pass
                                                # State 38062
                                                if len(subjects) == 0:
                                                    pass
                                                    # 0: (d*(x**j*f + e)**p)**q
                                        if len(subjects19) == 0:
                                            break
                                        tmp42.append(subjects19.popleft())
                                    subjects19.extendleft(reversed(tmp42))
                        subjects19.appendleft(tmp38)
                    subjects.appendleft(tmp18)
            if len(subjects) >= 1 and isinstance(subjects[0], Mul):
                tmp45 = subjects.popleft()
                associative1 = tmp45
                associative_type1 = type(tmp45)
                subjects46 = deque(tmp45._args)
                matcher = CommutativeMatcher38064.get()
                tmp47 = subjects46
                subjects46 = []
                for s in tmp47:
                    matcher.add_subject(s)
                for pattern_index, subst2 in matcher.match(tmp47, subst1):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 38129
                        if len(subjects) == 0:
                            pass
                            # 0: (d*(x**j*f + e)**p)**q
                subjects.appendleft(tmp45)
        if len(subjects) >= 1 and isinstance(subjects[0], Pow):
            tmp48 = subjects.popleft()
            subjects49 = deque(tmp48._args)
            # State 38130
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.2.0', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 38131
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.2.2', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 38132
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.2.1.2.2.2.0', S(0))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 38133
                        subst4 = Substitution(subst3)
                        try:
                            subst4.try_add_variable('i2.2.1.2.2.2.1.0', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 38134
                            if len(subjects49) >= 1 and isinstance(subjects49[0], Pow):
                                tmp54 = subjects49.popleft()
                                subjects55 = deque(tmp54._args)
                                # State 38135
                                if len(subjects55) >= 1:
                                    tmp56 = subjects55.popleft()
                                    subst5 = Substitution(subst4)
                                    try:
                                        subst5.try_add_variable('i2.2.1.1', tmp56)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 38136
                                        if len(subjects55) >= 1:
                                            tmp58 = subjects55.popleft()
                                            subst6 = Substitution(subst5)
                                            try:
                                                subst6.try_add_variable('i2.2.1.2', tmp58)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 38137
                                                if len(subjects55) == 0:
                                                    pass
                                                    # State 38138
                                                    subst7 = Substitution(subst6)
                                                    try:
                                                        subst7.try_add_variable('i2.2.1.2.2', 1)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 38139
                                                        if len(subjects49) == 0:
                                                            pass
                                                            # State 38140
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 0: (d*(x**j*f + e)**p)**q
                                                    if len(subjects49) >= 1:
                                                        tmp61 = subjects49.popleft()
                                                        subst7 = Substitution(subst6)
                                                        try:
                                                            subst7.try_add_variable('i2.2.1.2.2', tmp61)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            # State 38139
                                                            if len(subjects49) == 0:
                                                                pass
                                                                # State 38140
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 0: (d*(x**j*f + e)**p)**q
                                                        subjects49.appendleft(tmp61)
                                            subjects55.appendleft(tmp58)
                                    subjects55.appendleft(tmp56)
                                subjects49.appendleft(tmp54)
                        if len(subjects49) >= 1 and isinstance(subjects49[0], Mul):
                            tmp63 = subjects49.popleft()
                            associative1 = tmp63
                            associative_type1 = type(tmp63)
                            subjects64 = deque(tmp63._args)
                            matcher = CommutativeMatcher38142.get()
                            tmp65 = subjects64
                            subjects64 = []
                            for s in tmp65:
                                matcher.add_subject(s)
                            for pattern_index, subst4 in matcher.match(tmp65, subst3):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 38147
                                    subst5 = Substitution(subst4)
                                    try:
                                        subst5.try_add_variable('i2.2.1.2.2', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 38148
                                        if len(subjects49) == 0:
                                            pass
                                            # State 38149
                                            if len(subjects) == 0:
                                                pass
                                                # 0: (d*(x**j*f + e)**p)**q
                                    if len(subjects49) >= 1:
                                        tmp67 = []
                                        tmp67.append(subjects49.popleft())
                                        while True:
                                            if len(tmp67) > 1:
                                                tmp68 = create_operation_expression(associative1, tmp67)
                                            elif len(tmp67) == 1:
                                                tmp68 = tmp67[0]
                                            else:
                                                assert False, "Unreachable"
                                            subst5 = Substitution(subst4)
                                            try:
                                                subst5.try_add_variable('i2.2.1.2.2', tmp68)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 38148
                                                if len(subjects49) == 0:
                                                    pass
                                                    # State 38149
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 0: (d*(x**j*f + e)**p)**q
                                            if len(subjects49) == 0:
                                                break
                                            tmp67.append(subjects49.popleft())
                                        subjects49.extendleft(reversed(tmp67))
                            subjects49.appendleft(tmp63)
                    if len(subjects49) >= 1 and isinstance(subjects49[0], Add):
                        tmp70 = subjects49.popleft()
                        associative1 = tmp70
                        associative_type1 = type(tmp70)
                        subjects71 = deque(tmp70._args)
                        matcher = CommutativeMatcher38151.get()
                        tmp72 = subjects71
                        subjects71 = []
                        for s in tmp72:
                            matcher.add_subject(s)
                        for pattern_index, subst3 in matcher.match(tmp72, subst2):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 38164
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.2.1.2.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 38165
                                    if len(subjects49) == 0:
                                        pass
                                        # State 38166
                                        if len(subjects) == 0:
                                            pass
                                            # 0: (d*(x**j*f + e)**p)**q
                                if len(subjects49) >= 1:
                                    tmp74 = []
                                    tmp74.append(subjects49.popleft())
                                    while True:
                                        if len(tmp74) > 1:
                                            tmp75 = create_operation_expression(associative1, tmp74)
                                        elif len(tmp74) == 1:
                                            tmp75 = tmp74[0]
                                        else:
                                            assert False, "Unreachable"
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.2.1.2.2', tmp75)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 38165
                                            if len(subjects49) == 0:
                                                pass
                                                # State 38166
                                                if len(subjects) == 0:
                                                    pass
                                                    # 0: (d*(x**j*f + e)**p)**q
                                        if len(subjects49) == 0:
                                            break
                                        tmp74.append(subjects49.popleft())
                                    subjects49.extendleft(reversed(tmp74))
                        subjects49.appendleft(tmp70)
                if len(subjects49) >= 1 and isinstance(subjects49[0], Pow):
                    tmp77 = subjects49.popleft()
                    subjects78 = deque(tmp77._args)
                    # State 38167
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.2.2.2.0', S(0))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 38168
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.2.2.2.1.0', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 38169
                            if len(subjects78) >= 1 and isinstance(subjects78[0], Pow):
                                tmp81 = subjects78.popleft()
                                subjects82 = deque(tmp81._args)
                                # State 38170
                                if len(subjects82) >= 1:
                                    tmp83 = subjects82.popleft()
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i2.2.1.1', tmp83)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 38171
                                        if len(subjects82) >= 1:
                                            tmp85 = subjects82.popleft()
                                            subst5 = Substitution(subst4)
                                            try:
                                                subst5.try_add_variable('i2.2.1.2', tmp85)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 38172
                                                if len(subjects82) == 0:
                                                    pass
                                                    # State 38173
                                                    subst6 = Substitution(subst5)
                                                    try:
                                                        subst6.try_add_variable('i2.2.1.2.2.2', 1)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 38174
                                                        if len(subjects78) == 0:
                                                            pass
                                                            # State 38175
                                                            subst7 = Substitution(subst6)
                                                            try:
                                                                subst7.try_add_variable('i2.2.1.2.2', 1)
                                                            except ValueError:
                                                                pass
                                                            else:
                                                                pass
                                                                # State 38176
                                                                if len(subjects49) == 0:
                                                                    pass
                                                                    # State 38177
                                                                    if len(subjects) == 0:
                                                                        pass
                                                                        # 0: (d*(x**j*f + e)**p)**q
                                                            if len(subjects49) >= 1:
                                                                tmp89 = subjects49.popleft()
                                                                subst7 = Substitution(subst6)
                                                                try:
                                                                    subst7.try_add_variable('i2.2.1.2.2', tmp89)
                                                                except ValueError:
                                                                    pass
                                                                else:
                                                                    pass
                                                                    # State 38176
                                                                    if len(subjects49) == 0:
                                                                        pass
                                                                        # State 38177
                                                                        if len(subjects) == 0:
                                                                            pass
                                                                            # 0: (d*(x**j*f + e)**p)**q
                                                                subjects49.appendleft(tmp89)
                                                    if len(subjects78) >= 1:
                                                        tmp91 = subjects78.popleft()
                                                        subst6 = Substitution(subst5)
                                                        try:
                                                            subst6.try_add_variable('i2.2.1.2.2.2', tmp91)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            # State 38174
                                                            if len(subjects78) == 0:
                                                                pass
                                                                # State 38175
                                                                subst7 = Substitution(subst6)
                                                                try:
                                                                    subst7.try_add_variable('i2.2.1.2.2', 1)
                                                                except ValueError:
                                                                    pass
                                                                else:
                                                                    pass
                                                                    # State 38176
                                                                    if len(subjects49) == 0:
                                                                        pass
                                                                        # State 38177
                                                                        if len(subjects) == 0:
                                                                            pass
                                                                            # 0: (d*(x**j*f + e)**p)**q
                                                                if len(subjects49) >= 1:
                                                                    tmp94 = subjects49.popleft()
                                                                    subst7 = Substitution(subst6)
                                                                    try:
                                                                        subst7.try_add_variable('i2.2.1.2.2', tmp94)
                                                                    except ValueError:
                                                                        pass
                                                                    else:
                                                                        pass
                                                                        # State 38176
                                                                        if len(subjects49) == 0:
                                                                            pass
                                                                            # State 38177
                                                                            if len(subjects) == 0:
                                                                                pass
                                                                                # 0: (d*(x**j*f + e)**p)**q
                                                                    subjects49.appendleft(tmp94)
                                                        subjects78.appendleft(tmp91)
                                            subjects82.appendleft(tmp85)
                                    subjects82.appendleft(tmp83)
                                subjects78.appendleft(tmp81)
                        if len(subjects78) >= 1 and isinstance(subjects78[0], Mul):
                            tmp96 = subjects78.popleft()
                            associative1 = tmp96
                            associative_type1 = type(tmp96)
                            subjects97 = deque(tmp96._args)
                            matcher = CommutativeMatcher38179.get()
                            tmp98 = subjects97
                            subjects97 = []
                            for s in tmp98:
                                matcher.add_subject(s)
                            for pattern_index, subst3 in matcher.match(tmp98, subst2):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 38184
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i2.2.1.2.2.2', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 38185
                                        if len(subjects78) == 0:
                                            pass
                                            # State 38186
                                            subst5 = Substitution(subst4)
                                            try:
                                                subst5.try_add_variable('i2.2.1.2.2', 1)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 38187
                                                if len(subjects49) == 0:
                                                    pass
                                                    # State 38188
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 0: (d*(x**j*f + e)**p)**q
                                            if len(subjects49) >= 1:
                                                tmp101 = subjects49.popleft()
                                                subst5 = Substitution(subst4)
                                                try:
                                                    subst5.try_add_variable('i2.2.1.2.2', tmp101)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 38187
                                                    if len(subjects49) == 0:
                                                        pass
                                                        # State 38188
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 0: (d*(x**j*f + e)**p)**q
                                                subjects49.appendleft(tmp101)
                                    if len(subjects78) >= 1:
                                        tmp103 = []
                                        tmp103.append(subjects78.popleft())
                                        while True:
                                            if len(tmp103) > 1:
                                                tmp104 = create_operation_expression(associative1, tmp103)
                                            elif len(tmp103) == 1:
                                                tmp104 = tmp103[0]
                                            else:
                                                assert False, "Unreachable"
                                            subst4 = Substitution(subst3)
                                            try:
                                                subst4.try_add_variable('i2.2.1.2.2.2', tmp104)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 38185
                                                if len(subjects78) == 0:
                                                    pass
                                                    # State 38186
                                                    subst5 = Substitution(subst4)
                                                    try:
                                                        subst5.try_add_variable('i2.2.1.2.2', 1)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 38187
                                                        if len(subjects49) == 0:
                                                            pass
                                                            # State 38188
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 0: (d*(x**j*f + e)**p)**q
                                                    if len(subjects49) >= 1:
                                                        tmp107 = subjects49.popleft()
                                                        subst5 = Substitution(subst4)
                                                        try:
                                                            subst5.try_add_variable('i2.2.1.2.2', tmp107)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            # State 38187
                                                            if len(subjects49) == 0:
                                                                pass
                                                                # State 38188
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 0: (d*(x**j*f + e)**p)**q
                                                        subjects49.appendleft(tmp107)
                                            if len(subjects78) == 0:
                                                break
                                            tmp103.append(subjects78.popleft())
                                        subjects78.extendleft(reversed(tmp103))
                            subjects78.appendleft(tmp96)
                    if len(subjects78) >= 1 and isinstance(subjects78[0], Add):
                        tmp109 = subjects78.popleft()
                        associative1 = tmp109
                        associative_type1 = type(tmp109)
                        subjects110 = deque(tmp109._args)
                        matcher = CommutativeMatcher38190.get()
                        tmp111 = subjects110
                        subjects110 = []
                        for s in tmp111:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp111, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 38203
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i2.2.1.2.2.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 38204
                                    if len(subjects78) == 0:
                                        pass
                                        # State 38205
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.2.1.2.2', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 38206
                                            if len(subjects49) == 0:
                                                pass
                                                # State 38207
                                                if len(subjects) == 0:
                                                    pass
                                                    # 0: (d*(x**j*f + e)**p)**q
                                        if len(subjects49) >= 1:
                                            tmp114 = subjects49.popleft()
                                            subst4 = Substitution(subst3)
                                            try:
                                                subst4.try_add_variable('i2.2.1.2.2', tmp114)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 38206
                                                if len(subjects49) == 0:
                                                    pass
                                                    # State 38207
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 0: (d*(x**j*f + e)**p)**q
                                            subjects49.appendleft(tmp114)
                                if len(subjects78) >= 1:
                                    tmp116 = []
                                    tmp116.append(subjects78.popleft())
                                    while True:
                                        if len(tmp116) > 1:
                                            tmp117 = create_operation_expression(associative1, tmp116)
                                        elif len(tmp116) == 1:
                                            tmp117 = tmp116[0]
                                        else:
                                            assert False, "Unreachable"
                                        subst3 = Substitution(subst2)
                                        try:
                                            subst3.try_add_variable('i2.2.1.2.2.2', tmp117)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 38204
                                            if len(subjects78) == 0:
                                                pass
                                                # State 38205
                                                subst4 = Substitution(subst3)
                                                try:
                                                    subst4.try_add_variable('i2.2.1.2.2', 1)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 38206
                                                    if len(subjects49) == 0:
                                                        pass
                                                        # State 38207
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 0: (d*(x**j*f + e)**p)**q
                                                if len(subjects49) >= 1:
                                                    tmp120 = subjects49.popleft()
                                                    subst4 = Substitution(subst3)
                                                    try:
                                                        subst4.try_add_variable('i2.2.1.2.2', tmp120)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 38206
                                                        if len(subjects49) == 0:
                                                            pass
                                                            # State 38207
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 0: (d*(x**j*f + e)**p)**q
                                                    subjects49.appendleft(tmp120)
                                        if len(subjects78) == 0:
                                            break
                                        tmp116.append(subjects78.popleft())
                                    subjects78.extendleft(reversed(tmp116))
                        subjects78.appendleft(tmp109)
                    subjects49.appendleft(tmp77)
            if len(subjects49) >= 1 and isinstance(subjects49[0], Mul):
                tmp122 = subjects49.popleft()
                associative1 = tmp122
                associative_type1 = type(tmp122)
                subjects123 = deque(tmp122._args)
                matcher = CommutativeMatcher38209.get()
                tmp124 = subjects123
                subjects123 = []
                for s in tmp124:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp124, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 38274
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.1.2.2', 1)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 38275
                            if len(subjects49) == 0:
                                pass
                                # State 38276
                                if len(subjects) == 0:
                                    pass
                                    # 0: (d*(x**j*f + e)**p)**q
                        if len(subjects49) >= 1:
                            tmp126 = []
                            tmp126.append(subjects49.popleft())
                            while True:
                                if len(tmp126) > 1:
                                    tmp127 = create_operation_expression(associative1, tmp126)
                                elif len(tmp126) == 1:
                                    tmp127 = tmp126[0]
                                else:
                                    assert False, "Unreachable"
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i2.2.1.2.2', tmp127)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 38275
                                    if len(subjects49) == 0:
                                        pass
                                        # State 38276
                                        if len(subjects) == 0:
                                            pass
                                            # 0: (d*(x**j*f + e)**p)**q
                                if len(subjects49) == 0:
                                    break
                                tmp126.append(subjects49.popleft())
                            subjects49.extendleft(reversed(tmp126))
                subjects49.appendleft(tmp122)
            subjects.appendleft(tmp48)
        return
        yield


from matchpy.utils import VariableWithCount
from matchpy.matching.many_to_one import CommutativeMatcher
from multiset import Multiset
from collections import deque
