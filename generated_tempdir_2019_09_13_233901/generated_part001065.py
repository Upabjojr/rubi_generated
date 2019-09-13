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

class CommutativeMatcher51607(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({0: 1}), [
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
        if CommutativeMatcher51607._instance is None:
            CommutativeMatcher51607._instance = CommutativeMatcher51607()
        return CommutativeMatcher51607._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 51606
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i3.1.2.2.1.0', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 51608
            if len(subjects) >= 1 and isinstance(subjects[0], Pow):
                tmp2 = subjects.popleft()
                subjects3 = deque(tmp2._args)
                # State 51609
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i3.1.2.2.1.2.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 51610
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i3.1.2.2.1.2.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 51611
                        if len(subjects3) >= 1:
                            tmp6 = subjects3.popleft()
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i3.1.2.2.1.2.1.0', tmp6)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 51612
                                if len(subjects3) >= 1 and subjects3[0] == -1:
                                    tmp8 = subjects3.popleft()
                                    # State 51613
                                    if len(subjects3) == 0:
                                        pass
                                        # State 51614
                                        if len(subjects) == 0:
                                            pass
                                            # 0: e/(f + x*g)
                                    subjects3.appendleft(tmp8)
                            subjects3.appendleft(tmp6)
                    if len(subjects3) >= 1 and isinstance(subjects3[0], Mul):
                        tmp9 = subjects3.popleft()
                        associative1 = tmp9
                        associative_type1 = type(tmp9)
                        subjects10 = deque(tmp9._args)
                        matcher = CommutativeMatcher51616.get()
                        tmp11 = subjects10
                        subjects10 = []
                        for s in tmp11:
                            matcher.add_subject(s)
                        for pattern_index, subst3 in matcher.match(tmp11, subst2):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 51617
                                if len(subjects3) >= 1 and subjects3[0] == -1:
                                    tmp12 = subjects3.popleft()
                                    # State 51618
                                    if len(subjects3) == 0:
                                        pass
                                        # State 51619
                                        if len(subjects) == 0:
                                            pass
                                            # 0: e/(f + x*g)
                                    subjects3.appendleft(tmp12)
                        subjects3.appendleft(tmp9)
                if len(subjects3) >= 1 and isinstance(subjects3[0], Add):
                    tmp13 = subjects3.popleft()
                    associative1 = tmp13
                    associative_type1 = type(tmp13)
                    subjects14 = deque(tmp13._args)
                    matcher = CommutativeMatcher51621.get()
                    tmp15 = subjects14
                    subjects14 = []
                    for s in tmp15:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp15, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 51627
                            if len(subjects3) >= 1 and subjects3[0] == -1:
                                tmp16 = subjects3.popleft()
                                # State 51628
                                if len(subjects3) == 0:
                                    pass
                                    # State 51629
                                    if len(subjects) == 0:
                                        pass
                                        # 0: e/(f + x*g)
                                subjects3.appendleft(tmp16)
                    subjects3.appendleft(tmp13)
                subjects.appendleft(tmp2)
        if len(subjects) >= 1 and isinstance(subjects[0], Mul):
            tmp17 = subjects.popleft()
            associative1 = tmp17
            associative_type1 = type(tmp17)
            subjects18 = deque(tmp17._args)
            matcher = CommutativeMatcher51631.get()
            tmp19 = subjects18
            subjects18 = []
            for s in tmp19:
                matcher.add_subject(s)
            for pattern_index, subst1 in matcher.match(tmp19, subst0):
                pass
                if pattern_index == 0:
                    pass
                    # State 51653
                    if len(subjects) == 0:
                        pass
                        # 0: e/(f + x*g)
            subjects.appendleft(tmp17)
        return
        yield


from matchpy.utils import VariableWithCount
from matchpy.matching.many_to_one import CommutativeMatcher
from multiset import Multiset
from collections import deque