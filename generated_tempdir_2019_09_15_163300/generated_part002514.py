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


class CommutativeMatcher30065(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({0: 1}), [
      (VariableWithCount('i2.2.1.2.2.2.1.0', 1, 1, None), Add)
])
}
    subjects = {}
    subjects_by_id = {}
    bipartite = BipartiteGraph()
    associative = Add
    max_optional_count = 0
    anonymous_patterns = set()

    def __init__(self):
        self.add_subject(None)

    @staticmethod
    def get():
        if CommutativeMatcher30065._instance is None:
            CommutativeMatcher30065._instance = CommutativeMatcher30065()
        return CommutativeMatcher30065._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 30064
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.2.2.2.1.1.0', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 30066
            subst2 = Substitution(subst1)
            try:
                subst2.try_add_variable('i2.2.1.2.2.2.1.1.2', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 30067
                if len(subjects) >= 1:
                    tmp3 = subjects.popleft()
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.2.1.2.2.2.1', tmp3)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 30068
                        if len(subjects) == 0:
                            pass
                            # 0: e*x**r
                            yield 0, subst3
                    subjects.appendleft(tmp3)
            if len(subjects) >= 1 and isinstance(subjects[0], Pow):
                tmp5 = subjects.popleft()
                subjects6 = deque(tmp5._args)
                # State 30069
                if len(subjects6) >= 1:
                    tmp7 = subjects6.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.2.2.2.1', tmp7)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 30070
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.2.2.2.1.1.2', 1)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 30071
                            if len(subjects6) == 0:
                                pass
                                # State 30072
                                if len(subjects) == 0:
                                    pass
                                    # 0: e*x**r
                                    yield 0, subst3
                        if len(subjects6) >= 1:
                            tmp10 = subjects6.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.2.2.2.1.1.2', tmp10)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 30071
                                if len(subjects6) == 0:
                                    pass
                                    # State 30072
                                    if len(subjects) == 0:
                                        pass
                                        # 0: e*x**r
                                        yield 0, subst3
                            subjects6.appendleft(tmp10)
                    subjects6.appendleft(tmp7)
                subjects.appendleft(tmp5)
        if len(subjects) >= 1 and isinstance(subjects[0], Mul):
            tmp12 = subjects.popleft()
            associative1 = tmp12
            associative_type1 = type(tmp12)
            subjects13 = deque(tmp12._args)
            matcher = CommutativeMatcher30074.get()
            tmp14 = subjects13
            subjects13 = []
            for s in tmp14:
                matcher.add_subject(s)
            for pattern_index, subst1 in matcher.match(tmp14, subst0):
                pass
                if pattern_index == 0:
                    pass
                    # State 30081
                    if len(subjects) == 0:
                        pass
                        # 0: e*x**r
                        yield 0, subst1
            subjects.appendleft(tmp12)
        return
        yield


from matchpy.matching.many_to_one import CommutativeMatcher
from collections import deque
from .generated_part002515 import *
from matchpy.utils import VariableWithCount
from multiset import Multiset