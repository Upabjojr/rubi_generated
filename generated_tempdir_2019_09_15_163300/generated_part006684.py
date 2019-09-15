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


class CommutativeMatcher46864(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({0: 1, 1: 1}), [
      (VariableWithCount('i2.3.2.0', 1, 1, S(1)), Mul)
]),
    1: (1, Multiset({2: 1, 3: 1}), [
      (VariableWithCount('i2.3.2.0', 1, 1, S(1)), Mul)
]),
    2: (2, Multiset({2: 1, 4: 1}), [
      (VariableWithCount('i2.3.2.0', 1, 1, S(1)), Mul)
]),
    3: (3, Multiset({5: 1, 6: 1}), [
      (VariableWithCount('i2.3.2.0', 1, 1, S(1)), Mul)
]),
    4: (4, Multiset({7: 1, 8: 1}), [
      (VariableWithCount('i2.3.2.0', 1, 1, S(1)), Mul)
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
        if CommutativeMatcher46864._instance is None:
            CommutativeMatcher46864._instance = CommutativeMatcher46864()
        return CommutativeMatcher46864._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 46863
        if len(subjects) >= 1 and isinstance(subjects[0], Pow):
            tmp1 = subjects.popleft()
            subjects2 = deque(tmp1._args)
            # State 46865
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.3.2.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 46866
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.3.2.2.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 46867
                    if len(subjects2) >= 1:
                        tmp5 = subjects2.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.3.2.2.1.0', tmp5)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 46868
                            if len(subjects2) >= 1 and subjects2[0] == Integer(-1):
                                tmp7 = subjects2.popleft()
                                # State 46869
                                if len(subjects2) == 0:
                                    pass
                                    # State 46870
                                    if len(subjects) == 0:
                                        pass
                                        # 0: 1/(c + x*d)
                                        yield 0, subst3
                                subjects2.appendleft(tmp7)
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i2.3.2.2', 1)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 49006
                                if len(subjects2) == 0:
                                    pass
                                    # State 49007
                                    if len(subjects) == 0:
                                        pass
                                        # 7: (c + x*d)**n1
                                        yield 7, subst4
                            if len(subjects2) >= 1:
                                tmp9 = subjects2.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.3.2.2', tmp9)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 49006
                                    if len(subjects2) == 0:
                                        pass
                                        # State 49007
                                        if len(subjects) == 0:
                                            pass
                                            # 7: (c + x*d)**n1
                                            yield 7, subst4
                                subjects2.appendleft(tmp9)
                        subjects2.appendleft(tmp5)
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.3.2.2.1.0', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 47696
                    if len(subjects2) >= 1:
                        tmp12 = subjects2.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.0', tmp12)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 47697
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i2.3.2.2', 1)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 47698
                                if len(subjects2) == 0:
                                    pass
                                    # State 47699
                                    if len(subjects) == 0:
                                        pass
                                        # 2: (x*b + a)**n1
                                        yield 2, subst4
                            if len(subjects2) >= 1:
                                tmp15 = subjects2.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.3.2.2', tmp15)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 47698
                                    if len(subjects2) == 0:
                                        pass
                                        # State 47699
                                        if len(subjects) == 0:
                                            pass
                                            # 2: (x*b + a)**n1
                                            yield 2, subst4
                                subjects2.appendleft(tmp15)
                        subjects2.appendleft(tmp12)
                    if len(subjects2) >= 1:
                        tmp17 = subjects2.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.1', tmp17)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 48558
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i2.3.2.2', 1)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 48559
                                if len(subjects2) == 0:
                                    pass
                                    # State 48560
                                    if len(subjects) == 0:
                                        pass
                                        # 5: (x*b + a)**n1
                                        yield 5, subst4
                            if len(subjects2) >= 1:
                                tmp20 = subjects2.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.3.2.2', tmp20)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 48559
                                    if len(subjects2) == 0:
                                        pass
                                        # State 48560
                                        if len(subjects) == 0:
                                            pass
                                            # 5: (x*b + a)**n1
                                            yield 5, subst4
                                subjects2.appendleft(tmp20)
                        subjects2.appendleft(tmp17)
                if len(subjects2) >= 1 and isinstance(subjects2[0], Mul):
                    tmp22 = subjects2.popleft()
                    associative1 = tmp22
                    associative_type1 = type(tmp22)
                    subjects23 = deque(tmp22._args)
                    matcher = CommutativeMatcher46872.get()
                    tmp24 = subjects23
                    subjects23 = []
                    for s in tmp24:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp24, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 46873
                            if len(subjects2) >= 1 and subjects2[0] == Integer(-1):
                                tmp25 = subjects2.popleft()
                                # State 46874
                                if len(subjects2) == 0:
                                    pass
                                    # State 46875
                                    if len(subjects) == 0:
                                        pass
                                        # 0: 1/(c + x*d)
                                        yield 0, subst2
                                subjects2.appendleft(tmp25)
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.3.2.2', 1)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 49008
                                if len(subjects2) == 0:
                                    pass
                                    # State 49009
                                    if len(subjects) == 0:
                                        pass
                                        # 7: (c + x*d)**n1
                                        yield 7, subst3
                            if len(subjects2) >= 1:
                                tmp27 = []
                                tmp27.append(subjects2.popleft())
                                while True:
                                    if len(tmp27) > 1:
                                        tmp28 = create_operation_expression(associative1, tmp27)
                                    elif len(tmp27) == 1:
                                        tmp28 = tmp27[0]
                                    else:
                                        assert False, "Unreachable"
                                    subst3 = Substitution(subst2)
                                    try:
                                        subst3.try_add_variable('i2.3.2.2', tmp28)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 49008
                                        if len(subjects2) == 0:
                                            pass
                                            # State 49009
                                            if len(subjects) == 0:
                                                pass
                                                # 7: (c + x*d)**n1
                                                yield 7, subst3
                                    if len(subjects2) == 0:
                                        break
                                    tmp27.append(subjects2.popleft())
                                subjects2.extendleft(reversed(tmp27))
                        if pattern_index == 1:
                            pass
                            # State 47700
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.3.2.2', 1)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 47701
                                if len(subjects2) == 0:
                                    pass
                                    # State 47702
                                    if len(subjects) == 0:
                                        pass
                                        # 2: (x*b + a)**n1
                                        yield 2, subst3
                            if len(subjects2) >= 1:
                                tmp31 = []
                                tmp31.append(subjects2.popleft())
                                while True:
                                    if len(tmp31) > 1:
                                        tmp32 = create_operation_expression(associative1, tmp31)
                                    elif len(tmp31) == 1:
                                        tmp32 = tmp31[0]
                                    else:
                                        assert False, "Unreachable"
                                    subst3 = Substitution(subst2)
                                    try:
                                        subst3.try_add_variable('i2.3.2.2', tmp32)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 47701
                                        if len(subjects2) == 0:
                                            pass
                                            # State 47702
                                            if len(subjects) == 0:
                                                pass
                                                # 2: (x*b + a)**n1
                                                yield 2, subst3
                                    if len(subjects2) == 0:
                                        break
                                    tmp31.append(subjects2.popleft())
                                subjects2.extendleft(reversed(tmp31))
                        if pattern_index == 2:
                            pass
                            # State 48561
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.3.2.2', 1)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 48562
                                if len(subjects2) == 0:
                                    pass
                                    # State 48563
                                    if len(subjects) == 0:
                                        pass
                                        # 5: (x*b + a)**n1
                                        yield 5, subst3
                            if len(subjects2) >= 1:
                                tmp35 = []
                                tmp35.append(subjects2.popleft())
                                while True:
                                    if len(tmp35) > 1:
                                        tmp36 = create_operation_expression(associative1, tmp35)
                                    elif len(tmp35) == 1:
                                        tmp36 = tmp35[0]
                                    else:
                                        assert False, "Unreachable"
                                    subst3 = Substitution(subst2)
                                    try:
                                        subst3.try_add_variable('i2.3.2.2', tmp36)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 48562
                                        if len(subjects2) == 0:
                                            pass
                                            # State 48563
                                            if len(subjects) == 0:
                                                pass
                                                # 5: (x*b + a)**n1
                                                yield 5, subst3
                                    if len(subjects2) == 0:
                                        break
                                    tmp35.append(subjects2.popleft())
                                subjects2.extendleft(reversed(tmp35))
                    subjects2.appendleft(tmp22)
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.3.2.2.0_1', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 47709
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.3.2.2.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 47710
                    if len(subjects2) >= 1:
                        tmp40 = subjects2.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.0', tmp40)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 47711
                            if len(subjects2) >= 1:
                                tmp42 = subjects2.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.3.2.2_1', tmp42)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 47712
                                    if len(subjects2) == 0:
                                        pass
                                        # State 47713
                                        if len(subjects) == 0:
                                            pass
                                            # 3: (x*d + c)**n2
                                            yield 3, subst4
                                subjects2.appendleft(tmp42)
                        subjects2.appendleft(tmp40)
                    if len(subjects2) >= 1:
                        tmp44 = subjects2.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.1', tmp44)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 48569
                            if len(subjects2) >= 1:
                                tmp46 = subjects2.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.3.2.2_1', tmp46)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 48570
                                    if len(subjects2) == 0:
                                        pass
                                        # State 48571
                                        if len(subjects) == 0:
                                            pass
                                            # 6: (x*d + c)**n2
                                            yield 6, subst4
                                subjects2.appendleft(tmp46)
                        subjects2.appendleft(tmp44)
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.3.2.2.1.0_2', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 49012
                    if len(subjects2) >= 1:
                        tmp49 = subjects2.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.3.2.2.1.0', tmp49)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 49013
                            if len(subjects2) >= 1:
                                tmp51 = subjects2.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.3.2.2_1', tmp51)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 49014
                                    if len(subjects2) == 0:
                                        pass
                                        # State 49015
                                        if len(subjects) == 0:
                                            pass
                                            # 8: (c + x*d)**n2
                                            yield 8, subst4
                                subjects2.appendleft(tmp51)
                        subjects2.appendleft(tmp49)
                if len(subjects2) >= 1 and isinstance(subjects2[0], Mul):
                    tmp53 = subjects2.popleft()
                    associative1 = tmp53
                    associative_type1 = type(tmp53)
                    subjects54 = deque(tmp53._args)
                    matcher = CommutativeMatcher47715.get()
                    tmp55 = subjects54
                    subjects54 = []
                    for s in tmp55:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp55, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 47716
                            if len(subjects2) >= 1:
                                tmp56 = []
                                tmp56.append(subjects2.popleft())
                                while True:
                                    if len(tmp56) > 1:
                                        tmp57 = create_operation_expression(associative1, tmp56)
                                    elif len(tmp56) == 1:
                                        tmp57 = tmp56[0]
                                    else:
                                        assert False, "Unreachable"
                                    subst3 = Substitution(subst2)
                                    try:
                                        subst3.try_add_variable('i2.3.2.2_1', tmp57)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 47717
                                        if len(subjects2) == 0:
                                            pass
                                            # State 47718
                                            if len(subjects) == 0:
                                                pass
                                                # 3: (x*d + c)**n2
                                                yield 3, subst3
                                    if len(subjects2) == 0:
                                        break
                                    tmp56.append(subjects2.popleft())
                                subjects2.extendleft(reversed(tmp56))
                        if pattern_index == 1:
                            pass
                            # State 48572
                            if len(subjects2) >= 1:
                                tmp59 = []
                                tmp59.append(subjects2.popleft())
                                while True:
                                    if len(tmp59) > 1:
                                        tmp60 = create_operation_expression(associative1, tmp59)
                                    elif len(tmp59) == 1:
                                        tmp60 = tmp59[0]
                                    else:
                                        assert False, "Unreachable"
                                    subst3 = Substitution(subst2)
                                    try:
                                        subst3.try_add_variable('i2.3.2.2_1', tmp60)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 48573
                                        if len(subjects2) == 0:
                                            pass
                                            # State 48574
                                            if len(subjects) == 0:
                                                pass
                                                # 6: (x*d + c)**n2
                                                yield 6, subst3
                                    if len(subjects2) == 0:
                                        break
                                    tmp59.append(subjects2.popleft())
                                subjects2.extendleft(reversed(tmp59))
                        if pattern_index == 2:
                            pass
                            # State 49016
                            if len(subjects2) >= 1:
                                tmp62 = []
                                tmp62.append(subjects2.popleft())
                                while True:
                                    if len(tmp62) > 1:
                                        tmp63 = create_operation_expression(associative1, tmp62)
                                    elif len(tmp62) == 1:
                                        tmp63 = tmp62[0]
                                    else:
                                        assert False, "Unreachable"
                                    subst3 = Substitution(subst2)
                                    try:
                                        subst3.try_add_variable('i2.3.2.2_1', tmp63)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 49017
                                        if len(subjects2) == 0:
                                            pass
                                            # State 49018
                                            if len(subjects) == 0:
                                                pass
                                                # 8: (c + x*d)**n2
                                                yield 8, subst3
                                    if len(subjects2) == 0:
                                        break
                                    tmp62.append(subjects2.popleft())
                                subjects2.extendleft(reversed(tmp62))
                    subjects2.appendleft(tmp53)
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 48307
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 48308
                    if len(subjects2) >= 1:
                        tmp67 = subjects2.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.0', tmp67)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 48309
                            if len(subjects2) >= 1:
                                tmp69 = subjects2.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.3.2.2_1', tmp69)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 48310
                                    if len(subjects2) == 0:
                                        pass
                                        # State 48311
                                        if len(subjects) == 0:
                                            pass
                                            # 4: (e + x*f)**n2
                                            yield 4, subst4
                                subjects2.appendleft(tmp69)
                        subjects2.appendleft(tmp67)
                if len(subjects2) >= 1 and isinstance(subjects2[0], Mul):
                    tmp71 = subjects2.popleft()
                    associative1 = tmp71
                    associative_type1 = type(tmp71)
                    subjects72 = deque(tmp71._args)
                    matcher = CommutativeMatcher48313.get()
                    tmp73 = subjects72
                    subjects72 = []
                    for s in tmp73:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp73, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 48314
                            if len(subjects2) >= 1:
                                tmp74 = []
                                tmp74.append(subjects2.popleft())
                                while True:
                                    if len(tmp74) > 1:
                                        tmp75 = create_operation_expression(associative1, tmp74)
                                    elif len(tmp74) == 1:
                                        tmp75 = tmp74[0]
                                    else:
                                        assert False, "Unreachable"
                                    subst3 = Substitution(subst2)
                                    try:
                                        subst3.try_add_variable('i2.3.2.2_1', tmp75)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 48315
                                        if len(subjects2) == 0:
                                            pass
                                            # State 48316
                                            if len(subjects) == 0:
                                                pass
                                                # 4: (e + x*f)**n2
                                                yield 4, subst3
                                    if len(subjects2) == 0:
                                        break
                                    tmp74.append(subjects2.popleft())
                                subjects2.extendleft(reversed(tmp74))
                    subjects2.appendleft(tmp71)
            if len(subjects2) >= 1 and isinstance(subjects2[0], Add):
                tmp77 = subjects2.popleft()
                associative1 = tmp77
                associative_type1 = type(tmp77)
                subjects78 = deque(tmp77._args)
                matcher = CommutativeMatcher46877.get()
                tmp79 = subjects78
                subjects78 = []
                for s in tmp79:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp79, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 46883
                        if len(subjects2) >= 1 and subjects2[0] == Integer(-1):
                            tmp80 = subjects2.popleft()
                            # State 46884
                            if len(subjects2) == 0:
                                pass
                                # State 46885
                                if len(subjects) == 0:
                                    pass
                                    # 0: 1/(c + x*d)
                                    yield 0, subst1
                            subjects2.appendleft(tmp80)
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.3.2.2', 1)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 49010
                            if len(subjects2) == 0:
                                pass
                                # State 49011
                                if len(subjects) == 0:
                                    pass
                                    # 7: (c + x*d)**n1
                                    yield 7, subst2
                        if len(subjects2) >= 1:
                            tmp82 = []
                            tmp82.append(subjects2.popleft())
                            while True:
                                if len(tmp82) > 1:
                                    tmp83 = create_operation_expression(associative1, tmp82)
                                elif len(tmp82) == 1:
                                    tmp83 = tmp82[0]
                                else:
                                    assert False, "Unreachable"
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i2.3.2.2', tmp83)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 49010
                                    if len(subjects2) == 0:
                                        pass
                                        # State 49011
                                        if len(subjects) == 0:
                                            pass
                                            # 7: (c + x*d)**n1
                                            yield 7, subst2
                                if len(subjects2) == 0:
                                    break
                                tmp82.append(subjects2.popleft())
                            subjects2.extendleft(reversed(tmp82))
                    if pattern_index == 1:
                        pass
                        # State 47706
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.3.2.2', 1)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 47707
                            if len(subjects2) == 0:
                                pass
                                # State 47708
                                if len(subjects) == 0:
                                    pass
                                    # 2: (x*b + a)**n1
                                    yield 2, subst2
                        if len(subjects2) >= 1:
                            tmp86 = []
                            tmp86.append(subjects2.popleft())
                            while True:
                                if len(tmp86) > 1:
                                    tmp87 = create_operation_expression(associative1, tmp86)
                                elif len(tmp86) == 1:
                                    tmp87 = tmp86[0]
                                else:
                                    assert False, "Unreachable"
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i2.3.2.2', tmp87)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 47707
                                    if len(subjects2) == 0:
                                        pass
                                        # State 47708
                                        if len(subjects) == 0:
                                            pass
                                            # 2: (x*b + a)**n1
                                            yield 2, subst2
                                if len(subjects2) == 0:
                                    break
                                tmp86.append(subjects2.popleft())
                            subjects2.extendleft(reversed(tmp86))
                    if pattern_index == 2:
                        pass
                        # State 47721
                        if len(subjects2) >= 1:
                            tmp89 = []
                            tmp89.append(subjects2.popleft())
                            while True:
                                if len(tmp89) > 1:
                                    tmp90 = create_operation_expression(associative1, tmp89)
                                elif len(tmp89) == 1:
                                    tmp90 = tmp89[0]
                                else:
                                    assert False, "Unreachable"
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i2.3.2.2_1', tmp90)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 47722
                                    if len(subjects2) == 0:
                                        pass
                                        # State 47723
                                        if len(subjects) == 0:
                                            pass
                                            # 3: (x*d + c)**n2
                                            yield 3, subst2
                                if len(subjects2) == 0:
                                    break
                                tmp89.append(subjects2.popleft())
                            subjects2.extendleft(reversed(tmp89))
                    if pattern_index == 3:
                        pass
                        # State 48320
                        if len(subjects2) >= 1:
                            tmp92 = []
                            tmp92.append(subjects2.popleft())
                            while True:
                                if len(tmp92) > 1:
                                    tmp93 = create_operation_expression(associative1, tmp92)
                                elif len(tmp92) == 1:
                                    tmp93 = tmp92[0]
                                else:
                                    assert False, "Unreachable"
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i2.3.2.2_1', tmp93)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 48321
                                    if len(subjects2) == 0:
                                        pass
                                        # State 48322
                                        if len(subjects) == 0:
                                            pass
                                            # 4: (e + x*f)**n2
                                            yield 4, subst2
                                if len(subjects2) == 0:
                                    break
                                tmp92.append(subjects2.popleft())
                            subjects2.extendleft(reversed(tmp92))
                    if pattern_index == 4:
                        pass
                        # State 48566
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.3.2.2', 1)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 48567
                            if len(subjects2) == 0:
                                pass
                                # State 48568
                                if len(subjects) == 0:
                                    pass
                                    # 5: (x*b + a)**n1
                                    yield 5, subst2
                        if len(subjects2) >= 1:
                            tmp96 = []
                            tmp96.append(subjects2.popleft())
                            while True:
                                if len(tmp96) > 1:
                                    tmp97 = create_operation_expression(associative1, tmp96)
                                elif len(tmp96) == 1:
                                    tmp97 = tmp96[0]
                                else:
                                    assert False, "Unreachable"
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i2.3.2.2', tmp97)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 48567
                                    if len(subjects2) == 0:
                                        pass
                                        # State 48568
                                        if len(subjects) == 0:
                                            pass
                                            # 5: (x*b + a)**n1
                                            yield 5, subst2
                                if len(subjects2) == 0:
                                    break
                                tmp96.append(subjects2.popleft())
                            subjects2.extendleft(reversed(tmp96))
                    if pattern_index == 5:
                        pass
                        # State 48577
                        if len(subjects2) >= 1:
                            tmp99 = []
                            tmp99.append(subjects2.popleft())
                            while True:
                                if len(tmp99) > 1:
                                    tmp100 = create_operation_expression(associative1, tmp99)
                                elif len(tmp99) == 1:
                                    tmp100 = tmp99[0]
                                else:
                                    assert False, "Unreachable"
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i2.3.2.2_1', tmp100)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 48578
                                    if len(subjects2) == 0:
                                        pass
                                        # State 48579
                                        if len(subjects) == 0:
                                            pass
                                            # 6: (x*d + c)**n2
                                            yield 6, subst2
                                if len(subjects2) == 0:
                                    break
                                tmp99.append(subjects2.popleft())
                            subjects2.extendleft(reversed(tmp99))
                    if pattern_index == 6:
                        pass
                        # State 49022
                        if len(subjects2) >= 1:
                            tmp102 = []
                            tmp102.append(subjects2.popleft())
                            while True:
                                if len(tmp102) > 1:
                                    tmp103 = create_operation_expression(associative1, tmp102)
                                elif len(tmp102) == 1:
                                    tmp103 = tmp102[0]
                                else:
                                    assert False, "Unreachable"
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i2.3.2.2_1', tmp103)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 49023
                                    if len(subjects2) == 0:
                                        pass
                                        # State 49024
                                        if len(subjects) == 0:
                                            pass
                                            # 8: (c + x*d)**n2
                                            yield 8, subst2
                                if len(subjects2) == 0:
                                    break
                                tmp102.append(subjects2.popleft())
                            subjects2.extendleft(reversed(tmp102))
                subjects2.appendleft(tmp77)
            subjects.appendleft(tmp1)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.3.2.1.0', S(0))
        except ValueError:
            pass
        else:
            pass
            # State 46886
            subst2 = Substitution(subst1)
            try:
                subst2.try_add_variable('i2.3.2.1.1.0', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 46887
                if len(subjects) >= 1:
                    tmp107 = subjects.popleft()
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.3.2.2.1.0', tmp107)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 46888
                        if len(subjects) == 0:
                            pass
                            # 1: a + b*x
                            yield 1, subst3
                    subjects.appendleft(tmp107)
            if len(subjects) >= 1 and isinstance(subjects[0], Mul):
                tmp109 = subjects.popleft()
                associative1 = tmp109
                associative_type1 = type(tmp109)
                subjects110 = deque(tmp109._args)
                matcher = CommutativeMatcher46890.get()
                tmp111 = subjects110
                subjects110 = []
                for s in tmp111:
                    matcher.add_subject(s)
                for pattern_index, subst2 in matcher.match(tmp111, subst1):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 46891
                        if len(subjects) == 0:
                            pass
                            # 1: a + b*x
                            yield 1, subst2
                subjects.appendleft(tmp109)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.3.2.2', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 47681
            subst2 = Substitution(subst1)
            try:
                subst2.try_add_variable('i2.3.2.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 47682
                subst3 = Substitution(subst2)
                try:
                    subst3.try_add_variable('i2.3.2.2.1.0', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 47683
                    if len(subjects) >= 1:
                        tmp115 = subjects.popleft()
                        subst4 = Substitution(subst3)
                        try:
                            subst4.try_add_variable('i2.2.1.0', tmp115)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 47684
                            if len(subjects) == 0:
                                pass
                                # 2: (x*b + a)**n1
                                yield 2, subst4
                        subjects.appendleft(tmp115)
                    if len(subjects) >= 1:
                        tmp117 = subjects.popleft()
                        subst4 = Substitution(subst3)
                        try:
                            subst4.try_add_variable('i2.2.1.1', tmp117)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 48553
                            if len(subjects) == 0:
                                pass
                                # 5: (x*b + a)**n1
                                yield 5, subst4
                        subjects.appendleft(tmp117)
                subst3 = Substitution(subst2)
                try:
                    subst3.try_add_variable('i2.3.2.2.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 48999
                    if len(subjects) >= 1:
                        tmp120 = subjects.popleft()
                        subst4 = Substitution(subst3)
                        try:
                            subst4.try_add_variable('i2.3.2.2.1.0', tmp120)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 49000
                            if len(subjects) == 0:
                                pass
                                # 7: (c + x*d)**n1
                                yield 7, subst4
                        subjects.appendleft(tmp120)
                if len(subjects) >= 1 and isinstance(subjects[0], Mul):
                    tmp122 = subjects.popleft()
                    associative1 = tmp122
                    associative_type1 = type(tmp122)
                    subjects123 = deque(tmp122._args)
                    matcher = CommutativeMatcher47686.get()
                    tmp124 = subjects123
                    subjects123 = []
                    for s in tmp124:
                        matcher.add_subject(s)
                    for pattern_index, subst3 in matcher.match(tmp124, subst2):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 47687
                            if len(subjects) == 0:
                                pass
                                # 2: (x*b + a)**n1
                                yield 2, subst3
                        if pattern_index == 1:
                            pass
                            # State 48554
                            if len(subjects) == 0:
                                pass
                                # 5: (x*b + a)**n1
                                yield 5, subst3
                        if pattern_index == 2:
                            pass
                            # State 49001
                            if len(subjects) == 0:
                                pass
                                # 7: (c + x*d)**n1
                                yield 7, subst3
                    subjects.appendleft(tmp122)
            if len(subjects) >= 1 and isinstance(subjects[0], Add):
                tmp125 = subjects.popleft()
                associative1 = tmp125
                associative_type1 = type(tmp125)
                subjects126 = deque(tmp125._args)
                matcher = CommutativeMatcher47689.get()
                tmp127 = subjects126
                subjects126 = []
                for s in tmp127:
                    matcher.add_subject(s)
                for pattern_index, subst2 in matcher.match(tmp127, subst1):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 47695
                        if len(subjects) == 0:
                            pass
                            # 2: (x*b + a)**n1
                            yield 2, subst2
                    if pattern_index == 1:
                        pass
                        # State 48557
                        if len(subjects) == 0:
                            pass
                            # 5: (x*b + a)**n1
                            yield 5, subst2
                    if pattern_index == 2:
                        pass
                        # State 49005
                        if len(subjects) == 0:
                            pass
                            # 7: (c + x*d)**n1
                            yield 7, subst2
                subjects.appendleft(tmp125)
        if len(subjects) >= 1 and isinstance(subjects[0], Add):
            tmp128 = subjects.popleft()
            associative1 = tmp128
            associative_type1 = type(tmp128)
            subjects129 = deque(tmp128._args)
            matcher = CommutativeMatcher46893.get()
            tmp130 = subjects129
            subjects129 = []
            for s in tmp130:
                matcher.add_subject(s)
            for pattern_index, subst1 in matcher.match(tmp130, subst0):
                pass
                if pattern_index == 0:
                    pass
                    # State 46899
                    if len(subjects) == 0:
                        pass
                        # 1: a + b*x
                        yield 1, subst1
            subjects.appendleft(tmp128)
        return
        yield


from .generated_part006686 import *
from .generated_part006691 import *
from .generated_part006690 import *
from .generated_part006688 import *
from .generated_part006694 import *
from .generated_part006687 import *
from matchpy.matching.many_to_one import CommutativeMatcher
from collections import deque
from multiset import Multiset
from matchpy.utils import VariableWithCount
from .generated_part006685 import *
from .generated_part006692 import *