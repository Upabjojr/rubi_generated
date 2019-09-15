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


class CommutativeMatcher146350(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({0: 1}), [
      (VariableWithCount('i2.3.0', 1, 1, S(1)), Mul)
]),
    1: (1, Multiset({1: 1}), [
      (VariableWithCount('i2.2.1.1', 1, 1, None), Mul),
      (VariableWithCount('i2.3.0', 1, 1, S(1)), Mul)
]),
    2: (2, Multiset({2: 1}), [
      (VariableWithCount('i2.2.1.1', 1, 1, None), Mul),
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
        if CommutativeMatcher146350._instance is None:
            CommutativeMatcher146350._instance = CommutativeMatcher146350()
        return CommutativeMatcher146350._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 146349
        if len(subjects) >= 1 and isinstance(subjects[0], Pow):
            tmp1 = subjects.popleft()
            subjects2 = deque(tmp1._args)
            # State 146351
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.3.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 146352
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.3.2.1.0', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 146353
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.3.2.1.2', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 146354
                        if len(subjects2) >= 1:
                            tmp6 = subjects2.popleft()
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i2.3.2.1.1', tmp6)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 146355
                                if len(subjects2) >= 1 and subjects2[0] == Integer(-1):
                                    tmp8 = subjects2.popleft()
                                    # State 146356
                                    if len(subjects2) == 0:
                                        pass
                                        # State 146357
                                        if len(subjects) == 0:
                                            pass
                                            # 0: 1/(a + b*x**n)
                                            yield 0, subst4
                                    subjects2.appendleft(tmp8)
                            subjects2.appendleft(tmp6)
                    if len(subjects2) >= 1 and isinstance(subjects2[0], Pow):
                        tmp9 = subjects2.popleft()
                        subjects10 = deque(tmp9._args)
                        # State 146358
                        if len(subjects10) >= 1:
                            tmp11 = subjects10.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.3.2.1.1', tmp11)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 146359
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.3.2.1.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 146360
                                    if len(subjects10) == 0:
                                        pass
                                        # State 146361
                                        if len(subjects2) >= 1 and subjects2[0] == Integer(-1):
                                            tmp14 = subjects2.popleft()
                                            # State 146362
                                            if len(subjects2) == 0:
                                                pass
                                                # State 146363
                                                if len(subjects) == 0:
                                                    pass
                                                    # 0: 1/(a + b*x**n)
                                                    yield 0, subst4
                                            subjects2.appendleft(tmp14)
                                if len(subjects10) >= 1:
                                    tmp15 = subjects10.popleft()
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i2.3.2.1.2', tmp15)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 146360
                                        if len(subjects10) == 0:
                                            pass
                                            # State 146361
                                            if len(subjects2) >= 1 and subjects2[0] == Integer(-1):
                                                tmp17 = subjects2.popleft()
                                                # State 146362
                                                if len(subjects2) == 0:
                                                    pass
                                                    # State 146363
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 0: 1/(a + b*x**n)
                                                        yield 0, subst4
                                                subjects2.appendleft(tmp17)
                                    subjects10.appendleft(tmp15)
                            subjects10.appendleft(tmp11)
                        if len(subjects10) >= 1:
                            tmp18 = subjects10.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.1', tmp18)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 146700
                                if len(subjects10) >= 1 and subjects10[0] == Integer(2):
                                    tmp20 = subjects10.popleft()
                                    # State 146701
                                    if len(subjects10) == 0:
                                        pass
                                        # State 146702
                                        if len(subjects2) >= 1 and subjects2[0] == Rational(-1, 2):
                                            tmp21 = subjects2.popleft()
                                            # State 146703
                                            if len(subjects2) == 0:
                                                pass
                                                # State 146704
                                                if len(subjects) == 0:
                                                    pass
                                                    # 2: 1/sqrt(x**2*b + a)
                                                    yield 2, subst3
                                            subjects2.appendleft(tmp21)
                                    subjects10.appendleft(tmp20)
                            subjects10.appendleft(tmp18)
                        subjects2.appendleft(tmp9)
                if len(subjects2) >= 1 and isinstance(subjects2[0], Mul):
                    tmp22 = subjects2.popleft()
                    associative1 = tmp22
                    associative_type1 = type(tmp22)
                    subjects23 = deque(tmp22._args)
                    matcher = CommutativeMatcher146365.get()
                    tmp24 = subjects23
                    subjects23 = []
                    for s in tmp24:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp24, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 146372
                            if len(subjects2) >= 1 and subjects2[0] == Integer(-1):
                                tmp25 = subjects2.popleft()
                                # State 146373
                                if len(subjects2) == 0:
                                    pass
                                    # State 146374
                                    if len(subjects) == 0:
                                        pass
                                        # 0: 1/(a + b*x**n)
                                        yield 0, subst2
                                subjects2.appendleft(tmp25)
                        if pattern_index == 1:
                            pass
                            # State 146708
                            if len(subjects2) >= 1 and subjects2[0] == Rational(-1, 2):
                                tmp26 = subjects2.popleft()
                                # State 146709
                                if len(subjects2) == 0:
                                    pass
                                    # State 146710
                                    if len(subjects) == 0:
                                        pass
                                        # 2: 1/sqrt(x**2*b + a)
                                        yield 2, subst2
                                subjects2.appendleft(tmp26)
                    subjects2.appendleft(tmp22)
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 146619
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.0', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 146620
                    if len(subjects2) >= 1 and isinstance(subjects2[0], Pow):
                        tmp29 = subjects2.popleft()
                        subjects30 = deque(tmp29._args)
                        # State 146621
                        if len(subjects30) >= 1:
                            tmp31 = subjects30.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.1', tmp31)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 146622
                                if len(subjects30) >= 1 and subjects30[0] == Integer(2):
                                    tmp33 = subjects30.popleft()
                                    # State 146623
                                    if len(subjects30) == 0:
                                        pass
                                        # State 146624
                                        if len(subjects2) >= 1 and subjects2[0] == Rational(-1, 2):
                                            tmp34 = subjects2.popleft()
                                            # State 146625
                                            if len(subjects2) == 0:
                                                pass
                                                # State 146626
                                                if len(subjects) == 0:
                                                    pass
                                                    # 1: 1/sqrt(d + e*x**2)
                                                    yield 1, subst3
                                            subjects2.appendleft(tmp34)
                                    subjects30.appendleft(tmp33)
                            subjects30.appendleft(tmp31)
                        subjects2.appendleft(tmp29)
                if len(subjects2) >= 1 and isinstance(subjects2[0], Mul):
                    tmp35 = subjects2.popleft()
                    associative1 = tmp35
                    associative_type1 = type(tmp35)
                    subjects36 = deque(tmp35._args)
                    matcher = CommutativeMatcher146628.get()
                    tmp37 = subjects36
                    subjects36 = []
                    for s in tmp37:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp37, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 146633
                            if len(subjects2) >= 1 and subjects2[0] == Rational(-1, 2):
                                tmp38 = subjects2.popleft()
                                # State 146634
                                if len(subjects2) == 0:
                                    pass
                                    # State 146635
                                    if len(subjects) == 0:
                                        pass
                                        # 1: 1/sqrt(d + e*x**2)
                                        yield 1, subst2
                                subjects2.appendleft(tmp38)
                    subjects2.appendleft(tmp35)
            if len(subjects2) >= 1 and isinstance(subjects2[0], Add):
                tmp39 = subjects2.popleft()
                associative1 = tmp39
                associative_type1 = type(tmp39)
                subjects40 = deque(tmp39._args)
                matcher = CommutativeMatcher146376.get()
                tmp41 = subjects40
                subjects40 = []
                for s in tmp41:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp41, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 146393
                        if len(subjects2) >= 1 and subjects2[0] == Integer(-1):
                            tmp42 = subjects2.popleft()
                            # State 146394
                            if len(subjects2) == 0:
                                pass
                                # State 146395
                                if len(subjects) == 0:
                                    pass
                                    # 0: 1/(a + b*x**n)
                                    yield 0, subst1
                            subjects2.appendleft(tmp42)
                    if pattern_index == 1:
                        pass
                        # State 146645
                        if len(subjects2) >= 1 and subjects2[0] == Rational(-1, 2):
                            tmp43 = subjects2.popleft()
                            # State 146646
                            if len(subjects2) == 0:
                                pass
                                # State 146647
                                if len(subjects) == 0:
                                    pass
                                    # 1: 1/sqrt(d + e*x**2)
                                    yield 1, subst1
                            subjects2.appendleft(tmp43)
                    if pattern_index == 2:
                        pass
                        # State 146715
                        if len(subjects2) >= 1 and subjects2[0] == Rational(-1, 2):
                            tmp44 = subjects2.popleft()
                            # State 146716
                            if len(subjects2) == 0:
                                pass
                                # State 146717
                                if len(subjects) == 0:
                                    pass
                                    # 2: 1/sqrt(x**2*b + a)
                                    yield 2, subst1
                            subjects2.appendleft(tmp44)
                subjects2.appendleft(tmp39)
            subjects.appendleft(tmp1)
        return
        yield


from .generated_part004335 import *
from matchpy.matching.many_to_one import CommutativeMatcher
from .generated_part004334 import *
from collections import deque
from .generated_part004336 import *
from matchpy.utils import VariableWithCount
from multiset import Multiset