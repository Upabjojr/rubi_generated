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


class CommutativeMatcher76700(CommutativeMatcher):
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
        if CommutativeMatcher76700._instance is None:
            CommutativeMatcher76700._instance = CommutativeMatcher76700()
        return CommutativeMatcher76700._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 76699
        if len(subjects) >= 1 and isinstance(subjects[0], Pow):
            tmp1 = subjects.popleft()
            subjects2 = deque(tmp1._args)
            # State 76701
            if len(subjects2) >= 1 and isinstance(subjects2[0], cos):
                tmp3 = subjects2.popleft()
                subjects4 = deque(tmp3._args)
                # State 76702
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.2.3.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 76703
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.2.3.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 76704
                        if len(subjects4) >= 1:
                            tmp7 = subjects4.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.2.3.1.0', tmp7)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 76705
                                if len(subjects4) == 0:
                                    pass
                                    # State 76706
                                    if len(subjects2) >= 1 and subjects2[0] == Integer(-1):
                                        tmp9 = subjects2.popleft()
                                        # State 76707
                                        if len(subjects2) == 0:
                                            pass
                                            # State 76708
                                            if len(subjects) == 0:
                                                pass
                                                # 0: 1/cos(e + x*f)
                                                yield 0, subst3
                                        subjects2.appendleft(tmp9)
                            subjects4.appendleft(tmp7)
                    if len(subjects4) >= 1 and isinstance(subjects4[0], Mul):
                        tmp10 = subjects4.popleft()
                        associative1 = tmp10
                        associative_type1 = type(tmp10)
                        subjects11 = deque(tmp10._args)
                        matcher = CommutativeMatcher76710.get()
                        tmp12 = subjects11
                        subjects11 = []
                        for s in tmp12:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp12, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 76711
                                if len(subjects4) == 0:
                                    pass
                                    # State 76712
                                    if len(subjects2) >= 1 and subjects2[0] == Integer(-1):
                                        tmp13 = subjects2.popleft()
                                        # State 76713
                                        if len(subjects2) == 0:
                                            pass
                                            # State 76714
                                            if len(subjects) == 0:
                                                pass
                                                # 0: 1/cos(e + x*f)
                                                yield 0, subst2
                                        subjects2.appendleft(tmp13)
                        subjects4.appendleft(tmp10)
                if len(subjects4) >= 1 and isinstance(subjects4[0], Add):
                    tmp14 = subjects4.popleft()
                    associative1 = tmp14
                    associative_type1 = type(tmp14)
                    subjects15 = deque(tmp14._args)
                    matcher = CommutativeMatcher76716.get()
                    tmp16 = subjects15
                    subjects15 = []
                    for s in tmp16:
                        matcher.add_subject(s)
                    for pattern_index, subst1 in matcher.match(tmp16, subst0):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 76722
                            if len(subjects4) == 0:
                                pass
                                # State 76723
                                if len(subjects2) >= 1 and subjects2[0] == Integer(-1):
                                    tmp17 = subjects2.popleft()
                                    # State 76724
                                    if len(subjects2) == 0:
                                        pass
                                        # State 76725
                                        if len(subjects) == 0:
                                            pass
                                            # 0: 1/cos(e + x*f)
                                            yield 0, subst1
                                    subjects2.appendleft(tmp17)
                    subjects4.appendleft(tmp14)
                subjects2.appendleft(tmp3)
            if len(subjects2) >= 1 and isinstance(subjects2[0], sin):
                tmp18 = subjects2.popleft()
                subjects19 = deque(tmp18._args)
                # State 76989
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.2.3.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 76990
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.2.3.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 76991
                        if len(subjects19) >= 1:
                            tmp22 = subjects19.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.2.3.1.0', tmp22)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 76992
                                if len(subjects19) == 0:
                                    pass
                                    # State 76993
                                    if len(subjects2) >= 1 and subjects2[0] == Integer(-1):
                                        tmp24 = subjects2.popleft()
                                        # State 76994
                                        if len(subjects2) == 0:
                                            pass
                                            # State 76995
                                            if len(subjects) == 0:
                                                pass
                                                # 1: 1/sin(e + x*f)
                                                yield 1, subst3
                                        subjects2.appendleft(tmp24)
                            subjects19.appendleft(tmp22)
                    if len(subjects19) >= 1 and isinstance(subjects19[0], Mul):
                        tmp25 = subjects19.popleft()
                        associative1 = tmp25
                        associative_type1 = type(tmp25)
                        subjects26 = deque(tmp25._args)
                        matcher = CommutativeMatcher76997.get()
                        tmp27 = subjects26
                        subjects26 = []
                        for s in tmp27:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp27, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 76998
                                if len(subjects19) == 0:
                                    pass
                                    # State 76999
                                    if len(subjects2) >= 1 and subjects2[0] == Integer(-1):
                                        tmp28 = subjects2.popleft()
                                        # State 77000
                                        if len(subjects2) == 0:
                                            pass
                                            # State 77001
                                            if len(subjects) == 0:
                                                pass
                                                # 1: 1/sin(e + x*f)
                                                yield 1, subst2
                                        subjects2.appendleft(tmp28)
                        subjects19.appendleft(tmp25)
                if len(subjects19) >= 1 and isinstance(subjects19[0], Add):
                    tmp29 = subjects19.popleft()
                    associative1 = tmp29
                    associative_type1 = type(tmp29)
                    subjects30 = deque(tmp29._args)
                    matcher = CommutativeMatcher77003.get()
                    tmp31 = subjects30
                    subjects30 = []
                    for s in tmp31:
                        matcher.add_subject(s)
                    for pattern_index, subst1 in matcher.match(tmp31, subst0):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 77009
                            if len(subjects19) == 0:
                                pass
                                # State 77010
                                if len(subjects2) >= 1 and subjects2[0] == Integer(-1):
                                    tmp32 = subjects2.popleft()
                                    # State 77011
                                    if len(subjects2) == 0:
                                        pass
                                        # State 77012
                                        if len(subjects) == 0:
                                            pass
                                            # 1: 1/sin(e + x*f)
                                            yield 1, subst1
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
            # State 102436
            subst2 = Substitution(subst1)
            try:
                subst2.try_add_variable('i2.2.2.1.1.0_1', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 102437
                if len(subjects) >= 1:
                    tmp35 = subjects.popleft()
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.2.2.1.1.0', tmp35)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 102438
                        if len(subjects) == 0:
                            pass
                            # 2: c + x*d
                            yield 2, subst3
                    subjects.appendleft(tmp35)
            if len(subjects) >= 1 and isinstance(subjects[0], Mul):
                tmp37 = subjects.popleft()
                associative1 = tmp37
                associative_type1 = type(tmp37)
                subjects38 = deque(tmp37._args)
                matcher = CommutativeMatcher102440.get()
                tmp39 = subjects38
                subjects38 = []
                for s in tmp39:
                    matcher.add_subject(s)
                for pattern_index, subst2 in matcher.match(tmp39, subst1):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 102441
                        if len(subjects) == 0:
                            pass
                            # 2: c + x*d
                            yield 2, subst2
                subjects.appendleft(tmp37)
        if len(subjects) >= 1 and isinstance(subjects[0], Add):
            tmp40 = subjects.popleft()
            associative1 = tmp40
            associative_type1 = type(tmp40)
            subjects41 = deque(tmp40._args)
            matcher = CommutativeMatcher102443.get()
            tmp42 = subjects41
            subjects41 = []
            for s in tmp42:
                matcher.add_subject(s)
            for pattern_index, subst1 in matcher.match(tmp42, subst0):
                pass
                if pattern_index == 0:
                    pass
                    # State 102449
                    if len(subjects) == 0:
                        pass
                        # 2: c + x*d
                        yield 2, subst1
            subjects.appendleft(tmp40)
        return
        yield


from .generated_part002897 import *
from .generated_part002891 import *
from .generated_part002895 import *
from matchpy.matching.many_to_one import CommutativeMatcher
from .generated_part002894 import *
from .generated_part002898 import *
from collections import deque
from .generated_part002892 import *
from matchpy.utils import VariableWithCount
from multiset import Multiset