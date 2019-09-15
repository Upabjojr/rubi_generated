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


class CommutativeMatcher133120(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({0: 1}), [
      (VariableWithCount('i4.0', 1, 1, S(1)), Mul)
]),
    1: (1, Multiset({1: 1}), [
      (VariableWithCount('i4.0', 1, 1, S(1)), Mul)
]),
    2: (2, Multiset({2: 1, 3: 1}), [
      (VariableWithCount('i4.0', 1, 1, S(1)), Mul)
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
        if CommutativeMatcher133120._instance is None:
            CommutativeMatcher133120._instance = CommutativeMatcher133120()
        return CommutativeMatcher133120._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 133119
        if len(subjects) >= 1 and isinstance(subjects[0], log):
            tmp1 = subjects.popleft()
            subjects2 = deque(tmp1._args)
            # State 133121
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i4.2.0', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 133122
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i4.2.2', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 133123
                    if len(subjects2) >= 1:
                        tmp5 = subjects2.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i4.2.1', tmp5)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 133124
                            if len(subjects2) == 0:
                                pass
                                # State 133125
                                if len(subjects) == 0:
                                    pass
                                    # 0: log(c*x**n) /; (cons_f8) and (cons_f1875)
                                    yield 0, subst3
                        subjects2.appendleft(tmp5)
                if len(subjects2) >= 1 and isinstance(subjects2[0], Pow):
                    tmp7 = subjects2.popleft()
                    subjects8 = deque(tmp7._args)
                    # State 133126
                    if len(subjects8) >= 1:
                        tmp9 = subjects8.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i4.2.1', tmp9)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 133127
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i4.2.2', 1)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 133128
                                if len(subjects8) == 0:
                                    pass
                                    # State 133129
                                    if len(subjects2) == 0:
                                        pass
                                        # State 133130
                                        if len(subjects) == 0:
                                            pass
                                            # 0: log(c*x**n) /; (cons_f8) and (cons_f1875)
                                            yield 0, subst3
                            if len(subjects8) >= 1:
                                tmp12 = subjects8.popleft()
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i4.2.2', tmp12)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 133128
                                    if len(subjects8) == 0:
                                        pass
                                        # State 133129
                                        if len(subjects2) == 0:
                                            pass
                                            # State 133130
                                            if len(subjects) == 0:
                                                pass
                                                # 0: log(c*x**n) /; (cons_f8) and (cons_f1875)
                                                yield 0, subst3
                                subjects8.appendleft(tmp12)
                        subjects8.appendleft(tmp9)
                    subjects2.appendleft(tmp7)
            if len(subjects2) >= 1 and isinstance(subjects2[0], Mul):
                tmp14 = subjects2.popleft()
                associative1 = tmp14
                associative_type1 = type(tmp14)
                subjects15 = deque(tmp14._args)
                matcher = CommutativeMatcher133132.get()
                tmp16 = subjects15
                subjects15 = []
                for s in tmp16:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp16, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 133139
                        if len(subjects2) == 0:
                            pass
                            # State 133140
                            if len(subjects) == 0:
                                pass
                                # 0: log(c*x**n) /; (cons_f8) and (cons_f1875)
                                yield 0, subst1
                subjects2.appendleft(tmp14)
            subjects.appendleft(tmp1)
        if len(subjects) >= 1 and isinstance(subjects[0], Pow):
            tmp17 = subjects.popleft()
            subjects18 = deque(tmp17._args)
            # State 136605
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i4.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 136606
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i4.2.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 136607
                    if len(subjects18) >= 1:
                        tmp21 = subjects18.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i4.2.1.0', tmp21)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 136608
                            if len(subjects18) >= 1 and subjects18[0] == Integer(-1):
                                tmp23 = subjects18.popleft()
                                # State 136609
                                if len(subjects18) == 0:
                                    pass
                                    # State 136610
                                    if len(subjects) == 0:
                                        pass
                                        # 1: 1/(c + x*d) /; (cons_f2) and (cons_f8) and (cons_f29)
                                        yield 1, subst3
                                        # 2: 1/(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f73)
                                        yield 2, subst3
                                subjects18.appendleft(tmp23)
                        subjects18.appendleft(tmp21)
                if len(subjects18) >= 1 and isinstance(subjects18[0], Mul):
                    tmp24 = subjects18.popleft()
                    associative1 = tmp24
                    associative_type1 = type(tmp24)
                    subjects25 = deque(tmp24._args)
                    matcher = CommutativeMatcher136612.get()
                    tmp26 = subjects25
                    subjects25 = []
                    for s in tmp26:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp26, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 136613
                            if len(subjects18) >= 1 and subjects18[0] == Integer(-1):
                                tmp27 = subjects18.popleft()
                                # State 136614
                                if len(subjects18) == 0:
                                    pass
                                    # State 136615
                                    if len(subjects) == 0:
                                        pass
                                        # 1: 1/(c + x*d) /; (cons_f2) and (cons_f8) and (cons_f29)
                                        yield 1, subst2
                                        # 2: 1/(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f73)
                                        yield 2, subst2
                                subjects18.appendleft(tmp27)
                    subjects18.appendleft(tmp24)
            if len(subjects18) >= 1 and isinstance(subjects18[0], Add):
                tmp28 = subjects18.popleft()
                associative1 = tmp28
                associative_type1 = type(tmp28)
                subjects29 = deque(tmp28._args)
                matcher = CommutativeMatcher136617.get()
                tmp30 = subjects29
                subjects29 = []
                for s in tmp30:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp30, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 136623
                        if len(subjects18) >= 1 and subjects18[0] == Integer(-1):
                            tmp31 = subjects18.popleft()
                            # State 136624
                            if len(subjects18) == 0:
                                pass
                                # State 136625
                                if len(subjects) == 0:
                                    pass
                                    # 1: 1/(c + x*d) /; (cons_f2) and (cons_f8) and (cons_f29)
                                    yield 1, subst1
                                    # 2: 1/(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f73)
                                    yield 2, subst1
                            subjects18.appendleft(tmp31)
                subjects18.appendleft(tmp28)
            subjects.appendleft(tmp17)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i4.1.0', S(0))
        except ValueError:
            pass
        else:
            pass
            # State 136731
            subst2 = Substitution(subst1)
            try:
                subst2.try_add_variable('i4.1.1.0', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 136732
                if len(subjects) >= 1:
                    tmp34 = subjects.popleft()
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i4.2.1.0', tmp34)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 136733
                        if len(subjects) == 0:
                            pass
                            # 3: a + b*x /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f73)
                            yield 3, subst3
                    subjects.appendleft(tmp34)
            if len(subjects) >= 1 and isinstance(subjects[0], Mul):
                tmp36 = subjects.popleft()
                associative1 = tmp36
                associative_type1 = type(tmp36)
                subjects37 = deque(tmp36._args)
                matcher = CommutativeMatcher136735.get()
                tmp38 = subjects37
                subjects37 = []
                for s in tmp38:
                    matcher.add_subject(s)
                for pattern_index, subst2 in matcher.match(tmp38, subst1):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 136736
                        if len(subjects) == 0:
                            pass
                            # 3: a + b*x /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f73)
                            yield 3, subst2
                subjects.appendleft(tmp36)
        if len(subjects) >= 1 and isinstance(subjects[0], Add):
            tmp39 = subjects.popleft()
            associative1 = tmp39
            associative_type1 = type(tmp39)
            subjects40 = deque(tmp39._args)
            matcher = CommutativeMatcher136738.get()
            tmp41 = subjects40
            subjects40 = []
            for s in tmp41:
                matcher.add_subject(s)
            for pattern_index, subst1 in matcher.match(tmp41, subst0):
                pass
                if pattern_index == 0:
                    pass
                    # State 136744
                    if len(subjects) == 0:
                        pass
                        # 3: a + b*x /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f73)
                        yield 3, subst1
            subjects.appendleft(tmp39)
        return
        yield


from .generated_part001657 import *
from .generated_part001655 import *
from matchpy.matching.many_to_one import CommutativeMatcher
from .generated_part001658 import *
from .generated_part001653 import *
from collections import deque
from .generated_part001654 import *
from matchpy.utils import VariableWithCount
from multiset import Multiset