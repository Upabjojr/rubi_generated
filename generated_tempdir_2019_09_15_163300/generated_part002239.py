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


class CommutativeMatcher17840(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({0: 1}), [
      (VariableWithCount('i2.2.1.3.0', 1, 1, S(1)), Mul)
]),
    1: (1, Multiset({1: 1, 2: 1}), [
      (VariableWithCount('i2.2.1.3.0', 1, 1, S(1)), Mul)
]),
    2: (2, Multiset({3: 1, 4: 1}), [
      (VariableWithCount('i2.2.1.3.0', 1, 1, S(1)), Mul)
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
        if CommutativeMatcher17840._instance is None:
            CommutativeMatcher17840._instance = CommutativeMatcher17840()
        return CommutativeMatcher17840._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 17839
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.3.1.0', S(0))
        except ValueError:
            pass
        else:
            pass
            # State 17841
            subst2 = Substitution(subst1)
            try:
                subst2.try_add_variable('i2.2.1.3.1.1.0_1', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 17842
                if len(subjects) >= 1:
                    tmp3 = subjects.popleft()
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.2.1.3.1.1.0', tmp3)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 17843
                        if len(subjects) == 0:
                            pass
                            # 0: c + x*d
                            yield 0, subst3
                    subjects.appendleft(tmp3)
            if len(subjects) >= 1 and isinstance(subjects[0], Mul):
                tmp5 = subjects.popleft()
                associative1 = tmp5
                associative_type1 = type(tmp5)
                subjects6 = deque(tmp5._args)
                matcher = CommutativeMatcher17845.get()
                tmp7 = subjects6
                subjects6 = []
                for s in tmp7:
                    matcher.add_subject(s)
                for pattern_index, subst2 in matcher.match(tmp7, subst1):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 17846
                        if len(subjects) == 0:
                            pass
                            # 0: c + x*d
                            yield 0, subst2
                subjects.appendleft(tmp5)
        if len(subjects) >= 1 and isinstance(subjects[0], Add):
            tmp8 = subjects.popleft()
            associative1 = tmp8
            associative_type1 = type(tmp8)
            subjects9 = deque(tmp8._args)
            matcher = CommutativeMatcher17848.get()
            tmp10 = subjects9
            subjects9 = []
            for s in tmp10:
                matcher.add_subject(s)
            for pattern_index, subst1 in matcher.match(tmp10, subst0):
                pass
                if pattern_index == 0:
                    pass
                    # State 17854
                    if len(subjects) == 0:
                        pass
                        # 0: c + x*d
                        yield 0, subst1
            subjects.appendleft(tmp8)
        if len(subjects) >= 1 and isinstance(subjects[0], Pow):
            tmp11 = subjects.popleft()
            subjects12 = deque(tmp11._args)
            # State 151150
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.3.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 151151
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.3.2.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 151152
                    if len(subjects12) >= 1:
                        tmp15 = subjects12.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.3.2.1.0', tmp15)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 151153
                            if len(subjects12) >= 1 and subjects12[0] == Rational(1, 2):
                                tmp17 = subjects12.popleft()
                                # State 151154
                                if len(subjects12) == 0:
                                    pass
                                    # State 151155
                                    if len(subjects) == 0:
                                        pass
                                        # 1: sqrt(d + x*e)
                                        yield 1, subst3
                                subjects12.appendleft(tmp17)
                        subjects12.appendleft(tmp15)
                if len(subjects12) >= 1 and isinstance(subjects12[0], Mul):
                    tmp18 = subjects12.popleft()
                    associative1 = tmp18
                    associative_type1 = type(tmp18)
                    subjects19 = deque(tmp18._args)
                    matcher = CommutativeMatcher151157.get()
                    tmp20 = subjects19
                    subjects19 = []
                    for s in tmp20:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp20, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 151158
                            if len(subjects12) >= 1 and subjects12[0] == Rational(1, 2):
                                tmp21 = subjects12.popleft()
                                # State 151159
                                if len(subjects12) == 0:
                                    pass
                                    # State 151160
                                    if len(subjects) == 0:
                                        pass
                                        # 1: sqrt(d + x*e)
                                        yield 1, subst2
                                subjects12.appendleft(tmp21)
                    subjects12.appendleft(tmp18)
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.3.2.0_1', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 151171
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.3.2.1.0_2', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 151172
                    if len(subjects12) >= 1:
                        tmp24 = subjects12.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.3.2.1.0', tmp24)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 151173
                            if len(subjects12) >= 1 and subjects12[0] == Rational(-1, 2):
                                tmp26 = subjects12.popleft()
                                # State 151174
                                if len(subjects12) == 0:
                                    pass
                                    # State 151175
                                    if len(subjects) == 0:
                                        pass
                                        # 2: 1/sqrt(f + x*g)
                                        yield 2, subst3
                                subjects12.appendleft(tmp26)
                        subjects12.appendleft(tmp24)
                if len(subjects12) >= 1 and isinstance(subjects12[0], Mul):
                    tmp27 = subjects12.popleft()
                    associative1 = tmp27
                    associative_type1 = type(tmp27)
                    subjects28 = deque(tmp27._args)
                    matcher = CommutativeMatcher151177.get()
                    tmp29 = subjects28
                    subjects28 = []
                    for s in tmp29:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp29, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 151178
                            if len(subjects12) >= 1 and subjects12[0] == Rational(-1, 2):
                                tmp30 = subjects12.popleft()
                                # State 151179
                                if len(subjects12) == 0:
                                    pass
                                    # State 151180
                                    if len(subjects) == 0:
                                        pass
                                        # 2: 1/sqrt(f + x*g)
                                        yield 2, subst2
                                subjects12.appendleft(tmp30)
                    subjects12.appendleft(tmp27)
            if len(subjects12) >= 1 and isinstance(subjects12[0], Add):
                tmp31 = subjects12.popleft()
                associative1 = tmp31
                associative_type1 = type(tmp31)
                subjects32 = deque(tmp31._args)
                matcher = CommutativeMatcher151162.get()
                tmp33 = subjects32
                subjects32 = []
                for s in tmp33:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp33, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 151168
                        if len(subjects12) >= 1 and subjects12[0] == Rational(1, 2):
                            tmp34 = subjects12.popleft()
                            # State 151169
                            if len(subjects12) == 0:
                                pass
                                # State 151170
                                if len(subjects) == 0:
                                    pass
                                    # 1: sqrt(d + x*e)
                                    yield 1, subst1
                            subjects12.appendleft(tmp34)
                    if pattern_index == 1:
                        pass
                        # State 151184
                        if len(subjects12) >= 1 and subjects12[0] == Rational(-1, 2):
                            tmp35 = subjects12.popleft()
                            # State 151185
                            if len(subjects12) == 0:
                                pass
                                # State 151186
                                if len(subjects) == 0:
                                    pass
                                    # 2: 1/sqrt(f + x*g)
                                    yield 2, subst1
                            subjects12.appendleft(tmp35)
                    if pattern_index == 2:
                        pass
                        # State 151404
                        if len(subjects12) >= 1 and subjects12[0] == Rational(1, 2):
                            tmp36 = subjects12.popleft()
                            # State 151405
                            if len(subjects12) == 0:
                                pass
                                # State 151406
                                if len(subjects) == 0:
                                    pass
                                    # 3: sqrt(x*e + 1)
                                    yield 3, subst1
                            subjects12.appendleft(tmp36)
                    if pattern_index == 3:
                        pass
                        # State 151407
                        if len(subjects12) >= 1 and subjects12[0] == Rational(-1, 2):
                            tmp37 = subjects12.popleft()
                            # State 151408
                            if len(subjects12) == 0:
                                pass
                                # State 151409
                                if len(subjects) == 0:
                                    pass
                                    # 4: 1/sqrt(x*g + 1)
                                    yield 4, subst1
                            subjects12.appendleft(tmp37)
                subjects12.appendleft(tmp31)
            subjects.appendleft(tmp11)
        return
        yield


from .generated_part002241 import *
from matchpy.matching.many_to_one import CommutativeMatcher
from .generated_part002244 import *
from .generated_part002240 import *
from collections import deque
from .generated_part002243 import *
from .generated_part002245 import *
from matchpy.utils import VariableWithCount
from multiset import Multiset