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


class CommutativeMatcher102413(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({0: 1}), [
      (VariableWithCount('i2.2.2.0', 1, 1, None), Mul),
      (VariableWithCount('i2.2.2.0_1', 1, 1, S(1)), Mul)
]),
    1: (1, Multiset({0: 1}), [
      (VariableWithCount('i2.2.2.0', 1, 1, None), Mul)
]),
    2: (2, Multiset({1: 1}), [
      (VariableWithCount('i2.2.2.0', 1, 1, S(1)), Mul)
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
        if CommutativeMatcher102413._instance is None:
            CommutativeMatcher102413._instance = CommutativeMatcher102413()
        return CommutativeMatcher102413._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 102412
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.2.1.0', S(0))
        except ValueError:
            pass
        else:
            pass
            # State 102414
            subst2 = Substitution(subst1)
            try:
                subst2.try_add_variable('i2.2.2.1.1.0_1', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 102415
                if len(subjects) >= 1:
                    tmp3 = subjects.popleft()
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.2.2.1.1.0', tmp3)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 102416
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
                matcher = CommutativeMatcher102418.get()
                tmp7 = subjects6
                subjects6 = []
                for s in tmp7:
                    matcher.add_subject(s)
                for pattern_index, subst2 in matcher.match(tmp7, subst1):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 102419
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
            matcher = CommutativeMatcher102421.get()
            tmp10 = subjects9
            subjects9 = []
            for s in tmp10:
                matcher.add_subject(s)
            for pattern_index, subst1 in matcher.match(tmp10, subst0):
                pass
                if pattern_index == 0:
                    pass
                    # State 102427
                    if len(subjects) == 0:
                        pass
                        # 0: c + x*d
                        yield 0, subst1
            subjects.appendleft(tmp8)
        if len(subjects) >= 1 and isinstance(subjects[0], Pow):
            tmp11 = subjects.popleft()
            subjects12 = deque(tmp11._args)
            # State 150697
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.2.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 150698
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.2.2.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 150699
                    if len(subjects12) >= 1:
                        tmp15 = subjects12.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.2.2.1.0', tmp15)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 150700
                            if len(subjects12) >= 1:
                                tmp17 = subjects12.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.2.2.2', tmp17)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 150701
                                    if len(subjects12) == 0:
                                        pass
                                        # State 150702
                                        if len(subjects) == 0:
                                            pass
                                            # 1: (a + x*b)**n
                                            yield 1, subst4
                                subjects12.appendleft(tmp17)
                        subjects12.appendleft(tmp15)
                if len(subjects12) >= 1 and isinstance(subjects12[0], Mul):
                    tmp19 = subjects12.popleft()
                    associative1 = tmp19
                    associative_type1 = type(tmp19)
                    subjects20 = deque(tmp19._args)
                    matcher = CommutativeMatcher150704.get()
                    tmp21 = subjects20
                    subjects20 = []
                    for s in tmp21:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp21, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 150705
                            if len(subjects12) >= 1:
                                tmp22 = []
                                tmp22.append(subjects12.popleft())
                                while True:
                                    if len(tmp22) > 1:
                                        tmp23 = create_operation_expression(associative1, tmp22)
                                    elif len(tmp22) == 1:
                                        tmp23 = tmp22[0]
                                    else:
                                        assert False, "Unreachable"
                                    subst3 = Substitution(subst2)
                                    try:
                                        subst3.try_add_variable('i2.2.2.2', tmp23)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 150706
                                        if len(subjects12) == 0:
                                            pass
                                            # State 150707
                                            if len(subjects) == 0:
                                                pass
                                                # 1: (a + x*b)**n
                                                yield 1, subst3
                                    if len(subjects12) == 0:
                                        break
                                    tmp22.append(subjects12.popleft())
                                subjects12.extendleft(reversed(tmp22))
                    subjects12.appendleft(tmp19)
            if len(subjects12) >= 1 and isinstance(subjects12[0], Add):
                tmp25 = subjects12.popleft()
                associative1 = tmp25
                associative_type1 = type(tmp25)
                subjects26 = deque(tmp25._args)
                matcher = CommutativeMatcher150709.get()
                tmp27 = subjects26
                subjects26 = []
                for s in tmp27:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp27, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 150715
                        if len(subjects12) >= 1:
                            tmp28 = []
                            tmp28.append(subjects12.popleft())
                            while True:
                                if len(tmp28) > 1:
                                    tmp29 = create_operation_expression(associative1, tmp28)
                                elif len(tmp28) == 1:
                                    tmp29 = tmp28[0]
                                else:
                                    assert False, "Unreachable"
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i2.2.2.2', tmp29)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 150716
                                    if len(subjects12) == 0:
                                        pass
                                        # State 150717
                                        if len(subjects) == 0:
                                            pass
                                            # 1: (a + x*b)**n
                                            yield 1, subst2
                                if len(subjects12) == 0:
                                    break
                                tmp28.append(subjects12.popleft())
                            subjects12.extendleft(reversed(tmp28))
                subjects12.appendleft(tmp25)
            subjects.appendleft(tmp11)
        return
        yield


from .generated_part000829 import *
from .generated_part000828 import *
from .generated_part000831 import *
from matchpy.matching.many_to_one import CommutativeMatcher
from collections import deque
from .generated_part000832 import *
from matchpy.utils import VariableWithCount
from multiset import Multiset