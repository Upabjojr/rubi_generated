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


class CommutativeMatcher150268(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({0: 1}), [
      (VariableWithCount('i2.3.0', 1, 1, S(1)), Mul)
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
        if CommutativeMatcher150268._instance is None:
            CommutativeMatcher150268._instance = CommutativeMatcher150268()
        return CommutativeMatcher150268._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 150267
        if len(subjects) >= 1 and isinstance(subjects[0], Pow):
            tmp1 = subjects.popleft()
            subjects2 = deque(tmp1._args)
            # State 150269
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.3.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 150270
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.3.2.1.0', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 150271
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.3.2.1.2', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 150272
                        if len(subjects2) >= 1:
                            tmp6 = subjects2.popleft()
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i2.3.2.1.1', tmp6)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 150273
                                if len(subjects2) >= 1 and subjects2[0] == Integer(-1):
                                    tmp8 = subjects2.popleft()
                                    # State 150274
                                    if len(subjects2) == 0:
                                        pass
                                        # State 150275
                                        if len(subjects) == 0:
                                            pass
                                            # 0: 1/(a + b*x**n)
                                            yield 0, subst4
                                    subjects2.appendleft(tmp8)
                            subjects2.appendleft(tmp6)
                    if len(subjects2) >= 1 and isinstance(subjects2[0], Pow):
                        tmp9 = subjects2.popleft()
                        subjects10 = deque(tmp9._args)
                        # State 150276
                        if len(subjects10) >= 1:
                            tmp11 = subjects10.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.3.2.1.1', tmp11)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 150277
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.3.2.1.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 150278
                                    if len(subjects10) == 0:
                                        pass
                                        # State 150279
                                        if len(subjects2) >= 1 and subjects2[0] == Integer(-1):
                                            tmp14 = subjects2.popleft()
                                            # State 150280
                                            if len(subjects2) == 0:
                                                pass
                                                # State 150281
                                                if len(subjects) == 0:
                                                    pass
                                                    # 0: 1/(a + b*x**n)
                                                    yield 0, subst4
                                            subjects2.appendleft(tmp14)
                                if len(subjects10) >= 1:
                                    tmp15 = subjects10.popleft()
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i2.3.2.1.2', tmp15)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 150278
                                        if len(subjects10) == 0:
                                            pass
                                            # State 150279
                                            if len(subjects2) >= 1 and subjects2[0] == Integer(-1):
                                                tmp17 = subjects2.popleft()
                                                # State 150280
                                                if len(subjects2) == 0:
                                                    pass
                                                    # State 150281
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 0: 1/(a + b*x**n)
                                                        yield 0, subst4
                                                subjects2.appendleft(tmp17)
                                    subjects10.appendleft(tmp15)
                            subjects10.appendleft(tmp11)
                        subjects2.appendleft(tmp9)
                if len(subjects2) >= 1 and isinstance(subjects2[0], Mul):
                    tmp18 = subjects2.popleft()
                    associative1 = tmp18
                    associative_type1 = type(tmp18)
                    subjects19 = deque(tmp18._args)
                    matcher = CommutativeMatcher150283.get()
                    tmp20 = subjects19
                    subjects19 = []
                    for s in tmp20:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp20, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 150290
                            if len(subjects2) >= 1 and subjects2[0] == Integer(-1):
                                tmp21 = subjects2.popleft()
                                # State 150291
                                if len(subjects2) == 0:
                                    pass
                                    # State 150292
                                    if len(subjects) == 0:
                                        pass
                                        # 0: 1/(a + b*x**n)
                                        yield 0, subst2
                                subjects2.appendleft(tmp21)
                    subjects2.appendleft(tmp18)
            if len(subjects2) >= 1 and isinstance(subjects2[0], Add):
                tmp22 = subjects2.popleft()
                associative1 = tmp22
                associative_type1 = type(tmp22)
                subjects23 = deque(tmp22._args)
                matcher = CommutativeMatcher150294.get()
                tmp24 = subjects23
                subjects23 = []
                for s in tmp24:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp24, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 150311
                        if len(subjects2) >= 1 and subjects2[0] == Integer(-1):
                            tmp25 = subjects2.popleft()
                            # State 150312
                            if len(subjects2) == 0:
                                pass
                                # State 150313
                                if len(subjects) == 0:
                                    pass
                                    # 0: 1/(a + b*x**n)
                                    yield 0, subst1
                            subjects2.appendleft(tmp25)
                subjects2.appendleft(tmp22)
            subjects.appendleft(tmp1)
        return
        yield


from .generated_part007094 import *
from matchpy.matching.many_to_one import CommutativeMatcher
from collections import deque
from .generated_part007095 import *
from matchpy.utils import VariableWithCount
from multiset import Multiset