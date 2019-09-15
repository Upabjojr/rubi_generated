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


class CommutativeMatcher13880(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({}), [
      (VariableWithCount('i2.2.1.0_2', 1, 1, S(1)), Mul),
      (VariableWithCount('i2.2.1.2.1.1', 1, 1, None), Mul)
]),
    1: (1, Multiset({0: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
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
        if CommutativeMatcher13880._instance is None:
            CommutativeMatcher13880._instance = CommutativeMatcher13880()
        return CommutativeMatcher13880._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 13879
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.4', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 15663
            if len(subjects) >= 1 and isinstance(subjects[0], Pow):
                tmp2 = subjects.popleft()
                subjects3 = deque(tmp2._args)
                # State 15664
                if len(subjects3) >= 1:
                    tmp4 = subjects3.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2', tmp4)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 15665
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.4.0', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 15666
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i2.4.1.0', S(0))
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 15667
                                subst5 = Substitution(subst4)
                                try:
                                    subst5.try_add_variable('i2.4.1.1.0_1', S(1))
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 15668
                                    if len(subjects3) >= 1:
                                        tmp9 = subjects3.popleft()
                                        subst6 = Substitution(subst5)
                                        try:
                                            subst6.try_add_variable('i2.4.1.1.0', tmp9)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 15669
                                            if len(subjects3) == 0:
                                                pass
                                                # State 15670
                                                if len(subjects) == 0:
                                                    pass
                                                    # 0: (F**(g*(e + x*f)))**n
                                                    yield 0, subst6
                                        subjects3.appendleft(tmp9)
                                if len(subjects3) >= 1 and isinstance(subjects3[0], Mul):
                                    tmp11 = subjects3.popleft()
                                    associative1 = tmp11
                                    associative_type1 = type(tmp11)
                                    subjects12 = deque(tmp11._args)
                                    matcher = CommutativeMatcher15672.get()
                                    tmp13 = subjects12
                                    subjects12 = []
                                    for s in tmp13:
                                        matcher.add_subject(s)
                                    for pattern_index, subst5 in matcher.match(tmp13, subst4):
                                        pass
                                        if pattern_index == 0:
                                            pass
                                            # State 15673
                                            if len(subjects3) == 0:
                                                pass
                                                # State 15674
                                                if len(subjects) == 0:
                                                    pass
                                                    # 0: (F**(g*(e + x*f)))**n
                                                    yield 0, subst5
                                    subjects3.appendleft(tmp11)
                            if len(subjects3) >= 1 and isinstance(subjects3[0], Add):
                                tmp14 = subjects3.popleft()
                                associative1 = tmp14
                                associative_type1 = type(tmp14)
                                subjects15 = deque(tmp14._args)
                                matcher = CommutativeMatcher15676.get()
                                tmp16 = subjects15
                                subjects15 = []
                                for s in tmp16:
                                    matcher.add_subject(s)
                                for pattern_index, subst4 in matcher.match(tmp16, subst3):
                                    pass
                                    if pattern_index == 0:
                                        pass
                                        # State 15682
                                        if len(subjects3) == 0:
                                            pass
                                            # State 15683
                                            if len(subjects) == 0:
                                                pass
                                                # 0: (F**(g*(e + x*f)))**n
                                                yield 0, subst4
                                subjects3.appendleft(tmp14)
                        if len(subjects3) >= 1 and isinstance(subjects3[0], Mul):
                            tmp17 = subjects3.popleft()
                            associative1 = tmp17
                            associative_type1 = type(tmp17)
                            subjects18 = deque(tmp17._args)
                            matcher = CommutativeMatcher15685.get()
                            tmp19 = subjects18
                            subjects18 = []
                            for s in tmp19:
                                matcher.add_subject(s)
                            for pattern_index, subst3 in matcher.match(tmp19, subst2):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 15700
                                    if len(subjects3) == 0:
                                        pass
                                        # State 15701
                                        if len(subjects) == 0:
                                            pass
                                            # 0: (F**(g*(e + x*f)))**n
                                            yield 0, subst3
                            subjects3.appendleft(tmp17)
                    subjects3.appendleft(tmp4)
                subjects.appendleft(tmp2)
        if len(subjects) >= 1 and isinstance(subjects[0], Pow):
            tmp20 = subjects.popleft()
            subjects21 = deque(tmp20._args)
            # State 15702
            if len(subjects21) >= 1 and isinstance(subjects21[0], Pow):
                tmp22 = subjects21.popleft()
                subjects23 = deque(tmp22._args)
                # State 15703
                if len(subjects23) >= 1:
                    tmp24 = subjects23.popleft()
                    subst1 = Substitution(subst0)
                    try:
                        subst1.try_add_variable('i2.2', tmp24)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 15704
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.4.0', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 15705
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.4.1.0', S(0))
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 15706
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.4.1.1.0_1', S(1))
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 15707
                                    if len(subjects23) >= 1:
                                        tmp29 = subjects23.popleft()
                                        subst5 = Substitution(subst4)
                                        try:
                                            subst5.try_add_variable('i2.4.1.1.0', tmp29)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 15708
                                            if len(subjects23) == 0:
                                                pass
                                                # State 15709
                                                subst6 = Substitution(subst5)
                                                try:
                                                    subst6.try_add_variable('i2.4', 1)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 15710
                                                    if len(subjects21) == 0:
                                                        pass
                                                        # State 15711
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 0: (F**(g*(e + x*f)))**n
                                                            yield 0, subst6
                                                if len(subjects21) >= 1:
                                                    tmp32 = subjects21.popleft()
                                                    subst6 = Substitution(subst5)
                                                    try:
                                                        subst6.try_add_variable('i2.4', tmp32)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 15710
                                                        if len(subjects21) == 0:
                                                            pass
                                                            # State 15711
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 0: (F**(g*(e + x*f)))**n
                                                                yield 0, subst6
                                                    subjects21.appendleft(tmp32)
                                        subjects23.appendleft(tmp29)
                                if len(subjects23) >= 1 and isinstance(subjects23[0], Mul):
                                    tmp34 = subjects23.popleft()
                                    associative1 = tmp34
                                    associative_type1 = type(tmp34)
                                    subjects35 = deque(tmp34._args)
                                    matcher = CommutativeMatcher15713.get()
                                    tmp36 = subjects35
                                    subjects35 = []
                                    for s in tmp36:
                                        matcher.add_subject(s)
                                    for pattern_index, subst4 in matcher.match(tmp36, subst3):
                                        pass
                                        if pattern_index == 0:
                                            pass
                                            # State 15714
                                            if len(subjects23) == 0:
                                                pass
                                                # State 15715
                                                subst5 = Substitution(subst4)
                                                try:
                                                    subst5.try_add_variable('i2.4', 1)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 15716
                                                    if len(subjects21) == 0:
                                                        pass
                                                        # State 15717
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 0: (F**(g*(e + x*f)))**n
                                                            yield 0, subst5
                                                if len(subjects21) >= 1:
                                                    tmp38 = subjects21.popleft()
                                                    subst5 = Substitution(subst4)
                                                    try:
                                                        subst5.try_add_variable('i2.4', tmp38)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 15716
                                                        if len(subjects21) == 0:
                                                            pass
                                                            # State 15717
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 0: (F**(g*(e + x*f)))**n
                                                                yield 0, subst5
                                                    subjects21.appendleft(tmp38)
                                    subjects23.appendleft(tmp34)
                            if len(subjects23) >= 1 and isinstance(subjects23[0], Add):
                                tmp40 = subjects23.popleft()
                                associative1 = tmp40
                                associative_type1 = type(tmp40)
                                subjects41 = deque(tmp40._args)
                                matcher = CommutativeMatcher15719.get()
                                tmp42 = subjects41
                                subjects41 = []
                                for s in tmp42:
                                    matcher.add_subject(s)
                                for pattern_index, subst3 in matcher.match(tmp42, subst2):
                                    pass
                                    if pattern_index == 0:
                                        pass
                                        # State 15725
                                        if len(subjects23) == 0:
                                            pass
                                            # State 15726
                                            subst4 = Substitution(subst3)
                                            try:
                                                subst4.try_add_variable('i2.4', 1)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 15727
                                                if len(subjects21) == 0:
                                                    pass
                                                    # State 15728
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 0: (F**(g*(e + x*f)))**n
                                                        yield 0, subst4
                                            if len(subjects21) >= 1:
                                                tmp44 = subjects21.popleft()
                                                subst4 = Substitution(subst3)
                                                try:
                                                    subst4.try_add_variable('i2.4', tmp44)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 15727
                                                    if len(subjects21) == 0:
                                                        pass
                                                        # State 15728
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 0: (F**(g*(e + x*f)))**n
                                                            yield 0, subst4
                                                subjects21.appendleft(tmp44)
                                subjects23.appendleft(tmp40)
                        if len(subjects23) >= 1 and isinstance(subjects23[0], Mul):
                            tmp46 = subjects23.popleft()
                            associative1 = tmp46
                            associative_type1 = type(tmp46)
                            subjects47 = deque(tmp46._args)
                            matcher = CommutativeMatcher15730.get()
                            tmp48 = subjects47
                            subjects47 = []
                            for s in tmp48:
                                matcher.add_subject(s)
                            for pattern_index, subst2 in matcher.match(tmp48, subst1):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 15745
                                    if len(subjects23) == 0:
                                        pass
                                        # State 15746
                                        subst3 = Substitution(subst2)
                                        try:
                                            subst3.try_add_variable('i2.4', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 15747
                                            if len(subjects21) == 0:
                                                pass
                                                # State 15748
                                                if len(subjects) == 0:
                                                    pass
                                                    # 0: (F**(g*(e + x*f)))**n
                                                    yield 0, subst3
                                        if len(subjects21) >= 1:
                                            tmp50 = subjects21.popleft()
                                            subst3 = Substitution(subst2)
                                            try:
                                                subst3.try_add_variable('i2.4', tmp50)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 15747
                                                if len(subjects21) == 0:
                                                    pass
                                                    # State 15748
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 0: (F**(g*(e + x*f)))**n
                                                        yield 0, subst3
                                            subjects21.appendleft(tmp50)
                            subjects23.appendleft(tmp46)
                    subjects23.appendleft(tmp24)
                subjects21.appendleft(tmp22)
            subjects.appendleft(tmp20)
        return
        yield


from .generated_part003325 import *
from .generated_part003324 import *
from matchpy.matching.many_to_one import CommutativeMatcher
from .generated_part003331 import *
from .generated_part003334 import *
from .generated_part003332 import *
from collections import deque
from .generated_part003327 import *
from matchpy.utils import VariableWithCount
from multiset import Multiset