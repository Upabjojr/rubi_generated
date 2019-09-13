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

class CommutativeMatcher102365(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({0: 1}), [
      (VariableWithCount('i2.2.0', 1, 1, S(1)), Mul)
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
        if CommutativeMatcher102365._instance is None:
            CommutativeMatcher102365._instance = CommutativeMatcher102365()
        return CommutativeMatcher102365._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 102364
        if len(subjects) >= 1 and isinstance(subjects[0], Pow):
            tmp1 = subjects.popleft()
            subjects2 = deque(tmp1._args)
            # State 102366
            if len(subjects2) >= 1 and isinstance(subjects2[0], Mul):
                tmp3 = subjects2.popleft()
                associative1 = tmp3
                associative_type1 = type(tmp3)
                subjects4 = deque(tmp3._args)
                matcher = CommutativeMatcher102368.get()
                tmp5 = subjects4
                subjects4 = []
                for s in tmp5:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp5, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 102383
                        if len(subjects2) >= 1:
                            tmp6 = []
                            tmp6.append(subjects2.popleft())
                            while True:
                                if len(tmp6) > 1:
                                    tmp7 = create_operation_expression(associative1, tmp6)
                                elif len(tmp6) == 1:
                                    tmp7 = tmp6[0]
                                else:
                                    assert False, "Unreachable"
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i2.2.2', tmp7)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 102384
                                    if len(subjects2) == 0:
                                        pass
                                        # State 102385
                                        if len(subjects) == 0:
                                            pass
                                            # 0: (F*b*(c + x*d))**p /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f5) and (cons_f1666) and (cons_f149)
                                if len(subjects2) == 0:
                                    break
                                tmp6.append(subjects2.popleft())
                            subjects2.extendleft(reversed(tmp6))
                subjects2.appendleft(tmp3)
            subjects.appendleft(tmp1)
        return
        yield


from matchpy.utils import VariableWithCount
from matchpy.matching.many_to_one import CommutativeMatcher
from multiset import Multiset
from collections import deque
