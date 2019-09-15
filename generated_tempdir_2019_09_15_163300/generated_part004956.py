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


class CommutativeMatcher39839(CommutativeMatcher):
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
        if CommutativeMatcher39839._instance is None:
            CommutativeMatcher39839._instance = CommutativeMatcher39839()
        return CommutativeMatcher39839._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 39838
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.2.2.2', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 39840
            subst2 = Substitution(subst1)
            try:
                subst2.try_add_variable('i2.2.1.2.2.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 39841
                subst3 = Substitution(subst2)
                try:
                    subst3.try_add_variable('i2.2.1.2.2.2.1.0', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 39842
                    if len(subjects) >= 1 and isinstance(subjects[0], Pow):
                        tmp4 = subjects.popleft()
                        subjects5 = deque(tmp4._args)
                        # State 39843
                        if len(subjects5) >= 1:
                            tmp6 = subjects5.popleft()
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i2.2.1.1', tmp6)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 39844
                                if len(subjects5) >= 1:
                                    tmp8 = subjects5.popleft()
                                    subst5 = Substitution(subst4)
                                    try:
                                        subst5.try_add_variable('i2.2.1.2', tmp8)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 39845
                                        if len(subjects5) == 0:
                                            pass
                                            # State 39846
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
                    matcher = CommutativeMatcher39848.get()
                    tmp12 = subjects11
                    subjects11 = []
                    for s in tmp12:
                        matcher.add_subject(s)
                    for pattern_index, subst3 in matcher.match(tmp12, subst2):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 39853
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
                matcher = CommutativeMatcher39855.get()
                tmp15 = subjects14
                subjects14 = []
                for s in tmp15:
                    matcher.add_subject(s)
                for pattern_index, subst2 in matcher.match(tmp15, subst1):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 39868
                        if len(subjects) == 0:
                            pass
                            # 0: (x**j*f + e)**p
                            yield 0, subst2
                subjects.appendleft(tmp13)
        if len(subjects) >= 1 and isinstance(subjects[0], Pow):
            tmp16 = subjects.popleft()
            subjects17 = deque(tmp16._args)
            # State 39869
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.2.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 39870
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.2.2.1.0', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 39871
                    if len(subjects17) >= 1 and isinstance(subjects17[0], Pow):
                        tmp20 = subjects17.popleft()
                        subjects21 = deque(tmp20._args)
                        # State 39872
                        if len(subjects21) >= 1:
                            tmp22 = subjects21.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.1', tmp22)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 39873
                                if len(subjects21) >= 1:
                                    tmp24 = subjects21.popleft()
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i2.2.1.2', tmp24)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 39874
                                        if len(subjects21) == 0:
                                            pass
                                            # State 39875
                                            subst5 = Substitution(subst4)
                                            try:
                                                subst5.try_add_variable('i2.2.1.2.2.2', 1)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 39876
                                                if len(subjects17) == 0:
                                                    pass
                                                    # State 39877
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
                                                    # State 39876
                                                    if len(subjects17) == 0:
                                                        pass
                                                        # State 39877
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
                    matcher = CommutativeMatcher39879.get()
                    tmp31 = subjects30
                    subjects30 = []
                    for s in tmp31:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp31, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 39884
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.2.2.2', 1)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 39885
                                if len(subjects17) == 0:
                                    pass
                                    # State 39886
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
                                        # State 39885
                                        if len(subjects17) == 0:
                                            pass
                                            # State 39886
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
                matcher = CommutativeMatcher39888.get()
                tmp38 = subjects37
                subjects37 = []
                for s in tmp38:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp38, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 39901
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.1.2.2.2', 1)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 39902
                            if len(subjects17) == 0:
                                pass
                                # State 39903
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
                                    # State 39902
                                    if len(subjects17) == 0:
                                        pass
                                        # State 39903
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


from .generated_part004958 import *
from .generated_part004957 import *
from .generated_part004960 import *
from matchpy.matching.many_to_one import CommutativeMatcher
from collections import deque
from matchpy.utils import VariableWithCount
from multiset import Multiset
from .generated_part004961 import *