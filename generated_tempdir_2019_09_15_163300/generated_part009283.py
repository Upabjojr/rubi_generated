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


class CommutativeMatcher50629(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({0: 1}), [
      (VariableWithCount('i3.1.2.2.0', 1, 1, None), Add)
]),
    1: (1, Multiset({1: 1}), [
      (VariableWithCount('i3.1.2.2.0', 1, 1, None), Add)
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
        if CommutativeMatcher50629._instance is None:
            CommutativeMatcher50629._instance = CommutativeMatcher50629()
        return CommutativeMatcher50629._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 50628
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i3.1.2.2.1.0', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 50630
            if len(subjects) >= 1 and isinstance(subjects[0], Pow):
                tmp2 = subjects.popleft()
                subjects3 = deque(tmp2._args)
                # State 50631
                if len(subjects3) >= 1:
                    tmp4 = subjects3.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i3.1.2.2.1.1', tmp4)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 50632
                        if len(subjects3) >= 1 and subjects3[0] == Integer(2):
                            tmp6 = subjects3.popleft()
                            # State 50633
                            if len(subjects3) == 0:
                                pass
                                # State 50634
                                if len(subjects) == 0:
                                    pass
                                    # 0: e*x**2
                                    yield 0, subst2
                            subjects3.appendleft(tmp6)
                    subjects3.appendleft(tmp4)
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i3.1.2.2.1.2.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 52630
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i3.1.2.2.1.2.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 52631
                        if len(subjects3) >= 1:
                            tmp9 = subjects3.popleft()
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i3.1.2.2.1.2.1.0', tmp9)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 52632
                                if len(subjects3) >= 1 and subjects3[0] == Integer(-1):
                                    tmp11 = subjects3.popleft()
                                    # State 52633
                                    if len(subjects3) == 0:
                                        pass
                                        # State 52634
                                        if len(subjects) == 0:
                                            pass
                                            # 1: e/(f + x*g)
                                            yield 1, subst4
                                    subjects3.appendleft(tmp11)
                            subjects3.appendleft(tmp9)
                    if len(subjects3) >= 1 and isinstance(subjects3[0], Mul):
                        tmp12 = subjects3.popleft()
                        associative1 = tmp12
                        associative_type1 = type(tmp12)
                        subjects13 = deque(tmp12._args)
                        matcher = CommutativeMatcher52636.get()
                        tmp14 = subjects13
                        subjects13 = []
                        for s in tmp14:
                            matcher.add_subject(s)
                        for pattern_index, subst3 in matcher.match(tmp14, subst2):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 52637
                                if len(subjects3) >= 1 and subjects3[0] == Integer(-1):
                                    tmp15 = subjects3.popleft()
                                    # State 52638
                                    if len(subjects3) == 0:
                                        pass
                                        # State 52639
                                        if len(subjects) == 0:
                                            pass
                                            # 1: e/(f + x*g)
                                            yield 1, subst3
                                    subjects3.appendleft(tmp15)
                        subjects3.appendleft(tmp12)
                if len(subjects3) >= 1 and isinstance(subjects3[0], Add):
                    tmp16 = subjects3.popleft()
                    associative1 = tmp16
                    associative_type1 = type(tmp16)
                    subjects17 = deque(tmp16._args)
                    matcher = CommutativeMatcher52641.get()
                    tmp18 = subjects17
                    subjects17 = []
                    for s in tmp18:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp18, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 52647
                            if len(subjects3) >= 1 and subjects3[0] == Integer(-1):
                                tmp19 = subjects3.popleft()
                                # State 52648
                                if len(subjects3) == 0:
                                    pass
                                    # State 52649
                                    if len(subjects) == 0:
                                        pass
                                        # 1: e/(f + x*g)
                                        yield 1, subst2
                                subjects3.appendleft(tmp19)
                    subjects3.appendleft(tmp16)
                subjects.appendleft(tmp2)
        if len(subjects) >= 1 and isinstance(subjects[0], Mul):
            tmp20 = subjects.popleft()
            associative1 = tmp20
            associative_type1 = type(tmp20)
            subjects21 = deque(tmp20._args)
            matcher = CommutativeMatcher50636.get()
            tmp22 = subjects21
            subjects21 = []
            for s in tmp22:
                matcher.add_subject(s)
            for pattern_index, subst1 in matcher.match(tmp22, subst0):
                pass
                if pattern_index == 0:
                    pass
                    # State 50641
                    if len(subjects) == 0:
                        pass
                        # 0: e*x**2
                        yield 0, subst1
                if pattern_index == 1:
                    pass
                    # State 52670
                    if len(subjects) == 0:
                        pass
                        # 1: e/(f + x*g)
                        yield 1, subst1
            subjects.appendleft(tmp20)
        return
        yield


from .generated_part009285 import *
from .generated_part009284 import *
from matchpy.matching.many_to_one import CommutativeMatcher
from collections import deque
from .generated_part009287 import *
from matchpy.utils import VariableWithCount
from multiset import Multiset