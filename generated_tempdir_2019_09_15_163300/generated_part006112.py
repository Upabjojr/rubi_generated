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


class CommutativeMatcher38819(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({0: 1}), [
      (VariableWithCount('i2.2.1.2.2.0', 1, 1, S(1)), Mul)
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
        if CommutativeMatcher38819._instance is None:
            CommutativeMatcher38819._instance = CommutativeMatcher38819()
        return CommutativeMatcher38819._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 38818
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.2.2.2', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 38820
            subst2 = Substitution(subst1)
            try:
                subst2.try_add_variable('i2.2.1.2.2.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 38821
                subst3 = Substitution(subst2)
                try:
                    subst3.try_add_variable('i2.2.1.2.2.2.1.0', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 38822
                    if len(subjects) >= 1 and isinstance(subjects[0], Pow):
                        tmp4 = subjects.popleft()
                        subjects5 = deque(tmp4._args)
                        # State 38823
                        if len(subjects5) >= 1:
                            tmp6 = subjects5.popleft()
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i2.2.1.1', tmp6)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 38824
                                if len(subjects5) >= 1:
                                    tmp8 = subjects5.popleft()
                                    subst5 = Substitution(subst4)
                                    try:
                                        subst5.try_add_variable('i2.2.1.2', tmp8)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 38825
                                        if len(subjects5) == 0:
                                            pass
                                            # State 38826
                                            if len(subjects) == 0:
                                                pass
                                                # 0: (x**j*f + e)**p
                                                yield 0, subst5
                                    subjects5.appendleft(tmp8)
                            subjects5.appendleft(tmp6)
                        subjects.appendleft(tmp4)
                if len(subjects) >= 1 and isinstance(subjects[0], Mul):
                    tmp10 = subjects.popleft()
                    associative1 = tmp10
                    associative_type1 = type(tmp10)
                    subjects11 = deque(tmp10._args)
                    matcher = CommutativeMatcher38828.get()
                    tmp12 = subjects11
                    subjects11 = []
                    for s in tmp12:
                        matcher.add_subject(s)
                    for pattern_index, subst3 in matcher.match(tmp12, subst2):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 38833
                            if len(subjects) == 0:
                                pass
                                # 0: (x**j*f + e)**p
                                yield 0, subst3
                    subjects.appendleft(tmp10)
            if len(subjects) >= 1 and isinstance(subjects[0], Add):
                tmp13 = subjects.popleft()
                associative1 = tmp13
                associative_type1 = type(tmp13)
                subjects14 = deque(tmp13._args)
                matcher = CommutativeMatcher38835.get()
                tmp15 = subjects14
                subjects14 = []
                for s in tmp15:
                    matcher.add_subject(s)
                for pattern_index, subst2 in matcher.match(tmp15, subst1):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 38848
                        if len(subjects) == 0:
                            pass
                            # 0: (x**j*f + e)**p
                            yield 0, subst2
                subjects.appendleft(tmp13)
        if len(subjects) >= 1 and isinstance(subjects[0], Pow):
            tmp16 = subjects.popleft()
            subjects17 = deque(tmp16._args)
            # State 38849
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.2.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 38850
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.2.2.1.0', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 38851
                    if len(subjects17) >= 1 and isinstance(subjects17[0], Pow):
                        tmp20 = subjects17.popleft()
                        subjects21 = deque(tmp20._args)
                        # State 38852
                        if len(subjects21) >= 1:
                            tmp22 = subjects21.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.1', tmp22)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 38853
                                if len(subjects21) >= 1:
                                    tmp24 = subjects21.popleft()
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i2.2.1.2', tmp24)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 38854
                                        if len(subjects21) == 0:
                                            pass
                                            # State 38855
                                            subst5 = Substitution(subst4)
                                            try:
                                                subst5.try_add_variable('i2.2.1.2.2.2', 1)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 38856
                                                if len(subjects17) == 0:
                                                    pass
                                                    # State 38857
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 0: (x**j*f + e)**p
                                                        yield 0, subst5
                                            if len(subjects17) >= 1:
                                                tmp27 = subjects17.popleft()
                                                subst5 = Substitution(subst4)
                                                try:
                                                    subst5.try_add_variable('i2.2.1.2.2.2', tmp27)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 38856
                                                    if len(subjects17) == 0:
                                                        pass
                                                        # State 38857
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 0: (x**j*f + e)**p
                                                            yield 0, subst5
                                                subjects17.appendleft(tmp27)
                                    subjects21.appendleft(tmp24)
                            subjects21.appendleft(tmp22)
                        subjects17.appendleft(tmp20)
                if len(subjects17) >= 1 and isinstance(subjects17[0], Mul):
                    tmp29 = subjects17.popleft()
                    associative1 = tmp29
                    associative_type1 = type(tmp29)
                    subjects30 = deque(tmp29._args)
                    matcher = CommutativeMatcher38859.get()
                    tmp31 = subjects30
                    subjects30 = []
                    for s in tmp31:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp31, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 38864
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.2.2.2', 1)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 38865
                                if len(subjects17) == 0:
                                    pass
                                    # State 38866
                                    if len(subjects) == 0:
                                        pass
                                        # 0: (x**j*f + e)**p
                                        yield 0, subst3
                            if len(subjects17) >= 1:
                                tmp33 = []
                                tmp33.append(subjects17.popleft())
                                while True:
                                    if len(tmp33) > 1:
                                        tmp34 = create_operation_expression(associative1, tmp33)
                                    elif len(tmp33) == 1:
                                        tmp34 = tmp33[0]
                                    else:
                                        assert False, "Unreachable"
                                    subst3 = Substitution(subst2)
                                    try:
                                        subst3.try_add_variable('i2.2.1.2.2.2', tmp34)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 38865
                                        if len(subjects17) == 0:
                                            pass
                                            # State 38866
                                            if len(subjects) == 0:
                                                pass
                                                # 0: (x**j*f + e)**p
                                                yield 0, subst3
                                    if len(subjects17) == 0:
                                        break
                                    tmp33.append(subjects17.popleft())
                                subjects17.extendleft(reversed(tmp33))
                    subjects17.appendleft(tmp29)
            if len(subjects17) >= 1 and isinstance(subjects17[0], Add):
                tmp36 = subjects17.popleft()
                associative1 = tmp36
                associative_type1 = type(tmp36)
                subjects37 = deque(tmp36._args)
                matcher = CommutativeMatcher38868.get()
                tmp38 = subjects37
                subjects37 = []
                for s in tmp38:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp38, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 38881
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.1.2.2.2', 1)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 38882
                            if len(subjects17) == 0:
                                pass
                                # State 38883
                                if len(subjects) == 0:
                                    pass
                                    # 0: (x**j*f + e)**p
                                    yield 0, subst2
                        if len(subjects17) >= 1:
                            tmp40 = []
                            tmp40.append(subjects17.popleft())
                            while True:
                                if len(tmp40) > 1:
                                    tmp41 = create_operation_expression(associative1, tmp40)
                                elif len(tmp40) == 1:
                                    tmp41 = tmp40[0]
                                else:
                                    assert False, "Unreachable"
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i2.2.1.2.2.2', tmp41)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 38882
                                    if len(subjects17) == 0:
                                        pass
                                        # State 38883
                                        if len(subjects) == 0:
                                            pass
                                            # 0: (x**j*f + e)**p
                                            yield 0, subst2
                                if len(subjects17) == 0:
                                    break
                                tmp40.append(subjects17.popleft())
                            subjects17.extendleft(reversed(tmp40))
                subjects17.appendleft(tmp36)
            subjects.appendleft(tmp16)
        return
        yield


from .generated_part006117 import *
from .generated_part006113 import *
from .generated_part006114 import *
from matchpy.matching.many_to_one import CommutativeMatcher
from collections import deque
from .generated_part006116 import *
from matchpy.utils import VariableWithCount
from multiset import Multiset