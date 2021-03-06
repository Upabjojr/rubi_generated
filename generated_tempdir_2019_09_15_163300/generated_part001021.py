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


class CommutativeMatcher151722(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({0: 1}), [
      (VariableWithCount('i2.1.0', 1, 1, None), Add)
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
        if CommutativeMatcher151722._instance is None:
            CommutativeMatcher151722._instance = CommutativeMatcher151722()
        return CommutativeMatcher151722._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 151721
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.1.1.0', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 151723
            if len(subjects) >= 1 and isinstance(subjects[0], Pow):
                tmp2 = subjects.popleft()
                subjects3 = deque(tmp2._args)
                # State 151724
                if len(subjects3) >= 1:
                    tmp4 = subjects3.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.1.1.1', tmp4)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 151725
                        if len(subjects3) >= 1:
                            tmp6 = subjects3.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.1.1.2', tmp6)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 151726
                                if len(subjects3) == 0:
                                    pass
                                    # State 151727
                                    if len(subjects) == 0:
                                        pass
                                        # 0: b*y**n /; (cons_f3) and (cons_f4) and (cons_f1833) and (With6952)
                                        yield 0, subst3
                            subjects3.appendleft(tmp6)
                    subjects3.appendleft(tmp4)
                subjects.appendleft(tmp2)
        if len(subjects) >= 1 and isinstance(subjects[0], Mul):
            tmp8 = subjects.popleft()
            associative1 = tmp8
            associative_type1 = type(tmp8)
            subjects9 = deque(tmp8._args)
            matcher = CommutativeMatcher151729.get()
            tmp10 = subjects9
            subjects9 = []
            for s in tmp10:
                matcher.add_subject(s)
            for pattern_index, subst1 in matcher.match(tmp10, subst0):
                pass
                if pattern_index == 0:
                    pass
                    # State 151734
                    if len(subjects) == 0:
                        pass
                        # 0: b*y**n /; (cons_f3) and (cons_f4) and (cons_f1833) and (With6952)
                        yield 0, subst1
            subjects.appendleft(tmp8)
        return
        yield


from matchpy.matching.many_to_one import CommutativeMatcher
from collections import deque
from .generated_part001022 import *
from matchpy.utils import VariableWithCount
from multiset import Multiset