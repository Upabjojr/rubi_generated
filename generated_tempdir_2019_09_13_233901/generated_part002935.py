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

class CommutativeMatcher76762(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({0: 1}), [
      (VariableWithCount('i2.2.2.0', 1, 1, S(1)), Mul)
]),
    1: (1, Multiset({1: 1}), [
      (VariableWithCount('i2.2.2.0', 1, 1, S(1)), Mul)
]),
    2: (2, Multiset({2: 1}), [
      (VariableWithCount('i2.2.2.0', 1, 1, None), Mul),
      (VariableWithCount('i2.2.2.0_1', 1, 1, S(1)), Mul)
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
        if CommutativeMatcher76762._instance is None:
            CommutativeMatcher76762._instance = CommutativeMatcher76762()
        return CommutativeMatcher76762._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 76761
        if len(subjects) >= 1 and isinstance(subjects[0], Pow):
            tmp1 = subjects.popleft()
            subjects2 = deque(tmp1._args)
            # State 76763
            if len(subjects2) >= 1 and isinstance(subjects2[0], cos):
                tmp3 = subjects2.popleft()
                subjects4 = deque(tmp3._args)
                # State 76764
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.2.3.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 76765
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.2.3.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 76766
                        if len(subjects4) >= 1:
                            tmp7 = subjects4.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.2.3.1.0', tmp7)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 76767
                                if len(subjects4) == 0:
                                    pass
                                    # State 76768
                                    if len(subjects2) >= 1 and subjects2[0] == -1:
                                        tmp9 = subjects2.popleft()
                                        # State 76769
                                        if len(subjects2) == 0:
                                            pass
                                            # State 76770
                                            if len(subjects) == 0:
                                                pass
                                                # 0: 1/cos(e + x*f)
                                        subjects2.appendleft(tmp9)
                            subjects4.appendleft(tmp7)
                    if len(subjects4) >= 1 and isinstance(subjects4[0], Mul):
                        tmp10 = subjects4.popleft()
                        associative1 = tmp10
                        associative_type1 = type(tmp10)
                        subjects11 = deque(tmp10._args)
                        matcher = CommutativeMatcher76772.get()
                        tmp12 = subjects11
                        subjects11 = []
                        for s in tmp12:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp12, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 76773
                                if len(subjects4) == 0:
                                    pass
                                    # State 76774
                                    if len(subjects2) >= 1 and subjects2[0] == -1:
                                        tmp13 = subjects2.popleft()
                                        # State 76775
                                        if len(subjects2) == 0:
                                            pass
                                            # State 76776
                                            if len(subjects) == 0:
                                                pass
                                                # 0: 1/cos(e + x*f)
                                        subjects2.appendleft(tmp13)
                        subjects4.appendleft(tmp10)
                if len(subjects4) >= 1 and isinstance(subjects4[0], Add):
                    tmp14 = subjects4.popleft()
                    associative1 = tmp14
                    associative_type1 = type(tmp14)
                    subjects15 = deque(tmp14._args)
                    matcher = CommutativeMatcher76778.get()
                    tmp16 = subjects15
                    subjects15 = []
                    for s in tmp16:
                        matcher.add_subject(s)
                    for pattern_index, subst1 in matcher.match(tmp16, subst0):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 76784
                            if len(subjects4) == 0:
                                pass
                                # State 76785
                                if len(subjects2) >= 1 and subjects2[0] == -1:
                                    tmp17 = subjects2.popleft()
                                    # State 76786
                                    if len(subjects2) == 0:
                                        pass
                                        # State 76787
                                        if len(subjects) == 0:
                                            pass
                                            # 0: 1/cos(e + x*f)
                                    subjects2.appendleft(tmp17)
                    subjects4.appendleft(tmp14)
                subjects2.appendleft(tmp3)
            if len(subjects2) >= 1 and isinstance(subjects2[0], sin):
                tmp18 = subjects2.popleft()
                subjects19 = deque(tmp18._args)
                # State 77046
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.2.3.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 77047
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.2.3.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 77048
                        if len(subjects19) >= 1:
                            tmp22 = subjects19.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.2.3.1.0', tmp22)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 77049
                                if len(subjects19) == 0:
                                    pass
                                    # State 77050
                                    if len(subjects2) >= 1 and subjects2[0] == -1:
                                        tmp24 = subjects2.popleft()
                                        # State 77051
                                        if len(subjects2) == 0:
                                            pass
                                            # State 77052
                                            if len(subjects) == 0:
                                                pass
                                                # 1: 1/sin(e + x*f)
                                        subjects2.appendleft(tmp24)
                            subjects19.appendleft(tmp22)
                    if len(subjects19) >= 1 and isinstance(subjects19[0], Mul):
                        tmp25 = subjects19.popleft()
                        associative1 = tmp25
                        associative_type1 = type(tmp25)
                        subjects26 = deque(tmp25._args)
                        matcher = CommutativeMatcher77054.get()
                        tmp27 = subjects26
                        subjects26 = []
                        for s in tmp27:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp27, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 77055
                                if len(subjects19) == 0:
                                    pass
                                    # State 77056
                                    if len(subjects2) >= 1 and subjects2[0] == -1:
                                        tmp28 = subjects2.popleft()
                                        # State 77057
                                        if len(subjects2) == 0:
                                            pass
                                            # State 77058
                                            if len(subjects) == 0:
                                                pass
                                                # 1: 1/sin(e + x*f)
                                        subjects2.appendleft(tmp28)
                        subjects19.appendleft(tmp25)
                if len(subjects19) >= 1 and isinstance(subjects19[0], Add):
                    tmp29 = subjects19.popleft()
                    associative1 = tmp29
                    associative_type1 = type(tmp29)
                    subjects30 = deque(tmp29._args)
                    matcher = CommutativeMatcher77060.get()
                    tmp31 = subjects30
                    subjects30 = []
                    for s in tmp31:
                        matcher.add_subject(s)
                    for pattern_index, subst1 in matcher.match(tmp31, subst0):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 77066
                            if len(subjects19) == 0:
                                pass
                                # State 77067
                                if len(subjects2) >= 1 and subjects2[0] == -1:
                                    tmp32 = subjects2.popleft()
                                    # State 77068
                                    if len(subjects2) == 0:
                                        pass
                                        # State 77069
                                        if len(subjects) == 0:
                                            pass
                                            # 1: 1/sin(e + x*f)
                                    subjects2.appendleft(tmp32)
                    subjects19.appendleft(tmp29)
                subjects2.appendleft(tmp18)
            subjects.appendleft(tmp1)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.2.1.0', S(0))
        except ValueError:
            pass
        else:
            pass
            # State 102453
            subst2 = Substitution(subst1)
            try:
                subst2.try_add_variable('i2.2.2.1.1.0_1', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 102454
                if len(subjects) >= 1:
                    tmp35 = subjects.popleft()
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.2.2.1.1.0', tmp35)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 102455
                        if len(subjects) == 0:
                            pass
                            # 2: c + x*d
                    subjects.appendleft(tmp35)
            if len(subjects) >= 1 and isinstance(subjects[0], Mul):
                tmp37 = subjects.popleft()
                associative1 = tmp37
                associative_type1 = type(tmp37)
                subjects38 = deque(tmp37._args)
                matcher = CommutativeMatcher102457.get()
                tmp39 = subjects38
                subjects38 = []
                for s in tmp39:
                    matcher.add_subject(s)
                for pattern_index, subst2 in matcher.match(tmp39, subst1):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 102458
                        if len(subjects) == 0:
                            pass
                            # 2: c + x*d
                subjects.appendleft(tmp37)
        if len(subjects) >= 1 and isinstance(subjects[0], Add):
            tmp40 = subjects.popleft()
            associative1 = tmp40
            associative_type1 = type(tmp40)
            subjects41 = deque(tmp40._args)
            matcher = CommutativeMatcher102460.get()
            tmp42 = subjects41
            subjects41 = []
            for s in tmp42:
                matcher.add_subject(s)
            for pattern_index, subst1 in matcher.match(tmp42, subst0):
                pass
                if pattern_index == 0:
                    pass
                    # State 102466
                    if len(subjects) == 0:
                        pass
                        # 2: c + x*d
            subjects.appendleft(tmp40)
        return
        yield


from matchpy.utils import VariableWithCount
from matchpy.matching.many_to_one import CommutativeMatcher
from multiset import Multiset
from collections import deque
