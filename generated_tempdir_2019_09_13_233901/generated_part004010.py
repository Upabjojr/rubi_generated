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

class CommutativeMatcher24715(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({0: 1}), [
      (VariableWithCount('i2.1.1.2.2.0', 1, 1, S(1)), Mul)
]),
    1: (1, Multiset({1: 1}), [
      (VariableWithCount('i2.1.1.2.2.0', 1, 1, S(1)), Mul)
]),
    2: (2, Multiset({2: 1}), [
      (VariableWithCount('i2.1.1.2.2.0', 1, 1, S(1)), Mul)
]),
    3: (3, Multiset({3: 1}), [
      (VariableWithCount('i2.1.1.2.2.0', 1, 1, S(1)), Mul)
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
        if CommutativeMatcher24715._instance is None:
            CommutativeMatcher24715._instance = CommutativeMatcher24715()
        return CommutativeMatcher24715._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 24714
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.1.1.2.2.2', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 24716
            subst2 = Substitution(subst1)
            try:
                subst2.try_add_variable('i2.1.1.2.2.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 24717
                subst3 = Substitution(subst2)
                try:
                    subst3.try_add_variable('i2.1.1.2.2.2.1.0', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 24718
                    if len(subjects) >= 1:
                        tmp4 = subjects.popleft()
                        subst4 = Substitution(subst3)
                        try:
                            subst4.try_add_variable('i2.2.1.0', tmp4)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 24719
                            if len(subjects) == 0:
                                pass
                                # 0: (e + f*x)**p
                        subjects.appendleft(tmp4)
                    if len(subjects) >= 1:
                        tmp6 = subjects.popleft()
                        subst4 = Substitution(subst3)
                        try:
                            subst4.try_add_variable('i2.2.1.1', tmp6)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 26854
                            if len(subjects) == 0:
                                pass
                                # 1: (e + f*x)**p
                        subjects.appendleft(tmp6)
                    if len(subjects) >= 1:
                        tmp8 = subjects.popleft()
                        subst4 = Substitution(subst3)
                        try:
                            subst4.try_add_variable('i2.3.1.0', tmp8)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 27921
                            if len(subjects) == 0:
                                pass
                                # 3: (e + f*x)**p
                        subjects.appendleft(tmp8)
                if len(subjects) >= 1 and isinstance(subjects[0], Mul):
                    tmp10 = subjects.popleft()
                    associative1 = tmp10
                    associative_type1 = type(tmp10)
                    subjects11 = deque(tmp10._args)
                    matcher = CommutativeMatcher24721.get()
                    tmp12 = subjects11
                    subjects11 = []
                    for s in tmp12:
                        matcher.add_subject(s)
                    for pattern_index, subst3 in matcher.match(tmp12, subst2):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 24722
                            if len(subjects) == 0:
                                pass
                                # 0: (e + f*x)**p
                        if pattern_index == 1:
                            pass
                            # State 26855
                            if len(subjects) == 0:
                                pass
                                # 1: (e + f*x)**p
                        if pattern_index == 2:
                            pass
                            # State 27922
                            if len(subjects) == 0:
                                pass
                                # 3: (e + f*x)**p
                    subjects.appendleft(tmp10)
            if len(subjects) >= 1 and isinstance(subjects[0], Add):
                tmp13 = subjects.popleft()
                associative1 = tmp13
                associative_type1 = type(tmp13)
                subjects14 = deque(tmp13._args)
                matcher = CommutativeMatcher24724.get()
                tmp15 = subjects14
                subjects14 = []
                for s in tmp15:
                    matcher.add_subject(s)
                for pattern_index, subst2 in matcher.match(tmp15, subst1):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 24730
                        if len(subjects) == 0:
                            pass
                            # 0: (e + f*x)**p
                    if pattern_index == 1:
                        pass
                        # State 26858
                        if len(subjects) == 0:
                            pass
                            # 1: (e + f*x)**p
                    if pattern_index == 2:
                        pass
                        # State 27336
                        if len(subjects) == 0:
                            pass
                            # 2: (e + f*x)**p
                    if pattern_index == 3:
                        pass
                        # State 27925
                        if len(subjects) == 0:
                            pass
                            # 3: (e + f*x)**p
                subjects.appendleft(tmp13)
        if len(subjects) >= 1 and isinstance(subjects[0], Pow):
            tmp16 = subjects.popleft()
            subjects17 = deque(tmp16._args)
            # State 24731
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.1.1.2.2.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 24732
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.1.1.2.2.2.1.0', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 24733
                    if len(subjects17) >= 1:
                        tmp20 = subjects17.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.0', tmp20)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 24734
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i2.1.1.2.2.2', 1)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 24735
                                if len(subjects17) == 0:
                                    pass
                                    # State 24736
                                    if len(subjects) == 0:
                                        pass
                                        # 0: (e + f*x)**p
                            if len(subjects17) >= 1:
                                tmp23 = subjects17.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.1.1.2.2.2', tmp23)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 24735
                                    if len(subjects17) == 0:
                                        pass
                                        # State 24736
                                        if len(subjects) == 0:
                                            pass
                                            # 0: (e + f*x)**p
                                subjects17.appendleft(tmp23)
                        subjects17.appendleft(tmp20)
                    if len(subjects17) >= 1:
                        tmp25 = subjects17.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.1', tmp25)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 26859
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i2.1.1.2.2.2', 1)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 26860
                                if len(subjects17) == 0:
                                    pass
                                    # State 26861
                                    if len(subjects) == 0:
                                        pass
                                        # 1: (e + f*x)**p
                            if len(subjects17) >= 1:
                                tmp28 = subjects17.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.1.1.2.2.2', tmp28)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 26860
                                    if len(subjects17) == 0:
                                        pass
                                        # State 26861
                                        if len(subjects) == 0:
                                            pass
                                            # 1: (e + f*x)**p
                                subjects17.appendleft(tmp28)
                        subjects17.appendleft(tmp25)
                    if len(subjects17) >= 1:
                        tmp30 = subjects17.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.3.1.0', tmp30)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 27926
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i2.1.1.2.2.2', 1)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 27927
                                if len(subjects17) == 0:
                                    pass
                                    # State 27928
                                    if len(subjects) == 0:
                                        pass
                                        # 3: (e + f*x)**p
                            if len(subjects17) >= 1:
                                tmp33 = subjects17.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.1.1.2.2.2', tmp33)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 27927
                                    if len(subjects17) == 0:
                                        pass
                                        # State 27928
                                        if len(subjects) == 0:
                                            pass
                                            # 3: (e + f*x)**p
                                subjects17.appendleft(tmp33)
                        subjects17.appendleft(tmp30)
                if len(subjects17) >= 1 and isinstance(subjects17[0], Mul):
                    tmp35 = subjects17.popleft()
                    associative1 = tmp35
                    associative_type1 = type(tmp35)
                    subjects36 = deque(tmp35._args)
                    matcher = CommutativeMatcher24738.get()
                    tmp37 = subjects36
                    subjects36 = []
                    for s in tmp37:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp37, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 24739
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.1.1.2.2.2', 1)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 24740
                                if len(subjects17) == 0:
                                    pass
                                    # State 24741
                                    if len(subjects) == 0:
                                        pass
                                        # 0: (e + f*x)**p
                            if len(subjects17) >= 1:
                                tmp39 = []
                                tmp39.append(subjects17.popleft())
                                while True:
                                    if len(tmp39) > 1:
                                        tmp40 = create_operation_expression(associative1, tmp39)
                                    elif len(tmp39) == 1:
                                        tmp40 = tmp39[0]
                                    else:
                                        assert False, "Unreachable"
                                    subst3 = Substitution(subst2)
                                    try:
                                        subst3.try_add_variable('i2.1.1.2.2.2', tmp40)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 24740
                                        if len(subjects17) == 0:
                                            pass
                                            # State 24741
                                            if len(subjects) == 0:
                                                pass
                                                # 0: (e + f*x)**p
                                    if len(subjects17) == 0:
                                        break
                                    tmp39.append(subjects17.popleft())
                                subjects17.extendleft(reversed(tmp39))
                        if pattern_index == 1:
                            pass
                            # State 26862
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.1.1.2.2.2', 1)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 26863
                                if len(subjects17) == 0:
                                    pass
                                    # State 26864
                                    if len(subjects) == 0:
                                        pass
                                        # 1: (e + f*x)**p
                            if len(subjects17) >= 1:
                                tmp43 = []
                                tmp43.append(subjects17.popleft())
                                while True:
                                    if len(tmp43) > 1:
                                        tmp44 = create_operation_expression(associative1, tmp43)
                                    elif len(tmp43) == 1:
                                        tmp44 = tmp43[0]
                                    else:
                                        assert False, "Unreachable"
                                    subst3 = Substitution(subst2)
                                    try:
                                        subst3.try_add_variable('i2.1.1.2.2.2', tmp44)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 26863
                                        if len(subjects17) == 0:
                                            pass
                                            # State 26864
                                            if len(subjects) == 0:
                                                pass
                                                # 1: (e + f*x)**p
                                    if len(subjects17) == 0:
                                        break
                                    tmp43.append(subjects17.popleft())
                                subjects17.extendleft(reversed(tmp43))
                        if pattern_index == 2:
                            pass
                            # State 27929
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.1.1.2.2.2', 1)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 27930
                                if len(subjects17) == 0:
                                    pass
                                    # State 27931
                                    if len(subjects) == 0:
                                        pass
                                        # 3: (e + f*x)**p
                            if len(subjects17) >= 1:
                                tmp47 = []
                                tmp47.append(subjects17.popleft())
                                while True:
                                    if len(tmp47) > 1:
                                        tmp48 = create_operation_expression(associative1, tmp47)
                                    elif len(tmp47) == 1:
                                        tmp48 = tmp47[0]
                                    else:
                                        assert False, "Unreachable"
                                    subst3 = Substitution(subst2)
                                    try:
                                        subst3.try_add_variable('i2.1.1.2.2.2', tmp48)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 27930
                                        if len(subjects17) == 0:
                                            pass
                                            # State 27931
                                            if len(subjects) == 0:
                                                pass
                                                # 3: (e + f*x)**p
                                    if len(subjects17) == 0:
                                        break
                                    tmp47.append(subjects17.popleft())
                                subjects17.extendleft(reversed(tmp47))
                    subjects17.appendleft(tmp35)
            if len(subjects17) >= 1 and isinstance(subjects17[0], Add):
                tmp50 = subjects17.popleft()
                associative1 = tmp50
                associative_type1 = type(tmp50)
                subjects51 = deque(tmp50._args)
                matcher = CommutativeMatcher24743.get()
                tmp52 = subjects51
                subjects51 = []
                for s in tmp52:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp52, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 24749
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.1.1.2.2.2', 1)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 24750
                            if len(subjects17) == 0:
                                pass
                                # State 24751
                                if len(subjects) == 0:
                                    pass
                                    # 0: (e + f*x)**p
                        if len(subjects17) >= 1:
                            tmp54 = []
                            tmp54.append(subjects17.popleft())
                            while True:
                                if len(tmp54) > 1:
                                    tmp55 = create_operation_expression(associative1, tmp54)
                                elif len(tmp54) == 1:
                                    tmp55 = tmp54[0]
                                else:
                                    assert False, "Unreachable"
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i2.1.1.2.2.2', tmp55)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 24750
                                    if len(subjects17) == 0:
                                        pass
                                        # State 24751
                                        if len(subjects) == 0:
                                            pass
                                            # 0: (e + f*x)**p
                                if len(subjects17) == 0:
                                    break
                                tmp54.append(subjects17.popleft())
                            subjects17.extendleft(reversed(tmp54))
                    if pattern_index == 1:
                        pass
                        # State 26867
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.1.1.2.2.2', 1)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 26868
                            if len(subjects17) == 0:
                                pass
                                # State 26869
                                if len(subjects) == 0:
                                    pass
                                    # 1: (e + f*x)**p
                        if len(subjects17) >= 1:
                            tmp58 = []
                            tmp58.append(subjects17.popleft())
                            while True:
                                if len(tmp58) > 1:
                                    tmp59 = create_operation_expression(associative1, tmp58)
                                elif len(tmp58) == 1:
                                    tmp59 = tmp58[0]
                                else:
                                    assert False, "Unreachable"
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i2.1.1.2.2.2', tmp59)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 26868
                                    if len(subjects17) == 0:
                                        pass
                                        # State 26869
                                        if len(subjects) == 0:
                                            pass
                                            # 1: (e + f*x)**p
                                if len(subjects17) == 0:
                                    break
                                tmp58.append(subjects17.popleft())
                            subjects17.extendleft(reversed(tmp58))
                    if pattern_index == 2:
                        pass
                        # State 27337
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.1.1.2.2.2', 1)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 27338
                            if len(subjects17) == 0:
                                pass
                                # State 27339
                                if len(subjects) == 0:
                                    pass
                                    # 2: (e + f*x)**p
                        if len(subjects17) >= 1:
                            tmp62 = []
                            tmp62.append(subjects17.popleft())
                            while True:
                                if len(tmp62) > 1:
                                    tmp63 = create_operation_expression(associative1, tmp62)
                                elif len(tmp62) == 1:
                                    tmp63 = tmp62[0]
                                else:
                                    assert False, "Unreachable"
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i2.1.1.2.2.2', tmp63)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 27338
                                    if len(subjects17) == 0:
                                        pass
                                        # State 27339
                                        if len(subjects) == 0:
                                            pass
                                            # 2: (e + f*x)**p
                                if len(subjects17) == 0:
                                    break
                                tmp62.append(subjects17.popleft())
                            subjects17.extendleft(reversed(tmp62))
                    if pattern_index == 3:
                        pass
                        # State 27934
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.1.1.2.2.2', 1)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 27935
                            if len(subjects17) == 0:
                                pass
                                # State 27936
                                if len(subjects) == 0:
                                    pass
                                    # 3: (e + f*x)**p
                        if len(subjects17) >= 1:
                            tmp66 = []
                            tmp66.append(subjects17.popleft())
                            while True:
                                if len(tmp66) > 1:
                                    tmp67 = create_operation_expression(associative1, tmp66)
                                elif len(tmp66) == 1:
                                    tmp67 = tmp66[0]
                                else:
                                    assert False, "Unreachable"
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i2.1.1.2.2.2', tmp67)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 27935
                                    if len(subjects17) == 0:
                                        pass
                                        # State 27936
                                        if len(subjects) == 0:
                                            pass
                                            # 3: (e + f*x)**p
                                if len(subjects17) == 0:
                                    break
                                tmp66.append(subjects17.popleft())
                            subjects17.extendleft(reversed(tmp66))
                subjects17.appendleft(tmp50)
            subjects.appendleft(tmp16)
        return
        yield


from matchpy.utils import VariableWithCount
from matchpy.matching.many_to_one import CommutativeMatcher
from multiset import Multiset
from collections import deque