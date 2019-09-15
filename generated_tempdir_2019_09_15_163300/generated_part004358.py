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


class CommutativeMatcher64597(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({0: 1}), [
      (VariableWithCount('i2.4.0', 1, 1, S(0)), Add)
]),
    1: (1, Multiset({1: 1}), [
      (VariableWithCount('i2.4.0', 1, 1, S(0)), Add)
]),
    2: (2, Multiset({2: 1}), [
      (VariableWithCount('i2.4.0', 1, 1, S(0)), Add)
])
}
    subjects = {}
    subjects_by_id = {}
    bipartite = BipartiteGraph()
    associative = Add
    max_optional_count = 1
    anonymous_patterns = set()

    def __init__(self):
        self.add_subject(None)

    @staticmethod
    def get():
        if CommutativeMatcher64597._instance is None:
            CommutativeMatcher64597._instance = CommutativeMatcher64597()
        return CommutativeMatcher64597._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 64596
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.4.1.0_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 64598
            if len(subjects) >= 1:
                tmp2 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.4.1.0', tmp2)
                except ValueError:
                    pass
                else:
                    pass
                    # State 64599
                    if len(subjects) == 0:
                        pass
                        # 0: x*f
                        yield 0, subst2
                subjects.appendleft(tmp2)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.4.1.0', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 89230
            subst2 = Substitution(subst1)
            try:
                subst2.try_add_variable('i2.4.1.2', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 89231
                if len(subjects) >= 1:
                    tmp6 = subjects.popleft()
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.4.1.1', tmp6)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 89232
                        if len(subjects) == 0:
                            pass
                            # 1: b*x**n
                            yield 1, subst3
                    subjects.appendleft(tmp6)
            if len(subjects) >= 1 and isinstance(subjects[0], Pow):
                tmp8 = subjects.popleft()
                subjects9 = deque(tmp8._args)
                # State 89233
                if len(subjects9) >= 1:
                    tmp10 = subjects9.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.4.1.1', tmp10)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 89234
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.4.1.2', 1)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 89235
                            if len(subjects9) == 0:
                                pass
                                # State 89236
                                if len(subjects) == 0:
                                    pass
                                    # 1: b*x**n
                                    yield 1, subst3
                        if len(subjects9) >= 1:
                            tmp13 = subjects9.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.4.1.2', tmp13)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 89235
                                if len(subjects9) == 0:
                                    pass
                                    # State 89236
                                    if len(subjects) == 0:
                                        pass
                                        # 1: b*x**n
                                        yield 1, subst3
                            subjects9.appendleft(tmp13)
                    subjects9.appendleft(tmp10)
                subjects.appendleft(tmp8)
            if len(subjects) >= 1 and isinstance(subjects[0], log):
                tmp15 = subjects.popleft()
                subjects16 = deque(tmp15._args)
                # State 106670
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.4.1.2.0', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 106671
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.4.1.2.2', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 106672
                        if len(subjects16) >= 1:
                            tmp19 = subjects16.popleft()
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i2.4.1.2.1', tmp19)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 106673
                                if len(subjects16) == 0:
                                    pass
                                    # State 106674
                                    if len(subjects) == 0:
                                        pass
                                        # 2: b*log(c*x**n)
                                        yield 2, subst4
                            subjects16.appendleft(tmp19)
                    if len(subjects16) >= 1 and isinstance(subjects16[0], Pow):
                        tmp21 = subjects16.popleft()
                        subjects22 = deque(tmp21._args)
                        # State 106675
                        if len(subjects22) >= 1:
                            tmp23 = subjects22.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.4.1.2.1', tmp23)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 106676
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.4.1.2.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 106677
                                    if len(subjects22) == 0:
                                        pass
                                        # State 106678
                                        if len(subjects16) == 0:
                                            pass
                                            # State 106679
                                            if len(subjects) == 0:
                                                pass
                                                # 2: b*log(c*x**n)
                                                yield 2, subst4
                                if len(subjects22) >= 1:
                                    tmp26 = subjects22.popleft()
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i2.4.1.2.2', tmp26)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 106677
                                        if len(subjects22) == 0:
                                            pass
                                            # State 106678
                                            if len(subjects16) == 0:
                                                pass
                                                # State 106679
                                                if len(subjects) == 0:
                                                    pass
                                                    # 2: b*log(c*x**n)
                                                    yield 2, subst4
                                    subjects22.appendleft(tmp26)
                            subjects22.appendleft(tmp23)
                        subjects16.appendleft(tmp21)
                if len(subjects16) >= 1 and isinstance(subjects16[0], Mul):
                    tmp28 = subjects16.popleft()
                    associative1 = tmp28
                    associative_type1 = type(tmp28)
                    subjects29 = deque(tmp28._args)
                    matcher = CommutativeMatcher106681.get()
                    tmp30 = subjects29
                    subjects29 = []
                    for s in tmp30:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp30, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 106688
                            if len(subjects16) == 0:
                                pass
                                # State 106689
                                if len(subjects) == 0:
                                    pass
                                    # 2: b*log(c*x**n)
                                    yield 2, subst2
                    subjects16.appendleft(tmp28)
                subjects.appendleft(tmp15)
        if len(subjects) >= 1 and isinstance(subjects[0], Mul):
            tmp31 = subjects.popleft()
            associative1 = tmp31
            associative_type1 = type(tmp31)
            subjects32 = deque(tmp31._args)
            matcher = CommutativeMatcher64601.get()
            tmp33 = subjects32
            subjects32 = []
            for s in tmp33:
                matcher.add_subject(s)
            for pattern_index, subst1 in matcher.match(tmp33, subst0):
                pass
                if pattern_index == 0:
                    pass
                    # State 64602
                    if len(subjects) == 0:
                        pass
                        # 0: x*f
                        yield 0, subst1
                if pattern_index == 1:
                    pass
                    # State 89243
                    if len(subjects) == 0:
                        pass
                        # 1: b*x**n
                        yield 1, subst1
                if pattern_index == 2:
                    pass
                    # State 106710
                    if len(subjects) == 0:
                        pass
                        # 2: b*log(c*x**n)
                        yield 2, subst1
            subjects.appendleft(tmp31)
        return
        yield


from .generated_part004359 import *
from matchpy.matching.many_to_one import CommutativeMatcher
from collections import deque
from .generated_part004360 import *
from matchpy.utils import VariableWithCount
from multiset import Multiset