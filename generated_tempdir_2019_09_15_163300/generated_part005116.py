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


class CommutativeMatcher15018(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({0: 1}), [
      (VariableWithCount('i2.2.1.4.0', 1, 1, S(1)), Mul)
]),
    1: (1, Multiset({}), [
      (VariableWithCount('i2.2.1.4.0', 1, 1, None), Mul),
      (VariableWithCount('i2.2.1.4.0_1', 1, 1, S(1)), Mul)
]),
    2: (2, Multiset({1: 1}), [
      (VariableWithCount('i2.2.1.4.0', 1, 1, S(1)), Mul)
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
        if CommutativeMatcher15018._instance is None:
            CommutativeMatcher15018._instance = CommutativeMatcher15018()
        return CommutativeMatcher15018._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 15017
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.4.1.0', S(0))
        except ValueError:
            pass
        else:
            pass
            # State 15019
            subst2 = Substitution(subst1)
            try:
                subst2.try_add_variable('i2.2.1.4.1.1.0_1', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 15020
                if len(subjects) >= 1:
                    tmp3 = subjects.popleft()
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.2.1.4.1.1.0', tmp3)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 15021
                        if len(subjects) == 0:
                            pass
                            # 0: e + x*f
                            yield 0, subst3
                    subjects.appendleft(tmp3)
            subst2 = Substitution(subst1)
            try:
                subst2.try_add_variable('i2.2.1.4.1.1.0', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 16721
                if len(subjects) >= 1:
                    tmp6 = subjects.popleft()
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.2.3.1.1.0', tmp6)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 16722
                        if len(subjects) == 0:
                            pass
                            # 1: e + f*x
                            yield 1, subst3
                    subjects.appendleft(tmp6)
            if len(subjects) >= 1 and isinstance(subjects[0], Mul):
                tmp8 = subjects.popleft()
                associative1 = tmp8
                associative_type1 = type(tmp8)
                subjects9 = deque(tmp8._args)
                matcher = CommutativeMatcher15023.get()
                tmp10 = subjects9
                subjects9 = []
                for s in tmp10:
                    matcher.add_subject(s)
                for pattern_index, subst2 in matcher.match(tmp10, subst1):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 15024
                        if len(subjects) == 0:
                            pass
                            # 0: e + x*f
                            yield 0, subst2
                    if pattern_index == 1:
                        pass
                        # State 16723
                        if len(subjects) == 0:
                            pass
                            # 1: e + f*x
                            yield 1, subst2
                subjects.appendleft(tmp8)
        if len(subjects) >= 1 and isinstance(subjects[0], Add):
            tmp11 = subjects.popleft()
            associative1 = tmp11
            associative_type1 = type(tmp11)
            subjects12 = deque(tmp11._args)
            matcher = CommutativeMatcher15026.get()
            tmp13 = subjects12
            subjects12 = []
            for s in tmp13:
                matcher.add_subject(s)
            for pattern_index, subst1 in matcher.match(tmp13, subst0):
                pass
                if pattern_index == 0:
                    pass
                    # State 15032
                    if len(subjects) == 0:
                        pass
                        # 0: e + x*f
                        yield 0, subst1
                if pattern_index == 1:
                    pass
                    # State 16727
                    if len(subjects) == 0:
                        pass
                        # 1: e + f*x
                        yield 1, subst1
            subjects.appendleft(tmp11)
        return
        yield


from .generated_part005117 import *
from matchpy.matching.many_to_one import CommutativeMatcher
from .generated_part005118 import *
from collections import deque
from matchpy.utils import VariableWithCount
from multiset import Multiset