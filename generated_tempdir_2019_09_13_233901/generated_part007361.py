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

class CommutativeMatcher2540(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({}), [
      (VariableWithCount('i2.1.1.0', 1, 1, None), Mul),
      (VariableWithCount('i2.1.1.0_1', 1, 1, S(1)), Mul)
]),
    1: (1, Multiset({0: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    2: (2, Multiset({}), [
      (VariableWithCount('i2.1.1.0_1', 1, 1, S(1)), Mul),
      (VariableWithCount('i2.2.0', 1, 1, None), Mul)
]),
    3: (3, Multiset({1: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    4: (4, Multiset({}), [
      (VariableWithCount('i2.1.1.0_1', 1, 1, S(1)), Mul),
      (VariableWithCount('i2.2.1.0', 1, 1, None), Mul)
]),
    5: (5, Multiset({}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul),
      (VariableWithCount('i2.2.1.1', 1, 1, None), Mul)
]),
    6: (6, Multiset({}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul),
      (VariableWithCount('i2.2.1.0', 1, 1, None), Mul)
]),
    7: (7, Multiset({}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul),
      (VariableWithCount('i2.2.0', 1, 1, None), Mul)
]),
    8: (8, Multiset({}), [
      (VariableWithCount('i2.1.1.0_1', 1, 1, S(1)), Mul),
      (VariableWithCount('i2.2.1.1', 1, 1, None), Mul)
]),
    9: (9, Multiset({}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul),
      (VariableWithCount('i2.2.0_1', 1, 1, None), Mul)
]),
    10: (10, Multiset({2: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    11: (11, Multiset({3: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    12: (12, Multiset({4: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    13: (13, Multiset({5: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    14: (14, Multiset({6: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    15: (15, Multiset({7: 1}), [
      (VariableWithCount('i2.1.1.0_1', 1, 1, S(1)), Mul)
]),
    16: (16, Multiset({7: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    17: (17, Multiset({8: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    18: (18, Multiset({9: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    19: (19, Multiset({9: 1}), [
      (VariableWithCount('i2.1.1.0_1', 1, 1, S(1)), Mul)
]),
    20: (20, Multiset({10: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    21: (21, Multiset({11: 1}), [
      (VariableWithCount('i2.1.1.0_2', 1, 1, S(1)), Mul)
]),
    22: (22, Multiset({12: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    23: (23, Multiset({13: 1}), [
      (VariableWithCount('i2.1.1.0_1', 1, 1, S(1)), Mul)
]),
    24: (24, Multiset({14: 1}), [
      (VariableWithCount('i2.1.1.0_2', 1, 1, S(1)), Mul)
]),
    25: (25, Multiset({6: 1}), [
      (VariableWithCount('i2.1.1.0_1', 1, 1, S(1)), Mul)
]),
    26: (26, Multiset({}), [
      (VariableWithCount('i2.1.1.0_2', 1, 1, S(1)), Mul),
      (VariableWithCount('i2.2.1.1', 1, 1, None), Mul)
]),
    27: (27, Multiset({8: 1}), [
      (VariableWithCount('i2.1.1.0_1', 1, 1, S(1)), Mul)
]),
    28: (28, Multiset({6: 1}), [
      (VariableWithCount('i2.1.1.0_2', 1, 1, S(1)), Mul)
]),
    29: (29, Multiset({15: 1}), [
      (VariableWithCount('i2.1.1.0_3', 1, 1, S(1)), Mul)
]),
    30: (30, Multiset({15: 1}), [
      (VariableWithCount('i2.1.1.0_2', 1, 1, S(1)), Mul)
]),
    31: (31, Multiset({16: 1}), [
      (VariableWithCount('i2.1.1.0_1', 1, 1, S(1)), Mul)
]),
    32: (32, Multiset({17: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    33: (33, Multiset({16: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    34: (34, Multiset({18: 1}), [
      (VariableWithCount('i2.1.1.0_1', 1, 1, S(1)), Mul)
]),
    35: (35, Multiset({18: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    36: (36, Multiset({19: 1}), [
      (VariableWithCount('i2.1.1.0_1', 1, 1, S(1)), Mul)
]),
    37: (37, Multiset({19: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    38: (38, Multiset({9: 1}), [
      (VariableWithCount('i2.1.1.0_2', 1, 1, S(1)), Mul)
]),
    39: (39, Multiset({11: 1}), [
      (VariableWithCount('i2.1.1.0_1', 1, 1, S(1)), Mul)
]),
    40: (40, Multiset({20: 1}), [
      (VariableWithCount('i2.1.1.0_2', 1, 1, S(1)), Mul)
]),
    41: (41, Multiset({13: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    42: (42, Multiset({14: 1}), [
      (VariableWithCount('i2.1.1.0_1', 1, 1, S(1)), Mul)
]),
    43: (43, Multiset({21: 1}), [
      (VariableWithCount('i2.1.1.0_2', 1, 1, S(1)), Mul)
]),
    44: (44, Multiset({}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul),
      (VariableWithCount('i2.2.1.2.1.1', 1, 1, None), Mul)
]),
    45: (45, Multiset({22: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    46: (46, Multiset({7: 1}), [
      (VariableWithCount('i2.1.1.0_2', 1, 1, None), Mul)
]),
    47: (47, Multiset({23: 1}), [
      (VariableWithCount('i2.1.1.0_1', 1, 1, S(1)), Mul)
]),
    48: (48, Multiset({7: 1}), [
      (VariableWithCount('i2.1.1.0_1', 1, 1, None), Mul)
]),
    49: (49, Multiset({23: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    50: (50, Multiset({7: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, None), Mul)
]),
    51: (51, Multiset({3: 1}), [
      (VariableWithCount('i2.1.1.0_1', 1, 1, S(1)), Mul)
]),
    52: (52, Multiset({24: 1}), [
      (VariableWithCount('i2.1.1.0_2', 1, 1, None), Mul)
]),
    53: (53, Multiset({24: 1}), [
      (VariableWithCount('i2.1.1.0_1', 1, 1, None), Mul)
]),
    54: (54, Multiset({25: 1, 26: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    55: (55, Multiset({}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul),
      (VariableWithCount('i2.3.1.1', 1, 1, None), Mul)
]),
    56: (56, Multiset({27: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    57: (57, Multiset({28: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    58: (58, Multiset({29: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    59: (59, Multiset({30: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    60: (60, Multiset({31: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    61: (61, Multiset({32: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    62: (62, Multiset({33: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    63: (63, Multiset({34: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    64: (64, Multiset({35: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    65: (65, Multiset({36: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    66: (66, Multiset({37: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    67: (67, Multiset({38: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    68: (68, Multiset({39: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    69: (69, Multiset({40: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    70: (70, Multiset({41: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    71: (71, Multiset({42: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    72: (72, Multiset({43: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    73: (73, Multiset({43: 1}), [
      (VariableWithCount('i2.1.1.0_1', 1, 1, S(1)), Mul)
]),
    74: (74, Multiset({44: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    75: (75, Multiset({44: 1}), [
      (VariableWithCount('i2.1.1.0_1', 1, 1, S(1)), Mul)
]),
    76: (76, Multiset({45: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    77: (77, Multiset({46: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    78: (78, Multiset({45: 1}), [
      (VariableWithCount('i2.1.1.0_1', 1, 1, S(1)), Mul)
]),
    79: (79, Multiset({46: 1}), [
      (VariableWithCount('i2.1.1.0_1', 1, 1, S(1)), Mul)
]),
    80: (80, Multiset({47: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    81: (81, Multiset({41: 1}), [
      (VariableWithCount('i2.1.1.0_1', 1, 1, S(1)), Mul)
]),
    82: (82, Multiset({48: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    83: (83, Multiset({42: 1}), [
      (VariableWithCount('i2.1.1.0_1', 1, 1, S(1)), Mul)
]),
    84: (84, Multiset({49: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    85: (85, Multiset({50: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    86: (86, Multiset({51: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    87: (87, Multiset({52: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    88: (88, Multiset({53: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    89: (89, Multiset({54: 1}), [
      (VariableWithCount('i2.1.1.0_1', 1, 1, S(1)), Mul)
]),
    90: (90, Multiset({55: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    91: (91, Multiset({56: 1}), [
      (VariableWithCount('i2.1.1.0_1', 1, 1, S(1)), Mul)
]),
    92: (92, Multiset({51: 1}), [
      (VariableWithCount('i2.1.1.0_1', 1, 1, S(1)), Mul)
]),
    93: (93, Multiset({45: 1}), [
      (VariableWithCount('i2.1.1.0_2', 1, 1, S(1)), Mul)
]),
    94: (94, Multiset({52: 1}), [
      (VariableWithCount('i2.1.1.0_1', 1, 1, S(1)), Mul)
]),
    95: (95, Multiset({46: 1}), [
      (VariableWithCount('i2.1.1.0_2', 1, 1, S(1)), Mul)
]),
    96: (96, Multiset({57: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    97: (97, Multiset({58: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    98: (98, Multiset({}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul),
      (VariableWithCount('i2.2.2.1.0', 1, 1, None), Mul)
]),
    99: (99, Multiset({59: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    100: (100, Multiset({60: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    101: (101, Multiset({61: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    102: (102, Multiset({61: 1}), [
      (VariableWithCount('i2.1.1.0_1', 1, 1, S(1)), Mul)
]),
    103: (103, Multiset({62: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    104: (104, Multiset({62: 1}), [
      (VariableWithCount('i2.1.1.0_1', 1, 1, S(1)), Mul)
]),
    105: (105, Multiset({63: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    106: (106, Multiset({64: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    107: (107, Multiset({65: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    108: (108, Multiset({63: 1}), [
      (VariableWithCount('i2.1.1.0_1', 1, 1, S(1)), Mul)
]),
    109: (109, Multiset({64: 1}), [
      (VariableWithCount('i2.1.1.0_1', 1, 1, S(1)), Mul)
]),
    110: (110, Multiset({66: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    111: (111, Multiset({67: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    112: (112, Multiset({67: 1}), [
      (VariableWithCount('i2.1.1.0_1', 1, 1, S(1)), Mul)
]),
    113: (113, Multiset({68: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    114: (114, Multiset({69: 1}), [
      (VariableWithCount('i2.1.1.0_1', 1, 1, S(1)), Mul)
]),
    115: (115, Multiset({70: 1}), [
      (VariableWithCount('i2.1.1.0_1', 1, 1, S(1)), Mul)
]),
    116: (116, Multiset({70: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    117: (117, Multiset({66: 1}), [
      (VariableWithCount('i2.1.1.0_1', 1, 1, S(1)), Mul)
]),
    118: (118, Multiset({63: 1}), [
      (VariableWithCount('i2.1.1.0_2', 1, 1, S(1)), Mul)
]),
    119: (119, Multiset({67: 1}), [
      (VariableWithCount('i2.1.1.0_2', 1, 1, S(1)), Mul)
]),
    120: (120, Multiset({71: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    121: (121, Multiset({}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul),
      (VariableWithCount('i2.2.1.2.1.0', 1, 1, None), Mul)
]),
    122: (122, Multiset({}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul),
      (VariableWithCount('i2.2.1.3.1.0', 1, 1, None), Mul)
]),
    123: (123, Multiset({72: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    124: (124, Multiset({73: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    125: (125, Multiset({74: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    126: (126, Multiset({75: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    127: (127, Multiset({76: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    128: (128, Multiset({77: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    129: (129, Multiset({77: 1}), [
      (VariableWithCount('i2.1.1.0_1', 1, 1, S(1)), Mul)
]),
    130: (130, Multiset({76: 1}), [
      (VariableWithCount('i2.1.1.0_1', 1, 1, S(1)), Mul)
]),
    131: (131, Multiset({78: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    132: (132, Multiset({79: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    133: (133, Multiset({72: 1}), [
      (VariableWithCount('i2.1.1.0_1', 1, 1, S(1)), Mul)
]),
    134: (134, Multiset({73: 1}), [
      (VariableWithCount('i2.1.1.0_1', 1, 1, S(1)), Mul)
]),
    135: (135, Multiset({80: 1}), [
      (VariableWithCount('i2.1.1.0_1', 1, 1, S(1)), Mul)
]),
    136: (136, Multiset({81: 1}), [
      (VariableWithCount('i2.1.1.0_1', 1, 1, S(1)), Mul)
]),
    137: (137, Multiset({80: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    138: (138, Multiset({81: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    139: (139, Multiset({82: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    140: (140, Multiset({83: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    141: (141, Multiset({82: 1}), [
      (VariableWithCount('i2.1.1.0_1', 1, 1, S(1)), Mul)
]),
    142: (142, Multiset({83: 1}), [
      (VariableWithCount('i2.1.1.0_1', 1, 1, S(1)), Mul)
]),
    143: (143, Multiset({84: 1}), [
      (VariableWithCount('i2.1.1.0_2', 1, 1, S(1)), Mul)
]),
    144: (144, Multiset({85: 1}), [
      (VariableWithCount('i2.1.1.0_2', 1, 1, S(1)), Mul)
]),
    145: (145, Multiset({84: 1}), [
      (VariableWithCount('i2.1.1.0_1', 1, 1, S(1)), Mul)
]),
    146: (146, Multiset({85: 1}), [
      (VariableWithCount('i2.1.1.0_1', 1, 1, S(1)), Mul)
]),
    147: (147, Multiset({86: 1}), [
      (VariableWithCount('i2.1.1.0_1', 1, 1, S(1)), Mul)
]),
    148: (148, Multiset({87: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    149: (149, Multiset({88: 1}), [
      (VariableWithCount('i2.1.1.0_1', 1, 1, S(1)), Mul)
]),
    150: (150, Multiset({86: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    151: (151, Multiset({88: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    152: (152, Multiset({89: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    153: (153, Multiset({90: 1}), [
      (VariableWithCount('i2.1.1.0_1', 1, 1, S(1)), Mul)
]),
    154: (154, Multiset({91: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    155: (155, Multiset({92: 1}), [
      (VariableWithCount('i2.1.1.0_1', 1, 1, S(1)), Mul)
]),
    156: (156, Multiset({90: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    157: (157, Multiset({92: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    158: (158, Multiset({82: 1}), [
      (VariableWithCount('i2.1.1.0_2', 1, 1, S(1)), Mul)
]),
    159: (159, Multiset({83: 1}), [
      (VariableWithCount('i2.1.1.0_2', 1, 1, S(1)), Mul)
]),
    160: (160, Multiset({}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul),
      (VariableWithCount('i2.2.3.1.0', 1, 1, None), Mul)
]),
    161: (161, Multiset({85: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    162: (162, Multiset({84: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    163: (163, Multiset({93: 1}), [
      (VariableWithCount('i2.1.1.0_1', 1, 1, S(1)), Mul)
]),
    164: (164, Multiset({94: 1}), [
      (VariableWithCount('i2.1.1.0_1', 1, 1, S(1)), Mul)
]),
    165: (165, Multiset({95: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    166: (166, Multiset({96: 1}), [
      (VariableWithCount('i2.1.1.0_1', 1, 1, S(1)), Mul)
]),
    167: (167, Multiset({97: 1}), [
      (VariableWithCount('i2.1.1.0_2', 1, 1, S(1)), Mul)
]),
    168: (168, Multiset({98: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    169: (169, Multiset({99: 1}), [
      (VariableWithCount('i2.1.1.0_1', 1, 1, S(1)), Mul)
]),
    170: (170, Multiset({100: 1}), [
      (VariableWithCount('i2.1.1.0_2', 1, 1, S(1)), Mul)
]),
    171: (171, Multiset({101: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    172: (172, Multiset({102: 1}), [
      (VariableWithCount('i2.1.1.0_1', 1, 1, S(1)), Mul)
]),
    173: (173, Multiset({103: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    174: (174, Multiset({59: 1}), [
      (VariableWithCount('i2.1.1.0_1', 1, 1, S(1)), Mul)
]),
    175: (175, Multiset({102: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    176: (176, Multiset({104: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    177: (177, Multiset({105: 1}), [
      (VariableWithCount('i2.1.1.0_1', 1, 1, S(1)), Mul)
]),
    178: (178, Multiset({106: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    179: (179, Multiset({107: 1}), [
      (VariableWithCount('i2.1.1.0_1', 1, 1, S(1)), Mul)
]),
    180: (180, Multiset({108: 1}), [
      (VariableWithCount('i2.1.1.0_2', 1, 1, S(1)), Mul)
]),
    181: (181, Multiset({109: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    182: (182, Multiset({110: 1}), [
      (VariableWithCount('i2.1.1.0_1', 1, 1, S(1)), Mul)
]),
    183: (183, Multiset({111: 1}), [
      (VariableWithCount('i2.1.1.0_2', 1, 1, S(1)), Mul)
]),
    184: (184, Multiset({56: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    185: (185, Multiset({54: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    186: (186, Multiset({112: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    187: (187, Multiset({113: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    188: (188, Multiset({114: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    189: (189, Multiset({115: 1}), [
      (VariableWithCount('i2.1.1.0_1', 1, 1, S(1)), Mul)
]),
    190: (190, Multiset({116: 1}), [
      (VariableWithCount('i2.1.1.0_2', 1, 1, S(1)), Mul)
]),
    191: (191, Multiset({117: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    192: (192, Multiset({118: 1}), [
      (VariableWithCount('i2.1.1.0_1', 1, 1, S(1)), Mul)
]),
    193: (193, Multiset({119: 1}), [
      (VariableWithCount('i2.1.1.0_2', 1, 1, S(1)), Mul)
]),
    194: (194, Multiset({120: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    195: (195, Multiset({}), [
      (VariableWithCount('i2.1.1.0_1', 1, 1, S(1)), Mul),
      (VariableWithCount('i2.2.1.2.1.0', 1, 1, None), Mul)
]),
    196: (196, Multiset({121: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    197: (197, Multiset({122: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    198: (198, Multiset({123: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    199: (199, Multiset({124: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    200: (200, Multiset({125: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    201: (201, Multiset({126: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    202: (202, Multiset({127: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    203: (203, Multiset({128: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    204: (204, Multiset({129: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    205: (205, Multiset({130: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    206: (206, Multiset({131: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    207: (207, Multiset({132: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    208: (208, Multiset({133: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    209: (209, Multiset({134: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    210: (210, Multiset({135: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    211: (211, Multiset({136: 1}), [
      (VariableWithCount('i2.1.1.0_1', 1, 1, S(1)), Mul)
]),
    212: (212, Multiset({137: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    213: (213, Multiset({138: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    214: (214, Multiset({139: 1}), [
      (VariableWithCount('i2.1.1.0_1', 1, 1, S(1)), Mul)
]),
    215: (215, Multiset({140: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    216: (216, Multiset({141: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    217: (217, Multiset({142: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    218: (218, Multiset({143: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    219: (219, Multiset({144: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    220: (220, Multiset({145: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    221: (221, Multiset({146: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    222: (222, Multiset({147: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    223: (223, Multiset({148: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    224: (224, Multiset({149: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    225: (225, Multiset({}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul),
      (VariableWithCount('i2.4.1.0', 1, 1, None), Mul)
]),
    226: (226, Multiset({150: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    227: (227, Multiset({151: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    228: (228, Multiset({151: 1}), [
      (VariableWithCount('i2.1.1.0_1', 1, 1, S(1)), Mul)
]),
    229: (229, Multiset({152: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    230: (230, Multiset({153: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    231: (231, Multiset({154: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    232: (232, Multiset({155: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    233: (233, Multiset({156: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    234: (234, Multiset({155: 1}), [
      (VariableWithCount('i2.1.1.0_1', 1, 1, S(1)), Mul)
]),
    235: (235, Multiset({157: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    236: (236, Multiset({158: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    237: (237, Multiset({159: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    238: (238, Multiset({160: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    239: (239, Multiset({161: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    240: (240, Multiset({162: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    241: (241, Multiset({163: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    242: (242, Multiset({164: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    243: (243, Multiset({165: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    244: (244, Multiset({166: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    245: (245, Multiset({167: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    246: (246, Multiset({168: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    247: (247, Multiset({169: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    248: (248, Multiset({170: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    249: (249, Multiset({171: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    250: (250, Multiset({172: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    251: (251, Multiset({173: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    252: (252, Multiset({174: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    253: (253, Multiset({175: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    254: (254, Multiset({176: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    255: (255, Multiset({177: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    256: (256, Multiset({178: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    257: (257, Multiset({179: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
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
        if CommutativeMatcher2540._instance is None:
            CommutativeMatcher2540._instance = CommutativeMatcher2540()
        return CommutativeMatcher2540._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 2539
        if len(subjects) >= 1 and isinstance(subjects[0], Pow):
            tmp1 = subjects.popleft()
            subjects2 = deque(tmp1._args)
            # State 2641
            if len(subjects2) >= 1:
                tmp3 = subjects2.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.0', tmp3)
                except ValueError:
                    pass
                else:
                    pass
                    # State 2642
                    if len(subjects2) >= 1 and subjects2[0] == 2:
                        tmp5 = subjects2.popleft()
                        # State 2643
                        if len(subjects2) == 0:
                            pass
                            # State 2644
                            if len(subjects) == 0:
                                pass
                                # 0: v**2
                        subjects2.appendleft(tmp5)
                    if len(subjects2) >= 1:
                        tmp6 = subjects2.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.1.2', tmp6)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 7209
                            if len(subjects2) == 0:
                                pass
                                # State 7210
                                if len(subjects) == 0:
                                    pass
                                    # 4: x**n
                        subjects2.appendleft(tmp6)
                    if len(subjects2) >= 1:
                        tmp8 = subjects2.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.1.1.2', tmp8)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 7252
                            if len(subjects2) == 0:
                                pass
                                # State 7253
                                if len(subjects) == 0:
                                    pass
                                    # 5: x**n
                        subjects2.appendleft(tmp8)
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.1.1.2', 1)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 11715
                        if len(subjects2) == 0:
                            pass
                            # State 11716
                            if len(subjects) == 0:
                                pass
                                # 16: x**n2
                    if len(subjects2) >= 1:
                        tmp11 = subjects2.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.1.1.2', tmp11)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 11715
                            if len(subjects2) == 0:
                                pass
                                # State 11716
                                if len(subjects) == 0:
                                    pass
                                    # 16: x**n2
                        subjects2.appendleft(tmp11)
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.2', 1)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 11722
                        if len(subjects2) == 0:
                            pass
                            # State 11723
                            if len(subjects) == 0:
                                pass
                                # 17: x**non2
                    if len(subjects2) >= 1:
                        tmp14 = subjects2.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.1.2', tmp14)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 11722
                            if len(subjects2) == 0:
                                pass
                                # State 11723
                                if len(subjects) == 0:
                                    pass
                                    # 17: x**non2
                        subjects2.appendleft(tmp14)
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.2_1', 1)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 11831
                        if len(subjects2) == 0:
                            pass
                            # State 11832
                            if len(subjects) == 0:
                                pass
                                # 19: x**n2
                    if len(subjects2) >= 1:
                        tmp17 = subjects2.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.1.2_1', tmp17)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 11831
                            if len(subjects2) == 0:
                                pass
                                # State 11832
                                if len(subjects) == 0:
                                    pass
                                    # 19: x**n2
                        subjects2.appendleft(tmp17)
                subjects2.appendleft(tmp3)
            if len(subjects2) >= 1:
                tmp19 = subjects2.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.1.0', tmp19)
                except ValueError:
                    pass
                else:
                    pass
                    # State 2655
                    if len(subjects2) >= 1 and subjects2[0] == 2:
                        tmp21 = subjects2.popleft()
                        # State 2656
                        if len(subjects2) == 0:
                            pass
                            # State 2657
                            if len(subjects) == 0:
                                pass
                                # 1: v**2
                        subjects2.appendleft(tmp21)
                subjects2.appendleft(tmp19)
            if len(subjects2) >= 1:
                tmp22 = subjects2.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.1.1', tmp22)
                except ValueError:
                    pass
                else:
                    pass
                    # State 5329
                    if len(subjects2) >= 1 and subjects2[0] == 2:
                        tmp24 = subjects2.popleft()
                        # State 5330
                        if len(subjects2) == 0:
                            pass
                            # State 5331
                            if len(subjects) == 0:
                                pass
                                # 2: x**2
                        subjects2.appendleft(tmp24)
                    if len(subjects2) >= 1:
                        tmp25 = subjects2.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.1.2', tmp25)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 6955
                            if len(subjects2) == 0:
                                pass
                                # State 6956
                                if len(subjects) == 0:
                                    pass
                                    # 3: x**j
                        subjects2.appendleft(tmp25)
                    if len(subjects2) >= 1:
                        tmp27 = subjects2.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.1.1.2', tmp27)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 8701
                            if len(subjects2) == 0:
                                pass
                                # State 8702
                                if len(subjects) == 0:
                                    pass
                                    # 7: x**n2
                        subjects2.appendleft(tmp27)
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.1.1.2', 1)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 9135
                        if len(subjects2) == 0:
                            pass
                            # State 9136
                            if len(subjects) == 0:
                                pass
                                # 9: x**m
                    if len(subjects2) >= 1:
                        tmp30 = subjects2.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.1.1.2', tmp30)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 9135
                            if len(subjects2) == 0:
                                pass
                                # State 9136
                                if len(subjects) == 0:
                                    pass
                                    # 9: x**m
                        subjects2.appendleft(tmp30)
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.2', 1)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 11303
                        if len(subjects2) == 0:
                            pass
                            # State 11304
                            if len(subjects) == 0:
                                pass
                                # 10: x**n
                    if len(subjects2) >= 1:
                        tmp33 = subjects2.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.1.2', tmp33)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 11303
                            if len(subjects2) == 0:
                                pass
                                # State 11304
                                if len(subjects) == 0:
                                    pass
                                    # 10: x**n
                        subjects2.appendleft(tmp33)
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.1.1.2_1', 1)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 11315
                        if len(subjects2) == 0:
                            pass
                            # State 11316
                            if len(subjects) == 0:
                                pass
                                # 11: x**r
                    if len(subjects2) >= 1:
                        tmp36 = subjects2.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.1.1.2_1', tmp36)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 11315
                            if len(subjects2) == 0:
                                pass
                                # State 11316
                                if len(subjects) == 0:
                                    pass
                                    # 11: x**r
                        subjects2.appendleft(tmp36)
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.2_1', 1)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 11811
                        if len(subjects2) == 0:
                            pass
                            # State 11812
                            if len(subjects) == 0:
                                pass
                                # 18: x**n
                    if len(subjects2) >= 1:
                        tmp39 = subjects2.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.1.2_1', tmp39)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 11811
                            if len(subjects2) == 0:
                                pass
                                # State 11812
                                if len(subjects) == 0:
                                    pass
                                    # 18: x**n
                        subjects2.appendleft(tmp39)
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.1.1.2_2', 1)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 11901
                        if len(subjects2) == 0:
                            pass
                            # State 11902
                            if len(subjects) == 0:
                                pass
                                # 20: x**s
                    if len(subjects2) >= 1:
                        tmp42 = subjects2.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.1.1.2_2', tmp42)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 11901
                            if len(subjects2) == 0:
                                pass
                                # State 11902
                                if len(subjects) == 0:
                                    pass
                                    # 20: x**s
                        subjects2.appendleft(tmp42)
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.2_2', 1)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 14411
                        if len(subjects2) == 0:
                            pass
                            # State 14412
                            if len(subjects) == 0:
                                pass
                                # 22: x**r
                    if len(subjects2) >= 1:
                        tmp45 = subjects2.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.1.2_2', tmp45)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 14411
                            if len(subjects2) == 0:
                                pass
                                # State 14412
                                if len(subjects) == 0:
                                    pass
                                    # 22: x**r
                        subjects2.appendleft(tmp45)
                    if len(subjects2) >= 1:
                        tmp47 = subjects2.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.1.2_1', tmp47)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 14421
                            if len(subjects2) == 0:
                                pass
                                # State 14422
                                if len(subjects) == 0:
                                    pass
                                    # 23: x**n2
                        subjects2.appendleft(tmp47)
                    if len(subjects2) >= 1:
                        tmp49 = subjects2.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.1.1.2_1', tmp49)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 14456
                            if len(subjects2) == 0:
                                pass
                                # State 14457
                                if len(subjects) == 0:
                                    pass
                                    # 24: x**n3
                        subjects2.appendleft(tmp49)
                    if len(subjects2) >= 1 and subjects2[0] == 4:
                        tmp51 = subjects2.popleft()
                        # State 7639
                        if len(subjects2) == 0:
                            pass
                            # State 7640
                            if len(subjects) == 0:
                                pass
                                # 6: x**4
                        subjects2.appendleft(tmp51)
                    if len(subjects2) >= 1 and subjects2[0] == 3:
                        tmp52 = subjects2.popleft()
                        # State 8743
                        if len(subjects2) == 0:
                            pass
                            # State 8744
                            if len(subjects) == 0:
                                pass
                                # 8: x**3
                        subjects2.appendleft(tmp52)
                    if len(subjects2) >= 1 and subjects2[0] == 6:
                        tmp53 = subjects2.popleft()
                        # State 11443
                        if len(subjects2) == 0:
                            pass
                            # State 11444
                            if len(subjects) == 0:
                                pass
                                # 15: x**6
                        subjects2.appendleft(tmp53)
                subjects2.appendleft(tmp22)
            if len(subjects2) >= 1:
                tmp54 = subjects2.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.0_1', tmp54)
                except ValueError:
                    pass
                else:
                    pass
                    # State 11329
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.2', 1)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 11330
                        if len(subjects2) == 0:
                            pass
                            # State 11331
                            if len(subjects) == 0:
                                pass
                                # 12: x**mn
                    if len(subjects2) >= 1:
                        tmp57 = subjects2.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.1.2', tmp57)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 11330
                            if len(subjects2) == 0:
                                pass
                                # State 11331
                                if len(subjects) == 0:
                                    pass
                                    # 12: x**mn
                        subjects2.appendleft(tmp57)
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.1.1.2', 1)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 11338
                        if len(subjects2) == 0:
                            pass
                            # State 11339
                            if len(subjects) == 0:
                                pass
                                # 13: x**q
                    if len(subjects2) >= 1:
                        tmp60 = subjects2.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.1.1.2', tmp60)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 11338
                            if len(subjects2) == 0:
                                pass
                                # State 11339
                                if len(subjects) == 0:
                                    pass
                                    # 13: x**q
                        subjects2.appendleft(tmp60)
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.1.1.2_1', 1)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 11346
                        if len(subjects2) == 0:
                            pass
                            # State 11347
                            if len(subjects) == 0:
                                pass
                                # 14: x**r
                    if len(subjects2) >= 1:
                        tmp63 = subjects2.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.1.1.2_1', tmp63)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 11346
                            if len(subjects2) == 0:
                                pass
                                # State 11347
                                if len(subjects) == 0:
                                    pass
                                    # 14: x**r
                        subjects2.appendleft(tmp63)
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.1.1.2_2', 1)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 11923
                        if len(subjects2) == 0:
                            pass
                            # State 11924
                            if len(subjects) == 0:
                                pass
                                # 21: x**s
                    if len(subjects2) >= 1:
                        tmp66 = subjects2.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.1.1.2_2', tmp66)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 11923
                            if len(subjects2) == 0:
                                pass
                                # State 11924
                                if len(subjects) == 0:
                                    pass
                                    # 21: x**s
                        subjects2.appendleft(tmp66)
                subjects2.appendleft(tmp54)
            if len(subjects2) >= 1:
                tmp68 = subjects2.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.1.1.1', tmp68)
                except ValueError:
                    pass
                else:
                    pass
                    # State 101626
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.1.1.3.0', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 101627
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.1.1.3.1.0', S(0))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 101628
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i2.1.1.3.1.1.0_1', S(1))
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 101629
                                if len(subjects2) >= 1:
                                    tmp73 = subjects2.popleft()
                                    subst5 = Substitution(subst4)
                                    try:
                                        subst5.try_add_variable('i2.1.1.3.1.1.0', tmp73)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 101630
                                        if len(subjects2) == 0:
                                            pass
                                            # State 101631
                                            if len(subjects) == 0:
                                                pass
                                                # 120: F**(c*(a + x*b))
                                    subjects2.appendleft(tmp73)
                            if len(subjects2) >= 1 and isinstance(subjects2[0], Mul):
                                tmp75 = subjects2.popleft()
                                associative1 = tmp75
                                associative_type1 = type(tmp75)
                                subjects76 = deque(tmp75._args)
                                matcher = CommutativeMatcher101633.get()
                                tmp77 = subjects76
                                subjects76 = []
                                for s in tmp77:
                                    matcher.add_subject(s)
                                for pattern_index, subst4 in matcher.match(tmp77, subst3):
                                    pass
                                    if pattern_index == 0:
                                        pass
                                        # State 101634
                                        if len(subjects2) == 0:
                                            pass
                                            # State 101635
                                            if len(subjects) == 0:
                                                pass
                                                # 120: F**(c*(a + x*b))
                                subjects2.appendleft(tmp75)
                        if len(subjects2) >= 1 and isinstance(subjects2[0], Add):
                            tmp78 = subjects2.popleft()
                            associative1 = tmp78
                            associative_type1 = type(tmp78)
                            subjects79 = deque(tmp78._args)
                            matcher = CommutativeMatcher101637.get()
                            tmp80 = subjects79
                            subjects79 = []
                            for s in tmp80:
                                matcher.add_subject(s)
                            for pattern_index, subst3 in matcher.match(tmp80, subst2):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 101643
                                    if len(subjects2) == 0:
                                        pass
                                        # State 101644
                                        if len(subjects) == 0:
                                            pass
                                            # 120: F**(c*(a + x*b))
                            subjects2.appendleft(tmp78)
                    if len(subjects2) >= 1:
                        tmp81 = subjects2.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.1.1.2', tmp81)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 151740
                            if len(subjects2) == 0:
                                pass
                                # State 151741
                                if len(subjects) == 0:
                                    pass
                                    # 178: y**n
                        subjects2.appendleft(tmp81)
                    if len(subjects2) >= 1:
                        tmp83 = subjects2.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.1.2', tmp83)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 151804
                            if len(subjects2) == 0:
                                pass
                                # State 151805
                                if len(subjects) == 0:
                                    pass
                                    # 179: y**n
                        subjects2.appendleft(tmp83)
                    if len(subjects2) >= 1 and isinstance(subjects2[0], Mul):
                        tmp85 = subjects2.popleft()
                        associative1 = tmp85
                        associative_type1 = type(tmp85)
                        subjects86 = deque(tmp85._args)
                        matcher = CommutativeMatcher101646.get()
                        tmp87 = subjects86
                        subjects86 = []
                        for s in tmp87:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp87, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 101661
                                if len(subjects2) == 0:
                                    pass
                                    # State 101662
                                    if len(subjects) == 0:
                                        pass
                                        # 120: F**(c*(a + x*b))
                        subjects2.appendleft(tmp85)
                subjects2.appendleft(tmp68)
            if len(subjects2) >= 1 and isinstance(subjects2[0], sin):
                tmp88 = subjects2.popleft()
                subjects89 = deque(tmp88._args)
                # State 65537
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.2.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 65538
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.2.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 65539
                        if len(subjects89) >= 1:
                            tmp92 = subjects89.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.2.1.0', tmp92)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 65540
                                if len(subjects89) == 0:
                                    pass
                                    # State 65541
                                    if len(subjects2) >= 1 and subjects2[0] == 2:
                                        tmp94 = subjects2.popleft()
                                        # State 65542
                                        if len(subjects2) == 0:
                                            pass
                                            # State 65543
                                            if len(subjects) == 0:
                                                pass
                                                # 47: sin(e + x*f)**2
                                        subjects2.appendleft(tmp94)
                                    if len(subjects2) >= 1 and subjects2[0] == -1:
                                        tmp95 = subjects2.popleft()
                                        # State 93982
                                        if len(subjects2) == 0:
                                            pass
                                            # State 93983
                                            if len(subjects) == 0:
                                                pass
                                                # 87: 1/sin(e + x*f)
                                        subjects2.appendleft(tmp95)
                                    if len(subjects2) >= 1 and subjects2[0] == -2:
                                        tmp96 = subjects2.popleft()
                                        # State 94008
                                        if len(subjects2) == 0:
                                            pass
                                            # State 94009
                                            if len(subjects) == 0:
                                                pass
                                                # 88: sin(e + x*f)**(-2)
                                        subjects2.appendleft(tmp96)
                            subjects89.appendleft(tmp92)
                    if len(subjects89) >= 1 and isinstance(subjects89[0], Mul):
                        tmp97 = subjects89.popleft()
                        associative1 = tmp97
                        associative_type1 = type(tmp97)
                        subjects98 = deque(tmp97._args)
                        matcher = CommutativeMatcher65545.get()
                        tmp99 = subjects98
                        subjects98 = []
                        for s in tmp99:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp99, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 65546
                                if len(subjects89) == 0:
                                    pass
                                    # State 65547
                                    if len(subjects2) >= 1 and subjects2[0] == 2:
                                        tmp100 = subjects2.popleft()
                                        # State 65548
                                        if len(subjects2) == 0:
                                            pass
                                            # State 65549
                                            if len(subjects) == 0:
                                                pass
                                                # 47: sin(e + x*f)**2
                                        subjects2.appendleft(tmp100)
                                    if len(subjects2) >= 1 and subjects2[0] == -1:
                                        tmp101 = subjects2.popleft()
                                        # State 93984
                                        if len(subjects2) == 0:
                                            pass
                                            # State 93985
                                            if len(subjects) == 0:
                                                pass
                                                # 87: 1/sin(e + x*f)
                                        subjects2.appendleft(tmp101)
                                    if len(subjects2) >= 1 and subjects2[0] == -2:
                                        tmp102 = subjects2.popleft()
                                        # State 94010
                                        if len(subjects2) == 0:
                                            pass
                                            # State 94011
                                            if len(subjects) == 0:
                                                pass
                                                # 88: sin(e + x*f)**(-2)
                                        subjects2.appendleft(tmp102)
                        subjects89.appendleft(tmp97)
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.3.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 65698
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.3.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 65699
                        if len(subjects89) >= 1:
                            tmp105 = subjects89.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.3.1.0', tmp105)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 65700
                                if len(subjects89) == 0:
                                    pass
                                    # State 65701
                                    if len(subjects2) >= 1 and subjects2[0] == 2:
                                        tmp107 = subjects2.popleft()
                                        # State 65702
                                        if len(subjects2) == 0:
                                            pass
                                            # State 65703
                                            if len(subjects) == 0:
                                                pass
                                                # 49: sin(e + x*f)**2
                                        subjects2.appendleft(tmp107)
                            subjects89.appendleft(tmp105)
                    if len(subjects89) >= 1 and isinstance(subjects89[0], Mul):
                        tmp108 = subjects89.popleft()
                        associative1 = tmp108
                        associative_type1 = type(tmp108)
                        subjects109 = deque(tmp108._args)
                        matcher = CommutativeMatcher65705.get()
                        tmp110 = subjects109
                        subjects109 = []
                        for s in tmp110:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp110, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 65706
                                if len(subjects89) == 0:
                                    pass
                                    # State 65707
                                    if len(subjects2) >= 1 and subjects2[0] == 2:
                                        tmp111 = subjects2.popleft()
                                        # State 65708
                                        if len(subjects2) == 0:
                                            pass
                                            # State 65709
                                            if len(subjects) == 0:
                                                pass
                                                # 49: sin(e + x*f)**2
                                        subjects2.appendleft(tmp111)
                        subjects89.appendleft(tmp108)
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.1.2.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 65836
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.2.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 65837
                        if len(subjects89) >= 1:
                            tmp114 = subjects89.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.2.1.0', tmp114)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 65838
                                if len(subjects89) == 0:
                                    pass
                                    # State 65839
                                    if len(subjects2) >= 1 and subjects2[0] == 2:
                                        tmp116 = subjects2.popleft()
                                        # State 65840
                                        if len(subjects2) == 0:
                                            pass
                                            # State 65841
                                            if len(subjects) == 0:
                                                pass
                                                # 51: sin(c + x*d)**2
                                        subjects2.appendleft(tmp116)
                            subjects89.appendleft(tmp114)
                    if len(subjects89) >= 1 and isinstance(subjects89[0], Mul):
                        tmp117 = subjects89.popleft()
                        associative1 = tmp117
                        associative_type1 = type(tmp117)
                        subjects118 = deque(tmp117._args)
                        matcher = CommutativeMatcher65843.get()
                        tmp119 = subjects118
                        subjects118 = []
                        for s in tmp119:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp119, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 65844
                                if len(subjects89) == 0:
                                    pass
                                    # State 65845
                                    if len(subjects2) >= 1 and subjects2[0] == 2:
                                        tmp120 = subjects2.popleft()
                                        # State 65846
                                        if len(subjects2) == 0:
                                            pass
                                            # State 65847
                                            if len(subjects) == 0:
                                                pass
                                                # 51: sin(c + x*d)**2
                                        subjects2.appendleft(tmp120)
                        subjects89.appendleft(tmp117)
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.3.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 66097
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.3.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 66098
                        if len(subjects89) >= 1:
                            tmp123 = subjects89.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.3.1.0', tmp123)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 66099
                                if len(subjects89) == 0:
                                    pass
                                    # State 66100
                                    if len(subjects2) >= 1 and subjects2[0] == 2:
                                        tmp125 = subjects2.popleft()
                                        # State 66101
                                        if len(subjects2) == 0:
                                            pass
                                            # State 66102
                                            if len(subjects) == 0:
                                                pass
                                                # 53: sin(e + x*f)**2
                                        subjects2.appendleft(tmp125)
                                    if len(subjects2) >= 1 and subjects2[0] == -1:
                                        tmp126 = subjects2.popleft()
                                        # State 90162
                                        if len(subjects2) == 0:
                                            pass
                                            # State 90163
                                            if len(subjects) == 0:
                                                pass
                                                # 73: 1/sin(e + x*f)
                                        subjects2.appendleft(tmp126)
                                    if len(subjects2) >= 1 and subjects2[0] == -2:
                                        tmp127 = subjects2.popleft()
                                        # State 93619
                                        if len(subjects2) == 0:
                                            pass
                                            # State 93620
                                            if len(subjects) == 0:
                                                pass
                                                # 83: sin(e + x*f)**(-2)
                                        subjects2.appendleft(tmp127)
                            subjects89.appendleft(tmp123)
                    if len(subjects89) >= 1 and isinstance(subjects89[0], Mul):
                        tmp128 = subjects89.popleft()
                        associative1 = tmp128
                        associative_type1 = type(tmp128)
                        subjects129 = deque(tmp128._args)
                        matcher = CommutativeMatcher66104.get()
                        tmp130 = subjects129
                        subjects129 = []
                        for s in tmp130:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp130, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 66105
                                if len(subjects89) == 0:
                                    pass
                                    # State 66106
                                    if len(subjects2) >= 1 and subjects2[0] == 2:
                                        tmp131 = subjects2.popleft()
                                        # State 66107
                                        if len(subjects2) == 0:
                                            pass
                                            # State 66108
                                            if len(subjects) == 0:
                                                pass
                                                # 53: sin(e + x*f)**2
                                        subjects2.appendleft(tmp131)
                                    if len(subjects2) >= 1 and subjects2[0] == -1:
                                        tmp132 = subjects2.popleft()
                                        # State 90164
                                        if len(subjects2) == 0:
                                            pass
                                            # State 90165
                                            if len(subjects) == 0:
                                                pass
                                                # 73: 1/sin(e + x*f)
                                        subjects2.appendleft(tmp132)
                                    if len(subjects2) >= 1 and subjects2[0] == -2:
                                        tmp133 = subjects2.popleft()
                                        # State 93621
                                        if len(subjects2) == 0:
                                            pass
                                            # State 93622
                                            if len(subjects) == 0:
                                                pass
                                                # 83: sin(e + x*f)**(-2)
                                        subjects2.appendleft(tmp133)
                        subjects89.appendleft(tmp128)
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.1.1.3.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 90909
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.1.1.3.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 90910
                        if len(subjects89) >= 1:
                            tmp136 = subjects89.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.1.1.3.1.0', tmp136)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 90911
                                if len(subjects89) == 0:
                                    pass
                                    # State 90912
                                    if len(subjects2) >= 1 and subjects2[0] == -1:
                                        tmp138 = subjects2.popleft()
                                        # State 90913
                                        if len(subjects2) == 0:
                                            pass
                                            # State 90914
                                            if len(subjects) == 0:
                                                pass
                                                # 76: 1/sin(c + x*d)
                                        subjects2.appendleft(tmp138)
                                    if len(subjects2) >= 1 and subjects2[0] == -2:
                                        tmp139 = subjects2.popleft()
                                        # State 93731
                                        if len(subjects2) == 0:
                                            pass
                                            # State 93732
                                            if len(subjects) == 0:
                                                pass
                                                # 85: sin(c + x*d)**(-2)
                                        subjects2.appendleft(tmp139)
                                    if len(subjects2) >= 1:
                                        tmp140 = subjects2.popleft()
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.1.1.3', tmp140)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 99728
                                            if len(subjects2) == 0:
                                                pass
                                                # State 99729
                                                if len(subjects) == 0:
                                                    pass
                                                    # 95: sin(c + x*d)**n1
                                        subjects2.appendleft(tmp140)
                                    if len(subjects2) >= 1:
                                        tmp142 = subjects2.popleft()
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.1.1.3_1', tmp142)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 99741
                                            if len(subjects2) == 0:
                                                pass
                                                # State 99742
                                                if len(subjects) == 0:
                                                    pass
                                                    # 96: sin(c + x*d)**n2
                                        subjects2.appendleft(tmp142)
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i2.1.1.3_2', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 99792
                                        if len(subjects2) == 0:
                                            pass
                                            # State 99793
                                            if len(subjects) == 0:
                                                pass
                                                # 97: sin(c + x*d)**n
                                    if len(subjects2) >= 1:
                                        tmp145 = subjects2.popleft()
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.1.1.3_2', tmp145)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 99792
                                            if len(subjects2) == 0:
                                                pass
                                                # State 99793
                                                if len(subjects) == 0:
                                                    pass
                                                    # 97: sin(c + x*d)**n
                                        subjects2.appendleft(tmp145)
                                    if len(subjects2) >= 1 and subjects2[0] == 2:
                                        tmp147 = subjects2.popleft()
                                        # State 100477
                                        if len(subjects2) == 0:
                                            pass
                                            # State 100478
                                            if len(subjects) == 0:
                                                pass
                                                # 113: sin(c + x*d)**2
                                        subjects2.appendleft(tmp147)
                            subjects89.appendleft(tmp136)
                    if len(subjects89) >= 1 and isinstance(subjects89[0], Mul):
                        tmp148 = subjects89.popleft()
                        associative1 = tmp148
                        associative_type1 = type(tmp148)
                        subjects149 = deque(tmp148._args)
                        matcher = CommutativeMatcher90916.get()
                        tmp150 = subjects149
                        subjects149 = []
                        for s in tmp150:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp150, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 90917
                                if len(subjects89) == 0:
                                    pass
                                    # State 90918
                                    if len(subjects2) >= 1 and subjects2[0] == -1:
                                        tmp151 = subjects2.popleft()
                                        # State 90919
                                        if len(subjects2) == 0:
                                            pass
                                            # State 90920
                                            if len(subjects) == 0:
                                                pass
                                                # 76: 1/sin(c + x*d)
                                        subjects2.appendleft(tmp151)
                                    if len(subjects2) >= 1 and subjects2[0] == -2:
                                        tmp152 = subjects2.popleft()
                                        # State 93733
                                        if len(subjects2) == 0:
                                            pass
                                            # State 93734
                                            if len(subjects) == 0:
                                                pass
                                                # 85: sin(c + x*d)**(-2)
                                        subjects2.appendleft(tmp152)
                                    if len(subjects2) >= 1:
                                        tmp153 = subjects2.popleft()
                                        subst3 = Substitution(subst2)
                                        try:
                                            subst3.try_add_variable('i2.1.1.3', tmp153)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 99730
                                            if len(subjects2) == 0:
                                                pass
                                                # State 99731
                                                if len(subjects) == 0:
                                                    pass
                                                    # 95: sin(c + x*d)**n1
                                        subjects2.appendleft(tmp153)
                                    if len(subjects2) >= 1:
                                        tmp155 = subjects2.popleft()
                                        subst3 = Substitution(subst2)
                                        try:
                                            subst3.try_add_variable('i2.1.1.3_1', tmp155)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 99743
                                            if len(subjects2) == 0:
                                                pass
                                                # State 99744
                                                if len(subjects) == 0:
                                                    pass
                                                    # 96: sin(c + x*d)**n2
                                        subjects2.appendleft(tmp155)
                                    subst3 = Substitution(subst2)
                                    try:
                                        subst3.try_add_variable('i2.1.1.3_2', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 99794
                                        if len(subjects2) == 0:
                                            pass
                                            # State 99795
                                            if len(subjects) == 0:
                                                pass
                                                # 97: sin(c + x*d)**n
                                    if len(subjects2) >= 1:
                                        tmp158 = subjects2.popleft()
                                        subst3 = Substitution(subst2)
                                        try:
                                            subst3.try_add_variable('i2.1.1.3_2', tmp158)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 99794
                                            if len(subjects2) == 0:
                                                pass
                                                # State 99795
                                                if len(subjects) == 0:
                                                    pass
                                                    # 97: sin(c + x*d)**n
                                        subjects2.appendleft(tmp158)
                                    if len(subjects2) >= 1 and subjects2[0] == 2:
                                        tmp160 = subjects2.popleft()
                                        # State 100479
                                        if len(subjects2) == 0:
                                            pass
                                            # State 100480
                                            if len(subjects) == 0:
                                                pass
                                                # 113: sin(c + x*d)**2
                                        subjects2.appendleft(tmp160)
                        subjects89.appendleft(tmp148)
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.1.3.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 91571
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.3.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 91572
                        if len(subjects89) >= 1:
                            tmp163 = subjects89.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.3.1.0', tmp163)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 91573
                                if len(subjects89) == 0:
                                    pass
                                    # State 91574
                                    if len(subjects2) >= 1 and subjects2[0] == -1:
                                        tmp165 = subjects2.popleft()
                                        # State 91575
                                        if len(subjects2) == 0:
                                            pass
                                            # State 91576
                                            if len(subjects) == 0:
                                                pass
                                                # 79: 1/sin(e + x*f)
                                        subjects2.appendleft(tmp165)
                                    if len(subjects2) >= 1 and subjects2[0] == -2:
                                        tmp166 = subjects2.popleft()
                                        # State 93485
                                        if len(subjects2) == 0:
                                            pass
                                            # State 93486
                                            if len(subjects) == 0:
                                                pass
                                                # 81: sin(e + x*f)**(-2)
                                        subjects2.appendleft(tmp166)
                            subjects89.appendleft(tmp163)
                    if len(subjects89) >= 1 and isinstance(subjects89[0], Mul):
                        tmp167 = subjects89.popleft()
                        associative1 = tmp167
                        associative_type1 = type(tmp167)
                        subjects168 = deque(tmp167._args)
                        matcher = CommutativeMatcher91578.get()
                        tmp169 = subjects168
                        subjects168 = []
                        for s in tmp169:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp169, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 91579
                                if len(subjects89) == 0:
                                    pass
                                    # State 91580
                                    if len(subjects2) >= 1 and subjects2[0] == -1:
                                        tmp170 = subjects2.popleft()
                                        # State 91581
                                        if len(subjects2) == 0:
                                            pass
                                            # State 91582
                                            if len(subjects) == 0:
                                                pass
                                                # 79: 1/sin(e + x*f)
                                        subjects2.appendleft(tmp170)
                                    if len(subjects2) >= 1 and subjects2[0] == -2:
                                        tmp171 = subjects2.popleft()
                                        # State 93487
                                        if len(subjects2) == 0:
                                            pass
                                            # State 93488
                                            if len(subjects) == 0:
                                                pass
                                                # 81: sin(e + x*f)**(-2)
                                        subjects2.appendleft(tmp171)
                        subjects89.appendleft(tmp167)
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.2.3.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 94155
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.2.3.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 94156
                        if len(subjects89) >= 1:
                            tmp174 = subjects89.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.2.3.1.0', tmp174)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 94157
                                if len(subjects89) == 0:
                                    pass
                                    # State 94158
                                    if len(subjects2) >= 1 and subjects2[0] == -1:
                                        tmp176 = subjects2.popleft()
                                        # State 94159
                                        if len(subjects2) == 0:
                                            pass
                                            # State 94160
                                            if len(subjects) == 0:
                                                pass
                                                # 91: 1/sin(e + x*f)
                                        subjects2.appendleft(tmp176)
                                    if len(subjects2) >= 1 and subjects2[0] == -2:
                                        tmp177 = subjects2.popleft()
                                        # State 94194
                                        if len(subjects2) == 0:
                                            pass
                                            # State 94195
                                            if len(subjects) == 0:
                                                pass
                                                # 92: sin(e + x*f)**(-2)
                                        subjects2.appendleft(tmp177)
                            subjects89.appendleft(tmp174)
                    if len(subjects89) >= 1 and isinstance(subjects89[0], Mul):
                        tmp178 = subjects89.popleft()
                        associative1 = tmp178
                        associative_type1 = type(tmp178)
                        subjects179 = deque(tmp178._args)
                        matcher = CommutativeMatcher94162.get()
                        tmp180 = subjects179
                        subjects179 = []
                        for s in tmp180:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp180, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 94163
                                if len(subjects89) == 0:
                                    pass
                                    # State 94164
                                    if len(subjects2) >= 1 and subjects2[0] == -1:
                                        tmp181 = subjects2.popleft()
                                        # State 94165
                                        if len(subjects2) == 0:
                                            pass
                                            # State 94166
                                            if len(subjects) == 0:
                                                pass
                                                # 91: 1/sin(e + x*f)
                                        subjects2.appendleft(tmp181)
                                    if len(subjects2) >= 1 and subjects2[0] == -2:
                                        tmp182 = subjects2.popleft()
                                        # State 94196
                                        if len(subjects2) == 0:
                                            pass
                                            # State 94197
                                            if len(subjects) == 0:
                                                pass
                                                # 92: sin(e + x*f)**(-2)
                                        subjects2.appendleft(tmp182)
                        subjects89.appendleft(tmp178)
                if len(subjects89) >= 1 and isinstance(subjects89[0], Add):
                    tmp183 = subjects89.popleft()
                    associative1 = tmp183
                    associative_type1 = type(tmp183)
                    subjects184 = deque(tmp183._args)
                    matcher = CommutativeMatcher65551.get()
                    tmp185 = subjects184
                    subjects184 = []
                    for s in tmp185:
                        matcher.add_subject(s)
                    for pattern_index, subst1 in matcher.match(tmp185, subst0):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 65557
                            if len(subjects89) == 0:
                                pass
                                # State 65558
                                if len(subjects2) >= 1 and subjects2[0] == 2:
                                    tmp186 = subjects2.popleft()
                                    # State 65559
                                    if len(subjects2) == 0:
                                        pass
                                        # State 65560
                                        if len(subjects) == 0:
                                            pass
                                            # 47: sin(e + x*f)**2
                                    subjects2.appendleft(tmp186)
                                if len(subjects2) >= 1 and subjects2[0] == -1:
                                    tmp187 = subjects2.popleft()
                                    # State 93986
                                    if len(subjects2) == 0:
                                        pass
                                        # State 93987
                                        if len(subjects) == 0:
                                            pass
                                            # 87: 1/sin(e + x*f)
                                    subjects2.appendleft(tmp187)
                                if len(subjects2) >= 1 and subjects2[0] == -2:
                                    tmp188 = subjects2.popleft()
                                    # State 94012
                                    if len(subjects2) == 0:
                                        pass
                                        # State 94013
                                        if len(subjects) == 0:
                                            pass
                                            # 88: sin(e + x*f)**(-2)
                                    subjects2.appendleft(tmp188)
                        if pattern_index == 1:
                            pass
                            # State 65713
                            if len(subjects89) == 0:
                                pass
                                # State 65714
                                if len(subjects2) >= 1 and subjects2[0] == 2:
                                    tmp189 = subjects2.popleft()
                                    # State 65715
                                    if len(subjects2) == 0:
                                        pass
                                        # State 65716
                                        if len(subjects) == 0:
                                            pass
                                            # 49: sin(e + x*f)**2
                                    subjects2.appendleft(tmp189)
                        if pattern_index == 2:
                            pass
                            # State 65851
                            if len(subjects89) == 0:
                                pass
                                # State 65852
                                if len(subjects2) >= 1 and subjects2[0] == 2:
                                    tmp190 = subjects2.popleft()
                                    # State 65853
                                    if len(subjects2) == 0:
                                        pass
                                        # State 65854
                                        if len(subjects) == 0:
                                            pass
                                            # 51: sin(c + x*d)**2
                                    subjects2.appendleft(tmp190)
                        if pattern_index == 3:
                            pass
                            # State 66112
                            if len(subjects89) == 0:
                                pass
                                # State 66113
                                if len(subjects2) >= 1 and subjects2[0] == 2:
                                    tmp191 = subjects2.popleft()
                                    # State 66114
                                    if len(subjects2) == 0:
                                        pass
                                        # State 66115
                                        if len(subjects) == 0:
                                            pass
                                            # 53: sin(e + x*f)**2
                                    subjects2.appendleft(tmp191)
                                if len(subjects2) >= 1 and subjects2[0] == -1:
                                    tmp192 = subjects2.popleft()
                                    # State 90166
                                    if len(subjects2) == 0:
                                        pass
                                        # State 90167
                                        if len(subjects) == 0:
                                            pass
                                            # 73: 1/sin(e + x*f)
                                    subjects2.appendleft(tmp192)
                                if len(subjects2) >= 1 and subjects2[0] == -2:
                                    tmp193 = subjects2.popleft()
                                    # State 93623
                                    if len(subjects2) == 0:
                                        pass
                                        # State 93624
                                        if len(subjects) == 0:
                                            pass
                                            # 83: sin(e + x*f)**(-2)
                                    subjects2.appendleft(tmp193)
                        if pattern_index == 4:
                            pass
                            # State 90924
                            if len(subjects89) == 0:
                                pass
                                # State 90925
                                if len(subjects2) >= 1 and subjects2[0] == -1:
                                    tmp194 = subjects2.popleft()
                                    # State 90926
                                    if len(subjects2) == 0:
                                        pass
                                        # State 90927
                                        if len(subjects) == 0:
                                            pass
                                            # 76: 1/sin(c + x*d)
                                    subjects2.appendleft(tmp194)
                                if len(subjects2) >= 1 and subjects2[0] == -2:
                                    tmp195 = subjects2.popleft()
                                    # State 93735
                                    if len(subjects2) == 0:
                                        pass
                                        # State 93736
                                        if len(subjects) == 0:
                                            pass
                                            # 85: sin(c + x*d)**(-2)
                                    subjects2.appendleft(tmp195)
                                if len(subjects2) >= 1:
                                    tmp196 = subjects2.popleft()
                                    subst2 = Substitution(subst1)
                                    try:
                                        subst2.try_add_variable('i2.1.1.3', tmp196)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 99732
                                        if len(subjects2) == 0:
                                            pass
                                            # State 99733
                                            if len(subjects) == 0:
                                                pass
                                                # 95: sin(c + x*d)**n1
                                    subjects2.appendleft(tmp196)
                                if len(subjects2) >= 1:
                                    tmp198 = subjects2.popleft()
                                    subst2 = Substitution(subst1)
                                    try:
                                        subst2.try_add_variable('i2.1.1.3_1', tmp198)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 99745
                                        if len(subjects2) == 0:
                                            pass
                                            # State 99746
                                            if len(subjects) == 0:
                                                pass
                                                # 96: sin(c + x*d)**n2
                                    subjects2.appendleft(tmp198)
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i2.1.1.3_2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 99796
                                    if len(subjects2) == 0:
                                        pass
                                        # State 99797
                                        if len(subjects) == 0:
                                            pass
                                            # 97: sin(c + x*d)**n
                                if len(subjects2) >= 1:
                                    tmp201 = subjects2.popleft()
                                    subst2 = Substitution(subst1)
                                    try:
                                        subst2.try_add_variable('i2.1.1.3_2', tmp201)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 99796
                                        if len(subjects2) == 0:
                                            pass
                                            # State 99797
                                            if len(subjects) == 0:
                                                pass
                                                # 97: sin(c + x*d)**n
                                    subjects2.appendleft(tmp201)
                                if len(subjects2) >= 1 and subjects2[0] == 2:
                                    tmp203 = subjects2.popleft()
                                    # State 100481
                                    if len(subjects2) == 0:
                                        pass
                                        # State 100482
                                        if len(subjects) == 0:
                                            pass
                                            # 113: sin(c + x*d)**2
                                    subjects2.appendleft(tmp203)
                        if pattern_index == 5:
                            pass
                            # State 91586
                            if len(subjects89) == 0:
                                pass
                                # State 91587
                                if len(subjects2) >= 1 and subjects2[0] == -1:
                                    tmp204 = subjects2.popleft()
                                    # State 91588
                                    if len(subjects2) == 0:
                                        pass
                                        # State 91589
                                        if len(subjects) == 0:
                                            pass
                                            # 79: 1/sin(e + x*f)
                                    subjects2.appendleft(tmp204)
                                if len(subjects2) >= 1 and subjects2[0] == -2:
                                    tmp205 = subjects2.popleft()
                                    # State 93489
                                    if len(subjects2) == 0:
                                        pass
                                        # State 93490
                                        if len(subjects) == 0:
                                            pass
                                            # 81: sin(e + x*f)**(-2)
                                    subjects2.appendleft(tmp205)
                        if pattern_index == 6:
                            pass
                            # State 94170
                            if len(subjects89) == 0:
                                pass
                                # State 94171
                                if len(subjects2) >= 1 and subjects2[0] == -1:
                                    tmp206 = subjects2.popleft()
                                    # State 94172
                                    if len(subjects2) == 0:
                                        pass
                                        # State 94173
                                        if len(subjects) == 0:
                                            pass
                                            # 91: 1/sin(e + x*f)
                                    subjects2.appendleft(tmp206)
                                if len(subjects2) >= 1 and subjects2[0] == -2:
                                    tmp207 = subjects2.popleft()
                                    # State 94198
                                    if len(subjects2) == 0:
                                        pass
                                        # State 94199
                                        if len(subjects) == 0:
                                            pass
                                            # 92: sin(e + x*f)**(-2)
                                    subjects2.appendleft(tmp207)
                    subjects89.appendleft(tmp183)
                subjects2.appendleft(tmp88)
            if len(subjects2) >= 1 and isinstance(subjects2[0], cos):
                tmp208 = subjects2.popleft()
                subjects209 = deque(tmp208._args)
                # State 65604
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.2.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 65605
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.2.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 65606
                        if len(subjects209) >= 1:
                            tmp212 = subjects209.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.2.1.0', tmp212)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 65607
                                if len(subjects209) == 0:
                                    pass
                                    # State 65608
                                    if len(subjects2) >= 1 and subjects2[0] == 2:
                                        tmp214 = subjects2.popleft()
                                        # State 65609
                                        if len(subjects2) == 0:
                                            pass
                                            # State 65610
                                            if len(subjects) == 0:
                                                pass
                                                # 48: cos(e + x*f)**2
                                        subjects2.appendleft(tmp214)
                                    if len(subjects2) >= 1 and subjects2[0] == -1:
                                        tmp215 = subjects2.popleft()
                                        # State 90853
                                        if len(subjects2) == 0:
                                            pass
                                            # State 90854
                                            if len(subjects) == 0:
                                                pass
                                                # 74: 1/cos(e + x*f)
                                        subjects2.appendleft(tmp215)
                                    if len(subjects2) >= 1 and subjects2[0] == -2:
                                        tmp216 = subjects2.popleft()
                                        # State 93965
                                        if len(subjects2) == 0:
                                            pass
                                            # State 93966
                                            if len(subjects) == 0:
                                                pass
                                                # 86: cos(e + x*f)**(-2)
                                        subjects2.appendleft(tmp216)
                            subjects209.appendleft(tmp212)
                    if len(subjects209) >= 1 and isinstance(subjects209[0], Mul):
                        tmp217 = subjects209.popleft()
                        associative1 = tmp217
                        associative_type1 = type(tmp217)
                        subjects218 = deque(tmp217._args)
                        matcher = CommutativeMatcher65612.get()
                        tmp219 = subjects218
                        subjects218 = []
                        for s in tmp219:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp219, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 65613
                                if len(subjects209) == 0:
                                    pass
                                    # State 65614
                                    if len(subjects2) >= 1 and subjects2[0] == 2:
                                        tmp220 = subjects2.popleft()
                                        # State 65615
                                        if len(subjects2) == 0:
                                            pass
                                            # State 65616
                                            if len(subjects) == 0:
                                                pass
                                                # 48: cos(e + x*f)**2
                                        subjects2.appendleft(tmp220)
                                    if len(subjects2) >= 1 and subjects2[0] == -1:
                                        tmp221 = subjects2.popleft()
                                        # State 90855
                                        if len(subjects2) == 0:
                                            pass
                                            # State 90856
                                            if len(subjects) == 0:
                                                pass
                                                # 74: 1/cos(e + x*f)
                                        subjects2.appendleft(tmp221)
                                    if len(subjects2) >= 1 and subjects2[0] == -2:
                                        tmp222 = subjects2.popleft()
                                        # State 93967
                                        if len(subjects2) == 0:
                                            pass
                                            # State 93968
                                            if len(subjects) == 0:
                                                pass
                                                # 86: cos(e + x*f)**(-2)
                                        subjects2.appendleft(tmp222)
                        subjects209.appendleft(tmp217)
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.3.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 65773
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.3.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 65774
                        if len(subjects209) >= 1:
                            tmp225 = subjects209.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.3.1.0', tmp225)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 65775
                                if len(subjects209) == 0:
                                    pass
                                    # State 65776
                                    if len(subjects2) >= 1 and subjects2[0] == 2:
                                        tmp227 = subjects2.popleft()
                                        # State 65777
                                        if len(subjects2) == 0:
                                            pass
                                            # State 65778
                                            if len(subjects) == 0:
                                                pass
                                                # 50: cos(e + x*f)**2
                                        subjects2.appendleft(tmp227)
                                    if len(subjects2) >= 1 and subjects2[0] == -1:
                                        tmp228 = subjects2.popleft()
                                        # State 90879
                                        if len(subjects2) == 0:
                                            pass
                                            # State 90880
                                            if len(subjects) == 0:
                                                pass
                                                # 75: 1/cos(e + x*f)
                                        subjects2.appendleft(tmp228)
                            subjects209.appendleft(tmp225)
                    if len(subjects209) >= 1 and isinstance(subjects209[0], Mul):
                        tmp229 = subjects209.popleft()
                        associative1 = tmp229
                        associative_type1 = type(tmp229)
                        subjects230 = deque(tmp229._args)
                        matcher = CommutativeMatcher65780.get()
                        tmp231 = subjects230
                        subjects230 = []
                        for s in tmp231:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp231, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 65781
                                if len(subjects209) == 0:
                                    pass
                                    # State 65782
                                    if len(subjects2) >= 1 and subjects2[0] == 2:
                                        tmp232 = subjects2.popleft()
                                        # State 65783
                                        if len(subjects2) == 0:
                                            pass
                                            # State 65784
                                            if len(subjects) == 0:
                                                pass
                                                # 50: cos(e + x*f)**2
                                        subjects2.appendleft(tmp232)
                                    if len(subjects2) >= 1 and subjects2[0] == -1:
                                        tmp233 = subjects2.popleft()
                                        # State 90881
                                        if len(subjects2) == 0:
                                            pass
                                            # State 90882
                                            if len(subjects) == 0:
                                                pass
                                                # 75: 1/cos(e + x*f)
                                        subjects2.appendleft(tmp233)
                        subjects209.appendleft(tmp229)
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.1.2.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 65879
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.2.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 65880
                        if len(subjects209) >= 1:
                            tmp236 = subjects209.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.2.1.0', tmp236)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 65881
                                if len(subjects209) == 0:
                                    pass
                                    # State 65882
                                    if len(subjects2) >= 1 and subjects2[0] == 2:
                                        tmp238 = subjects2.popleft()
                                        # State 65883
                                        if len(subjects2) == 0:
                                            pass
                                            # State 65884
                                            if len(subjects) == 0:
                                                pass
                                                # 52: cos(c + x*d)**2
                                        subjects2.appendleft(tmp238)
                            subjects209.appendleft(tmp236)
                    if len(subjects209) >= 1 and isinstance(subjects209[0], Mul):
                        tmp239 = subjects209.popleft()
                        associative1 = tmp239
                        associative_type1 = type(tmp239)
                        subjects240 = deque(tmp239._args)
                        matcher = CommutativeMatcher65886.get()
                        tmp241 = subjects240
                        subjects240 = []
                        for s in tmp241:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp241, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 65887
                                if len(subjects209) == 0:
                                    pass
                                    # State 65888
                                    if len(subjects2) >= 1 and subjects2[0] == 2:
                                        tmp242 = subjects2.popleft()
                                        # State 65889
                                        if len(subjects2) == 0:
                                            pass
                                            # State 65890
                                            if len(subjects) == 0:
                                                pass
                                                # 52: cos(c + x*d)**2
                                        subjects2.appendleft(tmp242)
                        subjects209.appendleft(tmp239)
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.3.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 66188
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.3.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 66189
                        if len(subjects209) >= 1:
                            tmp245 = subjects209.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.3.1.0', tmp245)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 66190
                                if len(subjects209) == 0:
                                    pass
                                    # State 66191
                                    if len(subjects2) >= 1 and subjects2[0] == 2:
                                        tmp247 = subjects2.popleft()
                                        # State 66192
                                        if len(subjects2) == 0:
                                            pass
                                            # State 66193
                                            if len(subjects) == 0:
                                                pass
                                                # 55: cos(e + x*f)**2
                                        subjects2.appendleft(tmp247)
                                    if len(subjects2) >= 1 and subjects2[0] == -1:
                                        tmp248 = subjects2.popleft()
                                        # State 90145
                                        if len(subjects2) == 0:
                                            pass
                                            # State 90146
                                            if len(subjects) == 0:
                                                pass
                                                # 72: 1/cos(e + x*f)
                                        subjects2.appendleft(tmp248)
                                    if len(subjects2) >= 1 and subjects2[0] == -2:
                                        tmp249 = subjects2.popleft()
                                        # State 93602
                                        if len(subjects2) == 0:
                                            pass
                                            # State 93603
                                            if len(subjects) == 0:
                                                pass
                                                # 82: cos(e + x*f)**(-2)
                                        subjects2.appendleft(tmp249)
                            subjects209.appendleft(tmp245)
                    if len(subjects209) >= 1 and isinstance(subjects209[0], Mul):
                        tmp250 = subjects209.popleft()
                        associative1 = tmp250
                        associative_type1 = type(tmp250)
                        subjects251 = deque(tmp250._args)
                        matcher = CommutativeMatcher66195.get()
                        tmp252 = subjects251
                        subjects251 = []
                        for s in tmp252:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp252, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 66196
                                if len(subjects209) == 0:
                                    pass
                                    # State 66197
                                    if len(subjects2) >= 1 and subjects2[0] == 2:
                                        tmp253 = subjects2.popleft()
                                        # State 66198
                                        if len(subjects2) == 0:
                                            pass
                                            # State 66199
                                            if len(subjects) == 0:
                                                pass
                                                # 55: cos(e + x*f)**2
                                        subjects2.appendleft(tmp253)
                                    if len(subjects2) >= 1 and subjects2[0] == -1:
                                        tmp254 = subjects2.popleft()
                                        # State 90147
                                        if len(subjects2) == 0:
                                            pass
                                            # State 90148
                                            if len(subjects) == 0:
                                                pass
                                                # 72: 1/cos(e + x*f)
                                        subjects2.appendleft(tmp254)
                                    if len(subjects2) >= 1 and subjects2[0] == -2:
                                        tmp255 = subjects2.popleft()
                                        # State 93604
                                        if len(subjects2) == 0:
                                            pass
                                            # State 93605
                                            if len(subjects) == 0:
                                                pass
                                                # 82: cos(e + x*f)**(-2)
                                        subjects2.appendleft(tmp255)
                        subjects209.appendleft(tmp250)
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.1.1.3.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 91434
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.1.1.3.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 91435
                        if len(subjects209) >= 1:
                            tmp258 = subjects209.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.1.1.3.1.0', tmp258)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 91436
                                if len(subjects209) == 0:
                                    pass
                                    # State 91437
                                    if len(subjects2) >= 1 and subjects2[0] == -1:
                                        tmp260 = subjects2.popleft()
                                        # State 91438
                                        if len(subjects2) == 0:
                                            pass
                                            # State 91439
                                            if len(subjects) == 0:
                                                pass
                                                # 77: 1/cos(c + x*d)
                                        subjects2.appendleft(tmp260)
                                    if len(subjects2) >= 1 and subjects2[0] == -2:
                                        tmp261 = subjects2.popleft()
                                        # State 93696
                                        if len(subjects2) == 0:
                                            pass
                                            # State 93697
                                            if len(subjects) == 0:
                                                pass
                                                # 84: cos(c + x*d)**(-2)
                                        subjects2.appendleft(tmp261)
                                    if len(subjects2) >= 1:
                                        tmp262 = subjects2.popleft()
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.1.1.3', tmp262)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 99809
                                            if len(subjects2) == 0:
                                                pass
                                                # State 99810
                                                if len(subjects) == 0:
                                                    pass
                                                    # 98: cos(c + x*d)**n1
                                        subjects2.appendleft(tmp262)
                                    if len(subjects2) >= 1:
                                        tmp264 = subjects2.popleft()
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.1.1.3_1', tmp264)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 99822
                                            if len(subjects2) == 0:
                                                pass
                                                # State 99823
                                                if len(subjects) == 0:
                                                    pass
                                                    # 99: cos(c + x*d)**n2
                                        subjects2.appendleft(tmp264)
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i2.1.1.3_2', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 99871
                                        if len(subjects2) == 0:
                                            pass
                                            # State 99872
                                            if len(subjects) == 0:
                                                pass
                                                # 100: cos(c + x*d)**n
                                    if len(subjects2) >= 1:
                                        tmp267 = subjects2.popleft()
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.1.1.3_2', tmp267)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 99871
                                            if len(subjects2) == 0:
                                                pass
                                                # State 99872
                                                if len(subjects) == 0:
                                                    pass
                                                    # 100: cos(c + x*d)**n
                                        subjects2.appendleft(tmp267)
                                    if len(subjects2) >= 1 and subjects2[0] == 2:
                                        tmp269 = subjects2.popleft()
                                        # State 100460
                                        if len(subjects2) == 0:
                                            pass
                                            # State 100461
                                            if len(subjects) == 0:
                                                pass
                                                # 112: cos(c + x*d)**2
                                        subjects2.appendleft(tmp269)
                            subjects209.appendleft(tmp258)
                    if len(subjects209) >= 1 and isinstance(subjects209[0], Mul):
                        tmp270 = subjects209.popleft()
                        associative1 = tmp270
                        associative_type1 = type(tmp270)
                        subjects271 = deque(tmp270._args)
                        matcher = CommutativeMatcher91441.get()
                        tmp272 = subjects271
                        subjects271 = []
                        for s in tmp272:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp272, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 91442
                                if len(subjects209) == 0:
                                    pass
                                    # State 91443
                                    if len(subjects2) >= 1 and subjects2[0] == -1:
                                        tmp273 = subjects2.popleft()
                                        # State 91444
                                        if len(subjects2) == 0:
                                            pass
                                            # State 91445
                                            if len(subjects) == 0:
                                                pass
                                                # 77: 1/cos(c + x*d)
                                        subjects2.appendleft(tmp273)
                                    if len(subjects2) >= 1 and subjects2[0] == -2:
                                        tmp274 = subjects2.popleft()
                                        # State 93698
                                        if len(subjects2) == 0:
                                            pass
                                            # State 93699
                                            if len(subjects) == 0:
                                                pass
                                                # 84: cos(c + x*d)**(-2)
                                        subjects2.appendleft(tmp274)
                                    if len(subjects2) >= 1:
                                        tmp275 = subjects2.popleft()
                                        subst3 = Substitution(subst2)
                                        try:
                                            subst3.try_add_variable('i2.1.1.3', tmp275)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 99811
                                            if len(subjects2) == 0:
                                                pass
                                                # State 99812
                                                if len(subjects) == 0:
                                                    pass
                                                    # 98: cos(c + x*d)**n1
                                        subjects2.appendleft(tmp275)
                                    if len(subjects2) >= 1:
                                        tmp277 = subjects2.popleft()
                                        subst3 = Substitution(subst2)
                                        try:
                                            subst3.try_add_variable('i2.1.1.3_1', tmp277)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 99824
                                            if len(subjects2) == 0:
                                                pass
                                                # State 99825
                                                if len(subjects) == 0:
                                                    pass
                                                    # 99: cos(c + x*d)**n2
                                        subjects2.appendleft(tmp277)
                                    subst3 = Substitution(subst2)
                                    try:
                                        subst3.try_add_variable('i2.1.1.3_2', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 99873
                                        if len(subjects2) == 0:
                                            pass
                                            # State 99874
                                            if len(subjects) == 0:
                                                pass
                                                # 100: cos(c + x*d)**n
                                    if len(subjects2) >= 1:
                                        tmp280 = subjects2.popleft()
                                        subst3 = Substitution(subst2)
                                        try:
                                            subst3.try_add_variable('i2.1.1.3_2', tmp280)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 99873
                                            if len(subjects2) == 0:
                                                pass
                                                # State 99874
                                                if len(subjects) == 0:
                                                    pass
                                                    # 100: cos(c + x*d)**n
                                        subjects2.appendleft(tmp280)
                                    if len(subjects2) >= 1 and subjects2[0] == 2:
                                        tmp282 = subjects2.popleft()
                                        # State 100462
                                        if len(subjects2) == 0:
                                            pass
                                            # State 100463
                                            if len(subjects) == 0:
                                                pass
                                                # 112: cos(c + x*d)**2
                                        subjects2.appendleft(tmp282)
                        subjects209.appendleft(tmp270)
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.1.3.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 91528
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.3.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 91529
                        if len(subjects209) >= 1:
                            tmp285 = subjects209.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.3.1.0', tmp285)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 91530
                                if len(subjects209) == 0:
                                    pass
                                    # State 91531
                                    if len(subjects2) >= 1 and subjects2[0] == -1:
                                        tmp287 = subjects2.popleft()
                                        # State 91532
                                        if len(subjects2) == 0:
                                            pass
                                            # State 91533
                                            if len(subjects) == 0:
                                                pass
                                                # 78: 1/cos(e + x*f)
                                        subjects2.appendleft(tmp287)
                                    if len(subjects2) >= 1 and subjects2[0] == -2:
                                        tmp288 = subjects2.popleft()
                                        # State 93455
                                        if len(subjects2) == 0:
                                            pass
                                            # State 93456
                                            if len(subjects) == 0:
                                                pass
                                                # 80: cos(e + x*f)**(-2)
                                        subjects2.appendleft(tmp288)
                            subjects209.appendleft(tmp285)
                    if len(subjects209) >= 1 and isinstance(subjects209[0], Mul):
                        tmp289 = subjects209.popleft()
                        associative1 = tmp289
                        associative_type1 = type(tmp289)
                        subjects290 = deque(tmp289._args)
                        matcher = CommutativeMatcher91535.get()
                        tmp291 = subjects290
                        subjects290 = []
                        for s in tmp291:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp291, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 91536
                                if len(subjects209) == 0:
                                    pass
                                    # State 91537
                                    if len(subjects2) >= 1 and subjects2[0] == -1:
                                        tmp292 = subjects2.popleft()
                                        # State 91538
                                        if len(subjects2) == 0:
                                            pass
                                            # State 91539
                                            if len(subjects) == 0:
                                                pass
                                                # 78: 1/cos(e + x*f)
                                        subjects2.appendleft(tmp292)
                                    if len(subjects2) >= 1 and subjects2[0] == -2:
                                        tmp293 = subjects2.popleft()
                                        # State 93457
                                        if len(subjects2) == 0:
                                            pass
                                            # State 93458
                                            if len(subjects) == 0:
                                                pass
                                                # 80: cos(e + x*f)**(-2)
                                        subjects2.appendleft(tmp293)
                        subjects209.appendleft(tmp289)
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.2.3.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 94086
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.2.3.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 94087
                        if len(subjects209) >= 1:
                            tmp296 = subjects209.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.2.3.1.0', tmp296)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 94088
                                if len(subjects209) == 0:
                                    pass
                                    # State 94089
                                    if len(subjects2) >= 1 and subjects2[0] == -1:
                                        tmp298 = subjects2.popleft()
                                        # State 94090
                                        if len(subjects2) == 0:
                                            pass
                                            # State 94091
                                            if len(subjects) == 0:
                                                pass
                                                # 89: 1/cos(e + x*f)
                                        subjects2.appendleft(tmp298)
                                    if len(subjects2) >= 1 and subjects2[0] == -2:
                                        tmp299 = subjects2.popleft()
                                        # State 94125
                                        if len(subjects2) == 0:
                                            pass
                                            # State 94126
                                            if len(subjects) == 0:
                                                pass
                                                # 90: cos(e + x*f)**(-2)
                                        subjects2.appendleft(tmp299)
                            subjects209.appendleft(tmp296)
                    if len(subjects209) >= 1 and isinstance(subjects209[0], Mul):
                        tmp300 = subjects209.popleft()
                        associative1 = tmp300
                        associative_type1 = type(tmp300)
                        subjects301 = deque(tmp300._args)
                        matcher = CommutativeMatcher94093.get()
                        tmp302 = subjects301
                        subjects301 = []
                        for s in tmp302:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp302, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 94094
                                if len(subjects209) == 0:
                                    pass
                                    # State 94095
                                    if len(subjects2) >= 1 and subjects2[0] == -1:
                                        tmp303 = subjects2.popleft()
                                        # State 94096
                                        if len(subjects2) == 0:
                                            pass
                                            # State 94097
                                            if len(subjects) == 0:
                                                pass
                                                # 89: 1/cos(e + x*f)
                                        subjects2.appendleft(tmp303)
                                    if len(subjects2) >= 1 and subjects2[0] == -2:
                                        tmp304 = subjects2.popleft()
                                        # State 94127
                                        if len(subjects2) == 0:
                                            pass
                                            # State 94128
                                            if len(subjects) == 0:
                                                pass
                                                # 90: cos(e + x*f)**(-2)
                                        subjects2.appendleft(tmp304)
                        subjects209.appendleft(tmp300)
                if len(subjects209) >= 1 and isinstance(subjects209[0], Add):
                    tmp305 = subjects209.popleft()
                    associative1 = tmp305
                    associative_type1 = type(tmp305)
                    subjects306 = deque(tmp305._args)
                    matcher = CommutativeMatcher65618.get()
                    tmp307 = subjects306
                    subjects306 = []
                    for s in tmp307:
                        matcher.add_subject(s)
                    for pattern_index, subst1 in matcher.match(tmp307, subst0):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 65624
                            if len(subjects209) == 0:
                                pass
                                # State 65625
                                if len(subjects2) >= 1 and subjects2[0] == 2:
                                    tmp308 = subjects2.popleft()
                                    # State 65626
                                    if len(subjects2) == 0:
                                        pass
                                        # State 65627
                                        if len(subjects) == 0:
                                            pass
                                            # 48: cos(e + x*f)**2
                                    subjects2.appendleft(tmp308)
                                if len(subjects2) >= 1 and subjects2[0] == -1:
                                    tmp309 = subjects2.popleft()
                                    # State 90857
                                    if len(subjects2) == 0:
                                        pass
                                        # State 90858
                                        if len(subjects) == 0:
                                            pass
                                            # 74: 1/cos(e + x*f)
                                    subjects2.appendleft(tmp309)
                                if len(subjects2) >= 1 and subjects2[0] == -2:
                                    tmp310 = subjects2.popleft()
                                    # State 93969
                                    if len(subjects2) == 0:
                                        pass
                                        # State 93970
                                        if len(subjects) == 0:
                                            pass
                                            # 86: cos(e + x*f)**(-2)
                                    subjects2.appendleft(tmp310)
                        if pattern_index == 1:
                            pass
                            # State 65788
                            if len(subjects209) == 0:
                                pass
                                # State 65789
                                if len(subjects2) >= 1 and subjects2[0] == 2:
                                    tmp311 = subjects2.popleft()
                                    # State 65790
                                    if len(subjects2) == 0:
                                        pass
                                        # State 65791
                                        if len(subjects) == 0:
                                            pass
                                            # 50: cos(e + x*f)**2
                                    subjects2.appendleft(tmp311)
                                if len(subjects2) >= 1 and subjects2[0] == -1:
                                    tmp312 = subjects2.popleft()
                                    # State 90883
                                    if len(subjects2) == 0:
                                        pass
                                        # State 90884
                                        if len(subjects) == 0:
                                            pass
                                            # 75: 1/cos(e + x*f)
                                    subjects2.appendleft(tmp312)
                        if pattern_index == 2:
                            pass
                            # State 65894
                            if len(subjects209) == 0:
                                pass
                                # State 65895
                                if len(subjects2) >= 1 and subjects2[0] == 2:
                                    tmp313 = subjects2.popleft()
                                    # State 65896
                                    if len(subjects2) == 0:
                                        pass
                                        # State 65897
                                        if len(subjects) == 0:
                                            pass
                                            # 52: cos(c + x*d)**2
                                    subjects2.appendleft(tmp313)
                        if pattern_index == 3:
                            pass
                            # State 66203
                            if len(subjects209) == 0:
                                pass
                                # State 66204
                                if len(subjects2) >= 1 and subjects2[0] == 2:
                                    tmp314 = subjects2.popleft()
                                    # State 66205
                                    if len(subjects2) == 0:
                                        pass
                                        # State 66206
                                        if len(subjects) == 0:
                                            pass
                                            # 55: cos(e + x*f)**2
                                    subjects2.appendleft(tmp314)
                                if len(subjects2) >= 1 and subjects2[0] == -1:
                                    tmp315 = subjects2.popleft()
                                    # State 90149
                                    if len(subjects2) == 0:
                                        pass
                                        # State 90150
                                        if len(subjects) == 0:
                                            pass
                                            # 72: 1/cos(e + x*f)
                                    subjects2.appendleft(tmp315)
                                if len(subjects2) >= 1 and subjects2[0] == -2:
                                    tmp316 = subjects2.popleft()
                                    # State 93606
                                    if len(subjects2) == 0:
                                        pass
                                        # State 93607
                                        if len(subjects) == 0:
                                            pass
                                            # 82: cos(e + x*f)**(-2)
                                    subjects2.appendleft(tmp316)
                        if pattern_index == 4:
                            pass
                            # State 91449
                            if len(subjects209) == 0:
                                pass
                                # State 91450
                                if len(subjects2) >= 1 and subjects2[0] == -1:
                                    tmp317 = subjects2.popleft()
                                    # State 91451
                                    if len(subjects2) == 0:
                                        pass
                                        # State 91452
                                        if len(subjects) == 0:
                                            pass
                                            # 77: 1/cos(c + x*d)
                                    subjects2.appendleft(tmp317)
                                if len(subjects2) >= 1 and subjects2[0] == -2:
                                    tmp318 = subjects2.popleft()
                                    # State 93700
                                    if len(subjects2) == 0:
                                        pass
                                        # State 93701
                                        if len(subjects) == 0:
                                            pass
                                            # 84: cos(c + x*d)**(-2)
                                    subjects2.appendleft(tmp318)
                                if len(subjects2) >= 1:
                                    tmp319 = subjects2.popleft()
                                    subst2 = Substitution(subst1)
                                    try:
                                        subst2.try_add_variable('i2.1.1.3', tmp319)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 99813
                                        if len(subjects2) == 0:
                                            pass
                                            # State 99814
                                            if len(subjects) == 0:
                                                pass
                                                # 98: cos(c + x*d)**n1
                                    subjects2.appendleft(tmp319)
                                if len(subjects2) >= 1:
                                    tmp321 = subjects2.popleft()
                                    subst2 = Substitution(subst1)
                                    try:
                                        subst2.try_add_variable('i2.1.1.3_1', tmp321)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 99826
                                        if len(subjects2) == 0:
                                            pass
                                            # State 99827
                                            if len(subjects) == 0:
                                                pass
                                                # 99: cos(c + x*d)**n2
                                    subjects2.appendleft(tmp321)
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i2.1.1.3_2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 99875
                                    if len(subjects2) == 0:
                                        pass
                                        # State 99876
                                        if len(subjects) == 0:
                                            pass
                                            # 100: cos(c + x*d)**n
                                if len(subjects2) >= 1:
                                    tmp324 = subjects2.popleft()
                                    subst2 = Substitution(subst1)
                                    try:
                                        subst2.try_add_variable('i2.1.1.3_2', tmp324)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 99875
                                        if len(subjects2) == 0:
                                            pass
                                            # State 99876
                                            if len(subjects) == 0:
                                                pass
                                                # 100: cos(c + x*d)**n
                                    subjects2.appendleft(tmp324)
                                if len(subjects2) >= 1 and subjects2[0] == 2:
                                    tmp326 = subjects2.popleft()
                                    # State 100464
                                    if len(subjects2) == 0:
                                        pass
                                        # State 100465
                                        if len(subjects) == 0:
                                            pass
                                            # 112: cos(c + x*d)**2
                                    subjects2.appendleft(tmp326)
                        if pattern_index == 5:
                            pass
                            # State 91543
                            if len(subjects209) == 0:
                                pass
                                # State 91544
                                if len(subjects2) >= 1 and subjects2[0] == -1:
                                    tmp327 = subjects2.popleft()
                                    # State 91545
                                    if len(subjects2) == 0:
                                        pass
                                        # State 91546
                                        if len(subjects) == 0:
                                            pass
                                            # 78: 1/cos(e + x*f)
                                    subjects2.appendleft(tmp327)
                                if len(subjects2) >= 1 and subjects2[0] == -2:
                                    tmp328 = subjects2.popleft()
                                    # State 93459
                                    if len(subjects2) == 0:
                                        pass
                                        # State 93460
                                        if len(subjects) == 0:
                                            pass
                                            # 80: cos(e + x*f)**(-2)
                                    subjects2.appendleft(tmp328)
                        if pattern_index == 6:
                            pass
                            # State 94101
                            if len(subjects209) == 0:
                                pass
                                # State 94102
                                if len(subjects2) >= 1 and subjects2[0] == -1:
                                    tmp329 = subjects2.popleft()
                                    # State 94103
                                    if len(subjects2) == 0:
                                        pass
                                        # State 94104
                                        if len(subjects) == 0:
                                            pass
                                            # 89: 1/cos(e + x*f)
                                    subjects2.appendleft(tmp329)
                                if len(subjects2) >= 1 and subjects2[0] == -2:
                                    tmp330 = subjects2.popleft()
                                    # State 94129
                                    if len(subjects2) == 0:
                                        pass
                                        # State 94130
                                        if len(subjects) == 0:
                                            pass
                                            # 90: cos(e + x*f)**(-2)
                                    subjects2.appendleft(tmp330)
                    subjects209.appendleft(tmp305)
                subjects2.appendleft(tmp208)
            if len(subjects2) >= 1 and isinstance(subjects2[0], tan):
                tmp331 = subjects2.popleft()
                subjects332 = deque(tmp331._args)
                # State 77639
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.3.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 77640
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.3.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 77641
                        if len(subjects332) >= 1:
                            tmp335 = subjects332.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.3.1.0', tmp335)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 77642
                                if len(subjects332) == 0:
                                    pass
                                    # State 77643
                                    if len(subjects2) >= 1 and subjects2[0] == -1:
                                        tmp337 = subjects2.popleft()
                                        # State 77644
                                        if len(subjects2) == 0:
                                            pass
                                            # State 77645
                                            if len(subjects) == 0:
                                                pass
                                                # 60: 1/tan(e + x*f)
                                        subjects2.appendleft(tmp337)
                                    if len(subjects2) >= 1 and subjects2[0] == 2:
                                        tmp338 = subjects2.popleft()
                                        # State 99982
                                        if len(subjects2) == 0:
                                            pass
                                            # State 99983
                                            if len(subjects) == 0:
                                                pass
                                                # 103: tan(e + x*f)**2
                                        subjects2.appendleft(tmp338)
                            subjects332.appendleft(tmp335)
                    if len(subjects332) >= 1 and isinstance(subjects332[0], Mul):
                        tmp339 = subjects332.popleft()
                        associative1 = tmp339
                        associative_type1 = type(tmp339)
                        subjects340 = deque(tmp339._args)
                        matcher = CommutativeMatcher77647.get()
                        tmp341 = subjects340
                        subjects340 = []
                        for s in tmp341:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp341, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 77648
                                if len(subjects332) == 0:
                                    pass
                                    # State 77649
                                    if len(subjects2) >= 1 and subjects2[0] == -1:
                                        tmp342 = subjects2.popleft()
                                        # State 77650
                                        if len(subjects2) == 0:
                                            pass
                                            # State 77651
                                            if len(subjects) == 0:
                                                pass
                                                # 60: 1/tan(e + x*f)
                                        subjects2.appendleft(tmp342)
                                    if len(subjects2) >= 1 and subjects2[0] == 2:
                                        tmp343 = subjects2.popleft()
                                        # State 99984
                                        if len(subjects2) == 0:
                                            pass
                                            # State 99985
                                            if len(subjects) == 0:
                                                pass
                                                # 103: tan(e + x*f)**2
                                        subjects2.appendleft(tmp343)
                        subjects332.appendleft(tmp339)
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.1.1.3.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 78839
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.1.1.3.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 78840
                        if len(subjects332) >= 1:
                            tmp346 = subjects332.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.1.1.3.1.0', tmp346)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 78841
                                if len(subjects332) == 0:
                                    pass
                                    # State 78842
                                    if len(subjects2) >= 1 and subjects2[0] == -1:
                                        tmp348 = subjects2.popleft()
                                        # State 78843
                                        if len(subjects2) == 0:
                                            pass
                                            # State 78844
                                            if len(subjects) == 0:
                                                pass
                                                # 62: 1/tan(e + x*f)
                                        subjects2.appendleft(tmp348)
                                    if len(subjects2) >= 1 and subjects2[0] == -2:
                                        tmp349 = subjects2.popleft()
                                        # State 81713
                                        if len(subjects2) == 0:
                                            pass
                                            # State 81714
                                            if len(subjects) == 0:
                                                pass
                                                # 70: tan(e + x*f)**(-2)
                                        subjects2.appendleft(tmp349)
                                    if len(subjects2) >= 1 and subjects2[0] == 2:
                                        tmp350 = subjects2.popleft()
                                        # State 100032
                                        if len(subjects2) == 0:
                                            pass
                                            # State 100033
                                            if len(subjects) == 0:
                                                pass
                                                # 104: tan(e + x*f)**2
                                        subjects2.appendleft(tmp350)
                                    if len(subjects2) >= 1:
                                        tmp351 = subjects2.popleft()
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.1.1.3', tmp351)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 100087
                                            if len(subjects2) == 0:
                                                pass
                                                # State 100088
                                                if len(subjects) == 0:
                                                    pass
                                                    # 106: tan(e + x*f)**n1
                                        subjects2.appendleft(tmp351)
                                    if len(subjects2) >= 1:
                                        tmp353 = subjects2.popleft()
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.1.1.3_1', tmp353)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 100100
                                            if len(subjects2) == 0:
                                                pass
                                                # State 100101
                                                if len(subjects) == 0:
                                                    pass
                                                    # 107: tan(e + x*f)**n2
                                        subjects2.appendleft(tmp353)
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i2.1.1.3_2', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 100162
                                        if len(subjects2) == 0:
                                            pass
                                            # State 100163
                                            if len(subjects) == 0:
                                                pass
                                                # 108: tan(e + x*f)**n
                                    if len(subjects2) >= 1:
                                        tmp356 = subjects2.popleft()
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.1.1.3_2', tmp356)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 100162
                                            if len(subjects2) == 0:
                                                pass
                                                # State 100163
                                                if len(subjects) == 0:
                                                    pass
                                                    # 108: tan(e + x*f)**n
                                        subjects2.appendleft(tmp356)
                            subjects332.appendleft(tmp346)
                    if len(subjects332) >= 1 and isinstance(subjects332[0], Mul):
                        tmp358 = subjects332.popleft()
                        associative1 = tmp358
                        associative_type1 = type(tmp358)
                        subjects359 = deque(tmp358._args)
                        matcher = CommutativeMatcher78846.get()
                        tmp360 = subjects359
                        subjects359 = []
                        for s in tmp360:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp360, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 78847
                                if len(subjects332) == 0:
                                    pass
                                    # State 78848
                                    if len(subjects2) >= 1 and subjects2[0] == -1:
                                        tmp361 = subjects2.popleft()
                                        # State 78849
                                        if len(subjects2) == 0:
                                            pass
                                            # State 78850
                                            if len(subjects) == 0:
                                                pass
                                                # 62: 1/tan(e + x*f)
                                        subjects2.appendleft(tmp361)
                                    if len(subjects2) >= 1 and subjects2[0] == -2:
                                        tmp362 = subjects2.popleft()
                                        # State 81715
                                        if len(subjects2) == 0:
                                            pass
                                            # State 81716
                                            if len(subjects) == 0:
                                                pass
                                                # 70: tan(e + x*f)**(-2)
                                        subjects2.appendleft(tmp362)
                                    if len(subjects2) >= 1 and subjects2[0] == 2:
                                        tmp363 = subjects2.popleft()
                                        # State 100034
                                        if len(subjects2) == 0:
                                            pass
                                            # State 100035
                                            if len(subjects) == 0:
                                                pass
                                                # 104: tan(e + x*f)**2
                                        subjects2.appendleft(tmp363)
                                    if len(subjects2) >= 1:
                                        tmp364 = subjects2.popleft()
                                        subst3 = Substitution(subst2)
                                        try:
                                            subst3.try_add_variable('i2.1.1.3', tmp364)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 100089
                                            if len(subjects2) == 0:
                                                pass
                                                # State 100090
                                                if len(subjects) == 0:
                                                    pass
                                                    # 106: tan(e + x*f)**n1
                                        subjects2.appendleft(tmp364)
                                    if len(subjects2) >= 1:
                                        tmp366 = subjects2.popleft()
                                        subst3 = Substitution(subst2)
                                        try:
                                            subst3.try_add_variable('i2.1.1.3_1', tmp366)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 100102
                                            if len(subjects2) == 0:
                                                pass
                                                # State 100103
                                                if len(subjects) == 0:
                                                    pass
                                                    # 107: tan(e + x*f)**n2
                                        subjects2.appendleft(tmp366)
                                    subst3 = Substitution(subst2)
                                    try:
                                        subst3.try_add_variable('i2.1.1.3_2', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 100164
                                        if len(subjects2) == 0:
                                            pass
                                            # State 100165
                                            if len(subjects) == 0:
                                                pass
                                                # 108: tan(e + x*f)**n
                                    if len(subjects2) >= 1:
                                        tmp369 = subjects2.popleft()
                                        subst3 = Substitution(subst2)
                                        try:
                                            subst3.try_add_variable('i2.1.1.3_2', tmp369)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 100164
                                            if len(subjects2) == 0:
                                                pass
                                                # State 100165
                                                if len(subjects) == 0:
                                                    pass
                                                    # 108: tan(e + x*f)**n
                                        subjects2.appendleft(tmp369)
                        subjects332.appendleft(tmp358)
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.1.3.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 79121
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.3.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 79122
                        if len(subjects332) >= 1:
                            tmp373 = subjects332.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.3.1.0', tmp373)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 79123
                                if len(subjects332) == 0:
                                    pass
                                    # State 79124
                                    if len(subjects2) >= 1 and subjects2[0] == -1:
                                        tmp375 = subjects2.popleft()
                                        # State 79125
                                        if len(subjects2) == 0:
                                            pass
                                            # State 79126
                                            if len(subjects) == 0:
                                                pass
                                                # 64: 1/tan(e + x*f)
                                        subjects2.appendleft(tmp375)
                                    if len(subjects2) >= 1 and subjects2[0] == -2:
                                        tmp376 = subjects2.popleft()
                                        # State 81525
                                        if len(subjects2) == 0:
                                            pass
                                            # State 81526
                                            if len(subjects) == 0:
                                                pass
                                                # 67: tan(e + x*f)**(-2)
                                        subjects2.appendleft(tmp376)
                            subjects332.appendleft(tmp373)
                    if len(subjects332) >= 1 and isinstance(subjects332[0], Mul):
                        tmp377 = subjects332.popleft()
                        associative1 = tmp377
                        associative_type1 = type(tmp377)
                        subjects378 = deque(tmp377._args)
                        matcher = CommutativeMatcher79128.get()
                        tmp379 = subjects378
                        subjects378 = []
                        for s in tmp379:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp379, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 79129
                                if len(subjects332) == 0:
                                    pass
                                    # State 79130
                                    if len(subjects2) >= 1 and subjects2[0] == -1:
                                        tmp380 = subjects2.popleft()
                                        # State 79131
                                        if len(subjects2) == 0:
                                            pass
                                            # State 79132
                                            if len(subjects) == 0:
                                                pass
                                                # 64: 1/tan(e + x*f)
                                        subjects2.appendleft(tmp380)
                                    if len(subjects2) >= 1 and subjects2[0] == -2:
                                        tmp381 = subjects2.popleft()
                                        # State 81527
                                        if len(subjects2) == 0:
                                            pass
                                            # State 81528
                                            if len(subjects) == 0:
                                                pass
                                                # 67: tan(e + x*f)**(-2)
                                        subjects2.appendleft(tmp381)
                        subjects332.appendleft(tmp377)
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.1.2.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 81495
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.2.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 81496
                        if len(subjects332) >= 1:
                            tmp384 = subjects332.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.2.1.0', tmp384)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 81497
                                if len(subjects332) == 0:
                                    pass
                                    # State 81498
                                    if len(subjects2) >= 1 and subjects2[0] == 2:
                                        tmp386 = subjects2.popleft()
                                        # State 81499
                                        if len(subjects2) == 0:
                                            pass
                                            # State 81500
                                            if len(subjects) == 0:
                                                pass
                                                # 66: tan(c + x*d)**2
                                        subjects2.appendleft(tmp386)
                            subjects332.appendleft(tmp384)
                    if len(subjects332) >= 1 and isinstance(subjects332[0], Mul):
                        tmp387 = subjects332.popleft()
                        associative1 = tmp387
                        associative_type1 = type(tmp387)
                        subjects388 = deque(tmp387._args)
                        matcher = CommutativeMatcher81502.get()
                        tmp389 = subjects388
                        subjects388 = []
                        for s in tmp389:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp389, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 81503
                                if len(subjects332) == 0:
                                    pass
                                    # State 81504
                                    if len(subjects2) >= 1 and subjects2[0] == 2:
                                        tmp390 = subjects2.popleft()
                                        # State 81505
                                        if len(subjects2) == 0:
                                            pass
                                            # State 81506
                                            if len(subjects) == 0:
                                                pass
                                                # 66: tan(c + x*d)**2
                                        subjects2.appendleft(tmp390)
                        subjects332.appendleft(tmp387)
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.3.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 81656
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.3.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 81657
                        if len(subjects332) >= 1:
                            tmp393 = subjects332.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.3.1.0', tmp393)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 81658
                                if len(subjects332) == 0:
                                    pass
                                    # State 81659
                                    if len(subjects2) >= 1 and subjects2[0] == 2:
                                        tmp395 = subjects2.popleft()
                                        # State 81660
                                        if len(subjects2) == 0:
                                            pass
                                            # State 81661
                                            if len(subjects) == 0:
                                                pass
                                                # 68: tan(e + x*f)**2
                                        subjects2.appendleft(tmp395)
                            subjects332.appendleft(tmp393)
                    if len(subjects332) >= 1 and isinstance(subjects332[0], Mul):
                        tmp396 = subjects332.popleft()
                        associative1 = tmp396
                        associative_type1 = type(tmp396)
                        subjects397 = deque(tmp396._args)
                        matcher = CommutativeMatcher81663.get()
                        tmp398 = subjects397
                        subjects397 = []
                        for s in tmp398:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp398, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 81664
                                if len(subjects332) == 0:
                                    pass
                                    # State 81665
                                    if len(subjects2) >= 1 and subjects2[0] == 2:
                                        tmp399 = subjects2.popleft()
                                        # State 81666
                                        if len(subjects2) == 0:
                                            pass
                                            # State 81667
                                            if len(subjects) == 0:
                                                pass
                                                # 68: tan(e + x*f)**2
                                        subjects2.appendleft(tmp399)
                        subjects332.appendleft(tmp396)
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.2.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 99913
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.2.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 99914
                        if len(subjects332) >= 1:
                            tmp402 = subjects332.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.2.1.0', tmp402)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 99915
                                if len(subjects332) == 0:
                                    pass
                                    # State 99916
                                    if len(subjects2) >= 1 and subjects2[0] == -1:
                                        tmp404 = subjects2.popleft()
                                        # State 99917
                                        if len(subjects2) == 0:
                                            pass
                                            # State 99918
                                            if len(subjects) == 0:
                                                pass
                                                # 101: 1/tan(e + x*f)
                                        subjects2.appendleft(tmp404)
                                    if len(subjects2) >= 1 and subjects2[0] == -2:
                                        tmp405 = subjects2.popleft()
                                        # State 99965
                                        if len(subjects2) == 0:
                                            pass
                                            # State 99966
                                            if len(subjects) == 0:
                                                pass
                                                # 102: tan(e + x*f)**(-2)
                                        subjects2.appendleft(tmp405)
                            subjects332.appendleft(tmp402)
                    if len(subjects332) >= 1 and isinstance(subjects332[0], Mul):
                        tmp406 = subjects332.popleft()
                        associative1 = tmp406
                        associative_type1 = type(tmp406)
                        subjects407 = deque(tmp406._args)
                        matcher = CommutativeMatcher99920.get()
                        tmp408 = subjects407
                        subjects407 = []
                        for s in tmp408:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp408, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 99921
                                if len(subjects332) == 0:
                                    pass
                                    # State 99922
                                    if len(subjects2) >= 1 and subjects2[0] == -1:
                                        tmp409 = subjects2.popleft()
                                        # State 99923
                                        if len(subjects2) == 0:
                                            pass
                                            # State 99924
                                            if len(subjects) == 0:
                                                pass
                                                # 101: 1/tan(e + x*f)
                                        subjects2.appendleft(tmp409)
                                    if len(subjects2) >= 1 and subjects2[0] == -2:
                                        tmp410 = subjects2.popleft()
                                        # State 99967
                                        if len(subjects2) == 0:
                                            pass
                                            # State 99968
                                            if len(subjects) == 0:
                                                pass
                                                # 102: tan(e + x*f)**(-2)
                                        subjects2.appendleft(tmp410)
                        subjects332.appendleft(tmp406)
                if len(subjects332) >= 1 and isinstance(subjects332[0], Add):
                    tmp411 = subjects332.popleft()
                    associative1 = tmp411
                    associative_type1 = type(tmp411)
                    subjects412 = deque(tmp411._args)
                    matcher = CommutativeMatcher77653.get()
                    tmp413 = subjects412
                    subjects412 = []
                    for s in tmp413:
                        matcher.add_subject(s)
                    for pattern_index, subst1 in matcher.match(tmp413, subst0):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 77659
                            if len(subjects332) == 0:
                                pass
                                # State 77660
                                if len(subjects2) >= 1 and subjects2[0] == -1:
                                    tmp414 = subjects2.popleft()
                                    # State 77661
                                    if len(subjects2) == 0:
                                        pass
                                        # State 77662
                                        if len(subjects) == 0:
                                            pass
                                            # 60: 1/tan(e + x*f)
                                    subjects2.appendleft(tmp414)
                                if len(subjects2) >= 1 and subjects2[0] == 2:
                                    tmp415 = subjects2.popleft()
                                    # State 99986
                                    if len(subjects2) == 0:
                                        pass
                                        # State 99987
                                        if len(subjects) == 0:
                                            pass
                                            # 103: tan(e + x*f)**2
                                    subjects2.appendleft(tmp415)
                        if pattern_index == 1:
                            pass
                            # State 78854
                            if len(subjects332) == 0:
                                pass
                                # State 78855
                                if len(subjects2) >= 1 and subjects2[0] == -1:
                                    tmp416 = subjects2.popleft()
                                    # State 78856
                                    if len(subjects2) == 0:
                                        pass
                                        # State 78857
                                        if len(subjects) == 0:
                                            pass
                                            # 62: 1/tan(e + x*f)
                                    subjects2.appendleft(tmp416)
                                if len(subjects2) >= 1 and subjects2[0] == -2:
                                    tmp417 = subjects2.popleft()
                                    # State 81717
                                    if len(subjects2) == 0:
                                        pass
                                        # State 81718
                                        if len(subjects) == 0:
                                            pass
                                            # 70: tan(e + x*f)**(-2)
                                    subjects2.appendleft(tmp417)
                                if len(subjects2) >= 1 and subjects2[0] == 2:
                                    tmp418 = subjects2.popleft()
                                    # State 100036
                                    if len(subjects2) == 0:
                                        pass
                                        # State 100037
                                        if len(subjects) == 0:
                                            pass
                                            # 104: tan(e + x*f)**2
                                    subjects2.appendleft(tmp418)
                                if len(subjects2) >= 1:
                                    tmp419 = subjects2.popleft()
                                    subst2 = Substitution(subst1)
                                    try:
                                        subst2.try_add_variable('i2.1.1.3', tmp419)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 100091
                                        if len(subjects2) == 0:
                                            pass
                                            # State 100092
                                            if len(subjects) == 0:
                                                pass
                                                # 106: tan(e + x*f)**n1
                                    subjects2.appendleft(tmp419)
                                if len(subjects2) >= 1:
                                    tmp421 = subjects2.popleft()
                                    subst2 = Substitution(subst1)
                                    try:
                                        subst2.try_add_variable('i2.1.1.3_1', tmp421)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 100104
                                        if len(subjects2) == 0:
                                            pass
                                            # State 100105
                                            if len(subjects) == 0:
                                                pass
                                                # 107: tan(e + x*f)**n2
                                    subjects2.appendleft(tmp421)
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i2.1.1.3_2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 100166
                                    if len(subjects2) == 0:
                                        pass
                                        # State 100167
                                        if len(subjects) == 0:
                                            pass
                                            # 108: tan(e + x*f)**n
                                if len(subjects2) >= 1:
                                    tmp424 = subjects2.popleft()
                                    subst2 = Substitution(subst1)
                                    try:
                                        subst2.try_add_variable('i2.1.1.3_2', tmp424)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 100166
                                        if len(subjects2) == 0:
                                            pass
                                            # State 100167
                                            if len(subjects) == 0:
                                                pass
                                                # 108: tan(e + x*f)**n
                                    subjects2.appendleft(tmp424)
                        if pattern_index == 2:
                            pass
                            # State 79136
                            if len(subjects332) == 0:
                                pass
                                # State 79137
                                if len(subjects2) >= 1 and subjects2[0] == -1:
                                    tmp426 = subjects2.popleft()
                                    # State 79138
                                    if len(subjects2) == 0:
                                        pass
                                        # State 79139
                                        if len(subjects) == 0:
                                            pass
                                            # 64: 1/tan(e + x*f)
                                    subjects2.appendleft(tmp426)
                                if len(subjects2) >= 1 and subjects2[0] == -2:
                                    tmp427 = subjects2.popleft()
                                    # State 81529
                                    if len(subjects2) == 0:
                                        pass
                                        # State 81530
                                        if len(subjects) == 0:
                                            pass
                                            # 67: tan(e + x*f)**(-2)
                                    subjects2.appendleft(tmp427)
                        if pattern_index == 3:
                            pass
                            # State 81510
                            if len(subjects332) == 0:
                                pass
                                # State 81511
                                if len(subjects2) >= 1 and subjects2[0] == 2:
                                    tmp428 = subjects2.popleft()
                                    # State 81512
                                    if len(subjects2) == 0:
                                        pass
                                        # State 81513
                                        if len(subjects) == 0:
                                            pass
                                            # 66: tan(c + x*d)**2
                                    subjects2.appendleft(tmp428)
                        if pattern_index == 4:
                            pass
                            # State 81671
                            if len(subjects332) == 0:
                                pass
                                # State 81672
                                if len(subjects2) >= 1 and subjects2[0] == 2:
                                    tmp429 = subjects2.popleft()
                                    # State 81673
                                    if len(subjects2) == 0:
                                        pass
                                        # State 81674
                                        if len(subjects) == 0:
                                            pass
                                            # 68: tan(e + x*f)**2
                                    subjects2.appendleft(tmp429)
                        if pattern_index == 5:
                            pass
                            # State 99928
                            if len(subjects332) == 0:
                                pass
                                # State 99929
                                if len(subjects2) >= 1 and subjects2[0] == -1:
                                    tmp430 = subjects2.popleft()
                                    # State 99930
                                    if len(subjects2) == 0:
                                        pass
                                        # State 99931
                                        if len(subjects) == 0:
                                            pass
                                            # 101: 1/tan(e + x*f)
                                    subjects2.appendleft(tmp430)
                                if len(subjects2) >= 1 and subjects2[0] == -2:
                                    tmp431 = subjects2.popleft()
                                    # State 99969
                                    if len(subjects2) == 0:
                                        pass
                                        # State 99970
                                        if len(subjects) == 0:
                                            pass
                                            # 102: tan(e + x*f)**(-2)
                                    subjects2.appendleft(tmp431)
                    subjects332.appendleft(tmp411)
                subjects2.appendleft(tmp331)
            if len(subjects2) >= 1 and isinstance(subjects2[0], Pow):
                tmp432 = subjects2.popleft()
                subjects433 = deque(tmp432._args)
                # State 100204
                if len(subjects433) >= 1 and isinstance(subjects433[0], tan):
                    tmp434 = subjects433.popleft()
                    subjects435 = deque(tmp434._args)
                    # State 100205
                    subst1 = Substitution(subst0)
                    try:
                        subst1.try_add_variable('i2.1.1.4.0', S(0))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 100206
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.1.1.4.1.0_1', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 100207
                            if len(subjects435) >= 1:
                                tmp438 = subjects435.popleft()
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i2.1.1.4.1.0', tmp438)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 100208
                                    if len(subjects435) == 0:
                                        pass
                                        # State 100209
                                        if len(subjects433) >= 1 and subjects433[0] == -1:
                                            tmp440 = subjects433.popleft()
                                            # State 100210
                                            if len(subjects433) == 0:
                                                pass
                                                # State 100211
                                                if len(subjects2) >= 1:
                                                    tmp441 = subjects2.popleft()
                                                    subst4 = Substitution(subst3)
                                                    try:
                                                        subst4.try_add_variable('i2.1.1.5', tmp441)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 100212
                                                        if len(subjects2) == 0:
                                                            pass
                                                            # State 100213
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 109: (1/tan(a + x*b))**n1
                                                    subjects2.appendleft(tmp441)
                                                if len(subjects2) >= 1:
                                                    tmp443 = subjects2.popleft()
                                                    subst4 = Substitution(subst3)
                                                    try:
                                                        subst4.try_add_variable('i2.1.1.5_1', tmp443)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 100267
                                                        if len(subjects2) == 0:
                                                            pass
                                                            # State 100268
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 110: (1/tan(a + x*b))**n2
                                                    subjects2.appendleft(tmp443)
                                                subst4 = Substitution(subst3)
                                                try:
                                                    subst4.try_add_variable('i2.1.1.5_2', 1)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 100357
                                                    if len(subjects2) == 0:
                                                        pass
                                                        # State 100358
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 111: (1/tan(a + x*b))**n
                                                if len(subjects2) >= 1:
                                                    tmp446 = subjects2.popleft()
                                                    subst4 = Substitution(subst3)
                                                    try:
                                                        subst4.try_add_variable('i2.1.1.5_2', tmp446)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 100357
                                                        if len(subjects2) == 0:
                                                            pass
                                                            # State 100358
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 111: (1/tan(a + x*b))**n
                                                    subjects2.appendleft(tmp446)
                                            subjects433.appendleft(tmp440)
                                subjects435.appendleft(tmp438)
                        if len(subjects435) >= 1 and isinstance(subjects435[0], Mul):
                            tmp448 = subjects435.popleft()
                            associative1 = tmp448
                            associative_type1 = type(tmp448)
                            subjects449 = deque(tmp448._args)
                            matcher = CommutativeMatcher100215.get()
                            tmp450 = subjects449
                            subjects449 = []
                            for s in tmp450:
                                matcher.add_subject(s)
                            for pattern_index, subst2 in matcher.match(tmp450, subst1):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 100216
                                    if len(subjects435) == 0:
                                        pass
                                        # State 100217
                                        if len(subjects433) >= 1 and subjects433[0] == -1:
                                            tmp451 = subjects433.popleft()
                                            # State 100218
                                            if len(subjects433) == 0:
                                                pass
                                                # State 100219
                                                if len(subjects2) >= 1:
                                                    tmp452 = subjects2.popleft()
                                                    subst3 = Substitution(subst2)
                                                    try:
                                                        subst3.try_add_variable('i2.1.1.5', tmp452)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 100220
                                                        if len(subjects2) == 0:
                                                            pass
                                                            # State 100221
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 109: (1/tan(a + x*b))**n1
                                                    subjects2.appendleft(tmp452)
                                                if len(subjects2) >= 1:
                                                    tmp454 = subjects2.popleft()
                                                    subst3 = Substitution(subst2)
                                                    try:
                                                        subst3.try_add_variable('i2.1.1.5_1', tmp454)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 100269
                                                        if len(subjects2) == 0:
                                                            pass
                                                            # State 100270
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 110: (1/tan(a + x*b))**n2
                                                    subjects2.appendleft(tmp454)
                                                subst3 = Substitution(subst2)
                                                try:
                                                    subst3.try_add_variable('i2.1.1.5_2', 1)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 100359
                                                    if len(subjects2) == 0:
                                                        pass
                                                        # State 100360
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 111: (1/tan(a + x*b))**n
                                                if len(subjects2) >= 1:
                                                    tmp457 = subjects2.popleft()
                                                    subst3 = Substitution(subst2)
                                                    try:
                                                        subst3.try_add_variable('i2.1.1.5_2', tmp457)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 100359
                                                        if len(subjects2) == 0:
                                                            pass
                                                            # State 100360
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 111: (1/tan(a + x*b))**n
                                                    subjects2.appendleft(tmp457)
                                            subjects433.appendleft(tmp451)
                            subjects435.appendleft(tmp448)
                    if len(subjects435) >= 1 and isinstance(subjects435[0], Add):
                        tmp459 = subjects435.popleft()
                        associative1 = tmp459
                        associative_type1 = type(tmp459)
                        subjects460 = deque(tmp459._args)
                        matcher = CommutativeMatcher100223.get()
                        tmp461 = subjects460
                        subjects460 = []
                        for s in tmp461:
                            matcher.add_subject(s)
                        for pattern_index, subst1 in matcher.match(tmp461, subst0):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 100229
                                if len(subjects435) == 0:
                                    pass
                                    # State 100230
                                    if len(subjects433) >= 1 and subjects433[0] == -1:
                                        tmp462 = subjects433.popleft()
                                        # State 100231
                                        if len(subjects433) == 0:
                                            pass
                                            # State 100232
                                            if len(subjects2) >= 1:
                                                tmp463 = subjects2.popleft()
                                                subst2 = Substitution(subst1)
                                                try:
                                                    subst2.try_add_variable('i2.1.1.5', tmp463)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 100233
                                                    if len(subjects2) == 0:
                                                        pass
                                                        # State 100234
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 109: (1/tan(a + x*b))**n1
                                                subjects2.appendleft(tmp463)
                                            if len(subjects2) >= 1:
                                                tmp465 = subjects2.popleft()
                                                subst2 = Substitution(subst1)
                                                try:
                                                    subst2.try_add_variable('i2.1.1.5_1', tmp465)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 100271
                                                    if len(subjects2) == 0:
                                                        pass
                                                        # State 100272
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 110: (1/tan(a + x*b))**n2
                                                subjects2.appendleft(tmp465)
                                            subst2 = Substitution(subst1)
                                            try:
                                                subst2.try_add_variable('i2.1.1.5_2', 1)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 100361
                                                if len(subjects2) == 0:
                                                    pass
                                                    # State 100362
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 111: (1/tan(a + x*b))**n
                                            if len(subjects2) >= 1:
                                                tmp468 = subjects2.popleft()
                                                subst2 = Substitution(subst1)
                                                try:
                                                    subst2.try_add_variable('i2.1.1.5_2', tmp468)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 100361
                                                    if len(subjects2) == 0:
                                                        pass
                                                        # State 100362
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 111: (1/tan(a + x*b))**n
                                                subjects2.appendleft(tmp468)
                                        subjects433.appendleft(tmp462)
                        subjects435.appendleft(tmp459)
                    subjects433.appendleft(tmp434)
                if len(subjects433) >= 1 and isinstance(subjects433[0], cos):
                    tmp470 = subjects433.popleft()
                    subjects471 = deque(tmp470._args)
                    # State 100526
                    subst1 = Substitution(subst0)
                    try:
                        subst1.try_add_variable('i2.1.1.4.0', S(0))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 100527
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.1.1.4.1.0_1', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 100528
                            if len(subjects471) >= 1:
                                tmp474 = subjects471.popleft()
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i2.1.1.4.1.0', tmp474)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 100529
                                    if len(subjects471) == 0:
                                        pass
                                        # State 100530
                                        if len(subjects433) >= 1 and subjects433[0] == -1:
                                            tmp476 = subjects433.popleft()
                                            # State 100531
                                            if len(subjects433) == 0:
                                                pass
                                                # State 100532
                                                if len(subjects2) >= 1:
                                                    tmp477 = subjects2.popleft()
                                                    subst4 = Substitution(subst3)
                                                    try:
                                                        subst4.try_add_variable('i2.1.1.5', tmp477)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 100533
                                                        if len(subjects2) == 0:
                                                            pass
                                                            # State 100534
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 114: (1/cos(a + x*b))**n1
                                                    subjects2.appendleft(tmp477)
                                                if len(subjects2) >= 1:
                                                    tmp479 = subjects2.popleft()
                                                    subst4 = Substitution(subst3)
                                                    try:
                                                        subst4.try_add_variable('i2.1.1.5_1', tmp479)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 100587
                                                        if len(subjects2) == 0:
                                                            pass
                                                            # State 100588
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 115: (1/cos(a + x*b))**n2
                                                    subjects2.appendleft(tmp479)
                                                subst4 = Substitution(subst3)
                                                try:
                                                    subst4.try_add_variable('i2.1.1.5_2', 1)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 100672
                                                    if len(subjects2) == 0:
                                                        pass
                                                        # State 100673
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 116: (1/cos(a + x*b))**n
                                                if len(subjects2) >= 1:
                                                    tmp482 = subjects2.popleft()
                                                    subst4 = Substitution(subst3)
                                                    try:
                                                        subst4.try_add_variable('i2.1.1.5_2', tmp482)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 100672
                                                        if len(subjects2) == 0:
                                                            pass
                                                            # State 100673
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 116: (1/cos(a + x*b))**n
                                                    subjects2.appendleft(tmp482)
                                            subjects433.appendleft(tmp476)
                                subjects471.appendleft(tmp474)
                        if len(subjects471) >= 1 and isinstance(subjects471[0], Mul):
                            tmp484 = subjects471.popleft()
                            associative1 = tmp484
                            associative_type1 = type(tmp484)
                            subjects485 = deque(tmp484._args)
                            matcher = CommutativeMatcher100536.get()
                            tmp486 = subjects485
                            subjects485 = []
                            for s in tmp486:
                                matcher.add_subject(s)
                            for pattern_index, subst2 in matcher.match(tmp486, subst1):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 100537
                                    if len(subjects471) == 0:
                                        pass
                                        # State 100538
                                        if len(subjects433) >= 1 and subjects433[0] == -1:
                                            tmp487 = subjects433.popleft()
                                            # State 100539
                                            if len(subjects433) == 0:
                                                pass
                                                # State 100540
                                                if len(subjects2) >= 1:
                                                    tmp488 = subjects2.popleft()
                                                    subst3 = Substitution(subst2)
                                                    try:
                                                        subst3.try_add_variable('i2.1.1.5', tmp488)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 100541
                                                        if len(subjects2) == 0:
                                                            pass
                                                            # State 100542
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 114: (1/cos(a + x*b))**n1
                                                    subjects2.appendleft(tmp488)
                                                if len(subjects2) >= 1:
                                                    tmp490 = subjects2.popleft()
                                                    subst3 = Substitution(subst2)
                                                    try:
                                                        subst3.try_add_variable('i2.1.1.5_1', tmp490)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 100589
                                                        if len(subjects2) == 0:
                                                            pass
                                                            # State 100590
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 115: (1/cos(a + x*b))**n2
                                                    subjects2.appendleft(tmp490)
                                                subst3 = Substitution(subst2)
                                                try:
                                                    subst3.try_add_variable('i2.1.1.5_2', 1)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 100674
                                                    if len(subjects2) == 0:
                                                        pass
                                                        # State 100675
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 116: (1/cos(a + x*b))**n
                                                if len(subjects2) >= 1:
                                                    tmp493 = subjects2.popleft()
                                                    subst3 = Substitution(subst2)
                                                    try:
                                                        subst3.try_add_variable('i2.1.1.5_2', tmp493)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 100674
                                                        if len(subjects2) == 0:
                                                            pass
                                                            # State 100675
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 116: (1/cos(a + x*b))**n
                                                    subjects2.appendleft(tmp493)
                                            subjects433.appendleft(tmp487)
                            subjects471.appendleft(tmp484)
                    if len(subjects471) >= 1 and isinstance(subjects471[0], Add):
                        tmp495 = subjects471.popleft()
                        associative1 = tmp495
                        associative_type1 = type(tmp495)
                        subjects496 = deque(tmp495._args)
                        matcher = CommutativeMatcher100544.get()
                        tmp497 = subjects496
                        subjects496 = []
                        for s in tmp497:
                            matcher.add_subject(s)
                        for pattern_index, subst1 in matcher.match(tmp497, subst0):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 100550
                                if len(subjects471) == 0:
                                    pass
                                    # State 100551
                                    if len(subjects433) >= 1 and subjects433[0] == -1:
                                        tmp498 = subjects433.popleft()
                                        # State 100552
                                        if len(subjects433) == 0:
                                            pass
                                            # State 100553
                                            if len(subjects2) >= 1:
                                                tmp499 = subjects2.popleft()
                                                subst2 = Substitution(subst1)
                                                try:
                                                    subst2.try_add_variable('i2.1.1.5', tmp499)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 100554
                                                    if len(subjects2) == 0:
                                                        pass
                                                        # State 100555
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 114: (1/cos(a + x*b))**n1
                                                subjects2.appendleft(tmp499)
                                            if len(subjects2) >= 1:
                                                tmp501 = subjects2.popleft()
                                                subst2 = Substitution(subst1)
                                                try:
                                                    subst2.try_add_variable('i2.1.1.5_1', tmp501)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 100591
                                                    if len(subjects2) == 0:
                                                        pass
                                                        # State 100592
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 115: (1/cos(a + x*b))**n2
                                                subjects2.appendleft(tmp501)
                                            subst2 = Substitution(subst1)
                                            try:
                                                subst2.try_add_variable('i2.1.1.5_2', 1)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 100676
                                                if len(subjects2) == 0:
                                                    pass
                                                    # State 100677
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 116: (1/cos(a + x*b))**n
                                            if len(subjects2) >= 1:
                                                tmp504 = subjects2.popleft()
                                                subst2 = Substitution(subst1)
                                                try:
                                                    subst2.try_add_variable('i2.1.1.5_2', tmp504)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 100676
                                                    if len(subjects2) == 0:
                                                        pass
                                                        # State 100677
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 116: (1/cos(a + x*b))**n
                                                subjects2.appendleft(tmp504)
                                        subjects433.appendleft(tmp498)
                        subjects471.appendleft(tmp495)
                    subjects433.appendleft(tmp470)
                if len(subjects433) >= 1 and isinstance(subjects433[0], sin):
                    tmp506 = subjects433.popleft()
                    subjects507 = deque(tmp506._args)
                    # State 100713
                    subst1 = Substitution(subst0)
                    try:
                        subst1.try_add_variable('i2.1.1.4.0', S(0))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 100714
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.1.1.4.1.0_1', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 100715
                            if len(subjects507) >= 1:
                                tmp510 = subjects507.popleft()
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i2.1.1.4.1.0', tmp510)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 100716
                                    if len(subjects507) == 0:
                                        pass
                                        # State 100717
                                        if len(subjects433) >= 1 and subjects433[0] == -1:
                                            tmp512 = subjects433.popleft()
                                            # State 100718
                                            if len(subjects433) == 0:
                                                pass
                                                # State 100719
                                                if len(subjects2) >= 1:
                                                    tmp513 = subjects2.popleft()
                                                    subst4 = Substitution(subst3)
                                                    try:
                                                        subst4.try_add_variable('i2.1.1.5', tmp513)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 100720
                                                        if len(subjects2) == 0:
                                                            pass
                                                            # State 100721
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 117: (1/sin(a + x*b))**n1
                                                    subjects2.appendleft(tmp513)
                                                if len(subjects2) >= 1:
                                                    tmp515 = subjects2.popleft()
                                                    subst4 = Substitution(subst3)
                                                    try:
                                                        subst4.try_add_variable('i2.1.1.5_1', tmp515)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 100774
                                                        if len(subjects2) == 0:
                                                            pass
                                                            # State 100775
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 118: (1/sin(a + x*b))**n2
                                                    subjects2.appendleft(tmp515)
                                                subst4 = Substitution(subst3)
                                                try:
                                                    subst4.try_add_variable('i2.1.1.5_2', 1)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 100859
                                                    if len(subjects2) == 0:
                                                        pass
                                                        # State 100860
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 119: (1/sin(a + x*b))**n
                                                if len(subjects2) >= 1:
                                                    tmp518 = subjects2.popleft()
                                                    subst4 = Substitution(subst3)
                                                    try:
                                                        subst4.try_add_variable('i2.1.1.5_2', tmp518)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 100859
                                                        if len(subjects2) == 0:
                                                            pass
                                                            # State 100860
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 119: (1/sin(a + x*b))**n
                                                    subjects2.appendleft(tmp518)
                                            subjects433.appendleft(tmp512)
                                subjects507.appendleft(tmp510)
                        if len(subjects507) >= 1 and isinstance(subjects507[0], Mul):
                            tmp520 = subjects507.popleft()
                            associative1 = tmp520
                            associative_type1 = type(tmp520)
                            subjects521 = deque(tmp520._args)
                            matcher = CommutativeMatcher100723.get()
                            tmp522 = subjects521
                            subjects521 = []
                            for s in tmp522:
                                matcher.add_subject(s)
                            for pattern_index, subst2 in matcher.match(tmp522, subst1):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 100724
                                    if len(subjects507) == 0:
                                        pass
                                        # State 100725
                                        if len(subjects433) >= 1 and subjects433[0] == -1:
                                            tmp523 = subjects433.popleft()
                                            # State 100726
                                            if len(subjects433) == 0:
                                                pass
                                                # State 100727
                                                if len(subjects2) >= 1:
                                                    tmp524 = subjects2.popleft()
                                                    subst3 = Substitution(subst2)
                                                    try:
                                                        subst3.try_add_variable('i2.1.1.5', tmp524)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 100728
                                                        if len(subjects2) == 0:
                                                            pass
                                                            # State 100729
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 117: (1/sin(a + x*b))**n1
                                                    subjects2.appendleft(tmp524)
                                                if len(subjects2) >= 1:
                                                    tmp526 = subjects2.popleft()
                                                    subst3 = Substitution(subst2)
                                                    try:
                                                        subst3.try_add_variable('i2.1.1.5_1', tmp526)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 100776
                                                        if len(subjects2) == 0:
                                                            pass
                                                            # State 100777
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 118: (1/sin(a + x*b))**n2
                                                    subjects2.appendleft(tmp526)
                                                subst3 = Substitution(subst2)
                                                try:
                                                    subst3.try_add_variable('i2.1.1.5_2', 1)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 100861
                                                    if len(subjects2) == 0:
                                                        pass
                                                        # State 100862
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 119: (1/sin(a + x*b))**n
                                                if len(subjects2) >= 1:
                                                    tmp529 = subjects2.popleft()
                                                    subst3 = Substitution(subst2)
                                                    try:
                                                        subst3.try_add_variable('i2.1.1.5_2', tmp529)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 100861
                                                        if len(subjects2) == 0:
                                                            pass
                                                            # State 100862
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 119: (1/sin(a + x*b))**n
                                                    subjects2.appendleft(tmp529)
                                            subjects433.appendleft(tmp523)
                            subjects507.appendleft(tmp520)
                    if len(subjects507) >= 1 and isinstance(subjects507[0], Add):
                        tmp531 = subjects507.popleft()
                        associative1 = tmp531
                        associative_type1 = type(tmp531)
                        subjects532 = deque(tmp531._args)
                        matcher = CommutativeMatcher100731.get()
                        tmp533 = subjects532
                        subjects532 = []
                        for s in tmp533:
                            matcher.add_subject(s)
                        for pattern_index, subst1 in matcher.match(tmp533, subst0):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 100737
                                if len(subjects507) == 0:
                                    pass
                                    # State 100738
                                    if len(subjects433) >= 1 and subjects433[0] == -1:
                                        tmp534 = subjects433.popleft()
                                        # State 100739
                                        if len(subjects433) == 0:
                                            pass
                                            # State 100740
                                            if len(subjects2) >= 1:
                                                tmp535 = subjects2.popleft()
                                                subst2 = Substitution(subst1)
                                                try:
                                                    subst2.try_add_variable('i2.1.1.5', tmp535)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 100741
                                                    if len(subjects2) == 0:
                                                        pass
                                                        # State 100742
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 117: (1/sin(a + x*b))**n1
                                                subjects2.appendleft(tmp535)
                                            if len(subjects2) >= 1:
                                                tmp537 = subjects2.popleft()
                                                subst2 = Substitution(subst1)
                                                try:
                                                    subst2.try_add_variable('i2.1.1.5_1', tmp537)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 100778
                                                    if len(subjects2) == 0:
                                                        pass
                                                        # State 100779
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 118: (1/sin(a + x*b))**n2
                                                subjects2.appendleft(tmp537)
                                            subst2 = Substitution(subst1)
                                            try:
                                                subst2.try_add_variable('i2.1.1.5_2', 1)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 100863
                                                if len(subjects2) == 0:
                                                    pass
                                                    # State 100864
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 119: (1/sin(a + x*b))**n
                                            if len(subjects2) >= 1:
                                                tmp540 = subjects2.popleft()
                                                subst2 = Substitution(subst1)
                                                try:
                                                    subst2.try_add_variable('i2.1.1.5_2', tmp540)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 100863
                                                    if len(subjects2) == 0:
                                                        pass
                                                        # State 100864
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 119: (1/sin(a + x*b))**n
                                                subjects2.appendleft(tmp540)
                                        subjects433.appendleft(tmp534)
                        subjects507.appendleft(tmp531)
                    subjects433.appendleft(tmp506)
                subjects2.appendleft(tmp432)
            subjects.appendleft(tmp1)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.1.1.2', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 9133
            if len(subjects) >= 1:
                tmp543 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.1', tmp543)
                except ValueError:
                    pass
                else:
                    pass
                    # State 9134
                    if len(subjects) == 0:
                        pass
                        # 9: x**m
                subjects.appendleft(tmp543)
            if len(subjects) >= 1:
                tmp545 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.0_1', tmp545)
                except ValueError:
                    pass
                else:
                    pass
                    # State 11337
                    if len(subjects) == 0:
                        pass
                        # 13: x**q
                subjects.appendleft(tmp545)
            if len(subjects) >= 1:
                tmp547 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.0', tmp547)
                except ValueError:
                    pass
                else:
                    pass
                    # State 11714
                    if len(subjects) == 0:
                        pass
                        # 16: x**n2
                subjects.appendleft(tmp547)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.2', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 11301
            if len(subjects) >= 1:
                tmp550 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.1', tmp550)
                except ValueError:
                    pass
                else:
                    pass
                    # State 11302
                    if len(subjects) == 0:
                        pass
                        # 10: x**n
                subjects.appendleft(tmp550)
            if len(subjects) >= 1:
                tmp552 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.0_1', tmp552)
                except ValueError:
                    pass
                else:
                    pass
                    # State 11328
                    if len(subjects) == 0:
                        pass
                        # 12: x**mn
                subjects.appendleft(tmp552)
            if len(subjects) >= 1:
                tmp554 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.0', tmp554)
                except ValueError:
                    pass
                else:
                    pass
                    # State 11721
                    if len(subjects) == 0:
                        pass
                        # 17: x**non2
                subjects.appendleft(tmp554)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.1.1.2_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 11313
            if len(subjects) >= 1:
                tmp557 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.1', tmp557)
                except ValueError:
                    pass
                else:
                    pass
                    # State 11314
                    if len(subjects) == 0:
                        pass
                        # 11: x**r
                subjects.appendleft(tmp557)
            if len(subjects) >= 1:
                tmp559 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.0_1', tmp559)
                except ValueError:
                    pass
                else:
                    pass
                    # State 11345
                    if len(subjects) == 0:
                        pass
                        # 14: x**r
                subjects.appendleft(tmp559)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.2_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 11809
            if len(subjects) >= 1:
                tmp562 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.1', tmp562)
                except ValueError:
                    pass
                else:
                    pass
                    # State 11810
                    if len(subjects) == 0:
                        pass
                        # 18: x**n
                subjects.appendleft(tmp562)
            if len(subjects) >= 1:
                tmp564 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.0', tmp564)
                except ValueError:
                    pass
                else:
                    pass
                    # State 11830
                    if len(subjects) == 0:
                        pass
                        # 19: x**n2
                subjects.appendleft(tmp564)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.1.1.2_2', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 11899
            if len(subjects) >= 1:
                tmp567 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.1', tmp567)
                except ValueError:
                    pass
                else:
                    pass
                    # State 11900
                    if len(subjects) == 0:
                        pass
                        # 20: x**s
                subjects.appendleft(tmp567)
            if len(subjects) >= 1:
                tmp569 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.0_1', tmp569)
                except ValueError:
                    pass
                else:
                    pass
                    # State 11922
                    if len(subjects) == 0:
                        pass
                        # 21: x**s
                subjects.appendleft(tmp569)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.2_2', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 14409
            if len(subjects) >= 1:
                tmp572 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.1', tmp572)
                except ValueError:
                    pass
                else:
                    pass
                    # State 14410
                    if len(subjects) == 0:
                        pass
                        # 22: x**r
                subjects.appendleft(tmp572)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.1.1.1.0', S(0))
        except ValueError:
            pass
        else:
            pass
            # State 16949
            subst2 = Substitution(subst1)
            try:
                subst2.try_add_variable('i2.1.1.1.1.0', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 16950
                if len(subjects) >= 1:
                    tmp576 = subjects.popleft()
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.3.0', tmp576)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 16951
                        if len(subjects) == 0:
                            pass
                            # 25: f + g*x
                    subjects.appendleft(tmp576)
            if len(subjects) >= 1 and isinstance(subjects[0], Mul):
                tmp578 = subjects.popleft()
                associative1 = tmp578
                associative_type1 = type(tmp578)
                subjects579 = deque(tmp578._args)
                matcher = CommutativeMatcher16953.get()
                tmp580 = subjects579
                subjects579 = []
                for s in tmp580:
                    matcher.add_subject(s)
                for pattern_index, subst2 in matcher.match(tmp580, subst1):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 16954
                        if len(subjects) == 0:
                            pass
                            # 25: f + g*x
                subjects.appendleft(tmp578)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.1.1.3_2', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 99773
            if len(subjects) >= 1 and isinstance(subjects[0], sin):
                tmp582 = subjects.popleft()
                subjects583 = deque(tmp582._args)
                # State 99774
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.1.1.3.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 99775
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.1.1.3.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 99776
                        if len(subjects583) >= 1:
                            tmp586 = subjects583.popleft()
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i2.1.1.3.1.0', tmp586)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 99777
                                if len(subjects583) == 0:
                                    pass
                                    # State 99778
                                    if len(subjects) == 0:
                                        pass
                                        # 97: sin(c + x*d)**n
                            subjects583.appendleft(tmp586)
                    if len(subjects583) >= 1 and isinstance(subjects583[0], Mul):
                        tmp588 = subjects583.popleft()
                        associative1 = tmp588
                        associative_type1 = type(tmp588)
                        subjects589 = deque(tmp588._args)
                        matcher = CommutativeMatcher99780.get()
                        tmp590 = subjects589
                        subjects589 = []
                        for s in tmp590:
                            matcher.add_subject(s)
                        for pattern_index, subst3 in matcher.match(tmp590, subst2):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 99781
                                if len(subjects583) == 0:
                                    pass
                                    # State 99782
                                    if len(subjects) == 0:
                                        pass
                                        # 97: sin(c + x*d)**n
                        subjects583.appendleft(tmp588)
                if len(subjects583) >= 1 and isinstance(subjects583[0], Add):
                    tmp591 = subjects583.popleft()
                    associative1 = tmp591
                    associative_type1 = type(tmp591)
                    subjects592 = deque(tmp591._args)
                    matcher = CommutativeMatcher99784.get()
                    tmp593 = subjects592
                    subjects592 = []
                    for s in tmp593:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp593, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 99790
                            if len(subjects583) == 0:
                                pass
                                # State 99791
                                if len(subjects) == 0:
                                    pass
                                    # 97: sin(c + x*d)**n
                    subjects583.appendleft(tmp591)
                subjects.appendleft(tmp582)
            if len(subjects) >= 1 and isinstance(subjects[0], cos):
                tmp594 = subjects.popleft()
                subjects595 = deque(tmp594._args)
                # State 99853
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.1.1.3.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 99854
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.1.1.3.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 99855
                        if len(subjects595) >= 1:
                            tmp598 = subjects595.popleft()
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i2.1.1.3.1.0', tmp598)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 99856
                                if len(subjects595) == 0:
                                    pass
                                    # State 99857
                                    if len(subjects) == 0:
                                        pass
                                        # 100: cos(c + x*d)**n
                            subjects595.appendleft(tmp598)
                    if len(subjects595) >= 1 and isinstance(subjects595[0], Mul):
                        tmp600 = subjects595.popleft()
                        associative1 = tmp600
                        associative_type1 = type(tmp600)
                        subjects601 = deque(tmp600._args)
                        matcher = CommutativeMatcher99859.get()
                        tmp602 = subjects601
                        subjects601 = []
                        for s in tmp602:
                            matcher.add_subject(s)
                        for pattern_index, subst3 in matcher.match(tmp602, subst2):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 99860
                                if len(subjects595) == 0:
                                    pass
                                    # State 99861
                                    if len(subjects) == 0:
                                        pass
                                        # 100: cos(c + x*d)**n
                        subjects595.appendleft(tmp600)
                if len(subjects595) >= 1 and isinstance(subjects595[0], Add):
                    tmp603 = subjects595.popleft()
                    associative1 = tmp603
                    associative_type1 = type(tmp603)
                    subjects604 = deque(tmp603._args)
                    matcher = CommutativeMatcher99863.get()
                    tmp605 = subjects604
                    subjects604 = []
                    for s in tmp605:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp605, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 99869
                            if len(subjects595) == 0:
                                pass
                                # State 99870
                                if len(subjects) == 0:
                                    pass
                                    # 100: cos(c + x*d)**n
                    subjects595.appendleft(tmp603)
                subjects.appendleft(tmp594)
            if len(subjects) >= 1 and isinstance(subjects[0], tan):
                tmp606 = subjects.popleft()
                subjects607 = deque(tmp606._args)
                # State 100144
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.1.1.3.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 100145
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.1.1.3.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 100146
                        if len(subjects607) >= 1:
                            tmp610 = subjects607.popleft()
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i2.1.1.3.1.0', tmp610)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 100147
                                if len(subjects607) == 0:
                                    pass
                                    # State 100148
                                    if len(subjects) == 0:
                                        pass
                                        # 108: tan(e + x*f)**n
                            subjects607.appendleft(tmp610)
                    if len(subjects607) >= 1 and isinstance(subjects607[0], Mul):
                        tmp612 = subjects607.popleft()
                        associative1 = tmp612
                        associative_type1 = type(tmp612)
                        subjects613 = deque(tmp612._args)
                        matcher = CommutativeMatcher100150.get()
                        tmp614 = subjects613
                        subjects613 = []
                        for s in tmp614:
                            matcher.add_subject(s)
                        for pattern_index, subst3 in matcher.match(tmp614, subst2):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 100151
                                if len(subjects607) == 0:
                                    pass
                                    # State 100152
                                    if len(subjects) == 0:
                                        pass
                                        # 108: tan(e + x*f)**n
                        subjects607.appendleft(tmp612)
                if len(subjects607) >= 1 and isinstance(subjects607[0], Add):
                    tmp615 = subjects607.popleft()
                    associative1 = tmp615
                    associative_type1 = type(tmp615)
                    subjects616 = deque(tmp615._args)
                    matcher = CommutativeMatcher100154.get()
                    tmp617 = subjects616
                    subjects616 = []
                    for s in tmp617:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp617, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 100160
                            if len(subjects607) == 0:
                                pass
                                # State 100161
                                if len(subjects) == 0:
                                    pass
                                    # 108: tan(e + x*f)**n
                    subjects607.appendleft(tmp615)
                subjects.appendleft(tmp606)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.1.1.5_2', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 100331
            if len(subjects) >= 1 and isinstance(subjects[0], Pow):
                tmp619 = subjects.popleft()
                subjects620 = deque(tmp619._args)
                # State 100332
                if len(subjects620) >= 1 and isinstance(subjects620[0], tan):
                    tmp621 = subjects620.popleft()
                    subjects622 = deque(tmp621._args)
                    # State 100333
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.1.1.4.0', S(0))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 100334
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.1.1.4.1.0_1', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 100335
                            if len(subjects622) >= 1:
                                tmp625 = subjects622.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.1.1.4.1.0', tmp625)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 100336
                                    if len(subjects622) == 0:
                                        pass
                                        # State 100337
                                        if len(subjects620) >= 1 and subjects620[0] == -1:
                                            tmp627 = subjects620.popleft()
                                            # State 100338
                                            if len(subjects620) == 0:
                                                pass
                                                # State 100339
                                                if len(subjects) == 0:
                                                    pass
                                                    # 111: (1/tan(a + x*b))**n
                                            subjects620.appendleft(tmp627)
                                subjects622.appendleft(tmp625)
                        if len(subjects622) >= 1 and isinstance(subjects622[0], Mul):
                            tmp628 = subjects622.popleft()
                            associative1 = tmp628
                            associative_type1 = type(tmp628)
                            subjects629 = deque(tmp628._args)
                            matcher = CommutativeMatcher100341.get()
                            tmp630 = subjects629
                            subjects629 = []
                            for s in tmp630:
                                matcher.add_subject(s)
                            for pattern_index, subst3 in matcher.match(tmp630, subst2):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 100342
                                    if len(subjects622) == 0:
                                        pass
                                        # State 100343
                                        if len(subjects620) >= 1 and subjects620[0] == -1:
                                            tmp631 = subjects620.popleft()
                                            # State 100344
                                            if len(subjects620) == 0:
                                                pass
                                                # State 100345
                                                if len(subjects) == 0:
                                                    pass
                                                    # 111: (1/tan(a + x*b))**n
                                            subjects620.appendleft(tmp631)
                            subjects622.appendleft(tmp628)
                    if len(subjects622) >= 1 and isinstance(subjects622[0], Add):
                        tmp632 = subjects622.popleft()
                        associative1 = tmp632
                        associative_type1 = type(tmp632)
                        subjects633 = deque(tmp632._args)
                        matcher = CommutativeMatcher100347.get()
                        tmp634 = subjects633
                        subjects633 = []
                        for s in tmp634:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp634, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 100353
                                if len(subjects622) == 0:
                                    pass
                                    # State 100354
                                    if len(subjects620) >= 1 and subjects620[0] == -1:
                                        tmp635 = subjects620.popleft()
                                        # State 100355
                                        if len(subjects620) == 0:
                                            pass
                                            # State 100356
                                            if len(subjects) == 0:
                                                pass
                                                # 111: (1/tan(a + x*b))**n
                                        subjects620.appendleft(tmp635)
                        subjects622.appendleft(tmp632)
                    subjects620.appendleft(tmp621)
                if len(subjects620) >= 1 and isinstance(subjects620[0], cos):
                    tmp636 = subjects620.popleft()
                    subjects637 = deque(tmp636._args)
                    # State 100648
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.1.1.4.0', S(0))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 100649
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.1.1.4.1.0_1', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 100650
                            if len(subjects637) >= 1:
                                tmp640 = subjects637.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.1.1.4.1.0', tmp640)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 100651
                                    if len(subjects637) == 0:
                                        pass
                                        # State 100652
                                        if len(subjects620) >= 1 and subjects620[0] == -1:
                                            tmp642 = subjects620.popleft()
                                            # State 100653
                                            if len(subjects620) == 0:
                                                pass
                                                # State 100654
                                                if len(subjects) == 0:
                                                    pass
                                                    # 116: (1/cos(a + x*b))**n
                                            subjects620.appendleft(tmp642)
                                subjects637.appendleft(tmp640)
                        if len(subjects637) >= 1 and isinstance(subjects637[0], Mul):
                            tmp643 = subjects637.popleft()
                            associative1 = tmp643
                            associative_type1 = type(tmp643)
                            subjects644 = deque(tmp643._args)
                            matcher = CommutativeMatcher100656.get()
                            tmp645 = subjects644
                            subjects644 = []
                            for s in tmp645:
                                matcher.add_subject(s)
                            for pattern_index, subst3 in matcher.match(tmp645, subst2):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 100657
                                    if len(subjects637) == 0:
                                        pass
                                        # State 100658
                                        if len(subjects620) >= 1 and subjects620[0] == -1:
                                            tmp646 = subjects620.popleft()
                                            # State 100659
                                            if len(subjects620) == 0:
                                                pass
                                                # State 100660
                                                if len(subjects) == 0:
                                                    pass
                                                    # 116: (1/cos(a + x*b))**n
                                            subjects620.appendleft(tmp646)
                            subjects637.appendleft(tmp643)
                    if len(subjects637) >= 1 and isinstance(subjects637[0], Add):
                        tmp647 = subjects637.popleft()
                        associative1 = tmp647
                        associative_type1 = type(tmp647)
                        subjects648 = deque(tmp647._args)
                        matcher = CommutativeMatcher100662.get()
                        tmp649 = subjects648
                        subjects648 = []
                        for s in tmp649:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp649, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 100668
                                if len(subjects637) == 0:
                                    pass
                                    # State 100669
                                    if len(subjects620) >= 1 and subjects620[0] == -1:
                                        tmp650 = subjects620.popleft()
                                        # State 100670
                                        if len(subjects620) == 0:
                                            pass
                                            # State 100671
                                            if len(subjects) == 0:
                                                pass
                                                # 116: (1/cos(a + x*b))**n
                                        subjects620.appendleft(tmp650)
                        subjects637.appendleft(tmp647)
                    subjects620.appendleft(tmp636)
                if len(subjects620) >= 1 and isinstance(subjects620[0], sin):
                    tmp651 = subjects620.popleft()
                    subjects652 = deque(tmp651._args)
                    # State 100835
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.1.1.4.0', S(0))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 100836
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.1.1.4.1.0_1', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 100837
                            if len(subjects652) >= 1:
                                tmp655 = subjects652.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.1.1.4.1.0', tmp655)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 100838
                                    if len(subjects652) == 0:
                                        pass
                                        # State 100839
                                        if len(subjects620) >= 1 and subjects620[0] == -1:
                                            tmp657 = subjects620.popleft()
                                            # State 100840
                                            if len(subjects620) == 0:
                                                pass
                                                # State 100841
                                                if len(subjects) == 0:
                                                    pass
                                                    # 119: (1/sin(a + x*b))**n
                                            subjects620.appendleft(tmp657)
                                subjects652.appendleft(tmp655)
                        if len(subjects652) >= 1 and isinstance(subjects652[0], Mul):
                            tmp658 = subjects652.popleft()
                            associative1 = tmp658
                            associative_type1 = type(tmp658)
                            subjects659 = deque(tmp658._args)
                            matcher = CommutativeMatcher100843.get()
                            tmp660 = subjects659
                            subjects659 = []
                            for s in tmp660:
                                matcher.add_subject(s)
                            for pattern_index, subst3 in matcher.match(tmp660, subst2):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 100844
                                    if len(subjects652) == 0:
                                        pass
                                        # State 100845
                                        if len(subjects620) >= 1 and subjects620[0] == -1:
                                            tmp661 = subjects620.popleft()
                                            # State 100846
                                            if len(subjects620) == 0:
                                                pass
                                                # State 100847
                                                if len(subjects) == 0:
                                                    pass
                                                    # 119: (1/sin(a + x*b))**n
                                            subjects620.appendleft(tmp661)
                            subjects652.appendleft(tmp658)
                    if len(subjects652) >= 1 and isinstance(subjects652[0], Add):
                        tmp662 = subjects652.popleft()
                        associative1 = tmp662
                        associative_type1 = type(tmp662)
                        subjects663 = deque(tmp662._args)
                        matcher = CommutativeMatcher100849.get()
                        tmp664 = subjects663
                        subjects663 = []
                        for s in tmp664:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp664, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 100855
                                if len(subjects652) == 0:
                                    pass
                                    # State 100856
                                    if len(subjects620) >= 1 and subjects620[0] == -1:
                                        tmp665 = subjects620.popleft()
                                        # State 100857
                                        if len(subjects620) == 0:
                                            pass
                                            # State 100858
                                            if len(subjects) == 0:
                                                pass
                                                # 119: (1/sin(a + x*b))**n
                                        subjects620.appendleft(tmp665)
                        subjects652.appendleft(tmp662)
                    subjects620.appendleft(tmp651)
                subjects.appendleft(tmp619)
        if len(subjects) >= 1 and isinstance(subjects[0], Add):
            tmp666 = subjects.popleft()
            associative1 = tmp666
            associative_type1 = type(tmp666)
            subjects667 = deque(tmp666._args)
            matcher = CommutativeMatcher16956.get()
            tmp668 = subjects667
            subjects667 = []
            for s in tmp668:
                matcher.add_subject(s)
            for pattern_index, subst1 in matcher.match(tmp668, subst0):
                pass
                if pattern_index == 0:
                    pass
                    # State 16962
                    if len(subjects) == 0:
                        pass
                        # 25: f + g*x
            subjects.appendleft(tmp666)
        if len(subjects) >= 1 and isinstance(subjects[0], log):
            tmp669 = subjects.popleft()
            subjects670 = deque(tmp669._args)
            # State 16963
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.3.0_1', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 16964
                if len(subjects670) >= 1:
                    tmp672 = subjects670.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.3.0', tmp672)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 16965
                        if len(subjects670) == 0:
                            pass
                            # State 16966
                            if len(subjects) == 0:
                                pass
                                # 26: log(v*c)
                    subjects670.appendleft(tmp672)
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.1.1.2.0', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 24011
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.1.1.2.1.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 24012
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.1.1.2.1.1.0', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 24013
                        if len(subjects670) >= 1:
                            tmp677 = subjects670.popleft()
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i2.2.1.0', tmp677)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 24014
                                if len(subjects670) == 0:
                                    pass
                                    # State 24015
                                    if len(subjects) == 0:
                                        pass
                                        # 27: log(c*(e + f*x))
                            subjects670.appendleft(tmp677)
                    if len(subjects670) >= 1 and isinstance(subjects670[0], Mul):
                        tmp679 = subjects670.popleft()
                        associative1 = tmp679
                        associative_type1 = type(tmp679)
                        subjects680 = deque(tmp679._args)
                        matcher = CommutativeMatcher24017.get()
                        tmp681 = subjects680
                        subjects680 = []
                        for s in tmp681:
                            matcher.add_subject(s)
                        for pattern_index, subst3 in matcher.match(tmp681, subst2):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 24018
                                if len(subjects670) == 0:
                                    pass
                                    # State 24019
                                    if len(subjects) == 0:
                                        pass
                                        # 27: log(c*(e + f*x))
                        subjects670.appendleft(tmp679)
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.1.1.2.2', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 25110
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.1.1.2.2.0', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 25111
                        subst4 = Substitution(subst3)
                        try:
                            subst4.try_add_variable('i2.1.1.2.2.2', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 25112
                            subst5 = Substitution(subst4)
                            try:
                                subst5.try_add_variable('i2.1.1.2.2.2.0', S(0))
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 25113
                                subst6 = Substitution(subst5)
                                try:
                                    subst6.try_add_variable('i2.1.1.2.2.2.1.0', S(1))
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 25114
                                    if len(subjects670) >= 1:
                                        tmp687 = subjects670.popleft()
                                        subst7 = Substitution(subst6)
                                        try:
                                            subst7.try_add_variable('i2.2.1.0', tmp687)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 25115
                                            if len(subjects670) == 0:
                                                pass
                                                # State 25116
                                                if len(subjects) == 0:
                                                    pass
                                                    # 28: log(c*(d*(e + f*x)**p)**q)
                                        subjects670.appendleft(tmp687)
                                    if len(subjects670) >= 1:
                                        tmp689 = subjects670.popleft()
                                        subst7 = Substitution(subst6)
                                        try:
                                            subst7.try_add_variable('i2.2.1.1', tmp689)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 27052
                                            if len(subjects670) == 0:
                                                pass
                                                # State 27053
                                                if len(subjects) == 0:
                                                    pass
                                                    # 31: log(c*(d*(e + f*x)**p)**q)
                                        subjects670.appendleft(tmp689)
                                    if len(subjects670) >= 1:
                                        tmp691 = subjects670.popleft()
                                        subst7 = Substitution(subst6)
                                        try:
                                            subst7.try_add_variable('i2.3.1.0', tmp691)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 28119
                                            if len(subjects670) == 0:
                                                pass
                                                # State 28120
                                                if len(subjects) == 0:
                                                    pass
                                                    # 33: log(c*(d*(e + f*x)**p)**q)
                                        subjects670.appendleft(tmp691)
                                if len(subjects670) >= 1 and isinstance(subjects670[0], Mul):
                                    tmp693 = subjects670.popleft()
                                    associative1 = tmp693
                                    associative_type1 = type(tmp693)
                                    subjects694 = deque(tmp693._args)
                                    matcher = CommutativeMatcher25118.get()
                                    tmp695 = subjects694
                                    subjects694 = []
                                    for s in tmp695:
                                        matcher.add_subject(s)
                                    for pattern_index, subst6 in matcher.match(tmp695, subst5):
                                        pass
                                        if pattern_index == 0:
                                            pass
                                            # State 25119
                                            if len(subjects670) == 0:
                                                pass
                                                # State 25120
                                                if len(subjects) == 0:
                                                    pass
                                                    # 28: log(c*(d*(e + f*x)**p)**q)
                                        if pattern_index == 1:
                                            pass
                                            # State 27054
                                            if len(subjects670) == 0:
                                                pass
                                                # State 27055
                                                if len(subjects) == 0:
                                                    pass
                                                    # 31: log(c*(d*(e + f*x)**p)**q)
                                        if pattern_index == 2:
                                            pass
                                            # State 28121
                                            if len(subjects670) == 0:
                                                pass
                                                # State 28122
                                                if len(subjects) == 0:
                                                    pass
                                                    # 33: log(c*(d*(e + f*x)**p)**q)
                                    subjects670.appendleft(tmp693)
                            if len(subjects670) >= 1 and isinstance(subjects670[0], Add):
                                tmp696 = subjects670.popleft()
                                associative1 = tmp696
                                associative_type1 = type(tmp696)
                                subjects697 = deque(tmp696._args)
                                matcher = CommutativeMatcher25122.get()
                                tmp698 = subjects697
                                subjects697 = []
                                for s in tmp698:
                                    matcher.add_subject(s)
                                for pattern_index, subst5 in matcher.match(tmp698, subst4):
                                    pass
                                    if pattern_index == 0:
                                        pass
                                        # State 25128
                                        if len(subjects670) == 0:
                                            pass
                                            # State 25129
                                            if len(subjects) == 0:
                                                pass
                                                # 28: log(c*(d*(e + f*x)**p)**q)
                                    if pattern_index == 1:
                                        pass
                                        # State 27058
                                        if len(subjects670) == 0:
                                            pass
                                            # State 27059
                                            if len(subjects) == 0:
                                                pass
                                                # 31: log(c*(d*(e + f*x)**p)**q)
                                    if pattern_index == 2:
                                        pass
                                        # State 27402
                                        if len(subjects670) == 0:
                                            pass
                                            # State 27403
                                            if len(subjects) == 0:
                                                pass
                                                # 32: log(c*(d*(e + f*x)**p)**q)
                                    if pattern_index == 3:
                                        pass
                                        # State 28125
                                        if len(subjects670) == 0:
                                            pass
                                            # State 28126
                                            if len(subjects) == 0:
                                                pass
                                                # 33: log(c*(d*(e + f*x)**p)**q)
                                subjects670.appendleft(tmp696)
                        if len(subjects670) >= 1 and isinstance(subjects670[0], Pow):
                            tmp699 = subjects670.popleft()
                            subjects700 = deque(tmp699._args)
                            # State 25130
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i2.1.1.2.2.2.0', S(0))
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 25131
                                subst5 = Substitution(subst4)
                                try:
                                    subst5.try_add_variable('i2.1.1.2.2.2.1.0', S(1))
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 25132
                                    if len(subjects700) >= 1:
                                        tmp703 = subjects700.popleft()
                                        subst6 = Substitution(subst5)
                                        try:
                                            subst6.try_add_variable('i2.2.1.0', tmp703)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 25133
                                            subst7 = Substitution(subst6)
                                            try:
                                                subst7.try_add_variable('i2.1.1.2.2.2', 1)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 25134
                                                if len(subjects700) == 0:
                                                    pass
                                                    # State 25135
                                                    if len(subjects670) == 0:
                                                        pass
                                                        # State 25136
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 28: log(c*(d*(e + f*x)**p)**q)
                                            if len(subjects700) >= 1:
                                                tmp706 = subjects700.popleft()
                                                subst7 = Substitution(subst6)
                                                try:
                                                    subst7.try_add_variable('i2.1.1.2.2.2', tmp706)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 25134
                                                    if len(subjects700) == 0:
                                                        pass
                                                        # State 25135
                                                        if len(subjects670) == 0:
                                                            pass
                                                            # State 25136
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 28: log(c*(d*(e + f*x)**p)**q)
                                                subjects700.appendleft(tmp706)
                                        subjects700.appendleft(tmp703)
                                    if len(subjects700) >= 1:
                                        tmp708 = subjects700.popleft()
                                        subst6 = Substitution(subst5)
                                        try:
                                            subst6.try_add_variable('i2.2.1.1', tmp708)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 27060
                                            subst7 = Substitution(subst6)
                                            try:
                                                subst7.try_add_variable('i2.1.1.2.2.2', 1)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 27061
                                                if len(subjects700) == 0:
                                                    pass
                                                    # State 27062
                                                    if len(subjects670) == 0:
                                                        pass
                                                        # State 27063
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 31: log(c*(d*(e + f*x)**p)**q)
                                            if len(subjects700) >= 1:
                                                tmp711 = subjects700.popleft()
                                                subst7 = Substitution(subst6)
                                                try:
                                                    subst7.try_add_variable('i2.1.1.2.2.2', tmp711)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 27061
                                                    if len(subjects700) == 0:
                                                        pass
                                                        # State 27062
                                                        if len(subjects670) == 0:
                                                            pass
                                                            # State 27063
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 31: log(c*(d*(e + f*x)**p)**q)
                                                subjects700.appendleft(tmp711)
                                        subjects700.appendleft(tmp708)
                                    if len(subjects700) >= 1:
                                        tmp713 = subjects700.popleft()
                                        subst6 = Substitution(subst5)
                                        try:
                                            subst6.try_add_variable('i2.3.1.0', tmp713)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 28127
                                            subst7 = Substitution(subst6)
                                            try:
                                                subst7.try_add_variable('i2.1.1.2.2.2', 1)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 28128
                                                if len(subjects700) == 0:
                                                    pass
                                                    # State 28129
                                                    if len(subjects670) == 0:
                                                        pass
                                                        # State 28130
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 33: log(c*(d*(e + f*x)**p)**q)
                                            if len(subjects700) >= 1:
                                                tmp716 = subjects700.popleft()
                                                subst7 = Substitution(subst6)
                                                try:
                                                    subst7.try_add_variable('i2.1.1.2.2.2', tmp716)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 28128
                                                    if len(subjects700) == 0:
                                                        pass
                                                        # State 28129
                                                        if len(subjects670) == 0:
                                                            pass
                                                            # State 28130
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 33: log(c*(d*(e + f*x)**p)**q)
                                                subjects700.appendleft(tmp716)
                                        subjects700.appendleft(tmp713)
                                if len(subjects700) >= 1 and isinstance(subjects700[0], Mul):
                                    tmp718 = subjects700.popleft()
                                    associative1 = tmp718
                                    associative_type1 = type(tmp718)
                                    subjects719 = deque(tmp718._args)
                                    matcher = CommutativeMatcher25138.get()
                                    tmp720 = subjects719
                                    subjects719 = []
                                    for s in tmp720:
                                        matcher.add_subject(s)
                                    for pattern_index, subst5 in matcher.match(tmp720, subst4):
                                        pass
                                        if pattern_index == 0:
                                            pass
                                            # State 25139
                                            subst6 = Substitution(subst5)
                                            try:
                                                subst6.try_add_variable('i2.1.1.2.2.2', 1)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 25140
                                                if len(subjects700) == 0:
                                                    pass
                                                    # State 25141
                                                    if len(subjects670) == 0:
                                                        pass
                                                        # State 25142
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 28: log(c*(d*(e + f*x)**p)**q)
                                            if len(subjects700) >= 1:
                                                tmp722 = []
                                                tmp722.append(subjects700.popleft())
                                                while True:
                                                    if len(tmp722) > 1:
                                                        tmp723 = create_operation_expression(associative1, tmp722)
                                                    elif len(tmp722) == 1:
                                                        tmp723 = tmp722[0]
                                                    else:
                                                        assert False, "Unreachable"
                                                    subst6 = Substitution(subst5)
                                                    try:
                                                        subst6.try_add_variable('i2.1.1.2.2.2', tmp723)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 25140
                                                        if len(subjects700) == 0:
                                                            pass
                                                            # State 25141
                                                            if len(subjects670) == 0:
                                                                pass
                                                                # State 25142
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 28: log(c*(d*(e + f*x)**p)**q)
                                                    if len(subjects700) == 0:
                                                        break
                                                    tmp722.append(subjects700.popleft())
                                                subjects700.extendleft(reversed(tmp722))
                                        if pattern_index == 1:
                                            pass
                                            # State 27064
                                            subst6 = Substitution(subst5)
                                            try:
                                                subst6.try_add_variable('i2.1.1.2.2.2', 1)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 27065
                                                if len(subjects700) == 0:
                                                    pass
                                                    # State 27066
                                                    if len(subjects670) == 0:
                                                        pass
                                                        # State 27067
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 31: log(c*(d*(e + f*x)**p)**q)
                                            if len(subjects700) >= 1:
                                                tmp726 = []
                                                tmp726.append(subjects700.popleft())
                                                while True:
                                                    if len(tmp726) > 1:
                                                        tmp727 = create_operation_expression(associative1, tmp726)
                                                    elif len(tmp726) == 1:
                                                        tmp727 = tmp726[0]
                                                    else:
                                                        assert False, "Unreachable"
                                                    subst6 = Substitution(subst5)
                                                    try:
                                                        subst6.try_add_variable('i2.1.1.2.2.2', tmp727)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 27065
                                                        if len(subjects700) == 0:
                                                            pass
                                                            # State 27066
                                                            if len(subjects670) == 0:
                                                                pass
                                                                # State 27067
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 31: log(c*(d*(e + f*x)**p)**q)
                                                    if len(subjects700) == 0:
                                                        break
                                                    tmp726.append(subjects700.popleft())
                                                subjects700.extendleft(reversed(tmp726))
                                        if pattern_index == 2:
                                            pass
                                            # State 28131
                                            subst6 = Substitution(subst5)
                                            try:
                                                subst6.try_add_variable('i2.1.1.2.2.2', 1)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 28132
                                                if len(subjects700) == 0:
                                                    pass
                                                    # State 28133
                                                    if len(subjects670) == 0:
                                                        pass
                                                        # State 28134
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 33: log(c*(d*(e + f*x)**p)**q)
                                            if len(subjects700) >= 1:
                                                tmp730 = []
                                                tmp730.append(subjects700.popleft())
                                                while True:
                                                    if len(tmp730) > 1:
                                                        tmp731 = create_operation_expression(associative1, tmp730)
                                                    elif len(tmp730) == 1:
                                                        tmp731 = tmp730[0]
                                                    else:
                                                        assert False, "Unreachable"
                                                    subst6 = Substitution(subst5)
                                                    try:
                                                        subst6.try_add_variable('i2.1.1.2.2.2', tmp731)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 28132
                                                        if len(subjects700) == 0:
                                                            pass
                                                            # State 28133
                                                            if len(subjects670) == 0:
                                                                pass
                                                                # State 28134
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 33: log(c*(d*(e + f*x)**p)**q)
                                                    if len(subjects700) == 0:
                                                        break
                                                    tmp730.append(subjects700.popleft())
                                                subjects700.extendleft(reversed(tmp730))
                                    subjects700.appendleft(tmp718)
                            if len(subjects700) >= 1 and isinstance(subjects700[0], Add):
                                tmp733 = subjects700.popleft()
                                associative1 = tmp733
                                associative_type1 = type(tmp733)
                                subjects734 = deque(tmp733._args)
                                matcher = CommutativeMatcher25144.get()
                                tmp735 = subjects734
                                subjects734 = []
                                for s in tmp735:
                                    matcher.add_subject(s)
                                for pattern_index, subst4 in matcher.match(tmp735, subst3):
                                    pass
                                    if pattern_index == 0:
                                        pass
                                        # State 25150
                                        subst5 = Substitution(subst4)
                                        try:
                                            subst5.try_add_variable('i2.1.1.2.2.2', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 25151
                                            if len(subjects700) == 0:
                                                pass
                                                # State 25152
                                                if len(subjects670) == 0:
                                                    pass
                                                    # State 25153
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 28: log(c*(d*(e + f*x)**p)**q)
                                        if len(subjects700) >= 1:
                                            tmp737 = []
                                            tmp737.append(subjects700.popleft())
                                            while True:
                                                if len(tmp737) > 1:
                                                    tmp738 = create_operation_expression(associative1, tmp737)
                                                elif len(tmp737) == 1:
                                                    tmp738 = tmp737[0]
                                                else:
                                                    assert False, "Unreachable"
                                                subst5 = Substitution(subst4)
                                                try:
                                                    subst5.try_add_variable('i2.1.1.2.2.2', tmp738)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 25151
                                                    if len(subjects700) == 0:
                                                        pass
                                                        # State 25152
                                                        if len(subjects670) == 0:
                                                            pass
                                                            # State 25153
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 28: log(c*(d*(e + f*x)**p)**q)
                                                if len(subjects700) == 0:
                                                    break
                                                tmp737.append(subjects700.popleft())
                                            subjects700.extendleft(reversed(tmp737))
                                    if pattern_index == 1:
                                        pass
                                        # State 27070
                                        subst5 = Substitution(subst4)
                                        try:
                                            subst5.try_add_variable('i2.1.1.2.2.2', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 27071
                                            if len(subjects700) == 0:
                                                pass
                                                # State 27072
                                                if len(subjects670) == 0:
                                                    pass
                                                    # State 27073
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 31: log(c*(d*(e + f*x)**p)**q)
                                        if len(subjects700) >= 1:
                                            tmp741 = []
                                            tmp741.append(subjects700.popleft())
                                            while True:
                                                if len(tmp741) > 1:
                                                    tmp742 = create_operation_expression(associative1, tmp741)
                                                elif len(tmp741) == 1:
                                                    tmp742 = tmp741[0]
                                                else:
                                                    assert False, "Unreachable"
                                                subst5 = Substitution(subst4)
                                                try:
                                                    subst5.try_add_variable('i2.1.1.2.2.2', tmp742)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 27071
                                                    if len(subjects700) == 0:
                                                        pass
                                                        # State 27072
                                                        if len(subjects670) == 0:
                                                            pass
                                                            # State 27073
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 31: log(c*(d*(e + f*x)**p)**q)
                                                if len(subjects700) == 0:
                                                    break
                                                tmp741.append(subjects700.popleft())
                                            subjects700.extendleft(reversed(tmp741))
                                    if pattern_index == 2:
                                        pass
                                        # State 27404
                                        subst5 = Substitution(subst4)
                                        try:
                                            subst5.try_add_variable('i2.1.1.2.2.2', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 27405
                                            if len(subjects700) == 0:
                                                pass
                                                # State 27406
                                                if len(subjects670) == 0:
                                                    pass
                                                    # State 27407
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 32: log(c*(d*(e + f*x)**p)**q)
                                        if len(subjects700) >= 1:
                                            tmp745 = []
                                            tmp745.append(subjects700.popleft())
                                            while True:
                                                if len(tmp745) > 1:
                                                    tmp746 = create_operation_expression(associative1, tmp745)
                                                elif len(tmp745) == 1:
                                                    tmp746 = tmp745[0]
                                                else:
                                                    assert False, "Unreachable"
                                                subst5 = Substitution(subst4)
                                                try:
                                                    subst5.try_add_variable('i2.1.1.2.2.2', tmp746)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 27405
                                                    if len(subjects700) == 0:
                                                        pass
                                                        # State 27406
                                                        if len(subjects670) == 0:
                                                            pass
                                                            # State 27407
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 32: log(c*(d*(e + f*x)**p)**q)
                                                if len(subjects700) == 0:
                                                    break
                                                tmp745.append(subjects700.popleft())
                                            subjects700.extendleft(reversed(tmp745))
                                    if pattern_index == 3:
                                        pass
                                        # State 28137
                                        subst5 = Substitution(subst4)
                                        try:
                                            subst5.try_add_variable('i2.1.1.2.2.2', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 28138
                                            if len(subjects700) == 0:
                                                pass
                                                # State 28139
                                                if len(subjects670) == 0:
                                                    pass
                                                    # State 28140
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 33: log(c*(d*(e + f*x)**p)**q)
                                        if len(subjects700) >= 1:
                                            tmp749 = []
                                            tmp749.append(subjects700.popleft())
                                            while True:
                                                if len(tmp749) > 1:
                                                    tmp750 = create_operation_expression(associative1, tmp749)
                                                elif len(tmp749) == 1:
                                                    tmp750 = tmp749[0]
                                                else:
                                                    assert False, "Unreachable"
                                                subst5 = Substitution(subst4)
                                                try:
                                                    subst5.try_add_variable('i2.1.1.2.2.2', tmp750)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 28138
                                                    if len(subjects700) == 0:
                                                        pass
                                                        # State 28139
                                                        if len(subjects670) == 0:
                                                            pass
                                                            # State 28140
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 33: log(c*(d*(e + f*x)**p)**q)
                                                if len(subjects700) == 0:
                                                    break
                                                tmp749.append(subjects700.popleft())
                                            subjects700.extendleft(reversed(tmp749))
                                subjects700.appendleft(tmp733)
                            subjects670.appendleft(tmp699)
                    if len(subjects670) >= 1:
                        tmp752 = subjects670.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.1', tmp752)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 40434
                            if len(subjects670) == 0:
                                pass
                                # State 40435
                                if len(subjects) == 0:
                                    pass
                                    # 34: log(c*x**n)
                        subjects670.appendleft(tmp752)
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.1.1.2.2.0', S(0))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 49644
                        subst4 = Substitution(subst3)
                        try:
                            subst4.try_add_variable('i2.1.1.2.2.1.0', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 49645
                            if len(subjects670) >= 1 and isinstance(subjects670[0], Pow):
                                tmp756 = subjects670.popleft()
                                subjects757 = deque(tmp756._args)
                                # State 49646
                                if len(subjects757) >= 1:
                                    tmp758 = subjects757.popleft()
                                    subst5 = Substitution(subst4)
                                    try:
                                        subst5.try_add_variable('i2.2.1.0', tmp758)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 49647
                                        if len(subjects757) >= 1:
                                            tmp760 = subjects757.popleft()
                                            subst6 = Substitution(subst5)
                                            try:
                                                subst6.try_add_variable('i2.1.1.2.2.1.2', tmp760)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 49648
                                                if len(subjects757) == 0:
                                                    pass
                                                    # State 49649
                                                    if len(subjects670) == 0:
                                                        pass
                                                        # State 49650
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 35: log(c*(d + e*x**n)**p)
                                            subjects757.appendleft(tmp760)
                                    subjects757.appendleft(tmp758)
                                if len(subjects757) >= 1:
                                    tmp762 = subjects757.popleft()
                                    subst5 = Substitution(subst4)
                                    try:
                                        subst5.try_add_variable('i2.3.1.0', tmp762)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 50103
                                        if len(subjects757) >= 1:
                                            tmp764 = subjects757.popleft()
                                            subst6 = Substitution(subst5)
                                            try:
                                                subst6.try_add_variable('i2.1.1.2.2.1.2', tmp764)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 50104
                                                if len(subjects757) == 0:
                                                    pass
                                                    # State 50105
                                                    if len(subjects670) == 0:
                                                        pass
                                                        # State 50106
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 37: log(c*(d + e*x**n)**p)
                                            subjects757.appendleft(tmp764)
                                    subjects757.appendleft(tmp762)
                                if len(subjects757) >= 1:
                                    tmp766 = subjects757.popleft()
                                    subst5 = Substitution(subst4)
                                    try:
                                        subst5.try_add_variable('i2.2.1.1', tmp766)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 50429
                                        if len(subjects757) >= 1 and subjects757[0] == 2:
                                            tmp768 = subjects757.popleft()
                                            # State 50430
                                            if len(subjects757) == 0:
                                                pass
                                                # State 50431
                                                if len(subjects670) == 0:
                                                    pass
                                                    # State 50432
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 38: log(c*(d + e*x**2)**p)
                                            subjects757.appendleft(tmp768)
                                    subjects757.appendleft(tmp766)
                                subjects670.appendleft(tmp756)
                        if len(subjects670) >= 1 and isinstance(subjects670[0], Mul):
                            tmp769 = subjects670.popleft()
                            associative1 = tmp769
                            associative_type1 = type(tmp769)
                            subjects770 = deque(tmp769._args)
                            matcher = CommutativeMatcher49652.get()
                            tmp771 = subjects770
                            subjects770 = []
                            for s in tmp771:
                                matcher.add_subject(s)
                            for pattern_index, subst4 in matcher.match(tmp771, subst3):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 49657
                                    if len(subjects670) == 0:
                                        pass
                                        # State 49658
                                        if len(subjects) == 0:
                                            pass
                                            # 35: log(c*(d + e*x**n)**p)
                                if pattern_index == 1:
                                    pass
                                    # State 50110
                                    if len(subjects670) == 0:
                                        pass
                                        # State 50111
                                        if len(subjects) == 0:
                                            pass
                                            # 37: log(c*(d + e*x**n)**p)
                                if pattern_index == 2:
                                    pass
                                    # State 50436
                                    if len(subjects670) == 0:
                                        pass
                                        # State 50437
                                        if len(subjects) == 0:
                                            pass
                                            # 38: log(c*(d + e*x**2)**p)
                            subjects670.appendleft(tmp769)
                    if len(subjects670) >= 1:
                        tmp772 = subjects670.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.1.1.2.1', tmp772)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 49803
                            if len(subjects670) == 0:
                                pass
                                # State 49804
                                if len(subjects) == 0:
                                    pass
                                    # 36: log(c*v**p)
                        subjects670.appendleft(tmp772)
                    if len(subjects670) >= 1 and isinstance(subjects670[0], Mul):
                        tmp774 = subjects670.popleft()
                        associative1 = tmp774
                        associative_type1 = type(tmp774)
                        subjects775 = deque(tmp774._args)
                        matcher = CommutativeMatcher25155.get()
                        tmp776 = subjects775
                        subjects775 = []
                        for s in tmp776:
                            matcher.add_subject(s)
                        for pattern_index, subst3 in matcher.match(tmp776, subst2):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 25192
                                if len(subjects670) == 0:
                                    pass
                                    # State 25193
                                    if len(subjects) == 0:
                                        pass
                                        # 28: log(c*(d*(e + f*x)**p)**q)
                            if pattern_index == 1:
                                pass
                                # State 27090
                                if len(subjects670) == 0:
                                    pass
                                    # State 27091
                                    if len(subjects) == 0:
                                        pass
                                        # 31: log(c*(d*(e + f*x)**p)**q)
                            if pattern_index == 2:
                                pass
                                # State 27412
                                if len(subjects670) == 0:
                                    pass
                                    # State 27413
                                    if len(subjects) == 0:
                                        pass
                                        # 32: log(c*(d*(e + f*x)**p)**q)
                            if pattern_index == 3:
                                pass
                                # State 28157
                                if len(subjects670) == 0:
                                    pass
                                    # State 28158
                                    if len(subjects) == 0:
                                        pass
                                        # 33: log(c*(d*(e + f*x)**p)**q)
                        subjects670.appendleft(tmp774)
                    if len(subjects670) >= 1 and isinstance(subjects670[0], Add):
                        tmp777 = subjects670.popleft()
                        associative1 = tmp777
                        associative_type1 = type(tmp777)
                        subjects778 = deque(tmp777._args)
                        matcher = CommutativeMatcher49660.get()
                        tmp779 = subjects778
                        subjects778 = []
                        for s in tmp779:
                            matcher.add_subject(s)
                        for pattern_index, subst3 in matcher.match(tmp779, subst2):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 49673
                                if len(subjects670) == 0:
                                    pass
                                    # State 49674
                                    if len(subjects) == 0:
                                        pass
                                        # 35: log(c*(d + e*x**n)**p)
                            if pattern_index == 1:
                                pass
                                # State 50119
                                if len(subjects670) == 0:
                                    pass
                                    # State 50120
                                    if len(subjects) == 0:
                                        pass
                                        # 37: log(c*(d + e*x**n)**p)
                            if pattern_index == 2:
                                pass
                                # State 50445
                                if len(subjects670) == 0:
                                    pass
                                    # State 50446
                                    if len(subjects) == 0:
                                        pass
                                        # 38: log(c*(d + e*x**2)**p)
                        subjects670.appendleft(tmp777)
                if len(subjects670) >= 1 and isinstance(subjects670[0], Add):
                    tmp780 = subjects670.popleft()
                    associative1 = tmp780
                    associative_type1 = type(tmp780)
                    subjects781 = deque(tmp780._args)
                    matcher = CommutativeMatcher24021.get()
                    tmp782 = subjects781
                    subjects781 = []
                    for s in tmp782:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp782, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 24027
                            if len(subjects670) == 0:
                                pass
                                # State 24028
                                if len(subjects) == 0:
                                    pass
                                    # 27: log(c*(e + f*x))
                    subjects670.appendleft(tmp780)
                if len(subjects670) >= 1 and isinstance(subjects670[0], Pow):
                    tmp783 = subjects670.popleft()
                    subjects784 = deque(tmp783._args)
                    # State 25194
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.1.1.2.2.0', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 25195
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.1.1.2.2.2', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 25196
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i2.1.1.2.2.2.0', S(0))
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 25197
                                subst5 = Substitution(subst4)
                                try:
                                    subst5.try_add_variable('i2.1.1.2.2.2.1.0', S(1))
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 25198
                                    if len(subjects784) >= 1:
                                        tmp789 = subjects784.popleft()
                                        subst6 = Substitution(subst5)
                                        try:
                                            subst6.try_add_variable('i2.2.1.0', tmp789)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 25199
                                            subst7 = Substitution(subst6)
                                            try:
                                                subst7.try_add_variable('i2.1.1.2.2', 1)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 25200
                                                if len(subjects784) == 0:
                                                    pass
                                                    # State 25201
                                                    if len(subjects670) == 0:
                                                        pass
                                                        # State 25202
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 28: log(c*(d*(e + f*x)**p)**q)
                                            if len(subjects784) >= 1:
                                                tmp792 = subjects784.popleft()
                                                subst7 = Substitution(subst6)
                                                try:
                                                    subst7.try_add_variable('i2.1.1.2.2', tmp792)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 25200
                                                    if len(subjects784) == 0:
                                                        pass
                                                        # State 25201
                                                        if len(subjects670) == 0:
                                                            pass
                                                            # State 25202
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 28: log(c*(d*(e + f*x)**p)**q)
                                                subjects784.appendleft(tmp792)
                                        subjects784.appendleft(tmp789)
                                    if len(subjects784) >= 1:
                                        tmp794 = subjects784.popleft()
                                        subst6 = Substitution(subst5)
                                        try:
                                            subst6.try_add_variable('i2.2.1.1', tmp794)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 27092
                                            subst7 = Substitution(subst6)
                                            try:
                                                subst7.try_add_variable('i2.1.1.2.2', 1)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 27093
                                                if len(subjects784) == 0:
                                                    pass
                                                    # State 27094
                                                    if len(subjects670) == 0:
                                                        pass
                                                        # State 27095
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 31: log(c*(d*(e + f*x)**p)**q)
                                            if len(subjects784) >= 1:
                                                tmp797 = subjects784.popleft()
                                                subst7 = Substitution(subst6)
                                                try:
                                                    subst7.try_add_variable('i2.1.1.2.2', tmp797)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 27093
                                                    if len(subjects784) == 0:
                                                        pass
                                                        # State 27094
                                                        if len(subjects670) == 0:
                                                            pass
                                                            # State 27095
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 31: log(c*(d*(e + f*x)**p)**q)
                                                subjects784.appendleft(tmp797)
                                        subjects784.appendleft(tmp794)
                                    if len(subjects784) >= 1:
                                        tmp799 = subjects784.popleft()
                                        subst6 = Substitution(subst5)
                                        try:
                                            subst6.try_add_variable('i2.3.1.0', tmp799)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 28159
                                            subst7 = Substitution(subst6)
                                            try:
                                                subst7.try_add_variable('i2.1.1.2.2', 1)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 28160
                                                if len(subjects784) == 0:
                                                    pass
                                                    # State 28161
                                                    if len(subjects670) == 0:
                                                        pass
                                                        # State 28162
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 33: log(c*(d*(e + f*x)**p)**q)
                                            if len(subjects784) >= 1:
                                                tmp802 = subjects784.popleft()
                                                subst7 = Substitution(subst6)
                                                try:
                                                    subst7.try_add_variable('i2.1.1.2.2', tmp802)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 28160
                                                    if len(subjects784) == 0:
                                                        pass
                                                        # State 28161
                                                        if len(subjects670) == 0:
                                                            pass
                                                            # State 28162
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 33: log(c*(d*(e + f*x)**p)**q)
                                                subjects784.appendleft(tmp802)
                                        subjects784.appendleft(tmp799)
                                if len(subjects784) >= 1 and isinstance(subjects784[0], Mul):
                                    tmp804 = subjects784.popleft()
                                    associative1 = tmp804
                                    associative_type1 = type(tmp804)
                                    subjects805 = deque(tmp804._args)
                                    matcher = CommutativeMatcher25204.get()
                                    tmp806 = subjects805
                                    subjects805 = []
                                    for s in tmp806:
                                        matcher.add_subject(s)
                                    for pattern_index, subst5 in matcher.match(tmp806, subst4):
                                        pass
                                        if pattern_index == 0:
                                            pass
                                            # State 25205
                                            subst6 = Substitution(subst5)
                                            try:
                                                subst6.try_add_variable('i2.1.1.2.2', 1)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 25206
                                                if len(subjects784) == 0:
                                                    pass
                                                    # State 25207
                                                    if len(subjects670) == 0:
                                                        pass
                                                        # State 25208
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 28: log(c*(d*(e + f*x)**p)**q)
                                            if len(subjects784) >= 1:
                                                tmp808 = []
                                                tmp808.append(subjects784.popleft())
                                                while True:
                                                    if len(tmp808) > 1:
                                                        tmp809 = create_operation_expression(associative1, tmp808)
                                                    elif len(tmp808) == 1:
                                                        tmp809 = tmp808[0]
                                                    else:
                                                        assert False, "Unreachable"
                                                    subst6 = Substitution(subst5)
                                                    try:
                                                        subst6.try_add_variable('i2.1.1.2.2', tmp809)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 25206
                                                        if len(subjects784) == 0:
                                                            pass
                                                            # State 25207
                                                            if len(subjects670) == 0:
                                                                pass
                                                                # State 25208
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 28: log(c*(d*(e + f*x)**p)**q)
                                                    if len(subjects784) == 0:
                                                        break
                                                    tmp808.append(subjects784.popleft())
                                                subjects784.extendleft(reversed(tmp808))
                                        if pattern_index == 1:
                                            pass
                                            # State 27096
                                            subst6 = Substitution(subst5)
                                            try:
                                                subst6.try_add_variable('i2.1.1.2.2', 1)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 27097
                                                if len(subjects784) == 0:
                                                    pass
                                                    # State 27098
                                                    if len(subjects670) == 0:
                                                        pass
                                                        # State 27099
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 31: log(c*(d*(e + f*x)**p)**q)
                                            if len(subjects784) >= 1:
                                                tmp812 = []
                                                tmp812.append(subjects784.popleft())
                                                while True:
                                                    if len(tmp812) > 1:
                                                        tmp813 = create_operation_expression(associative1, tmp812)
                                                    elif len(tmp812) == 1:
                                                        tmp813 = tmp812[0]
                                                    else:
                                                        assert False, "Unreachable"
                                                    subst6 = Substitution(subst5)
                                                    try:
                                                        subst6.try_add_variable('i2.1.1.2.2', tmp813)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 27097
                                                        if len(subjects784) == 0:
                                                            pass
                                                            # State 27098
                                                            if len(subjects670) == 0:
                                                                pass
                                                                # State 27099
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 31: log(c*(d*(e + f*x)**p)**q)
                                                    if len(subjects784) == 0:
                                                        break
                                                    tmp812.append(subjects784.popleft())
                                                subjects784.extendleft(reversed(tmp812))
                                        if pattern_index == 2:
                                            pass
                                            # State 28163
                                            subst6 = Substitution(subst5)
                                            try:
                                                subst6.try_add_variable('i2.1.1.2.2', 1)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 28164
                                                if len(subjects784) == 0:
                                                    pass
                                                    # State 28165
                                                    if len(subjects670) == 0:
                                                        pass
                                                        # State 28166
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 33: log(c*(d*(e + f*x)**p)**q)
                                            if len(subjects784) >= 1:
                                                tmp816 = []
                                                tmp816.append(subjects784.popleft())
                                                while True:
                                                    if len(tmp816) > 1:
                                                        tmp817 = create_operation_expression(associative1, tmp816)
                                                    elif len(tmp816) == 1:
                                                        tmp817 = tmp816[0]
                                                    else:
                                                        assert False, "Unreachable"
                                                    subst6 = Substitution(subst5)
                                                    try:
                                                        subst6.try_add_variable('i2.1.1.2.2', tmp817)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 28164
                                                        if len(subjects784) == 0:
                                                            pass
                                                            # State 28165
                                                            if len(subjects670) == 0:
                                                                pass
                                                                # State 28166
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 33: log(c*(d*(e + f*x)**p)**q)
                                                    if len(subjects784) == 0:
                                                        break
                                                    tmp816.append(subjects784.popleft())
                                                subjects784.extendleft(reversed(tmp816))
                                    subjects784.appendleft(tmp804)
                            if len(subjects784) >= 1 and isinstance(subjects784[0], Add):
                                tmp819 = subjects784.popleft()
                                associative1 = tmp819
                                associative_type1 = type(tmp819)
                                subjects820 = deque(tmp819._args)
                                matcher = CommutativeMatcher25210.get()
                                tmp821 = subjects820
                                subjects820 = []
                                for s in tmp821:
                                    matcher.add_subject(s)
                                for pattern_index, subst4 in matcher.match(tmp821, subst3):
                                    pass
                                    if pattern_index == 0:
                                        pass
                                        # State 25216
                                        subst5 = Substitution(subst4)
                                        try:
                                            subst5.try_add_variable('i2.1.1.2.2', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 25217
                                            if len(subjects784) == 0:
                                                pass
                                                # State 25218
                                                if len(subjects670) == 0:
                                                    pass
                                                    # State 25219
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 28: log(c*(d*(e + f*x)**p)**q)
                                        if len(subjects784) >= 1:
                                            tmp823 = []
                                            tmp823.append(subjects784.popleft())
                                            while True:
                                                if len(tmp823) > 1:
                                                    tmp824 = create_operation_expression(associative1, tmp823)
                                                elif len(tmp823) == 1:
                                                    tmp824 = tmp823[0]
                                                else:
                                                    assert False, "Unreachable"
                                                subst5 = Substitution(subst4)
                                                try:
                                                    subst5.try_add_variable('i2.1.1.2.2', tmp824)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 25217
                                                    if len(subjects784) == 0:
                                                        pass
                                                        # State 25218
                                                        if len(subjects670) == 0:
                                                            pass
                                                            # State 25219
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 28: log(c*(d*(e + f*x)**p)**q)
                                                if len(subjects784) == 0:
                                                    break
                                                tmp823.append(subjects784.popleft())
                                            subjects784.extendleft(reversed(tmp823))
                                    if pattern_index == 1:
                                        pass
                                        # State 27102
                                        subst5 = Substitution(subst4)
                                        try:
                                            subst5.try_add_variable('i2.1.1.2.2', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 27103
                                            if len(subjects784) == 0:
                                                pass
                                                # State 27104
                                                if len(subjects670) == 0:
                                                    pass
                                                    # State 27105
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 31: log(c*(d*(e + f*x)**p)**q)
                                        if len(subjects784) >= 1:
                                            tmp827 = []
                                            tmp827.append(subjects784.popleft())
                                            while True:
                                                if len(tmp827) > 1:
                                                    tmp828 = create_operation_expression(associative1, tmp827)
                                                elif len(tmp827) == 1:
                                                    tmp828 = tmp827[0]
                                                else:
                                                    assert False, "Unreachable"
                                                subst5 = Substitution(subst4)
                                                try:
                                                    subst5.try_add_variable('i2.1.1.2.2', tmp828)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 27103
                                                    if len(subjects784) == 0:
                                                        pass
                                                        # State 27104
                                                        if len(subjects670) == 0:
                                                            pass
                                                            # State 27105
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 31: log(c*(d*(e + f*x)**p)**q)
                                                if len(subjects784) == 0:
                                                    break
                                                tmp827.append(subjects784.popleft())
                                            subjects784.extendleft(reversed(tmp827))
                                    if pattern_index == 2:
                                        pass
                                        # State 27414
                                        subst5 = Substitution(subst4)
                                        try:
                                            subst5.try_add_variable('i2.1.1.2.2', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 27415
                                            if len(subjects784) == 0:
                                                pass
                                                # State 27416
                                                if len(subjects670) == 0:
                                                    pass
                                                    # State 27417
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 32: log(c*(d*(e + f*x)**p)**q)
                                        if len(subjects784) >= 1:
                                            tmp831 = []
                                            tmp831.append(subjects784.popleft())
                                            while True:
                                                if len(tmp831) > 1:
                                                    tmp832 = create_operation_expression(associative1, tmp831)
                                                elif len(tmp831) == 1:
                                                    tmp832 = tmp831[0]
                                                else:
                                                    assert False, "Unreachable"
                                                subst5 = Substitution(subst4)
                                                try:
                                                    subst5.try_add_variable('i2.1.1.2.2', tmp832)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 27415
                                                    if len(subjects784) == 0:
                                                        pass
                                                        # State 27416
                                                        if len(subjects670) == 0:
                                                            pass
                                                            # State 27417
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 32: log(c*(d*(e + f*x)**p)**q)
                                                if len(subjects784) == 0:
                                                    break
                                                tmp831.append(subjects784.popleft())
                                            subjects784.extendleft(reversed(tmp831))
                                    if pattern_index == 3:
                                        pass
                                        # State 28169
                                        subst5 = Substitution(subst4)
                                        try:
                                            subst5.try_add_variable('i2.1.1.2.2', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 28170
                                            if len(subjects784) == 0:
                                                pass
                                                # State 28171
                                                if len(subjects670) == 0:
                                                    pass
                                                    # State 28172
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 33: log(c*(d*(e + f*x)**p)**q)
                                        if len(subjects784) >= 1:
                                            tmp835 = []
                                            tmp835.append(subjects784.popleft())
                                            while True:
                                                if len(tmp835) > 1:
                                                    tmp836 = create_operation_expression(associative1, tmp835)
                                                elif len(tmp835) == 1:
                                                    tmp836 = tmp835[0]
                                                else:
                                                    assert False, "Unreachable"
                                                subst5 = Substitution(subst4)
                                                try:
                                                    subst5.try_add_variable('i2.1.1.2.2', tmp836)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 28170
                                                    if len(subjects784) == 0:
                                                        pass
                                                        # State 28171
                                                        if len(subjects670) == 0:
                                                            pass
                                                            # State 28172
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 33: log(c*(d*(e + f*x)**p)**q)
                                                if len(subjects784) == 0:
                                                    break
                                                tmp835.append(subjects784.popleft())
                                            subjects784.extendleft(reversed(tmp835))
                                subjects784.appendleft(tmp819)
                        if len(subjects784) >= 1 and isinstance(subjects784[0], Pow):
                            tmp838 = subjects784.popleft()
                            subjects839 = deque(tmp838._args)
                            # State 25220
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.1.1.2.2.2.0', S(0))
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 25221
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.1.1.2.2.2.1.0', S(1))
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 25222
                                    if len(subjects839) >= 1:
                                        tmp842 = subjects839.popleft()
                                        subst5 = Substitution(subst4)
                                        try:
                                            subst5.try_add_variable('i2.2.1.0', tmp842)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 25223
                                            subst6 = Substitution(subst5)
                                            try:
                                                subst6.try_add_variable('i2.1.1.2.2.2', 1)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 25224
                                                if len(subjects839) == 0:
                                                    pass
                                                    # State 25225
                                                    subst7 = Substitution(subst6)
                                                    try:
                                                        subst7.try_add_variable('i2.1.1.2.2', 1)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 25226
                                                        if len(subjects784) == 0:
                                                            pass
                                                            # State 25227
                                                            if len(subjects670) == 0:
                                                                pass
                                                                # State 25228
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 28: log(c*(d*(e + f*x)**p)**q)
                                                    if len(subjects784) >= 1:
                                                        tmp846 = subjects784.popleft()
                                                        subst7 = Substitution(subst6)
                                                        try:
                                                            subst7.try_add_variable('i2.1.1.2.2', tmp846)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            # State 25226
                                                            if len(subjects784) == 0:
                                                                pass
                                                                # State 25227
                                                                if len(subjects670) == 0:
                                                                    pass
                                                                    # State 25228
                                                                    if len(subjects) == 0:
                                                                        pass
                                                                        # 28: log(c*(d*(e + f*x)**p)**q)
                                                        subjects784.appendleft(tmp846)
                                            if len(subjects839) >= 1:
                                                tmp848 = subjects839.popleft()
                                                subst6 = Substitution(subst5)
                                                try:
                                                    subst6.try_add_variable('i2.1.1.2.2.2', tmp848)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 25224
                                                    if len(subjects839) == 0:
                                                        pass
                                                        # State 25225
                                                        subst7 = Substitution(subst6)
                                                        try:
                                                            subst7.try_add_variable('i2.1.1.2.2', 1)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            # State 25226
                                                            if len(subjects784) == 0:
                                                                pass
                                                                # State 25227
                                                                if len(subjects670) == 0:
                                                                    pass
                                                                    # State 25228
                                                                    if len(subjects) == 0:
                                                                        pass
                                                                        # 28: log(c*(d*(e + f*x)**p)**q)
                                                        if len(subjects784) >= 1:
                                                            tmp851 = subjects784.popleft()
                                                            subst7 = Substitution(subst6)
                                                            try:
                                                                subst7.try_add_variable('i2.1.1.2.2', tmp851)
                                                            except ValueError:
                                                                pass
                                                            else:
                                                                pass
                                                                # State 25226
                                                                if len(subjects784) == 0:
                                                                    pass
                                                                    # State 25227
                                                                    if len(subjects670) == 0:
                                                                        pass
                                                                        # State 25228
                                                                        if len(subjects) == 0:
                                                                            pass
                                                                            # 28: log(c*(d*(e + f*x)**p)**q)
                                                            subjects784.appendleft(tmp851)
                                                subjects839.appendleft(tmp848)
                                        subjects839.appendleft(tmp842)
                                    if len(subjects839) >= 1:
                                        tmp853 = subjects839.popleft()
                                        subst5 = Substitution(subst4)
                                        try:
                                            subst5.try_add_variable('i2.2.1.1', tmp853)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 27106
                                            subst6 = Substitution(subst5)
                                            try:
                                                subst6.try_add_variable('i2.1.1.2.2.2', 1)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 27107
                                                if len(subjects839) == 0:
                                                    pass
                                                    # State 27108
                                                    subst7 = Substitution(subst6)
                                                    try:
                                                        subst7.try_add_variable('i2.1.1.2.2', 1)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 27109
                                                        if len(subjects784) == 0:
                                                            pass
                                                            # State 27110
                                                            if len(subjects670) == 0:
                                                                pass
                                                                # State 27111
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 31: log(c*(d*(e + f*x)**p)**q)
                                                    if len(subjects784) >= 1:
                                                        tmp857 = subjects784.popleft()
                                                        subst7 = Substitution(subst6)
                                                        try:
                                                            subst7.try_add_variable('i2.1.1.2.2', tmp857)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            # State 27109
                                                            if len(subjects784) == 0:
                                                                pass
                                                                # State 27110
                                                                if len(subjects670) == 0:
                                                                    pass
                                                                    # State 27111
                                                                    if len(subjects) == 0:
                                                                        pass
                                                                        # 31: log(c*(d*(e + f*x)**p)**q)
                                                        subjects784.appendleft(tmp857)
                                            if len(subjects839) >= 1:
                                                tmp859 = subjects839.popleft()
                                                subst6 = Substitution(subst5)
                                                try:
                                                    subst6.try_add_variable('i2.1.1.2.2.2', tmp859)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 27107
                                                    if len(subjects839) == 0:
                                                        pass
                                                        # State 27108
                                                        subst7 = Substitution(subst6)
                                                        try:
                                                            subst7.try_add_variable('i2.1.1.2.2', 1)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            # State 27109
                                                            if len(subjects784) == 0:
                                                                pass
                                                                # State 27110
                                                                if len(subjects670) == 0:
                                                                    pass
                                                                    # State 27111
                                                                    if len(subjects) == 0:
                                                                        pass
                                                                        # 31: log(c*(d*(e + f*x)**p)**q)
                                                        if len(subjects784) >= 1:
                                                            tmp862 = subjects784.popleft()
                                                            subst7 = Substitution(subst6)
                                                            try:
                                                                subst7.try_add_variable('i2.1.1.2.2', tmp862)
                                                            except ValueError:
                                                                pass
                                                            else:
                                                                pass
                                                                # State 27109
                                                                if len(subjects784) == 0:
                                                                    pass
                                                                    # State 27110
                                                                    if len(subjects670) == 0:
                                                                        pass
                                                                        # State 27111
                                                                        if len(subjects) == 0:
                                                                            pass
                                                                            # 31: log(c*(d*(e + f*x)**p)**q)
                                                            subjects784.appendleft(tmp862)
                                                subjects839.appendleft(tmp859)
                                        subjects839.appendleft(tmp853)
                                    if len(subjects839) >= 1:
                                        tmp864 = subjects839.popleft()
                                        subst5 = Substitution(subst4)
                                        try:
                                            subst5.try_add_variable('i2.3.1.0', tmp864)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 28173
                                            subst6 = Substitution(subst5)
                                            try:
                                                subst6.try_add_variable('i2.1.1.2.2.2', 1)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 28174
                                                if len(subjects839) == 0:
                                                    pass
                                                    # State 28175
                                                    subst7 = Substitution(subst6)
                                                    try:
                                                        subst7.try_add_variable('i2.1.1.2.2', 1)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 28176
                                                        if len(subjects784) == 0:
                                                            pass
                                                            # State 28177
                                                            if len(subjects670) == 0:
                                                                pass
                                                                # State 28178
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 33: log(c*(d*(e + f*x)**p)**q)
                                                    if len(subjects784) >= 1:
                                                        tmp868 = subjects784.popleft()
                                                        subst7 = Substitution(subst6)
                                                        try:
                                                            subst7.try_add_variable('i2.1.1.2.2', tmp868)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            # State 28176
                                                            if len(subjects784) == 0:
                                                                pass
                                                                # State 28177
                                                                if len(subjects670) == 0:
                                                                    pass
                                                                    # State 28178
                                                                    if len(subjects) == 0:
                                                                        pass
                                                                        # 33: log(c*(d*(e + f*x)**p)**q)
                                                        subjects784.appendleft(tmp868)
                                            if len(subjects839) >= 1:
                                                tmp870 = subjects839.popleft()
                                                subst6 = Substitution(subst5)
                                                try:
                                                    subst6.try_add_variable('i2.1.1.2.2.2', tmp870)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 28174
                                                    if len(subjects839) == 0:
                                                        pass
                                                        # State 28175
                                                        subst7 = Substitution(subst6)
                                                        try:
                                                            subst7.try_add_variable('i2.1.1.2.2', 1)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            # State 28176
                                                            if len(subjects784) == 0:
                                                                pass
                                                                # State 28177
                                                                if len(subjects670) == 0:
                                                                    pass
                                                                    # State 28178
                                                                    if len(subjects) == 0:
                                                                        pass
                                                                        # 33: log(c*(d*(e + f*x)**p)**q)
                                                        if len(subjects784) >= 1:
                                                            tmp873 = subjects784.popleft()
                                                            subst7 = Substitution(subst6)
                                                            try:
                                                                subst7.try_add_variable('i2.1.1.2.2', tmp873)
                                                            except ValueError:
                                                                pass
                                                            else:
                                                                pass
                                                                # State 28176
                                                                if len(subjects784) == 0:
                                                                    pass
                                                                    # State 28177
                                                                    if len(subjects670) == 0:
                                                                        pass
                                                                        # State 28178
                                                                        if len(subjects) == 0:
                                                                            pass
                                                                            # 33: log(c*(d*(e + f*x)**p)**q)
                                                            subjects784.appendleft(tmp873)
                                                subjects839.appendleft(tmp870)
                                        subjects839.appendleft(tmp864)
                                if len(subjects839) >= 1 and isinstance(subjects839[0], Mul):
                                    tmp875 = subjects839.popleft()
                                    associative1 = tmp875
                                    associative_type1 = type(tmp875)
                                    subjects876 = deque(tmp875._args)
                                    matcher = CommutativeMatcher25230.get()
                                    tmp877 = subjects876
                                    subjects876 = []
                                    for s in tmp877:
                                        matcher.add_subject(s)
                                    for pattern_index, subst4 in matcher.match(tmp877, subst3):
                                        pass
                                        if pattern_index == 0:
                                            pass
                                            # State 25231
                                            subst5 = Substitution(subst4)
                                            try:
                                                subst5.try_add_variable('i2.1.1.2.2.2', 1)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 25232
                                                if len(subjects839) == 0:
                                                    pass
                                                    # State 25233
                                                    subst6 = Substitution(subst5)
                                                    try:
                                                        subst6.try_add_variable('i2.1.1.2.2', 1)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 25234
                                                        if len(subjects784) == 0:
                                                            pass
                                                            # State 25235
                                                            if len(subjects670) == 0:
                                                                pass
                                                                # State 25236
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 28: log(c*(d*(e + f*x)**p)**q)
                                                    if len(subjects784) >= 1:
                                                        tmp880 = subjects784.popleft()
                                                        subst6 = Substitution(subst5)
                                                        try:
                                                            subst6.try_add_variable('i2.1.1.2.2', tmp880)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            # State 25234
                                                            if len(subjects784) == 0:
                                                                pass
                                                                # State 25235
                                                                if len(subjects670) == 0:
                                                                    pass
                                                                    # State 25236
                                                                    if len(subjects) == 0:
                                                                        pass
                                                                        # 28: log(c*(d*(e + f*x)**p)**q)
                                                        subjects784.appendleft(tmp880)
                                            if len(subjects839) >= 1:
                                                tmp882 = []
                                                tmp882.append(subjects839.popleft())
                                                while True:
                                                    if len(tmp882) > 1:
                                                        tmp883 = create_operation_expression(associative1, tmp882)
                                                    elif len(tmp882) == 1:
                                                        tmp883 = tmp882[0]
                                                    else:
                                                        assert False, "Unreachable"
                                                    subst5 = Substitution(subst4)
                                                    try:
                                                        subst5.try_add_variable('i2.1.1.2.2.2', tmp883)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 25232
                                                        if len(subjects839) == 0:
                                                            pass
                                                            # State 25233
                                                            subst6 = Substitution(subst5)
                                                            try:
                                                                subst6.try_add_variable('i2.1.1.2.2', 1)
                                                            except ValueError:
                                                                pass
                                                            else:
                                                                pass
                                                                # State 25234
                                                                if len(subjects784) == 0:
                                                                    pass
                                                                    # State 25235
                                                                    if len(subjects670) == 0:
                                                                        pass
                                                                        # State 25236
                                                                        if len(subjects) == 0:
                                                                            pass
                                                                            # 28: log(c*(d*(e + f*x)**p)**q)
                                                            if len(subjects784) >= 1:
                                                                tmp886 = subjects784.popleft()
                                                                subst6 = Substitution(subst5)
                                                                try:
                                                                    subst6.try_add_variable('i2.1.1.2.2', tmp886)
                                                                except ValueError:
                                                                    pass
                                                                else:
                                                                    pass
                                                                    # State 25234
                                                                    if len(subjects784) == 0:
                                                                        pass
                                                                        # State 25235
                                                                        if len(subjects670) == 0:
                                                                            pass
                                                                            # State 25236
                                                                            if len(subjects) == 0:
                                                                                pass
                                                                                # 28: log(c*(d*(e + f*x)**p)**q)
                                                                subjects784.appendleft(tmp886)
                                                    if len(subjects839) == 0:
                                                        break
                                                    tmp882.append(subjects839.popleft())
                                                subjects839.extendleft(reversed(tmp882))
                                        if pattern_index == 1:
                                            pass
                                            # State 27112
                                            subst5 = Substitution(subst4)
                                            try:
                                                subst5.try_add_variable('i2.1.1.2.2.2', 1)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 27113
                                                if len(subjects839) == 0:
                                                    pass
                                                    # State 27114
                                                    subst6 = Substitution(subst5)
                                                    try:
                                                        subst6.try_add_variable('i2.1.1.2.2', 1)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 27115
                                                        if len(subjects784) == 0:
                                                            pass
                                                            # State 27116
                                                            if len(subjects670) == 0:
                                                                pass
                                                                # State 27117
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 31: log(c*(d*(e + f*x)**p)**q)
                                                    if len(subjects784) >= 1:
                                                        tmp890 = subjects784.popleft()
                                                        subst6 = Substitution(subst5)
                                                        try:
                                                            subst6.try_add_variable('i2.1.1.2.2', tmp890)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            # State 27115
                                                            if len(subjects784) == 0:
                                                                pass
                                                                # State 27116
                                                                if len(subjects670) == 0:
                                                                    pass
                                                                    # State 27117
                                                                    if len(subjects) == 0:
                                                                        pass
                                                                        # 31: log(c*(d*(e + f*x)**p)**q)
                                                        subjects784.appendleft(tmp890)
                                            if len(subjects839) >= 1:
                                                tmp892 = []
                                                tmp892.append(subjects839.popleft())
                                                while True:
                                                    if len(tmp892) > 1:
                                                        tmp893 = create_operation_expression(associative1, tmp892)
                                                    elif len(tmp892) == 1:
                                                        tmp893 = tmp892[0]
                                                    else:
                                                        assert False, "Unreachable"
                                                    subst5 = Substitution(subst4)
                                                    try:
                                                        subst5.try_add_variable('i2.1.1.2.2.2', tmp893)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 27113
                                                        if len(subjects839) == 0:
                                                            pass
                                                            # State 27114
                                                            subst6 = Substitution(subst5)
                                                            try:
                                                                subst6.try_add_variable('i2.1.1.2.2', 1)
                                                            except ValueError:
                                                                pass
                                                            else:
                                                                pass
                                                                # State 27115
                                                                if len(subjects784) == 0:
                                                                    pass
                                                                    # State 27116
                                                                    if len(subjects670) == 0:
                                                                        pass
                                                                        # State 27117
                                                                        if len(subjects) == 0:
                                                                            pass
                                                                            # 31: log(c*(d*(e + f*x)**p)**q)
                                                            if len(subjects784) >= 1:
                                                                tmp896 = subjects784.popleft()
                                                                subst6 = Substitution(subst5)
                                                                try:
                                                                    subst6.try_add_variable('i2.1.1.2.2', tmp896)
                                                                except ValueError:
                                                                    pass
                                                                else:
                                                                    pass
                                                                    # State 27115
                                                                    if len(subjects784) == 0:
                                                                        pass
                                                                        # State 27116
                                                                        if len(subjects670) == 0:
                                                                            pass
                                                                            # State 27117
                                                                            if len(subjects) == 0:
                                                                                pass
                                                                                # 31: log(c*(d*(e + f*x)**p)**q)
                                                                subjects784.appendleft(tmp896)
                                                    if len(subjects839) == 0:
                                                        break
                                                    tmp892.append(subjects839.popleft())
                                                subjects839.extendleft(reversed(tmp892))
                                        if pattern_index == 2:
                                            pass
                                            # State 28179
                                            subst5 = Substitution(subst4)
                                            try:
                                                subst5.try_add_variable('i2.1.1.2.2.2', 1)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 28180
                                                if len(subjects839) == 0:
                                                    pass
                                                    # State 28181
                                                    subst6 = Substitution(subst5)
                                                    try:
                                                        subst6.try_add_variable('i2.1.1.2.2', 1)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 28182
                                                        if len(subjects784) == 0:
                                                            pass
                                                            # State 28183
                                                            if len(subjects670) == 0:
                                                                pass
                                                                # State 28184
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 33: log(c*(d*(e + f*x)**p)**q)
                                                    if len(subjects784) >= 1:
                                                        tmp900 = subjects784.popleft()
                                                        subst6 = Substitution(subst5)
                                                        try:
                                                            subst6.try_add_variable('i2.1.1.2.2', tmp900)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            # State 28182
                                                            if len(subjects784) == 0:
                                                                pass
                                                                # State 28183
                                                                if len(subjects670) == 0:
                                                                    pass
                                                                    # State 28184
                                                                    if len(subjects) == 0:
                                                                        pass
                                                                        # 33: log(c*(d*(e + f*x)**p)**q)
                                                        subjects784.appendleft(tmp900)
                                            if len(subjects839) >= 1:
                                                tmp902 = []
                                                tmp902.append(subjects839.popleft())
                                                while True:
                                                    if len(tmp902) > 1:
                                                        tmp903 = create_operation_expression(associative1, tmp902)
                                                    elif len(tmp902) == 1:
                                                        tmp903 = tmp902[0]
                                                    else:
                                                        assert False, "Unreachable"
                                                    subst5 = Substitution(subst4)
                                                    try:
                                                        subst5.try_add_variable('i2.1.1.2.2.2', tmp903)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 28180
                                                        if len(subjects839) == 0:
                                                            pass
                                                            # State 28181
                                                            subst6 = Substitution(subst5)
                                                            try:
                                                                subst6.try_add_variable('i2.1.1.2.2', 1)
                                                            except ValueError:
                                                                pass
                                                            else:
                                                                pass
                                                                # State 28182
                                                                if len(subjects784) == 0:
                                                                    pass
                                                                    # State 28183
                                                                    if len(subjects670) == 0:
                                                                        pass
                                                                        # State 28184
                                                                        if len(subjects) == 0:
                                                                            pass
                                                                            # 33: log(c*(d*(e + f*x)**p)**q)
                                                            if len(subjects784) >= 1:
                                                                tmp906 = subjects784.popleft()
                                                                subst6 = Substitution(subst5)
                                                                try:
                                                                    subst6.try_add_variable('i2.1.1.2.2', tmp906)
                                                                except ValueError:
                                                                    pass
                                                                else:
                                                                    pass
                                                                    # State 28182
                                                                    if len(subjects784) == 0:
                                                                        pass
                                                                        # State 28183
                                                                        if len(subjects670) == 0:
                                                                            pass
                                                                            # State 28184
                                                                            if len(subjects) == 0:
                                                                                pass
                                                                                # 33: log(c*(d*(e + f*x)**p)**q)
                                                                subjects784.appendleft(tmp906)
                                                    if len(subjects839) == 0:
                                                        break
                                                    tmp902.append(subjects839.popleft())
                                                subjects839.extendleft(reversed(tmp902))
                                    subjects839.appendleft(tmp875)
                            if len(subjects839) >= 1 and isinstance(subjects839[0], Add):
                                tmp908 = subjects839.popleft()
                                associative1 = tmp908
                                associative_type1 = type(tmp908)
                                subjects909 = deque(tmp908._args)
                                matcher = CommutativeMatcher25238.get()
                                tmp910 = subjects909
                                subjects909 = []
                                for s in tmp910:
                                    matcher.add_subject(s)
                                for pattern_index, subst3 in matcher.match(tmp910, subst2):
                                    pass
                                    if pattern_index == 0:
                                        pass
                                        # State 25244
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.1.1.2.2.2', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 25245
                                            if len(subjects839) == 0:
                                                pass
                                                # State 25246
                                                subst5 = Substitution(subst4)
                                                try:
                                                    subst5.try_add_variable('i2.1.1.2.2', 1)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 25247
                                                    if len(subjects784) == 0:
                                                        pass
                                                        # State 25248
                                                        if len(subjects670) == 0:
                                                            pass
                                                            # State 25249
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 28: log(c*(d*(e + f*x)**p)**q)
                                                if len(subjects784) >= 1:
                                                    tmp913 = subjects784.popleft()
                                                    subst5 = Substitution(subst4)
                                                    try:
                                                        subst5.try_add_variable('i2.1.1.2.2', tmp913)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 25247
                                                        if len(subjects784) == 0:
                                                            pass
                                                            # State 25248
                                                            if len(subjects670) == 0:
                                                                pass
                                                                # State 25249
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 28: log(c*(d*(e + f*x)**p)**q)
                                                    subjects784.appendleft(tmp913)
                                        if len(subjects839) >= 1:
                                            tmp915 = []
                                            tmp915.append(subjects839.popleft())
                                            while True:
                                                if len(tmp915) > 1:
                                                    tmp916 = create_operation_expression(associative1, tmp915)
                                                elif len(tmp915) == 1:
                                                    tmp916 = tmp915[0]
                                                else:
                                                    assert False, "Unreachable"
                                                subst4 = Substitution(subst3)
                                                try:
                                                    subst4.try_add_variable('i2.1.1.2.2.2', tmp916)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 25245
                                                    if len(subjects839) == 0:
                                                        pass
                                                        # State 25246
                                                        subst5 = Substitution(subst4)
                                                        try:
                                                            subst5.try_add_variable('i2.1.1.2.2', 1)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            # State 25247
                                                            if len(subjects784) == 0:
                                                                pass
                                                                # State 25248
                                                                if len(subjects670) == 0:
                                                                    pass
                                                                    # State 25249
                                                                    if len(subjects) == 0:
                                                                        pass
                                                                        # 28: log(c*(d*(e + f*x)**p)**q)
                                                        if len(subjects784) >= 1:
                                                            tmp919 = subjects784.popleft()
                                                            subst5 = Substitution(subst4)
                                                            try:
                                                                subst5.try_add_variable('i2.1.1.2.2', tmp919)
                                                            except ValueError:
                                                                pass
                                                            else:
                                                                pass
                                                                # State 25247
                                                                if len(subjects784) == 0:
                                                                    pass
                                                                    # State 25248
                                                                    if len(subjects670) == 0:
                                                                        pass
                                                                        # State 25249
                                                                        if len(subjects) == 0:
                                                                            pass
                                                                            # 28: log(c*(d*(e + f*x)**p)**q)
                                                            subjects784.appendleft(tmp919)
                                                if len(subjects839) == 0:
                                                    break
                                                tmp915.append(subjects839.popleft())
                                            subjects839.extendleft(reversed(tmp915))
                                    if pattern_index == 1:
                                        pass
                                        # State 27120
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.1.1.2.2.2', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 27121
                                            if len(subjects839) == 0:
                                                pass
                                                # State 27122
                                                subst5 = Substitution(subst4)
                                                try:
                                                    subst5.try_add_variable('i2.1.1.2.2', 1)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 27123
                                                    if len(subjects784) == 0:
                                                        pass
                                                        # State 27124
                                                        if len(subjects670) == 0:
                                                            pass
                                                            # State 27125
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 31: log(c*(d*(e + f*x)**p)**q)
                                                if len(subjects784) >= 1:
                                                    tmp923 = subjects784.popleft()
                                                    subst5 = Substitution(subst4)
                                                    try:
                                                        subst5.try_add_variable('i2.1.1.2.2', tmp923)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 27123
                                                        if len(subjects784) == 0:
                                                            pass
                                                            # State 27124
                                                            if len(subjects670) == 0:
                                                                pass
                                                                # State 27125
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 31: log(c*(d*(e + f*x)**p)**q)
                                                    subjects784.appendleft(tmp923)
                                        if len(subjects839) >= 1:
                                            tmp925 = []
                                            tmp925.append(subjects839.popleft())
                                            while True:
                                                if len(tmp925) > 1:
                                                    tmp926 = create_operation_expression(associative1, tmp925)
                                                elif len(tmp925) == 1:
                                                    tmp926 = tmp925[0]
                                                else:
                                                    assert False, "Unreachable"
                                                subst4 = Substitution(subst3)
                                                try:
                                                    subst4.try_add_variable('i2.1.1.2.2.2', tmp926)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 27121
                                                    if len(subjects839) == 0:
                                                        pass
                                                        # State 27122
                                                        subst5 = Substitution(subst4)
                                                        try:
                                                            subst5.try_add_variable('i2.1.1.2.2', 1)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            # State 27123
                                                            if len(subjects784) == 0:
                                                                pass
                                                                # State 27124
                                                                if len(subjects670) == 0:
                                                                    pass
                                                                    # State 27125
                                                                    if len(subjects) == 0:
                                                                        pass
                                                                        # 31: log(c*(d*(e + f*x)**p)**q)
                                                        if len(subjects784) >= 1:
                                                            tmp929 = subjects784.popleft()
                                                            subst5 = Substitution(subst4)
                                                            try:
                                                                subst5.try_add_variable('i2.1.1.2.2', tmp929)
                                                            except ValueError:
                                                                pass
                                                            else:
                                                                pass
                                                                # State 27123
                                                                if len(subjects784) == 0:
                                                                    pass
                                                                    # State 27124
                                                                    if len(subjects670) == 0:
                                                                        pass
                                                                        # State 27125
                                                                        if len(subjects) == 0:
                                                                            pass
                                                                            # 31: log(c*(d*(e + f*x)**p)**q)
                                                            subjects784.appendleft(tmp929)
                                                if len(subjects839) == 0:
                                                    break
                                                tmp925.append(subjects839.popleft())
                                            subjects839.extendleft(reversed(tmp925))
                                    if pattern_index == 2:
                                        pass
                                        # State 27418
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.1.1.2.2.2', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 27419
                                            if len(subjects839) == 0:
                                                pass
                                                # State 27420
                                                subst5 = Substitution(subst4)
                                                try:
                                                    subst5.try_add_variable('i2.1.1.2.2', 1)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 27421
                                                    if len(subjects784) == 0:
                                                        pass
                                                        # State 27422
                                                        if len(subjects670) == 0:
                                                            pass
                                                            # State 27423
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 32: log(c*(d*(e + f*x)**p)**q)
                                                if len(subjects784) >= 1:
                                                    tmp933 = subjects784.popleft()
                                                    subst5 = Substitution(subst4)
                                                    try:
                                                        subst5.try_add_variable('i2.1.1.2.2', tmp933)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 27421
                                                        if len(subjects784) == 0:
                                                            pass
                                                            # State 27422
                                                            if len(subjects670) == 0:
                                                                pass
                                                                # State 27423
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 32: log(c*(d*(e + f*x)**p)**q)
                                                    subjects784.appendleft(tmp933)
                                        if len(subjects839) >= 1:
                                            tmp935 = []
                                            tmp935.append(subjects839.popleft())
                                            while True:
                                                if len(tmp935) > 1:
                                                    tmp936 = create_operation_expression(associative1, tmp935)
                                                elif len(tmp935) == 1:
                                                    tmp936 = tmp935[0]
                                                else:
                                                    assert False, "Unreachable"
                                                subst4 = Substitution(subst3)
                                                try:
                                                    subst4.try_add_variable('i2.1.1.2.2.2', tmp936)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 27419
                                                    if len(subjects839) == 0:
                                                        pass
                                                        # State 27420
                                                        subst5 = Substitution(subst4)
                                                        try:
                                                            subst5.try_add_variable('i2.1.1.2.2', 1)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            # State 27421
                                                            if len(subjects784) == 0:
                                                                pass
                                                                # State 27422
                                                                if len(subjects670) == 0:
                                                                    pass
                                                                    # State 27423
                                                                    if len(subjects) == 0:
                                                                        pass
                                                                        # 32: log(c*(d*(e + f*x)**p)**q)
                                                        if len(subjects784) >= 1:
                                                            tmp939 = subjects784.popleft()
                                                            subst5 = Substitution(subst4)
                                                            try:
                                                                subst5.try_add_variable('i2.1.1.2.2', tmp939)
                                                            except ValueError:
                                                                pass
                                                            else:
                                                                pass
                                                                # State 27421
                                                                if len(subjects784) == 0:
                                                                    pass
                                                                    # State 27422
                                                                    if len(subjects670) == 0:
                                                                        pass
                                                                        # State 27423
                                                                        if len(subjects) == 0:
                                                                            pass
                                                                            # 32: log(c*(d*(e + f*x)**p)**q)
                                                            subjects784.appendleft(tmp939)
                                                if len(subjects839) == 0:
                                                    break
                                                tmp935.append(subjects839.popleft())
                                            subjects839.extendleft(reversed(tmp935))
                                    if pattern_index == 3:
                                        pass
                                        # State 28187
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.1.1.2.2.2', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 28188
                                            if len(subjects839) == 0:
                                                pass
                                                # State 28189
                                                subst5 = Substitution(subst4)
                                                try:
                                                    subst5.try_add_variable('i2.1.1.2.2', 1)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 28190
                                                    if len(subjects784) == 0:
                                                        pass
                                                        # State 28191
                                                        if len(subjects670) == 0:
                                                            pass
                                                            # State 28192
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 33: log(c*(d*(e + f*x)**p)**q)
                                                if len(subjects784) >= 1:
                                                    tmp943 = subjects784.popleft()
                                                    subst5 = Substitution(subst4)
                                                    try:
                                                        subst5.try_add_variable('i2.1.1.2.2', tmp943)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 28190
                                                        if len(subjects784) == 0:
                                                            pass
                                                            # State 28191
                                                            if len(subjects670) == 0:
                                                                pass
                                                                # State 28192
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 33: log(c*(d*(e + f*x)**p)**q)
                                                    subjects784.appendleft(tmp943)
                                        if len(subjects839) >= 1:
                                            tmp945 = []
                                            tmp945.append(subjects839.popleft())
                                            while True:
                                                if len(tmp945) > 1:
                                                    tmp946 = create_operation_expression(associative1, tmp945)
                                                elif len(tmp945) == 1:
                                                    tmp946 = tmp945[0]
                                                else:
                                                    assert False, "Unreachable"
                                                subst4 = Substitution(subst3)
                                                try:
                                                    subst4.try_add_variable('i2.1.1.2.2.2', tmp946)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 28188
                                                    if len(subjects839) == 0:
                                                        pass
                                                        # State 28189
                                                        subst5 = Substitution(subst4)
                                                        try:
                                                            subst5.try_add_variable('i2.1.1.2.2', 1)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            # State 28190
                                                            if len(subjects784) == 0:
                                                                pass
                                                                # State 28191
                                                                if len(subjects670) == 0:
                                                                    pass
                                                                    # State 28192
                                                                    if len(subjects) == 0:
                                                                        pass
                                                                        # 33: log(c*(d*(e + f*x)**p)**q)
                                                        if len(subjects784) >= 1:
                                                            tmp949 = subjects784.popleft()
                                                            subst5 = Substitution(subst4)
                                                            try:
                                                                subst5.try_add_variable('i2.1.1.2.2', tmp949)
                                                            except ValueError:
                                                                pass
                                                            else:
                                                                pass
                                                                # State 28190
                                                                if len(subjects784) == 0:
                                                                    pass
                                                                    # State 28191
                                                                    if len(subjects670) == 0:
                                                                        pass
                                                                        # State 28192
                                                                        if len(subjects) == 0:
                                                                            pass
                                                                            # 33: log(c*(d*(e + f*x)**p)**q)
                                                            subjects784.appendleft(tmp949)
                                                if len(subjects839) == 0:
                                                    break
                                                tmp945.append(subjects839.popleft())
                                            subjects839.extendleft(reversed(tmp945))
                                subjects839.appendleft(tmp908)
                            subjects784.appendleft(tmp838)
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.1.1.2.2.0', S(0))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 25946
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.1.1.2.2.1.0', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 25947
                            if len(subjects784) >= 1:
                                tmp953 = subjects784.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.2.1.0', tmp953)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 25948
                                    if len(subjects784) >= 1 and subjects784[0] == -1:
                                        tmp955 = subjects784.popleft()
                                        # State 25949
                                        if len(subjects784) == 0:
                                            pass
                                            # State 25950
                                            if len(subjects670) == 0:
                                                pass
                                                # State 25951
                                                if len(subjects) == 0:
                                                    pass
                                                    # 29: log(c/(e + f*x))
                                        subjects784.appendleft(tmp955)
                                subjects784.appendleft(tmp953)
                            if len(subjects784) >= 1:
                                tmp956 = subjects784.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.2.1.1', tmp956)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 26491
                                    if len(subjects784) >= 1 and subjects784[0] == -1:
                                        tmp958 = subjects784.popleft()
                                        # State 26492
                                        if len(subjects784) == 0:
                                            pass
                                            # State 26493
                                            if len(subjects670) == 0:
                                                pass
                                                # State 26494
                                                if len(subjects) == 0:
                                                    pass
                                                    # 30: log(c/(e + f*x))
                                        subjects784.appendleft(tmp958)
                                subjects784.appendleft(tmp956)
                            if len(subjects784) >= 1 and isinstance(subjects784[0], Pow):
                                tmp959 = subjects784.popleft()
                                subjects960 = deque(tmp959._args)
                                # State 49675
                                if len(subjects960) >= 1:
                                    tmp961 = subjects960.popleft()
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i2.2.1.0', tmp961)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 49676
                                        if len(subjects960) >= 1:
                                            tmp963 = subjects960.popleft()
                                            subst5 = Substitution(subst4)
                                            try:
                                                subst5.try_add_variable('i2.1.1.2.2.1.2', tmp963)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 49677
                                                if len(subjects960) == 0:
                                                    pass
                                                    # State 49678
                                                    subst6 = Substitution(subst5)
                                                    try:
                                                        subst6.try_add_variable('i2.1.1.2.2', 1)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 49679
                                                        if len(subjects784) == 0:
                                                            pass
                                                            # State 49680
                                                            if len(subjects670) == 0:
                                                                pass
                                                                # State 49681
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 35: log(c*(d + e*x**n)**p)
                                                    if len(subjects784) >= 1:
                                                        tmp966 = subjects784.popleft()
                                                        subst6 = Substitution(subst5)
                                                        try:
                                                            subst6.try_add_variable('i2.1.1.2.2', tmp966)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            # State 49679
                                                            if len(subjects784) == 0:
                                                                pass
                                                                # State 49680
                                                                if len(subjects670) == 0:
                                                                    pass
                                                                    # State 49681
                                                                    if len(subjects) == 0:
                                                                        pass
                                                                        # 35: log(c*(d + e*x**n)**p)
                                                        subjects784.appendleft(tmp966)
                                            subjects960.appendleft(tmp963)
                                    subjects960.appendleft(tmp961)
                                if len(subjects960) >= 1:
                                    tmp968 = subjects960.popleft()
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i2.3.1.0', tmp968)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 50121
                                        if len(subjects960) >= 1:
                                            tmp970 = subjects960.popleft()
                                            subst5 = Substitution(subst4)
                                            try:
                                                subst5.try_add_variable('i2.1.1.2.2.1.2', tmp970)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 50122
                                                if len(subjects960) == 0:
                                                    pass
                                                    # State 50123
                                                    subst6 = Substitution(subst5)
                                                    try:
                                                        subst6.try_add_variable('i2.1.1.2.2', 1)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 50124
                                                        if len(subjects784) == 0:
                                                            pass
                                                            # State 50125
                                                            if len(subjects670) == 0:
                                                                pass
                                                                # State 50126
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 37: log(c*(d + e*x**n)**p)
                                                    if len(subjects784) >= 1:
                                                        tmp973 = subjects784.popleft()
                                                        subst6 = Substitution(subst5)
                                                        try:
                                                            subst6.try_add_variable('i2.1.1.2.2', tmp973)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            # State 50124
                                                            if len(subjects784) == 0:
                                                                pass
                                                                # State 50125
                                                                if len(subjects670) == 0:
                                                                    pass
                                                                    # State 50126
                                                                    if len(subjects) == 0:
                                                                        pass
                                                                        # 37: log(c*(d + e*x**n)**p)
                                                        subjects784.appendleft(tmp973)
                                            subjects960.appendleft(tmp970)
                                    subjects960.appendleft(tmp968)
                                if len(subjects960) >= 1:
                                    tmp975 = subjects960.popleft()
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i2.2.1.1', tmp975)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 50447
                                        if len(subjects960) >= 1 and subjects960[0] == 2:
                                            tmp977 = subjects960.popleft()
                                            # State 50448
                                            if len(subjects960) == 0:
                                                pass
                                                # State 50449
                                                subst5 = Substitution(subst4)
                                                try:
                                                    subst5.try_add_variable('i2.1.1.2.2', 1)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 50450
                                                    if len(subjects784) == 0:
                                                        pass
                                                        # State 50451
                                                        if len(subjects670) == 0:
                                                            pass
                                                            # State 50452
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 38: log(c*(d + e*x**2)**p)
                                                if len(subjects784) >= 1:
                                                    tmp979 = subjects784.popleft()
                                                    subst5 = Substitution(subst4)
                                                    try:
                                                        subst5.try_add_variable('i2.1.1.2.2', tmp979)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 50450
                                                        if len(subjects784) == 0:
                                                            pass
                                                            # State 50451
                                                            if len(subjects670) == 0:
                                                                pass
                                                                # State 50452
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 38: log(c*(d + e*x**2)**p)
                                                    subjects784.appendleft(tmp979)
                                            subjects960.appendleft(tmp977)
                                    subjects960.appendleft(tmp975)
                                subjects784.appendleft(tmp959)
                        if len(subjects784) >= 1 and isinstance(subjects784[0], Mul):
                            tmp981 = subjects784.popleft()
                            associative1 = tmp981
                            associative_type1 = type(tmp981)
                            subjects982 = deque(tmp981._args)
                            matcher = CommutativeMatcher25953.get()
                            tmp983 = subjects982
                            subjects982 = []
                            for s in tmp983:
                                matcher.add_subject(s)
                            for pattern_index, subst3 in matcher.match(tmp983, subst2):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 25954
                                    if len(subjects784) >= 1 and subjects784[0] == -1:
                                        tmp984 = subjects784.popleft()
                                        # State 25955
                                        if len(subjects784) == 0:
                                            pass
                                            # State 25956
                                            if len(subjects670) == 0:
                                                pass
                                                # State 25957
                                                if len(subjects) == 0:
                                                    pass
                                                    # 29: log(c/(e + f*x))
                                        subjects784.appendleft(tmp984)
                                if pattern_index == 1:
                                    pass
                                    # State 26495
                                    if len(subjects784) >= 1 and subjects784[0] == -1:
                                        tmp985 = subjects784.popleft()
                                        # State 26496
                                        if len(subjects784) == 0:
                                            pass
                                            # State 26497
                                            if len(subjects670) == 0:
                                                pass
                                                # State 26498
                                                if len(subjects) == 0:
                                                    pass
                                                    # 30: log(c/(e + f*x))
                                        subjects784.appendleft(tmp985)
                                if pattern_index == 2:
                                    pass
                                    # State 49686
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i2.1.1.2.2', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 49687
                                        if len(subjects784) == 0:
                                            pass
                                            # State 49688
                                            if len(subjects670) == 0:
                                                pass
                                                # State 49689
                                                if len(subjects) == 0:
                                                    pass
                                                    # 35: log(c*(d + e*x**n)**p)
                                    if len(subjects784) >= 1:
                                        tmp987 = []
                                        tmp987.append(subjects784.popleft())
                                        while True:
                                            if len(tmp987) > 1:
                                                tmp988 = create_operation_expression(associative1, tmp987)
                                            elif len(tmp987) == 1:
                                                tmp988 = tmp987[0]
                                            else:
                                                assert False, "Unreachable"
                                            subst4 = Substitution(subst3)
                                            try:
                                                subst4.try_add_variable('i2.1.1.2.2', tmp988)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 49687
                                                if len(subjects784) == 0:
                                                    pass
                                                    # State 49688
                                                    if len(subjects670) == 0:
                                                        pass
                                                        # State 49689
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 35: log(c*(d + e*x**n)**p)
                                            if len(subjects784) == 0:
                                                break
                                            tmp987.append(subjects784.popleft())
                                        subjects784.extendleft(reversed(tmp987))
                                if pattern_index == 3:
                                    pass
                                    # State 50130
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i2.1.1.2.2', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 50131
                                        if len(subjects784) == 0:
                                            pass
                                            # State 50132
                                            if len(subjects670) == 0:
                                                pass
                                                # State 50133
                                                if len(subjects) == 0:
                                                    pass
                                                    # 37: log(c*(d + e*x**n)**p)
                                    if len(subjects784) >= 1:
                                        tmp991 = []
                                        tmp991.append(subjects784.popleft())
                                        while True:
                                            if len(tmp991) > 1:
                                                tmp992 = create_operation_expression(associative1, tmp991)
                                            elif len(tmp991) == 1:
                                                tmp992 = tmp991[0]
                                            else:
                                                assert False, "Unreachable"
                                            subst4 = Substitution(subst3)
                                            try:
                                                subst4.try_add_variable('i2.1.1.2.2', tmp992)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 50131
                                                if len(subjects784) == 0:
                                                    pass
                                                    # State 50132
                                                    if len(subjects670) == 0:
                                                        pass
                                                        # State 50133
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 37: log(c*(d + e*x**n)**p)
                                            if len(subjects784) == 0:
                                                break
                                            tmp991.append(subjects784.popleft())
                                        subjects784.extendleft(reversed(tmp991))
                                if pattern_index == 4:
                                    pass
                                    # State 50456
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i2.1.1.2.2', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 50457
                                        if len(subjects784) == 0:
                                            pass
                                            # State 50458
                                            if len(subjects670) == 0:
                                                pass
                                                # State 50459
                                                if len(subjects) == 0:
                                                    pass
                                                    # 38: log(c*(d + e*x**2)**p)
                                    if len(subjects784) >= 1:
                                        tmp995 = []
                                        tmp995.append(subjects784.popleft())
                                        while True:
                                            if len(tmp995) > 1:
                                                tmp996 = create_operation_expression(associative1, tmp995)
                                            elif len(tmp995) == 1:
                                                tmp996 = tmp995[0]
                                            else:
                                                assert False, "Unreachable"
                                            subst4 = Substitution(subst3)
                                            try:
                                                subst4.try_add_variable('i2.1.1.2.2', tmp996)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 50457
                                                if len(subjects784) == 0:
                                                    pass
                                                    # State 50458
                                                    if len(subjects670) == 0:
                                                        pass
                                                        # State 50459
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 38: log(c*(d + e*x**2)**p)
                                            if len(subjects784) == 0:
                                                break
                                            tmp995.append(subjects784.popleft())
                                        subjects784.extendleft(reversed(tmp995))
                            subjects784.appendleft(tmp981)
                    if len(subjects784) >= 1:
                        tmp998 = subjects784.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.1.1', tmp998)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 40436
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.1.1.2.2', 1)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 40437
                                if len(subjects784) == 0:
                                    pass
                                    # State 40438
                                    if len(subjects670) == 0:
                                        pass
                                        # State 40439
                                        if len(subjects) == 0:
                                            pass
                                            # 34: log(c*x**n)
                            if len(subjects784) >= 1:
                                tmp1001 = subjects784.popleft()
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i2.1.1.2.2', tmp1001)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 40437
                                    if len(subjects784) == 0:
                                        pass
                                        # State 40438
                                        if len(subjects670) == 0:
                                            pass
                                            # State 40439
                                            if len(subjects) == 0:
                                                pass
                                                # 34: log(c*x**n)
                                subjects784.appendleft(tmp1001)
                        subjects784.appendleft(tmp998)
                    if len(subjects784) >= 1:
                        tmp1003 = subjects784.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.1.1.2.1', tmp1003)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 49805
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.1.1.2.2', 1)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 49806
                                if len(subjects784) == 0:
                                    pass
                                    # State 49807
                                    if len(subjects670) == 0:
                                        pass
                                        # State 49808
                                        if len(subjects) == 0:
                                            pass
                                            # 36: log(c*v**p)
                            if len(subjects784) >= 1:
                                tmp1006 = subjects784.popleft()
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i2.1.1.2.2', tmp1006)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 49806
                                    if len(subjects784) == 0:
                                        pass
                                        # State 49807
                                        if len(subjects670) == 0:
                                            pass
                                            # State 49808
                                            if len(subjects) == 0:
                                                pass
                                                # 36: log(c*v**p)
                                subjects784.appendleft(tmp1006)
                        subjects784.appendleft(tmp1003)
                    if len(subjects784) >= 1 and isinstance(subjects784[0], Mul):
                        tmp1008 = subjects784.popleft()
                        associative1 = tmp1008
                        associative_type1 = type(tmp1008)
                        subjects1009 = deque(tmp1008._args)
                        matcher = CommutativeMatcher25251.get()
                        tmp1010 = subjects1009
                        subjects1009 = []
                        for s in tmp1010:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp1010, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 25288
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i2.1.1.2.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 25289
                                    if len(subjects784) == 0:
                                        pass
                                        # State 25290
                                        if len(subjects670) == 0:
                                            pass
                                            # State 25291
                                            if len(subjects) == 0:
                                                pass
                                                # 28: log(c*(d*(e + f*x)**p)**q)
                                if len(subjects784) >= 1:
                                    tmp1012 = []
                                    tmp1012.append(subjects784.popleft())
                                    while True:
                                        if len(tmp1012) > 1:
                                            tmp1013 = create_operation_expression(associative1, tmp1012)
                                        elif len(tmp1012) == 1:
                                            tmp1013 = tmp1012[0]
                                        else:
                                            assert False, "Unreachable"
                                        subst3 = Substitution(subst2)
                                        try:
                                            subst3.try_add_variable('i2.1.1.2.2', tmp1013)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 25289
                                            if len(subjects784) == 0:
                                                pass
                                                # State 25290
                                                if len(subjects670) == 0:
                                                    pass
                                                    # State 25291
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 28: log(c*(d*(e + f*x)**p)**q)
                                        if len(subjects784) == 0:
                                            break
                                        tmp1012.append(subjects784.popleft())
                                    subjects784.extendleft(reversed(tmp1012))
                            if pattern_index == 1:
                                pass
                                # State 27142
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i2.1.1.2.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 27143
                                    if len(subjects784) == 0:
                                        pass
                                        # State 27144
                                        if len(subjects670) == 0:
                                            pass
                                            # State 27145
                                            if len(subjects) == 0:
                                                pass
                                                # 31: log(c*(d*(e + f*x)**p)**q)
                                if len(subjects784) >= 1:
                                    tmp1016 = []
                                    tmp1016.append(subjects784.popleft())
                                    while True:
                                        if len(tmp1016) > 1:
                                            tmp1017 = create_operation_expression(associative1, tmp1016)
                                        elif len(tmp1016) == 1:
                                            tmp1017 = tmp1016[0]
                                        else:
                                            assert False, "Unreachable"
                                        subst3 = Substitution(subst2)
                                        try:
                                            subst3.try_add_variable('i2.1.1.2.2', tmp1017)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 27143
                                            if len(subjects784) == 0:
                                                pass
                                                # State 27144
                                                if len(subjects670) == 0:
                                                    pass
                                                    # State 27145
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 31: log(c*(d*(e + f*x)**p)**q)
                                        if len(subjects784) == 0:
                                            break
                                        tmp1016.append(subjects784.popleft())
                                    subjects784.extendleft(reversed(tmp1016))
                            if pattern_index == 2:
                                pass
                                # State 27428
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i2.1.1.2.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 27429
                                    if len(subjects784) == 0:
                                        pass
                                        # State 27430
                                        if len(subjects670) == 0:
                                            pass
                                            # State 27431
                                            if len(subjects) == 0:
                                                pass
                                                # 32: log(c*(d*(e + f*x)**p)**q)
                                if len(subjects784) >= 1:
                                    tmp1020 = []
                                    tmp1020.append(subjects784.popleft())
                                    while True:
                                        if len(tmp1020) > 1:
                                            tmp1021 = create_operation_expression(associative1, tmp1020)
                                        elif len(tmp1020) == 1:
                                            tmp1021 = tmp1020[0]
                                        else:
                                            assert False, "Unreachable"
                                        subst3 = Substitution(subst2)
                                        try:
                                            subst3.try_add_variable('i2.1.1.2.2', tmp1021)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 27429
                                            if len(subjects784) == 0:
                                                pass
                                                # State 27430
                                                if len(subjects670) == 0:
                                                    pass
                                                    # State 27431
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 32: log(c*(d*(e + f*x)**p)**q)
                                        if len(subjects784) == 0:
                                            break
                                        tmp1020.append(subjects784.popleft())
                                    subjects784.extendleft(reversed(tmp1020))
                            if pattern_index == 3:
                                pass
                                # State 28209
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i2.1.1.2.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 28210
                                    if len(subjects784) == 0:
                                        pass
                                        # State 28211
                                        if len(subjects670) == 0:
                                            pass
                                            # State 28212
                                            if len(subjects) == 0:
                                                pass
                                                # 33: log(c*(d*(e + f*x)**p)**q)
                                if len(subjects784) >= 1:
                                    tmp1024 = []
                                    tmp1024.append(subjects784.popleft())
                                    while True:
                                        if len(tmp1024) > 1:
                                            tmp1025 = create_operation_expression(associative1, tmp1024)
                                        elif len(tmp1024) == 1:
                                            tmp1025 = tmp1024[0]
                                        else:
                                            assert False, "Unreachable"
                                        subst3 = Substitution(subst2)
                                        try:
                                            subst3.try_add_variable('i2.1.1.2.2', tmp1025)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 28210
                                            if len(subjects784) == 0:
                                                pass
                                                # State 28211
                                                if len(subjects670) == 0:
                                                    pass
                                                    # State 28212
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 33: log(c*(d*(e + f*x)**p)**q)
                                        if len(subjects784) == 0:
                                            break
                                        tmp1024.append(subjects784.popleft())
                                    subjects784.extendleft(reversed(tmp1024))
                        subjects784.appendleft(tmp1008)
                    if len(subjects784) >= 1 and isinstance(subjects784[0], Add):
                        tmp1027 = subjects784.popleft()
                        associative1 = tmp1027
                        associative_type1 = type(tmp1027)
                        subjects1028 = deque(tmp1027._args)
                        matcher = CommutativeMatcher25959.get()
                        tmp1029 = subjects1028
                        subjects1028 = []
                        for s in tmp1029:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp1029, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 25965
                                if len(subjects784) >= 1 and subjects784[0] == -1:
                                    tmp1030 = subjects784.popleft()
                                    # State 25966
                                    if len(subjects784) == 0:
                                        pass
                                        # State 25967
                                        if len(subjects670) == 0:
                                            pass
                                            # State 25968
                                            if len(subjects) == 0:
                                                pass
                                                # 29: log(c/(e + f*x))
                                    subjects784.appendleft(tmp1030)
                            if pattern_index == 1:
                                pass
                                # State 26501
                                if len(subjects784) >= 1 and subjects784[0] == -1:
                                    tmp1031 = subjects784.popleft()
                                    # State 26502
                                    if len(subjects784) == 0:
                                        pass
                                        # State 26503
                                        if len(subjects670) == 0:
                                            pass
                                            # State 26504
                                            if len(subjects) == 0:
                                                pass
                                                # 30: log(c/(e + f*x))
                                    subjects784.appendleft(tmp1031)
                            if pattern_index == 2:
                                pass
                                # State 49699
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i2.1.1.2.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 49700
                                    if len(subjects784) == 0:
                                        pass
                                        # State 49701
                                        if len(subjects670) == 0:
                                            pass
                                            # State 49702
                                            if len(subjects) == 0:
                                                pass
                                                # 35: log(c*(d + e*x**n)**p)
                                if len(subjects784) >= 1:
                                    tmp1033 = []
                                    tmp1033.append(subjects784.popleft())
                                    while True:
                                        if len(tmp1033) > 1:
                                            tmp1034 = create_operation_expression(associative1, tmp1033)
                                        elif len(tmp1033) == 1:
                                            tmp1034 = tmp1033[0]
                                        else:
                                            assert False, "Unreachable"
                                        subst3 = Substitution(subst2)
                                        try:
                                            subst3.try_add_variable('i2.1.1.2.2', tmp1034)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 49700
                                            if len(subjects784) == 0:
                                                pass
                                                # State 49701
                                                if len(subjects670) == 0:
                                                    pass
                                                    # State 49702
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 35: log(c*(d + e*x**n)**p)
                                        if len(subjects784) == 0:
                                            break
                                        tmp1033.append(subjects784.popleft())
                                    subjects784.extendleft(reversed(tmp1033))
                            if pattern_index == 3:
                                pass
                                # State 50141
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i2.1.1.2.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 50142
                                    if len(subjects784) == 0:
                                        pass
                                        # State 50143
                                        if len(subjects670) == 0:
                                            pass
                                            # State 50144
                                            if len(subjects) == 0:
                                                pass
                                                # 37: log(c*(d + e*x**n)**p)
                                if len(subjects784) >= 1:
                                    tmp1037 = []
                                    tmp1037.append(subjects784.popleft())
                                    while True:
                                        if len(tmp1037) > 1:
                                            tmp1038 = create_operation_expression(associative1, tmp1037)
                                        elif len(tmp1037) == 1:
                                            tmp1038 = tmp1037[0]
                                        else:
                                            assert False, "Unreachable"
                                        subst3 = Substitution(subst2)
                                        try:
                                            subst3.try_add_variable('i2.1.1.2.2', tmp1038)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 50142
                                            if len(subjects784) == 0:
                                                pass
                                                # State 50143
                                                if len(subjects670) == 0:
                                                    pass
                                                    # State 50144
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 37: log(c*(d + e*x**n)**p)
                                        if len(subjects784) == 0:
                                            break
                                        tmp1037.append(subjects784.popleft())
                                    subjects784.extendleft(reversed(tmp1037))
                            if pattern_index == 4:
                                pass
                                # State 50467
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i2.1.1.2.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 50468
                                    if len(subjects784) == 0:
                                        pass
                                        # State 50469
                                        if len(subjects670) == 0:
                                            pass
                                            # State 50470
                                            if len(subjects) == 0:
                                                pass
                                                # 38: log(c*(d + e*x**2)**p)
                                if len(subjects784) >= 1:
                                    tmp1041 = []
                                    tmp1041.append(subjects784.popleft())
                                    while True:
                                        if len(tmp1041) > 1:
                                            tmp1042 = create_operation_expression(associative1, tmp1041)
                                        elif len(tmp1041) == 1:
                                            tmp1042 = tmp1041[0]
                                        else:
                                            assert False, "Unreachable"
                                        subst3 = Substitution(subst2)
                                        try:
                                            subst3.try_add_variable('i2.1.1.2.2', tmp1042)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 50468
                                            if len(subjects784) == 0:
                                                pass
                                                # State 50469
                                                if len(subjects670) == 0:
                                                    pass
                                                    # State 50470
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 38: log(c*(d + e*x**2)**p)
                                        if len(subjects784) == 0:
                                            break
                                        tmp1041.append(subjects784.popleft())
                                    subjects784.extendleft(reversed(tmp1041))
                        subjects784.appendleft(tmp1027)
                    subjects670.appendleft(tmp783)
            if len(subjects670) >= 1:
                tmp1044 = subjects670.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.1.1.1', tmp1044)
                except ValueError:
                    pass
                else:
                    pass
                    # State 51114
                    if len(subjects670) == 0:
                        pass
                        # State 51115
                        if len(subjects) == 0:
                            pass
                            # 39: log(u)
                subjects670.appendleft(tmp1044)
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 54120
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 54121
                    if len(subjects670) >= 1:
                        tmp1048 = subjects670.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.2.1.0', tmp1048)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 54122
                            if len(subjects670) == 0:
                                pass
                                # State 54123
                                if len(subjects) == 0:
                                    pass
                                    # 40: log(c + x*d)
                        subjects670.appendleft(tmp1048)
                if len(subjects670) >= 1 and isinstance(subjects670[0], Mul):
                    tmp1050 = subjects670.popleft()
                    associative1 = tmp1050
                    associative_type1 = type(tmp1050)
                    subjects1051 = deque(tmp1050._args)
                    matcher = CommutativeMatcher54125.get()
                    tmp1052 = subjects1051
                    subjects1051 = []
                    for s in tmp1052:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp1052, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 54126
                            if len(subjects670) == 0:
                                pass
                                # State 54127
                                if len(subjects) == 0:
                                    pass
                                    # 40: log(c + x*d)
                    subjects670.appendleft(tmp1050)
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.1.1.2.0_2', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 114000
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.1.1.2.1.0', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 114001
                    if len(subjects670) >= 1 and isinstance(subjects670[0], Pow):
                        tmp1055 = subjects670.popleft()
                        subjects1056 = deque(tmp1055._args)
                        # State 114002
                        if len(subjects1056) >= 1:
                            tmp1057 = subjects1056.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.1.1.2.0', tmp1057)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 114003
                                if len(subjects1056) >= 1 and subjects1056[0] == 2:
                                    tmp1059 = subjects1056.popleft()
                                    # State 114004
                                    if len(subjects1056) == 0:
                                        pass
                                        # State 114005
                                        if len(subjects670) == 0:
                                            pass
                                            # State 114006
                                            if len(subjects) == 0:
                                                pass
                                                # 136: log(x**2*g + f)
                                    subjects1056.appendleft(tmp1059)
                            subjects1056.appendleft(tmp1057)
                        subjects670.appendleft(tmp1055)
                if len(subjects670) >= 1 and isinstance(subjects670[0], Mul):
                    tmp1060 = subjects670.popleft()
                    associative1 = tmp1060
                    associative_type1 = type(tmp1060)
                    subjects1061 = deque(tmp1060._args)
                    matcher = CommutativeMatcher114008.get()
                    tmp1062 = subjects1061
                    subjects1061 = []
                    for s in tmp1062:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp1062, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 114013
                            if len(subjects670) == 0:
                                pass
                                # State 114014
                                if len(subjects) == 0:
                                    pass
                                    # 136: log(x**2*g + f)
                    subjects670.appendleft(tmp1060)
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.1.1.2.0_1', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 114150
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.1.1.2.1.0', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 114151
                    if len(subjects670) >= 1 and isinstance(subjects670[0], Pow):
                        tmp1065 = subjects670.popleft()
                        subjects1066 = deque(tmp1065._args)
                        # State 114152
                        if len(subjects1066) >= 1:
                            tmp1067 = subjects1066.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.1', tmp1067)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 114153
                                if len(subjects1066) >= 1 and subjects1066[0] == 2:
                                    tmp1069 = subjects1066.popleft()
                                    # State 114154
                                    if len(subjects1066) == 0:
                                        pass
                                        # State 114155
                                        if len(subjects670) == 0:
                                            pass
                                            # State 114156
                                            if len(subjects) == 0:
                                                pass
                                                # 139: log(f + g*x**2)
                                    subjects1066.appendleft(tmp1069)
                            subjects1066.appendleft(tmp1067)
                        subjects670.appendleft(tmp1065)
                if len(subjects670) >= 1 and isinstance(subjects670[0], Mul):
                    tmp1070 = subjects670.popleft()
                    associative1 = tmp1070
                    associative_type1 = type(tmp1070)
                    subjects1071 = deque(tmp1070._args)
                    matcher = CommutativeMatcher114158.get()
                    tmp1072 = subjects1071
                    subjects1071 = []
                    for s in tmp1072:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp1072, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 114163
                            if len(subjects670) == 0:
                                pass
                                # State 114164
                                if len(subjects) == 0:
                                    pass
                                    # 139: log(f + g*x**2)
                    subjects670.appendleft(tmp1070)
            if len(subjects670) >= 1 and isinstance(subjects670[0], Mul):
                tmp1073 = subjects670.popleft()
                associative1 = tmp1073
                associative_type1 = type(tmp1073)
                subjects1074 = deque(tmp1073._args)
                matcher = CommutativeMatcher16968.get()
                tmp1075 = subjects1074
                subjects1074 = []
                for s in tmp1075:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp1075, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 16969
                        if len(subjects670) == 0:
                            pass
                            # State 16970
                            if len(subjects) == 0:
                                pass
                                # 26: log(v*c)
                    if pattern_index == 1:
                        pass
                        # State 24043
                        if len(subjects670) == 0:
                            pass
                            # State 24044
                            if len(subjects) == 0:
                                pass
                                # 27: log(c*(e + f*x))
                    if pattern_index == 2:
                        pass
                        # State 25460
                        if len(subjects670) == 0:
                            pass
                            # State 25461
                            if len(subjects) == 0:
                                pass
                                # 28: log(c*(d*(e + f*x)**p)**q)
                    if pattern_index == 3:
                        pass
                        # State 25989
                        if len(subjects670) == 0:
                            pass
                            # State 25990
                            if len(subjects) == 0:
                                pass
                                # 29: log(c/(e + f*x))
                    if pattern_index == 4:
                        pass
                        # State 26516
                        if len(subjects670) == 0:
                            pass
                            # State 26517
                            if len(subjects) == 0:
                                pass
                                # 30: log(c/(e + f*x))
                    if pattern_index == 5:
                        pass
                        # State 27226
                        if len(subjects670) == 0:
                            pass
                            # State 27227
                            if len(subjects) == 0:
                                pass
                                # 31: log(c*(d*(e + f*x)**p)**q)
                    if pattern_index == 6:
                        pass
                        # State 27456
                        if len(subjects670) == 0:
                            pass
                            # State 27457
                            if len(subjects) == 0:
                                pass
                                # 32: log(c*(d*(e + f*x)**p)**q)
                    if pattern_index == 7:
                        pass
                        # State 28293
                        if len(subjects670) == 0:
                            pass
                            # State 28294
                            if len(subjects) == 0:
                                pass
                                # 33: log(c*(d*(e + f*x)**p)**q)
                    if pattern_index == 8:
                        pass
                        # State 40444
                        if len(subjects670) == 0:
                            pass
                            # State 40445
                            if len(subjects) == 0:
                                pass
                                # 34: log(c*x**n)
                    if pattern_index == 9:
                        pass
                        # State 49756
                        if len(subjects670) == 0:
                            pass
                            # State 49757
                            if len(subjects) == 0:
                                pass
                                # 35: log(c*(d + e*x**n)**p)
                    if pattern_index == 10:
                        pass
                        # State 49813
                        if len(subjects670) == 0:
                            pass
                            # State 49814
                            if len(subjects) == 0:
                                pass
                                # 36: log(c*v**p)
                    if pattern_index == 11:
                        pass
                        # State 50181
                        if len(subjects670) == 0:
                            pass
                            # State 50182
                            if len(subjects) == 0:
                                pass
                                # 37: log(c*(d + e*x**n)**p)
                    if pattern_index == 12:
                        pass
                        # State 50507
                        if len(subjects670) == 0:
                            pass
                            # State 50508
                            if len(subjects) == 0:
                                pass
                                # 38: log(c*(d + e*x**2)**p)
                subjects670.appendleft(tmp1073)
            if len(subjects670) >= 1 and isinstance(subjects670[0], Add):
                tmp1076 = subjects670.popleft()
                associative1 = tmp1076
                associative_type1 = type(tmp1076)
                subjects1077 = deque(tmp1076._args)
                matcher = CommutativeMatcher54129.get()
                tmp1078 = subjects1077
                subjects1077 = []
                for s in tmp1078:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp1078, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 54135
                        if len(subjects670) == 0:
                            pass
                            # State 54136
                            if len(subjects) == 0:
                                pass
                                # 40: log(c + x*d)
                    if pattern_index == 1:
                        pass
                        # State 114025
                        if len(subjects670) == 0:
                            pass
                            # State 114026
                            if len(subjects) == 0:
                                pass
                                # 136: log(x**2*g + f)
                    if pattern_index == 2:
                        pass
                        # State 114172
                        if len(subjects670) == 0:
                            pass
                            # State 114173
                            if len(subjects) == 0:
                                pass
                                # 139: log(f + g*x**2)
                    if pattern_index == 3:
                        pass
                        # State 114265
                        if len(subjects670) == 0:
                            pass
                            # State 114266
                            if len(subjects) == 0:
                                pass
                                # 141: log(f + g*x**2)
                subjects670.appendleft(tmp1076)
            subjects.appendleft(tmp669)
        if len(subjects) >= 1 and isinstance(subjects[0], sin):
            tmp1079 = subjects.popleft()
            subjects1080 = deque(tmp1079._args)
            # State 58553
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 58554
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.2.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 58555
                    if len(subjects1080) >= 1:
                        tmp1083 = subjects1080.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.2.1.0', tmp1083)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 58556
                            if len(subjects1080) == 0:
                                pass
                                # State 58557
                                if len(subjects) == 0:
                                    pass
                                    # 41: sin(e + x*f)
                        subjects1080.appendleft(tmp1083)
                if len(subjects1080) >= 1 and isinstance(subjects1080[0], Mul):
                    tmp1085 = subjects1080.popleft()
                    associative1 = tmp1085
                    associative_type1 = type(tmp1085)
                    subjects1086 = deque(tmp1085._args)
                    matcher = CommutativeMatcher58559.get()
                    tmp1087 = subjects1086
                    subjects1086 = []
                    for s in tmp1087:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp1087, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 58560
                            if len(subjects1080) == 0:
                                pass
                                # State 58561
                                if len(subjects) == 0:
                                    pass
                                    # 41: sin(e + x*f)
                    subjects1080.appendleft(tmp1085)
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.1.1.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 59762
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.1.1.2.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 59763
                    if len(subjects1080) >= 1:
                        tmp1090 = subjects1080.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.1.1.2.1.0', tmp1090)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 59764
                            if len(subjects1080) == 0:
                                pass
                                # State 59765
                                if len(subjects) == 0:
                                    pass
                                    # 43: sin(e + x*f)
                        subjects1080.appendleft(tmp1090)
                if len(subjects1080) >= 1 and isinstance(subjects1080[0], Mul):
                    tmp1092 = subjects1080.popleft()
                    associative1 = tmp1092
                    associative_type1 = type(tmp1092)
                    subjects1093 = deque(tmp1092._args)
                    matcher = CommutativeMatcher59767.get()
                    tmp1094 = subjects1093
                    subjects1093 = []
                    for s in tmp1094:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp1094, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 59768
                            if len(subjects1080) == 0:
                                pass
                                # State 59769
                                if len(subjects) == 0:
                                    pass
                                    # 43: sin(e + x*f)
                    subjects1080.appendleft(tmp1092)
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 60023
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 60024
                    if len(subjects1080) >= 1:
                        tmp1097 = subjects1080.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.2.1.0', tmp1097)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 60025
                            if len(subjects1080) == 0:
                                pass
                                # State 60026
                                if len(subjects) == 0:
                                    pass
                                    # 45: sin(c + x*d)
                        subjects1080.appendleft(tmp1097)
                if len(subjects1080) >= 1 and isinstance(subjects1080[0], Mul):
                    tmp1099 = subjects1080.popleft()
                    associative1 = tmp1099
                    associative_type1 = type(tmp1099)
                    subjects1100 = deque(tmp1099._args)
                    matcher = CommutativeMatcher60028.get()
                    tmp1101 = subjects1100
                    subjects1100 = []
                    for s in tmp1101:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp1101, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 60029
                            if len(subjects1080) == 0:
                                pass
                                # State 60030
                                if len(subjects) == 0:
                                    pass
                                    # 45: sin(c + x*d)
                    subjects1080.appendleft(tmp1099)
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.3.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 66130
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.3.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 66131
                    if len(subjects1080) >= 1:
                        tmp1104 = subjects1080.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.3.1.0', tmp1104)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 66132
                            if len(subjects1080) == 0:
                                pass
                                # State 66133
                                if len(subjects) == 0:
                                    pass
                                    # 54: sin(e + x*f)
                        subjects1080.appendleft(tmp1104)
                if len(subjects1080) >= 1 and isinstance(subjects1080[0], Mul):
                    tmp1106 = subjects1080.popleft()
                    associative1 = tmp1106
                    associative_type1 = type(tmp1106)
                    subjects1107 = deque(tmp1106._args)
                    matcher = CommutativeMatcher66135.get()
                    tmp1108 = subjects1107
                    subjects1107 = []
                    for s in tmp1108:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp1108, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 66136
                            if len(subjects1080) == 0:
                                pass
                                # State 66137
                                if len(subjects) == 0:
                                    pass
                                    # 54: sin(e + x*f)
                    subjects1080.appendleft(tmp1106)
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.3.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 71897
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.3.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 71898
                    if len(subjects1080) >= 1:
                        tmp1111 = subjects1080.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.3.1.0', tmp1111)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 71899
                            if len(subjects1080) == 0:
                                pass
                                # State 71900
                                if len(subjects) == 0:
                                    pass
                                    # 57: sin(e + x*f)
                        subjects1080.appendleft(tmp1111)
                if len(subjects1080) >= 1 and isinstance(subjects1080[0], Mul):
                    tmp1113 = subjects1080.popleft()
                    associative1 = tmp1113
                    associative_type1 = type(tmp1113)
                    subjects1114 = deque(tmp1113._args)
                    matcher = CommutativeMatcher71902.get()
                    tmp1115 = subjects1114
                    subjects1114 = []
                    for s in tmp1115:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp1115, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 71903
                            if len(subjects1080) == 0:
                                pass
                                # State 71904
                                if len(subjects) == 0:
                                    pass
                                    # 57: sin(e + x*f)
                    subjects1080.appendleft(tmp1113)
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.1.1.3.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 99673
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.1.1.3.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 99674
                    if len(subjects1080) >= 1:
                        tmp1118 = subjects1080.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.1.1.3.1.0', tmp1118)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 99675
                            if len(subjects1080) == 0:
                                pass
                                # State 99676
                                if len(subjects) == 0:
                                    pass
                                    # 93: sin(c + x*d)
                        subjects1080.appendleft(tmp1118)
                if len(subjects1080) >= 1 and isinstance(subjects1080[0], Mul):
                    tmp1120 = subjects1080.popleft()
                    associative1 = tmp1120
                    associative_type1 = type(tmp1120)
                    subjects1121 = deque(tmp1120._args)
                    matcher = CommutativeMatcher99678.get()
                    tmp1122 = subjects1121
                    subjects1121 = []
                    for s in tmp1122:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp1122, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 99679
                            if len(subjects1080) == 0:
                                pass
                                # State 99680
                                if len(subjects) == 0:
                                    pass
                                    # 93: sin(c + x*d)
                    subjects1080.appendleft(tmp1120)
            if len(subjects1080) >= 1 and isinstance(subjects1080[0], Add):
                tmp1123 = subjects1080.popleft()
                associative1 = tmp1123
                associative_type1 = type(tmp1123)
                subjects1124 = deque(tmp1123._args)
                matcher = CommutativeMatcher58563.get()
                tmp1125 = subjects1124
                subjects1124 = []
                for s in tmp1125:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp1125, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 58569
                        if len(subjects1080) == 0:
                            pass
                            # State 58570
                            if len(subjects) == 0:
                                pass
                                # 41: sin(e + x*f)
                    if pattern_index == 1:
                        pass
                        # State 59773
                        if len(subjects1080) == 0:
                            pass
                            # State 59774
                            if len(subjects) == 0:
                                pass
                                # 43: sin(e + x*f)
                    if pattern_index == 2:
                        pass
                        # State 60034
                        if len(subjects1080) == 0:
                            pass
                            # State 60035
                            if len(subjects) == 0:
                                pass
                                # 45: sin(c + x*d)
                    if pattern_index == 3:
                        pass
                        # State 66141
                        if len(subjects1080) == 0:
                            pass
                            # State 66142
                            if len(subjects) == 0:
                                pass
                                # 54: sin(e + x*f)
                    if pattern_index == 4:
                        pass
                        # State 71908
                        if len(subjects1080) == 0:
                            pass
                            # State 71909
                            if len(subjects) == 0:
                                pass
                                # 57: sin(e + x*f)
                    if pattern_index == 5:
                        pass
                        # State 99684
                        if len(subjects1080) == 0:
                            pass
                            # State 99685
                            if len(subjects) == 0:
                                pass
                                # 93: sin(c + x*d)
                subjects1080.appendleft(tmp1123)
            subjects.appendleft(tmp1079)
        if len(subjects) >= 1 and isinstance(subjects[0], cos):
            tmp1126 = subjects.popleft()
            subjects1127 = deque(tmp1126._args)
            # State 58602
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 58603
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.2.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 58604
                    if len(subjects1127) >= 1:
                        tmp1130 = subjects1127.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.2.1.0', tmp1130)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 58605
                            if len(subjects1127) == 0:
                                pass
                                # State 58606
                                if len(subjects) == 0:
                                    pass
                                    # 42: cos(e + x*f)
                        subjects1127.appendleft(tmp1130)
                if len(subjects1127) >= 1 and isinstance(subjects1127[0], Mul):
                    tmp1132 = subjects1127.popleft()
                    associative1 = tmp1132
                    associative_type1 = type(tmp1132)
                    subjects1133 = deque(tmp1132._args)
                    matcher = CommutativeMatcher58608.get()
                    tmp1134 = subjects1133
                    subjects1133 = []
                    for s in tmp1134:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp1134, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 58609
                            if len(subjects1127) == 0:
                                pass
                                # State 58610
                                if len(subjects) == 0:
                                    pass
                                    # 42: cos(e + x*f)
                    subjects1127.appendleft(tmp1132)
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.1.1.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 59850
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.1.1.2.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 59851
                    if len(subjects1127) >= 1:
                        tmp1137 = subjects1127.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.1.1.2.1.0', tmp1137)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 59852
                            if len(subjects1127) == 0:
                                pass
                                # State 59853
                                if len(subjects) == 0:
                                    pass
                                    # 44: cos(e + x*f)
                        subjects1127.appendleft(tmp1137)
                if len(subjects1127) >= 1 and isinstance(subjects1127[0], Mul):
                    tmp1139 = subjects1127.popleft()
                    associative1 = tmp1139
                    associative_type1 = type(tmp1139)
                    subjects1140 = deque(tmp1139._args)
                    matcher = CommutativeMatcher59855.get()
                    tmp1141 = subjects1140
                    subjects1140 = []
                    for s in tmp1141:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp1141, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 59856
                            if len(subjects1127) == 0:
                                pass
                                # State 59857
                                if len(subjects) == 0:
                                    pass
                                    # 44: cos(e + x*f)
                    subjects1127.appendleft(tmp1139)
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 60139
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 60140
                    if len(subjects1127) >= 1:
                        tmp1144 = subjects1127.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.2.1.0', tmp1144)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 60141
                            if len(subjects1127) == 0:
                                pass
                                # State 60142
                                if len(subjects) == 0:
                                    pass
                                    # 46: cos(c + x*d)
                        subjects1127.appendleft(tmp1144)
                if len(subjects1127) >= 1 and isinstance(subjects1127[0], Mul):
                    tmp1146 = subjects1127.popleft()
                    associative1 = tmp1146
                    associative_type1 = type(tmp1146)
                    subjects1147 = deque(tmp1146._args)
                    matcher = CommutativeMatcher60144.get()
                    tmp1148 = subjects1147
                    subjects1147 = []
                    for s in tmp1148:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp1148, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 60145
                            if len(subjects1127) == 0:
                                pass
                                # State 60146
                                if len(subjects) == 0:
                                    pass
                                    # 46: cos(c + x*d)
                    subjects1127.appendleft(tmp1146)
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.3.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 66221
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.3.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 66222
                    if len(subjects1127) >= 1:
                        tmp1151 = subjects1127.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.3.1.0', tmp1151)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 66223
                            if len(subjects1127) == 0:
                                pass
                                # State 66224
                                if len(subjects) == 0:
                                    pass
                                    # 56: cos(e + x*f)
                        subjects1127.appendleft(tmp1151)
                if len(subjects1127) >= 1 and isinstance(subjects1127[0], Mul):
                    tmp1153 = subjects1127.popleft()
                    associative1 = tmp1153
                    associative_type1 = type(tmp1153)
                    subjects1154 = deque(tmp1153._args)
                    matcher = CommutativeMatcher66226.get()
                    tmp1155 = subjects1154
                    subjects1154 = []
                    for s in tmp1155:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp1155, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 66227
                            if len(subjects1127) == 0:
                                pass
                                # State 66228
                                if len(subjects) == 0:
                                    pass
                                    # 56: cos(e + x*f)
                    subjects1127.appendleft(tmp1153)
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.3.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 71931
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.3.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 71932
                    if len(subjects1127) >= 1:
                        tmp1158 = subjects1127.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.3.1.0', tmp1158)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 71933
                            if len(subjects1127) == 0:
                                pass
                                # State 71934
                                if len(subjects) == 0:
                                    pass
                                    # 58: cos(e + x*f)
                        subjects1127.appendleft(tmp1158)
                if len(subjects1127) >= 1 and isinstance(subjects1127[0], Mul):
                    tmp1160 = subjects1127.popleft()
                    associative1 = tmp1160
                    associative_type1 = type(tmp1160)
                    subjects1161 = deque(tmp1160._args)
                    matcher = CommutativeMatcher71936.get()
                    tmp1162 = subjects1161
                    subjects1161 = []
                    for s in tmp1162:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp1162, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 71937
                            if len(subjects1127) == 0:
                                pass
                                # State 71938
                                if len(subjects) == 0:
                                    pass
                                    # 58: cos(e + x*f)
                    subjects1127.appendleft(tmp1160)
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.1.1.3.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 99704
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.1.1.3.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 99705
                    if len(subjects1127) >= 1:
                        tmp1165 = subjects1127.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.1.1.3.1.0', tmp1165)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 99706
                            if len(subjects1127) == 0:
                                pass
                                # State 99707
                                if len(subjects) == 0:
                                    pass
                                    # 94: cos(c + x*d)
                        subjects1127.appendleft(tmp1165)
                if len(subjects1127) >= 1 and isinstance(subjects1127[0], Mul):
                    tmp1167 = subjects1127.popleft()
                    associative1 = tmp1167
                    associative_type1 = type(tmp1167)
                    subjects1168 = deque(tmp1167._args)
                    matcher = CommutativeMatcher99709.get()
                    tmp1169 = subjects1168
                    subjects1168 = []
                    for s in tmp1169:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp1169, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 99710
                            if len(subjects1127) == 0:
                                pass
                                # State 99711
                                if len(subjects) == 0:
                                    pass
                                    # 94: cos(c + x*d)
                    subjects1127.appendleft(tmp1167)
            if len(subjects1127) >= 1 and isinstance(subjects1127[0], Add):
                tmp1170 = subjects1127.popleft()
                associative1 = tmp1170
                associative_type1 = type(tmp1170)
                subjects1171 = deque(tmp1170._args)
                matcher = CommutativeMatcher58612.get()
                tmp1172 = subjects1171
                subjects1171 = []
                for s in tmp1172:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp1172, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 58618
                        if len(subjects1127) == 0:
                            pass
                            # State 58619
                            if len(subjects) == 0:
                                pass
                                # 42: cos(e + x*f)
                    if pattern_index == 1:
                        pass
                        # State 59861
                        if len(subjects1127) == 0:
                            pass
                            # State 59862
                            if len(subjects) == 0:
                                pass
                                # 44: cos(e + x*f)
                    if pattern_index == 2:
                        pass
                        # State 60150
                        if len(subjects1127) == 0:
                            pass
                            # State 60151
                            if len(subjects) == 0:
                                pass
                                # 46: cos(c + x*d)
                    if pattern_index == 3:
                        pass
                        # State 66232
                        if len(subjects1127) == 0:
                            pass
                            # State 66233
                            if len(subjects) == 0:
                                pass
                                # 56: cos(e + x*f)
                    if pattern_index == 4:
                        pass
                        # State 71942
                        if len(subjects1127) == 0:
                            pass
                            # State 71943
                            if len(subjects) == 0:
                                pass
                                # 58: cos(e + x*f)
                    if pattern_index == 5:
                        pass
                        # State 99715
                        if len(subjects1127) == 0:
                            pass
                            # State 99716
                            if len(subjects) == 0:
                                pass
                                # 94: cos(c + x*d)
                subjects1127.appendleft(tmp1170)
            subjects.appendleft(tmp1126)
        if len(subjects) >= 1 and isinstance(subjects[0], tan):
            tmp1173 = subjects.popleft()
            subjects1174 = deque(tmp1173._args)
            # State 77592
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.3.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 77593
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.3.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 77594
                    if len(subjects1174) >= 1:
                        tmp1177 = subjects1174.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.3.1.0', tmp1177)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 77595
                            if len(subjects1174) == 0:
                                pass
                                # State 77596
                                if len(subjects) == 0:
                                    pass
                                    # 59: tan(e + x*f)
                        subjects1174.appendleft(tmp1177)
                if len(subjects1174) >= 1 and isinstance(subjects1174[0], Mul):
                    tmp1179 = subjects1174.popleft()
                    associative1 = tmp1179
                    associative_type1 = type(tmp1179)
                    subjects1180 = deque(tmp1179._args)
                    matcher = CommutativeMatcher77598.get()
                    tmp1181 = subjects1180
                    subjects1180 = []
                    for s in tmp1181:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp1181, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 77599
                            if len(subjects1174) == 0:
                                pass
                                # State 77600
                                if len(subjects) == 0:
                                    pass
                                    # 59: tan(e + x*f)
                    subjects1174.appendleft(tmp1179)
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.1.1.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 78782
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.1.1.2.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 78783
                    if len(subjects1174) >= 1:
                        tmp1184 = subjects1174.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.1.1.2.1.0', tmp1184)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 78784
                            if len(subjects1174) == 0:
                                pass
                                # State 78785
                                if len(subjects) == 0:
                                    pass
                                    # 61: tan(e + x*f)
                        subjects1174.appendleft(tmp1184)
                if len(subjects1174) >= 1 and isinstance(subjects1174[0], Mul):
                    tmp1186 = subjects1174.popleft()
                    associative1 = tmp1186
                    associative_type1 = type(tmp1186)
                    subjects1187 = deque(tmp1186._args)
                    matcher = CommutativeMatcher78787.get()
                    tmp1188 = subjects1187
                    subjects1187 = []
                    for s in tmp1188:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp1188, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 78788
                            if len(subjects1174) == 0:
                                pass
                                # State 78789
                                if len(subjects) == 0:
                                    pass
                                    # 61: tan(e + x*f)
                    subjects1174.appendleft(tmp1186)
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 79035
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 79036
                    if len(subjects1174) >= 1:
                        tmp1191 = subjects1174.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.2.1.0', tmp1191)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 79037
                            if len(subjects1174) == 0:
                                pass
                                # State 79038
                                if len(subjects) == 0:
                                    pass
                                    # 63: tan(c + x*d)
                        subjects1174.appendleft(tmp1191)
                if len(subjects1174) >= 1 and isinstance(subjects1174[0], Mul):
                    tmp1193 = subjects1174.popleft()
                    associative1 = tmp1193
                    associative_type1 = type(tmp1193)
                    subjects1194 = deque(tmp1193._args)
                    matcher = CommutativeMatcher79040.get()
                    tmp1195 = subjects1194
                    subjects1194 = []
                    for s in tmp1195:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp1195, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 79041
                            if len(subjects1174) == 0:
                                pass
                                # State 79042
                                if len(subjects) == 0:
                                    pass
                                    # 63: tan(c + x*d)
                    subjects1174.appendleft(tmp1193)
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 79318
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.2.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 79319
                    if len(subjects1174) >= 1:
                        tmp1198 = subjects1174.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.2.1.0', tmp1198)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 79320
                            if len(subjects1174) == 0:
                                pass
                                # State 79321
                                if len(subjects) == 0:
                                    pass
                                    # 65: tan(e + x*f)
                        subjects1174.appendleft(tmp1198)
                if len(subjects1174) >= 1 and isinstance(subjects1174[0], Mul):
                    tmp1200 = subjects1174.popleft()
                    associative1 = tmp1200
                    associative_type1 = type(tmp1200)
                    subjects1201 = deque(tmp1200._args)
                    matcher = CommutativeMatcher79323.get()
                    tmp1202 = subjects1201
                    subjects1201 = []
                    for s in tmp1202:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp1202, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 79324
                            if len(subjects1174) == 0:
                                pass
                                # State 79325
                                if len(subjects) == 0:
                                    pass
                                    # 65: tan(e + x*f)
                    subjects1174.appendleft(tmp1200)
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.3.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 81689
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.3.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 81690
                    if len(subjects1174) >= 1:
                        tmp1205 = subjects1174.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.3.1.0', tmp1205)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 81691
                            if len(subjects1174) == 0:
                                pass
                                # State 81692
                                if len(subjects) == 0:
                                    pass
                                    # 69: tan(e + x*f)
                        subjects1174.appendleft(tmp1205)
                if len(subjects1174) >= 1 and isinstance(subjects1174[0], Mul):
                    tmp1207 = subjects1174.popleft()
                    associative1 = tmp1207
                    associative_type1 = type(tmp1207)
                    subjects1208 = deque(tmp1207._args)
                    matcher = CommutativeMatcher81694.get()
                    tmp1209 = subjects1208
                    subjects1208 = []
                    for s in tmp1209:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp1209, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 81695
                            if len(subjects1174) == 0:
                                pass
                                # State 81696
                                if len(subjects) == 0:
                                    pass
                                    # 69: tan(e + x*f)
                    subjects1174.appendleft(tmp1207)
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.3.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 86602
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.3.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 86603
                    if len(subjects1174) >= 1:
                        tmp1212 = subjects1174.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.3.1.0', tmp1212)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 86604
                            if len(subjects1174) == 0:
                                pass
                                # State 86605
                                if len(subjects) == 0:
                                    pass
                                    # 71: tan(e + x*f)
                        subjects1174.appendleft(tmp1212)
                if len(subjects1174) >= 1 and isinstance(subjects1174[0], Mul):
                    tmp1214 = subjects1174.popleft()
                    associative1 = tmp1214
                    associative_type1 = type(tmp1214)
                    subjects1215 = deque(tmp1214._args)
                    matcher = CommutativeMatcher86607.get()
                    tmp1216 = subjects1215
                    subjects1215 = []
                    for s in tmp1216:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp1216, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 86608
                            if len(subjects1174) == 0:
                                pass
                                # State 86609
                                if len(subjects) == 0:
                                    pass
                                    # 71: tan(e + x*f)
                    subjects1174.appendleft(tmp1214)
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.1.1.3.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 100052
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.1.1.3.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 100053
                    if len(subjects1174) >= 1:
                        tmp1219 = subjects1174.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.1.1.3.1.0', tmp1219)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 100054
                            if len(subjects1174) == 0:
                                pass
                                # State 100055
                                if len(subjects) == 0:
                                    pass
                                    # 105: tan(e + x*f)
                        subjects1174.appendleft(tmp1219)
                if len(subjects1174) >= 1 and isinstance(subjects1174[0], Mul):
                    tmp1221 = subjects1174.popleft()
                    associative1 = tmp1221
                    associative_type1 = type(tmp1221)
                    subjects1222 = deque(tmp1221._args)
                    matcher = CommutativeMatcher100057.get()
                    tmp1223 = subjects1222
                    subjects1222 = []
                    for s in tmp1223:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp1223, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 100058
                            if len(subjects1174) == 0:
                                pass
                                # State 100059
                                if len(subjects) == 0:
                                    pass
                                    # 105: tan(e + x*f)
                    subjects1174.appendleft(tmp1221)
            if len(subjects1174) >= 1 and isinstance(subjects1174[0], Add):
                tmp1224 = subjects1174.popleft()
                associative1 = tmp1224
                associative_type1 = type(tmp1224)
                subjects1225 = deque(tmp1224._args)
                matcher = CommutativeMatcher77602.get()
                tmp1226 = subjects1225
                subjects1225 = []
                for s in tmp1226:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp1226, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 77608
                        if len(subjects1174) == 0:
                            pass
                            # State 77609
                            if len(subjects) == 0:
                                pass
                                # 59: tan(e + x*f)
                    if pattern_index == 1:
                        pass
                        # State 78793
                        if len(subjects1174) == 0:
                            pass
                            # State 78794
                            if len(subjects) == 0:
                                pass
                                # 61: tan(e + x*f)
                    if pattern_index == 2:
                        pass
                        # State 79046
                        if len(subjects1174) == 0:
                            pass
                            # State 79047
                            if len(subjects) == 0:
                                pass
                                # 63: tan(c + x*d)
                    if pattern_index == 3:
                        pass
                        # State 79329
                        if len(subjects1174) == 0:
                            pass
                            # State 79330
                            if len(subjects) == 0:
                                pass
                                # 65: tan(e + x*f)
                    if pattern_index == 4:
                        pass
                        # State 81700
                        if len(subjects1174) == 0:
                            pass
                            # State 81701
                            if len(subjects) == 0:
                                pass
                                # 69: tan(e + x*f)
                    if pattern_index == 5:
                        pass
                        # State 86613
                        if len(subjects1174) == 0:
                            pass
                            # State 86614
                            if len(subjects) == 0:
                                pass
                                # 71: tan(e + x*f)
                    if pattern_index == 6:
                        pass
                        # State 100063
                        if len(subjects1174) == 0:
                            pass
                            # State 100064
                            if len(subjects) == 0:
                                pass
                                # 105: tan(e + x*f)
                subjects1174.appendleft(tmp1224)
            subjects.appendleft(tmp1173)
        if len(subjects) >= 1 and isinstance(subjects[0], asin):
            tmp1227 = subjects.popleft()
            subjects1228 = deque(tmp1227._args)
            # State 108760
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.1.1.2.0', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 108761
                if len(subjects1228) >= 1:
                    tmp1230 = subjects1228.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.1', tmp1230)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 108762
                        if len(subjects1228) == 0:
                            pass
                            # State 108763
                            if len(subjects) == 0:
                                pass
                                # 121: asin(c*x)
                    subjects1228.appendleft(tmp1230)
                if len(subjects1228) >= 1:
                    tmp1232 = subjects1228.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.0', tmp1232)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 109168
                        if len(subjects1228) == 0:
                            pass
                            # State 109169
                            if len(subjects) == 0:
                                pass
                                # 123: asin(c*x)
                    subjects1228.appendleft(tmp1232)
                if len(subjects1228) >= 1:
                    tmp1234 = subjects1228.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.0', tmp1234)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 109574
                        if len(subjects1228) == 0:
                            pass
                            # State 109575
                            if len(subjects) == 0:
                                pass
                                # 127: asin(c*x)
                    subjects1228.appendleft(tmp1234)
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.1.1.2.0_1', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 109519
                if len(subjects1228) >= 1:
                    tmp1237 = subjects1228.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.1.1.2.0', tmp1237)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 109520
                        if len(subjects1228) == 0:
                            pass
                            # State 109521
                            if len(subjects) == 0:
                                pass
                                # 125: asin(x*c)
                    subjects1228.appendleft(tmp1237)
            if len(subjects1228) >= 1:
                tmp1239 = subjects1228.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.1.1.1', tmp1239)
                except ValueError:
                    pass
                else:
                    pass
                    # State 112563
                    if len(subjects1228) == 0:
                        pass
                        # State 112564
                        if len(subjects) == 0:
                            pass
                            # 129: asin(u)
                subjects1228.appendleft(tmp1239)
            if len(subjects1228) >= 1 and isinstance(subjects1228[0], Mul):
                tmp1241 = subjects1228.popleft()
                associative1 = tmp1241
                associative_type1 = type(tmp1241)
                subjects1242 = deque(tmp1241._args)
                matcher = CommutativeMatcher108765.get()
                tmp1243 = subjects1242
                subjects1242 = []
                for s in tmp1243:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp1243, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 108766
                        if len(subjects1228) == 0:
                            pass
                            # State 108767
                            if len(subjects) == 0:
                                pass
                                # 121: asin(c*x)
                    if pattern_index == 1:
                        pass
                        # State 109170
                        if len(subjects1228) == 0:
                            pass
                            # State 109171
                            if len(subjects) == 0:
                                pass
                                # 123: asin(c*x)
                    if pattern_index == 2:
                        pass
                        # State 109522
                        if len(subjects1228) == 0:
                            pass
                            # State 109523
                            if len(subjects) == 0:
                                pass
                                # 125: asin(x*c)
                    if pattern_index == 3:
                        pass
                        # State 109576
                        if len(subjects1228) == 0:
                            pass
                            # State 109577
                            if len(subjects) == 0:
                                pass
                                # 127: asin(c*x)
                subjects1228.appendleft(tmp1241)
            subjects.appendleft(tmp1227)
        if len(subjects) >= 1 and isinstance(subjects[0], acos):
            tmp1244 = subjects.popleft()
            subjects1245 = deque(tmp1244._args)
            # State 108798
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.1.1.2.0', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 108799
                if len(subjects1245) >= 1:
                    tmp1247 = subjects1245.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.1', tmp1247)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 108800
                        if len(subjects1245) == 0:
                            pass
                            # State 108801
                            if len(subjects) == 0:
                                pass
                                # 122: acos(c*x)
                    subjects1245.appendleft(tmp1247)
                if len(subjects1245) >= 1:
                    tmp1249 = subjects1245.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.0', tmp1249)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 109190
                        if len(subjects1245) == 0:
                            pass
                            # State 109191
                            if len(subjects) == 0:
                                pass
                                # 124: acos(c*x)
                    subjects1245.appendleft(tmp1249)
                if len(subjects1245) >= 1:
                    tmp1251 = subjects1245.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.0', tmp1251)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 109596
                        if len(subjects1245) == 0:
                            pass
                            # State 109597
                            if len(subjects) == 0:
                                pass
                                # 128: acos(c*x)
                    subjects1245.appendleft(tmp1251)
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.1.1.2.0_1', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 109545
                if len(subjects1245) >= 1:
                    tmp1254 = subjects1245.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.1.1.2.0', tmp1254)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 109546
                        if len(subjects1245) == 0:
                            pass
                            # State 109547
                            if len(subjects) == 0:
                                pass
                                # 126: acos(x*c)
                    subjects1245.appendleft(tmp1254)
            if len(subjects1245) >= 1:
                tmp1256 = subjects1245.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.1.1.1', tmp1256)
                except ValueError:
                    pass
                else:
                    pass
                    # State 112577
                    if len(subjects1245) == 0:
                        pass
                        # State 112578
                        if len(subjects) == 0:
                            pass
                            # 130: acos(u)
                subjects1245.appendleft(tmp1256)
            if len(subjects1245) >= 1 and isinstance(subjects1245[0], Mul):
                tmp1258 = subjects1245.popleft()
                associative1 = tmp1258
                associative_type1 = type(tmp1258)
                subjects1259 = deque(tmp1258._args)
                matcher = CommutativeMatcher108803.get()
                tmp1260 = subjects1259
                subjects1259 = []
                for s in tmp1260:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp1260, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 108804
                        if len(subjects1245) == 0:
                            pass
                            # State 108805
                            if len(subjects) == 0:
                                pass
                                # 122: acos(c*x)
                    if pattern_index == 1:
                        pass
                        # State 109192
                        if len(subjects1245) == 0:
                            pass
                            # State 109193
                            if len(subjects) == 0:
                                pass
                                # 124: acos(c*x)
                    if pattern_index == 2:
                        pass
                        # State 109548
                        if len(subjects1245) == 0:
                            pass
                            # State 109549
                            if len(subjects) == 0:
                                pass
                                # 126: acos(x*c)
                    if pattern_index == 3:
                        pass
                        # State 109598
                        if len(subjects1245) == 0:
                            pass
                            # State 109599
                            if len(subjects) == 0:
                                pass
                                # 128: acos(c*x)
                subjects1245.appendleft(tmp1258)
            subjects.appendleft(tmp1244)
        if len(subjects) >= 1 and isinstance(subjects[0], atan):
            tmp1261 = subjects.popleft()
            subjects1262 = deque(tmp1261._args)
            # State 113009
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.1.1.2.0', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 113010
                if len(subjects1262) >= 1:
                    tmp1264 = subjects1262.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.0', tmp1264)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 113011
                        if len(subjects1262) == 0:
                            pass
                            # State 113012
                            if len(subjects) == 0:
                                pass
                                # 131: atan(c*x)
                    subjects1262.appendleft(tmp1264)
                if len(subjects1262) >= 1:
                    tmp1266 = subjects1262.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.1', tmp1266)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 113173
                        if len(subjects1262) == 0:
                            pass
                            # State 113174
                            if len(subjects) == 0:
                                pass
                                # 133: atan(c*x)
                    subjects1262.appendleft(tmp1266)
                if len(subjects1262) >= 1:
                    tmp1268 = subjects1262.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.1', tmp1268)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 114071
                        if len(subjects1262) == 0:
                            pass
                            # State 114072
                            if len(subjects) == 0:
                                pass
                                # 138: atan(c*x)
                    subjects1262.appendleft(tmp1268)
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.1.1.2.0_1', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 113896
                if len(subjects1262) >= 1:
                    tmp1271 = subjects1262.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.1.1.2.0', tmp1271)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 113897
                        if len(subjects1262) == 0:
                            pass
                            # State 113898
                            if len(subjects) == 0:
                                pass
                                # 135: atan(x*c)
                    subjects1262.appendleft(tmp1271)
            if len(subjects1262) >= 1:
                tmp1273 = subjects1262.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.1.1.1', tmp1273)
                except ValueError:
                    pass
                else:
                    pass
                    # State 119457
                    if len(subjects1262) == 0:
                        pass
                        # State 119458
                        if len(subjects) == 0:
                            pass
                            # 142: atan(u)
                subjects1262.appendleft(tmp1273)
            if len(subjects1262) >= 1 and isinstance(subjects1262[0], Mul):
                tmp1275 = subjects1262.popleft()
                associative1 = tmp1275
                associative_type1 = type(tmp1275)
                subjects1276 = deque(tmp1275._args)
                matcher = CommutativeMatcher113014.get()
                tmp1277 = subjects1276
                subjects1276 = []
                for s in tmp1277:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp1277, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 113015
                        if len(subjects1262) == 0:
                            pass
                            # State 113016
                            if len(subjects) == 0:
                                pass
                                # 131: atan(c*x)
                    if pattern_index == 1:
                        pass
                        # State 113175
                        if len(subjects1262) == 0:
                            pass
                            # State 113176
                            if len(subjects) == 0:
                                pass
                                # 133: atan(c*x)
                    if pattern_index == 2:
                        pass
                        # State 113899
                        if len(subjects1262) == 0:
                            pass
                            # State 113900
                            if len(subjects) == 0:
                                pass
                                # 135: atan(x*c)
                    if pattern_index == 3:
                        pass
                        # State 114073
                        if len(subjects1262) == 0:
                            pass
                            # State 114074
                            if len(subjects) == 0:
                                pass
                                # 138: atan(c*x)
                subjects1262.appendleft(tmp1275)
            subjects.appendleft(tmp1261)
        if len(subjects) >= 1 and isinstance(subjects[0], acot):
            tmp1278 = subjects.popleft()
            subjects1279 = deque(tmp1278._args)
            # State 113030
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.1.1.2.0', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 113031
                if len(subjects1279) >= 1:
                    tmp1281 = subjects1279.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.0', tmp1281)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 113032
                        if len(subjects1279) == 0:
                            pass
                            # State 113033
                            if len(subjects) == 0:
                                pass
                                # 132: acot(c*x)
                    subjects1279.appendleft(tmp1281)
                if len(subjects1279) >= 1:
                    tmp1283 = subjects1279.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.1', tmp1283)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 113195
                        if len(subjects1279) == 0:
                            pass
                            # State 113196
                            if len(subjects) == 0:
                                pass
                                # 134: acot(c*x)
                    subjects1279.appendleft(tmp1283)
                if len(subjects1279) >= 1:
                    tmp1285 = subjects1279.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.1', tmp1285)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 114192
                        if len(subjects1279) == 0:
                            pass
                            # State 114193
                            if len(subjects) == 0:
                                pass
                                # 140: acot(c*x)
                    subjects1279.appendleft(tmp1285)
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.1.1.2.0_1', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 114048
                if len(subjects1279) >= 1:
                    tmp1288 = subjects1279.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.1.1.2.0', tmp1288)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 114049
                        if len(subjects1279) == 0:
                            pass
                            # State 114050
                            if len(subjects) == 0:
                                pass
                                # 137: acot(x*c)
                    subjects1279.appendleft(tmp1288)
            if len(subjects1279) >= 1:
                tmp1290 = subjects1279.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.1.1.1', tmp1290)
                except ValueError:
                    pass
                else:
                    pass
                    # State 119471
                    if len(subjects1279) == 0:
                        pass
                        # State 119472
                        if len(subjects) == 0:
                            pass
                            # 143: acot(u)
                subjects1279.appendleft(tmp1290)
            if len(subjects1279) >= 1 and isinstance(subjects1279[0], Mul):
                tmp1292 = subjects1279.popleft()
                associative1 = tmp1292
                associative_type1 = type(tmp1292)
                subjects1293 = deque(tmp1292._args)
                matcher = CommutativeMatcher113035.get()
                tmp1294 = subjects1293
                subjects1293 = []
                for s in tmp1294:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp1294, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 113036
                        if len(subjects1279) == 0:
                            pass
                            # State 113037
                            if len(subjects) == 0:
                                pass
                                # 132: acot(c*x)
                    if pattern_index == 1:
                        pass
                        # State 113197
                        if len(subjects1279) == 0:
                            pass
                            # State 113198
                            if len(subjects) == 0:
                                pass
                                # 134: acot(c*x)
                    if pattern_index == 2:
                        pass
                        # State 114051
                        if len(subjects1279) == 0:
                            pass
                            # State 114052
                            if len(subjects) == 0:
                                pass
                                # 137: acot(x*c)
                    if pattern_index == 3:
                        pass
                        # State 114194
                        if len(subjects1279) == 0:
                            pass
                            # State 114195
                            if len(subjects) == 0:
                                pass
                                # 140: acot(c*x)
                subjects1279.appendleft(tmp1292)
            subjects.appendleft(tmp1278)
        if len(subjects) >= 1 and isinstance(subjects[0], asec):
            tmp1295 = subjects.popleft()
            subjects1296 = deque(tmp1295._args)
            # State 119654
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.1.1.2.0', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 119655
                if len(subjects1296) >= 1:
                    tmp1298 = subjects1296.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.1', tmp1298)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 119656
                        if len(subjects1296) == 0:
                            pass
                            # State 119657
                            if len(subjects) == 0:
                                pass
                                # 144: asec(c*x)
                    subjects1296.appendleft(tmp1298)
                if len(subjects1296) >= 1:
                    tmp1300 = subjects1296.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.1', tmp1300)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 119908
                        if len(subjects1296) == 0:
                            pass
                            # State 119909
                            if len(subjects) == 0:
                                pass
                                # 146: asec(c*x)
                    subjects1296.appendleft(tmp1300)
            if len(subjects1296) >= 1:
                tmp1302 = subjects1296.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.1.1.1', tmp1302)
                except ValueError:
                    pass
                else:
                    pass
                    # State 121562
                    if len(subjects1296) == 0:
                        pass
                        # State 121563
                        if len(subjects) == 0:
                            pass
                            # 148: asec(u)
                subjects1296.appendleft(tmp1302)
            if len(subjects1296) >= 1 and isinstance(subjects1296[0], Mul):
                tmp1304 = subjects1296.popleft()
                associative1 = tmp1304
                associative_type1 = type(tmp1304)
                subjects1305 = deque(tmp1304._args)
                matcher = CommutativeMatcher119659.get()
                tmp1306 = subjects1305
                subjects1305 = []
                for s in tmp1306:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp1306, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 119660
                        if len(subjects1296) == 0:
                            pass
                            # State 119661
                            if len(subjects) == 0:
                                pass
                                # 144: asec(c*x)
                    if pattern_index == 1:
                        pass
                        # State 119910
                        if len(subjects1296) == 0:
                            pass
                            # State 119911
                            if len(subjects) == 0:
                                pass
                                # 146: asec(c*x)
                subjects1296.appendleft(tmp1304)
            subjects.appendleft(tmp1295)
        if len(subjects) >= 1 and isinstance(subjects[0], acsc):
            tmp1307 = subjects.popleft()
            subjects1308 = deque(tmp1307._args)
            # State 119692
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.1.1.2.0', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 119693
                if len(subjects1308) >= 1:
                    tmp1310 = subjects1308.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.1', tmp1310)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 119694
                        if len(subjects1308) == 0:
                            pass
                            # State 119695
                            if len(subjects) == 0:
                                pass
                                # 145: acsc(c*x)
                    subjects1308.appendleft(tmp1310)
                if len(subjects1308) >= 1:
                    tmp1312 = subjects1308.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.1', tmp1312)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 119930
                        if len(subjects1308) == 0:
                            pass
                            # State 119931
                            if len(subjects) == 0:
                                pass
                                # 147: acsc(c*x)
                    subjects1308.appendleft(tmp1312)
            if len(subjects1308) >= 1:
                tmp1314 = subjects1308.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.1.1.1', tmp1314)
                except ValueError:
                    pass
                else:
                    pass
                    # State 121576
                    if len(subjects1308) == 0:
                        pass
                        # State 121577
                        if len(subjects) == 0:
                            pass
                            # 149: acsc(u)
                subjects1308.appendleft(tmp1314)
            if len(subjects1308) >= 1 and isinstance(subjects1308[0], Mul):
                tmp1316 = subjects1308.popleft()
                associative1 = tmp1316
                associative_type1 = type(tmp1316)
                subjects1317 = deque(tmp1316._args)
                matcher = CommutativeMatcher119697.get()
                tmp1318 = subjects1317
                subjects1317 = []
                for s in tmp1318:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp1318, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 119698
                        if len(subjects1308) == 0:
                            pass
                            # State 119699
                            if len(subjects) == 0:
                                pass
                                # 145: acsc(c*x)
                    if pattern_index == 1:
                        pass
                        # State 119932
                        if len(subjects1308) == 0:
                            pass
                            # State 119933
                            if len(subjects) == 0:
                                pass
                                # 147: acsc(c*x)
                subjects1308.appendleft(tmp1316)
            subjects.appendleft(tmp1307)
        if len(subjects) >= 1 and isinstance(subjects[0], cosh):
            tmp1319 = subjects.popleft()
            subjects1320 = deque(tmp1319._args)
            # State 132805
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 132806
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 132807
                    if len(subjects1320) >= 1:
                        tmp1323 = subjects1320.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.2.1.0', tmp1323)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 132808
                            if len(subjects1320) == 0:
                                pass
                                # State 132809
                                if len(subjects) == 0:
                                    pass
                                    # 150: cosh(e + x*d)
                        subjects1320.appendleft(tmp1323)
                if len(subjects1320) >= 1 and isinstance(subjects1320[0], Mul):
                    tmp1325 = subjects1320.popleft()
                    associative1 = tmp1325
                    associative_type1 = type(tmp1325)
                    subjects1326 = deque(tmp1325._args)
                    matcher = CommutativeMatcher132811.get()
                    tmp1327 = subjects1326
                    subjects1326 = []
                    for s in tmp1327:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp1327, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 132812
                            if len(subjects1320) == 0:
                                pass
                                # State 132813
                                if len(subjects) == 0:
                                    pass
                                    # 150: cosh(e + x*d)
                    subjects1320.appendleft(tmp1325)
            if len(subjects1320) >= 1 and isinstance(subjects1320[0], Add):
                tmp1328 = subjects1320.popleft()
                associative1 = tmp1328
                associative_type1 = type(tmp1328)
                subjects1329 = deque(tmp1328._args)
                matcher = CommutativeMatcher132815.get()
                tmp1330 = subjects1329
                subjects1329 = []
                for s in tmp1330:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp1330, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 132821
                        if len(subjects1320) == 0:
                            pass
                            # State 132822
                            if len(subjects) == 0:
                                pass
                                # 150: cosh(e + x*d)
                subjects1320.appendleft(tmp1328)
            subjects.appendleft(tmp1319)
        if len(subjects) >= 1 and isinstance(subjects[0], sinh):
            tmp1331 = subjects.popleft()
            subjects1332 = deque(tmp1331._args)
            # State 132846
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 132847
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 132848
                    if len(subjects1332) >= 1:
                        tmp1335 = subjects1332.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.2.1.0', tmp1335)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 132849
                            if len(subjects1332) == 0:
                                pass
                                # State 132850
                                if len(subjects) == 0:
                                    pass
                                    # 151: sinh(e + x*d)
                        subjects1332.appendleft(tmp1335)
                if len(subjects1332) >= 1 and isinstance(subjects1332[0], Mul):
                    tmp1337 = subjects1332.popleft()
                    associative1 = tmp1337
                    associative_type1 = type(tmp1337)
                    subjects1338 = deque(tmp1337._args)
                    matcher = CommutativeMatcher132852.get()
                    tmp1339 = subjects1338
                    subjects1338 = []
                    for s in tmp1339:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp1339, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 132853
                            if len(subjects1332) == 0:
                                pass
                                # State 132854
                                if len(subjects) == 0:
                                    pass
                                    # 151: sinh(e + x*d)
                    subjects1332.appendleft(tmp1337)
            if len(subjects1332) >= 1 and isinstance(subjects1332[0], Add):
                tmp1340 = subjects1332.popleft()
                associative1 = tmp1340
                associative_type1 = type(tmp1340)
                subjects1341 = deque(tmp1340._args)
                matcher = CommutativeMatcher132856.get()
                tmp1342 = subjects1341
                subjects1341 = []
                for s in tmp1342:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp1342, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 132862
                        if len(subjects1332) == 0:
                            pass
                            # State 132863
                            if len(subjects) == 0:
                                pass
                                # 151: sinh(e + x*d)
                subjects1332.appendleft(tmp1340)
            subjects.appendleft(tmp1331)
        if len(subjects) >= 1 and isinstance(subjects[0], asinh):
            tmp1343 = subjects.popleft()
            subjects1344 = deque(tmp1343._args)
            # State 138426
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.1.1.2.0', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 138427
                if len(subjects1344) >= 1:
                    tmp1346 = subjects1344.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.1', tmp1346)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 138428
                        if len(subjects1344) == 0:
                            pass
                            # State 138429
                            if len(subjects) == 0:
                                pass
                                # 152: asinh(c*x)
                    subjects1344.appendleft(tmp1346)
                if len(subjects1344) >= 1:
                    tmp1348 = subjects1344.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.0', tmp1348)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 138939
                        if len(subjects1344) == 0:
                            pass
                            # State 138940
                            if len(subjects) == 0:
                                pass
                                # 154: asinh(c*x)
                    subjects1344.appendleft(tmp1348)
                if len(subjects1344) >= 1:
                    tmp1350 = subjects1344.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.0', tmp1350)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 139396
                        if len(subjects1344) == 0:
                            pass
                            # State 139397
                            if len(subjects) == 0:
                                pass
                                # 159: asinh(c*x)
                    subjects1344.appendleft(tmp1350)
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.1.1.2.0_1', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 139341
                if len(subjects1344) >= 1:
                    tmp1353 = subjects1344.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.1.1.2.0', tmp1353)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 139342
                        if len(subjects1344) == 0:
                            pass
                            # State 139343
                            if len(subjects) == 0:
                                pass
                                # 157: asinh(x*c)
                    subjects1344.appendleft(tmp1353)
            if len(subjects1344) >= 1:
                tmp1355 = subjects1344.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.1.1.1', tmp1355)
                except ValueError:
                    pass
                else:
                    pass
                    # State 142145
                    if len(subjects1344) == 0:
                        pass
                        # State 142146
                        if len(subjects) == 0:
                            pass
                            # 160: asinh(u)
                subjects1344.appendleft(tmp1355)
            if len(subjects1344) >= 1 and isinstance(subjects1344[0], Mul):
                tmp1357 = subjects1344.popleft()
                associative1 = tmp1357
                associative_type1 = type(tmp1357)
                subjects1358 = deque(tmp1357._args)
                matcher = CommutativeMatcher138431.get()
                tmp1359 = subjects1358
                subjects1358 = []
                for s in tmp1359:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp1359, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 138432
                        if len(subjects1344) == 0:
                            pass
                            # State 138433
                            if len(subjects) == 0:
                                pass
                                # 152: asinh(c*x)
                    if pattern_index == 1:
                        pass
                        # State 138941
                        if len(subjects1344) == 0:
                            pass
                            # State 138942
                            if len(subjects) == 0:
                                pass
                                # 154: asinh(c*x)
                    if pattern_index == 2:
                        pass
                        # State 139344
                        if len(subjects1344) == 0:
                            pass
                            # State 139345
                            if len(subjects) == 0:
                                pass
                                # 157: asinh(x*c)
                    if pattern_index == 3:
                        pass
                        # State 139398
                        if len(subjects1344) == 0:
                            pass
                            # State 139399
                            if len(subjects) == 0:
                                pass
                                # 159: asinh(c*x)
                subjects1344.appendleft(tmp1357)
            subjects.appendleft(tmp1343)
        if len(subjects) >= 1 and isinstance(subjects[0], acosh):
            tmp1360 = subjects.popleft()
            subjects1361 = deque(tmp1360._args)
            # State 138464
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.1.1.2.0', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 138465
                if len(subjects1361) >= 1:
                    tmp1363 = subjects1361.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.1', tmp1363)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 138466
                        if len(subjects1361) == 0:
                            pass
                            # State 138467
                            if len(subjects) == 0:
                                pass
                                # 153: acosh(c*x)
                    subjects1361.appendleft(tmp1363)
                if len(subjects1361) >= 1:
                    tmp1365 = subjects1361.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.0', tmp1365)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 138961
                        if len(subjects1361) == 0:
                            pass
                            # State 138962
                            if len(subjects) == 0:
                                pass
                                # 155: acosh(c*x)
                    subjects1361.appendleft(tmp1365)
                if len(subjects1361) >= 1:
                    tmp1367 = subjects1361.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.0', tmp1367)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 138994
                        if len(subjects1361) == 0:
                            pass
                            # State 138995
                            if len(subjects) == 0:
                                pass
                                # 156: acosh(c*x)
                    subjects1361.appendleft(tmp1367)
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.1.1.2.0_1', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 139367
                if len(subjects1361) >= 1:
                    tmp1370 = subjects1361.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.1.1.2.0', tmp1370)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 139368
                        if len(subjects1361) == 0:
                            pass
                            # State 139369
                            if len(subjects) == 0:
                                pass
                                # 158: acosh(x*c)
                    subjects1361.appendleft(tmp1370)
            if len(subjects1361) >= 1:
                tmp1372 = subjects1361.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.1.1.1', tmp1372)
                except ValueError:
                    pass
                else:
                    pass
                    # State 142159
                    if len(subjects1361) == 0:
                        pass
                        # State 142160
                        if len(subjects) == 0:
                            pass
                            # 161: acosh(u)
                subjects1361.appendleft(tmp1372)
            if len(subjects1361) >= 1 and isinstance(subjects1361[0], Mul):
                tmp1374 = subjects1361.popleft()
                associative1 = tmp1374
                associative_type1 = type(tmp1374)
                subjects1375 = deque(tmp1374._args)
                matcher = CommutativeMatcher138469.get()
                tmp1376 = subjects1375
                subjects1375 = []
                for s in tmp1376:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp1376, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 138470
                        if len(subjects1361) == 0:
                            pass
                            # State 138471
                            if len(subjects) == 0:
                                pass
                                # 153: acosh(c*x)
                    if pattern_index == 1:
                        pass
                        # State 138963
                        if len(subjects1361) == 0:
                            pass
                            # State 138964
                            if len(subjects) == 0:
                                pass
                                # 155: acosh(c*x)
                    if pattern_index == 2:
                        pass
                        # State 138996
                        if len(subjects1361) == 0:
                            pass
                            # State 138997
                            if len(subjects) == 0:
                                pass
                                # 156: acosh(c*x)
                    if pattern_index == 3:
                        pass
                        # State 139370
                        if len(subjects1361) == 0:
                            pass
                            # State 139371
                            if len(subjects) == 0:
                                pass
                                # 158: acosh(x*c)
                subjects1361.appendleft(tmp1374)
            subjects.appendleft(tmp1360)
        if len(subjects) >= 1 and isinstance(subjects[0], atanh):
            tmp1377 = subjects.popleft()
            subjects1378 = deque(tmp1377._args)
            # State 142639
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.1.1.2.0', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 142640
                if len(subjects1378) >= 1:
                    tmp1380 = subjects1378.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.0', tmp1380)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 142641
                        if len(subjects1378) == 0:
                            pass
                            # State 142642
                            if len(subjects) == 0:
                                pass
                                # 162: atanh(c*x)
                    subjects1378.appendleft(tmp1380)
                if len(subjects1378) >= 1:
                    tmp1382 = subjects1378.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.1', tmp1382)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 142798
                        if len(subjects1378) == 0:
                            pass
                            # State 142799
                            if len(subjects) == 0:
                                pass
                                # 164: atanh(c*x)
                    subjects1378.appendleft(tmp1382)
                if len(subjects1378) >= 1:
                    tmp1384 = subjects1378.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.1', tmp1384)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 143563
                        if len(subjects1378) == 0:
                            pass
                            # State 143564
                            if len(subjects) == 0:
                                pass
                                # 168: atanh(c*x)
                    subjects1378.appendleft(tmp1384)
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.1.1.2.0_1', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 143514
                if len(subjects1378) >= 1:
                    tmp1387 = subjects1378.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.1.1.2.0', tmp1387)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 143515
                        if len(subjects1378) == 0:
                            pass
                            # State 143516
                            if len(subjects) == 0:
                                pass
                                # 166: atanh(x*c)
                    subjects1378.appendleft(tmp1387)
            if len(subjects1378) >= 1:
                tmp1389 = subjects1378.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.1.1.1', tmp1389)
                except ValueError:
                    pass
                else:
                    pass
                    # State 148652
                    if len(subjects1378) == 0:
                        pass
                        # State 148653
                        if len(subjects) == 0:
                            pass
                            # 170: atanh(u)
                subjects1378.appendleft(tmp1389)
            if len(subjects1378) >= 1 and isinstance(subjects1378[0], Mul):
                tmp1391 = subjects1378.popleft()
                associative1 = tmp1391
                associative_type1 = type(tmp1391)
                subjects1392 = deque(tmp1391._args)
                matcher = CommutativeMatcher142644.get()
                tmp1393 = subjects1392
                subjects1392 = []
                for s in tmp1393:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp1393, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 142645
                        if len(subjects1378) == 0:
                            pass
                            # State 142646
                            if len(subjects) == 0:
                                pass
                                # 162: atanh(c*x)
                    if pattern_index == 1:
                        pass
                        # State 142800
                        if len(subjects1378) == 0:
                            pass
                            # State 142801
                            if len(subjects) == 0:
                                pass
                                # 164: atanh(c*x)
                    if pattern_index == 2:
                        pass
                        # State 143517
                        if len(subjects1378) == 0:
                            pass
                            # State 143518
                            if len(subjects) == 0:
                                pass
                                # 166: atanh(x*c)
                    if pattern_index == 3:
                        pass
                        # State 143565
                        if len(subjects1378) == 0:
                            pass
                            # State 143566
                            if len(subjects) == 0:
                                pass
                                # 168: atanh(c*x)
                subjects1378.appendleft(tmp1391)
            subjects.appendleft(tmp1377)
        if len(subjects) >= 1 and isinstance(subjects[0], acoth):
            tmp1394 = subjects.popleft()
            subjects1395 = deque(tmp1394._args)
            # State 142660
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.1.1.2.0', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 142661
                if len(subjects1395) >= 1:
                    tmp1397 = subjects1395.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.0', tmp1397)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 142662
                        if len(subjects1395) == 0:
                            pass
                            # State 142663
                            if len(subjects) == 0:
                                pass
                                # 163: acoth(c*x)
                    subjects1395.appendleft(tmp1397)
                if len(subjects1395) >= 1:
                    tmp1399 = subjects1395.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.1', tmp1399)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 142820
                        if len(subjects1395) == 0:
                            pass
                            # State 142821
                            if len(subjects) == 0:
                                pass
                                # 165: acoth(c*x)
                    subjects1395.appendleft(tmp1399)
                if len(subjects1395) >= 1:
                    tmp1401 = subjects1395.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.1', tmp1401)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 143585
                        if len(subjects1395) == 0:
                            pass
                            # State 143586
                            if len(subjects) == 0:
                                pass
                                # 169: acoth(c*x)
                    subjects1395.appendleft(tmp1401)
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.1.1.2.0_1', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 143540
                if len(subjects1395) >= 1:
                    tmp1404 = subjects1395.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.1.1.2.0', tmp1404)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 143541
                        if len(subjects1395) == 0:
                            pass
                            # State 143542
                            if len(subjects) == 0:
                                pass
                                # 167: acoth(x*c)
                    subjects1395.appendleft(tmp1404)
            if len(subjects1395) >= 1:
                tmp1406 = subjects1395.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.1.1.1', tmp1406)
                except ValueError:
                    pass
                else:
                    pass
                    # State 148666
                    if len(subjects1395) == 0:
                        pass
                        # State 148667
                        if len(subjects) == 0:
                            pass
                            # 171: acoth(u)
                subjects1395.appendleft(tmp1406)
            if len(subjects1395) >= 1 and isinstance(subjects1395[0], Mul):
                tmp1408 = subjects1395.popleft()
                associative1 = tmp1408
                associative_type1 = type(tmp1408)
                subjects1409 = deque(tmp1408._args)
                matcher = CommutativeMatcher142665.get()
                tmp1410 = subjects1409
                subjects1409 = []
                for s in tmp1410:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp1410, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 142666
                        if len(subjects1395) == 0:
                            pass
                            # State 142667
                            if len(subjects) == 0:
                                pass
                                # 163: acoth(c*x)
                    if pattern_index == 1:
                        pass
                        # State 142822
                        if len(subjects1395) == 0:
                            pass
                            # State 142823
                            if len(subjects) == 0:
                                pass
                                # 165: acoth(c*x)
                    if pattern_index == 2:
                        pass
                        # State 143543
                        if len(subjects1395) == 0:
                            pass
                            # State 143544
                            if len(subjects) == 0:
                                pass
                                # 167: acoth(x*c)
                    if pattern_index == 3:
                        pass
                        # State 143587
                        if len(subjects1395) == 0:
                            pass
                            # State 143588
                            if len(subjects) == 0:
                                pass
                                # 169: acoth(c*x)
                subjects1395.appendleft(tmp1408)
            subjects.appendleft(tmp1394)
        if len(subjects) >= 1 and isinstance(subjects[0], asech):
            tmp1411 = subjects.popleft()
            subjects1412 = deque(tmp1411._args)
            # State 148830
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.1.1.2.0', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 148831
                if len(subjects1412) >= 1:
                    tmp1414 = subjects1412.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.1', tmp1414)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 148832
                        if len(subjects1412) == 0:
                            pass
                            # State 148833
                            if len(subjects) == 0:
                                pass
                                # 172: asech(c*x)
                    subjects1412.appendleft(tmp1414)
                if len(subjects1412) >= 1:
                    tmp1416 = subjects1412.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.1', tmp1416)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 149084
                        if len(subjects1412) == 0:
                            pass
                            # State 149085
                            if len(subjects) == 0:
                                pass
                                # 174: asech(c*x)
                    subjects1412.appendleft(tmp1416)
            if len(subjects1412) >= 1:
                tmp1418 = subjects1412.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.1.1.1', tmp1418)
                except ValueError:
                    pass
                else:
                    pass
                    # State 150502
                    if len(subjects1412) == 0:
                        pass
                        # State 150503
                        if len(subjects) == 0:
                            pass
                            # 176: asech(u)
                subjects1412.appendleft(tmp1418)
            if len(subjects1412) >= 1 and isinstance(subjects1412[0], Mul):
                tmp1420 = subjects1412.popleft()
                associative1 = tmp1420
                associative_type1 = type(tmp1420)
                subjects1421 = deque(tmp1420._args)
                matcher = CommutativeMatcher148835.get()
                tmp1422 = subjects1421
                subjects1421 = []
                for s in tmp1422:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp1422, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 148836
                        if len(subjects1412) == 0:
                            pass
                            # State 148837
                            if len(subjects) == 0:
                                pass
                                # 172: asech(c*x)
                    if pattern_index == 1:
                        pass
                        # State 149086
                        if len(subjects1412) == 0:
                            pass
                            # State 149087
                            if len(subjects) == 0:
                                pass
                                # 174: asech(c*x)
                subjects1412.appendleft(tmp1420)
            subjects.appendleft(tmp1411)
        if len(subjects) >= 1 and isinstance(subjects[0], acsch):
            tmp1423 = subjects.popleft()
            subjects1424 = deque(tmp1423._args)
            # State 148868
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.1.1.2.0', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 148869
                if len(subjects1424) >= 1:
                    tmp1426 = subjects1424.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.1', tmp1426)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 148870
                        if len(subjects1424) == 0:
                            pass
                            # State 148871
                            if len(subjects) == 0:
                                pass
                                # 173: acsch(c*x)
                    subjects1424.appendleft(tmp1426)
                if len(subjects1424) >= 1:
                    tmp1428 = subjects1424.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.1', tmp1428)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 149106
                        if len(subjects1424) == 0:
                            pass
                            # State 149107
                            if len(subjects) == 0:
                                pass
                                # 175: acsch(c*x)
                    subjects1424.appendleft(tmp1428)
            if len(subjects1424) >= 1:
                tmp1430 = subjects1424.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.1.1.1', tmp1430)
                except ValueError:
                    pass
                else:
                    pass
                    # State 150516
                    if len(subjects1424) == 0:
                        pass
                        # State 150517
                        if len(subjects) == 0:
                            pass
                            # 177: acsch(u)
                subjects1424.appendleft(tmp1430)
            if len(subjects1424) >= 1 and isinstance(subjects1424[0], Mul):
                tmp1432 = subjects1424.popleft()
                associative1 = tmp1432
                associative_type1 = type(tmp1432)
                subjects1433 = deque(tmp1432._args)
                matcher = CommutativeMatcher148873.get()
                tmp1434 = subjects1433
                subjects1433 = []
                for s in tmp1434:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp1434, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 148874
                        if len(subjects1424) == 0:
                            pass
                            # State 148875
                            if len(subjects) == 0:
                                pass
                                # 173: acsch(c*x)
                    if pattern_index == 1:
                        pass
                        # State 149108
                        if len(subjects1424) == 0:
                            pass
                            # State 149109
                            if len(subjects) == 0:
                                pass
                                # 175: acsch(c*x)
                subjects1424.appendleft(tmp1432)
            subjects.appendleft(tmp1423)
        return
        yield


from matchpy.utils import VariableWithCount
from matchpy.matching.many_to_one import CommutativeMatcher
from multiset import Multiset
from collections import deque
