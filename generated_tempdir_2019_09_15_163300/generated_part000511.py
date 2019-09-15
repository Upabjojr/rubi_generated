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


class CommutativeMatcher43463(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({0: 1}), [
      (VariableWithCount('i2.2.1.2.2.0', 1, 1, S(1)), Mul)
]),
    1: (1, Multiset({1: 1}), [
      (VariableWithCount('i2.2.1.2.2.0', 1, 1, S(1)), Mul)
]),
    2: (2, Multiset({2: 1}), [
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
        if CommutativeMatcher43463._instance is None:
            CommutativeMatcher43463._instance = CommutativeMatcher43463()
        return CommutativeMatcher43463._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 43462
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.2.2.2', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 43464
            if len(subjects) >= 1 and isinstance(subjects[0], Add):
                tmp2 = subjects.popleft()
                associative1 = tmp2
                associative_type1 = type(tmp2)
                subjects3 = deque(tmp2._args)
                matcher = CommutativeMatcher43466.get()
                tmp4 = subjects3
                subjects3 = []
                for s in tmp4:
                    matcher.add_subject(s)
                for pattern_index, subst2 in matcher.match(tmp4, subst1):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 43482
                        if len(subjects) == 0:
                            pass
                            # 0: (e + f*x + g*x**2)**p
                            yield 0, subst2
                    if pattern_index == 1:
                        pass
                        # State 55228
                        if len(subjects) == 0:
                            pass
                            # 2: (e + x*f)**p
                            yield 2, subst2
                subjects.appendleft(tmp2)
            if len(subjects) >= 1:
                tmp5 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.2.1', tmp5)
                except ValueError:
                    pass
                else:
                    pass
                    # State 45379
                    if len(subjects) == 0:
                        pass
                        # 1: v**p
                        yield 1, subst2
                subjects.appendleft(tmp5)
            subst2 = Substitution(subst1)
            try:
                subst2.try_add_variable('i2.2.1.2.2.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 55220
                subst3 = Substitution(subst2)
                try:
                    subst3.try_add_variable('i2.2.1.2.2.2.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 55221
                    if len(subjects) >= 1:
                        tmp9 = subjects.popleft()
                        subst4 = Substitution(subst3)
                        try:
                            subst4.try_add_variable('i2.2.1.2.2.2.1.0', tmp9)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 55222
                            if len(subjects) == 0:
                                pass
                                # 2: (e + x*f)**p
                                yield 2, subst4
                        subjects.appendleft(tmp9)
                if len(subjects) >= 1 and isinstance(subjects[0], Mul):
                    tmp11 = subjects.popleft()
                    associative1 = tmp11
                    associative_type1 = type(tmp11)
                    subjects12 = deque(tmp11._args)
                    matcher = CommutativeMatcher55224.get()
                    tmp13 = subjects12
                    subjects12 = []
                    for s in tmp13:
                        matcher.add_subject(s)
                    for pattern_index, subst3 in matcher.match(tmp13, subst2):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 55225
                            if len(subjects) == 0:
                                pass
                                # 2: (e + x*f)**p
                                yield 2, subst3
                    subjects.appendleft(tmp11)
        if len(subjects) >= 1 and isinstance(subjects[0], Pow):
            tmp14 = subjects.popleft()
            subjects15 = deque(tmp14._args)
            # State 43483
            if len(subjects15) >= 1 and isinstance(subjects15[0], Add):
                tmp16 = subjects15.popleft()
                associative1 = tmp16
                associative_type1 = type(tmp16)
                subjects17 = deque(tmp16._args)
                matcher = CommutativeMatcher43485.get()
                tmp18 = subjects17
                subjects17 = []
                for s in tmp18:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp18, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 43501
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.1.2.2.2', 1)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 43502
                            if len(subjects15) == 0:
                                pass
                                # State 43503
                                if len(subjects) == 0:
                                    pass
                                    # 0: (e + f*x + g*x**2)**p
                                    yield 0, subst2
                        if len(subjects15) >= 1:
                            tmp20 = []
                            tmp20.append(subjects15.popleft())
                            while True:
                                if len(tmp20) > 1:
                                    tmp21 = create_operation_expression(associative1, tmp20)
                                elif len(tmp20) == 1:
                                    tmp21 = tmp20[0]
                                else:
                                    assert False, "Unreachable"
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i2.2.1.2.2.2', tmp21)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 43502
                                    if len(subjects15) == 0:
                                        pass
                                        # State 43503
                                        if len(subjects) == 0:
                                            pass
                                            # 0: (e + f*x + g*x**2)**p
                                            yield 0, subst2
                                if len(subjects15) == 0:
                                    break
                                tmp20.append(subjects15.popleft())
                            subjects15.extendleft(reversed(tmp20))
                    if pattern_index == 1:
                        pass
                        # State 55241
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.1.2.2.2', 1)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 55242
                            if len(subjects15) == 0:
                                pass
                                # State 55243
                                if len(subjects) == 0:
                                    pass
                                    # 2: (e + x*f)**p
                                    yield 2, subst2
                        if len(subjects15) >= 1:
                            tmp24 = []
                            tmp24.append(subjects15.popleft())
                            while True:
                                if len(tmp24) > 1:
                                    tmp25 = create_operation_expression(associative1, tmp24)
                                elif len(tmp24) == 1:
                                    tmp25 = tmp24[0]
                                else:
                                    assert False, "Unreachable"
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i2.2.1.2.2.2', tmp25)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 55242
                                    if len(subjects15) == 0:
                                        pass
                                        # State 55243
                                        if len(subjects) == 0:
                                            pass
                                            # 2: (e + x*f)**p
                                            yield 2, subst2
                                if len(subjects15) == 0:
                                    break
                                tmp24.append(subjects15.popleft())
                            subjects15.extendleft(reversed(tmp24))
                subjects15.appendleft(tmp16)
            if len(subjects15) >= 1:
                tmp27 = subjects15.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.1.2.2.1', tmp27)
                except ValueError:
                    pass
                else:
                    pass
                    # State 45380
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.2.2.2', 1)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 45381
                        if len(subjects15) == 0:
                            pass
                            # State 45382
                            if len(subjects) == 0:
                                pass
                                # 1: v**p
                                yield 1, subst2
                    if len(subjects15) >= 1:
                        tmp30 = subjects15.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.1.2.2.2', tmp30)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 45381
                            if len(subjects15) == 0:
                                pass
                                # State 45382
                                if len(subjects) == 0:
                                    pass
                                    # 1: v**p
                                    yield 1, subst2
                        subjects15.appendleft(tmp30)
                subjects15.appendleft(tmp27)
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.2.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 55229
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.2.2.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 55230
                    if len(subjects15) >= 1:
                        tmp34 = subjects15.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.2.2.2.1.0', tmp34)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 55231
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i2.2.1.2.2.2', 1)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 55232
                                if len(subjects15) == 0:
                                    pass
                                    # State 55233
                                    if len(subjects) == 0:
                                        pass
                                        # 2: (e + x*f)**p
                                        yield 2, subst4
                            if len(subjects15) >= 1:
                                tmp37 = subjects15.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.2.1.2.2.2', tmp37)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 55232
                                    if len(subjects15) == 0:
                                        pass
                                        # State 55233
                                        if len(subjects) == 0:
                                            pass
                                            # 2: (e + x*f)**p
                                            yield 2, subst4
                                subjects15.appendleft(tmp37)
                        subjects15.appendleft(tmp34)
                if len(subjects15) >= 1 and isinstance(subjects15[0], Mul):
                    tmp39 = subjects15.popleft()
                    associative1 = tmp39
                    associative_type1 = type(tmp39)
                    subjects40 = deque(tmp39._args)
                    matcher = CommutativeMatcher55235.get()
                    tmp41 = subjects40
                    subjects40 = []
                    for s in tmp41:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp41, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 55236
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.2.2.2', 1)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 55237
                                if len(subjects15) == 0:
                                    pass
                                    # State 55238
                                    if len(subjects) == 0:
                                        pass
                                        # 2: (e + x*f)**p
                                        yield 2, subst3
                            if len(subjects15) >= 1:
                                tmp43 = []
                                tmp43.append(subjects15.popleft())
                                while True:
                                    if len(tmp43) > 1:
                                        tmp44 = create_operation_expression(associative1, tmp43)
                                    elif len(tmp43) == 1:
                                        tmp44 = tmp43[0]
                                    else:
                                        assert False, "Unreachable"
                                    subst3 = Substitution(subst2)
                                    try:
                                        subst3.try_add_variable('i2.2.1.2.2.2', tmp44)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 55237
                                        if len(subjects15) == 0:
                                            pass
                                            # State 55238
                                            if len(subjects) == 0:
                                                pass
                                                # 2: (e + x*f)**p
                                                yield 2, subst3
                                    if len(subjects15) == 0:
                                        break
                                    tmp43.append(subjects15.popleft())
                                subjects15.extendleft(reversed(tmp43))
                    subjects15.appendleft(tmp39)
            subjects.appendleft(tmp14)
        return
        yield


from .generated_part000512 import *
from .generated_part000515 import *
from matchpy.matching.many_to_one import CommutativeMatcher
from collections import deque
from .generated_part000514 import *
from .generated_part000517 import *
from matchpy.utils import VariableWithCount
from multiset import Multiset