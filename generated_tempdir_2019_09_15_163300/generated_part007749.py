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


class CommutativeMatcher123466(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({0: 1}), [
      (VariableWithCount('i2.2.0', 1, 1, S(1)), Mul)
]),
    1: (1, Multiset({1: 1}), [
      (VariableWithCount('i2.2.0', 1, 1, S(1)), Mul),
      (VariableWithCount('i2.3.0', 1, 1, None), Mul)
]),
    2: (2, Multiset({1: 1, 2: 1}), [
      (VariableWithCount('i2.2.0', 1, 1, S(1)), Mul)
]),
    3: (3, Multiset({1: 1, 3: 1}), [
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
        if CommutativeMatcher123466._instance is None:
            CommutativeMatcher123466._instance = CommutativeMatcher123466()
        return CommutativeMatcher123466._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 123465
        if len(subjects) >= 1 and isinstance(subjects[0], Pow):
            tmp1 = subjects.popleft()
            subjects2 = deque(tmp1._args)
            # State 123467
            if len(subjects2) >= 1:
                tmp3 = subjects2.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.1', tmp3)
                except ValueError:
                    pass
                else:
                    pass
                    # State 123468
                    if len(subjects2) >= 1:
                        tmp5 = subjects2.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.2', tmp5)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 123469
                            if len(subjects2) == 0:
                                pass
                                # State 123470
                                if len(subjects) == 0:
                                    pass
                                    # 0: x**n
                                    yield 0, subst2
                        subjects2.appendleft(tmp5)
                subjects2.appendleft(tmp3)
            if len(subjects2) >= 1:
                tmp7 = subjects2.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.3.0', tmp7)
                except ValueError:
                    pass
                else:
                    pass
                    # State 136425
                    if len(subjects2) >= 1:
                        tmp9 = subjects2.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.2', tmp9)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 136426
                            if len(subjects2) == 0:
                                pass
                                # State 136427
                                if len(subjects) == 0:
                                    pass
                                    # 2: x**n
                                    yield 2, subst2
                        subjects2.appendleft(tmp9)
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.2', 1)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 136444
                        if len(subjects2) == 0:
                            pass
                            # State 136445
                            if len(subjects) == 0:
                                pass
                                # 3: x**n
                                yield 3, subst2
                    if len(subjects2) >= 1:
                        tmp12 = subjects2.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.2', tmp12)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 136444
                            if len(subjects2) == 0:
                                pass
                                # State 136445
                                if len(subjects) == 0:
                                    pass
                                    # 3: x**n
                                    yield 3, subst2
                        subjects2.appendleft(tmp12)
                subjects2.appendleft(tmp7)
            if len(subjects2) >= 1 and isinstance(subjects2[0], log):
                tmp14 = subjects2.popleft()
                subjects15 = deque(tmp14._args)
                # State 136400
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.3.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 136401
                    if len(subjects15) >= 1:
                        tmp17 = subjects15.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.3.0', tmp17)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 136402
                            if len(subjects15) == 0:
                                pass
                                # State 136403
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i2.3', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 136404
                                    if len(subjects2) == 0:
                                        pass
                                        # State 136405
                                        if len(subjects) == 0:
                                            pass
                                            # 1: log(v*c)**p
                                            yield 1, subst3
                                if len(subjects2) >= 1:
                                    tmp20 = subjects2.popleft()
                                    subst3 = Substitution(subst2)
                                    try:
                                        subst3.try_add_variable('i2.3', tmp20)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 136404
                                        if len(subjects2) == 0:
                                            pass
                                            # State 136405
                                            if len(subjects) == 0:
                                                pass
                                                # 1: log(v*c)**p
                                                yield 1, subst3
                                    subjects2.appendleft(tmp20)
                        subjects15.appendleft(tmp17)
                if len(subjects15) >= 1 and isinstance(subjects15[0], Mul):
                    tmp22 = subjects15.popleft()
                    associative1 = tmp22
                    associative_type1 = type(tmp22)
                    subjects23 = deque(tmp22._args)
                    matcher = CommutativeMatcher136407.get()
                    tmp24 = subjects23
                    subjects23 = []
                    for s in tmp24:
                        matcher.add_subject(s)
                    for pattern_index, subst1 in matcher.match(tmp24, subst0):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 136408
                            if len(subjects15) == 0:
                                pass
                                # State 136409
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i2.3', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 136410
                                    if len(subjects2) == 0:
                                        pass
                                        # State 136411
                                        if len(subjects) == 0:
                                            pass
                                            # 1: log(v*c)**p
                                            yield 1, subst2
                                if len(subjects2) >= 1:
                                    tmp26 = subjects2.popleft()
                                    subst2 = Substitution(subst1)
                                    try:
                                        subst2.try_add_variable('i2.3', tmp26)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 136410
                                        if len(subjects2) == 0:
                                            pass
                                            # State 136411
                                            if len(subjects) == 0:
                                                pass
                                                # 1: log(v*c)**p
                                                yield 1, subst2
                                    subjects2.appendleft(tmp26)
                    subjects15.appendleft(tmp22)
                subjects2.appendleft(tmp14)
            subjects.appendleft(tmp1)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.3', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 136391
            if len(subjects) >= 1 and isinstance(subjects[0], log):
                tmp29 = subjects.popleft()
                subjects30 = deque(tmp29._args)
                # State 136392
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.3.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 136393
                    if len(subjects30) >= 1:
                        tmp32 = subjects30.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.3.0', tmp32)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 136394
                            if len(subjects30) == 0:
                                pass
                                # State 136395
                                if len(subjects) == 0:
                                    pass
                                    # 1: log(v*c)**p
                                    yield 1, subst3
                        subjects30.appendleft(tmp32)
                if len(subjects30) >= 1 and isinstance(subjects30[0], Mul):
                    tmp34 = subjects30.popleft()
                    associative1 = tmp34
                    associative_type1 = type(tmp34)
                    subjects35 = deque(tmp34._args)
                    matcher = CommutativeMatcher136397.get()
                    tmp36 = subjects35
                    subjects35 = []
                    for s in tmp36:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp36, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 136398
                            if len(subjects30) == 0:
                                pass
                                # State 136399
                                if len(subjects) == 0:
                                    pass
                                    # 1: log(v*c)**p
                                    yield 1, subst2
                    subjects30.appendleft(tmp34)
                subjects.appendleft(tmp29)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.2', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 136442
            if len(subjects) >= 1:
                tmp38 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.3.0', tmp38)
                except ValueError:
                    pass
                else:
                    pass
                    # State 136443
                    if len(subjects) == 0:
                        pass
                        # 3: x**n
                        yield 3, subst2
                subjects.appendleft(tmp38)
        return
        yield


from matchpy.matching.many_to_one import CommutativeMatcher
from .generated_part007751 import *
from .generated_part007750 import *
from collections import deque
from matchpy.utils import VariableWithCount
from multiset import Multiset