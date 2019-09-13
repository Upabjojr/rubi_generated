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

class CommutativeMatcher128610(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({0: 1}), [
      (VariableWithCount('i2.4.0', 1, 1, S(0)), Add)
]),
    1: (1, Multiset({1: 1}), [
      (VariableWithCount('i2.4.0', 1, 1, S(0)), Add)
]),
    2: (2, Multiset({2: 1}), [
      (VariableWithCount('i2.4.0', 1, 1, S(0)), Add)
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
        if CommutativeMatcher128610._instance is None:
            CommutativeMatcher128610._instance = CommutativeMatcher128610()
        return CommutativeMatcher128610._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 128609
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.4.1.0', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 128611
            subst2 = Substitution(subst1)
            try:
                subst2.try_add_variable('i2.4.1.2', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 128612
                if len(subjects) >= 1:
                    tmp3 = subjects.popleft()
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.4.1.1', tmp3)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 128613
                        if len(subjects) == 0:
                            pass
                            # 0: b*x**n
                    subjects.appendleft(tmp3)
            if len(subjects) >= 1 and isinstance(subjects[0], Pow):
                tmp5 = subjects.popleft()
                subjects6 = deque(tmp5._args)
                # State 128614
                if len(subjects6) >= 1:
                    tmp7 = subjects6.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.4.1.1', tmp7)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 128615
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.4.1.2', 1)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 128616
                            if len(subjects6) == 0:
                                pass
                                # State 128617
                                if len(subjects) == 0:
                                    pass
                                    # 0: b*x**n
                        if len(subjects6) >= 1:
                            tmp10 = subjects6.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.4.1.2', tmp10)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 128616
                                if len(subjects6) == 0:
                                    pass
                                    # State 128617
                                    if len(subjects) == 0:
                                        pass
                                        # 0: b*x**n
                            subjects6.appendleft(tmp10)
                    subjects6.appendleft(tmp7)
                subjects.appendleft(tmp5)
            if len(subjects) >= 1 and isinstance(subjects[0], log):
                tmp12 = subjects.popleft()
                subjects13 = deque(tmp12._args)
                # State 136196
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.4.1.2.0', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 136197
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.4.1.2.2', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 136198
                        if len(subjects13) >= 1:
                            tmp16 = subjects13.popleft()
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i2.4.1.2.1', tmp16)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 136199
                                if len(subjects13) == 0:
                                    pass
                                    # State 136200
                                    if len(subjects) == 0:
                                        pass
                                        # 2: b*log(c*x**n)
                            subjects13.appendleft(tmp16)
                    if len(subjects13) >= 1 and isinstance(subjects13[0], Pow):
                        tmp18 = subjects13.popleft()
                        subjects19 = deque(tmp18._args)
                        # State 136201
                        if len(subjects19) >= 1:
                            tmp20 = subjects19.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.4.1.2.1', tmp20)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 136202
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.4.1.2.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 136203
                                    if len(subjects19) == 0:
                                        pass
                                        # State 136204
                                        if len(subjects13) == 0:
                                            pass
                                            # State 136205
                                            if len(subjects) == 0:
                                                pass
                                                # 2: b*log(c*x**n)
                                if len(subjects19) >= 1:
                                    tmp23 = subjects19.popleft()
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i2.4.1.2.2', tmp23)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 136203
                                        if len(subjects19) == 0:
                                            pass
                                            # State 136204
                                            if len(subjects13) == 0:
                                                pass
                                                # State 136205
                                                if len(subjects) == 0:
                                                    pass
                                                    # 2: b*log(c*x**n)
                                    subjects19.appendleft(tmp23)
                            subjects19.appendleft(tmp20)
                        subjects13.appendleft(tmp18)
                if len(subjects13) >= 1 and isinstance(subjects13[0], Mul):
                    tmp25 = subjects13.popleft()
                    associative1 = tmp25
                    associative_type1 = type(tmp25)
                    subjects26 = deque(tmp25._args)
                    matcher = CommutativeMatcher136207.get()
                    tmp27 = subjects26
                    subjects26 = []
                    for s in tmp27:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp27, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 136214
                            if len(subjects13) == 0:
                                pass
                                # State 136215
                                if len(subjects) == 0:
                                    pass
                                    # 2: b*log(c*x**n)
                    subjects13.appendleft(tmp25)
                subjects.appendleft(tmp12)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.4.1.0_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 129562
            if len(subjects) >= 1:
                tmp29 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.4.1.0', tmp29)
                except ValueError:
                    pass
                else:
                    pass
                    # State 129563
                    if len(subjects) == 0:
                        pass
                        # 1: x*b
                subjects.appendleft(tmp29)
        if len(subjects) >= 1 and isinstance(subjects[0], Mul):
            tmp31 = subjects.popleft()
            associative1 = tmp31
            associative_type1 = type(tmp31)
            subjects32 = deque(tmp31._args)
            matcher = CommutativeMatcher128619.get()
            tmp33 = subjects32
            subjects32 = []
            for s in tmp33:
                matcher.add_subject(s)
            for pattern_index, subst1 in matcher.match(tmp33, subst0):
                pass
                if pattern_index == 0:
                    pass
                    # State 128626
                    if len(subjects) == 0:
                        pass
                        # 0: b*x**n
                if pattern_index == 1:
                    pass
                    # State 129564
                    if len(subjects) == 0:
                        pass
                        # 1: x*b
                if pattern_index == 2:
                    pass
                    # State 136236
                    if len(subjects) == 0:
                        pass
                        # 2: b*log(c*x**n)
            subjects.appendleft(tmp31)
        return
        yield


from matchpy.utils import VariableWithCount
from matchpy.matching.many_to_one import CommutativeMatcher
from multiset import Multiset
from collections import deque
