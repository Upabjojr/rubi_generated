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


class CommutativeMatcher46662(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({0: 1, 1: 1}), [
      (VariableWithCount('i2.3.2.0', 1, 1, S(1)), Mul)
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
        if CommutativeMatcher46662._instance is None:
            CommutativeMatcher46662._instance = CommutativeMatcher46662()
        return CommutativeMatcher46662._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 46661
        if len(subjects) >= 1 and isinstance(subjects[0], Pow):
            tmp1 = subjects.popleft()
            subjects2 = deque(tmp1._args)
            # State 46663
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.3.2.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 46664
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.3.2.2.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 46665
                    if len(subjects2) >= 1:
                        tmp5 = subjects2.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.3.2.2.1.0', tmp5)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 46666
                            if len(subjects2) >= 1 and subjects2[0] == Integer(-1):
                                tmp7 = subjects2.popleft()
                                # State 46667
                                if len(subjects2) == 0:
                                    pass
                                    # State 46668
                                    if len(subjects) == 0:
                                        pass
                                        # 0: 1/(c + x*d)
                                        yield 0, subst3
                                subjects2.appendleft(tmp7)
                        subjects2.appendleft(tmp5)
                if len(subjects2) >= 1 and isinstance(subjects2[0], Mul):
                    tmp8 = subjects2.popleft()
                    associative1 = tmp8
                    associative_type1 = type(tmp8)
                    subjects9 = deque(tmp8._args)
                    matcher = CommutativeMatcher46670.get()
                    tmp10 = subjects9
                    subjects9 = []
                    for s in tmp10:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp10, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 46671
                            if len(subjects2) >= 1 and subjects2[0] == Integer(-1):
                                tmp11 = subjects2.popleft()
                                # State 46672
                                if len(subjects2) == 0:
                                    pass
                                    # State 46673
                                    if len(subjects) == 0:
                                        pass
                                        # 0: 1/(c + x*d)
                                        yield 0, subst2
                                subjects2.appendleft(tmp11)
                    subjects2.appendleft(tmp8)
            if len(subjects2) >= 1 and isinstance(subjects2[0], Add):
                tmp12 = subjects2.popleft()
                associative1 = tmp12
                associative_type1 = type(tmp12)
                subjects13 = deque(tmp12._args)
                matcher = CommutativeMatcher46675.get()
                tmp14 = subjects13
                subjects13 = []
                for s in tmp14:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp14, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 46681
                        if len(subjects2) >= 1 and subjects2[0] == Integer(-1):
                            tmp15 = subjects2.popleft()
                            # State 46682
                            if len(subjects2) == 0:
                                pass
                                # State 46683
                                if len(subjects) == 0:
                                    pass
                                    # 0: 1/(c + x*d)
                                    yield 0, subst1
                            subjects2.appendleft(tmp15)
                subjects2.appendleft(tmp12)
            subjects.appendleft(tmp1)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.3.2.1.0', S(0))
        except ValueError:
            pass
        else:
            pass
            # State 46684
            subst2 = Substitution(subst1)
            try:
                subst2.try_add_variable('i2.3.2.1.1.0', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 46685
                if len(subjects) >= 1:
                    tmp18 = subjects.popleft()
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.3.2.2.1.0', tmp18)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 46686
                        if len(subjects) == 0:
                            pass
                            # 1: a + b*x
                            yield 1, subst3
                    subjects.appendleft(tmp18)
            if len(subjects) >= 1 and isinstance(subjects[0], Mul):
                tmp20 = subjects.popleft()
                associative1 = tmp20
                associative_type1 = type(tmp20)
                subjects21 = deque(tmp20._args)
                matcher = CommutativeMatcher46688.get()
                tmp22 = subjects21
                subjects21 = []
                for s in tmp22:
                    matcher.add_subject(s)
                for pattern_index, subst2 in matcher.match(tmp22, subst1):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 46689
                        if len(subjects) == 0:
                            pass
                            # 1: a + b*x
                            yield 1, subst2
                subjects.appendleft(tmp20)
        if len(subjects) >= 1 and isinstance(subjects[0], Add):
            tmp23 = subjects.popleft()
            associative1 = tmp23
            associative_type1 = type(tmp23)
            subjects24 = deque(tmp23._args)
            matcher = CommutativeMatcher46691.get()
            tmp25 = subjects24
            subjects24 = []
            for s in tmp25:
                matcher.add_subject(s)
            for pattern_index, subst1 in matcher.match(tmp25, subst0):
                pass
                if pattern_index == 0:
                    pass
                    # State 46697
                    if len(subjects) == 0:
                        pass
                        # 1: a + b*x
                        yield 1, subst1
            subjects.appendleft(tmp23)
        return
        yield


from .generated_part000861 import *
from matchpy.matching.many_to_one import CommutativeMatcher
from .generated_part000863 import *
from .generated_part000864 import *
from collections import deque
from .generated_part000860 import *
from matchpy.utils import VariableWithCount
from multiset import Multiset