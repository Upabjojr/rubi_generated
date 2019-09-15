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


class CommutativeMatcher46620(CommutativeMatcher):
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
        if CommutativeMatcher46620._instance is None:
            CommutativeMatcher46620._instance = CommutativeMatcher46620()
        return CommutativeMatcher46620._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 46619
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.3.2', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 46621
            if len(subjects) >= 1 and isinstance(subjects[0], Mul):
                tmp2 = subjects.popleft()
                associative1 = tmp2
                associative_type1 = type(tmp2)
                subjects3 = deque(tmp2._args)
                matcher = CommutativeMatcher46623.get()
                tmp4 = subjects3
                subjects3 = []
                for s in tmp4:
                    matcher.add_subject(s)
                for pattern_index, subst2 in matcher.match(tmp4, subst1):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 46659
                        if len(subjects) == 0:
                            pass
                            # 0: (e1*(a + b*x)/(a + x*b))**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f5) and (cons_f654) and (cons_f27)
                            yield 0, subst2
                subjects.appendleft(tmp2)
        if len(subjects) >= 1 and isinstance(subjects[0], Pow):
            tmp5 = subjects.popleft()
            subjects6 = deque(tmp5._args)
            # State 46660
            if len(subjects6) >= 1 and isinstance(subjects6[0], Mul):
                tmp7 = subjects6.popleft()
                associative1 = tmp7
                associative_type1 = type(tmp7)
                subjects8 = deque(tmp7._args)
                matcher = CommutativeMatcher46662.get()
                tmp9 = subjects8
                subjects8 = []
                for s in tmp9:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp9, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 46698
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.3.2', 1)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 46699
                            if len(subjects6) == 0:
                                pass
                                # State 46700
                                if len(subjects) == 0:
                                    pass
                                    # 0: (e1*(a + b*x)/(a + x*b))**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f5) and (cons_f654) and (cons_f27)
                                    yield 0, subst2
                        if len(subjects6) >= 1:
                            tmp11 = []
                            tmp11.append(subjects6.popleft())
                            while True:
                                if len(tmp11) > 1:
                                    tmp12 = create_operation_expression(associative1, tmp11)
                                elif len(tmp11) == 1:
                                    tmp12 = tmp11[0]
                                else:
                                    assert False, "Unreachable"
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i2.3.2', tmp12)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 46699
                                    if len(subjects6) == 0:
                                        pass
                                        # State 46700
                                        if len(subjects) == 0:
                                            pass
                                            # 0: (e1*(a + b*x)/(a + x*b))**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f5) and (cons_f654) and (cons_f27)
                                            yield 0, subst2
                                if len(subjects6) == 0:
                                    break
                                tmp11.append(subjects6.popleft())
                            subjects6.extendleft(reversed(tmp11))
                subjects6.appendleft(tmp7)
            subjects.appendleft(tmp5)
        return
        yield


from .generated_part000852 import *
from .generated_part000859 import *
from matchpy.matching.many_to_one import CommutativeMatcher
from collections import deque
from matchpy.utils import VariableWithCount
from multiset import Multiset