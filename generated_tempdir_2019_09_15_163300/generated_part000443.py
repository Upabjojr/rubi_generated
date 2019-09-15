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


class CommutativeMatcher12733(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({0: 1}), [
      (VariableWithCount('i2.2.1.2.0', 1, 1, S(0)), Add)
]),
    1: (1, Multiset({1: 1}), [
      (VariableWithCount('i2.2.1.2.0', 1, 1, None), Add)
]),
    2: (2, Multiset({2: 1}), [
      (VariableWithCount('i2.2.1.2.0_1', 1, 1, S(0)), Add)
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
        if CommutativeMatcher12733._instance is None:
            CommutativeMatcher12733._instance = CommutativeMatcher12733()
        return CommutativeMatcher12733._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 12732
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.2.1.0', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 12734
            subst2 = Substitution(subst1)
            try:
                subst2.try_add_variable('i2.2.1.2.1.2', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 12735
                if len(subjects) >= 1:
                    tmp3 = subjects.popleft()
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.2.1.2.1.1', tmp3)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 12736
                        if len(subjects) == 0:
                            pass
                            # 0: b*x**p
                            yield 0, subst3
                    subjects.appendleft(tmp3)
            if len(subjects) >= 1 and isinstance(subjects[0], Pow):
                tmp5 = subjects.popleft()
                subjects6 = deque(tmp5._args)
                # State 12737
                if len(subjects6) >= 1:
                    tmp7 = subjects6.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.2.1.1', tmp7)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 12738
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.2.1.2', 1)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 12739
                            if len(subjects6) == 0:
                                pass
                                # State 12740
                                if len(subjects) == 0:
                                    pass
                                    # 0: b*x**p
                                    yield 0, subst3
                        if len(subjects6) >= 1:
                            tmp10 = subjects6.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.2.1.2', tmp10)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 12739
                                if len(subjects6) == 0:
                                    pass
                                    # State 12740
                                    if len(subjects) == 0:
                                        pass
                                        # 0: b*x**p
                                        yield 0, subst3
                            subjects6.appendleft(tmp10)
                        if len(subjects6) >= 1:
                            tmp12 = subjects6.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.2.1.2', tmp12)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 14374
                                if len(subjects6) == 0:
                                    pass
                                    # State 14375
                                    if len(subjects) == 0:
                                        pass
                                        # 1: b*x**n
                                        yield 1, subst3
                            subjects6.appendleft(tmp12)
                    subjects6.appendleft(tmp7)
                subjects.appendleft(tmp5)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.2.1.0_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 151555
            subst2 = Substitution(subst1)
            try:
                subst2.try_add_variable('i2.2.1.2.1.2', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 151556
                if len(subjects) >= 1:
                    tmp16 = subjects.popleft()
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.2.1.2.1.1', tmp16)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 151557
                        if len(subjects) == 0:
                            pass
                            # 2: d*x**n
                            yield 2, subst3
                    subjects.appendleft(tmp16)
            if len(subjects) >= 1 and isinstance(subjects[0], Pow):
                tmp18 = subjects.popleft()
                subjects19 = deque(tmp18._args)
                # State 151558
                if len(subjects19) >= 1:
                    tmp20 = subjects19.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.2.1.1', tmp20)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 151559
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.2.1.2', 1)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 151560
                            if len(subjects19) == 0:
                                pass
                                # State 151561
                                if len(subjects) == 0:
                                    pass
                                    # 2: d*x**n
                                    yield 2, subst3
                        if len(subjects19) >= 1:
                            tmp23 = subjects19.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.2.1.2', tmp23)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 151560
                                if len(subjects19) == 0:
                                    pass
                                    # State 151561
                                    if len(subjects) == 0:
                                        pass
                                        # 2: d*x**n
                                        yield 2, subst3
                            subjects19.appendleft(tmp23)
                    subjects19.appendleft(tmp20)
                subjects.appendleft(tmp18)
        if len(subjects) >= 1 and isinstance(subjects[0], Mul):
            tmp25 = subjects.popleft()
            associative1 = tmp25
            associative_type1 = type(tmp25)
            subjects26 = deque(tmp25._args)
            matcher = CommutativeMatcher12742.get()
            tmp27 = subjects26
            subjects26 = []
            for s in tmp27:
                matcher.add_subject(s)
            for pattern_index, subst1 in matcher.match(tmp27, subst0):
                pass
                if pattern_index == 0:
                    pass
                    # State 12749
                    if len(subjects) == 0:
                        pass
                        # 0: b*x**p
                        yield 0, subst1
                if pattern_index == 1:
                    pass
                    # State 14378
                    if len(subjects) == 0:
                        pass
                        # 1: b*x**n
                        yield 1, subst1
                if pattern_index == 2:
                    pass
                    # State 151562
                    if len(subjects) == 0:
                        pass
                        # 2: d*x**n
                        yield 2, subst1
            subjects.appendleft(tmp25)
        return
        yield


from .generated_part000444 import *
from matchpy.matching.many_to_one import CommutativeMatcher
from collections import deque
from matchpy.utils import VariableWithCount
from multiset import Multiset