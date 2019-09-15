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


class CommutativeMatcher2617(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({}), [
      (VariableWithCount('i2.2.1.0', 1, 1, None), Mul),
      (VariableWithCount('i2.2.1.0_2', 1, 1, S(1)), Mul)
]),
    1: (1, Multiset({0: 1}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul)
]),
    2: (2, Multiset({}), [
      (VariableWithCount('i2.2.0', 1, 1, None), Mul),
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    3: (3, Multiset({}), [
      (VariableWithCount('i2.2.1.0', 1, 1, None), Mul),
      (VariableWithCount('i2.2.1.0_3', 1, 1, S(1)), Mul)
]),
    4: (4, Multiset({1: 1}), [
      (VariableWithCount('i2.2.1.0_2', 1, 1, S(1)), Mul)
]),
    5: (5, Multiset({}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul),
      (VariableWithCount('i2.2.1.1', 1, 1, None), Mul)
]),
    6: (6, Multiset({}), [
      (VariableWithCount('i2.2.1.0_2', 1, 1, S(1)), Mul),
      (VariableWithCount('i2.2.1.1', 1, 1, None), Mul)
]),
    7: (7, Multiset({2: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    8: (8, Multiset({3: 1}), [
      (VariableWithCount('i2.2.1.0_2', 1, 1, S(1)), Mul)
]),
    9: (9, Multiset({}), [
      (VariableWithCount('i2.2.1.0_3', 1, 1, S(1)), Mul),
      (VariableWithCount('i2.2.1.1', 1, 1, None), Mul)
]),
    10: (10, Multiset({3: 1}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul)
]),
    11: (11, Multiset({4: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    12: (12, Multiset({5: 1}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul)
]),
    13: (13, Multiset({6: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    14: (14, Multiset({7: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    15: (15, Multiset({7: 1}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul)
]),
    16: (16, Multiset({8: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    17: (17, Multiset({0: 1}), [
      (VariableWithCount('i2.2.1.0_2', 1, 1, S(1)), Mul)
]),
    18: (18, Multiset({9: 1}), [
      (VariableWithCount('i2.2.1.0_3', 1, 1, S(1)), Mul)
]),
    19: (19, Multiset({10: 1}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul)
]),
    20: (20, Multiset({11: 1}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul)
]),
    21: (21, Multiset({12: 1}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul)
]),
    22: (22, Multiset({5: 1}), [
      (VariableWithCount('i2.2.1.0_2', 1, 1, S(1)), Mul)
]),
    23: (23, Multiset({13: 1}), [
      (VariableWithCount('i2.2.1.0_2', 1, 1, S(1)), Mul)
]),
    24: (24, Multiset({13: 1}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul)
]),
    25: (25, Multiset({9: 1}), [
      (VariableWithCount('i2.2.1.0_2', 1, 1, S(1)), Mul)
]),
    26: (26, Multiset({14: 1}), [
      (VariableWithCount('i2.2.1.0_2', 1, 1, S(1)), Mul)
]),
    27: (27, Multiset({15: 1}), [
      (VariableWithCount('i2.2.1.0_3', 1, 1, S(1)), Mul)
]),
    28: (28, Multiset({16: 1}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul)
]),
    29: (29, Multiset({4: 1}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul)
]),
    30: (30, Multiset({11: 1}), [
      (VariableWithCount('i2.2.1.0_2', 1, 1, S(1)), Mul)
]),
    31: (31, Multiset({17: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    32: (32, Multiset({18: 1}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul)
]),
    33: (33, Multiset({15: 1}), [
      (VariableWithCount('i2.2.1.0_2', 1, 1, S(1)), Mul)
]),
    34: (34, Multiset({}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, None), Mul),
      (VariableWithCount('i2.2.1.0_2', 1, 1, S(1)), Mul)
]),
    35: (35, Multiset({}), [
      (VariableWithCount('i2.2.1.0_2', 1, 1, S(1)), Mul),
      (VariableWithCount('i2.2.1.2.1.1', 1, 1, None), Mul)
]),
    36: (36, Multiset({19: 1}), [
      (VariableWithCount('i2.2.1.0_2', 1, 1, S(1)), Mul)
]),
    37: (37, Multiset({}), [
      (VariableWithCount('i2.2.1.0_3', 1, 1, S(1)), Mul),
      (VariableWithCount('i2.2.1.2.1.1', 1, 1, None), Mul)
]),
    38: (38, Multiset({20: 1}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul)
]),
    39: (39, Multiset({}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul),
      (VariableWithCount('i2.2.3.1.1.0', 1, 1, None), Mul)
]),
    40: (40, Multiset({}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul),
      (VariableWithCount('i2.2.1.4.1.1.0', 1, 1, None), Mul)
]),
    41: (41, Multiset({}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul),
      (VariableWithCount('i2.4.1.1.0', 1, 1, None), Mul)
]),
    42: (42, Multiset({21: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    43: (43, Multiset({22: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    44: (44, Multiset({}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul),
      (VariableWithCount('i2.2.1.2.2.2.1.0', 1, 1, None), Mul)
]),
    45: (45, Multiset({}), [
      (VariableWithCount('i2.2.1.0_2', 1, 1, S(1)), Mul),
      (VariableWithCount('i2.2.1.2.1.1.0', 1, 1, None), Mul)
]),
    46: (46, Multiset({}), [
      (VariableWithCount('i2.2.1.0_2', 1, 1, S(1)), Mul),
      (VariableWithCount('i2.2.1.2.2.2.1.0', 1, 1, None), Mul)
]),
    47: (47, Multiset({23: 1}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul)
]),
    48: (48, Multiset({24: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    49: (49, Multiset({25: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    50: (50, Multiset({26: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    51: (51, Multiset({27: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    52: (52, Multiset({28: 1}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul)
]),
    53: (53, Multiset({29: 1}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul)
]),
    54: (54, Multiset({30: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    55: (55, Multiset({31: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    56: (56, Multiset({32: 1}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul)
]),
    57: (57, Multiset({33: 1}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul)
]),
    58: (58, Multiset({34: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    59: (59, Multiset({35: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    60: (60, Multiset({36: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    61: (61, Multiset({37: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    62: (62, Multiset({}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul),
      (VariableWithCount('i2.2.2.1.0', 1, 1, None), Mul)
]),
    63: (63, Multiset({38: 1}), [
      (VariableWithCount('i2.2.1.0_2', 1, 1, S(1)), Mul)
]),
    64: (64, Multiset({}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul),
      (VariableWithCount('i2.2.1.2.1.0', 1, 1, None), Mul)
]),
    65: (65, Multiset({39: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    66: (66, Multiset({40: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    67: (67, Multiset({41: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    68: (68, Multiset({42: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    69: (69, Multiset({43: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    70: (70, Multiset({44: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    71: (71, Multiset({45: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    72: (72, Multiset({46: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    73: (73, Multiset({47: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    74: (74, Multiset({48: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    75: (75, Multiset({49: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    76: (76, Multiset({50: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    77: (77, Multiset({51: 1}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul)
]),
    78: (78, Multiset({52: 1}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul)
]),
    79: (79, Multiset({53: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    80: (80, Multiset({54: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    81: (81, Multiset({55: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    82: (82, Multiset({56: 1}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul)
]),
    83: (83, Multiset({}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul),
      (VariableWithCount('i2.2.3.1.0', 1, 1, None), Mul)
]),
    84: (84, Multiset({57: 1}), [
      (VariableWithCount('i2.2.1.0_2', 1, 1, S(1)), Mul)
]),
    85: (85, Multiset({}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul),
      (VariableWithCount('i2.2.1.3.1.0', 1, 1, None), Mul)
]),
    86: (86, Multiset({58: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    87: (87, Multiset({59: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    88: (88, Multiset({60: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    89: (89, Multiset({61: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    90: (90, Multiset({62: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    91: (91, Multiset({63: 1}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul)
]),
    92: (92, Multiset({64: 1}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul)
]),
    93: (93, Multiset({65: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    94: (94, Multiset({66: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    95: (95, Multiset({67: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    96: (96, Multiset({68: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    97: (97, Multiset({69: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    98: (98, Multiset({70: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    99: (99, Multiset({71: 1, 38: 1}), [
      (VariableWithCount('i2.2.1.0_2', 1, 1, S(1)), Mul)
]),
    100: (100, Multiset({72: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    101: (101, Multiset({73: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    102: (102, Multiset({74: 1}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul)
]),
    103: (103, Multiset({75: 1}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul)
]),
    104: (104, Multiset({72: 1}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul)
]),
    105: (105, Multiset({73: 1}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul)
]),
    106: (106, Multiset({}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul),
      (VariableWithCount('i2.2.1.2.0', 1, 1, None), Mul)
]),
    107: (107, Multiset({76: 1}), [
      (VariableWithCount('i2.2.1.0_2', 1, 1, S(1)), Mul)
]),
    108: (108, Multiset({}), [
      (VariableWithCount('i2.2.1.0_3', 1, 1, S(1)), Mul),
      (VariableWithCount('i2.2.1.2.0', 1, 1, None), Mul)
]),
    109: (109, Multiset({}), [
      (VariableWithCount('i2.2.1.0_2', 1, 1, S(1)), Mul),
      (VariableWithCount('i2.2.1.2.0', 1, 1, None), Mul)
]),
    110: (110, Multiset({77: 1}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul)
]),
    111: (111, Multiset({78: 1}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul)
]),
    112: (112, Multiset({79: 1}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul)
]),
    113: (113, Multiset({}), [
      (VariableWithCount('i2.2.1.0_2', 1, 1, S(1)), Mul),
      (VariableWithCount('i2.2.1.2.1.0', 1, 1, None), Mul)
]),
    114: (114, Multiset({80: 1}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul)
]),
    115: (115, Multiset({81: 1}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul)
]),
    116: (116, Multiset({82: 1}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul)
]),
    117: (117, Multiset({83: 1}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul)
]),
    118: (118, Multiset({84: 1}), [
      (VariableWithCount('i2.2.1.0_2', 1, 1, S(1)), Mul)
]),
    119: (119, Multiset({85: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    120: (120, Multiset({86: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    121: (121, Multiset({87: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    122: (122, Multiset({88: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    123: (123, Multiset({89: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    124: (124, Multiset({90: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    125: (125, Multiset({91: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    126: (126, Multiset({92: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    127: (127, Multiset({93: 1}), [
      (VariableWithCount('i2.2.1.0_2', 1, 1, S(1)), Mul)
]),
    128: (128, Multiset({94: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    129: (129, Multiset({95: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    130: (130, Multiset({96: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    131: (131, Multiset({97: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    132: (132, Multiset({98: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    133: (133, Multiset({99: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    134: (134, Multiset({100: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    135: (135, Multiset({101: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    136: (136, Multiset({102: 1, 84: 1}), [
      (VariableWithCount('i2.2.1.0_2', 1, 1, S(1)), Mul)
]),
    137: (137, Multiset({103: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    138: (138, Multiset({104: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    139: (139, Multiset({105: 1}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul)
]),
    140: (140, Multiset({106: 1}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul)
]),
    141: (141, Multiset({103: 1}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul)
]),
    142: (142, Multiset({107: 1}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul)
]),
    143: (143, Multiset({108: 1, 109: 1}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul)
]),
    144: (144, Multiset({110: 1}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul)
]),
    145: (145, Multiset({111: 1}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul)
]),
    146: (146, Multiset({112: 1}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul)
]),
    147: (147, Multiset({113: 1}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul)
]),
    148: (148, Multiset({}), [
      (VariableWithCount('i2.2.1.0_2', 1, 1, None), Mul),
      (VariableWithCount('i2.2.1.0_3', 1, 1, S(1)), Mul)
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
        if CommutativeMatcher2617._instance is None:
            CommutativeMatcher2617._instance = CommutativeMatcher2617()
        return CommutativeMatcher2617._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 2616
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.2_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 2672
            if len(subjects) >= 1:
                tmp2 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.1', tmp2)
                except ValueError:
                    pass
                else:
                    pass
                    # State 2673
                    if len(subjects) == 0:
                        pass
                        # 0: x**n
                        yield 0, subst2
                subjects.appendleft(tmp2)
            if len(subjects) >= 1:
                tmp4 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.0', tmp4)
                except ValueError:
                    pass
                else:
                    pass
                    # State 8348
                    if len(subjects) == 0:
                        pass
                        # 11: x**n2
                        yield 11, subst2
                subjects.appendleft(tmp4)
            if len(subjects) >= 1:
                tmp6 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.0_1', tmp6)
                except ValueError:
                    pass
                else:
                    pass
                    # State 8451
                    if len(subjects) == 0:
                        pass
                        # 12: x**n
                        yield 12, subst2
                subjects.appendleft(tmp6)
            subst2 = Substitution(subst1)
            try:
                subst2.try_add_variable('i2.2.1.2.0', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 11110
                if len(subjects) >= 1 and isinstance(subjects[0], Pow):
                    tmp9 = subjects.popleft()
                    subjects10 = deque(tmp9._args)
                    # State 11111
                    if len(subjects10) >= 1:
                        tmp11 = subjects10.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.0', tmp11)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 11112
                            if len(subjects10) >= 1 and subjects10[0] == Integer(-1):
                                tmp13 = subjects10.popleft()
                                # State 11113
                                if len(subjects10) == 0:
                                    pass
                                    # State 11114
                                    if len(subjects) == 0:
                                        pass
                                        # 18: (c/x)**n2
                                        yield 18, subst3
                                subjects10.appendleft(tmp13)
                        subjects10.appendleft(tmp11)
                    subjects.appendleft(tmp9)
            if len(subjects) >= 1 and isinstance(subjects[0], Mul):
                tmp14 = subjects.popleft()
                associative1 = tmp14
                associative_type1 = type(tmp14)
                subjects15 = deque(tmp14._args)
                matcher = CommutativeMatcher11116.get()
                tmp16 = subjects15
                subjects15 = []
                for s in tmp16:
                    matcher.add_subject(s)
                for pattern_index, subst2 in matcher.match(tmp16, subst1):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 11121
                        if len(subjects) == 0:
                            pass
                            # 18: (c/x)**n2
                            yield 18, subst2
                subjects.appendleft(tmp14)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.2', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 7220
            if len(subjects) >= 1:
                tmp18 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.0', tmp18)
                except ValueError:
                    pass
                else:
                    pass
                    # State 7221
                    if len(subjects) == 0:
                        pass
                        # 7: x**non2
                        yield 7, subst2
                subjects.appendleft(tmp18)
            if len(subjects) >= 1:
                tmp20 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.0_1', tmp20)
                except ValueError:
                    pass
                else:
                    pass
                    # State 7467
                    if len(subjects) == 0:
                        pass
                        # 8: x**mn
                        yield 8, subst2
                subjects.appendleft(tmp20)
            if len(subjects) >= 1:
                tmp22 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.1', tmp22)
                except ValueError:
                    pass
                else:
                    pass
                    # State 9046
                    if len(subjects) == 0:
                        pass
                        # 14: x**n
                        yield 14, subst2
                subjects.appendleft(tmp22)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.2_2', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 7575
            if len(subjects) >= 1:
                tmp25 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.1', tmp25)
                except ValueError:
                    pass
                else:
                    pass
                    # State 7576
                    if len(subjects) == 0:
                        pass
                        # 9: x**r
                        yield 9, subst2
                subjects.appendleft(tmp25)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.4', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 15835
            if len(subjects) >= 1 and isinstance(subjects[0], Pow):
                tmp28 = subjects.popleft()
                subjects29 = deque(tmp28._args)
                # State 15836
                if len(subjects29) >= 1:
                    tmp30 = subjects29.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2', tmp30)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 15837
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.4.0', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 15838
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i2.4.1.0', S(0))
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 15839
                                subst5 = Substitution(subst4)
                                try:
                                    subst5.try_add_variable('i2.4.1.1.0_1', S(1))
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 15840
                                    if len(subjects29) >= 1:
                                        tmp35 = subjects29.popleft()
                                        subst6 = Substitution(subst5)
                                        try:
                                            subst6.try_add_variable('i2.4.1.1.0', tmp35)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 15841
                                            if len(subjects29) == 0:
                                                pass
                                                # State 15842
                                                if len(subjects) == 0:
                                                    pass
                                                    # 21: (F**(g*(e + x*f)))**n
                                                    yield 21, subst6
                                        subjects29.appendleft(tmp35)
                                if len(subjects29) >= 1 and isinstance(subjects29[0], Mul):
                                    tmp37 = subjects29.popleft()
                                    associative1 = tmp37
                                    associative_type1 = type(tmp37)
                                    subjects38 = deque(tmp37._args)
                                    matcher = CommutativeMatcher15844.get()
                                    tmp39 = subjects38
                                    subjects38 = []
                                    for s in tmp39:
                                        matcher.add_subject(s)
                                    for pattern_index, subst5 in matcher.match(tmp39, subst4):
                                        pass
                                        if pattern_index == 0:
                                            pass
                                            # State 15845
                                            if len(subjects29) == 0:
                                                pass
                                                # State 15846
                                                if len(subjects) == 0:
                                                    pass
                                                    # 21: (F**(g*(e + x*f)))**n
                                                    yield 21, subst5
                                    subjects29.appendleft(tmp37)
                            if len(subjects29) >= 1 and isinstance(subjects29[0], Add):
                                tmp40 = subjects29.popleft()
                                associative1 = tmp40
                                associative_type1 = type(tmp40)
                                subjects41 = deque(tmp40._args)
                                matcher = CommutativeMatcher15848.get()
                                tmp42 = subjects41
                                subjects41 = []
                                for s in tmp42:
                                    matcher.add_subject(s)
                                for pattern_index, subst4 in matcher.match(tmp42, subst3):
                                    pass
                                    if pattern_index == 0:
                                        pass
                                        # State 15854
                                        if len(subjects29) == 0:
                                            pass
                                            # State 15855
                                            if len(subjects) == 0:
                                                pass
                                                # 21: (F**(g*(e + x*f)))**n
                                                yield 21, subst4
                                subjects29.appendleft(tmp40)
                        if len(subjects29) >= 1 and isinstance(subjects29[0], Mul):
                            tmp43 = subjects29.popleft()
                            associative1 = tmp43
                            associative_type1 = type(tmp43)
                            subjects44 = deque(tmp43._args)
                            matcher = CommutativeMatcher15857.get()
                            tmp45 = subjects44
                            subjects44 = []
                            for s in tmp45:
                                matcher.add_subject(s)
                            for pattern_index, subst3 in matcher.match(tmp45, subst2):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 15872
                                    if len(subjects29) == 0:
                                        pass
                                        # State 15873
                                        if len(subjects) == 0:
                                            pass
                                            # 21: (F**(g*(e + x*f)))**n
                                            yield 21, subst3
                            subjects29.appendleft(tmp43)
                    subjects29.appendleft(tmp30)
                subjects.appendleft(tmp28)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.4', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 16389
            if len(subjects) >= 1 and isinstance(subjects[0], Pow):
                tmp47 = subjects.popleft()
                subjects48 = deque(tmp47._args)
                # State 16390
                if len(subjects48) >= 1:
                    tmp49 = subjects48.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.2', tmp49)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 16391
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.4.0', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 16392
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i2.2.1.4.1.0', S(0))
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 16393
                                subst5 = Substitution(subst4)
                                try:
                                    subst5.try_add_variable('i2.2.1.4.1.1.0', S(1))
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 16394
                                    if len(subjects48) >= 1:
                                        tmp54 = subjects48.popleft()
                                        subst6 = Substitution(subst5)
                                        try:
                                            subst6.try_add_variable('i2.2.3.1.1.0', tmp54)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 16395
                                            if len(subjects48) == 0:
                                                pass
                                                # State 16396
                                                if len(subjects) == 0:
                                                    pass
                                                    # 22: (F**(g*(e + f*x)))**n
                                                    yield 22, subst6
                                        subjects48.appendleft(tmp54)
                                if len(subjects48) >= 1 and isinstance(subjects48[0], Mul):
                                    tmp56 = subjects48.popleft()
                                    associative1 = tmp56
                                    associative_type1 = type(tmp56)
                                    subjects57 = deque(tmp56._args)
                                    matcher = CommutativeMatcher16398.get()
                                    tmp58 = subjects57
                                    subjects57 = []
                                    for s in tmp58:
                                        matcher.add_subject(s)
                                    for pattern_index, subst5 in matcher.match(tmp58, subst4):
                                        pass
                                        if pattern_index == 0:
                                            pass
                                            # State 16399
                                            if len(subjects48) == 0:
                                                pass
                                                # State 16400
                                                if len(subjects) == 0:
                                                    pass
                                                    # 22: (F**(g*(e + f*x)))**n
                                                    yield 22, subst5
                                    subjects48.appendleft(tmp56)
                            if len(subjects48) >= 1 and isinstance(subjects48[0], Add):
                                tmp59 = subjects48.popleft()
                                associative1 = tmp59
                                associative_type1 = type(tmp59)
                                subjects60 = deque(tmp59._args)
                                matcher = CommutativeMatcher16402.get()
                                tmp61 = subjects60
                                subjects60 = []
                                for s in tmp61:
                                    matcher.add_subject(s)
                                for pattern_index, subst4 in matcher.match(tmp61, subst3):
                                    pass
                                    if pattern_index == 0:
                                        pass
                                        # State 16408
                                        if len(subjects48) == 0:
                                            pass
                                            # State 16409
                                            if len(subjects) == 0:
                                                pass
                                                # 22: (F**(g*(e + f*x)))**n
                                                yield 22, subst4
                                subjects48.appendleft(tmp59)
                        if len(subjects48) >= 1 and isinstance(subjects48[0], Mul):
                            tmp62 = subjects48.popleft()
                            associative1 = tmp62
                            associative_type1 = type(tmp62)
                            subjects63 = deque(tmp62._args)
                            matcher = CommutativeMatcher16411.get()
                            tmp64 = subjects63
                            subjects63 = []
                            for s in tmp64:
                                matcher.add_subject(s)
                            for pattern_index, subst3 in matcher.match(tmp64, subst2):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 16426
                                    if len(subjects48) == 0:
                                        pass
                                        # State 16427
                                        if len(subjects) == 0:
                                            pass
                                            # 22: (F**(g*(e + f*x)))**n
                                            yield 22, subst3
                            subjects48.appendleft(tmp62)
                    subjects48.appendleft(tmp49)
                subjects.appendleft(tmp47)
        if len(subjects) >= 1 and isinstance(subjects[0], Pow):
            tmp65 = subjects.popleft()
            subjects66 = deque(tmp65._args)
            # State 2674
            if len(subjects66) >= 1:
                tmp67 = subjects66.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.1.1', tmp67)
                except ValueError:
                    pass
                else:
                    pass
                    # State 2675
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.2_1', 1)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 2676
                        if len(subjects66) == 0:
                            pass
                            # State 2677
                            if len(subjects) == 0:
                                pass
                                # 0: x**n
                                yield 0, subst2
                    if len(subjects66) >= 1:
                        tmp70 = subjects66.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.1.2_1', tmp70)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 2676
                            if len(subjects66) == 0:
                                pass
                                # State 2677
                                if len(subjects) == 0:
                                    pass
                                    # 0: x**n
                                    yield 0, subst2
                        subjects66.appendleft(tmp70)
                    if len(subjects66) >= 1:
                        tmp72 = subjects66.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.1.2', tmp72)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 6913
                            if len(subjects66) == 0:
                                pass
                                # State 6914
                                if len(subjects) == 0:
                                    pass
                                    # 5: x**j
                                    yield 5, subst2
                        subjects66.appendleft(tmp72)
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.2_2', 1)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 7577
                        if len(subjects66) == 0:
                            pass
                            # State 7578
                            if len(subjects) == 0:
                                pass
                                # 9: x**r
                                yield 9, subst2
                    if len(subjects66) >= 1:
                        tmp75 = subjects66.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.1.2_2', tmp75)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 7577
                            if len(subjects66) == 0:
                                pass
                                # State 7578
                                if len(subjects) == 0:
                                    pass
                                    # 9: x**r
                                    yield 9, subst2
                        subjects66.appendleft(tmp75)
                    if len(subjects66) >= 1:
                        tmp77 = subjects66.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.1.2_1', tmp77)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 8673
                            if len(subjects66) == 0:
                                pass
                                # State 8674
                                if len(subjects) == 0:
                                    pass
                                    # 13: x**n2
                                    yield 13, subst2
                        subjects66.appendleft(tmp77)
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.2', 1)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 9047
                        if len(subjects66) == 0:
                            pass
                            # State 9048
                            if len(subjects) == 0:
                                pass
                                # 14: x**n
                                yield 14, subst2
                    if len(subjects66) >= 1:
                        tmp80 = subjects66.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.1.2', tmp80)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 9047
                            if len(subjects66) == 0:
                                pass
                                # State 9048
                                if len(subjects) == 0:
                                    pass
                                    # 14: x**n
                                    yield 14, subst2
                        subjects66.appendleft(tmp80)
                    if len(subjects66) >= 1:
                        tmp82 = subjects66.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.1.2_2', tmp82)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 9111
                            if len(subjects66) == 0:
                                pass
                                # State 9112
                                if len(subjects) == 0:
                                    pass
                                    # 15: x**n2
                                    yield 15, subst2
                        subjects66.appendleft(tmp82)
                    if len(subjects66) >= 1 and subjects66[0] == Integer(2):
                        tmp84 = subjects66.popleft()
                        # State 5294
                        if len(subjects66) == 0:
                            pass
                            # State 5295
                            if len(subjects) == 0:
                                pass
                                # 3: x**2
                                yield 3, subst1
                        subjects66.appendleft(tmp84)
                subjects66.appendleft(tmp67)
            if len(subjects66) >= 1:
                tmp85 = subjects66.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.1.0', tmp85)
                except ValueError:
                    pass
                else:
                    pass
                    # State 4062
                    if len(subjects66) >= 1 and subjects66[0] == Integer(2):
                        tmp87 = subjects66.popleft()
                        # State 4063
                        if len(subjects66) == 0:
                            pass
                            # State 4064
                            if len(subjects) == 0:
                                pass
                                # 1: v**2
                                yield 1, subst1
                        subjects66.appendleft(tmp87)
                subjects66.appendleft(tmp85)
            if len(subjects66) >= 1:
                tmp88 = subjects66.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.0', tmp88)
                except ValueError:
                    pass
                else:
                    pass
                    # State 5252
                    if len(subjects66) >= 1 and subjects66[0] == Integer(2):
                        tmp90 = subjects66.popleft()
                        # State 5253
                        if len(subjects66) == 0:
                            pass
                            # State 5254
                            if len(subjects) == 0:
                                pass
                                # 2: v**2
                                yield 2, subst1
                        subjects66.appendleft(tmp90)
                    if len(subjects66) >= 1:
                        tmp91 = subjects66.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.1.2', tmp91)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 6553
                            if len(subjects66) == 0:
                                pass
                                # State 6554
                                if len(subjects) == 0:
                                    pass
                                    # 4: x**n
                                    yield 4, subst2
                        subjects66.appendleft(tmp91)
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.2', 1)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 7222
                        if len(subjects66) == 0:
                            pass
                            # State 7223
                            if len(subjects) == 0:
                                pass
                                # 7: x**non2
                                yield 7, subst2
                    if len(subjects66) >= 1:
                        tmp94 = subjects66.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.1.2', tmp94)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 7222
                            if len(subjects66) == 0:
                                pass
                                # State 7223
                                if len(subjects) == 0:
                                    pass
                                    # 7: x**non2
                                    yield 7, subst2
                        subjects66.appendleft(tmp94)
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.2_1', 1)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 8349
                        if len(subjects66) == 0:
                            pass
                            # State 8350
                            if len(subjects) == 0:
                                pass
                                # 11: x**n2
                                yield 11, subst2
                    if len(subjects66) >= 1:
                        tmp97 = subjects66.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.1.2_1', tmp97)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 8349
                            if len(subjects66) == 0:
                                pass
                                # State 8350
                                if len(subjects) == 0:
                                    pass
                                    # 11: x**n2
                                    yield 11, subst2
                        subjects66.appendleft(tmp97)
                    if len(subjects66) >= 1:
                        tmp99 = subjects66.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.1.2_1', tmp99)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 9345
                            if len(subjects66) == 0:
                                pass
                                # State 9346
                                if len(subjects) == 0:
                                    pass
                                    # 16: x**n2
                                    yield 16, subst2
                        subjects66.appendleft(tmp99)
                subjects66.appendleft(tmp88)
            if len(subjects66) >= 1:
                tmp101 = subjects66.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.0_1', tmp101)
                except ValueError:
                    pass
                else:
                    pass
                    # State 7173
                    if len(subjects66) >= 1:
                        tmp103 = subjects66.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.1.2', tmp103)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 7174
                            if len(subjects66) == 0:
                                pass
                                # State 7175
                                if len(subjects) == 0:
                                    pass
                                    # 6: x**n
                                    yield 6, subst2
                        subjects66.appendleft(tmp103)
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.2', 1)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 7468
                        if len(subjects66) == 0:
                            pass
                            # State 7469
                            if len(subjects) == 0:
                                pass
                                # 8: x**mn
                                yield 8, subst2
                    if len(subjects66) >= 1:
                        tmp106 = subjects66.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.1.2', tmp106)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 7468
                            if len(subjects66) == 0:
                                pass
                                # State 7469
                                if len(subjects) == 0:
                                    pass
                                    # 8: x**mn
                                    yield 8, subst2
                        subjects66.appendleft(tmp106)
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.2_1', 1)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 8452
                        if len(subjects66) == 0:
                            pass
                            # State 8453
                            if len(subjects) == 0:
                                pass
                                # 12: x**n
                                yield 12, subst2
                    if len(subjects66) >= 1:
                        tmp109 = subjects66.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.1.2_1', tmp109)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 8452
                            if len(subjects66) == 0:
                                pass
                                # State 8453
                                if len(subjects) == 0:
                                    pass
                                    # 12: x**n
                                    yield 12, subst2
                        subjects66.appendleft(tmp109)
                subjects66.appendleft(tmp101)
            if len(subjects66) >= 1:
                tmp111 = subjects66.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.1.1_1', tmp111)
                except ValueError:
                    pass
                else:
                    pass
                    # State 7770
                    if len(subjects66) >= 1:
                        tmp113 = subjects66.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.1.2', tmp113)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 7771
                            if len(subjects66) == 0:
                                pass
                                # State 7772
                                if len(subjects) == 0:
                                    pass
                                    # 10: v**n
                                    yield 10, subst2
                        subjects66.appendleft(tmp113)
                subjects66.appendleft(tmp111)
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.0', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 10782
                if len(subjects66) >= 1 and isinstance(subjects66[0], Pow):
                    tmp116 = subjects66.popleft()
                    subjects117 = deque(tmp116._args)
                    # State 10783
                    if len(subjects117) >= 1:
                        tmp118 = subjects117.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.0', tmp118)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 10784
                            if len(subjects117) >= 1 and subjects117[0] == Integer(-1):
                                tmp120 = subjects117.popleft()
                                # State 10785
                                if len(subjects117) == 0:
                                    pass
                                    # State 10786
                                    if len(subjects66) >= 1:
                                        tmp121 = subjects66.popleft()
                                        subst3 = Substitution(subst2)
                                        try:
                                            subst3.try_add_variable('i2.2.1.2', tmp121)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 10787
                                            if len(subjects66) == 0:
                                                pass
                                                # State 10788
                                                if len(subjects) == 0:
                                                    pass
                                                    # 17: (c/x)**n
                                                    yield 17, subst3
                                        subjects66.appendleft(tmp121)
                                    subst3 = Substitution(subst2)
                                    try:
                                        subst3.try_add_variable('i2.2.1.2_1', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 11122
                                        if len(subjects66) == 0:
                                            pass
                                            # State 11123
                                            if len(subjects) == 0:
                                                pass
                                                # 18: (c/x)**n2
                                                yield 18, subst3
                                    if len(subjects66) >= 1:
                                        tmp124 = subjects66.popleft()
                                        subst3 = Substitution(subst2)
                                        try:
                                            subst3.try_add_variable('i2.2.1.2_1', tmp124)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 11122
                                            if len(subjects66) == 0:
                                                pass
                                                # State 11123
                                                if len(subjects) == 0:
                                                    pass
                                                    # 18: (c/x)**n2
                                                    yield 18, subst3
                                        subjects66.appendleft(tmp124)
                                subjects117.appendleft(tmp120)
                        subjects117.appendleft(tmp118)
                    subjects66.appendleft(tmp116)
            if len(subjects66) >= 1:
                tmp126 = subjects66.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.1.2.1.1', tmp126)
                except ValueError:
                    pass
                else:
                    pass
                    # State 13920
                    if len(subjects66) >= 1 and subjects66[0] == Integer(2):
                        tmp128 = subjects66.popleft()
                        # State 13921
                        if len(subjects66) == 0:
                            pass
                            # State 13922
                            if len(subjects) == 0:
                                pass
                                # 19: x**2
                                yield 19, subst1
                        subjects66.appendleft(tmp128)
                subjects66.appendleft(tmp126)
            if len(subjects66) >= 1:
                tmp129 = subjects66.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.1.2.0', tmp129)
                except ValueError:
                    pass
                else:
                    pass
                    # State 109630
                    if len(subjects66) >= 1 and subjects66[0] == Integer(2):
                        tmp131 = subjects66.popleft()
                        # State 109631
                        if len(subjects66) == 0:
                            pass
                            # State 109632
                            if len(subjects) == 0:
                                pass
                                # 76: x**2
                                yield 76, subst1
                        subjects66.appendleft(tmp131)
                subjects66.appendleft(tmp129)
            if len(subjects66) >= 1:
                tmp132 = subjects66.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.1.2.1.0', tmp132)
                except ValueError:
                    pass
                else:
                    pass
                    # State 110623
                    if len(subjects66) >= 1 and subjects66[0] == Integer(2):
                        tmp134 = subjects66.popleft()
                        # State 110624
                        if len(subjects66) == 0:
                            pass
                            # State 110625
                            if len(subjects) == 0:
                                pass
                                # 79: x**2
                                yield 79, subst1
                        subjects66.appendleft(tmp134)
                subjects66.appendleft(tmp132)
            if len(subjects66) >= 1 and isinstance(subjects66[0], Mul):
                tmp135 = subjects66.popleft()
                associative1 = tmp135
                associative_type1 = type(tmp135)
                subjects136 = deque(tmp135._args)
                matcher = CommutativeMatcher10790.get()
                tmp137 = subjects136
                subjects136 = []
                for s in tmp137:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp137, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 10795
                        if len(subjects66) >= 1:
                            tmp138 = []
                            tmp138.append(subjects66.popleft())
                            while True:
                                if len(tmp138) > 1:
                                    tmp139 = create_operation_expression(associative1, tmp138)
                                elif len(tmp138) == 1:
                                    tmp139 = tmp138[0]
                                else:
                                    assert False, "Unreachable"
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i2.2.1.2', tmp139)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 10796
                                    if len(subjects66) == 0:
                                        pass
                                        # State 10797
                                        if len(subjects) == 0:
                                            pass
                                            # 17: (c/x)**n
                                            yield 17, subst2
                                if len(subjects66) == 0:
                                    break
                                tmp138.append(subjects66.popleft())
                            subjects66.extendleft(reversed(tmp138))
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.1.2_1', 1)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 11124
                            if len(subjects66) == 0:
                                pass
                                # State 11125
                                if len(subjects) == 0:
                                    pass
                                    # 18: (c/x)**n2
                                    yield 18, subst2
                        if len(subjects66) >= 1:
                            tmp142 = []
                            tmp142.append(subjects66.popleft())
                            while True:
                                if len(tmp142) > 1:
                                    tmp143 = create_operation_expression(associative1, tmp142)
                                elif len(tmp142) == 1:
                                    tmp143 = tmp142[0]
                                else:
                                    assert False, "Unreachable"
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i2.2.1.2_1', tmp143)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 11124
                                    if len(subjects66) == 0:
                                        pass
                                        # State 11125
                                        if len(subjects) == 0:
                                            pass
                                            # 18: (c/x)**n2
                                            yield 18, subst2
                                if len(subjects66) == 0:
                                    break
                                tmp142.append(subjects66.popleft())
                            subjects66.extendleft(reversed(tmp142))
                subjects66.appendleft(tmp135)
            if len(subjects66) >= 1 and isinstance(subjects66[0], Add):
                tmp145 = subjects66.popleft()
                associative1 = tmp145
                associative_type1 = type(tmp145)
                subjects146 = deque(tmp145._args)
                matcher = CommutativeMatcher13985.get()
                tmp147 = subjects146
                subjects146 = []
                for s in tmp147:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp147, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 13998
                        if len(subjects66) >= 1 and subjects66[0] == Rational(1, 2):
                            tmp148 = subjects66.popleft()
                            # State 13999
                            if len(subjects66) == 0:
                                pass
                                # State 14000
                                if len(subjects) == 0:
                                    pass
                                    # 20: sqrt(x**2*c + a)
                                    yield 20, subst1
                            subjects66.appendleft(tmp148)
                    if pattern_index == 1:
                        pass
                        # State 139663
                        if len(subjects66) >= 1:
                            tmp149 = []
                            tmp149.append(subjects66.popleft())
                            while True:
                                if len(tmp149) > 1:
                                    tmp150 = create_operation_expression(associative1, tmp149)
                                elif len(tmp149) == 1:
                                    tmp150 = tmp149[0]
                                else:
                                    assert False, "Unreachable"
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i2.2.1.2', tmp150)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 139664
                                    if len(subjects66) == 0:
                                        pass
                                        # State 139665
                                        if len(subjects) == 0:
                                            pass
                                            # 108: (x*e1 + d1)**p
                                            yield 108, subst2
                                if len(subjects66) == 0:
                                    break
                                tmp149.append(subjects66.popleft())
                            subjects66.extendleft(reversed(tmp149))
                    if pattern_index == 2:
                        pass
                        # State 139669
                        if len(subjects66) >= 1:
                            tmp152 = []
                            tmp152.append(subjects66.popleft())
                            while True:
                                if len(tmp152) > 1:
                                    tmp153 = create_operation_expression(associative1, tmp152)
                                elif len(tmp152) == 1:
                                    tmp153 = tmp152[0]
                                else:
                                    assert False, "Unreachable"
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i2.2.1.2', tmp153)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 139670
                                    if len(subjects66) == 0:
                                        pass
                                        # State 139671
                                        if len(subjects) == 0:
                                            pass
                                            # 109: (x*e2 + d2)**p
                                            yield 109, subst2
                                if len(subjects66) == 0:
                                    break
                                tmp152.append(subjects66.popleft())
                            subjects66.extendleft(reversed(tmp152))
                subjects66.appendleft(tmp145)
            if len(subjects66) >= 1 and isinstance(subjects66[0], Pow):
                tmp155 = subjects66.popleft()
                subjects156 = deque(tmp155._args)
                # State 15874
                if len(subjects156) >= 1:
                    tmp157 = subjects156.popleft()
                    subst1 = Substitution(subst0)
                    try:
                        subst1.try_add_variable('i2.2', tmp157)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 15875
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.4.0', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 15876
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.4.1.0', S(0))
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 15877
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.4.1.1.0_1', S(1))
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 15878
                                    if len(subjects156) >= 1:
                                        tmp162 = subjects156.popleft()
                                        subst5 = Substitution(subst4)
                                        try:
                                            subst5.try_add_variable('i2.4.1.1.0', tmp162)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 15879
                                            if len(subjects156) == 0:
                                                pass
                                                # State 15880
                                                subst6 = Substitution(subst5)
                                                try:
                                                    subst6.try_add_variable('i2.4', 1)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 15881
                                                    if len(subjects66) == 0:
                                                        pass
                                                        # State 15882
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 21: (F**(g*(e + x*f)))**n
                                                            yield 21, subst6
                                                if len(subjects66) >= 1:
                                                    tmp165 = subjects66.popleft()
                                                    subst6 = Substitution(subst5)
                                                    try:
                                                        subst6.try_add_variable('i2.4', tmp165)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 15881
                                                        if len(subjects66) == 0:
                                                            pass
                                                            # State 15882
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 21: (F**(g*(e + x*f)))**n
                                                                yield 21, subst6
                                                    subjects66.appendleft(tmp165)
                                        subjects156.appendleft(tmp162)
                                if len(subjects156) >= 1 and isinstance(subjects156[0], Mul):
                                    tmp167 = subjects156.popleft()
                                    associative1 = tmp167
                                    associative_type1 = type(tmp167)
                                    subjects168 = deque(tmp167._args)
                                    matcher = CommutativeMatcher15884.get()
                                    tmp169 = subjects168
                                    subjects168 = []
                                    for s in tmp169:
                                        matcher.add_subject(s)
                                    for pattern_index, subst4 in matcher.match(tmp169, subst3):
                                        pass
                                        if pattern_index == 0:
                                            pass
                                            # State 15885
                                            if len(subjects156) == 0:
                                                pass
                                                # State 15886
                                                subst5 = Substitution(subst4)
                                                try:
                                                    subst5.try_add_variable('i2.4', 1)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 15887
                                                    if len(subjects66) == 0:
                                                        pass
                                                        # State 15888
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 21: (F**(g*(e + x*f)))**n
                                                            yield 21, subst5
                                                if len(subjects66) >= 1:
                                                    tmp171 = subjects66.popleft()
                                                    subst5 = Substitution(subst4)
                                                    try:
                                                        subst5.try_add_variable('i2.4', tmp171)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 15887
                                                        if len(subjects66) == 0:
                                                            pass
                                                            # State 15888
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 21: (F**(g*(e + x*f)))**n
                                                                yield 21, subst5
                                                    subjects66.appendleft(tmp171)
                                    subjects156.appendleft(tmp167)
                            if len(subjects156) >= 1 and isinstance(subjects156[0], Add):
                                tmp173 = subjects156.popleft()
                                associative1 = tmp173
                                associative_type1 = type(tmp173)
                                subjects174 = deque(tmp173._args)
                                matcher = CommutativeMatcher15890.get()
                                tmp175 = subjects174
                                subjects174 = []
                                for s in tmp175:
                                    matcher.add_subject(s)
                                for pattern_index, subst3 in matcher.match(tmp175, subst2):
                                    pass
                                    if pattern_index == 0:
                                        pass
                                        # State 15896
                                        if len(subjects156) == 0:
                                            pass
                                            # State 15897
                                            subst4 = Substitution(subst3)
                                            try:
                                                subst4.try_add_variable('i2.4', 1)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 15898
                                                if len(subjects66) == 0:
                                                    pass
                                                    # State 15899
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 21: (F**(g*(e + x*f)))**n
                                                        yield 21, subst4
                                            if len(subjects66) >= 1:
                                                tmp177 = subjects66.popleft()
                                                subst4 = Substitution(subst3)
                                                try:
                                                    subst4.try_add_variable('i2.4', tmp177)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 15898
                                                    if len(subjects66) == 0:
                                                        pass
                                                        # State 15899
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 21: (F**(g*(e + x*f)))**n
                                                            yield 21, subst4
                                                subjects66.appendleft(tmp177)
                                subjects156.appendleft(tmp173)
                        if len(subjects156) >= 1 and isinstance(subjects156[0], Mul):
                            tmp179 = subjects156.popleft()
                            associative1 = tmp179
                            associative_type1 = type(tmp179)
                            subjects180 = deque(tmp179._args)
                            matcher = CommutativeMatcher15901.get()
                            tmp181 = subjects180
                            subjects180 = []
                            for s in tmp181:
                                matcher.add_subject(s)
                            for pattern_index, subst2 in matcher.match(tmp181, subst1):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 15916
                                    if len(subjects156) == 0:
                                        pass
                                        # State 15917
                                        subst3 = Substitution(subst2)
                                        try:
                                            subst3.try_add_variable('i2.4', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 15918
                                            if len(subjects66) == 0:
                                                pass
                                                # State 15919
                                                if len(subjects) == 0:
                                                    pass
                                                    # 21: (F**(g*(e + x*f)))**n
                                                    yield 21, subst3
                                        if len(subjects66) >= 1:
                                            tmp183 = subjects66.popleft()
                                            subst3 = Substitution(subst2)
                                            try:
                                                subst3.try_add_variable('i2.4', tmp183)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 15918
                                                if len(subjects66) == 0:
                                                    pass
                                                    # State 15919
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 21: (F**(g*(e + x*f)))**n
                                                        yield 21, subst3
                                            subjects66.appendleft(tmp183)
                            subjects156.appendleft(tmp179)
                    subjects156.appendleft(tmp157)
                if len(subjects156) >= 1:
                    tmp185 = subjects156.popleft()
                    subst1 = Substitution(subst0)
                    try:
                        subst1.try_add_variable('i2.2.1.2', tmp185)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 16428
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.1.4.0', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 16429
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.4.1.0', S(0))
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 16430
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.2.1.4.1.1.0', S(1))
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 16431
                                    if len(subjects156) >= 1:
                                        tmp190 = subjects156.popleft()
                                        subst5 = Substitution(subst4)
                                        try:
                                            subst5.try_add_variable('i2.2.3.1.1.0', tmp190)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 16432
                                            if len(subjects156) == 0:
                                                pass
                                                # State 16433
                                                subst6 = Substitution(subst5)
                                                try:
                                                    subst6.try_add_variable('i2.2.1.4', 1)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 16434
                                                    if len(subjects66) == 0:
                                                        pass
                                                        # State 16435
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 22: (F**(g*(e + f*x)))**n
                                                            yield 22, subst6
                                                if len(subjects66) >= 1:
                                                    tmp193 = subjects66.popleft()
                                                    subst6 = Substitution(subst5)
                                                    try:
                                                        subst6.try_add_variable('i2.2.1.4', tmp193)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 16434
                                                        if len(subjects66) == 0:
                                                            pass
                                                            # State 16435
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 22: (F**(g*(e + f*x)))**n
                                                                yield 22, subst6
                                                    subjects66.appendleft(tmp193)
                                        subjects156.appendleft(tmp190)
                                if len(subjects156) >= 1 and isinstance(subjects156[0], Mul):
                                    tmp195 = subjects156.popleft()
                                    associative1 = tmp195
                                    associative_type1 = type(tmp195)
                                    subjects196 = deque(tmp195._args)
                                    matcher = CommutativeMatcher16437.get()
                                    tmp197 = subjects196
                                    subjects196 = []
                                    for s in tmp197:
                                        matcher.add_subject(s)
                                    for pattern_index, subst4 in matcher.match(tmp197, subst3):
                                        pass
                                        if pattern_index == 0:
                                            pass
                                            # State 16438
                                            if len(subjects156) == 0:
                                                pass
                                                # State 16439
                                                subst5 = Substitution(subst4)
                                                try:
                                                    subst5.try_add_variable('i2.2.1.4', 1)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 16440
                                                    if len(subjects66) == 0:
                                                        pass
                                                        # State 16441
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 22: (F**(g*(e + f*x)))**n
                                                            yield 22, subst5
                                                if len(subjects66) >= 1:
                                                    tmp199 = subjects66.popleft()
                                                    subst5 = Substitution(subst4)
                                                    try:
                                                        subst5.try_add_variable('i2.2.1.4', tmp199)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 16440
                                                        if len(subjects66) == 0:
                                                            pass
                                                            # State 16441
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 22: (F**(g*(e + f*x)))**n
                                                                yield 22, subst5
                                                    subjects66.appendleft(tmp199)
                                    subjects156.appendleft(tmp195)
                            if len(subjects156) >= 1 and isinstance(subjects156[0], Add):
                                tmp201 = subjects156.popleft()
                                associative1 = tmp201
                                associative_type1 = type(tmp201)
                                subjects202 = deque(tmp201._args)
                                matcher = CommutativeMatcher16443.get()
                                tmp203 = subjects202
                                subjects202 = []
                                for s in tmp203:
                                    matcher.add_subject(s)
                                for pattern_index, subst3 in matcher.match(tmp203, subst2):
                                    pass
                                    if pattern_index == 0:
                                        pass
                                        # State 16449
                                        if len(subjects156) == 0:
                                            pass
                                            # State 16450
                                            subst4 = Substitution(subst3)
                                            try:
                                                subst4.try_add_variable('i2.2.1.4', 1)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 16451
                                                if len(subjects66) == 0:
                                                    pass
                                                    # State 16452
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 22: (F**(g*(e + f*x)))**n
                                                        yield 22, subst4
                                            if len(subjects66) >= 1:
                                                tmp205 = subjects66.popleft()
                                                subst4 = Substitution(subst3)
                                                try:
                                                    subst4.try_add_variable('i2.2.1.4', tmp205)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 16451
                                                    if len(subjects66) == 0:
                                                        pass
                                                        # State 16452
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 22: (F**(g*(e + f*x)))**n
                                                            yield 22, subst4
                                                subjects66.appendleft(tmp205)
                                subjects156.appendleft(tmp201)
                        if len(subjects156) >= 1 and isinstance(subjects156[0], Mul):
                            tmp207 = subjects156.popleft()
                            associative1 = tmp207
                            associative_type1 = type(tmp207)
                            subjects208 = deque(tmp207._args)
                            matcher = CommutativeMatcher16454.get()
                            tmp209 = subjects208
                            subjects208 = []
                            for s in tmp209:
                                matcher.add_subject(s)
                            for pattern_index, subst2 in matcher.match(tmp209, subst1):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 16469
                                    if len(subjects156) == 0:
                                        pass
                                        # State 16470
                                        subst3 = Substitution(subst2)
                                        try:
                                            subst3.try_add_variable('i2.2.1.4', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 16471
                                            if len(subjects66) == 0:
                                                pass
                                                # State 16472
                                                if len(subjects) == 0:
                                                    pass
                                                    # 22: (F**(g*(e + f*x)))**n
                                                    yield 22, subst3
                                        if len(subjects66) >= 1:
                                            tmp211 = subjects66.popleft()
                                            subst3 = Substitution(subst2)
                                            try:
                                                subst3.try_add_variable('i2.2.1.4', tmp211)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 16471
                                                if len(subjects66) == 0:
                                                    pass
                                                    # State 16472
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 22: (F**(g*(e + f*x)))**n
                                                        yield 22, subst3
                                            subjects66.appendleft(tmp211)
                            subjects156.appendleft(tmp207)
                    subjects156.appendleft(tmp185)
                subjects66.appendleft(tmp155)
            if len(subjects66) >= 1 and isinstance(subjects66[0], sin):
                tmp213 = subjects66.popleft()
                subjects214 = deque(tmp213._args)
                # State 63802
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.2.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 63803
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.2.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 63804
                        if len(subjects214) >= 1:
                            tmp217 = subjects214.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.2.1.0', tmp217)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 63805
                                if len(subjects214) == 0:
                                    pass
                                    # State 63806
                                    if len(subjects66) >= 1 and subjects66[0] == Integer(-1):
                                        tmp219 = subjects66.popleft()
                                        # State 63807
                                        if len(subjects66) == 0:
                                            pass
                                            # State 63808
                                            if len(subjects) == 0:
                                                pass
                                                # 34: 1/sin(e + x*f)
                                                yield 34, subst3
                                        subjects66.appendleft(tmp219)
                            subjects214.appendleft(tmp217)
                    if len(subjects214) >= 1 and isinstance(subjects214[0], Mul):
                        tmp220 = subjects214.popleft()
                        associative1 = tmp220
                        associative_type1 = type(tmp220)
                        subjects221 = deque(tmp220._args)
                        matcher = CommutativeMatcher63810.get()
                        tmp222 = subjects221
                        subjects221 = []
                        for s in tmp222:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp222, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 63811
                                if len(subjects214) == 0:
                                    pass
                                    # State 63812
                                    if len(subjects66) >= 1 and subjects66[0] == Integer(-1):
                                        tmp223 = subjects66.popleft()
                                        # State 63813
                                        if len(subjects66) == 0:
                                            pass
                                            # State 63814
                                            if len(subjects) == 0:
                                                pass
                                                # 34: 1/sin(e + x*f)
                                                yield 34, subst2
                                        subjects66.appendleft(tmp223)
                        subjects214.appendleft(tmp220)
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.3.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 64432
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.3.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 64433
                        if len(subjects214) >= 1:
                            tmp226 = subjects214.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.3.1.0', tmp226)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 64434
                                if len(subjects214) == 0:
                                    pass
                                    # State 64435
                                    if len(subjects66) >= 1 and subjects66[0] == Integer(-1):
                                        tmp228 = subjects66.popleft()
                                        # State 64436
                                        if len(subjects66) == 0:
                                            pass
                                            # State 64437
                                            if len(subjects) == 0:
                                                pass
                                                # 36: 1/sin(e + x*f)
                                                yield 36, subst3
                                        subjects66.appendleft(tmp228)
                            subjects214.appendleft(tmp226)
                    if len(subjects214) >= 1 and isinstance(subjects214[0], Mul):
                        tmp229 = subjects214.popleft()
                        associative1 = tmp229
                        associative_type1 = type(tmp229)
                        subjects230 = deque(tmp229._args)
                        matcher = CommutativeMatcher64439.get()
                        tmp231 = subjects230
                        subjects230 = []
                        for s in tmp231:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp231, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 64440
                                if len(subjects214) == 0:
                                    pass
                                    # State 64441
                                    if len(subjects66) >= 1 and subjects66[0] == Integer(-1):
                                        tmp232 = subjects66.popleft()
                                        # State 64442
                                        if len(subjects66) == 0:
                                            pass
                                            # State 64443
                                            if len(subjects) == 0:
                                                pass
                                                # 36: 1/sin(e + x*f)
                                                yield 36, subst2
                                        subjects66.appendleft(tmp232)
                        subjects214.appendleft(tmp229)
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.4.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 91143
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.4.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 91144
                        if len(subjects214) >= 1:
                            tmp235 = subjects214.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.4.1.0', tmp235)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 91145
                                if len(subjects214) == 0:
                                    pass
                                    # State 91146
                                    if len(subjects66) >= 1 and subjects66[0] == Integer(-1):
                                        tmp237 = subjects66.popleft()
                                        # State 91147
                                        if len(subjects66) == 0:
                                            pass
                                            # State 91148
                                            if len(subjects) == 0:
                                                pass
                                                # 62: 1/sin(c + x*d)
                                                yield 62, subst3
                                        subjects66.appendleft(tmp237)
                            subjects214.appendleft(tmp235)
                    if len(subjects214) >= 1 and isinstance(subjects214[0], Mul):
                        tmp238 = subjects214.popleft()
                        associative1 = tmp238
                        associative_type1 = type(tmp238)
                        subjects239 = deque(tmp238._args)
                        matcher = CommutativeMatcher91150.get()
                        tmp240 = subjects239
                        subjects239 = []
                        for s in tmp240:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp240, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 91151
                                if len(subjects214) == 0:
                                    pass
                                    # State 91152
                                    if len(subjects66) >= 1 and subjects66[0] == Integer(-1):
                                        tmp241 = subjects66.popleft()
                                        # State 91153
                                        if len(subjects66) == 0:
                                            pass
                                            # State 91154
                                            if len(subjects) == 0:
                                                pass
                                                # 62: 1/sin(c + x*d)
                                                yield 62, subst2
                                        subjects66.appendleft(tmp241)
                        subjects214.appendleft(tmp238)
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.1.3.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 91309
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.3.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 91310
                        if len(subjects214) >= 1:
                            tmp244 = subjects214.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.3.1.0', tmp244)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 91311
                                if len(subjects214) == 0:
                                    pass
                                    # State 91312
                                    if len(subjects66) >= 1 and subjects66[0] == Integer(-1):
                                        tmp246 = subjects66.popleft()
                                        # State 91313
                                        if len(subjects66) == 0:
                                            pass
                                            # State 91314
                                            if len(subjects) == 0:
                                                pass
                                                # 64: 1/sin(e + x*f)
                                                yield 64, subst3
                                        subjects66.appendleft(tmp246)
                            subjects214.appendleft(tmp244)
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.3.1.0', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 99241
                        if len(subjects214) >= 1 and isinstance(subjects214[0], Pow):
                            tmp248 = subjects214.popleft()
                            subjects249 = deque(tmp248._args)
                            # State 99242
                            if len(subjects249) >= 1:
                                tmp250 = subjects249.popleft()
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i2.2.0_1', tmp250)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 99243
                                    if len(subjects249) >= 1:
                                        tmp252 = subjects249.popleft()
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.2.1.3.1.2', tmp252)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 99244
                                            if len(subjects249) == 0:
                                                pass
                                                # State 99245
                                                if len(subjects214) == 0:
                                                    pass
                                                    # State 99246
                                                    if len(subjects66) >= 1 and subjects66[0] == Integer(-1):
                                                        tmp254 = subjects66.popleft()
                                                        # State 99247
                                                        if len(subjects66) == 0:
                                                            pass
                                                            # State 99248
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 68: 1/sin(x**n*d + c)
                                                                yield 68, subst4
                                                        subjects66.appendleft(tmp254)
                                        subjects249.appendleft(tmp252)
                                subjects249.appendleft(tmp250)
                            subjects214.appendleft(tmp248)
                    if len(subjects214) >= 1 and isinstance(subjects214[0], Mul):
                        tmp255 = subjects214.popleft()
                        associative1 = tmp255
                        associative_type1 = type(tmp255)
                        subjects256 = deque(tmp255._args)
                        matcher = CommutativeMatcher91316.get()
                        tmp257 = subjects256
                        subjects256 = []
                        for s in tmp257:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp257, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 91317
                                if len(subjects214) == 0:
                                    pass
                                    # State 91318
                                    if len(subjects66) >= 1 and subjects66[0] == Integer(-1):
                                        tmp258 = subjects66.popleft()
                                        # State 91319
                                        if len(subjects66) == 0:
                                            pass
                                            # State 91320
                                            if len(subjects) == 0:
                                                pass
                                                # 64: 1/sin(e + x*f)
                                                yield 64, subst2
                                        subjects66.appendleft(tmp258)
                            if pattern_index == 1:
                                pass
                                # State 99253
                                if len(subjects214) == 0:
                                    pass
                                    # State 99254
                                    if len(subjects66) >= 1 and subjects66[0] == Integer(-1):
                                        tmp259 = subjects66.popleft()
                                        # State 99255
                                        if len(subjects66) == 0:
                                            pass
                                            # State 99256
                                            if len(subjects) == 0:
                                                pass
                                                # 68: 1/sin(x**n*d + c)
                                                yield 68, subst2
                                        subjects66.appendleft(tmp259)
                        subjects214.appendleft(tmp255)
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.2.3.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 92046
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.2.3.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 92047
                        if len(subjects214) >= 1:
                            tmp262 = subjects214.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.2.3.1.0', tmp262)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 92048
                                if len(subjects214) == 0:
                                    pass
                                    # State 92049
                                    if len(subjects66) >= 1 and subjects66[0] == Integer(-1):
                                        tmp264 = subjects66.popleft()
                                        # State 92050
                                        if len(subjects66) == 0:
                                            pass
                                            # State 92051
                                            if len(subjects) == 0:
                                                pass
                                                # 66: 1/sin(e + x*f)
                                                yield 66, subst3
                                        subjects66.appendleft(tmp264)
                            subjects214.appendleft(tmp262)
                    if len(subjects214) >= 1 and isinstance(subjects214[0], Mul):
                        tmp265 = subjects214.popleft()
                        associative1 = tmp265
                        associative_type1 = type(tmp265)
                        subjects266 = deque(tmp265._args)
                        matcher = CommutativeMatcher92053.get()
                        tmp267 = subjects266
                        subjects266 = []
                        for s in tmp267:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp267, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 92054
                                if len(subjects214) == 0:
                                    pass
                                    # State 92055
                                    if len(subjects66) >= 1 and subjects66[0] == Integer(-1):
                                        tmp268 = subjects66.popleft()
                                        # State 92056
                                        if len(subjects66) == 0:
                                            pass
                                            # State 92057
                                            if len(subjects) == 0:
                                                pass
                                                # 66: 1/sin(e + x*f)
                                                yield 66, subst2
                                        subjects66.appendleft(tmp268)
                        subjects214.appendleft(tmp265)
                if len(subjects214) >= 1:
                    tmp269 = subjects214.popleft()
                    subst1 = Substitution(subst0)
                    try:
                        subst1.try_add_variable('i2.2.1.2', tmp269)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 99459
                        if len(subjects214) == 0:
                            pass
                            # State 99460
                            if len(subjects66) >= 1 and subjects66[0] == Integer(-1):
                                tmp271 = subjects66.popleft()
                                # State 99461
                                if len(subjects66) == 0:
                                    pass
                                    # State 99462
                                    if len(subjects) == 0:
                                        pass
                                        # 70: 1/sin(v)
                                        yield 70, subst1
                                subjects66.appendleft(tmp271)
                    subjects214.appendleft(tmp269)
                if len(subjects214) >= 1 and isinstance(subjects214[0], Add):
                    tmp272 = subjects214.popleft()
                    associative1 = tmp272
                    associative_type1 = type(tmp272)
                    subjects273 = deque(tmp272._args)
                    matcher = CommutativeMatcher63816.get()
                    tmp274 = subjects273
                    subjects273 = []
                    for s in tmp274:
                        matcher.add_subject(s)
                    for pattern_index, subst1 in matcher.match(tmp274, subst0):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 63822
                            if len(subjects214) == 0:
                                pass
                                # State 63823
                                if len(subjects66) >= 1 and subjects66[0] == Integer(-1):
                                    tmp275 = subjects66.popleft()
                                    # State 63824
                                    if len(subjects66) == 0:
                                        pass
                                        # State 63825
                                        if len(subjects) == 0:
                                            pass
                                            # 34: 1/sin(e + x*f)
                                            yield 34, subst1
                                    subjects66.appendleft(tmp275)
                        if pattern_index == 1:
                            pass
                            # State 64447
                            if len(subjects214) == 0:
                                pass
                                # State 64448
                                if len(subjects66) >= 1 and subjects66[0] == Integer(-1):
                                    tmp276 = subjects66.popleft()
                                    # State 64449
                                    if len(subjects66) == 0:
                                        pass
                                        # State 64450
                                        if len(subjects) == 0:
                                            pass
                                            # 36: 1/sin(e + x*f)
                                            yield 36, subst1
                                    subjects66.appendleft(tmp276)
                        if pattern_index == 2:
                            pass
                            # State 91158
                            if len(subjects214) == 0:
                                pass
                                # State 91159
                                if len(subjects66) >= 1 and subjects66[0] == Integer(-1):
                                    tmp277 = subjects66.popleft()
                                    # State 91160
                                    if len(subjects66) == 0:
                                        pass
                                        # State 91161
                                        if len(subjects) == 0:
                                            pass
                                            # 62: 1/sin(c + x*d)
                                            yield 62, subst1
                                    subjects66.appendleft(tmp277)
                        if pattern_index == 3:
                            pass
                            # State 91324
                            if len(subjects214) == 0:
                                pass
                                # State 91325
                                if len(subjects66) >= 1 and subjects66[0] == Integer(-1):
                                    tmp278 = subjects66.popleft()
                                    # State 91326
                                    if len(subjects66) == 0:
                                        pass
                                        # State 91327
                                        if len(subjects) == 0:
                                            pass
                                            # 64: 1/sin(e + x*f)
                                            yield 64, subst1
                                    subjects66.appendleft(tmp278)
                        if pattern_index == 4:
                            pass
                            # State 92061
                            if len(subjects214) == 0:
                                pass
                                # State 92062
                                if len(subjects66) >= 1 and subjects66[0] == Integer(-1):
                                    tmp279 = subjects66.popleft()
                                    # State 92063
                                    if len(subjects66) == 0:
                                        pass
                                        # State 92064
                                        if len(subjects) == 0:
                                            pass
                                            # 66: 1/sin(e + x*f)
                                            yield 66, subst1
                                    subjects66.appendleft(tmp279)
                        if pattern_index == 5:
                            pass
                            # State 99267
                            if len(subjects214) == 0:
                                pass
                                # State 99268
                                if len(subjects66) >= 1 and subjects66[0] == Integer(-1):
                                    tmp280 = subjects66.popleft()
                                    # State 99269
                                    if len(subjects66) == 0:
                                        pass
                                        # State 99270
                                        if len(subjects) == 0:
                                            pass
                                            # 68: 1/sin(x**n*d + c)
                                            yield 68, subst1
                                    subjects66.appendleft(tmp280)
                    subjects214.appendleft(tmp272)
                subjects66.appendleft(tmp213)
            if len(subjects66) >= 1 and isinstance(subjects66[0], cos):
                tmp281 = subjects66.popleft()
                subjects282 = deque(tmp281._args)
                # State 64081
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.2.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 64082
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.2.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 64083
                        if len(subjects282) >= 1:
                            tmp285 = subjects282.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.2.1.0', tmp285)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 64084
                                if len(subjects282) == 0:
                                    pass
                                    # State 64085
                                    if len(subjects66) >= 1 and subjects66[0] == Integer(-1):
                                        tmp287 = subjects66.popleft()
                                        # State 64086
                                        if len(subjects66) == 0:
                                            pass
                                            # State 64087
                                            if len(subjects) == 0:
                                                pass
                                                # 35: 1/cos(e + x*f)
                                                yield 35, subst3
                                        subjects66.appendleft(tmp287)
                            subjects282.appendleft(tmp285)
                    if len(subjects282) >= 1 and isinstance(subjects282[0], Mul):
                        tmp288 = subjects282.popleft()
                        associative1 = tmp288
                        associative_type1 = type(tmp288)
                        subjects289 = deque(tmp288._args)
                        matcher = CommutativeMatcher64089.get()
                        tmp290 = subjects289
                        subjects289 = []
                        for s in tmp290:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp290, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 64090
                                if len(subjects282) == 0:
                                    pass
                                    # State 64091
                                    if len(subjects66) >= 1 and subjects66[0] == Integer(-1):
                                        tmp291 = subjects66.popleft()
                                        # State 64092
                                        if len(subjects66) == 0:
                                            pass
                                            # State 64093
                                            if len(subjects) == 0:
                                                pass
                                                # 35: 1/cos(e + x*f)
                                                yield 35, subst2
                                        subjects66.appendleft(tmp291)
                        subjects282.appendleft(tmp288)
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.3.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 64517
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.3.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 64518
                        if len(subjects282) >= 1:
                            tmp294 = subjects282.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.3.1.0', tmp294)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 64519
                                if len(subjects282) == 0:
                                    pass
                                    # State 64520
                                    if len(subjects66) >= 1 and subjects66[0] == Integer(-1):
                                        tmp296 = subjects66.popleft()
                                        # State 64521
                                        if len(subjects66) == 0:
                                            pass
                                            # State 64522
                                            if len(subjects) == 0:
                                                pass
                                                # 37: 1/cos(e + x*f)
                                                yield 37, subst3
                                        subjects66.appendleft(tmp296)
                            subjects282.appendleft(tmp294)
                    if len(subjects282) >= 1 and isinstance(subjects282[0], Mul):
                        tmp297 = subjects282.popleft()
                        associative1 = tmp297
                        associative_type1 = type(tmp297)
                        subjects298 = deque(tmp297._args)
                        matcher = CommutativeMatcher64524.get()
                        tmp299 = subjects298
                        subjects298 = []
                        for s in tmp299:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp299, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 64525
                                if len(subjects282) == 0:
                                    pass
                                    # State 64526
                                    if len(subjects66) >= 1 and subjects66[0] == Integer(-1):
                                        tmp300 = subjects66.popleft()
                                        # State 64527
                                        if len(subjects66) == 0:
                                            pass
                                            # State 64528
                                            if len(subjects) == 0:
                                                pass
                                                # 37: 1/cos(e + x*f)
                                                yield 37, subst2
                                        subjects66.appendleft(tmp300)
                        subjects282.appendleft(tmp297)
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.1.3.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 91259
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.3.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 91260
                        if len(subjects282) >= 1:
                            tmp303 = subjects282.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.3.1.0', tmp303)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 91261
                                if len(subjects282) == 0:
                                    pass
                                    # State 91262
                                    if len(subjects66) >= 1 and subjects66[0] == Integer(-1):
                                        tmp305 = subjects66.popleft()
                                        # State 91263
                                        if len(subjects66) == 0:
                                            pass
                                            # State 91264
                                            if len(subjects) == 0:
                                                pass
                                                # 63: 1/cos(e + x*f)
                                                yield 63, subst3
                                        subjects66.appendleft(tmp305)
                            subjects282.appendleft(tmp303)
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.3.1.0', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 98964
                        if len(subjects282) >= 1 and isinstance(subjects282[0], Pow):
                            tmp307 = subjects282.popleft()
                            subjects308 = deque(tmp307._args)
                            # State 98965
                            if len(subjects308) >= 1:
                                tmp309 = subjects308.popleft()
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i2.2.0_1', tmp309)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 98966
                                    if len(subjects308) >= 1:
                                        tmp311 = subjects308.popleft()
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.2.1.3.1.2', tmp311)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 98967
                                            if len(subjects308) == 0:
                                                pass
                                                # State 98968
                                                if len(subjects282) == 0:
                                                    pass
                                                    # State 98969
                                                    if len(subjects66) >= 1 and subjects66[0] == Integer(-1):
                                                        tmp313 = subjects66.popleft()
                                                        # State 98970
                                                        if len(subjects66) == 0:
                                                            pass
                                                            # State 98971
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 67: 1/cos(x**n*d + c)
                                                                yield 67, subst4
                                                        subjects66.appendleft(tmp313)
                                        subjects308.appendleft(tmp311)
                                subjects308.appendleft(tmp309)
                            subjects282.appendleft(tmp307)
                    if len(subjects282) >= 1 and isinstance(subjects282[0], Mul):
                        tmp314 = subjects282.popleft()
                        associative1 = tmp314
                        associative_type1 = type(tmp314)
                        subjects315 = deque(tmp314._args)
                        matcher = CommutativeMatcher91266.get()
                        tmp316 = subjects315
                        subjects315 = []
                        for s in tmp316:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp316, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 91267
                                if len(subjects282) == 0:
                                    pass
                                    # State 91268
                                    if len(subjects66) >= 1 and subjects66[0] == Integer(-1):
                                        tmp317 = subjects66.popleft()
                                        # State 91269
                                        if len(subjects66) == 0:
                                            pass
                                            # State 91270
                                            if len(subjects) == 0:
                                                pass
                                                # 63: 1/cos(e + x*f)
                                                yield 63, subst2
                                        subjects66.appendleft(tmp317)
                            if pattern_index == 1:
                                pass
                                # State 98976
                                if len(subjects282) == 0:
                                    pass
                                    # State 98977
                                    if len(subjects66) >= 1 and subjects66[0] == Integer(-1):
                                        tmp318 = subjects66.popleft()
                                        # State 98978
                                        if len(subjects66) == 0:
                                            pass
                                            # State 98979
                                            if len(subjects) == 0:
                                                pass
                                                # 67: 1/cos(x**n*d + c)
                                                yield 67, subst2
                                        subjects66.appendleft(tmp318)
                        subjects282.appendleft(tmp314)
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.2.3.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 91865
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.2.3.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 91866
                        if len(subjects282) >= 1:
                            tmp321 = subjects282.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.2.3.1.0', tmp321)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 91867
                                if len(subjects282) == 0:
                                    pass
                                    # State 91868
                                    if len(subjects66) >= 1 and subjects66[0] == Integer(-1):
                                        tmp323 = subjects66.popleft()
                                        # State 91869
                                        if len(subjects66) == 0:
                                            pass
                                            # State 91870
                                            if len(subjects) == 0:
                                                pass
                                                # 65: 1/cos(e + x*f)
                                                yield 65, subst3
                                        subjects66.appendleft(tmp323)
                            subjects282.appendleft(tmp321)
                    if len(subjects282) >= 1 and isinstance(subjects282[0], Mul):
                        tmp324 = subjects282.popleft()
                        associative1 = tmp324
                        associative_type1 = type(tmp324)
                        subjects325 = deque(tmp324._args)
                        matcher = CommutativeMatcher91872.get()
                        tmp326 = subjects325
                        subjects325 = []
                        for s in tmp326:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp326, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 91873
                                if len(subjects282) == 0:
                                    pass
                                    # State 91874
                                    if len(subjects66) >= 1 and subjects66[0] == Integer(-1):
                                        tmp327 = subjects66.popleft()
                                        # State 91875
                                        if len(subjects66) == 0:
                                            pass
                                            # State 91876
                                            if len(subjects) == 0:
                                                pass
                                                # 65: 1/cos(e + x*f)
                                                yield 65, subst2
                                        subjects66.appendleft(tmp327)
                        subjects282.appendleft(tmp324)
                if len(subjects282) >= 1:
                    tmp328 = subjects282.popleft()
                    subst1 = Substitution(subst0)
                    try:
                        subst1.try_add_variable('i2.2.1.2', tmp328)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 99421
                        if len(subjects282) == 0:
                            pass
                            # State 99422
                            if len(subjects66) >= 1 and subjects66[0] == Integer(-1):
                                tmp330 = subjects66.popleft()
                                # State 99423
                                if len(subjects66) == 0:
                                    pass
                                    # State 99424
                                    if len(subjects) == 0:
                                        pass
                                        # 69: 1/cos(v)
                                        yield 69, subst1
                                subjects66.appendleft(tmp330)
                    subjects282.appendleft(tmp328)
                if len(subjects282) >= 1 and isinstance(subjects282[0], Add):
                    tmp331 = subjects282.popleft()
                    associative1 = tmp331
                    associative_type1 = type(tmp331)
                    subjects332 = deque(tmp331._args)
                    matcher = CommutativeMatcher64095.get()
                    tmp333 = subjects332
                    subjects332 = []
                    for s in tmp333:
                        matcher.add_subject(s)
                    for pattern_index, subst1 in matcher.match(tmp333, subst0):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 64101
                            if len(subjects282) == 0:
                                pass
                                # State 64102
                                if len(subjects66) >= 1 and subjects66[0] == Integer(-1):
                                    tmp334 = subjects66.popleft()
                                    # State 64103
                                    if len(subjects66) == 0:
                                        pass
                                        # State 64104
                                        if len(subjects) == 0:
                                            pass
                                            # 35: 1/cos(e + x*f)
                                            yield 35, subst1
                                    subjects66.appendleft(tmp334)
                        if pattern_index == 1:
                            pass
                            # State 64532
                            if len(subjects282) == 0:
                                pass
                                # State 64533
                                if len(subjects66) >= 1 and subjects66[0] == Integer(-1):
                                    tmp335 = subjects66.popleft()
                                    # State 64534
                                    if len(subjects66) == 0:
                                        pass
                                        # State 64535
                                        if len(subjects) == 0:
                                            pass
                                            # 37: 1/cos(e + x*f)
                                            yield 37, subst1
                                    subjects66.appendleft(tmp335)
                        if pattern_index == 2:
                            pass
                            # State 91274
                            if len(subjects282) == 0:
                                pass
                                # State 91275
                                if len(subjects66) >= 1 and subjects66[0] == Integer(-1):
                                    tmp336 = subjects66.popleft()
                                    # State 91276
                                    if len(subjects66) == 0:
                                        pass
                                        # State 91277
                                        if len(subjects) == 0:
                                            pass
                                            # 63: 1/cos(e + x*f)
                                            yield 63, subst1
                                    subjects66.appendleft(tmp336)
                        if pattern_index == 3:
                            pass
                            # State 91880
                            if len(subjects282) == 0:
                                pass
                                # State 91881
                                if len(subjects66) >= 1 and subjects66[0] == Integer(-1):
                                    tmp337 = subjects66.popleft()
                                    # State 91882
                                    if len(subjects66) == 0:
                                        pass
                                        # State 91883
                                        if len(subjects) == 0:
                                            pass
                                            # 65: 1/cos(e + x*f)
                                            yield 65, subst1
                                    subjects66.appendleft(tmp337)
                        if pattern_index == 4:
                            pass
                            # State 98990
                            if len(subjects282) == 0:
                                pass
                                # State 98991
                                if len(subjects66) >= 1 and subjects66[0] == Integer(-1):
                                    tmp338 = subjects66.popleft()
                                    # State 98992
                                    if len(subjects66) == 0:
                                        pass
                                        # State 98993
                                        if len(subjects) == 0:
                                            pass
                                            # 67: 1/cos(x**n*d + c)
                                            yield 67, subst1
                                    subjects66.appendleft(tmp338)
                    subjects282.appendleft(tmp331)
                subjects66.appendleft(tmp281)
            if len(subjects66) >= 1 and isinstance(subjects66[0], tan):
                tmp339 = subjects66.popleft()
                subjects340 = deque(tmp339._args)
                # State 78064
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.3.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 78065
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.3.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 78066
                        if len(subjects340) >= 1:
                            tmp343 = subjects340.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.3.1.0', tmp343)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 78067
                                if len(subjects340) == 0:
                                    pass
                                    # State 78068
                                    if len(subjects66) >= 1 and subjects66[0] == Integer(-1):
                                        tmp345 = subjects66.popleft()
                                        # State 78069
                                        if len(subjects66) == 0:
                                            pass
                                            # State 78070
                                            if len(subjects) == 0:
                                                pass
                                                # 48: 1/tan(e + x*f)
                                                yield 48, subst3
                                        subjects66.appendleft(tmp345)
                            subjects340.appendleft(tmp343)
                    if len(subjects340) >= 1 and isinstance(subjects340[0], Mul):
                        tmp346 = subjects340.popleft()
                        associative1 = tmp346
                        associative_type1 = type(tmp346)
                        subjects347 = deque(tmp346._args)
                        matcher = CommutativeMatcher78072.get()
                        tmp348 = subjects347
                        subjects347 = []
                        for s in tmp348:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp348, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 78073
                                if len(subjects340) == 0:
                                    pass
                                    # State 78074
                                    if len(subjects66) >= 1 and subjects66[0] == Integer(-1):
                                        tmp349 = subjects66.popleft()
                                        # State 78075
                                        if len(subjects66) == 0:
                                            pass
                                            # State 78076
                                            if len(subjects) == 0:
                                                pass
                                                # 48: 1/tan(e + x*f)
                                                yield 48, subst2
                                        subjects66.appendleft(tmp349)
                        subjects340.appendleft(tmp346)
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.2.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 78317
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.2.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 78318
                        if len(subjects340) >= 1:
                            tmp352 = subjects340.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.2.1.0', tmp352)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 78319
                                if len(subjects340) == 0:
                                    pass
                                    # State 78320
                                    if len(subjects66) >= 1 and subjects66[0] == Integer(-1):
                                        tmp354 = subjects66.popleft()
                                        # State 78321
                                        if len(subjects66) == 0:
                                            pass
                                            # State 78322
                                            if len(subjects) == 0:
                                                pass
                                                # 50: 1/tan(e + x*f)
                                                yield 50, subst3
                                        subjects66.appendleft(tmp354)
                            subjects340.appendleft(tmp352)
                    if len(subjects340) >= 1 and isinstance(subjects340[0], Mul):
                        tmp355 = subjects340.popleft()
                        associative1 = tmp355
                        associative_type1 = type(tmp355)
                        subjects356 = deque(tmp355._args)
                        matcher = CommutativeMatcher78324.get()
                        tmp357 = subjects356
                        subjects356 = []
                        for s in tmp357:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp357, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 78325
                                if len(subjects340) == 0:
                                    pass
                                    # State 78326
                                    if len(subjects66) >= 1 and subjects66[0] == Integer(-1):
                                        tmp358 = subjects66.popleft()
                                        # State 78327
                                        if len(subjects66) == 0:
                                            pass
                                            # State 78328
                                            if len(subjects) == 0:
                                                pass
                                                # 50: 1/tan(e + x*f)
                                                yield 50, subst2
                                        subjects66.appendleft(tmp358)
                        subjects340.appendleft(tmp355)
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.1.3.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 78732
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.3.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 78733
                        if len(subjects340) >= 1:
                            tmp361 = subjects340.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.3.1.0', tmp361)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 78734
                                if len(subjects340) == 0:
                                    pass
                                    # State 78735
                                    if len(subjects66) >= 1 and subjects66[0] == Integer(-1):
                                        tmp363 = subjects66.popleft()
                                        # State 78736
                                        if len(subjects66) == 0:
                                            pass
                                            # State 78737
                                            if len(subjects) == 0:
                                                pass
                                                # 52: 1/tan(e + x*f)
                                                yield 52, subst3
                                        subjects66.appendleft(tmp363)
                            subjects340.appendleft(tmp361)
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.3.1.0', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 88795
                        if len(subjects340) >= 1 and isinstance(subjects340[0], Pow):
                            tmp365 = subjects340.popleft()
                            subjects366 = deque(tmp365._args)
                            # State 88796
                            if len(subjects366) >= 1:
                                tmp367 = subjects366.popleft()
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i2.2.0_1', tmp367)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 88797
                                    if len(subjects366) >= 1:
                                        tmp369 = subjects366.popleft()
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.2.1.3.1.2', tmp369)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 88798
                                            if len(subjects366) == 0:
                                                pass
                                                # State 88799
                                                if len(subjects340) == 0:
                                                    pass
                                                    # State 88800
                                                    if len(subjects66) >= 1 and subjects66[0] == Integer(-1):
                                                        tmp371 = subjects66.popleft()
                                                        # State 88801
                                                        if len(subjects66) == 0:
                                                            pass
                                                            # State 88802
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 59: 1/tan(x**n*d + c)
                                                                yield 59, subst4
                                                        subjects66.appendleft(tmp371)
                                        subjects366.appendleft(tmp369)
                                subjects366.appendleft(tmp367)
                            subjects340.appendleft(tmp365)
                    if len(subjects340) >= 1 and isinstance(subjects340[0], Mul):
                        tmp372 = subjects340.popleft()
                        associative1 = tmp372
                        associative_type1 = type(tmp372)
                        subjects373 = deque(tmp372._args)
                        matcher = CommutativeMatcher78739.get()
                        tmp374 = subjects373
                        subjects373 = []
                        for s in tmp374:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp374, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 78740
                                if len(subjects340) == 0:
                                    pass
                                    # State 78741
                                    if len(subjects66) >= 1 and subjects66[0] == Integer(-1):
                                        tmp375 = subjects66.popleft()
                                        # State 78742
                                        if len(subjects66) == 0:
                                            pass
                                            # State 78743
                                            if len(subjects) == 0:
                                                pass
                                                # 52: 1/tan(e + x*f)
                                                yield 52, subst2
                                        subjects66.appendleft(tmp375)
                            if pattern_index == 1:
                                pass
                                # State 88807
                                if len(subjects340) == 0:
                                    pass
                                    # State 88808
                                    if len(subjects66) >= 1 and subjects66[0] == Integer(-1):
                                        tmp376 = subjects66.popleft()
                                        # State 88809
                                        if len(subjects66) == 0:
                                            pass
                                            # State 88810
                                            if len(subjects) == 0:
                                                pass
                                                # 59: 1/tan(x**n*d + c)
                                                yield 59, subst2
                                        subjects66.appendleft(tmp376)
                        subjects340.appendleft(tmp372)
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.2.3.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 80346
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.2.3.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 80347
                        if len(subjects340) >= 1:
                            tmp379 = subjects340.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.2.3.1.0', tmp379)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 80348
                                if len(subjects340) == 0:
                                    pass
                                    # State 80349
                                    if len(subjects66) >= 1 and subjects66[0] == Integer(-1):
                                        tmp381 = subjects66.popleft()
                                        # State 80350
                                        if len(subjects66) == 0:
                                            pass
                                            # State 80351
                                            if len(subjects) == 0:
                                                pass
                                                # 54: 1/tan(e + x*f)
                                                yield 54, subst3
                                        subjects66.appendleft(tmp381)
                            subjects340.appendleft(tmp379)
                    if len(subjects340) >= 1 and isinstance(subjects340[0], Mul):
                        tmp382 = subjects340.popleft()
                        associative1 = tmp382
                        associative_type1 = type(tmp382)
                        subjects383 = deque(tmp382._args)
                        matcher = CommutativeMatcher80353.get()
                        tmp384 = subjects383
                        subjects383 = []
                        for s in tmp384:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp384, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 80354
                                if len(subjects340) == 0:
                                    pass
                                    # State 80355
                                    if len(subjects66) >= 1 and subjects66[0] == Integer(-1):
                                        tmp385 = subjects66.popleft()
                                        # State 80356
                                        if len(subjects66) == 0:
                                            pass
                                            # State 80357
                                            if len(subjects) == 0:
                                                pass
                                                # 54: 1/tan(e + x*f)
                                                yield 54, subst2
                                        subjects66.appendleft(tmp385)
                        subjects340.appendleft(tmp382)
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.4.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 80794
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.4.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 80795
                        if len(subjects340) >= 1:
                            tmp388 = subjects340.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.4.1.0', tmp388)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 80796
                                if len(subjects340) == 0:
                                    pass
                                    # State 80797
                                    if len(subjects66) >= 1 and subjects66[0] == Integer(-1):
                                        tmp390 = subjects66.popleft()
                                        # State 80798
                                        if len(subjects66) == 0:
                                            pass
                                            # State 80799
                                            if len(subjects) == 0:
                                                pass
                                                # 55: 1/tan(e + x*f)
                                                yield 55, subst3
                                        subjects66.appendleft(tmp390)
                            subjects340.appendleft(tmp388)
                    if len(subjects340) >= 1 and isinstance(subjects340[0], Mul):
                        tmp391 = subjects340.popleft()
                        associative1 = tmp391
                        associative_type1 = type(tmp391)
                        subjects392 = deque(tmp391._args)
                        matcher = CommutativeMatcher80801.get()
                        tmp393 = subjects392
                        subjects392 = []
                        for s in tmp393:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp393, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 80802
                                if len(subjects340) == 0:
                                    pass
                                    # State 80803
                                    if len(subjects66) >= 1 and subjects66[0] == Integer(-1):
                                        tmp394 = subjects66.popleft()
                                        # State 80804
                                        if len(subjects66) == 0:
                                            pass
                                            # State 80805
                                            if len(subjects) == 0:
                                                pass
                                                # 55: 1/tan(e + x*f)
                                                yield 55, subst2
                                        subjects66.appendleft(tmp394)
                        subjects340.appendleft(tmp391)
                if len(subjects340) >= 1:
                    tmp395 = subjects340.popleft()
                    subst1 = Substitution(subst0)
                    try:
                        subst1.try_add_variable('i2.2.1.2', tmp395)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 89006
                        if len(subjects340) == 0:
                            pass
                            # State 89007
                            if len(subjects66) >= 1 and subjects66[0] == Integer(-1):
                                tmp397 = subjects66.popleft()
                                # State 89008
                                if len(subjects66) == 0:
                                    pass
                                    # State 89009
                                    if len(subjects) == 0:
                                        pass
                                        # 61: 1/tan(v)
                                        yield 61, subst1
                                subjects66.appendleft(tmp397)
                    subjects340.appendleft(tmp395)
                if len(subjects340) >= 1 and isinstance(subjects340[0], Add):
                    tmp398 = subjects340.popleft()
                    associative1 = tmp398
                    associative_type1 = type(tmp398)
                    subjects399 = deque(tmp398._args)
                    matcher = CommutativeMatcher78078.get()
                    tmp400 = subjects399
                    subjects399 = []
                    for s in tmp400:
                        matcher.add_subject(s)
                    for pattern_index, subst1 in matcher.match(tmp400, subst0):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 78084
                            if len(subjects340) == 0:
                                pass
                                # State 78085
                                if len(subjects66) >= 1 and subjects66[0] == Integer(-1):
                                    tmp401 = subjects66.popleft()
                                    # State 78086
                                    if len(subjects66) == 0:
                                        pass
                                        # State 78087
                                        if len(subjects) == 0:
                                            pass
                                            # 48: 1/tan(e + x*f)
                                            yield 48, subst1
                                    subjects66.appendleft(tmp401)
                        if pattern_index == 1:
                            pass
                            # State 78332
                            if len(subjects340) == 0:
                                pass
                                # State 78333
                                if len(subjects66) >= 1 and subjects66[0] == Integer(-1):
                                    tmp402 = subjects66.popleft()
                                    # State 78334
                                    if len(subjects66) == 0:
                                        pass
                                        # State 78335
                                        if len(subjects) == 0:
                                            pass
                                            # 50: 1/tan(e + x*f)
                                            yield 50, subst1
                                    subjects66.appendleft(tmp402)
                        if pattern_index == 2:
                            pass
                            # State 78747
                            if len(subjects340) == 0:
                                pass
                                # State 78748
                                if len(subjects66) >= 1 and subjects66[0] == Integer(-1):
                                    tmp403 = subjects66.popleft()
                                    # State 78749
                                    if len(subjects66) == 0:
                                        pass
                                        # State 78750
                                        if len(subjects) == 0:
                                            pass
                                            # 52: 1/tan(e + x*f)
                                            yield 52, subst1
                                    subjects66.appendleft(tmp403)
                        if pattern_index == 3:
                            pass
                            # State 80361
                            if len(subjects340) == 0:
                                pass
                                # State 80362
                                if len(subjects66) >= 1 and subjects66[0] == Integer(-1):
                                    tmp404 = subjects66.popleft()
                                    # State 80363
                                    if len(subjects66) == 0:
                                        pass
                                        # State 80364
                                        if len(subjects) == 0:
                                            pass
                                            # 54: 1/tan(e + x*f)
                                            yield 54, subst1
                                    subjects66.appendleft(tmp404)
                        if pattern_index == 4:
                            pass
                            # State 80809
                            if len(subjects340) == 0:
                                pass
                                # State 80810
                                if len(subjects66) >= 1 and subjects66[0] == Integer(-1):
                                    tmp405 = subjects66.popleft()
                                    # State 80811
                                    if len(subjects66) == 0:
                                        pass
                                        # State 80812
                                        if len(subjects) == 0:
                                            pass
                                            # 55: 1/tan(e + x*f)
                                            yield 55, subst1
                                    subjects66.appendleft(tmp405)
                        if pattern_index == 5:
                            pass
                            # State 88821
                            if len(subjects340) == 0:
                                pass
                                # State 88822
                                if len(subjects66) >= 1 and subjects66[0] == Integer(-1):
                                    tmp406 = subjects66.popleft()
                                    # State 88823
                                    if len(subjects66) == 0:
                                        pass
                                        # State 88824
                                        if len(subjects) == 0:
                                            pass
                                            # 59: 1/tan(x**n*d + c)
                                            yield 59, subst1
                                    subjects66.appendleft(tmp406)
                    subjects340.appendleft(tmp398)
                subjects66.appendleft(tmp339)
            if len(subjects66) >= 1 and isinstance(subjects66[0], tanh):
                tmp407 = subjects66.popleft()
                subjects408 = deque(tmp407._args)
                # State 128338
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.1.3.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 128339
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.3.1.0', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 128340
                        if len(subjects408) >= 1 and isinstance(subjects408[0], Pow):
                            tmp411 = subjects408.popleft()
                            subjects412 = deque(tmp411._args)
                            # State 128341
                            if len(subjects412) >= 1:
                                tmp413 = subjects412.popleft()
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i2.2.0_1', tmp413)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 128342
                                    if len(subjects412) >= 1:
                                        tmp415 = subjects412.popleft()
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.2.1.3.1.2', tmp415)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 128343
                                            if len(subjects412) == 0:
                                                pass
                                                # State 128344
                                                if len(subjects408) == 0:
                                                    pass
                                                    # State 128345
                                                    if len(subjects66) >= 1 and subjects66[0] == Integer(-1):
                                                        tmp417 = subjects66.popleft()
                                                        # State 128346
                                                        if len(subjects66) == 0:
                                                            pass
                                                            # State 128347
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 95: 1/tanh(x**n*d + c)
                                                                yield 95, subst4
                                                        subjects66.appendleft(tmp417)
                                        subjects412.appendleft(tmp415)
                                subjects412.appendleft(tmp413)
                            subjects408.appendleft(tmp411)
                    if len(subjects408) >= 1 and isinstance(subjects408[0], Mul):
                        tmp418 = subjects408.popleft()
                        associative1 = tmp418
                        associative_type1 = type(tmp418)
                        subjects419 = deque(tmp418._args)
                        matcher = CommutativeMatcher128349.get()
                        tmp420 = subjects419
                        subjects419 = []
                        for s in tmp420:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp420, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 128354
                                if len(subjects408) == 0:
                                    pass
                                    # State 128355
                                    if len(subjects66) >= 1 and subjects66[0] == Integer(-1):
                                        tmp421 = subjects66.popleft()
                                        # State 128356
                                        if len(subjects66) == 0:
                                            pass
                                            # State 128357
                                            if len(subjects) == 0:
                                                pass
                                                # 95: 1/tanh(x**n*d + c)
                                                yield 95, subst2
                                        subjects66.appendleft(tmp421)
                        subjects408.appendleft(tmp418)
                if len(subjects408) >= 1:
                    tmp422 = subjects408.popleft()
                    subst1 = Substitution(subst0)
                    try:
                        subst1.try_add_variable('i2.2.1.2', tmp422)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 128557
                        if len(subjects408) == 0:
                            pass
                            # State 128558
                            if len(subjects66) >= 1 and subjects66[0] == Integer(-1):
                                tmp424 = subjects66.popleft()
                                # State 128559
                                if len(subjects66) == 0:
                                    pass
                                    # State 128560
                                    if len(subjects) == 0:
                                        pass
                                        # 97: 1/tanh(v)
                                        yield 97, subst1
                                subjects66.appendleft(tmp424)
                    subjects408.appendleft(tmp422)
                if len(subjects408) >= 1 and isinstance(subjects408[0], Add):
                    tmp425 = subjects408.popleft()
                    associative1 = tmp425
                    associative_type1 = type(tmp425)
                    subjects426 = deque(tmp425._args)
                    matcher = CommutativeMatcher128359.get()
                    tmp427 = subjects426
                    subjects426 = []
                    for s in tmp427:
                        matcher.add_subject(s)
                    for pattern_index, subst1 in matcher.match(tmp427, subst0):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 128372
                            if len(subjects408) == 0:
                                pass
                                # State 128373
                                if len(subjects66) >= 1 and subjects66[0] == Integer(-1):
                                    tmp428 = subjects66.popleft()
                                    # State 128374
                                    if len(subjects66) == 0:
                                        pass
                                        # State 128375
                                        if len(subjects) == 0:
                                            pass
                                            # 95: 1/tanh(x**n*d + c)
                                            yield 95, subst1
                                    subjects66.appendleft(tmp428)
                    subjects408.appendleft(tmp425)
                subjects66.appendleft(tmp407)
            if len(subjects66) >= 1 and isinstance(subjects66[0], cosh):
                tmp429 = subjects66.popleft()
                subjects430 = deque(tmp429._args)
                # State 131282
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.1.3.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 131283
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.3.1.0', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 131284
                        if len(subjects430) >= 1 and isinstance(subjects430[0], Pow):
                            tmp433 = subjects430.popleft()
                            subjects434 = deque(tmp433._args)
                            # State 131285
                            if len(subjects434) >= 1:
                                tmp435 = subjects434.popleft()
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i2.2.0_1', tmp435)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 131286
                                    if len(subjects434) >= 1:
                                        tmp437 = subjects434.popleft()
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.2.1.3.1.2', tmp437)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 131287
                                            if len(subjects434) == 0:
                                                pass
                                                # State 131288
                                                if len(subjects430) == 0:
                                                    pass
                                                    # State 131289
                                                    if len(subjects66) >= 1 and subjects66[0] == Integer(-1):
                                                        tmp439 = subjects66.popleft()
                                                        # State 131290
                                                        if len(subjects66) == 0:
                                                            pass
                                                            # State 131291
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 98: 1/cosh(x**n*d + c)
                                                                yield 98, subst4
                                                        subjects66.appendleft(tmp439)
                                        subjects434.appendleft(tmp437)
                                subjects434.appendleft(tmp435)
                            subjects430.appendleft(tmp433)
                    if len(subjects430) >= 1 and isinstance(subjects430[0], Mul):
                        tmp440 = subjects430.popleft()
                        associative1 = tmp440
                        associative_type1 = type(tmp440)
                        subjects441 = deque(tmp440._args)
                        matcher = CommutativeMatcher131293.get()
                        tmp442 = subjects441
                        subjects441 = []
                        for s in tmp442:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp442, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 131298
                                if len(subjects430) == 0:
                                    pass
                                    # State 131299
                                    if len(subjects66) >= 1 and subjects66[0] == Integer(-1):
                                        tmp443 = subjects66.popleft()
                                        # State 131300
                                        if len(subjects66) == 0:
                                            pass
                                            # State 131301
                                            if len(subjects) == 0:
                                                pass
                                                # 98: 1/cosh(x**n*d + c)
                                                yield 98, subst2
                                        subjects66.appendleft(tmp443)
                        subjects430.appendleft(tmp440)
                if len(subjects430) >= 1:
                    tmp444 = subjects430.popleft()
                    subst1 = Substitution(subst0)
                    try:
                        subst1.try_add_variable('i2.2.1.2', tmp444)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 131770
                        if len(subjects430) == 0:
                            pass
                            # State 131771
                            if len(subjects66) >= 1 and subjects66[0] == Integer(-1):
                                tmp446 = subjects66.popleft()
                                # State 131772
                                if len(subjects66) == 0:
                                    pass
                                    # State 131773
                                    if len(subjects) == 0:
                                        pass
                                        # 100: 1/cosh(u)
                                        yield 100, subst1
                                subjects66.appendleft(tmp446)
                    subjects430.appendleft(tmp444)
                if len(subjects430) >= 1 and isinstance(subjects430[0], Add):
                    tmp447 = subjects430.popleft()
                    associative1 = tmp447
                    associative_type1 = type(tmp447)
                    subjects448 = deque(tmp447._args)
                    matcher = CommutativeMatcher131303.get()
                    tmp449 = subjects448
                    subjects448 = []
                    for s in tmp449:
                        matcher.add_subject(s)
                    for pattern_index, subst1 in matcher.match(tmp449, subst0):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 131316
                            if len(subjects430) == 0:
                                pass
                                # State 131317
                                if len(subjects66) >= 1 and subjects66[0] == Integer(-1):
                                    tmp450 = subjects66.popleft()
                                    # State 131318
                                    if len(subjects66) == 0:
                                        pass
                                        # State 131319
                                        if len(subjects) == 0:
                                            pass
                                            # 98: 1/cosh(x**n*d + c)
                                            yield 98, subst1
                                    subjects66.appendleft(tmp450)
                    subjects430.appendleft(tmp447)
                subjects66.appendleft(tmp429)
            if len(subjects66) >= 1 and isinstance(subjects66[0], sinh):
                tmp451 = subjects66.popleft()
                subjects452 = deque(tmp451._args)
                # State 131577
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.1.3.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 131578
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.3.1.0', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 131579
                        if len(subjects452) >= 1 and isinstance(subjects452[0], Pow):
                            tmp455 = subjects452.popleft()
                            subjects456 = deque(tmp455._args)
                            # State 131580
                            if len(subjects456) >= 1:
                                tmp457 = subjects456.popleft()
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i2.2.0_1', tmp457)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 131581
                                    if len(subjects456) >= 1:
                                        tmp459 = subjects456.popleft()
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.2.1.3.1.2', tmp459)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 131582
                                            if len(subjects456) == 0:
                                                pass
                                                # State 131583
                                                if len(subjects452) == 0:
                                                    pass
                                                    # State 131584
                                                    if len(subjects66) >= 1 and subjects66[0] == Integer(-1):
                                                        tmp461 = subjects66.popleft()
                                                        # State 131585
                                                        if len(subjects66) == 0:
                                                            pass
                                                            # State 131586
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 99: 1/sinh(x**n*d + c)
                                                                yield 99, subst4
                                                        subjects66.appendleft(tmp461)
                                        subjects456.appendleft(tmp459)
                                subjects456.appendleft(tmp457)
                            subjects452.appendleft(tmp455)
                    if len(subjects452) >= 1 and isinstance(subjects452[0], Mul):
                        tmp462 = subjects452.popleft()
                        associative1 = tmp462
                        associative_type1 = type(tmp462)
                        subjects463 = deque(tmp462._args)
                        matcher = CommutativeMatcher131588.get()
                        tmp464 = subjects463
                        subjects463 = []
                        for s in tmp464:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp464, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 131593
                                if len(subjects452) == 0:
                                    pass
                                    # State 131594
                                    if len(subjects66) >= 1 and subjects66[0] == Integer(-1):
                                        tmp465 = subjects66.popleft()
                                        # State 131595
                                        if len(subjects66) == 0:
                                            pass
                                            # State 131596
                                            if len(subjects) == 0:
                                                pass
                                                # 99: 1/sinh(x**n*d + c)
                                                yield 99, subst2
                                        subjects66.appendleft(tmp465)
                        subjects452.appendleft(tmp462)
                if len(subjects452) >= 1:
                    tmp466 = subjects452.popleft()
                    subst1 = Substitution(subst0)
                    try:
                        subst1.try_add_variable('i2.2.1.2', tmp466)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 131817
                        if len(subjects452) == 0:
                            pass
                            # State 131818
                            if len(subjects66) >= 1 and subjects66[0] == Integer(-1):
                                tmp468 = subjects66.popleft()
                                # State 131819
                                if len(subjects66) == 0:
                                    pass
                                    # State 131820
                                    if len(subjects) == 0:
                                        pass
                                        # 101: 1/sinh(u)
                                        yield 101, subst1
                                subjects66.appendleft(tmp468)
                    subjects452.appendleft(tmp466)
                if len(subjects452) >= 1 and isinstance(subjects452[0], Add):
                    tmp469 = subjects452.popleft()
                    associative1 = tmp469
                    associative_type1 = type(tmp469)
                    subjects470 = deque(tmp469._args)
                    matcher = CommutativeMatcher131598.get()
                    tmp471 = subjects470
                    subjects470 = []
                    for s in tmp471:
                        matcher.add_subject(s)
                    for pattern_index, subst1 in matcher.match(tmp471, subst0):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 131611
                            if len(subjects452) == 0:
                                pass
                                # State 131612
                                if len(subjects66) >= 1 and subjects66[0] == Integer(-1):
                                    tmp472 = subjects66.popleft()
                                    # State 131613
                                    if len(subjects66) == 0:
                                        pass
                                        # State 131614
                                        if len(subjects) == 0:
                                            pass
                                            # 99: 1/sinh(x**n*d + c)
                                            yield 99, subst1
                                    subjects66.appendleft(tmp472)
                    subjects452.appendleft(tmp469)
                subjects66.appendleft(tmp451)
            subjects.appendleft(tmp65)
        if len(subjects) >= 1 and isinstance(subjects[0], log):
            tmp473 = subjects.popleft()
            subjects474 = deque(tmp473._args)
            # State 37699
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.0', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 37700
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.2', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 37701
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.2.1.2.2.0', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 37702
                        subst4 = Substitution(subst3)
                        try:
                            subst4.try_add_variable('i2.2.1.2.2.2', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 37703
                            subst5 = Substitution(subst4)
                            try:
                                subst5.try_add_variable('i2.2.1.2.2.2.0', S(0))
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 37704
                                subst6 = Substitution(subst5)
                                try:
                                    subst6.try_add_variable('i2.2.1.2.2.2.1.0', S(1))
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 37705
                                    if len(subjects474) >= 1 and isinstance(subjects474[0], Pow):
                                        tmp481 = subjects474.popleft()
                                        subjects482 = deque(tmp481._args)
                                        # State 37706
                                        if len(subjects482) >= 1:
                                            tmp483 = subjects482.popleft()
                                            subst7 = Substitution(subst6)
                                            try:
                                                subst7.try_add_variable('i2.2.1.1', tmp483)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 37707
                                                if len(subjects482) >= 1:
                                                    tmp485 = subjects482.popleft()
                                                    subst8 = Substitution(subst7)
                                                    try:
                                                        subst8.try_add_variable('i2.2.1.2', tmp485)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 37708
                                                        if len(subjects482) == 0:
                                                            pass
                                                            # State 37709
                                                            if len(subjects474) == 0:
                                                                pass
                                                                # State 37710
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 23: log(c*(d*(x**j*f + e)**p)**q)
                                                                    yield 23, subst8
                                                    subjects482.appendleft(tmp485)
                                            subjects482.appendleft(tmp483)
                                        subjects474.appendleft(tmp481)
                                if len(subjects474) >= 1 and isinstance(subjects474[0], Mul):
                                    tmp487 = subjects474.popleft()
                                    associative1 = tmp487
                                    associative_type1 = type(tmp487)
                                    subjects488 = deque(tmp487._args)
                                    matcher = CommutativeMatcher37712.get()
                                    tmp489 = subjects488
                                    subjects488 = []
                                    for s in tmp489:
                                        matcher.add_subject(s)
                                    for pattern_index, subst6 in matcher.match(tmp489, subst5):
                                        pass
                                        if pattern_index == 0:
                                            pass
                                            # State 37717
                                            if len(subjects474) == 0:
                                                pass
                                                # State 37718
                                                if len(subjects) == 0:
                                                    pass
                                                    # 23: log(c*(d*(x**j*f + e)**p)**q)
                                                    yield 23, subst6
                                    subjects474.appendleft(tmp487)
                            if len(subjects474) >= 1 and isinstance(subjects474[0], Add):
                                tmp490 = subjects474.popleft()
                                associative1 = tmp490
                                associative_type1 = type(tmp490)
                                subjects491 = deque(tmp490._args)
                                matcher = CommutativeMatcher37720.get()
                                tmp492 = subjects491
                                subjects491 = []
                                for s in tmp492:
                                    matcher.add_subject(s)
                                for pattern_index, subst5 in matcher.match(tmp492, subst4):
                                    pass
                                    if pattern_index == 0:
                                        pass
                                        # State 37733
                                        if len(subjects474) == 0:
                                            pass
                                            # State 37734
                                            if len(subjects) == 0:
                                                pass
                                                # 23: log(c*(d*(x**j*f + e)**p)**q)
                                                yield 23, subst5
                                subjects474.appendleft(tmp490)
                        if len(subjects474) >= 1 and isinstance(subjects474[0], Pow):
                            tmp493 = subjects474.popleft()
                            subjects494 = deque(tmp493._args)
                            # State 37735
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i2.2.1.2.2.2.0', S(0))
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 37736
                                subst5 = Substitution(subst4)
                                try:
                                    subst5.try_add_variable('i2.2.1.2.2.2.1.0', S(1))
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 37737
                                    if len(subjects494) >= 1 and isinstance(subjects494[0], Pow):
                                        tmp497 = subjects494.popleft()
                                        subjects498 = deque(tmp497._args)
                                        # State 37738
                                        if len(subjects498) >= 1:
                                            tmp499 = subjects498.popleft()
                                            subst6 = Substitution(subst5)
                                            try:
                                                subst6.try_add_variable('i2.2.1.1', tmp499)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 37739
                                                if len(subjects498) >= 1:
                                                    tmp501 = subjects498.popleft()
                                                    subst7 = Substitution(subst6)
                                                    try:
                                                        subst7.try_add_variable('i2.2.1.2', tmp501)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 37740
                                                        if len(subjects498) == 0:
                                                            pass
                                                            # State 37741
                                                            subst8 = Substitution(subst7)
                                                            try:
                                                                subst8.try_add_variable('i2.2.1.2.2.2', 1)
                                                            except ValueError:
                                                                pass
                                                            else:
                                                                pass
                                                                # State 37742
                                                                if len(subjects494) == 0:
                                                                    pass
                                                                    # State 37743
                                                                    if len(subjects474) == 0:
                                                                        pass
                                                                        # State 37744
                                                                        if len(subjects) == 0:
                                                                            pass
                                                                            # 23: log(c*(d*(x**j*f + e)**p)**q)
                                                                            yield 23, subst8
                                                            if len(subjects494) >= 1:
                                                                tmp504 = subjects494.popleft()
                                                                subst8 = Substitution(subst7)
                                                                try:
                                                                    subst8.try_add_variable('i2.2.1.2.2.2', tmp504)
                                                                except ValueError:
                                                                    pass
                                                                else:
                                                                    pass
                                                                    # State 37742
                                                                    if len(subjects494) == 0:
                                                                        pass
                                                                        # State 37743
                                                                        if len(subjects474) == 0:
                                                                            pass
                                                                            # State 37744
                                                                            if len(subjects) == 0:
                                                                                pass
                                                                                # 23: log(c*(d*(x**j*f + e)**p)**q)
                                                                                yield 23, subst8
                                                                subjects494.appendleft(tmp504)
                                                    subjects498.appendleft(tmp501)
                                            subjects498.appendleft(tmp499)
                                        subjects494.appendleft(tmp497)
                                if len(subjects494) >= 1 and isinstance(subjects494[0], Mul):
                                    tmp506 = subjects494.popleft()
                                    associative1 = tmp506
                                    associative_type1 = type(tmp506)
                                    subjects507 = deque(tmp506._args)
                                    matcher = CommutativeMatcher37746.get()
                                    tmp508 = subjects507
                                    subjects507 = []
                                    for s in tmp508:
                                        matcher.add_subject(s)
                                    for pattern_index, subst5 in matcher.match(tmp508, subst4):
                                        pass
                                        if pattern_index == 0:
                                            pass
                                            # State 37751
                                            subst6 = Substitution(subst5)
                                            try:
                                                subst6.try_add_variable('i2.2.1.2.2.2', 1)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 37752
                                                if len(subjects494) == 0:
                                                    pass
                                                    # State 37753
                                                    if len(subjects474) == 0:
                                                        pass
                                                        # State 37754
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 23: log(c*(d*(x**j*f + e)**p)**q)
                                                            yield 23, subst6
                                            if len(subjects494) >= 1:
                                                tmp510 = []
                                                tmp510.append(subjects494.popleft())
                                                while True:
                                                    if len(tmp510) > 1:
                                                        tmp511 = create_operation_expression(associative1, tmp510)
                                                    elif len(tmp510) == 1:
                                                        tmp511 = tmp510[0]
                                                    else:
                                                        assert False, "Unreachable"
                                                    subst6 = Substitution(subst5)
                                                    try:
                                                        subst6.try_add_variable('i2.2.1.2.2.2', tmp511)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 37752
                                                        if len(subjects494) == 0:
                                                            pass
                                                            # State 37753
                                                            if len(subjects474) == 0:
                                                                pass
                                                                # State 37754
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 23: log(c*(d*(x**j*f + e)**p)**q)
                                                                    yield 23, subst6
                                                    if len(subjects494) == 0:
                                                        break
                                                    tmp510.append(subjects494.popleft())
                                                subjects494.extendleft(reversed(tmp510))
                                    subjects494.appendleft(tmp506)
                            if len(subjects494) >= 1 and isinstance(subjects494[0], Add):
                                tmp513 = subjects494.popleft()
                                associative1 = tmp513
                                associative_type1 = type(tmp513)
                                subjects514 = deque(tmp513._args)
                                matcher = CommutativeMatcher37756.get()
                                tmp515 = subjects514
                                subjects514 = []
                                for s in tmp515:
                                    matcher.add_subject(s)
                                for pattern_index, subst4 in matcher.match(tmp515, subst3):
                                    pass
                                    if pattern_index == 0:
                                        pass
                                        # State 37769
                                        subst5 = Substitution(subst4)
                                        try:
                                            subst5.try_add_variable('i2.2.1.2.2.2', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 37770
                                            if len(subjects494) == 0:
                                                pass
                                                # State 37771
                                                if len(subjects474) == 0:
                                                    pass
                                                    # State 37772
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 23: log(c*(d*(x**j*f + e)**p)**q)
                                                        yield 23, subst5
                                        if len(subjects494) >= 1:
                                            tmp517 = []
                                            tmp517.append(subjects494.popleft())
                                            while True:
                                                if len(tmp517) > 1:
                                                    tmp518 = create_operation_expression(associative1, tmp517)
                                                elif len(tmp517) == 1:
                                                    tmp518 = tmp517[0]
                                                else:
                                                    assert False, "Unreachable"
                                                subst5 = Substitution(subst4)
                                                try:
                                                    subst5.try_add_variable('i2.2.1.2.2.2', tmp518)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 37770
                                                    if len(subjects494) == 0:
                                                        pass
                                                        # State 37771
                                                        if len(subjects474) == 0:
                                                            pass
                                                            # State 37772
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 23: log(c*(d*(x**j*f + e)**p)**q)
                                                                yield 23, subst5
                                                if len(subjects494) == 0:
                                                    break
                                                tmp517.append(subjects494.popleft())
                                            subjects494.extendleft(reversed(tmp517))
                                subjects494.appendleft(tmp513)
                            subjects474.appendleft(tmp493)
                    if len(subjects474) >= 1 and isinstance(subjects474[0], Mul):
                        tmp520 = subjects474.popleft()
                        associative1 = tmp520
                        associative_type1 = type(tmp520)
                        subjects521 = deque(tmp520._args)
                        matcher = CommutativeMatcher37774.get()
                        tmp522 = subjects521
                        subjects521 = []
                        for s in tmp522:
                            matcher.add_subject(s)
                        for pattern_index, subst3 in matcher.match(tmp522, subst2):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 37839
                                if len(subjects474) == 0:
                                    pass
                                    # State 37840
                                    if len(subjects) == 0:
                                        pass
                                        # 23: log(c*(d*(x**j*f + e)**p)**q)
                                        yield 23, subst3
                        subjects474.appendleft(tmp520)
                if len(subjects474) >= 1 and isinstance(subjects474[0], Pow):
                    tmp523 = subjects474.popleft()
                    subjects524 = deque(tmp523._args)
                    # State 37841
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.2.2.0', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 37842
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.2.2.2', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 37843
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i2.2.1.2.2.2.0', S(0))
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 37844
                                subst5 = Substitution(subst4)
                                try:
                                    subst5.try_add_variable('i2.2.1.2.2.2.1.0', S(1))
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 37845
                                    if len(subjects524) >= 1 and isinstance(subjects524[0], Pow):
                                        tmp529 = subjects524.popleft()
                                        subjects530 = deque(tmp529._args)
                                        # State 37846
                                        if len(subjects530) >= 1:
                                            tmp531 = subjects530.popleft()
                                            subst6 = Substitution(subst5)
                                            try:
                                                subst6.try_add_variable('i2.2.1.1', tmp531)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 37847
                                                if len(subjects530) >= 1:
                                                    tmp533 = subjects530.popleft()
                                                    subst7 = Substitution(subst6)
                                                    try:
                                                        subst7.try_add_variable('i2.2.1.2', tmp533)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 37848
                                                        if len(subjects530) == 0:
                                                            pass
                                                            # State 37849
                                                            subst8 = Substitution(subst7)
                                                            try:
                                                                subst8.try_add_variable('i2.2.1.2.2', 1)
                                                            except ValueError:
                                                                pass
                                                            else:
                                                                pass
                                                                # State 37850
                                                                if len(subjects524) == 0:
                                                                    pass
                                                                    # State 37851
                                                                    if len(subjects474) == 0:
                                                                        pass
                                                                        # State 37852
                                                                        if len(subjects) == 0:
                                                                            pass
                                                                            # 23: log(c*(d*(x**j*f + e)**p)**q)
                                                                            yield 23, subst8
                                                            if len(subjects524) >= 1:
                                                                tmp536 = subjects524.popleft()
                                                                subst8 = Substitution(subst7)
                                                                try:
                                                                    subst8.try_add_variable('i2.2.1.2.2', tmp536)
                                                                except ValueError:
                                                                    pass
                                                                else:
                                                                    pass
                                                                    # State 37850
                                                                    if len(subjects524) == 0:
                                                                        pass
                                                                        # State 37851
                                                                        if len(subjects474) == 0:
                                                                            pass
                                                                            # State 37852
                                                                            if len(subjects) == 0:
                                                                                pass
                                                                                # 23: log(c*(d*(x**j*f + e)**p)**q)
                                                                                yield 23, subst8
                                                                subjects524.appendleft(tmp536)
                                                    subjects530.appendleft(tmp533)
                                            subjects530.appendleft(tmp531)
                                        subjects524.appendleft(tmp529)
                                if len(subjects524) >= 1 and isinstance(subjects524[0], Mul):
                                    tmp538 = subjects524.popleft()
                                    associative1 = tmp538
                                    associative_type1 = type(tmp538)
                                    subjects539 = deque(tmp538._args)
                                    matcher = CommutativeMatcher37854.get()
                                    tmp540 = subjects539
                                    subjects539 = []
                                    for s in tmp540:
                                        matcher.add_subject(s)
                                    for pattern_index, subst5 in matcher.match(tmp540, subst4):
                                        pass
                                        if pattern_index == 0:
                                            pass
                                            # State 37859
                                            subst6 = Substitution(subst5)
                                            try:
                                                subst6.try_add_variable('i2.2.1.2.2', 1)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 37860
                                                if len(subjects524) == 0:
                                                    pass
                                                    # State 37861
                                                    if len(subjects474) == 0:
                                                        pass
                                                        # State 37862
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 23: log(c*(d*(x**j*f + e)**p)**q)
                                                            yield 23, subst6
                                            if len(subjects524) >= 1:
                                                tmp542 = []
                                                tmp542.append(subjects524.popleft())
                                                while True:
                                                    if len(tmp542) > 1:
                                                        tmp543 = create_operation_expression(associative1, tmp542)
                                                    elif len(tmp542) == 1:
                                                        tmp543 = tmp542[0]
                                                    else:
                                                        assert False, "Unreachable"
                                                    subst6 = Substitution(subst5)
                                                    try:
                                                        subst6.try_add_variable('i2.2.1.2.2', tmp543)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 37860
                                                        if len(subjects524) == 0:
                                                            pass
                                                            # State 37861
                                                            if len(subjects474) == 0:
                                                                pass
                                                                # State 37862
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 23: log(c*(d*(x**j*f + e)**p)**q)
                                                                    yield 23, subst6
                                                    if len(subjects524) == 0:
                                                        break
                                                    tmp542.append(subjects524.popleft())
                                                subjects524.extendleft(reversed(tmp542))
                                    subjects524.appendleft(tmp538)
                            if len(subjects524) >= 1 and isinstance(subjects524[0], Add):
                                tmp545 = subjects524.popleft()
                                associative1 = tmp545
                                associative_type1 = type(tmp545)
                                subjects546 = deque(tmp545._args)
                                matcher = CommutativeMatcher37864.get()
                                tmp547 = subjects546
                                subjects546 = []
                                for s in tmp547:
                                    matcher.add_subject(s)
                                for pattern_index, subst4 in matcher.match(tmp547, subst3):
                                    pass
                                    if pattern_index == 0:
                                        pass
                                        # State 37877
                                        subst5 = Substitution(subst4)
                                        try:
                                            subst5.try_add_variable('i2.2.1.2.2', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 37878
                                            if len(subjects524) == 0:
                                                pass
                                                # State 37879
                                                if len(subjects474) == 0:
                                                    pass
                                                    # State 37880
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 23: log(c*(d*(x**j*f + e)**p)**q)
                                                        yield 23, subst5
                                        if len(subjects524) >= 1:
                                            tmp549 = []
                                            tmp549.append(subjects524.popleft())
                                            while True:
                                                if len(tmp549) > 1:
                                                    tmp550 = create_operation_expression(associative1, tmp549)
                                                elif len(tmp549) == 1:
                                                    tmp550 = tmp549[0]
                                                else:
                                                    assert False, "Unreachable"
                                                subst5 = Substitution(subst4)
                                                try:
                                                    subst5.try_add_variable('i2.2.1.2.2', tmp550)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 37878
                                                    if len(subjects524) == 0:
                                                        pass
                                                        # State 37879
                                                        if len(subjects474) == 0:
                                                            pass
                                                            # State 37880
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 23: log(c*(d*(x**j*f + e)**p)**q)
                                                                yield 23, subst5
                                                if len(subjects524) == 0:
                                                    break
                                                tmp549.append(subjects524.popleft())
                                            subjects524.extendleft(reversed(tmp549))
                                subjects524.appendleft(tmp545)
                        if len(subjects524) >= 1 and isinstance(subjects524[0], Pow):
                            tmp552 = subjects524.popleft()
                            subjects553 = deque(tmp552._args)
                            # State 37881
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.2.2.2.0', S(0))
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 37882
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.2.1.2.2.2.1.0', S(1))
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 37883
                                    if len(subjects553) >= 1 and isinstance(subjects553[0], Pow):
                                        tmp556 = subjects553.popleft()
                                        subjects557 = deque(tmp556._args)
                                        # State 37884
                                        if len(subjects557) >= 1:
                                            tmp558 = subjects557.popleft()
                                            subst5 = Substitution(subst4)
                                            try:
                                                subst5.try_add_variable('i2.2.1.1', tmp558)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 37885
                                                if len(subjects557) >= 1:
                                                    tmp560 = subjects557.popleft()
                                                    subst6 = Substitution(subst5)
                                                    try:
                                                        subst6.try_add_variable('i2.2.1.2', tmp560)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 37886
                                                        if len(subjects557) == 0:
                                                            pass
                                                            # State 37887
                                                            subst7 = Substitution(subst6)
                                                            try:
                                                                subst7.try_add_variable('i2.2.1.2.2.2', 1)
                                                            except ValueError:
                                                                pass
                                                            else:
                                                                pass
                                                                # State 37888
                                                                if len(subjects553) == 0:
                                                                    pass
                                                                    # State 37889
                                                                    subst8 = Substitution(subst7)
                                                                    try:
                                                                        subst8.try_add_variable('i2.2.1.2.2', 1)
                                                                    except ValueError:
                                                                        pass
                                                                    else:
                                                                        pass
                                                                        # State 37890
                                                                        if len(subjects524) == 0:
                                                                            pass
                                                                            # State 37891
                                                                            if len(subjects474) == 0:
                                                                                pass
                                                                                # State 37892
                                                                                if len(subjects) == 0:
                                                                                    pass
                                                                                    # 23: log(c*(d*(x**j*f + e)**p)**q)
                                                                                    yield 23, subst8
                                                                    if len(subjects524) >= 1:
                                                                        tmp564 = subjects524.popleft()
                                                                        subst8 = Substitution(subst7)
                                                                        try:
                                                                            subst8.try_add_variable('i2.2.1.2.2', tmp564)
                                                                        except ValueError:
                                                                            pass
                                                                        else:
                                                                            pass
                                                                            # State 37890
                                                                            if len(subjects524) == 0:
                                                                                pass
                                                                                # State 37891
                                                                                if len(subjects474) == 0:
                                                                                    pass
                                                                                    # State 37892
                                                                                    if len(subjects) == 0:
                                                                                        pass
                                                                                        # 23: log(c*(d*(x**j*f + e)**p)**q)
                                                                                        yield 23, subst8
                                                                        subjects524.appendleft(tmp564)
                                                            if len(subjects553) >= 1:
                                                                tmp566 = subjects553.popleft()
                                                                subst7 = Substitution(subst6)
                                                                try:
                                                                    subst7.try_add_variable('i2.2.1.2.2.2', tmp566)
                                                                except ValueError:
                                                                    pass
                                                                else:
                                                                    pass
                                                                    # State 37888
                                                                    if len(subjects553) == 0:
                                                                        pass
                                                                        # State 37889
                                                                        subst8 = Substitution(subst7)
                                                                        try:
                                                                            subst8.try_add_variable('i2.2.1.2.2', 1)
                                                                        except ValueError:
                                                                            pass
                                                                        else:
                                                                            pass
                                                                            # State 37890
                                                                            if len(subjects524) == 0:
                                                                                pass
                                                                                # State 37891
                                                                                if len(subjects474) == 0:
                                                                                    pass
                                                                                    # State 37892
                                                                                    if len(subjects) == 0:
                                                                                        pass
                                                                                        # 23: log(c*(d*(x**j*f + e)**p)**q)
                                                                                        yield 23, subst8
                                                                        if len(subjects524) >= 1:
                                                                            tmp569 = subjects524.popleft()
                                                                            subst8 = Substitution(subst7)
                                                                            try:
                                                                                subst8.try_add_variable('i2.2.1.2.2', tmp569)
                                                                            except ValueError:
                                                                                pass
                                                                            else:
                                                                                pass
                                                                                # State 37890
                                                                                if len(subjects524) == 0:
                                                                                    pass
                                                                                    # State 37891
                                                                                    if len(subjects474) == 0:
                                                                                        pass
                                                                                        # State 37892
                                                                                        if len(subjects) == 0:
                                                                                            pass
                                                                                            # 23: log(c*(d*(x**j*f + e)**p)**q)
                                                                                            yield 23, subst8
                                                                            subjects524.appendleft(tmp569)
                                                                subjects553.appendleft(tmp566)
                                                    subjects557.appendleft(tmp560)
                                            subjects557.appendleft(tmp558)
                                        subjects553.appendleft(tmp556)
                                if len(subjects553) >= 1 and isinstance(subjects553[0], Mul):
                                    tmp571 = subjects553.popleft()
                                    associative1 = tmp571
                                    associative_type1 = type(tmp571)
                                    subjects572 = deque(tmp571._args)
                                    matcher = CommutativeMatcher37894.get()
                                    tmp573 = subjects572
                                    subjects572 = []
                                    for s in tmp573:
                                        matcher.add_subject(s)
                                    for pattern_index, subst4 in matcher.match(tmp573, subst3):
                                        pass
                                        if pattern_index == 0:
                                            pass
                                            # State 37899
                                            subst5 = Substitution(subst4)
                                            try:
                                                subst5.try_add_variable('i2.2.1.2.2.2', 1)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 37900
                                                if len(subjects553) == 0:
                                                    pass
                                                    # State 37901
                                                    subst6 = Substitution(subst5)
                                                    try:
                                                        subst6.try_add_variable('i2.2.1.2.2', 1)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 37902
                                                        if len(subjects524) == 0:
                                                            pass
                                                            # State 37903
                                                            if len(subjects474) == 0:
                                                                pass
                                                                # State 37904
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 23: log(c*(d*(x**j*f + e)**p)**q)
                                                                    yield 23, subst6
                                                    if len(subjects524) >= 1:
                                                        tmp576 = subjects524.popleft()
                                                        subst6 = Substitution(subst5)
                                                        try:
                                                            subst6.try_add_variable('i2.2.1.2.2', tmp576)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            # State 37902
                                                            if len(subjects524) == 0:
                                                                pass
                                                                # State 37903
                                                                if len(subjects474) == 0:
                                                                    pass
                                                                    # State 37904
                                                                    if len(subjects) == 0:
                                                                        pass
                                                                        # 23: log(c*(d*(x**j*f + e)**p)**q)
                                                                        yield 23, subst6
                                                        subjects524.appendleft(tmp576)
                                            if len(subjects553) >= 1:
                                                tmp578 = []
                                                tmp578.append(subjects553.popleft())
                                                while True:
                                                    if len(tmp578) > 1:
                                                        tmp579 = create_operation_expression(associative1, tmp578)
                                                    elif len(tmp578) == 1:
                                                        tmp579 = tmp578[0]
                                                    else:
                                                        assert False, "Unreachable"
                                                    subst5 = Substitution(subst4)
                                                    try:
                                                        subst5.try_add_variable('i2.2.1.2.2.2', tmp579)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 37900
                                                        if len(subjects553) == 0:
                                                            pass
                                                            # State 37901
                                                            subst6 = Substitution(subst5)
                                                            try:
                                                                subst6.try_add_variable('i2.2.1.2.2', 1)
                                                            except ValueError:
                                                                pass
                                                            else:
                                                                pass
                                                                # State 37902
                                                                if len(subjects524) == 0:
                                                                    pass
                                                                    # State 37903
                                                                    if len(subjects474) == 0:
                                                                        pass
                                                                        # State 37904
                                                                        if len(subjects) == 0:
                                                                            pass
                                                                            # 23: log(c*(d*(x**j*f + e)**p)**q)
                                                                            yield 23, subst6
                                                            if len(subjects524) >= 1:
                                                                tmp582 = subjects524.popleft()
                                                                subst6 = Substitution(subst5)
                                                                try:
                                                                    subst6.try_add_variable('i2.2.1.2.2', tmp582)
                                                                except ValueError:
                                                                    pass
                                                                else:
                                                                    pass
                                                                    # State 37902
                                                                    if len(subjects524) == 0:
                                                                        pass
                                                                        # State 37903
                                                                        if len(subjects474) == 0:
                                                                            pass
                                                                            # State 37904
                                                                            if len(subjects) == 0:
                                                                                pass
                                                                                # 23: log(c*(d*(x**j*f + e)**p)**q)
                                                                                yield 23, subst6
                                                                subjects524.appendleft(tmp582)
                                                    if len(subjects553) == 0:
                                                        break
                                                    tmp578.append(subjects553.popleft())
                                                subjects553.extendleft(reversed(tmp578))
                                    subjects553.appendleft(tmp571)
                            if len(subjects553) >= 1 and isinstance(subjects553[0], Add):
                                tmp584 = subjects553.popleft()
                                associative1 = tmp584
                                associative_type1 = type(tmp584)
                                subjects585 = deque(tmp584._args)
                                matcher = CommutativeMatcher37906.get()
                                tmp586 = subjects585
                                subjects585 = []
                                for s in tmp586:
                                    matcher.add_subject(s)
                                for pattern_index, subst3 in matcher.match(tmp586, subst2):
                                    pass
                                    if pattern_index == 0:
                                        pass
                                        # State 37919
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.2.1.2.2.2', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 37920
                                            if len(subjects553) == 0:
                                                pass
                                                # State 37921
                                                subst5 = Substitution(subst4)
                                                try:
                                                    subst5.try_add_variable('i2.2.1.2.2', 1)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 37922
                                                    if len(subjects524) == 0:
                                                        pass
                                                        # State 37923
                                                        if len(subjects474) == 0:
                                                            pass
                                                            # State 37924
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 23: log(c*(d*(x**j*f + e)**p)**q)
                                                                yield 23, subst5
                                                if len(subjects524) >= 1:
                                                    tmp589 = subjects524.popleft()
                                                    subst5 = Substitution(subst4)
                                                    try:
                                                        subst5.try_add_variable('i2.2.1.2.2', tmp589)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 37922
                                                        if len(subjects524) == 0:
                                                            pass
                                                            # State 37923
                                                            if len(subjects474) == 0:
                                                                pass
                                                                # State 37924
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 23: log(c*(d*(x**j*f + e)**p)**q)
                                                                    yield 23, subst5
                                                    subjects524.appendleft(tmp589)
                                        if len(subjects553) >= 1:
                                            tmp591 = []
                                            tmp591.append(subjects553.popleft())
                                            while True:
                                                if len(tmp591) > 1:
                                                    tmp592 = create_operation_expression(associative1, tmp591)
                                                elif len(tmp591) == 1:
                                                    tmp592 = tmp591[0]
                                                else:
                                                    assert False, "Unreachable"
                                                subst4 = Substitution(subst3)
                                                try:
                                                    subst4.try_add_variable('i2.2.1.2.2.2', tmp592)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 37920
                                                    if len(subjects553) == 0:
                                                        pass
                                                        # State 37921
                                                        subst5 = Substitution(subst4)
                                                        try:
                                                            subst5.try_add_variable('i2.2.1.2.2', 1)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            # State 37922
                                                            if len(subjects524) == 0:
                                                                pass
                                                                # State 37923
                                                                if len(subjects474) == 0:
                                                                    pass
                                                                    # State 37924
                                                                    if len(subjects) == 0:
                                                                        pass
                                                                        # 23: log(c*(d*(x**j*f + e)**p)**q)
                                                                        yield 23, subst5
                                                        if len(subjects524) >= 1:
                                                            tmp595 = subjects524.popleft()
                                                            subst5 = Substitution(subst4)
                                                            try:
                                                                subst5.try_add_variable('i2.2.1.2.2', tmp595)
                                                            except ValueError:
                                                                pass
                                                            else:
                                                                pass
                                                                # State 37922
                                                                if len(subjects524) == 0:
                                                                    pass
                                                                    # State 37923
                                                                    if len(subjects474) == 0:
                                                                        pass
                                                                        # State 37924
                                                                        if len(subjects) == 0:
                                                                            pass
                                                                            # 23: log(c*(d*(x**j*f + e)**p)**q)
                                                                            yield 23, subst5
                                                            subjects524.appendleft(tmp595)
                                                if len(subjects553) == 0:
                                                    break
                                                tmp591.append(subjects553.popleft())
                                            subjects553.extendleft(reversed(tmp591))
                                subjects553.appendleft(tmp584)
                            subjects524.appendleft(tmp552)
                    if len(subjects524) >= 1 and isinstance(subjects524[0], Mul):
                        tmp597 = subjects524.popleft()
                        associative1 = tmp597
                        associative_type1 = type(tmp597)
                        subjects598 = deque(tmp597._args)
                        matcher = CommutativeMatcher37926.get()
                        tmp599 = subjects598
                        subjects598 = []
                        for s in tmp599:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp599, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 37991
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i2.2.1.2.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 37992
                                    if len(subjects524) == 0:
                                        pass
                                        # State 37993
                                        if len(subjects474) == 0:
                                            pass
                                            # State 37994
                                            if len(subjects) == 0:
                                                pass
                                                # 23: log(c*(d*(x**j*f + e)**p)**q)
                                                yield 23, subst3
                                if len(subjects524) >= 1:
                                    tmp601 = []
                                    tmp601.append(subjects524.popleft())
                                    while True:
                                        if len(tmp601) > 1:
                                            tmp602 = create_operation_expression(associative1, tmp601)
                                        elif len(tmp601) == 1:
                                            tmp602 = tmp601[0]
                                        else:
                                            assert False, "Unreachable"
                                        subst3 = Substitution(subst2)
                                        try:
                                            subst3.try_add_variable('i2.2.1.2.2', tmp602)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 37992
                                            if len(subjects524) == 0:
                                                pass
                                                # State 37993
                                                if len(subjects474) == 0:
                                                    pass
                                                    # State 37994
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 23: log(c*(d*(x**j*f + e)**p)**q)
                                                        yield 23, subst3
                                        if len(subjects524) == 0:
                                            break
                                        tmp601.append(subjects524.popleft())
                                    subjects524.extendleft(reversed(tmp601))
                        subjects524.appendleft(tmp597)
                    subjects474.appendleft(tmp523)
            if len(subjects474) >= 1 and isinstance(subjects474[0], Mul):
                tmp604 = subjects474.popleft()
                associative1 = tmp604
                associative_type1 = type(tmp604)
                subjects605 = deque(tmp604._args)
                matcher = CommutativeMatcher37996.get()
                tmp606 = subjects605
                subjects605 = []
                for s in tmp606:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp606, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 38277
                        if len(subjects474) == 0:
                            pass
                            # State 38278
                            if len(subjects) == 0:
                                pass
                                # 23: log(c*(d*(x**j*f + e)**p)**q)
                                yield 23, subst1
                subjects474.appendleft(tmp604)
            subjects.appendleft(tmp473)
        if len(subjects) >= 1 and isinstance(subjects[0], sin):
            tmp607 = subjects.popleft()
            subjects608 = deque(tmp607._args)
            # State 58855
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 58856
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.2.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 58857
                    if len(subjects608) >= 1:
                        tmp611 = subjects608.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.2.1.0', tmp611)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 58858
                            if len(subjects608) == 0:
                                pass
                                # State 58859
                                if len(subjects) == 0:
                                    pass
                                    # 24: sin(e + x*f)
                                    yield 24, subst3
                        subjects608.appendleft(tmp611)
                if len(subjects608) >= 1 and isinstance(subjects608[0], Mul):
                    tmp613 = subjects608.popleft()
                    associative1 = tmp613
                    associative_type1 = type(tmp613)
                    subjects614 = deque(tmp613._args)
                    matcher = CommutativeMatcher58861.get()
                    tmp615 = subjects614
                    subjects614 = []
                    for s in tmp615:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp615, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 58862
                            if len(subjects608) == 0:
                                pass
                                # State 58863
                                if len(subjects) == 0:
                                    pass
                                    # 24: sin(e + x*f)
                                    yield 24, subst2
                    subjects608.appendleft(tmp613)
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.3.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 59032
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.3.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 59033
                    if len(subjects608) >= 1:
                        tmp618 = subjects608.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.3.1.0', tmp618)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 59034
                            if len(subjects608) == 0:
                                pass
                                # State 59035
                                if len(subjects) == 0:
                                    pass
                                    # 26: sin(e + x*f)
                                    yield 26, subst3
                        subjects608.appendleft(tmp618)
                if len(subjects608) >= 1 and isinstance(subjects608[0], Mul):
                    tmp620 = subjects608.popleft()
                    associative1 = tmp620
                    associative_type1 = type(tmp620)
                    subjects621 = deque(tmp620._args)
                    matcher = CommutativeMatcher59037.get()
                    tmp622 = subjects621
                    subjects621 = []
                    for s in tmp622:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp622, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 59038
                            if len(subjects608) == 0:
                                pass
                                # State 59039
                                if len(subjects) == 0:
                                    pass
                                    # 26: sin(e + x*f)
                                    yield 26, subst2
                    subjects608.appendleft(tmp620)
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 60175
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 60176
                    if len(subjects608) >= 1:
                        tmp625 = subjects608.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.2.1.0', tmp625)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 60177
                            if len(subjects608) == 0:
                                pass
                                # State 60178
                                if len(subjects) == 0:
                                    pass
                                    # 28: sin(c + x*d)
                                    yield 28, subst3
                        subjects608.appendleft(tmp625)
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.1.0', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 72164
                    if len(subjects608) >= 1:
                        tmp628 = subjects608.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.0', tmp628)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 72165
                            if len(subjects608) == 0:
                                pass
                                # State 72166
                                if len(subjects) == 0:
                                    pass
                                    # 38: sin(x*f + e)
                                    yield 38, subst3
                        subjects608.appendleft(tmp628)
                    if len(subjects608) >= 1 and isinstance(subjects608[0], Pow):
                        tmp630 = subjects608.popleft()
                        subjects631 = deque(tmp630._args)
                        # State 74147
                        if len(subjects631) >= 1:
                            tmp632 = subjects631.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.0_1', tmp632)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 74148
                                if len(subjects631) >= 1:
                                    tmp634 = subjects631.popleft()
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i2.2.1.2.1.2', tmp634)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 74149
                                        if len(subjects631) == 0:
                                            pass
                                            # State 74150
                                            if len(subjects608) == 0:
                                                pass
                                                # State 74151
                                                if len(subjects) == 0:
                                                    pass
                                                    # 39: sin(x**n*d + c)
                                                    yield 39, subst4
                                    subjects631.appendleft(tmp634)
                            subjects631.appendleft(tmp632)
                        if len(subjects631) >= 1:
                            tmp636 = subjects631.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.0', tmp636)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 74748
                                if len(subjects631) >= 1:
                                    tmp638 = subjects631.popleft()
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i2.2.1.2.1.2', tmp638)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 74749
                                        if len(subjects631) == 0:
                                            pass
                                            # State 74750
                                            if len(subjects608) == 0:
                                                pass
                                                # State 74751
                                                if len(subjects) == 0:
                                                    pass
                                                    # 41: sin(x**n*d + c)
                                                    yield 41, subst4
                                    subjects631.appendleft(tmp638)
                            subjects631.appendleft(tmp636)
                        if len(subjects631) >= 1:
                            tmp640 = subjects631.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.2.1.1', tmp640)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 75172
                                if len(subjects631) >= 1:
                                    tmp642 = subjects631.popleft()
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i2.2.1.2.1.2', tmp642)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 75173
                                        if len(subjects631) == 0:
                                            pass
                                            # State 75174
                                            if len(subjects608) == 0:
                                                pass
                                                # State 75175
                                                if len(subjects) == 0:
                                                    pass
                                                    # 43: sin(c + d*x**n)
                                                    yield 43, subst4
                                    subjects631.appendleft(tmp642)
                            subjects631.appendleft(tmp640)
                        subjects608.appendleft(tmp630)
                if len(subjects608) >= 1 and isinstance(subjects608[0], Mul):
                    tmp644 = subjects608.popleft()
                    associative1 = tmp644
                    associative_type1 = type(tmp644)
                    subjects645 = deque(tmp644._args)
                    matcher = CommutativeMatcher60180.get()
                    tmp646 = subjects645
                    subjects645 = []
                    for s in tmp646:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp646, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 60181
                            if len(subjects608) == 0:
                                pass
                                # State 60182
                                if len(subjects) == 0:
                                    pass
                                    # 28: sin(c + x*d)
                                    yield 28, subst2
                        if pattern_index == 1:
                            pass
                            # State 72167
                            if len(subjects608) == 0:
                                pass
                                # State 72168
                                if len(subjects) == 0:
                                    pass
                                    # 38: sin(x*f + e)
                                    yield 38, subst2
                        if pattern_index == 2:
                            pass
                            # State 74156
                            if len(subjects608) == 0:
                                pass
                                # State 74157
                                if len(subjects) == 0:
                                    pass
                                    # 39: sin(x**n*d + c)
                                    yield 39, subst2
                        if pattern_index == 3:
                            pass
                            # State 74755
                            if len(subjects608) == 0:
                                pass
                                # State 74756
                                if len(subjects) == 0:
                                    pass
                                    # 41: sin(x**n*d + c)
                                    yield 41, subst2
                        if pattern_index == 4:
                            pass
                            # State 75179
                            if len(subjects608) == 0:
                                pass
                                # State 75180
                                if len(subjects) == 0:
                                    pass
                                    # 43: sin(c + d*x**n)
                                    yield 43, subst2
                    subjects608.appendleft(tmp644)
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.2.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 61503
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.2.2.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 61504
                    if len(subjects608) >= 1:
                        tmp649 = subjects608.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.2.2.1.0', tmp649)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 61505
                            if len(subjects608) == 0:
                                pass
                                # State 61506
                                if len(subjects) == 0:
                                    pass
                                    # 30: sin(e + x*f)
                                    yield 30, subst3
                        subjects608.appendleft(tmp649)
                if len(subjects608) >= 1 and isinstance(subjects608[0], Mul):
                    tmp651 = subjects608.popleft()
                    associative1 = tmp651
                    associative_type1 = type(tmp651)
                    subjects652 = deque(tmp651._args)
                    matcher = CommutativeMatcher61508.get()
                    tmp653 = subjects652
                    subjects652 = []
                    for s in tmp653:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp653, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 61509
                            if len(subjects608) == 0:
                                pass
                                # State 61510
                                if len(subjects) == 0:
                                    pass
                                    # 30: sin(e + x*f)
                                    yield 30, subst2
                    subjects608.appendleft(tmp651)
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.3.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 61930
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.3.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 61931
                    if len(subjects608) >= 1:
                        tmp656 = subjects608.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.3.1.0', tmp656)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 61932
                            if len(subjects608) == 0:
                                pass
                                # State 61933
                                if len(subjects) == 0:
                                    pass
                                    # 32: sin(e + x*f)
                                    yield 32, subst3
                        subjects608.appendleft(tmp656)
                if len(subjects608) >= 1 and isinstance(subjects608[0], Mul):
                    tmp658 = subjects608.popleft()
                    associative1 = tmp658
                    associative_type1 = type(tmp658)
                    subjects659 = deque(tmp658._args)
                    matcher = CommutativeMatcher61935.get()
                    tmp660 = subjects659
                    subjects659 = []
                    for s in tmp660:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp660, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 61936
                            if len(subjects608) == 0:
                                pass
                                # State 61937
                                if len(subjects) == 0:
                                    pass
                                    # 32: sin(e + x*f)
                                    yield 32, subst2
                    subjects608.appendleft(tmp658)
            if len(subjects608) >= 1:
                tmp661 = subjects608.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.1.1', tmp661)
                except ValueError:
                    pass
                else:
                    pass
                    # State 75376
                    if len(subjects608) == 0:
                        pass
                        # State 75377
                        if len(subjects) == 0:
                            pass
                            # 45: sin(v)
                            yield 45, subst1
                subjects608.appendleft(tmp661)
            if len(subjects608) >= 1 and isinstance(subjects608[0], Add):
                tmp663 = subjects608.popleft()
                associative1 = tmp663
                associative_type1 = type(tmp663)
                subjects664 = deque(tmp663._args)
                matcher = CommutativeMatcher58865.get()
                tmp665 = subjects664
                subjects664 = []
                for s in tmp665:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp665, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 58871
                        if len(subjects608) == 0:
                            pass
                            # State 58872
                            if len(subjects) == 0:
                                pass
                                # 24: sin(e + x*f)
                                yield 24, subst1
                    if pattern_index == 1:
                        pass
                        # State 59043
                        if len(subjects608) == 0:
                            pass
                            # State 59044
                            if len(subjects) == 0:
                                pass
                                # 26: sin(e + x*f)
                                yield 26, subst1
                    if pattern_index == 2:
                        pass
                        # State 60186
                        if len(subjects608) == 0:
                            pass
                            # State 60187
                            if len(subjects) == 0:
                                pass
                                # 28: sin(c + x*d)
                                yield 28, subst1
                    if pattern_index == 3:
                        pass
                        # State 61514
                        if len(subjects608) == 0:
                            pass
                            # State 61515
                            if len(subjects) == 0:
                                pass
                                # 30: sin(e + x*f)
                                yield 30, subst1
                    if pattern_index == 4:
                        pass
                        # State 61941
                        if len(subjects608) == 0:
                            pass
                            # State 61942
                            if len(subjects) == 0:
                                pass
                                # 32: sin(e + x*f)
                                yield 32, subst1
                    if pattern_index == 5:
                        pass
                        # State 72172
                        if len(subjects608) == 0:
                            pass
                            # State 72173
                            if len(subjects) == 0:
                                pass
                                # 38: sin(x*f + e)
                                yield 38, subst1
                    if pattern_index == 6:
                        pass
                        # State 74167
                        if len(subjects608) == 0:
                            pass
                            # State 74168
                            if len(subjects) == 0:
                                pass
                                # 39: sin(x**n*d + c)
                                yield 39, subst1
                    if pattern_index == 7:
                        pass
                        # State 74764
                        if len(subjects608) == 0:
                            pass
                            # State 74765
                            if len(subjects) == 0:
                                pass
                                # 41: sin(x**n*d + c)
                                yield 41, subst1
                    if pattern_index == 8:
                        pass
                        # State 75188
                        if len(subjects608) == 0:
                            pass
                            # State 75189
                            if len(subjects) == 0:
                                pass
                                # 43: sin(c + d*x**n)
                                yield 43, subst1
                subjects608.appendleft(tmp663)
            subjects.appendleft(tmp607)
        if len(subjects) >= 1 and isinstance(subjects[0], cos):
            tmp666 = subjects.popleft()
            subjects667 = deque(tmp666._args)
            # State 58898
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 58899
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.2.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 58900
                    if len(subjects667) >= 1:
                        tmp670 = subjects667.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.2.1.0', tmp670)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 58901
                            if len(subjects667) == 0:
                                pass
                                # State 58902
                                if len(subjects) == 0:
                                    pass
                                    # 25: cos(e + x*f)
                                    yield 25, subst3
                        subjects667.appendleft(tmp670)
                if len(subjects667) >= 1 and isinstance(subjects667[0], Mul):
                    tmp672 = subjects667.popleft()
                    associative1 = tmp672
                    associative_type1 = type(tmp672)
                    subjects673 = deque(tmp672._args)
                    matcher = CommutativeMatcher58904.get()
                    tmp674 = subjects673
                    subjects673 = []
                    for s in tmp674:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp674, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 58905
                            if len(subjects667) == 0:
                                pass
                                # State 58906
                                if len(subjects) == 0:
                                    pass
                                    # 25: cos(e + x*f)
                                    yield 25, subst2
                    subjects667.appendleft(tmp672)
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.3.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 59093
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.3.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 59094
                    if len(subjects667) >= 1:
                        tmp677 = subjects667.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.3.1.0', tmp677)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 59095
                            if len(subjects667) == 0:
                                pass
                                # State 59096
                                if len(subjects) == 0:
                                    pass
                                    # 27: cos(e + x*f)
                                    yield 27, subst3
                        subjects667.appendleft(tmp677)
                if len(subjects667) >= 1 and isinstance(subjects667[0], Mul):
                    tmp679 = subjects667.popleft()
                    associative1 = tmp679
                    associative_type1 = type(tmp679)
                    subjects680 = deque(tmp679._args)
                    matcher = CommutativeMatcher59098.get()
                    tmp681 = subjects680
                    subjects680 = []
                    for s in tmp681:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp681, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 59099
                            if len(subjects667) == 0:
                                pass
                                # State 59100
                                if len(subjects) == 0:
                                    pass
                                    # 27: cos(e + x*f)
                                    yield 27, subst2
                    subjects667.appendleft(tmp679)
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 60233
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 60234
                    if len(subjects667) >= 1:
                        tmp684 = subjects667.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.2.1.0', tmp684)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 60235
                            if len(subjects667) == 0:
                                pass
                                # State 60236
                                if len(subjects) == 0:
                                    pass
                                    # 29: cos(c + x*d)
                                    yield 29, subst3
                        subjects667.appendleft(tmp684)
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.1.0', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 74374
                    if len(subjects667) >= 1 and isinstance(subjects667[0], Pow):
                        tmp687 = subjects667.popleft()
                        subjects688 = deque(tmp687._args)
                        # State 74375
                        if len(subjects688) >= 1:
                            tmp689 = subjects688.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.0_1', tmp689)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 74376
                                if len(subjects688) >= 1:
                                    tmp691 = subjects688.popleft()
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i2.2.1.2.1.2', tmp691)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 74377
                                        if len(subjects688) == 0:
                                            pass
                                            # State 74378
                                            if len(subjects667) == 0:
                                                pass
                                                # State 74379
                                                if len(subjects) == 0:
                                                    pass
                                                    # 40: cos(x**n*d + c)
                                                    yield 40, subst4
                                    subjects688.appendleft(tmp691)
                            subjects688.appendleft(tmp689)
                        if len(subjects688) >= 1:
                            tmp693 = subjects688.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.0', tmp693)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 74911
                                if len(subjects688) >= 1:
                                    tmp695 = subjects688.popleft()
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i2.2.1.2.1.2', tmp695)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 74912
                                        if len(subjects688) == 0:
                                            pass
                                            # State 74913
                                            if len(subjects667) == 0:
                                                pass
                                                # State 74914
                                                if len(subjects) == 0:
                                                    pass
                                                    # 42: cos(x**n*d + c)
                                                    yield 42, subst4
                                    subjects688.appendleft(tmp695)
                            subjects688.appendleft(tmp693)
                        if len(subjects688) >= 1:
                            tmp697 = subjects688.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.2.1.1', tmp697)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 75298
                                if len(subjects688) >= 1:
                                    tmp699 = subjects688.popleft()
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i2.2.1.2.1.2', tmp699)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 75299
                                        if len(subjects688) == 0:
                                            pass
                                            # State 75300
                                            if len(subjects667) == 0:
                                                pass
                                                # State 75301
                                                if len(subjects) == 0:
                                                    pass
                                                    # 44: cos(c + d*x**n)
                                                    yield 44, subst4
                                    subjects688.appendleft(tmp699)
                            subjects688.appendleft(tmp697)
                        subjects667.appendleft(tmp687)
                    if len(subjects667) >= 1:
                        tmp701 = subjects667.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.0', tmp701)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 107255
                            if len(subjects667) == 0:
                                pass
                                # State 107256
                                if len(subjects) == 0:
                                    pass
                                    # 71: cos(x*d + c)
                                    yield 71, subst3
                        subjects667.appendleft(tmp701)
                if len(subjects667) >= 1 and isinstance(subjects667[0], Mul):
                    tmp703 = subjects667.popleft()
                    associative1 = tmp703
                    associative_type1 = type(tmp703)
                    subjects704 = deque(tmp703._args)
                    matcher = CommutativeMatcher60238.get()
                    tmp705 = subjects704
                    subjects704 = []
                    for s in tmp705:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp705, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 60239
                            if len(subjects667) == 0:
                                pass
                                # State 60240
                                if len(subjects) == 0:
                                    pass
                                    # 29: cos(c + x*d)
                                    yield 29, subst2
                        if pattern_index == 1:
                            pass
                            # State 74384
                            if len(subjects667) == 0:
                                pass
                                # State 74385
                                if len(subjects) == 0:
                                    pass
                                    # 40: cos(x**n*d + c)
                                    yield 40, subst2
                        if pattern_index == 2:
                            pass
                            # State 74918
                            if len(subjects667) == 0:
                                pass
                                # State 74919
                                if len(subjects) == 0:
                                    pass
                                    # 42: cos(x**n*d + c)
                                    yield 42, subst2
                        if pattern_index == 3:
                            pass
                            # State 75305
                            if len(subjects667) == 0:
                                pass
                                # State 75306
                                if len(subjects) == 0:
                                    pass
                                    # 44: cos(c + d*x**n)
                                    yield 44, subst2
                        if pattern_index == 4:
                            pass
                            # State 107257
                            if len(subjects667) == 0:
                                pass
                                # State 107258
                                if len(subjects) == 0:
                                    pass
                                    # 71: cos(x*d + c)
                                    yield 71, subst2
                    subjects667.appendleft(tmp703)
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.2.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 61732
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.2.2.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 61733
                    if len(subjects667) >= 1:
                        tmp708 = subjects667.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.2.2.1.0', tmp708)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 61734
                            if len(subjects667) == 0:
                                pass
                                # State 61735
                                if len(subjects) == 0:
                                    pass
                                    # 31: cos(e + x*f)
                                    yield 31, subst3
                        subjects667.appendleft(tmp708)
                if len(subjects667) >= 1 and isinstance(subjects667[0], Mul):
                    tmp710 = subjects667.popleft()
                    associative1 = tmp710
                    associative_type1 = type(tmp710)
                    subjects711 = deque(tmp710._args)
                    matcher = CommutativeMatcher61737.get()
                    tmp712 = subjects711
                    subjects711 = []
                    for s in tmp712:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp712, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 61738
                            if len(subjects667) == 0:
                                pass
                                # State 61739
                                if len(subjects) == 0:
                                    pass
                                    # 31: cos(e + x*f)
                                    yield 31, subst2
                    subjects667.appendleft(tmp710)
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.3.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 62093
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.3.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 62094
                    if len(subjects667) >= 1:
                        tmp715 = subjects667.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.3.1.0', tmp715)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 62095
                            if len(subjects667) == 0:
                                pass
                                # State 62096
                                if len(subjects) == 0:
                                    pass
                                    # 33: cos(e + x*f)
                                    yield 33, subst3
                        subjects667.appendleft(tmp715)
                if len(subjects667) >= 1 and isinstance(subjects667[0], Mul):
                    tmp717 = subjects667.popleft()
                    associative1 = tmp717
                    associative_type1 = type(tmp717)
                    subjects718 = deque(tmp717._args)
                    matcher = CommutativeMatcher62098.get()
                    tmp719 = subjects718
                    subjects718 = []
                    for s in tmp719:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp719, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 62099
                            if len(subjects667) == 0:
                                pass
                                # State 62100
                                if len(subjects) == 0:
                                    pass
                                    # 33: cos(e + x*f)
                                    yield 33, subst2
                    subjects667.appendleft(tmp717)
            if len(subjects667) >= 1:
                tmp720 = subjects667.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.1.1', tmp720)
                except ValueError:
                    pass
                else:
                    pass
                    # State 75402
                    if len(subjects667) == 0:
                        pass
                        # State 75403
                        if len(subjects) == 0:
                            pass
                            # 46: cos(v)
                            yield 46, subst1
                subjects667.appendleft(tmp720)
            if len(subjects667) >= 1 and isinstance(subjects667[0], Add):
                tmp722 = subjects667.popleft()
                associative1 = tmp722
                associative_type1 = type(tmp722)
                subjects723 = deque(tmp722._args)
                matcher = CommutativeMatcher58908.get()
                tmp724 = subjects723
                subjects723 = []
                for s in tmp724:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp724, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 58914
                        if len(subjects667) == 0:
                            pass
                            # State 58915
                            if len(subjects) == 0:
                                pass
                                # 25: cos(e + x*f)
                                yield 25, subst1
                    if pattern_index == 1:
                        pass
                        # State 59104
                        if len(subjects667) == 0:
                            pass
                            # State 59105
                            if len(subjects) == 0:
                                pass
                                # 27: cos(e + x*f)
                                yield 27, subst1
                    if pattern_index == 2:
                        pass
                        # State 60244
                        if len(subjects667) == 0:
                            pass
                            # State 60245
                            if len(subjects) == 0:
                                pass
                                # 29: cos(c + x*d)
                                yield 29, subst1
                    if pattern_index == 3:
                        pass
                        # State 61743
                        if len(subjects667) == 0:
                            pass
                            # State 61744
                            if len(subjects) == 0:
                                pass
                                # 31: cos(e + x*f)
                                yield 31, subst1
                    if pattern_index == 4:
                        pass
                        # State 62104
                        if len(subjects667) == 0:
                            pass
                            # State 62105
                            if len(subjects) == 0:
                                pass
                                # 33: cos(e + x*f)
                                yield 33, subst1
                    if pattern_index == 5:
                        pass
                        # State 74396
                        if len(subjects667) == 0:
                            pass
                            # State 74397
                            if len(subjects) == 0:
                                pass
                                # 40: cos(x**n*d + c)
                                yield 40, subst1
                    if pattern_index == 6:
                        pass
                        # State 74927
                        if len(subjects667) == 0:
                            pass
                            # State 74928
                            if len(subjects) == 0:
                                pass
                                # 42: cos(x**n*d + c)
                                yield 42, subst1
                    if pattern_index == 7:
                        pass
                        # State 75314
                        if len(subjects667) == 0:
                            pass
                            # State 75315
                            if len(subjects) == 0:
                                pass
                                # 44: cos(c + d*x**n)
                                yield 44, subst1
                    if pattern_index == 8:
                        pass
                        # State 107261
                        if len(subjects667) == 0:
                            pass
                            # State 107262
                            if len(subjects) == 0:
                                pass
                                # 71: cos(x*d + c)
                                yield 71, subst1
                subjects667.appendleft(tmp722)
            subjects.appendleft(tmp666)
        if len(subjects) >= 1 and isinstance(subjects[0], tan):
            tmp725 = subjects.popleft()
            subjects726 = deque(tmp725._args)
            # State 78015
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.3.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 78016
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.3.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 78017
                    if len(subjects726) >= 1:
                        tmp729 = subjects726.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.3.1.0', tmp729)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 78018
                            if len(subjects726) == 0:
                                pass
                                # State 78019
                                if len(subjects) == 0:
                                    pass
                                    # 47: tan(e + x*f)
                                    yield 47, subst3
                        subjects726.appendleft(tmp729)
                if len(subjects726) >= 1 and isinstance(subjects726[0], Mul):
                    tmp731 = subjects726.popleft()
                    associative1 = tmp731
                    associative_type1 = type(tmp731)
                    subjects732 = deque(tmp731._args)
                    matcher = CommutativeMatcher78021.get()
                    tmp733 = subjects732
                    subjects732 = []
                    for s in tmp733:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp733, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 78022
                            if len(subjects726) == 0:
                                pass
                                # State 78023
                                if len(subjects) == 0:
                                    pass
                                    # 47: tan(e + x*f)
                                    yield 47, subst2
                    subjects726.appendleft(tmp731)
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 78278
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.2.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 78279
                    if len(subjects726) >= 1:
                        tmp736 = subjects726.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.2.1.0', tmp736)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 78280
                            if len(subjects726) == 0:
                                pass
                                # State 78281
                                if len(subjects) == 0:
                                    pass
                                    # 49: tan(e + x*f)
                                    yield 49, subst3
                        subjects726.appendleft(tmp736)
                if len(subjects726) >= 1 and isinstance(subjects726[0], Mul):
                    tmp738 = subjects726.popleft()
                    associative1 = tmp738
                    associative_type1 = type(tmp738)
                    subjects739 = deque(tmp738._args)
                    matcher = CommutativeMatcher78283.get()
                    tmp740 = subjects739
                    subjects739 = []
                    for s in tmp740:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp740, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 78284
                            if len(subjects726) == 0:
                                pass
                                # State 78285
                                if len(subjects) == 0:
                                    pass
                                    # 49: tan(e + x*f)
                                    yield 49, subst2
                    subjects726.appendleft(tmp738)
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 78673
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 78674
                    if len(subjects726) >= 1:
                        tmp743 = subjects726.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.2.1.0', tmp743)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 78675
                            if len(subjects726) == 0:
                                pass
                                # State 78676
                                if len(subjects) == 0:
                                    pass
                                    # 51: tan(c + x*d)
                                    yield 51, subst3
                        subjects726.appendleft(tmp743)
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.1.0', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 86748
                    if len(subjects726) >= 1:
                        tmp746 = subjects726.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.0', tmp746)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 86749
                            if len(subjects726) == 0:
                                pass
                                # State 86750
                                if len(subjects) == 0:
                                    pass
                                    # 57: tan(x*f + e)
                                    yield 57, subst3
                        subjects726.appendleft(tmp746)
                    if len(subjects726) >= 1 and isinstance(subjects726[0], Pow):
                        tmp748 = subjects726.popleft()
                        subjects749 = deque(tmp748._args)
                        # State 88545
                        if len(subjects749) >= 1:
                            tmp750 = subjects749.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.0_1', tmp750)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 88546
                                if len(subjects749) >= 1:
                                    tmp752 = subjects749.popleft()
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i2.2.1.2.1.2', tmp752)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 88547
                                        if len(subjects749) == 0:
                                            pass
                                            # State 88548
                                            if len(subjects726) == 0:
                                                pass
                                                # State 88549
                                                if len(subjects) == 0:
                                                    pass
                                                    # 58: tan(x**n*d + c)
                                                    yield 58, subst4
                                    subjects749.appendleft(tmp752)
                            subjects749.appendleft(tmp750)
                        subjects726.appendleft(tmp748)
                if len(subjects726) >= 1 and isinstance(subjects726[0], Mul):
                    tmp754 = subjects726.popleft()
                    associative1 = tmp754
                    associative_type1 = type(tmp754)
                    subjects755 = deque(tmp754._args)
                    matcher = CommutativeMatcher78678.get()
                    tmp756 = subjects755
                    subjects755 = []
                    for s in tmp756:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp756, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 78679
                            if len(subjects726) == 0:
                                pass
                                # State 78680
                                if len(subjects) == 0:
                                    pass
                                    # 51: tan(c + x*d)
                                    yield 51, subst2
                        if pattern_index == 1:
                            pass
                            # State 86751
                            if len(subjects726) == 0:
                                pass
                                # State 86752
                                if len(subjects) == 0:
                                    pass
                                    # 57: tan(x*f + e)
                                    yield 57, subst2
                        if pattern_index == 2:
                            pass
                            # State 88554
                            if len(subjects726) == 0:
                                pass
                                # State 88555
                                if len(subjects) == 0:
                                    pass
                                    # 58: tan(x**n*d + c)
                                    yield 58, subst2
                    subjects726.appendleft(tmp754)
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.2.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 80080
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.2.2.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 80081
                    if len(subjects726) >= 1:
                        tmp759 = subjects726.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.2.2.1.0', tmp759)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 80082
                            if len(subjects726) == 0:
                                pass
                                # State 80083
                                if len(subjects) == 0:
                                    pass
                                    # 53: tan(e + x*f)
                                    yield 53, subst3
                        subjects726.appendleft(tmp759)
                if len(subjects726) >= 1 and isinstance(subjects726[0], Mul):
                    tmp761 = subjects726.popleft()
                    associative1 = tmp761
                    associative_type1 = type(tmp761)
                    subjects762 = deque(tmp761._args)
                    matcher = CommutativeMatcher80085.get()
                    tmp763 = subjects762
                    subjects762 = []
                    for s in tmp763:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp763, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 80086
                            if len(subjects726) == 0:
                                pass
                                # State 80087
                                if len(subjects) == 0:
                                    pass
                                    # 53: tan(e + x*f)
                                    yield 53, subst2
                    subjects726.appendleft(tmp761)
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.3.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 81019
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.3.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 81020
                    if len(subjects726) >= 1:
                        tmp766 = subjects726.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.3.1.0', tmp766)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 81021
                            if len(subjects726) == 0:
                                pass
                                # State 81022
                                if len(subjects) == 0:
                                    pass
                                    # 56: tan(e + x*f)
                                    yield 56, subst3
                        subjects726.appendleft(tmp766)
                if len(subjects726) >= 1 and isinstance(subjects726[0], Mul):
                    tmp768 = subjects726.popleft()
                    associative1 = tmp768
                    associative_type1 = type(tmp768)
                    subjects769 = deque(tmp768._args)
                    matcher = CommutativeMatcher81024.get()
                    tmp770 = subjects769
                    subjects769 = []
                    for s in tmp770:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp770, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 81025
                            if len(subjects726) == 0:
                                pass
                                # State 81026
                                if len(subjects) == 0:
                                    pass
                                    # 56: tan(e + x*f)
                                    yield 56, subst2
                    subjects726.appendleft(tmp768)
            if len(subjects726) >= 1:
                tmp771 = subjects726.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.1.1', tmp771)
                except ValueError:
                    pass
                else:
                    pass
                    # State 88974
                    if len(subjects726) == 0:
                        pass
                        # State 88975
                        if len(subjects) == 0:
                            pass
                            # 60: tan(v)
                            yield 60, subst1
                subjects726.appendleft(tmp771)
            if len(subjects726) >= 1 and isinstance(subjects726[0], Add):
                tmp773 = subjects726.popleft()
                associative1 = tmp773
                associative_type1 = type(tmp773)
                subjects774 = deque(tmp773._args)
                matcher = CommutativeMatcher78025.get()
                tmp775 = subjects774
                subjects774 = []
                for s in tmp775:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp775, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 78031
                        if len(subjects726) == 0:
                            pass
                            # State 78032
                            if len(subjects) == 0:
                                pass
                                # 47: tan(e + x*f)
                                yield 47, subst1
                    if pattern_index == 1:
                        pass
                        # State 78289
                        if len(subjects726) == 0:
                            pass
                            # State 78290
                            if len(subjects) == 0:
                                pass
                                # 49: tan(e + x*f)
                                yield 49, subst1
                    if pattern_index == 2:
                        pass
                        # State 78684
                        if len(subjects726) == 0:
                            pass
                            # State 78685
                            if len(subjects) == 0:
                                pass
                                # 51: tan(c + x*d)
                                yield 51, subst1
                    if pattern_index == 3:
                        pass
                        # State 80091
                        if len(subjects726) == 0:
                            pass
                            # State 80092
                            if len(subjects) == 0:
                                pass
                                # 53: tan(e + x*f)
                                yield 53, subst1
                    if pattern_index == 4:
                        pass
                        # State 81030
                        if len(subjects726) == 0:
                            pass
                            # State 81031
                            if len(subjects) == 0:
                                pass
                                # 56: tan(e + x*f)
                                yield 56, subst1
                    if pattern_index == 5:
                        pass
                        # State 86756
                        if len(subjects726) == 0:
                            pass
                            # State 86757
                            if len(subjects) == 0:
                                pass
                                # 57: tan(x*f + e)
                                yield 57, subst1
                    if pattern_index == 6:
                        pass
                        # State 88565
                        if len(subjects726) == 0:
                            pass
                            # State 88566
                            if len(subjects) == 0:
                                pass
                                # 58: tan(x**n*d + c)
                                yield 58, subst1
                subjects726.appendleft(tmp773)
            subjects.appendleft(tmp725)
        if len(subjects) >= 1 and isinstance(subjects[0], asin):
            tmp776 = subjects.popleft()
            subjects777 = deque(tmp776._args)
            # State 108385
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.0', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 108386
                if len(subjects777) >= 1:
                    tmp779 = subjects777.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.0', tmp779)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 108387
                        if len(subjects777) == 0:
                            pass
                            # State 108388
                            if len(subjects) == 0:
                                pass
                                # 72: asin(x*c)
                                yield 72, subst2
                    subjects777.appendleft(tmp779)
                if len(subjects777) >= 1:
                    tmp781 = subjects777.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.1', tmp781)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 108842
                        if len(subjects777) == 0:
                            pass
                            # State 108843
                            if len(subjects) == 0:
                                pass
                                # 74: asin(x*c)
                                yield 74, subst2
                    subjects777.appendleft(tmp781)
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.0_1', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 109858
                if len(subjects777) >= 1:
                    tmp784 = subjects777.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.2.1.1', tmp784)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 109859
                        if len(subjects777) == 0:
                            pass
                            # State 109860
                            if len(subjects) == 0:
                                pass
                                # 77: asin(c*x)
                                yield 77, subst2
                    subjects777.appendleft(tmp784)
            if len(subjects777) >= 1 and isinstance(subjects777[0], Mul):
                tmp786 = subjects777.popleft()
                associative1 = tmp786
                associative_type1 = type(tmp786)
                subjects787 = deque(tmp786._args)
                matcher = CommutativeMatcher108390.get()
                tmp788 = subjects787
                subjects787 = []
                for s in tmp788:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp788, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 108391
                        if len(subjects777) == 0:
                            pass
                            # State 108392
                            if len(subjects) == 0:
                                pass
                                # 72: asin(x*c)
                                yield 72, subst1
                    if pattern_index == 1:
                        pass
                        # State 108844
                        if len(subjects777) == 0:
                            pass
                            # State 108845
                            if len(subjects) == 0:
                                pass
                                # 74: asin(x*c)
                                yield 74, subst1
                    if pattern_index == 2:
                        pass
                        # State 109861
                        if len(subjects777) == 0:
                            pass
                            # State 109862
                            if len(subjects) == 0:
                                pass
                                # 77: asin(c*x)
                                yield 77, subst1
                subjects777.appendleft(tmp786)
            subjects.appendleft(tmp776)
        if len(subjects) >= 1 and isinstance(subjects[0], acos):
            tmp789 = subjects.popleft()
            subjects790 = deque(tmp789._args)
            # State 108460
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.0', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 108461
                if len(subjects790) >= 1:
                    tmp792 = subjects790.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.0', tmp792)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 108462
                        if len(subjects790) == 0:
                            pass
                            # State 108463
                            if len(subjects) == 0:
                                pass
                                # 73: acos(x*c)
                                yield 73, subst2
                    subjects790.appendleft(tmp792)
                if len(subjects790) >= 1:
                    tmp794 = subjects790.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.1', tmp794)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 108884
                        if len(subjects790) == 0:
                            pass
                            # State 108885
                            if len(subjects) == 0:
                                pass
                                # 75: acos(x*c)
                                yield 75, subst2
                    subjects790.appendleft(tmp794)
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.0_1', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 109914
                if len(subjects790) >= 1:
                    tmp797 = subjects790.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.2.1.1', tmp797)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 109915
                        if len(subjects790) == 0:
                            pass
                            # State 109916
                            if len(subjects) == 0:
                                pass
                                # 78: acos(c*x)
                                yield 78, subst2
                    subjects790.appendleft(tmp797)
            if len(subjects790) >= 1 and isinstance(subjects790[0], Mul):
                tmp799 = subjects790.popleft()
                associative1 = tmp799
                associative_type1 = type(tmp799)
                subjects800 = deque(tmp799._args)
                matcher = CommutativeMatcher108465.get()
                tmp801 = subjects800
                subjects800 = []
                for s in tmp801:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp801, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 108466
                        if len(subjects790) == 0:
                            pass
                            # State 108467
                            if len(subjects) == 0:
                                pass
                                # 73: acos(x*c)
                                yield 73, subst1
                    if pattern_index == 1:
                        pass
                        # State 108886
                        if len(subjects790) == 0:
                            pass
                            # State 108887
                            if len(subjects) == 0:
                                pass
                                # 75: acos(x*c)
                                yield 75, subst1
                    if pattern_index == 2:
                        pass
                        # State 109917
                        if len(subjects790) == 0:
                            pass
                            # State 109918
                            if len(subjects) == 0:
                                pass
                                # 78: acos(c*x)
                                yield 78, subst1
                subjects790.appendleft(tmp799)
            subjects.appendleft(tmp789)
        if len(subjects) >= 1 and isinstance(subjects[0], atan):
            tmp802 = subjects.popleft()
            subjects803 = deque(tmp802._args)
            # State 113493
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.0', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 113494
                if len(subjects803) >= 1:
                    tmp805 = subjects803.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.1', tmp805)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 113495
                        if len(subjects803) == 0:
                            pass
                            # State 113496
                            if len(subjects) == 0:
                                pass
                                # 80: atan(x*c)
                                yield 80, subst2
                    subjects803.appendleft(tmp805)
            if len(subjects803) >= 1 and isinstance(subjects803[0], Mul):
                tmp807 = subjects803.popleft()
                associative1 = tmp807
                associative_type1 = type(tmp807)
                subjects808 = deque(tmp807._args)
                matcher = CommutativeMatcher113498.get()
                tmp809 = subjects808
                subjects808 = []
                for s in tmp809:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp809, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 113499
                        if len(subjects803) == 0:
                            pass
                            # State 113500
                            if len(subjects) == 0:
                                pass
                                # 80: atan(x*c)
                                yield 80, subst1
                subjects803.appendleft(tmp807)
            subjects.appendleft(tmp802)
        if len(subjects) >= 1 and isinstance(subjects[0], acot):
            tmp810 = subjects.popleft()
            subjects811 = deque(tmp810._args)
            # State 113542
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.0', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 113543
                if len(subjects811) >= 1:
                    tmp813 = subjects811.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.1', tmp813)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 113544
                        if len(subjects811) == 0:
                            pass
                            # State 113545
                            if len(subjects) == 0:
                                pass
                                # 81: acot(x*c)
                                yield 81, subst2
                    subjects811.appendleft(tmp813)
            if len(subjects811) >= 1 and isinstance(subjects811[0], Mul):
                tmp815 = subjects811.popleft()
                associative1 = tmp815
                associative_type1 = type(tmp815)
                subjects816 = deque(tmp815._args)
                matcher = CommutativeMatcher113547.get()
                tmp817 = subjects816
                subjects816 = []
                for s in tmp817:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp817, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 113548
                        if len(subjects811) == 0:
                            pass
                            # State 113549
                            if len(subjects) == 0:
                                pass
                                # 81: acot(x*c)
                                yield 81, subst1
                subjects811.appendleft(tmp815)
            subjects.appendleft(tmp810)
        if len(subjects) >= 1 and isinstance(subjects[0], asec):
            tmp818 = subjects.popleft()
            subjects819 = deque(tmp818._args)
            # State 119964
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.0', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 119965
                if len(subjects819) >= 1:
                    tmp821 = subjects819.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.1', tmp821)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 119966
                        if len(subjects819) == 0:
                            pass
                            # State 119967
                            if len(subjects) == 0:
                                pass
                                # 82: asec(x*c)
                                yield 82, subst2
                    subjects819.appendleft(tmp821)
            if len(subjects819) >= 1 and isinstance(subjects819[0], Mul):
                tmp823 = subjects819.popleft()
                associative1 = tmp823
                associative_type1 = type(tmp823)
                subjects824 = deque(tmp823._args)
                matcher = CommutativeMatcher119969.get()
                tmp825 = subjects824
                subjects824 = []
                for s in tmp825:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp825, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 119970
                        if len(subjects819) == 0:
                            pass
                            # State 119971
                            if len(subjects) == 0:
                                pass
                                # 82: asec(x*c)
                                yield 82, subst1
                subjects819.appendleft(tmp823)
            subjects.appendleft(tmp818)
        if len(subjects) >= 1 and isinstance(subjects[0], acsc):
            tmp826 = subjects.popleft()
            subjects827 = deque(tmp826._args)
            # State 120042
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.0', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 120043
                if len(subjects827) >= 1:
                    tmp829 = subjects827.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.1', tmp829)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 120044
                        if len(subjects827) == 0:
                            pass
                            # State 120045
                            if len(subjects) == 0:
                                pass
                                # 83: acsc(x*c)
                                yield 83, subst2
                    subjects827.appendleft(tmp829)
            if len(subjects827) >= 1 and isinstance(subjects827[0], Mul):
                tmp831 = subjects827.popleft()
                associative1 = tmp831
                associative_type1 = type(tmp831)
                subjects832 = deque(tmp831._args)
                matcher = CommutativeMatcher120047.get()
                tmp833 = subjects832
                subjects832 = []
                for s in tmp833:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp833, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 120048
                        if len(subjects827) == 0:
                            pass
                            # State 120049
                            if len(subjects) == 0:
                                pass
                                # 83: acsc(x*c)
                                yield 83, subst1
                subjects827.appendleft(tmp831)
            subjects.appendleft(tmp826)
        if len(subjects) >= 1 and isinstance(subjects[0], sinh):
            tmp834 = subjects.popleft()
            subjects835 = deque(tmp834._args)
            # State 121843
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 121844
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.1.0', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 121845
                    if len(subjects835) >= 1:
                        tmp838 = subjects835.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.0', tmp838)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 121846
                            if len(subjects835) == 0:
                                pass
                                # State 121847
                                if len(subjects) == 0:
                                    pass
                                    # 84: sinh(x*b + a)
                                    yield 84, subst3
                        subjects835.appendleft(tmp838)
                    if len(subjects835) >= 1 and isinstance(subjects835[0], Pow):
                        tmp840 = subjects835.popleft()
                        subjects841 = deque(tmp840._args)
                        # State 124070
                        if len(subjects841) >= 1:
                            tmp842 = subjects841.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.0_1', tmp842)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 124071
                                if len(subjects841) >= 1:
                                    tmp844 = subjects841.popleft()
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i2.2.1.2.1.2', tmp844)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 124072
                                        if len(subjects841) == 0:
                                            pass
                                            # State 124073
                                            if len(subjects835) == 0:
                                                pass
                                                # State 124074
                                                if len(subjects) == 0:
                                                    pass
                                                    # 85: sinh(x**n*d + c)
                                                    yield 85, subst4
                                    subjects841.appendleft(tmp844)
                            subjects841.appendleft(tmp842)
                        if len(subjects841) >= 1:
                            tmp846 = subjects841.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.0', tmp846)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 124658
                                if len(subjects841) >= 1:
                                    tmp848 = subjects841.popleft()
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i2.2.1.2.1.2', tmp848)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 124659
                                        if len(subjects841) == 0:
                                            pass
                                            # State 124660
                                            if len(subjects835) == 0:
                                                pass
                                                # State 124661
                                                if len(subjects) == 0:
                                                    pass
                                                    # 87: sinh(x**n*d + c)
                                                    yield 87, subst4
                                    subjects841.appendleft(tmp848)
                            subjects841.appendleft(tmp846)
                        if len(subjects841) >= 1:
                            tmp850 = subjects841.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.2.1.1', tmp850)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 125082
                                if len(subjects841) >= 1:
                                    tmp852 = subjects841.popleft()
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i2.2.1.2.1.2', tmp852)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 125083
                                        if len(subjects841) == 0:
                                            pass
                                            # State 125084
                                            if len(subjects835) == 0:
                                                pass
                                                # State 125085
                                                if len(subjects) == 0:
                                                    pass
                                                    # 89: sinh(c + d*x**n)
                                                    yield 89, subst4
                                    subjects841.appendleft(tmp852)
                            subjects841.appendleft(tmp850)
                        subjects835.appendleft(tmp840)
                if len(subjects835) >= 1 and isinstance(subjects835[0], Mul):
                    tmp854 = subjects835.popleft()
                    associative1 = tmp854
                    associative_type1 = type(tmp854)
                    subjects855 = deque(tmp854._args)
                    matcher = CommutativeMatcher121849.get()
                    tmp856 = subjects855
                    subjects855 = []
                    for s in tmp856:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp856, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 121850
                            if len(subjects835) == 0:
                                pass
                                # State 121851
                                if len(subjects) == 0:
                                    pass
                                    # 84: sinh(x*b + a)
                                    yield 84, subst2
                        if pattern_index == 1:
                            pass
                            # State 124079
                            if len(subjects835) == 0:
                                pass
                                # State 124080
                                if len(subjects) == 0:
                                    pass
                                    # 85: sinh(x**n*d + c)
                                    yield 85, subst2
                        if pattern_index == 2:
                            pass
                            # State 124665
                            if len(subjects835) == 0:
                                pass
                                # State 124666
                                if len(subjects) == 0:
                                    pass
                                    # 87: sinh(x**n*d + c)
                                    yield 87, subst2
                        if pattern_index == 3:
                            pass
                            # State 125089
                            if len(subjects835) == 0:
                                pass
                                # State 125090
                                if len(subjects) == 0:
                                    pass
                                    # 89: sinh(c + d*x**n)
                                    yield 89, subst2
                    subjects835.appendleft(tmp854)
            if len(subjects835) >= 1:
                tmp857 = subjects835.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.1.1', tmp857)
                except ValueError:
                    pass
                else:
                    pass
                    # State 125286
                    if len(subjects835) == 0:
                        pass
                        # State 125287
                        if len(subjects) == 0:
                            pass
                            # 91: sinh(v)
                            yield 91, subst1
                subjects835.appendleft(tmp857)
            if len(subjects835) >= 1 and isinstance(subjects835[0], Add):
                tmp859 = subjects835.popleft()
                associative1 = tmp859
                associative_type1 = type(tmp859)
                subjects860 = deque(tmp859._args)
                matcher = CommutativeMatcher121853.get()
                tmp861 = subjects860
                subjects860 = []
                for s in tmp861:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp861, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 121859
                        if len(subjects835) == 0:
                            pass
                            # State 121860
                            if len(subjects) == 0:
                                pass
                                # 84: sinh(x*b + a)
                                yield 84, subst1
                    if pattern_index == 1:
                        pass
                        # State 124090
                        if len(subjects835) == 0:
                            pass
                            # State 124091
                            if len(subjects) == 0:
                                pass
                                # 85: sinh(x**n*d + c)
                                yield 85, subst1
                    if pattern_index == 2:
                        pass
                        # State 124674
                        if len(subjects835) == 0:
                            pass
                            # State 124675
                            if len(subjects) == 0:
                                pass
                                # 87: sinh(x**n*d + c)
                                yield 87, subst1
                    if pattern_index == 3:
                        pass
                        # State 125098
                        if len(subjects835) == 0:
                            pass
                            # State 125099
                            if len(subjects) == 0:
                                pass
                                # 89: sinh(c + d*x**n)
                                yield 89, subst1
                subjects835.appendleft(tmp859)
            subjects.appendleft(tmp834)
        if len(subjects) >= 1 and isinstance(subjects[0], cosh):
            tmp862 = subjects.popleft()
            subjects863 = deque(tmp862._args)
            # State 124307
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 124308
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.1.0', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 124309
                    if len(subjects863) >= 1 and isinstance(subjects863[0], Pow):
                        tmp866 = subjects863.popleft()
                        subjects867 = deque(tmp866._args)
                        # State 124310
                        if len(subjects867) >= 1:
                            tmp868 = subjects867.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.0_1', tmp868)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 124311
                                if len(subjects867) >= 1:
                                    tmp870 = subjects867.popleft()
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i2.2.1.2.1.2', tmp870)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 124312
                                        if len(subjects867) == 0:
                                            pass
                                            # State 124313
                                            if len(subjects863) == 0:
                                                pass
                                                # State 124314
                                                if len(subjects) == 0:
                                                    pass
                                                    # 86: cosh(x**n*d + c)
                                                    yield 86, subst4
                                    subjects867.appendleft(tmp870)
                            subjects867.appendleft(tmp868)
                        if len(subjects867) >= 1:
                            tmp872 = subjects867.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.0', tmp872)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 124821
                                if len(subjects867) >= 1:
                                    tmp874 = subjects867.popleft()
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i2.2.1.2.1.2', tmp874)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 124822
                                        if len(subjects867) == 0:
                                            pass
                                            # State 124823
                                            if len(subjects863) == 0:
                                                pass
                                                # State 124824
                                                if len(subjects) == 0:
                                                    pass
                                                    # 88: cosh(x**n*d + c)
                                                    yield 88, subst4
                                    subjects867.appendleft(tmp874)
                            subjects867.appendleft(tmp872)
                        if len(subjects867) >= 1:
                            tmp876 = subjects867.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.2.1.1', tmp876)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 125208
                                if len(subjects867) >= 1:
                                    tmp878 = subjects867.popleft()
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i2.2.1.2.1.2', tmp878)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 125209
                                        if len(subjects867) == 0:
                                            pass
                                            # State 125210
                                            if len(subjects863) == 0:
                                                pass
                                                # State 125211
                                                if len(subjects) == 0:
                                                    pass
                                                    # 90: cosh(c + d*x**n)
                                                    yield 90, subst4
                                    subjects867.appendleft(tmp878)
                            subjects867.appendleft(tmp876)
                        subjects863.appendleft(tmp866)
                    if len(subjects863) >= 1:
                        tmp880 = subjects863.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.0', tmp880)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 136860
                            if len(subjects863) == 0:
                                pass
                                # State 136861
                                if len(subjects) == 0:
                                    pass
                                    # 102: cosh(x*b + a)
                                    yield 102, subst3
                        subjects863.appendleft(tmp880)
                if len(subjects863) >= 1 and isinstance(subjects863[0], Mul):
                    tmp882 = subjects863.popleft()
                    associative1 = tmp882
                    associative_type1 = type(tmp882)
                    subjects883 = deque(tmp882._args)
                    matcher = CommutativeMatcher124316.get()
                    tmp884 = subjects883
                    subjects883 = []
                    for s in tmp884:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp884, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 124321
                            if len(subjects863) == 0:
                                pass
                                # State 124322
                                if len(subjects) == 0:
                                    pass
                                    # 86: cosh(x**n*d + c)
                                    yield 86, subst2
                        if pattern_index == 1:
                            pass
                            # State 124828
                            if len(subjects863) == 0:
                                pass
                                # State 124829
                                if len(subjects) == 0:
                                    pass
                                    # 88: cosh(x**n*d + c)
                                    yield 88, subst2
                        if pattern_index == 2:
                            pass
                            # State 125215
                            if len(subjects863) == 0:
                                pass
                                # State 125216
                                if len(subjects) == 0:
                                    pass
                                    # 90: cosh(c + d*x**n)
                                    yield 90, subst2
                        if pattern_index == 3:
                            pass
                            # State 136862
                            if len(subjects863) == 0:
                                pass
                                # State 136863
                                if len(subjects) == 0:
                                    pass
                                    # 102: cosh(x*b + a)
                                    yield 102, subst2
                    subjects863.appendleft(tmp882)
            if len(subjects863) >= 1:
                tmp885 = subjects863.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.1.1', tmp885)
                except ValueError:
                    pass
                else:
                    pass
                    # State 125312
                    if len(subjects863) == 0:
                        pass
                        # State 125313
                        if len(subjects) == 0:
                            pass
                            # 92: cosh(v)
                            yield 92, subst1
                subjects863.appendleft(tmp885)
            if len(subjects863) >= 1 and isinstance(subjects863[0], Add):
                tmp887 = subjects863.popleft()
                associative1 = tmp887
                associative_type1 = type(tmp887)
                subjects888 = deque(tmp887._args)
                matcher = CommutativeMatcher124324.get()
                tmp889 = subjects888
                subjects888 = []
                for s in tmp889:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp889, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 124337
                        if len(subjects863) == 0:
                            pass
                            # State 124338
                            if len(subjects) == 0:
                                pass
                                # 86: cosh(x**n*d + c)
                                yield 86, subst1
                    if pattern_index == 1:
                        pass
                        # State 124837
                        if len(subjects863) == 0:
                            pass
                            # State 124838
                            if len(subjects) == 0:
                                pass
                                # 88: cosh(x**n*d + c)
                                yield 88, subst1
                    if pattern_index == 2:
                        pass
                        # State 125224
                        if len(subjects863) == 0:
                            pass
                            # State 125225
                            if len(subjects) == 0:
                                pass
                                # 90: cosh(c + d*x**n)
                                yield 90, subst1
                    if pattern_index == 3:
                        pass
                        # State 136866
                        if len(subjects863) == 0:
                            pass
                            # State 136867
                            if len(subjects) == 0:
                                pass
                                # 102: cosh(x*b + a)
                                yield 102, subst1
                subjects863.appendleft(tmp887)
            subjects.appendleft(tmp862)
        if len(subjects) >= 1 and isinstance(subjects[0], tanh):
            tmp890 = subjects.popleft()
            subjects891 = deque(tmp890._args)
            # State 125972
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 125973
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.1.0', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 125974
                    if len(subjects891) >= 1:
                        tmp894 = subjects891.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.0', tmp894)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 125975
                            if len(subjects891) == 0:
                                pass
                                # State 125976
                                if len(subjects) == 0:
                                    pass
                                    # 93: tanh(x*b + a)
                                    yield 93, subst3
                        subjects891.appendleft(tmp894)
                    if len(subjects891) >= 1 and isinstance(subjects891[0], Pow):
                        tmp896 = subjects891.popleft()
                        subjects897 = deque(tmp896._args)
                        # State 128083
                        if len(subjects897) >= 1:
                            tmp898 = subjects897.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.0_1', tmp898)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 128084
                                if len(subjects897) >= 1:
                                    tmp900 = subjects897.popleft()
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i2.2.1.2.1.2', tmp900)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 128085
                                        if len(subjects897) == 0:
                                            pass
                                            # State 128086
                                            if len(subjects891) == 0:
                                                pass
                                                # State 128087
                                                if len(subjects) == 0:
                                                    pass
                                                    # 94: tanh(x**n*d + c)
                                                    yield 94, subst4
                                    subjects897.appendleft(tmp900)
                            subjects897.appendleft(tmp898)
                        subjects891.appendleft(tmp896)
                if len(subjects891) >= 1 and isinstance(subjects891[0], Mul):
                    tmp902 = subjects891.popleft()
                    associative1 = tmp902
                    associative_type1 = type(tmp902)
                    subjects903 = deque(tmp902._args)
                    matcher = CommutativeMatcher125978.get()
                    tmp904 = subjects903
                    subjects903 = []
                    for s in tmp904:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp904, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 125979
                            if len(subjects891) == 0:
                                pass
                                # State 125980
                                if len(subjects) == 0:
                                    pass
                                    # 93: tanh(x*b + a)
                                    yield 93, subst2
                        if pattern_index == 1:
                            pass
                            # State 128092
                            if len(subjects891) == 0:
                                pass
                                # State 128093
                                if len(subjects) == 0:
                                    pass
                                    # 94: tanh(x**n*d + c)
                                    yield 94, subst2
                    subjects891.appendleft(tmp902)
            if len(subjects891) >= 1:
                tmp905 = subjects891.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.1.1', tmp905)
                except ValueError:
                    pass
                else:
                    pass
                    # State 128525
                    if len(subjects891) == 0:
                        pass
                        # State 128526
                        if len(subjects) == 0:
                            pass
                            # 96: tanh(v)
                            yield 96, subst1
                subjects891.appendleft(tmp905)
            if len(subjects891) >= 1 and isinstance(subjects891[0], Add):
                tmp907 = subjects891.popleft()
                associative1 = tmp907
                associative_type1 = type(tmp907)
                subjects908 = deque(tmp907._args)
                matcher = CommutativeMatcher125982.get()
                tmp909 = subjects908
                subjects908 = []
                for s in tmp909:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp909, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 125988
                        if len(subjects891) == 0:
                            pass
                            # State 125989
                            if len(subjects) == 0:
                                pass
                                # 93: tanh(x*b + a)
                                yield 93, subst1
                    if pattern_index == 1:
                        pass
                        # State 128103
                        if len(subjects891) == 0:
                            pass
                            # State 128104
                            if len(subjects) == 0:
                                pass
                                # 94: tanh(x**n*d + c)
                                yield 94, subst1
                subjects891.appendleft(tmp907)
            subjects.appendleft(tmp890)
        if len(subjects) >= 1 and isinstance(subjects[0], asinh):
            tmp910 = subjects.popleft()
            subjects911 = deque(tmp910._args)
            # State 138121
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.0', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 138122
                if len(subjects911) >= 1:
                    tmp913 = subjects911.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.0', tmp913)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 138123
                        if len(subjects911) == 0:
                            pass
                            # State 138124
                            if len(subjects) == 0:
                                pass
                                # 103: asinh(x*c)
                                yield 103, subst2
                    subjects911.appendleft(tmp913)
                if len(subjects911) >= 1:
                    tmp915 = subjects911.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.1', tmp915)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 138585
                        if len(subjects911) == 0:
                            pass
                            # State 138586
                            if len(subjects) == 0:
                                pass
                                # 106: asinh(x*c)
                                yield 106, subst2
                    subjects911.appendleft(tmp915)
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.0_1', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 139621
                if len(subjects911) >= 1:
                    tmp918 = subjects911.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.2.1.1', tmp918)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 139622
                        if len(subjects911) == 0:
                            pass
                            # State 139623
                            if len(subjects) == 0:
                                pass
                                # 107: asinh(c*x)
                                yield 107, subst2
                    subjects911.appendleft(tmp918)
            if len(subjects911) >= 1 and isinstance(subjects911[0], Mul):
                tmp920 = subjects911.popleft()
                associative1 = tmp920
                associative_type1 = type(tmp920)
                subjects921 = deque(tmp920._args)
                matcher = CommutativeMatcher138126.get()
                tmp922 = subjects921
                subjects921 = []
                for s in tmp922:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp922, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 138127
                        if len(subjects911) == 0:
                            pass
                            # State 138128
                            if len(subjects) == 0:
                                pass
                                # 103: asinh(x*c)
                                yield 103, subst1
                    if pattern_index == 1:
                        pass
                        # State 138587
                        if len(subjects911) == 0:
                            pass
                            # State 138588
                            if len(subjects) == 0:
                                pass
                                # 106: asinh(x*c)
                                yield 106, subst1
                    if pattern_index == 2:
                        pass
                        # State 139624
                        if len(subjects911) == 0:
                            pass
                            # State 139625
                            if len(subjects) == 0:
                                pass
                                # 107: asinh(c*x)
                                yield 107, subst1
                subjects911.appendleft(tmp920)
            subjects.appendleft(tmp910)
        if len(subjects) >= 1 and isinstance(subjects[0], acosh):
            tmp923 = subjects.popleft()
            subjects924 = deque(tmp923._args)
            # State 138196
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.0', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 138197
                if len(subjects924) >= 1:
                    tmp926 = subjects924.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.0', tmp926)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 138198
                        if len(subjects924) == 0:
                            pass
                            # State 138199
                            if len(subjects) == 0:
                                pass
                                # 104: acosh(x*c)
                                yield 104, subst2
                    subjects924.appendleft(tmp926)
                if len(subjects924) >= 1:
                    tmp928 = subjects924.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.1', tmp928)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 138502
                        if len(subjects924) == 0:
                            pass
                            # State 138503
                            if len(subjects) == 0:
                                pass
                                # 105: acosh(x*c)
                                yield 105, subst2
                    subjects924.appendleft(tmp928)
            if len(subjects924) >= 1 and isinstance(subjects924[0], Mul):
                tmp930 = subjects924.popleft()
                associative1 = tmp930
                associative_type1 = type(tmp930)
                subjects931 = deque(tmp930._args)
                matcher = CommutativeMatcher138201.get()
                tmp932 = subjects931
                subjects931 = []
                for s in tmp932:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp932, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 138202
                        if len(subjects924) == 0:
                            pass
                            # State 138203
                            if len(subjects) == 0:
                                pass
                                # 104: acosh(x*c)
                                yield 104, subst1
                    if pattern_index == 1:
                        pass
                        # State 138504
                        if len(subjects924) == 0:
                            pass
                            # State 138505
                            if len(subjects) == 0:
                                pass
                                # 105: acosh(x*c)
                                yield 105, subst1
                subjects924.appendleft(tmp930)
            subjects.appendleft(tmp923)
        if len(subjects) >= 1 and isinstance(subjects[0], atanh):
            tmp933 = subjects.popleft()
            subjects934 = deque(tmp933._args)
            # State 143118
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.0', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 143119
                if len(subjects934) >= 1:
                    tmp936 = subjects934.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.1', tmp936)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 143120
                        if len(subjects934) == 0:
                            pass
                            # State 143121
                            if len(subjects) == 0:
                                pass
                                # 110: atanh(x*c)
                                yield 110, subst2
                    subjects934.appendleft(tmp936)
            if len(subjects934) >= 1 and isinstance(subjects934[0], Mul):
                tmp938 = subjects934.popleft()
                associative1 = tmp938
                associative_type1 = type(tmp938)
                subjects939 = deque(tmp938._args)
                matcher = CommutativeMatcher143123.get()
                tmp940 = subjects939
                subjects939 = []
                for s in tmp940:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp940, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 143124
                        if len(subjects934) == 0:
                            pass
                            # State 143125
                            if len(subjects) == 0:
                                pass
                                # 110: atanh(x*c)
                                yield 110, subst1
                subjects934.appendleft(tmp938)
            subjects.appendleft(tmp933)
        if len(subjects) >= 1 and isinstance(subjects[0], acoth):
            tmp941 = subjects.popleft()
            subjects942 = deque(tmp941._args)
            # State 143167
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.0', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 143168
                if len(subjects942) >= 1:
                    tmp944 = subjects942.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.1', tmp944)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 143169
                        if len(subjects942) == 0:
                            pass
                            # State 143170
                            if len(subjects) == 0:
                                pass
                                # 111: acoth(x*c)
                                yield 111, subst2
                    subjects942.appendleft(tmp944)
            if len(subjects942) >= 1 and isinstance(subjects942[0], Mul):
                tmp946 = subjects942.popleft()
                associative1 = tmp946
                associative_type1 = type(tmp946)
                subjects947 = deque(tmp946._args)
                matcher = CommutativeMatcher143172.get()
                tmp948 = subjects947
                subjects947 = []
                for s in tmp948:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp948, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 143173
                        if len(subjects942) == 0:
                            pass
                            # State 143174
                            if len(subjects) == 0:
                                pass
                                # 111: acoth(x*c)
                                yield 111, subst1
                subjects942.appendleft(tmp946)
            subjects.appendleft(tmp941)
        if len(subjects) >= 1 and isinstance(subjects[0], asech):
            tmp949 = subjects.popleft()
            subjects950 = deque(tmp949._args)
            # State 149140
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.0', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 149141
                if len(subjects950) >= 1:
                    tmp952 = subjects950.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.1', tmp952)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 149142
                        if len(subjects950) == 0:
                            pass
                            # State 149143
                            if len(subjects) == 0:
                                pass
                                # 112: asech(x*c)
                                yield 112, subst2
                    subjects950.appendleft(tmp952)
            if len(subjects950) >= 1 and isinstance(subjects950[0], Mul):
                tmp954 = subjects950.popleft()
                associative1 = tmp954
                associative_type1 = type(tmp954)
                subjects955 = deque(tmp954._args)
                matcher = CommutativeMatcher149145.get()
                tmp956 = subjects955
                subjects955 = []
                for s in tmp956:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp956, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 149146
                        if len(subjects950) == 0:
                            pass
                            # State 149147
                            if len(subjects) == 0:
                                pass
                                # 112: asech(x*c)
                                yield 112, subst1
                subjects950.appendleft(tmp954)
            subjects.appendleft(tmp949)
        if len(subjects) >= 1 and isinstance(subjects[0], acsch):
            tmp957 = subjects.popleft()
            subjects958 = deque(tmp957._args)
            # State 149218
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.0', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 149219
                if len(subjects958) >= 1:
                    tmp960 = subjects958.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.1', tmp960)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 149220
                        if len(subjects958) == 0:
                            pass
                            # State 149221
                            if len(subjects) == 0:
                                pass
                                # 113: acsch(x*c)
                                yield 113, subst2
                    subjects958.appendleft(tmp960)
            if len(subjects958) >= 1 and isinstance(subjects958[0], Mul):
                tmp962 = subjects958.popleft()
                associative1 = tmp962
                associative_type1 = type(tmp962)
                subjects963 = deque(tmp962._args)
                matcher = CommutativeMatcher149223.get()
                tmp964 = subjects963
                subjects963 = []
                for s in tmp964:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp964, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 149224
                        if len(subjects958) == 0:
                            pass
                            # State 149225
                            if len(subjects) == 0:
                                pass
                                # 113: acsch(x*c)
                                yield 113, subst1
                subjects958.appendleft(tmp962)
            subjects.appendleft(tmp957)
        return
        yield


from .generated_part003688 import *
from .generated_part003679 import *
from .generated_part003542 import *
from .generated_part003539 import *
from .generated_part003662 import *
from .generated_part003667 import *
from .generated_part003580 import *
from .generated_part003669 import *
from .generated_part003677 import *
from collections import deque
from .generated_part003659 import *
from .generated_part003546 import *
from .generated_part003693 import *
from matchpy.utils import VariableWithCount
from .generated_part003585 import *
from .generated_part003593 import *
from .generated_part003587 import *
from matchpy.matching.many_to_one import CommutativeMatcher
from .generated_part003597 import *
from .generated_part003664 import *
from .generated_part003591 import *
from .generated_part003564 import *
from .generated_part003584 import *
from .generated_part003615 import *
from .generated_part003613 import *
from .generated_part003549 import *
from .generated_part003572 import *
from .generated_part003573 import *
from .generated_part003600 import *
from .generated_part003689 import *
from .generated_part003653 import *
from .generated_part003588 import *
from .generated_part003661 import *
from .generated_part003678 import *
from .generated_part003586 import *
from .generated_part003540 import *
from .generated_part003577 import *
from .generated_part003655 import *
from .generated_part003683 import *
from .generated_part003616 import *
from .generated_part003656 import *
from .generated_part003575 import *
from multiset import Multiset
from .generated_part003618 import *
from .generated_part003574 import *
from .generated_part003563 import *
from .generated_part003663 import *
from .generated_part003654 import *
from .generated_part003625 import *
from .generated_part003691 import *
from .generated_part003547 import *
from .generated_part003676 import *
from .generated_part003692 import *
from .generated_part003657 import *
from .generated_part003570 import *
from .generated_part003682 import *
from .generated_part003690 import *
from .generated_part003666 import *
from .generated_part003602 import *
from .generated_part003581 import *
from .generated_part003652 import *
from .generated_part003674 import *
from .generated_part003680 import *
from .generated_part003579 import *
from .generated_part003675 import *
from .generated_part003578 import *
from .generated_part003596 import *
from .generated_part003599 import *
from .generated_part003673 import *
from .generated_part003685 import *
from .generated_part003670 import *
from .generated_part003671 import *
from .generated_part003554 import *
from .generated_part003686 import *
from .generated_part003571 import *
from .generated_part003612 import *
from .generated_part003594 import *
from .generated_part003583 import *
from .generated_part003566 import *
from .generated_part003603 import *
from .generated_part003553 import *
from .generated_part003590 import *
from .generated_part003557 import *
from .generated_part003538 import *
from .generated_part003668 import *
from .generated_part003559 import *
from .generated_part003660 import *
from .generated_part003556 import *
from .generated_part003605 import *