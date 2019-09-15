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


class CommutativeMatcher125582(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({0: 1, 1: 1}), [
      (VariableWithCount('i4.0', 1, 1, S(0)), Add)
]),
    1: (1, Multiset({2: 1}), [
      (VariableWithCount('i4.0', 1, 1, S(0)), Add)
]),
    2: (2, Multiset({3: 1}), [
      (VariableWithCount('i4.0', 1, 1, S(0)), Add)
]),
    3: (3, Multiset({4: 1}), [
      (VariableWithCount('i4.0', 1, 1, S(0)), Add)
]),
    4: (4, Multiset({5: 1}), [
      (VariableWithCount('i4.0', 1, 1, S(0)), Add)
]),
    5: (5, Multiset({6: 1}), [
      (VariableWithCount('i4.0', 1, 1, S(0)), Add)
]),
    6: (6, Multiset({7: 1}), [
      (VariableWithCount('i4.0', 1, 1, S(0)), Add)
]),
    7: (7, Multiset({8: 1}), [
      (VariableWithCount('i4.0', 1, 1, S(0)), Add)
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
        if CommutativeMatcher125582._instance is None:
            CommutativeMatcher125582._instance = CommutativeMatcher125582()
        return CommutativeMatcher125582._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 125581
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i4.1.0', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 125583
            if len(subjects) >= 1 and isinstance(subjects[0], Pow):
                tmp2 = subjects.popleft()
                subjects3 = deque(tmp2._args)
                # State 125584
                if len(subjects3) >= 1:
                    tmp4 = subjects3.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i4.1.1', tmp4)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 125585
                        if len(subjects3) >= 1 and subjects3[0] == Integer(2):
                            tmp6 = subjects3.popleft()
                            # State 125586
                            if len(subjects3) == 0:
                                pass
                                # State 125587
                                if len(subjects) == 0:
                                    pass
                                    # 0: c*x**2 /; (cons_f2) and (cons_f3) and (cons_f8)
                                    yield 0, subst2
                            subjects3.appendleft(tmp6)
                    subjects3.appendleft(tmp4)
                subjects.appendleft(tmp2)
            if len(subjects) >= 1 and isinstance(subjects[0], log):
                tmp7 = subjects.popleft()
                subjects8 = deque(tmp7._args)
                # State 133274
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i4.1.2.0', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 133275
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i4.1.2.2', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 133276
                        if len(subjects8) >= 1:
                            tmp11 = subjects8.popleft()
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i4.1.2.1', tmp11)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 133277
                                if len(subjects8) == 0:
                                    pass
                                    # State 133278
                                    if len(subjects) == 0:
                                        pass
                                        # 2: b*log(c*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f1876)
                                        yield 2, subst4
                                        # 3: b*log(c*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f1877)
                                        yield 3, subst4
                                        # 4: b*log(c*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f1878)
                                        yield 4, subst4
                                        # 5: b*log(c*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f1880)
                                        yield 5, subst4
                                        # 6: b*log(c*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f1881)
                                        yield 6, subst4
                                        # 7: b*log(c*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f1880)
                                        yield 7, subst4
                                        # 8: b*log(c*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f1887)
                                        yield 8, subst4
                            subjects8.appendleft(tmp11)
                    if len(subjects8) >= 1 and isinstance(subjects8[0], Pow):
                        tmp13 = subjects8.popleft()
                        subjects14 = deque(tmp13._args)
                        # State 133279
                        if len(subjects14) >= 1:
                            tmp15 = subjects14.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i4.1.2.1', tmp15)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 133280
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i4.1.2.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 133281
                                    if len(subjects14) == 0:
                                        pass
                                        # State 133282
                                        if len(subjects8) == 0:
                                            pass
                                            # State 133283
                                            if len(subjects) == 0:
                                                pass
                                                # 2: b*log(c*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f1876)
                                                yield 2, subst4
                                                # 3: b*log(c*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f1877)
                                                yield 3, subst4
                                                # 4: b*log(c*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f1878)
                                                yield 4, subst4
                                                # 5: b*log(c*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f1880)
                                                yield 5, subst4
                                                # 6: b*log(c*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f1881)
                                                yield 6, subst4
                                                # 7: b*log(c*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f1880)
                                                yield 7, subst4
                                                # 8: b*log(c*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f1887)
                                                yield 8, subst4
                                if len(subjects14) >= 1:
                                    tmp18 = subjects14.popleft()
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i4.1.2.2', tmp18)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 133281
                                        if len(subjects14) == 0:
                                            pass
                                            # State 133282
                                            if len(subjects8) == 0:
                                                pass
                                                # State 133283
                                                if len(subjects) == 0:
                                                    pass
                                                    # 2: b*log(c*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f1876)
                                                    yield 2, subst4
                                                    # 3: b*log(c*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f1877)
                                                    yield 3, subst4
                                                    # 4: b*log(c*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f1878)
                                                    yield 4, subst4
                                                    # 5: b*log(c*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f1880)
                                                    yield 5, subst4
                                                    # 6: b*log(c*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f1881)
                                                    yield 6, subst4
                                                    # 7: b*log(c*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f1880)
                                                    yield 7, subst4
                                                    # 8: b*log(c*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f1887)
                                                    yield 8, subst4
                                    subjects14.appendleft(tmp18)
                            subjects14.appendleft(tmp15)
                        subjects8.appendleft(tmp13)
                if len(subjects8) >= 1 and isinstance(subjects8[0], Mul):
                    tmp20 = subjects8.popleft()
                    associative1 = tmp20
                    associative_type1 = type(tmp20)
                    subjects21 = deque(tmp20._args)
                    matcher = CommutativeMatcher133285.get()
                    tmp22 = subjects21
                    subjects21 = []
                    for s in tmp22:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp22, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 133292
                            if len(subjects8) == 0:
                                pass
                                # State 133293
                                if len(subjects) == 0:
                                    pass
                                    # 2: b*log(c*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f1876)
                                    yield 2, subst2
                                    # 3: b*log(c*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f1877)
                                    yield 3, subst2
                                    # 4: b*log(c*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f1878)
                                    yield 4, subst2
                                    # 5: b*log(c*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f1880)
                                    yield 5, subst2
                                    # 6: b*log(c*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f1881)
                                    yield 6, subst2
                                    # 7: b*log(c*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f1880)
                                    yield 7, subst2
                                    # 8: b*log(c*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f1887)
                                    yield 8, subst2
                    subjects8.appendleft(tmp20)
                subjects.appendleft(tmp7)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i4.1.0_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 125595
            if len(subjects) >= 1:
                tmp24 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i4.1.1', tmp24)
                except ValueError:
                    pass
                else:
                    pass
                    # State 125596
                    if len(subjects) == 0:
                        pass
                        # 1: b*x /; (cons_f2) and (cons_f3) and (cons_f8)
                        yield 1, subst2
                subjects.appendleft(tmp24)
        if len(subjects) >= 1 and isinstance(subjects[0], Mul):
            tmp26 = subjects.popleft()
            associative1 = tmp26
            associative_type1 = type(tmp26)
            subjects27 = deque(tmp26._args)
            matcher = CommutativeMatcher125589.get()
            tmp28 = subjects27
            subjects27 = []
            for s in tmp28:
                matcher.add_subject(s)
            for pattern_index, subst1 in matcher.match(tmp28, subst0):
                pass
                if pattern_index == 0:
                    pass
                    # State 125594
                    if len(subjects) == 0:
                        pass
                        # 0: c*x**2 /; (cons_f2) and (cons_f3) and (cons_f8)
                        yield 0, subst1
                if pattern_index == 1:
                    pass
                    # State 125597
                    if len(subjects) == 0:
                        pass
                        # 1: b*x /; (cons_f2) and (cons_f3) and (cons_f8)
                        yield 1, subst1
                if pattern_index == 2:
                    pass
                    # State 133314
                    if len(subjects) == 0:
                        pass
                        # 2: b*log(c*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f1876)
                        yield 2, subst1
                        # 3: b*log(c*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f1877)
                        yield 3, subst1
                        # 4: b*log(c*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f1878)
                        yield 4, subst1
                        # 5: b*log(c*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f1880)
                        yield 5, subst1
                        # 6: b*log(c*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f1881)
                        yield 6, subst1
                        # 7: b*log(c*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f1880)
                        yield 7, subst1
                        # 8: b*log(c*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f1887)
                        yield 8, subst1
            subjects.appendleft(tmp26)
        return
        yield


from .generated_part010075 import *
from matchpy.matching.many_to_one import CommutativeMatcher
from .generated_part010074 import *
from collections import deque
from matchpy.utils import VariableWithCount
from multiset import Multiset