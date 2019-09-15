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


class CommutativeMatcher18744(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({0: 1}), [
      (VariableWithCount('i3.2.0', 1, 1, S(1)), Mul)
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
        if CommutativeMatcher18744._instance is None:
            CommutativeMatcher18744._instance = CommutativeMatcher18744()
        return CommutativeMatcher18744._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 18743
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i3.2.2', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 18745
            subst2 = Substitution(subst1)
            try:
                subst2.try_add_variable('i3.2.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 18746
                subst3 = Substitution(subst2)
                try:
                    subst3.try_add_variable('i3.2.2.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 18747
                    if len(subjects) >= 1:
                        tmp4 = subjects.popleft()
                        subst4 = Substitution(subst3)
                        try:
                            subst4.try_add_variable('i3.2.2.1.0', tmp4)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 18748
                            if len(subjects) == 0:
                                pass
                                # 0: (e + x*f)**p /; (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f1158)
                                yield 0, subst4
                        subjects.appendleft(tmp4)
                if len(subjects) >= 1 and isinstance(subjects[0], Mul):
                    tmp6 = subjects.popleft()
                    associative1 = tmp6
                    associative_type1 = type(tmp6)
                    subjects7 = deque(tmp6._args)
                    matcher = CommutativeMatcher18750.get()
                    tmp8 = subjects7
                    subjects7 = []
                    for s in tmp8:
                        matcher.add_subject(s)
                    for pattern_index, subst3 in matcher.match(tmp8, subst2):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 18751
                            if len(subjects) == 0:
                                pass
                                # 0: (e + x*f)**p /; (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f1158)
                                yield 0, subst3
                    subjects.appendleft(tmp6)
            if len(subjects) >= 1 and isinstance(subjects[0], Add):
                tmp9 = subjects.popleft()
                associative1 = tmp9
                associative_type1 = type(tmp9)
                subjects10 = deque(tmp9._args)
                matcher = CommutativeMatcher18753.get()
                tmp11 = subjects10
                subjects10 = []
                for s in tmp11:
                    matcher.add_subject(s)
                for pattern_index, subst2 in matcher.match(tmp11, subst1):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 18759
                        if len(subjects) == 0:
                            pass
                            # 0: (e + x*f)**p /; (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f1158)
                            yield 0, subst2
                subjects.appendleft(tmp9)
        if len(subjects) >= 1 and isinstance(subjects[0], Pow):
            tmp12 = subjects.popleft()
            subjects13 = deque(tmp12._args)
            # State 18760
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i3.2.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 18761
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i3.2.2.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 18762
                    if len(subjects13) >= 1:
                        tmp16 = subjects13.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i3.2.2.1.0', tmp16)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 18763
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i3.2.2', 1)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 18764
                                if len(subjects13) == 0:
                                    pass
                                    # State 18765
                                    if len(subjects) == 0:
                                        pass
                                        # 0: (e + x*f)**p /; (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f1158)
                                        yield 0, subst4
                            if len(subjects13) >= 1:
                                tmp19 = subjects13.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i3.2.2', tmp19)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 18764
                                    if len(subjects13) == 0:
                                        pass
                                        # State 18765
                                        if len(subjects) == 0:
                                            pass
                                            # 0: (e + x*f)**p /; (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f1158)
                                            yield 0, subst4
                                subjects13.appendleft(tmp19)
                        subjects13.appendleft(tmp16)
                if len(subjects13) >= 1 and isinstance(subjects13[0], Mul):
                    tmp21 = subjects13.popleft()
                    associative1 = tmp21
                    associative_type1 = type(tmp21)
                    subjects22 = deque(tmp21._args)
                    matcher = CommutativeMatcher18767.get()
                    tmp23 = subjects22
                    subjects22 = []
                    for s in tmp23:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp23, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 18768
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i3.2.2', 1)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 18769
                                if len(subjects13) == 0:
                                    pass
                                    # State 18770
                                    if len(subjects) == 0:
                                        pass
                                        # 0: (e + x*f)**p /; (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f1158)
                                        yield 0, subst3
                            if len(subjects13) >= 1:
                                tmp25 = []
                                tmp25.append(subjects13.popleft())
                                while True:
                                    if len(tmp25) > 1:
                                        tmp26 = create_operation_expression(associative1, tmp25)
                                    elif len(tmp25) == 1:
                                        tmp26 = tmp25[0]
                                    else:
                                        assert False, "Unreachable"
                                    subst3 = Substitution(subst2)
                                    try:
                                        subst3.try_add_variable('i3.2.2', tmp26)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 18769
                                        if len(subjects13) == 0:
                                            pass
                                            # State 18770
                                            if len(subjects) == 0:
                                                pass
                                                # 0: (e + x*f)**p /; (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f1158)
                                                yield 0, subst3
                                    if len(subjects13) == 0:
                                        break
                                    tmp25.append(subjects13.popleft())
                                subjects13.extendleft(reversed(tmp25))
                    subjects13.appendleft(tmp21)
            if len(subjects13) >= 1 and isinstance(subjects13[0], Add):
                tmp28 = subjects13.popleft()
                associative1 = tmp28
                associative_type1 = type(tmp28)
                subjects29 = deque(tmp28._args)
                matcher = CommutativeMatcher18772.get()
                tmp30 = subjects29
                subjects29 = []
                for s in tmp30:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp30, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 18778
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i3.2.2', 1)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 18779
                            if len(subjects13) == 0:
                                pass
                                # State 18780
                                if len(subjects) == 0:
                                    pass
                                    # 0: (e + x*f)**p /; (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f1158)
                                    yield 0, subst2
                        if len(subjects13) >= 1:
                            tmp32 = []
                            tmp32.append(subjects13.popleft())
                            while True:
                                if len(tmp32) > 1:
                                    tmp33 = create_operation_expression(associative1, tmp32)
                                elif len(tmp32) == 1:
                                    tmp33 = tmp32[0]
                                else:
                                    assert False, "Unreachable"
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i3.2.2', tmp33)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 18779
                                    if len(subjects13) == 0:
                                        pass
                                        # State 18780
                                        if len(subjects) == 0:
                                            pass
                                            # 0: (e + x*f)**p /; (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f1158)
                                            yield 0, subst2
                                if len(subjects13) == 0:
                                    break
                                tmp32.append(subjects13.popleft())
                            subjects13.extendleft(reversed(tmp32))
                subjects13.appendleft(tmp28)
            subjects.appendleft(tmp12)
        return
        yield


from .generated_part010190 import *
from matchpy.matching.many_to_one import CommutativeMatcher
from .generated_part010194 import *
from .generated_part010191 import *
from .generated_part010193 import *
from collections import deque
from matchpy.utils import VariableWithCount
from multiset import Multiset