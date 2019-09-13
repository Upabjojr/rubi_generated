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

class CommutativeMatcher128791(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({0: 1}), [
      (VariableWithCount('i2.4.1.0', 1, 1, S(1)), Mul)
]),
    1: (1, Multiset({}), [
      (VariableWithCount('i2.4.1.0', 1, 1, None), Mul),
      (VariableWithCount('i2.4.1.0_1', 1, 1, S(1)), Mul)
]),
    2: (2, Multiset({1: 1}), [
      (VariableWithCount('i2.4.1.0', 1, 1, S(1)), Mul)
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
        if CommutativeMatcher128791._instance is None:
            CommutativeMatcher128791._instance = CommutativeMatcher128791()
        return CommutativeMatcher128791._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 128790
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.4.1.2', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 128792
            if len(subjects) >= 1:
                tmp2 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.4.1.1', tmp2)
                except ValueError:
                    pass
                else:
                    pass
                    # State 128793
                    if len(subjects) == 0:
                        pass
                        # 0: x**n
                subjects.appendleft(tmp2)
        if len(subjects) >= 1 and isinstance(subjects[0], Pow):
            tmp4 = subjects.popleft()
            subjects5 = deque(tmp4._args)
            # State 128794
            if len(subjects5) >= 1:
                tmp6 = subjects5.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.4.1.1', tmp6)
                except ValueError:
                    pass
                else:
                    pass
                    # State 128795
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.4.1.2', 1)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 128796
                        if len(subjects5) == 0:
                            pass
                            # State 128797
                            if len(subjects) == 0:
                                pass
                                # 0: x**n
                    if len(subjects5) >= 1:
                        tmp9 = subjects5.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.4.1.2', tmp9)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 128796
                            if len(subjects5) == 0:
                                pass
                                # State 128797
                                if len(subjects) == 0:
                                    pass
                                    # 0: x**n
                        subjects5.appendleft(tmp9)
                subjects5.appendleft(tmp6)
            subjects.appendleft(tmp4)
        if len(subjects) >= 1 and isinstance(subjects[0], log):
            tmp11 = subjects.popleft()
            subjects12 = deque(tmp11._args)
            # State 136283
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.4.1.2.0', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 136284
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.4.1.2.2', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 136285
                    if len(subjects12) >= 1:
                        tmp15 = subjects12.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.4.1.2.1', tmp15)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 136286
                            if len(subjects12) == 0:
                                pass
                                # State 136287
                                if len(subjects) == 0:
                                    pass
                                    # 1: log(c*x**n)
                        subjects12.appendleft(tmp15)
                if len(subjects12) >= 1 and isinstance(subjects12[0], Pow):
                    tmp17 = subjects12.popleft()
                    subjects18 = deque(tmp17._args)
                    # State 136288
                    if len(subjects18) >= 1:
                        tmp19 = subjects18.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.4.1.2.1', tmp19)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 136289
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.4.1.2.2', 1)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 136290
                                if len(subjects18) == 0:
                                    pass
                                    # State 136291
                                    if len(subjects12) == 0:
                                        pass
                                        # State 136292
                                        if len(subjects) == 0:
                                            pass
                                            # 1: log(c*x**n)
                            if len(subjects18) >= 1:
                                tmp22 = subjects18.popleft()
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i2.4.1.2.2', tmp22)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 136290
                                    if len(subjects18) == 0:
                                        pass
                                        # State 136291
                                        if len(subjects12) == 0:
                                            pass
                                            # State 136292
                                            if len(subjects) == 0:
                                                pass
                                                # 1: log(c*x**n)
                                subjects18.appendleft(tmp22)
                        subjects18.appendleft(tmp19)
                    subjects12.appendleft(tmp17)
            if len(subjects12) >= 1 and isinstance(subjects12[0], Mul):
                tmp24 = subjects12.popleft()
                associative1 = tmp24
                associative_type1 = type(tmp24)
                subjects25 = deque(tmp24._args)
                matcher = CommutativeMatcher136294.get()
                tmp26 = subjects25
                subjects25 = []
                for s in tmp26:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp26, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 136301
                        if len(subjects12) == 0:
                            pass
                            # State 136302
                            if len(subjects) == 0:
                                pass
                                # 1: log(c*x**n)
                subjects12.appendleft(tmp24)
            subjects.appendleft(tmp11)
        return
        yield


from matchpy.utils import VariableWithCount
from matchpy.matching.many_to_one import CommutativeMatcher
from multiset import Multiset
from collections import deque
