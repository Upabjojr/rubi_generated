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

class CommutativeMatcher2613(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({0: 1}), [
      (VariableWithCount('i2.2.0_1', 1, 1, None), Add)
]),
    1: (1, Multiset({1: 1}), [
      (VariableWithCount('i2.2.0_1', 1, 1, None), Add)
]),
    2: (2, Multiset({0: 1}), [
      (VariableWithCount('i2.2.0_1', 1, 1, S(0)), Add)
]),
    3: (3, Multiset({2: 1}), [
      (VariableWithCount('i2.2.0_2', 1, 1, None), Add)
]),
    4: (4, Multiset({3: 1}), [
      (VariableWithCount('i2.2.0_2', 1, 1, S(0)), Add)
]),
    5: (5, Multiset({2: 1}), [
      (VariableWithCount('i2.2.0_2', 1, 1, S(0)), Add)
]),
    6: (6, Multiset({4: 1, 3: 1}), [
      (VariableWithCount('i2.2.0_1', 1, 1, S(0)), Add)
]),
    7: (7, Multiset({5: 1}), [
      (VariableWithCount('i2.2.0_1', 1, 1, None), Add)
]),
    8: (8, Multiset({4: 1, 3: 1}), [
      (VariableWithCount('i2.2.0_1', 1, 1, None), Add)
]),
    9: (9, Multiset({5: 1}), [
      (VariableWithCount('i2.2.0_1', 1, 1, S(0)), Add)
]),
    10: (10, Multiset({6: 1}), [
      (VariableWithCount('i2.2.0_2', 1, 1, S(0)), Add)
]),
    11: (11, Multiset({7: 1}), [
      (VariableWithCount('i2.2.0_2', 1, 1, None), Add)
]),
    12: (12, Multiset({8: 1, 9: 1}), [
      (VariableWithCount('i2.2.0_1', 1, 1, None), Add)
]),
    13: (13, Multiset({8: 1, 9: 1}), [
      (VariableWithCount('i2.2.0_1', 1, 1, S(0)), Add)
]),
    14: (14, Multiset({10: 1, 6: 1}), [
      (VariableWithCount('i2.2.0_1', 1, 1, S(0)), Add)
]),
    15: (15, Multiset({8: 1, 9: 1}), [
      (VariableWithCount('i2.2.0_2', 1, 1, S(0)), Add)
]),
    16: (16, Multiset({8: 1, 9: 1}), [
      (VariableWithCount('i2.2.0_2', 1, 1, None), Add)
]),
    17: (17, Multiset({10: 1}), [
      (VariableWithCount('i2.2.0_1', 1, 1, S(0)), Add)
]),
    18: (18, Multiset({6: 1}), [
      (VariableWithCount('i2.2.0_2', 1, 1, None), Add)
]),
    19: (19, Multiset({8: 1, 9: 1}), [
      (VariableWithCount('i2.2.0', 1, 1, S(0)), Add)
]),
    20: (20, Multiset({10: 1, 6: 1}), [
      
]),
    21: (21, Multiset({10: 1, 6: 1}), [
      (VariableWithCount('i2.2.0_1', 1, 1, None), Add)
]),
    22: (22, Multiset({11: 1}), [
      (VariableWithCount('i2.2.0_2', 1, 1, None), Add)
]),
    23: (23, Multiset({12: 1}), [
      (VariableWithCount('i2.2.0_1', 1, 1, None), Add)
]),
    24: (24, Multiset({12: 1}), [
      (VariableWithCount('i2.2.0_1', 1, 1, S(0)), Add)
]),
    25: (25, Multiset({13: 1}), [
      (VariableWithCount('i2.2.0_2', 1, 1, None), Add)
]),
    26: (26, Multiset({14: 1}), [
      (VariableWithCount('i2.2.0_2', 1, 1, None), Add)
]),
    27: (27, Multiset({15: 1}), [
      (VariableWithCount('i2.2.0_3', 1, 1, None), Add)
]),
    28: (28, Multiset({16: 1}), [
      (VariableWithCount('i2.2.0_2', 1, 1, None), Add)
]),
    29: (29, Multiset({17: 1}), [
      (VariableWithCount('i2.2.0_2', 1, 1, None), Add)
]),
    30: (30, Multiset({17: 1, 18: 1}), [
      (VariableWithCount('i2.2.0_2', 1, 1, None), Add)
]),
    31: (31, Multiset({19: 1}), [
      (VariableWithCount('i2.2.0_1', 1, 1, S(0)), Add)
]),
    32: (32, Multiset({1: 1}), [
      (VariableWithCount('i2.2.0_1', 1, 1, S(0)), Add)
]),
    33: (33, Multiset({11: 1, 20: 1}), [
      (VariableWithCount('i2.2.0_2', 1, 1, None), Add)
]),
    34: (34, Multiset({13: 1, 21: 1}), [
      (VariableWithCount('i2.2.0_2', 1, 1, None), Add)
]),
    35: (35, Multiset({12: 1, 17: 1}), [
      (VariableWithCount('i2.2.0_1', 1, 1, None), Add)
]),
    36: (36, Multiset({12: 1, 17: 1}), [
      (VariableWithCount('i2.2.0_1', 1, 1, S(0)), Add)
]),
    37: (37, Multiset({22: 1}), [
      (VariableWithCount('i2.2.0', 1, 1, None), Add)
]),
    38: (38, Multiset({12: 1, 23: 1}), [
      (VariableWithCount('i2.2.0_1', 1, 1, None), Add)
]),
    39: (39, Multiset({24: 1}), [
      (VariableWithCount('i2.2.0_1', 1, 1, None), Add)
]),
    40: (40, Multiset({1: 1, 25: 1}), [
      (VariableWithCount('i2.2.0_1', 1, 1, S(0)), Add)
]),
    41: (41, Multiset({24: 1, 26: 1}), [
      (VariableWithCount('i2.2.0_1', 1, 1, None), Add)
]),
    42: (42, Multiset({23: 1, 27: 1}), [
      (VariableWithCount('i2.2.0_2', 1, 1, S(0)), Add)
]),
    43: (43, Multiset({11: 1, 28: 1}), [
      (VariableWithCount('i2.2.0_2', 1, 1, None), Add)
]),
    44: (44, Multiset({29: 1, 30: 1}), [
      (VariableWithCount('i2.2.0_3', 1, 1, S(0)), Add)
]),
    45: (45, Multiset({20: 1}), [
      (VariableWithCount('i2.2.0_3', 1, 1, None), Add)
]),
    46: (46, Multiset({31: 1}), [
      (VariableWithCount('i2.2.0_2', 1, 1, S(0)), Add)
]),
    47: (47, Multiset({31: 1, 32: 1}), [
      (VariableWithCount('i2.2.0_2', 1, 1, None), Add)
]),
    48: (48, Multiset({31: 1, 20: 1}), [
      (VariableWithCount('i2.2.0_2', 1, 1, None), Add)
]),
    49: (49, Multiset({20: 1, 14: 1}), [
      (VariableWithCount('i2.2.0_2', 1, 1, None), Add)
]),
    50: (50, Multiset({33: 1}), [
      (VariableWithCount('i2.2.0', 1, 1, None), Add)
]),
    51: (51, Multiset({25: 1}), [
      (VariableWithCount('i2.2.0', 1, 1, None), Add)
]),
    52: (52, Multiset({34: 1}), [
      (VariableWithCount('i2.2.0_1', 1, 1, S(0)), Add)
]),
    53: (53, Multiset({35: 1}), [
      (VariableWithCount('i2.2.0', 1, 1, S(0)), Add)
]),
    54: (54, Multiset({36: 1}), [
      (VariableWithCount('i2.2.0', 1, 1, None), Add)
]),
    55: (55, Multiset({36: 1, 37: 1}), [
      (VariableWithCount('i2.2.0_1', 1, 1, S(0)), Add)
]),
    56: (56, Multiset({38: 1, 6: 1}), [
      (VariableWithCount('i2.2.0_1', 1, 1, S(0)), Add)
]),
    57: (57, Multiset({39: 1}), [
      (VariableWithCount('i2.2.0_1', 1, 1, S(0)), Add)
]),
    58: (58, Multiset({40: 1}), [
      (VariableWithCount('i2.2.0_1', 1, 1, S(0)), Add)
]),
    59: (59, Multiset({41: 1}), [
      (VariableWithCount('i2.2.0_1', 1, 1, S(0)), Add)
]),
    60: (60, Multiset({42: 1}), [
      (VariableWithCount('i2.2.0', 1, 1, S(0)), Add)
]),
    61: (61, Multiset({43: 1}), [
      (VariableWithCount('i2.2.0_1', 1, 1, S(0)), Add)
]),
    62: (62, Multiset({44: 1}), [
      (VariableWithCount('i2.2.0_1', 1, 1, S(0)), Add)
]),
    63: (63, Multiset({45: 1}), [
      (VariableWithCount('i2.2.0_2', 1, 1, S(0)), Add)
]),
    64: (64, Multiset({46: 1}), [
      (VariableWithCount('i2.2.0_2', 1, 1, S(0)), Add)
]),
    65: (65, Multiset({47: 1}), [
      (VariableWithCount('i2.2.0_1', 1, 1, S(0)), Add)
]),
    66: (66, Multiset({48: 1}), [
      (VariableWithCount('i2.2.0_1', 1, 1, None), Add)
]),
    67: (67, Multiset({49: 1}), [
      (VariableWithCount('i2.2.0_1', 1, 1, None), Add)
]),
    68: (68, Multiset({50: 1}), [
      (VariableWithCount('i2.2.0_1', 1, 1, None), Add)
]),
    69: (69, Multiset({51: 1}), [
      (VariableWithCount('i2.2.0_1', 1, 1, None), Add)
]),
    70: (70, Multiset({52: 1}), [
      (VariableWithCount('i2.2.0_1', 1, 1, None), Add)
]),
    71: (71, Multiset({53: 1}), [
      (VariableWithCount('i2.2.0_1', 1, 1, None), Add)
]),
    72: (72, Multiset({52: 1}), [
      (VariableWithCount('i2.2.0_1', 1, 1, S(0)), Add)
]),
    73: (73, Multiset({53: 1}), [
      (VariableWithCount('i2.2.0_1', 1, 1, S(0)), Add)
]),
    74: (74, Multiset({54: 1}), [
      (VariableWithCount('i2.2.0_1', 1, 1, S(0)), Add)
]),
    75: (75, Multiset({55: 1}), [
      (VariableWithCount('i2.2.0_1', 1, 1, S(0)), Add)
]),
    76: (76, Multiset({56: 1}), [
      (VariableWithCount('i2.2.0_1', 1, 1, None), Add)
]),
    77: (77, Multiset({57: 1}), [
      (VariableWithCount('i2.2.0_1', 1, 1, None), Add)
]),
    78: (78, Multiset({50: 1}), [
      (VariableWithCount('i2.2.0_1', 1, 1, S(0)), Add)
]),
    79: (79, Multiset({51: 1}), [
      (VariableWithCount('i2.2.0_1', 1, 1, S(0)), Add)
]),
    80: (80, Multiset({58: 1}), [
      (VariableWithCount('i2.2.0_1', 1, 1, S(0)), Add)
]),
    81: (81, Multiset({59: 1}), [
      (VariableWithCount('i2.2.0_1', 1, 1, S(0)), Add)
]),
    82: (82, Multiset({58: 1}), [
      (VariableWithCount('i2.2.0_1', 1, 1, None), Add)
]),
    83: (83, Multiset({59: 1}), [
      (VariableWithCount('i2.2.0_1', 1, 1, None), Add)
]),
    84: (84, Multiset({60: 1}), [
      (VariableWithCount('i2.2.0_1', 1, 1, None), Add)
]),
    85: (85, Multiset({61: 1}), [
      (VariableWithCount('i2.2.0_1', 1, 1, None), Add)
]),
    86: (86, Multiset({62: 1}), [
      (VariableWithCount('i2.2.0_1', 1, 1, S(0)), Add)
]),
    87: (87, Multiset({63: 1}), [
      (VariableWithCount('i2.2.0_1', 1, 1, None), Add)
]),
    88: (88, Multiset({64: 1}), [
      (VariableWithCount('i2.2.0_1', 1, 1, S(0)), Add)
]),
    89: (89, Multiset({63: 1}), [
      (VariableWithCount('i2.2.0_1', 1, 1, S(0)), Add)
]),
    90: (90, Multiset({65: 1}), [
      (VariableWithCount('i2.2.0_2', 1, 1, S(0)), Add)
]),
    91: (91, Multiset({66: 1}), [
      (VariableWithCount('i2.2.0_2', 1, 1, S(0)), Add)
]),
    92: (92, Multiset({67: 1}), [
      (VariableWithCount('i2.2.0_2', 1, 1, S(0)), Add)
]),
    93: (93, Multiset({68: 1}), [
      (VariableWithCount('i2.2.0_2', 1, 1, S(0)), Add)
]),
    94: (94, Multiset({69: 1}), [
      (VariableWithCount('i2.2.0_2', 1, 1, S(0)), Add)
]),
    95: (95, Multiset({70: 1}), [
      (VariableWithCount('i2.2.0_2', 1, 1, S(0)), Add)
]),
    96: (96, Multiset({71: 1}), [
      (VariableWithCount('i2.2.0_2', 1, 1, S(0)), Add)
]),
    97: (97, Multiset({72: 1}), [
      (VariableWithCount('i2.2.0_2', 1, 1, S(0)), Add)
]),
    98: (98, Multiset({73: 1}), [
      (VariableWithCount('i2.2.0_1', 1, 1, None), Add)
]),
    99: (99, Multiset({74: 1}), [
      (VariableWithCount('i2.2.0_1', 1, 1, None), Add)
]),
    100: (100, Multiset({75: 1}), [
      (VariableWithCount('i2.2.0_1', 1, 1, None), Add)
]),
    101: (101, Multiset({76: 1}), [
      (VariableWithCount('i2.2.0_1', 1, 1, None), Add)
]),
    102: (102, Multiset({73: 1}), [
      (VariableWithCount('i2.2.0_1', 1, 1, S(0)), Add)
]),
    103: (103, Multiset({74: 1}), [
      (VariableWithCount('i2.2.0_1', 1, 1, S(0)), Add)
]),
    104: (104, Multiset({77: 1}), [
      (VariableWithCount('i2.2.0_1', 1, 1, None), Add)
]),
    105: (105, Multiset({78: 1}), [
      (VariableWithCount('i2.2.0_1', 1, 1, None), Add)
]),
    106: (106, Multiset({76: 1}), [
      (VariableWithCount('i2.2.0_1', 1, 1, S(0)), Add)
]),
    107: (107, Multiset({79: 1}), [
      (VariableWithCount('i2.2.0_1', 1, 1, S(0)), Add)
]),
    108: (108, Multiset({80: 1}), [
      (VariableWithCount('i2.2.0_1', 1, 1, S(0)), Add)
]),
    109: (109, Multiset({81: 1}), [
      (VariableWithCount('i2.2.0_1', 1, 1, S(0)), Add)
]),
    110: (110, Multiset({82: 1}), [
      (VariableWithCount('i2.2.0_1', 1, 1, None), Add)
]),
    111: (111, Multiset({77: 1}), [
      (VariableWithCount('i2.2.0_1', 1, 1, S(0)), Add)
]),
    112: (112, Multiset({78: 1}), [
      (VariableWithCount('i2.2.0_1', 1, 1, S(0)), Add)
]),
    113: (113, Multiset({83: 1}), [
      (VariableWithCount('i2.2.0_1', 1, 1, S(0)), Add)
]),
    114: (114, Multiset({84: 1}), [
      (VariableWithCount('i2.2.0_1', 1, 1, None), Add)
]),
    115: (115, Multiset({85: 1}), [
      (VariableWithCount('i2.2.0_1', 1, 1, S(0)), Add)
]),
    116: (116, Multiset({84: 1}), [
      (VariableWithCount('i2.2.0_1', 1, 1, S(0)), Add)
]),
    117: (117, Multiset({86: 1}), [
      (VariableWithCount('i2.2.0_2', 1, 1, S(0)), Add)
]),
    118: (118, Multiset({87: 1}), [
      (VariableWithCount('i2.2.0_2', 1, 1, S(0)), Add)
]),
    119: (119, Multiset({88: 1}), [
      (VariableWithCount('i2.2.0_2', 1, 1, S(0)), Add)
]),
    120: (120, Multiset({89: 1}), [
      (VariableWithCount('i2.2.0_2', 1, 1, S(0)), Add)
]),
    121: (121, Multiset({60: 1}), [
      (VariableWithCount('i2.2.0_1', 1, 1, S(0)), Add)
]),
    122: (122, Multiset({90: 1}), [
      (VariableWithCount('i2.2.0_1', 1, 1, None), Add)
]),
    123: (123, Multiset({91: 1}), [
      (VariableWithCount('i2.2.0_1', 1, 1, None), Add)
]),
    124: (124, Multiset({92: 1}), [
      (VariableWithCount('i2.2.0_1', 1, 1, None), Add)
]),
    125: (125, Multiset({93: 1}), [
      (VariableWithCount('i2.2.0_1', 1, 1, S(0)), Add)
]),
    126: (126, Multiset({94: 1}), [
      (VariableWithCount('i2.2.0_1', 1, 1, S(0)), Add)
]),
    127: (127, Multiset({93: 1}), [
      (VariableWithCount('i2.2.0_1', 1, 1, None), Add)
]),
    128: (128, Multiset({94: 1}), [
      (VariableWithCount('i2.2.0_1', 1, 1, None), Add)
]),
    129: (129, Multiset({95: 1}), [
      (VariableWithCount('i2.2.0_2', 1, 1, S(0)), Add)
]),
    130: (130, Multiset({96: 1}), [
      (VariableWithCount('i2.2.0_2', 1, 1, S(0)), Add)
]),
    131: (131, Multiset({97: 1}), [
      (VariableWithCount('i2.2.0_2', 1, 1, S(0)), Add)
]),
    132: (132, Multiset({98: 1}), [
      (VariableWithCount('i2.2.0_2', 1, 1, S(0)), Add)
]),
    133: (133, Multiset({99: 1}), [
      (VariableWithCount('i2.2.0_1', 1, 1, None), Add)
]),
    134: (134, Multiset({100: 1}), [
      (VariableWithCount('i2.2.0_2', 1, 1, S(0)), Add)
]),
    135: (135, Multiset({101: 1}), [
      (VariableWithCount('i2.2.0_2', 1, 1, S(0)), Add)
]),
    136: (136, Multiset({102: 1}), [
      (VariableWithCount('i2.2.0_1', 1, 1, S(0)), Add)
]),
    137: (137, Multiset({103: 1}), [
      (VariableWithCount('i2.2.0_1', 1, 1, S(0)), Add)
]),
    138: (138, Multiset({104: 1}), [
      (VariableWithCount('i2.2.0_3', 1, 1, S(0)), Add)
]),
    139: (139, Multiset({105: 1}), [
      (VariableWithCount('i2.2.0_3', 1, 1, S(0)), Add)
]),
    140: (140, Multiset({106: 1}), [
      (VariableWithCount('i2.2.0_1', 1, 1, None), Add)
]),
    141: (141, Multiset({106: 1}), [
      (VariableWithCount('i2.2.0_1', 1, 1, S(0)), Add)
]),
    142: (142, Multiset({107: 1, 108: 1}), [
      (VariableWithCount('i2.2.0_2', 1, 1, S(0)), Add)
]),
    143: (143, Multiset({109: 1}), [
      (VariableWithCount('i2.2.0_2', 1, 1, None), Add)
]),
    144: (144, Multiset({110: 1}), [
      (VariableWithCount('i2.2.0_1', 1, 1, S(0)), Add)
]),
    145: (145, Multiset({111: 1}), [
      (VariableWithCount('i2.2.0_1', 1, 1, S(0)), Add)
]),
    146: (146, Multiset({102: 1}), [
      (VariableWithCount('i2.2.0_1', 1, 1, None), Add)
]),
    147: (147, Multiset({103: 1}), [
      (VariableWithCount('i2.2.0_1', 1, 1, None), Add)
]),
    148: (148, Multiset({112: 1, 113: 1}), [
      (VariableWithCount('i2.2.0_1', 1, 1, S(0)), Add)
]),
    149: (149, Multiset({114: 1}), [
      (VariableWithCount('i2.2.0_1', 1, 1, S(0)), Add)
]),
    150: (150, Multiset({115: 1}), [
      (VariableWithCount('i2.2.0_1', 1, 1, S(0)), Add)
]),
    151: (151, Multiset({116: 1}), [
      (VariableWithCount('i2.2.0_1', 1, 1, S(0)), Add)
]),
    152: (152, Multiset({117: 1}), [
      (VariableWithCount('i2.2.0_1', 1, 1, S(0)), Add)
]),
    153: (153, Multiset({118: 1}), [
      (VariableWithCount('i2.2.0_1', 1, 1, None), Add)
]),
    154: (154, Multiset({118: 1}), [
      (VariableWithCount('i2.2.0_1', 1, 1, S(0)), Add)
]),
    155: (155, Multiset({119: 1}), [
      (VariableWithCount('i2.2.0_2', 1, 1, S(0)), Add)
]),
    156: (156, Multiset({120: 1}), [
      (VariableWithCount('i2.2.0_2', 1, 1, S(0)), Add)
]),
    157: (157, Multiset({121: 1}), [
      (VariableWithCount('i2.2.0_2', 1, 1, S(0)), Add)
]),
    158: (158, Multiset({122: 1}), [
      (VariableWithCount('i2.2.0_2', 1, 1, S(0)), Add)
]),
    159: (159, Multiset({123: 1}), [
      (VariableWithCount('i2.2.0_2', 1, 1, S(0)), Add)
]),
    160: (160, Multiset({124: 1}), [
      (VariableWithCount('i2.2.0_2', 1, 1, S(0)), Add)
]),
    161: (161, Multiset({125: 1}), [
      (VariableWithCount('i2.2.0_2', 1, 1, S(0)), Add)
]),
    162: (162, Multiset({126: 1}), [
      (VariableWithCount('i2.2.0_2', 1, 1, S(0)), Add)
]),
    163: (163, Multiset({127: 1}), [
      (VariableWithCount('i2.2.0_1', 1, 1, None), Add)
]),
    164: (164, Multiset({127: 1}), [
      (VariableWithCount('i2.2.0_1', 1, 1, S(0)), Add)
]),
    165: (165, Multiset({128: 1}), [
      (VariableWithCount('i2.2.0_2', 1, 1, S(0)), Add)
]),
    166: (166, Multiset({129: 1}), [
      (VariableWithCount('i2.2.0_2', 1, 1, S(0)), Add)
]),
    167: (167, Multiset({130: 1}), [
      (VariableWithCount('i2.2.0_2', 1, 1, S(0)), Add)
]),
    168: (168, Multiset({131: 1}), [
      (VariableWithCount('i2.2.0_2', 1, 1, S(0)), Add)
]),
    169: (169, Multiset({132: 1}), [
      (VariableWithCount('i2.2.0_2', 1, 1, S(0)), Add)
]),
    170: (170, Multiset({133: 1}), [
      (VariableWithCount('i2.2.0_2', 1, 1, S(0)), Add)
]),
    171: (171, Multiset({134: 1}), [
      (VariableWithCount('i2.2.0_2', 1, 1, S(0)), Add)
]),
    172: (172, Multiset({135: 1}), [
      (VariableWithCount('i2.2.0_2', 1, 1, S(0)), Add)
]),
    173: (173, Multiset({136: 1}), [
      (VariableWithCount('i2.2.0_1', 1, 1, None), Add)
]),
    174: (174, Multiset({137: 1}), [
      (VariableWithCount('i2.2.0_2', 1, 1, S(0)), Add)
]),
    175: (175, Multiset({138: 1}), [
      (VariableWithCount('i2.2.0_2', 1, 1, S(0)), Add)
]),
    176: (176, Multiset({139: 1}), [
      (VariableWithCount('i2.2.0_1', 1, 1, S(0)), Add)
]),
    177: (177, Multiset({140: 1}), [
      (VariableWithCount('i2.2.0_1', 1, 1, S(0)), Add)
]),
    178: (178, Multiset({141: 1}), [
      (VariableWithCount('i2.2.0_3', 1, 1, S(0)), Add)
]),
    179: (179, Multiset({3: 1}), [
      (VariableWithCount('i2.2.0_2', 1, 1, None), Add)
]),
    180: (180, Multiset({108: 1}), [
      (VariableWithCount('i2.2.0_3', 1, 1, None), Add)
]),
    181: (181, Multiset({142: 1}), [
      (VariableWithCount('i2.2.0_1', 1, 1, S(0)), Add)
]),
    182: (182, Multiset({143: 1}), [
      (VariableWithCount('i2.2.0_1', 1, 1, None), Add)
]),
    183: (183, Multiset({140: 1}), [
      (VariableWithCount('i2.2.0_1', 1, 1, None), Add)
]),
    184: (184, Multiset({144: 1}), [
      (VariableWithCount('i2.2.0_1', 1, 1, S(0)), Add)
]),
    185: (185, Multiset({145: 1}), [
      (VariableWithCount('i2.2.0_1', 1, 1, S(0)), Add)
]),
    186: (186, Multiset({146: 1}), [
      (VariableWithCount('i2.2.0_1', 1, 1, S(0)), Add)
]),
    187: (187, Multiset({147: 1}), [
      (VariableWithCount('i2.2.0_1', 1, 1, S(0)), Add)
]),
    188: (188, Multiset({148: 1}), [
      (VariableWithCount('i2.2.0_1', 1, 1, S(0)), Add)
])
}
    subjects = {}
    subjects_by_id = {}
    bipartite = BipartiteGraph()
    associative = Add
    max_optional_count = 1
    anonymous_patterns = set()

    def __init__(self):
        self.add_subject(None)

    @staticmethod
    def get():
        if CommutativeMatcher2613._instance is None:
            CommutativeMatcher2613._instance = CommutativeMatcher2613()
        return CommutativeMatcher2613._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 2612
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.0_2', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 2614
            if len(subjects) >= 1:
                tmp2 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.0', tmp2)
                except ValueError:
                    pass
                else:
                    pass
                    # State 2615
                    if len(subjects) == 0:
                        pass
                        # 0: v*b
                subjects.appendleft(tmp2)
            if len(subjects) >= 1:
                tmp4 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.1', tmp4)
                except ValueError:
                    pass
                else:
                    pass
                    # State 4693
                    if len(subjects) == 0:
                        pass
                        # 6: e*x
                subjects.appendleft(tmp4)
            subst2 = Substitution(subst1)
            try:
                subst2.try_add_variable('i2.2.1.2_1', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 7552
                if len(subjects) >= 1:
                    tmp7 = subjects.popleft()
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.2.1.1', tmp7)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 7553
                        if len(subjects) == 0:
                            pass
                            # 17: b2*x**n
                    subjects.appendleft(tmp7)
                if len(subjects) >= 1:
                    tmp9 = subjects.popleft()
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.2.0', tmp9)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 9523
                        if len(subjects) == 0:
                            pass
                            # 30: x**n2*f1
                    subjects.appendleft(tmp9)
            subst2 = Substitution(subst1)
            try:
                subst2.try_add_variable('i2.2.1.2_2', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 9007
                if len(subjects) >= 1:
                    tmp12 = subjects.popleft()
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.2.1.1', tmp12)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 9008
                        if len(subjects) == 0:
                            pass
                            # 25: c*x**r
                    subjects.appendleft(tmp12)
            subst2 = Substitution(subst1)
            try:
                subst2.try_add_variable('i2.2.1.2', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 9042
                if len(subjects) >= 1:
                    tmp15 = subjects.popleft()
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.2.1.1', tmp15)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 9043
                        if len(subjects) == 0:
                            pass
                            # 26: c*x**n
                    subjects.appendleft(tmp15)
            if len(subjects) >= 1:
                tmp17 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.0_1', tmp17)
                except ValueError:
                    pass
                else:
                    pass
                    # State 13095
                    if len(subjects) == 0:
                        pass
                        # 34: x*h
                subjects.appendleft(tmp17)
            if len(subjects) >= 1:
                tmp19 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.1.1', tmp19)
                except ValueError:
                    pass
                else:
                    pass
                    # State 13882
                    if len(subjects) == 0:
                        pass
                        # 35: h*x
                subjects.appendleft(tmp19)
            if len(subjects) >= 1:
                tmp21 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.1.1.0', tmp21)
                except ValueError:
                    pass
                else:
                    pass
                    # State 26294
                    if len(subjects) == 0:
                        pass
                        # 45: j*x
                subjects.appendleft(tmp21)
            if len(subjects) >= 1:
                tmp23 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.2.2.1.0', tmp23)
                except ValueError:
                    pass
                else:
                    pass
                    # State 26313
                    if len(subjects) == 0:
                        pass
                        # 46: j*x
                subjects.appendleft(tmp23)
            if len(subjects) >= 1:
                tmp25 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.0', tmp25)
                except ValueError:
                    pass
                else:
                    pass
                    # State 109805
                    if len(subjects) == 0:
                        pass
                        # 109: g*x
                subjects.appendleft(tmp25)
            if len(subjects) >= 1:
                tmp27 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.1.0', tmp27)
                except ValueError:
                    pass
                else:
                    pass
                    # State 110627
                    if len(subjects) == 0:
                        pass
                        # 113: B*x
                subjects.appendleft(tmp27)
            if len(subjects) >= 1 and isinstance(subjects[0], Pow):
                tmp29 = subjects.popleft()
                subjects30 = deque(tmp29._args)
                # State 4058
                if len(subjects30) >= 1:
                    tmp31 = subjects30.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.0', tmp31)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 4059
                        if len(subjects30) >= 1 and subjects30[0] == 2:
                            tmp33 = subjects30.popleft()
                            # State 4060
                            if len(subjects30) == 0:
                                pass
                                # State 4061
                                if len(subjects) == 0:
                                    pass
                                    # 4: v**2*c
                            subjects30.appendleft(tmp33)
                    subjects30.appendleft(tmp31)
                if len(subjects30) >= 1:
                    tmp34 = subjects30.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.1', tmp34)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 5291
                        if len(subjects30) >= 1 and subjects30[0] == 2:
                            tmp36 = subjects30.popleft()
                            # State 5292
                            if len(subjects30) == 0:
                                pass
                                # State 5293
                                if len(subjects) == 0:
                                    pass
                                    # 8: f*x**2
                            subjects30.appendleft(tmp36)
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.2_1', 1)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 7554
                            if len(subjects30) == 0:
                                pass
                                # State 7555
                                if len(subjects) == 0:
                                    pass
                                    # 17: b2*x**n
                        if len(subjects30) >= 1:
                            tmp38 = subjects30.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.2_1', tmp38)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 7554
                                if len(subjects30) == 0:
                                    pass
                                    # State 7555
                                    if len(subjects) == 0:
                                        pass
                                        # 17: b2*x**n
                            subjects30.appendleft(tmp38)
                        if len(subjects30) >= 1:
                            tmp40 = subjects30.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.2', tmp40)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 8655
                                if len(subjects30) == 0:
                                    pass
                                    # State 8656
                                    if len(subjects) == 0:
                                        pass
                                        # 22: f*x**j
                            subjects30.appendleft(tmp40)
                        if len(subjects30) >= 1:
                            tmp42 = subjects30.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.2_1', tmp42)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 8671
                                if len(subjects30) == 0:
                                    pass
                                    # State 8672
                                    if len(subjects) == 0:
                                        pass
                                        # 23: c*x**n2
                            subjects30.appendleft(tmp42)
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.2_2', 1)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 9009
                            if len(subjects30) == 0:
                                pass
                                # State 9010
                                if len(subjects) == 0:
                                    pass
                                    # 25: c*x**r
                        if len(subjects30) >= 1:
                            tmp45 = subjects30.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.2_2', tmp45)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 9009
                                if len(subjects30) == 0:
                                    pass
                                    # State 9010
                                    if len(subjects) == 0:
                                        pass
                                        # 25: c*x**r
                            subjects30.appendleft(tmp45)
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.2', 1)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 9044
                            if len(subjects30) == 0:
                                pass
                                # State 9045
                                if len(subjects) == 0:
                                    pass
                                    # 26: c*x**n
                        if len(subjects30) >= 1:
                            tmp48 = subjects30.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.2', tmp48)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 9044
                                if len(subjects30) == 0:
                                    pass
                                    # State 9045
                                    if len(subjects) == 0:
                                        pass
                                        # 26: c*x**n
                            subjects30.appendleft(tmp48)
                        if len(subjects30) >= 1:
                            tmp50 = subjects30.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.2_2', tmp50)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 12201
                                if len(subjects30) == 0:
                                    pass
                                    # State 12202
                                    if len(subjects) == 0:
                                        pass
                                        # 33: d*x**n2
                            subjects30.appendleft(tmp50)
                    subjects30.appendleft(tmp34)
                if len(subjects30) >= 1:
                    tmp52 = subjects30.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.0', tmp52)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 9524
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.2_1', 1)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 9525
                            if len(subjects30) == 0:
                                pass
                                # State 9526
                                if len(subjects) == 0:
                                    pass
                                    # 30: x**n2*f1
                        if len(subjects30) >= 1:
                            tmp55 = subjects30.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.2_1', tmp55)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 9525
                                if len(subjects30) == 0:
                                    pass
                                    # State 9526
                                    if len(subjects) == 0:
                                        pass
                                        # 30: x**n2*f1
                            subjects30.appendleft(tmp55)
                    subjects30.appendleft(tmp52)
                if len(subjects30) >= 1:
                    tmp57 = subjects30.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.2.1.1', tmp57)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 13917
                        if len(subjects30) >= 1 and subjects30[0] == 2:
                            tmp59 = subjects30.popleft()
                            # State 13918
                            if len(subjects30) == 0:
                                pass
                                # State 13919
                                if len(subjects) == 0:
                                    pass
                                    # 36: i*x**2
                            subjects30.appendleft(tmp59)
                    subjects30.appendleft(tmp57)
                if len(subjects30) >= 1:
                    tmp60 = subjects30.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.2.0', tmp60)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 109627
                        if len(subjects30) >= 1 and subjects30[0] == 2:
                            tmp62 = subjects30.popleft()
                            # State 109628
                            if len(subjects30) == 0:
                                pass
                                # State 109629
                                if len(subjects) == 0:
                                    pass
                                    # 107: h*x**2
                            subjects30.appendleft(tmp62)
                    subjects30.appendleft(tmp60)
                subjects.appendleft(tmp29)
            if len(subjects) >= 1 and isinstance(subjects[0], sin):
                tmp63 = subjects.popleft()
                subjects64 = deque(tmp63._args)
                # State 72146
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 72147
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.2.1.2.1.0', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 72148
                        if len(subjects64) >= 1:
                            tmp67 = subjects64.popleft()
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i2.2.1.0', tmp67)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 72149
                                if len(subjects64) == 0:
                                    pass
                                    # State 72150
                                    if len(subjects) == 0:
                                        pass
                                        # 63: b*sin(x*f + e)
                            subjects64.appendleft(tmp67)
                    if len(subjects64) >= 1 and isinstance(subjects64[0], Mul):
                        tmp69 = subjects64.popleft()
                        associative1 = tmp69
                        associative_type1 = type(tmp69)
                        subjects70 = deque(tmp69._args)
                        matcher = CommutativeMatcher72152.get()
                        tmp71 = subjects70
                        subjects70 = []
                        for s in tmp71:
                            matcher.add_subject(s)
                        for pattern_index, subst3 in matcher.match(tmp71, subst2):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 72153
                                if len(subjects64) == 0:
                                    pass
                                    # State 72154
                                    if len(subjects) == 0:
                                        pass
                                        # 63: b*sin(x*f + e)
                        subjects64.appendleft(tmp69)
                if len(subjects64) >= 1 and isinstance(subjects64[0], Add):
                    tmp72 = subjects64.popleft()
                    associative1 = tmp72
                    associative_type1 = type(tmp72)
                    subjects73 = deque(tmp72._args)
                    matcher = CommutativeMatcher72156.get()
                    tmp74 = subjects73
                    subjects73 = []
                    for s in tmp74:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp74, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 72162
                            if len(subjects64) == 0:
                                pass
                                # State 72163
                                if len(subjects) == 0:
                                    pass
                                    # 63: b*sin(x*f + e)
                    subjects64.appendleft(tmp72)
                subjects.appendleft(tmp63)
            if len(subjects) >= 1 and isinstance(subjects[0], tan):
                tmp75 = subjects.popleft()
                subjects76 = deque(tmp75._args)
                # State 86730
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 86731
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.2.1.2.1.0', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 86732
                        if len(subjects76) >= 1:
                            tmp79 = subjects76.popleft()
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i2.2.1.0', tmp79)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 86733
                                if len(subjects76) == 0:
                                    pass
                                    # State 86734
                                    if len(subjects) == 0:
                                        pass
                                        # 84: b*tan(x*f + e)
                            subjects76.appendleft(tmp79)
                    if len(subjects76) >= 1 and isinstance(subjects76[0], Mul):
                        tmp81 = subjects76.popleft()
                        associative1 = tmp81
                        associative_type1 = type(tmp81)
                        subjects82 = deque(tmp81._args)
                        matcher = CommutativeMatcher86736.get()
                        tmp83 = subjects82
                        subjects82 = []
                        for s in tmp83:
                            matcher.add_subject(s)
                        for pattern_index, subst3 in matcher.match(tmp83, subst2):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 86737
                                if len(subjects76) == 0:
                                    pass
                                    # State 86738
                                    if len(subjects) == 0:
                                        pass
                                        # 84: b*tan(x*f + e)
                        subjects76.appendleft(tmp81)
                if len(subjects76) >= 1 and isinstance(subjects76[0], Add):
                    tmp84 = subjects76.popleft()
                    associative1 = tmp84
                    associative_type1 = type(tmp84)
                    subjects85 = deque(tmp84._args)
                    matcher = CommutativeMatcher86740.get()
                    tmp86 = subjects85
                    subjects85 = []
                    for s in tmp86:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp86, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 86746
                            if len(subjects76) == 0:
                                pass
                                # State 86747
                                if len(subjects) == 0:
                                    pass
                                    # 84: b*tan(x*f + e)
                    subjects76.appendleft(tmp84)
                subjects.appendleft(tmp75)
            if len(subjects) >= 1 and isinstance(subjects[0], sinh):
                tmp87 = subjects.popleft()
                subjects88 = deque(tmp87._args)
                # State 121825
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 121826
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.2.1.2.1.0', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 121827
                        if len(subjects88) >= 1:
                            tmp91 = subjects88.popleft()
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i2.2.1.0', tmp91)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 121828
                                if len(subjects88) == 0:
                                    pass
                                    # State 121829
                                    if len(subjects) == 0:
                                        pass
                                        # 118: b*sinh(x*b + a)
                            subjects88.appendleft(tmp91)
                    if len(subjects88) >= 1 and isinstance(subjects88[0], Mul):
                        tmp93 = subjects88.popleft()
                        associative1 = tmp93
                        associative_type1 = type(tmp93)
                        subjects94 = deque(tmp93._args)
                        matcher = CommutativeMatcher121831.get()
                        tmp95 = subjects94
                        subjects94 = []
                        for s in tmp95:
                            matcher.add_subject(s)
                        for pattern_index, subst3 in matcher.match(tmp95, subst2):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 121832
                                if len(subjects88) == 0:
                                    pass
                                    # State 121833
                                    if len(subjects) == 0:
                                        pass
                                        # 118: b*sinh(x*b + a)
                        subjects88.appendleft(tmp93)
                if len(subjects88) >= 1 and isinstance(subjects88[0], Add):
                    tmp96 = subjects88.popleft()
                    associative1 = tmp96
                    associative_type1 = type(tmp96)
                    subjects97 = deque(tmp96._args)
                    matcher = CommutativeMatcher121835.get()
                    tmp98 = subjects97
                    subjects97 = []
                    for s in tmp98:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp98, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 121841
                            if len(subjects88) == 0:
                                pass
                                # State 121842
                                if len(subjects) == 0:
                                    pass
                                    # 118: b*sinh(x*b + a)
                    subjects88.appendleft(tmp96)
                subjects.appendleft(tmp87)
            if len(subjects) >= 1 and isinstance(subjects[0], tanh):
                tmp99 = subjects.popleft()
                subjects100 = deque(tmp99._args)
                # State 125954
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 125955
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.2.1.2.1.0', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 125956
                        if len(subjects100) >= 1:
                            tmp103 = subjects100.popleft()
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i2.2.1.0', tmp103)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 125957
                                if len(subjects100) == 0:
                                    pass
                                    # State 125958
                                    if len(subjects) == 0:
                                        pass
                                        # 127: d*tanh(x*b + a)
                            subjects100.appendleft(tmp103)
                    if len(subjects100) >= 1 and isinstance(subjects100[0], Mul):
                        tmp105 = subjects100.popleft()
                        associative1 = tmp105
                        associative_type1 = type(tmp105)
                        subjects106 = deque(tmp105._args)
                        matcher = CommutativeMatcher125960.get()
                        tmp107 = subjects106
                        subjects106 = []
                        for s in tmp107:
                            matcher.add_subject(s)
                        for pattern_index, subst3 in matcher.match(tmp107, subst2):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 125961
                                if len(subjects100) == 0:
                                    pass
                                    # State 125962
                                    if len(subjects) == 0:
                                        pass
                                        # 127: d*tanh(x*b + a)
                        subjects100.appendleft(tmp105)
                if len(subjects100) >= 1 and isinstance(subjects100[0], Add):
                    tmp108 = subjects100.popleft()
                    associative1 = tmp108
                    associative_type1 = type(tmp108)
                    subjects109 = deque(tmp108._args)
                    matcher = CommutativeMatcher125964.get()
                    tmp110 = subjects109
                    subjects109 = []
                    for s in tmp110:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp110, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 125970
                            if len(subjects100) == 0:
                                pass
                                # State 125971
                                if len(subjects) == 0:
                                    pass
                                    # 127: d*tanh(x*b + a)
                    subjects100.appendleft(tmp108)
                subjects.appendleft(tmp99)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.0_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 2665
            subst2 = Substitution(subst1)
            try:
                subst2.try_add_variable('i2.2.1.2_1', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 2666
                if len(subjects) >= 1:
                    tmp113 = subjects.popleft()
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.2.1.1', tmp113)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 2667
                        if len(subjects) == 0:
                            pass
                            # 1: b*x**n
                    subjects.appendleft(tmp113)
                if len(subjects) >= 1:
                    tmp115 = subjects.popleft()
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.2.0', tmp115)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 8345
                        if len(subjects) == 0:
                            pass
                            # 20: x**n2*c
                    subjects.appendleft(tmp115)
                if len(subjects) >= 1:
                    tmp117 = subjects.popleft()
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.2.0_1', tmp117)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 8447
                        if len(subjects) == 0:
                            pass
                            # 21: x**n*b
                    subjects.appendleft(tmp117)
                subst3 = Substitution(subst2)
                try:
                    subst3.try_add_variable('i2.2.1.2.0', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 11082
                    if len(subjects) >= 1 and isinstance(subjects[0], Pow):
                        tmp120 = subjects.popleft()
                        subjects121 = deque(tmp120._args)
                        # State 11083
                        if len(subjects121) >= 1:
                            tmp122 = subjects121.popleft()
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i2.2.0', tmp122)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 11084
                                if len(subjects121) >= 1 and subjects121[0] == -1:
                                    tmp124 = subjects121.popleft()
                                    # State 11085
                                    if len(subjects121) == 0:
                                        pass
                                        # State 11086
                                        if len(subjects) == 0:
                                            pass
                                            # 32: c*(c/x)**n2
                                    subjects121.appendleft(tmp124)
                            subjects121.appendleft(tmp122)
                        subjects.appendleft(tmp120)
                if len(subjects) >= 1 and isinstance(subjects[0], Mul):
                    tmp125 = subjects.popleft()
                    associative1 = tmp125
                    associative_type1 = type(tmp125)
                    subjects126 = deque(tmp125._args)
                    matcher = CommutativeMatcher11088.get()
                    tmp127 = subjects126
                    subjects126 = []
                    for s in tmp127:
                        matcher.add_subject(s)
                    for pattern_index, subst3 in matcher.match(tmp127, subst2):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 11093
                            if len(subjects) == 0:
                                pass
                                # 32: c*(c/x)**n2
                    subjects.appendleft(tmp125)
            if len(subjects) >= 1:
                tmp128 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.1', tmp128)
                except ValueError:
                    pass
                else:
                    pass
                    # State 4077
                    if len(subjects) == 0:
                        pass
                        # 5: b*x
                subjects.appendleft(tmp128)
            subst2 = Substitution(subst1)
            try:
                subst2.try_add_variable('i2.2.1.2', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 7236
                if len(subjects) >= 1:
                    tmp131 = subjects.popleft()
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.2.0', tmp131)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 7237
                        if len(subjects) == 0:
                            pass
                            # 15: x**non2*b2
                    subjects.appendleft(tmp131)
            if len(subjects) >= 1:
                tmp133 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.4.1.1.0', tmp133)
                except ValueError:
                    pass
                else:
                    pass
                    # State 15087
                    if len(subjects) == 0:
                        pass
                        # 40: d*x
                subjects.appendleft(tmp133)
            if len(subjects) >= 1:
                tmp135 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.4.1.1.0', tmp135)
                except ValueError:
                    pass
                else:
                    pass
                    # State 15559
                    if len(subjects) == 0:
                        pass
                        # 41: d*x
                subjects.appendleft(tmp135)
            if len(subjects) >= 1:
                tmp137 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.2.2.1.0', tmp137)
                except ValueError:
                    pass
                else:
                    pass
                    # State 23652
                    if len(subjects) == 0:
                        pass
                        # 44: h*x
                subjects.appendleft(tmp137)
            if len(subjects) >= 1:
                tmp139 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.1.0', tmp139)
                except ValueError:
                    pass
                else:
                    pass
                    # State 72205
                    if len(subjects) == 0:
                        pass
                        # 64: d*x
                subjects.appendleft(tmp139)
            if len(subjects) >= 1:
                tmp141 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.3.1.0', tmp141)
                except ValueError:
                    pass
                else:
                    pass
                    # State 86797
                    if len(subjects) == 0:
                        pass
                        # 85: d*x
                subjects.appendleft(tmp141)
            if len(subjects) >= 1:
                tmp143 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.0', tmp143)
                except ValueError:
                    pass
                else:
                    pass
                    # State 109468
                    if len(subjects) == 0:
                        pass
                        # 106: e*x
                subjects.appendleft(tmp143)
            if len(subjects) >= 1 and isinstance(subjects[0], Pow):
                tmp145 = subjects.popleft()
                subjects146 = deque(tmp145._args)
                # State 2668
                if len(subjects146) >= 1:
                    tmp147 = subjects146.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.1', tmp147)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 2669
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.2_1', 1)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 2670
                            if len(subjects146) == 0:
                                pass
                                # State 2671
                                if len(subjects) == 0:
                                    pass
                                    # 1: b*x**n
                        if len(subjects146) >= 1:
                            tmp150 = subjects146.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.2_1', tmp150)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 2670
                                if len(subjects146) == 0:
                                    pass
                                    # State 2671
                                    if len(subjects) == 0:
                                        pass
                                        # 1: b*x**n
                            subjects146.appendleft(tmp150)
                        if len(subjects146) >= 1:
                            tmp152 = subjects146.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.2', tmp152)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 6911
                                if len(subjects146) == 0:
                                    pass
                                    # State 6912
                                    if len(subjects) == 0:
                                        pass
                                        # 12: b2*x**j
                            subjects146.appendleft(tmp152)
                        if len(subjects146) >= 1:
                            tmp154 = subjects146.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.2_1', tmp154)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 8682
                                if len(subjects146) == 0:
                                    pass
                                    # State 8683
                                    if len(subjects) == 0:
                                        pass
                                        # 24: c*x**n2
                            subjects146.appendleft(tmp154)
                        if len(subjects146) >= 1 and subjects146[0] == 2:
                            tmp156 = subjects146.popleft()
                            # State 5384
                            if len(subjects146) == 0:
                                pass
                                # State 5385
                                if len(subjects) == 0:
                                    pass
                                    # 10: c*x**2
                            subjects146.appendleft(tmp156)
                    subjects146.appendleft(tmp147)
                if len(subjects146) >= 1:
                    tmp157 = subjects146.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.0', tmp157)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 7238
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.2', 1)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 7239
                            if len(subjects146) == 0:
                                pass
                                # State 7240
                                if len(subjects) == 0:
                                    pass
                                    # 15: x**non2*b2
                        if len(subjects146) >= 1:
                            tmp160 = subjects146.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.2', tmp160)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 7239
                                if len(subjects146) == 0:
                                    pass
                                    # State 7240
                                    if len(subjects) == 0:
                                        pass
                                        # 15: x**non2*b2
                            subjects146.appendleft(tmp160)
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.2_1', 1)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 8346
                            if len(subjects146) == 0:
                                pass
                                # State 8347
                                if len(subjects) == 0:
                                    pass
                                    # 20: x**n2*c
                        if len(subjects146) >= 1:
                            tmp163 = subjects146.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.2_1', tmp163)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 8346
                                if len(subjects146) == 0:
                                    pass
                                    # State 8347
                                    if len(subjects) == 0:
                                        pass
                                        # 20: x**n2*c
                            subjects146.appendleft(tmp163)
                        if len(subjects146) >= 1:
                            tmp165 = subjects146.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.2_1', tmp165)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 9343
                                if len(subjects146) == 0:
                                    pass
                                    # State 9344
                                    if len(subjects) == 0:
                                        pass
                                        # 28: x**n2*c
                            subjects146.appendleft(tmp165)
                        if len(subjects146) >= 1:
                            tmp167 = subjects146.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.2', tmp167)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 9520
                                if len(subjects146) == 0:
                                    pass
                                    # State 9521
                                    if len(subjects) == 0:
                                        pass
                                        # 29: x**n*b2
                            subjects146.appendleft(tmp167)
                    subjects146.appendleft(tmp157)
                if len(subjects146) >= 1:
                    tmp169 = subjects146.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.1_1', tmp169)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 7767
                        if len(subjects146) >= 1:
                            tmp171 = subjects146.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.2', tmp171)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 7768
                                if len(subjects146) == 0:
                                    pass
                                    # State 7769
                                    if len(subjects) == 0:
                                        pass
                                        # 19: d*v**n
                            subjects146.appendleft(tmp171)
                    subjects146.appendleft(tmp169)
                if len(subjects146) >= 1:
                    tmp173 = subjects146.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.0_1', tmp173)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 8448
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.2_1', 1)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 8449
                            if len(subjects146) == 0:
                                pass
                                # State 8450
                                if len(subjects) == 0:
                                    pass
                                    # 21: x**n*b
                        if len(subjects146) >= 1:
                            tmp176 = subjects146.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.2_1', tmp176)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 8449
                                if len(subjects146) == 0:
                                    pass
                                    # State 8450
                                    if len(subjects) == 0:
                                        pass
                                        # 21: x**n*b
                            subjects146.appendleft(tmp176)
                    subjects146.appendleft(tmp173)
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.0', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 11094
                    if len(subjects146) >= 1 and isinstance(subjects146[0], Pow):
                        tmp179 = subjects146.popleft()
                        subjects180 = deque(tmp179._args)
                        # State 11095
                        if len(subjects180) >= 1:
                            tmp181 = subjects180.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.0', tmp181)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 11096
                                if len(subjects180) >= 1 and subjects180[0] == -1:
                                    tmp183 = subjects180.popleft()
                                    # State 11097
                                    if len(subjects180) == 0:
                                        pass
                                        # State 11098
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.2.1.2_1', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 11099
                                            if len(subjects146) == 0:
                                                pass
                                                # State 11100
                                                if len(subjects) == 0:
                                                    pass
                                                    # 32: c*(c/x)**n2
                                        if len(subjects146) >= 1:
                                            tmp185 = subjects146.popleft()
                                            subst4 = Substitution(subst3)
                                            try:
                                                subst4.try_add_variable('i2.2.1.2_1', tmp185)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 11099
                                                if len(subjects146) == 0:
                                                    pass
                                                    # State 11100
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 32: c*(c/x)**n2
                                            subjects146.appendleft(tmp185)
                                    subjects180.appendleft(tmp183)
                            subjects180.appendleft(tmp181)
                        subjects146.appendleft(tmp179)
                if len(subjects146) >= 1:
                    tmp187 = subjects146.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.2.1.0', tmp187)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 110620
                        if len(subjects146) >= 1 and subjects146[0] == 2:
                            tmp189 = subjects146.popleft()
                            # State 110621
                            if len(subjects146) == 0:
                                pass
                                # State 110622
                                if len(subjects) == 0:
                                    pass
                                    # 112: C*x**2
                            subjects146.appendleft(tmp189)
                    subjects146.appendleft(tmp187)
                if len(subjects146) >= 1 and isinstance(subjects146[0], Mul):
                    tmp190 = subjects146.popleft()
                    associative1 = tmp190
                    associative_type1 = type(tmp190)
                    subjects191 = deque(tmp190._args)
                    matcher = CommutativeMatcher11102.get()
                    tmp192 = subjects191
                    subjects191 = []
                    for s in tmp192:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp192, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 11107
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.2_1', 1)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 11108
                                if len(subjects146) == 0:
                                    pass
                                    # State 11109
                                    if len(subjects) == 0:
                                        pass
                                        # 32: c*(c/x)**n2
                            if len(subjects146) >= 1:
                                tmp194 = []
                                tmp194.append(subjects146.popleft())
                                while True:
                                    if len(tmp194) > 1:
                                        tmp195 = create_operation_expression(associative1, tmp194)
                                    elif len(tmp194) == 1:
                                        tmp195 = tmp194[0]
                                    else:
                                        assert False, "Unreachable"
                                    subst3 = Substitution(subst2)
                                    try:
                                        subst3.try_add_variable('i2.2.1.2_1', tmp195)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 11108
                                        if len(subjects146) == 0:
                                            pass
                                            # State 11109
                                            if len(subjects) == 0:
                                                pass
                                                # 32: c*(c/x)**n2
                                    if len(subjects146) == 0:
                                        break
                                    tmp194.append(subjects146.popleft())
                                subjects146.extendleft(reversed(tmp194))
                    subjects146.appendleft(tmp190)
                if len(subjects146) >= 1 and isinstance(subjects146[0], Add):
                    tmp197 = subjects146.popleft()
                    associative1 = tmp197
                    associative_type1 = type(tmp197)
                    subjects198 = deque(tmp197._args)
                    matcher = CommutativeMatcher13968.get()
                    tmp199 = subjects198
                    subjects198 = []
                    for s in tmp199:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp199, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 13981
                            if len(subjects146) >= 1 and subjects146[0] == 1/2:
                                tmp200 = subjects146.popleft()
                                # State 13982
                                if len(subjects146) == 0:
                                    pass
                                    # State 13983
                                    if len(subjects) == 0:
                                        pass
                                        # 38: f*sqrt(x**2*c + a)
                                subjects146.appendleft(tmp200)
                    subjects146.appendleft(tmp197)
                if len(subjects146) >= 1 and isinstance(subjects146[0], tan):
                    tmp201 = subjects146.popleft()
                    subjects202 = deque(tmp201._args)
                    # State 78708
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.3.0', S(0))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 78709
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.3.1.0_1', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 78710
                            if len(subjects202) >= 1:
                                tmp205 = subjects202.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.2.1.3.1.0', tmp205)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 78711
                                    if len(subjects202) == 0:
                                        pass
                                        # State 78712
                                        if len(subjects146) >= 1 and subjects146[0] == -1:
                                            tmp207 = subjects146.popleft()
                                            # State 78713
                                            if len(subjects146) == 0:
                                                pass
                                                # State 78714
                                                if len(subjects) == 0:
                                                    pass
                                                    # 78: d/tan(e + x*f)
                                            subjects146.appendleft(tmp207)
                                subjects202.appendleft(tmp205)
                        if len(subjects202) >= 1 and isinstance(subjects202[0], Mul):
                            tmp208 = subjects202.popleft()
                            associative1 = tmp208
                            associative_type1 = type(tmp208)
                            subjects209 = deque(tmp208._args)
                            matcher = CommutativeMatcher78716.get()
                            tmp210 = subjects209
                            subjects209 = []
                            for s in tmp210:
                                matcher.add_subject(s)
                            for pattern_index, subst3 in matcher.match(tmp210, subst2):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 78717
                                    if len(subjects202) == 0:
                                        pass
                                        # State 78718
                                        if len(subjects146) >= 1 and subjects146[0] == -1:
                                            tmp211 = subjects146.popleft()
                                            # State 78719
                                            if len(subjects146) == 0:
                                                pass
                                                # State 78720
                                                if len(subjects) == 0:
                                                    pass
                                                    # 78: d/tan(e + x*f)
                                            subjects146.appendleft(tmp211)
                            subjects202.appendleft(tmp208)
                    if len(subjects202) >= 1 and isinstance(subjects202[0], Add):
                        tmp212 = subjects202.popleft()
                        associative1 = tmp212
                        associative_type1 = type(tmp212)
                        subjects213 = deque(tmp212._args)
                        matcher = CommutativeMatcher78722.get()
                        tmp214 = subjects213
                        subjects213 = []
                        for s in tmp214:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp214, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 78728
                                if len(subjects202) == 0:
                                    pass
                                    # State 78729
                                    if len(subjects146) >= 1 and subjects146[0] == -1:
                                        tmp215 = subjects146.popleft()
                                        # State 78730
                                        if len(subjects146) == 0:
                                            pass
                                            # State 78731
                                            if len(subjects) == 0:
                                                pass
                                                # 78: d/tan(e + x*f)
                                        subjects146.appendleft(tmp215)
                        subjects202.appendleft(tmp212)
                    subjects146.appendleft(tmp201)
                if len(subjects146) >= 1 and isinstance(subjects146[0], cos):
                    tmp216 = subjects146.popleft()
                    subjects217 = deque(tmp216._args)
                    # State 91235
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.3.0', S(0))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 91236
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.3.1.0_1', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 91237
                            if len(subjects217) >= 1:
                                tmp220 = subjects217.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.2.1.3.1.0', tmp220)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 91238
                                    if len(subjects217) == 0:
                                        pass
                                        # State 91239
                                        if len(subjects146) >= 1 and subjects146[0] == -1:
                                            tmp222 = subjects146.popleft()
                                            # State 91240
                                            if len(subjects146) == 0:
                                                pass
                                                # State 91241
                                                if len(subjects) == 0:
                                                    pass
                                                    # 91: d/cos(e + x*f)
                                            subjects146.appendleft(tmp222)
                                subjects217.appendleft(tmp220)
                        if len(subjects217) >= 1 and isinstance(subjects217[0], Mul):
                            tmp223 = subjects217.popleft()
                            associative1 = tmp223
                            associative_type1 = type(tmp223)
                            subjects224 = deque(tmp223._args)
                            matcher = CommutativeMatcher91243.get()
                            tmp225 = subjects224
                            subjects224 = []
                            for s in tmp225:
                                matcher.add_subject(s)
                            for pattern_index, subst3 in matcher.match(tmp225, subst2):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 91244
                                    if len(subjects217) == 0:
                                        pass
                                        # State 91245
                                        if len(subjects146) >= 1 and subjects146[0] == -1:
                                            tmp226 = subjects146.popleft()
                                            # State 91246
                                            if len(subjects146) == 0:
                                                pass
                                                # State 91247
                                                if len(subjects) == 0:
                                                    pass
                                                    # 91: d/cos(e + x*f)
                                            subjects146.appendleft(tmp226)
                            subjects217.appendleft(tmp223)
                    if len(subjects217) >= 1 and isinstance(subjects217[0], Add):
                        tmp227 = subjects217.popleft()
                        associative1 = tmp227
                        associative_type1 = type(tmp227)
                        subjects228 = deque(tmp227._args)
                        matcher = CommutativeMatcher91249.get()
                        tmp229 = subjects228
                        subjects228 = []
                        for s in tmp229:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp229, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 91255
                                if len(subjects217) == 0:
                                    pass
                                    # State 91256
                                    if len(subjects146) >= 1 and subjects146[0] == -1:
                                        tmp230 = subjects146.popleft()
                                        # State 91257
                                        if len(subjects146) == 0:
                                            pass
                                            # State 91258
                                            if len(subjects) == 0:
                                                pass
                                                # 91: d/cos(e + x*f)
                                        subjects146.appendleft(tmp230)
                        subjects217.appendleft(tmp227)
                    subjects146.appendleft(tmp216)
                if len(subjects146) >= 1 and isinstance(subjects146[0], sin):
                    tmp231 = subjects146.popleft()
                    subjects232 = deque(tmp231._args)
                    # State 91285
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.3.0', S(0))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 91286
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.3.1.0_1', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 91287
                            if len(subjects232) >= 1:
                                tmp235 = subjects232.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.2.1.3.1.0', tmp235)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 91288
                                    if len(subjects232) == 0:
                                        pass
                                        # State 91289
                                        if len(subjects146) >= 1 and subjects146[0] == -1:
                                            tmp237 = subjects146.popleft()
                                            # State 91290
                                            if len(subjects146) == 0:
                                                pass
                                                # State 91291
                                                if len(subjects) == 0:
                                                    pass
                                                    # 92: d/sin(e + x*f)
                                            subjects146.appendleft(tmp237)
                                subjects232.appendleft(tmp235)
                        if len(subjects232) >= 1 and isinstance(subjects232[0], Mul):
                            tmp238 = subjects232.popleft()
                            associative1 = tmp238
                            associative_type1 = type(tmp238)
                            subjects239 = deque(tmp238._args)
                            matcher = CommutativeMatcher91293.get()
                            tmp240 = subjects239
                            subjects239 = []
                            for s in tmp240:
                                matcher.add_subject(s)
                            for pattern_index, subst3 in matcher.match(tmp240, subst2):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 91294
                                    if len(subjects232) == 0:
                                        pass
                                        # State 91295
                                        if len(subjects146) >= 1 and subjects146[0] == -1:
                                            tmp241 = subjects146.popleft()
                                            # State 91296
                                            if len(subjects146) == 0:
                                                pass
                                                # State 91297
                                                if len(subjects) == 0:
                                                    pass
                                                    # 92: d/sin(e + x*f)
                                            subjects146.appendleft(tmp241)
                            subjects232.appendleft(tmp238)
                    if len(subjects232) >= 1 and isinstance(subjects232[0], Add):
                        tmp242 = subjects232.popleft()
                        associative1 = tmp242
                        associative_type1 = type(tmp242)
                        subjects243 = deque(tmp242._args)
                        matcher = CommutativeMatcher91299.get()
                        tmp244 = subjects243
                        subjects243 = []
                        for s in tmp244:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp244, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 91305
                                if len(subjects232) == 0:
                                    pass
                                    # State 91306
                                    if len(subjects146) >= 1 and subjects146[0] == -1:
                                        tmp245 = subjects146.popleft()
                                        # State 91307
                                        if len(subjects146) == 0:
                                            pass
                                            # State 91308
                                            if len(subjects) == 0:
                                                pass
                                                # 92: d/sin(e + x*f)
                                        subjects146.appendleft(tmp245)
                        subjects232.appendleft(tmp242)
                    subjects146.appendleft(tmp231)
                subjects.appendleft(tmp145)
            if len(subjects) >= 1 and isinstance(subjects[0], log):
                tmp246 = subjects.popleft()
                subjects247 = deque(tmp246._args)
                # State 37119
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.0', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 37120
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.2.1.2.2', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 37121
                        subst4 = Substitution(subst3)
                        try:
                            subst4.try_add_variable('i2.2.1.2.2.0', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 37122
                            subst5 = Substitution(subst4)
                            try:
                                subst5.try_add_variable('i2.2.1.2.2.2', S(1))
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 37123
                                subst6 = Substitution(subst5)
                                try:
                                    subst6.try_add_variable('i2.2.1.2.2.2.0', S(0))
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 37124
                                    subst7 = Substitution(subst6)
                                    try:
                                        subst7.try_add_variable('i2.2.1.2.2.2.1.0', S(1))
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 37125
                                        if len(subjects247) >= 1 and isinstance(subjects247[0], Pow):
                                            tmp254 = subjects247.popleft()
                                            subjects255 = deque(tmp254._args)
                                            # State 37126
                                            if len(subjects255) >= 1:
                                                tmp256 = subjects255.popleft()
                                                subst8 = Substitution(subst7)
                                                try:
                                                    subst8.try_add_variable('i2.2.1.1', tmp256)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 37127
                                                    if len(subjects255) >= 1:
                                                        tmp258 = subjects255.popleft()
                                                        subst9 = Substitution(subst8)
                                                        try:
                                                            subst9.try_add_variable('i2.2.1.2', tmp258)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            # State 37128
                                                            if len(subjects255) == 0:
                                                                pass
                                                                # State 37129
                                                                if len(subjects247) == 0:
                                                                    pass
                                                                    # State 37130
                                                                    if len(subjects) == 0:
                                                                        pass
                                                                        # 47: b*log(c*(d*(x**j*f + e)**p)**q)
                                                        subjects255.appendleft(tmp258)
                                                subjects255.appendleft(tmp256)
                                            subjects247.appendleft(tmp254)
                                    if len(subjects247) >= 1 and isinstance(subjects247[0], Mul):
                                        tmp260 = subjects247.popleft()
                                        associative1 = tmp260
                                        associative_type1 = type(tmp260)
                                        subjects261 = deque(tmp260._args)
                                        matcher = CommutativeMatcher37132.get()
                                        tmp262 = subjects261
                                        subjects261 = []
                                        for s in tmp262:
                                            matcher.add_subject(s)
                                        for pattern_index, subst7 in matcher.match(tmp262, subst6):
                                            pass
                                            if pattern_index == 0:
                                                pass
                                                # State 37137
                                                if len(subjects247) == 0:
                                                    pass
                                                    # State 37138
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 47: b*log(c*(d*(x**j*f + e)**p)**q)
                                        subjects247.appendleft(tmp260)
                                if len(subjects247) >= 1 and isinstance(subjects247[0], Add):
                                    tmp263 = subjects247.popleft()
                                    associative1 = tmp263
                                    associative_type1 = type(tmp263)
                                    subjects264 = deque(tmp263._args)
                                    matcher = CommutativeMatcher37140.get()
                                    tmp265 = subjects264
                                    subjects264 = []
                                    for s in tmp265:
                                        matcher.add_subject(s)
                                    for pattern_index, subst6 in matcher.match(tmp265, subst5):
                                        pass
                                        if pattern_index == 0:
                                            pass
                                            # State 37153
                                            if len(subjects247) == 0:
                                                pass
                                                # State 37154
                                                if len(subjects) == 0:
                                                    pass
                                                    # 47: b*log(c*(d*(x**j*f + e)**p)**q)
                                    subjects247.appendleft(tmp263)
                            if len(subjects247) >= 1 and isinstance(subjects247[0], Pow):
                                tmp266 = subjects247.popleft()
                                subjects267 = deque(tmp266._args)
                                # State 37155
                                subst5 = Substitution(subst4)
                                try:
                                    subst5.try_add_variable('i2.2.1.2.2.2.0', S(0))
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 37156
                                    subst6 = Substitution(subst5)
                                    try:
                                        subst6.try_add_variable('i2.2.1.2.2.2.1.0', S(1))
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 37157
                                        if len(subjects267) >= 1 and isinstance(subjects267[0], Pow):
                                            tmp270 = subjects267.popleft()
                                            subjects271 = deque(tmp270._args)
                                            # State 37158
                                            if len(subjects271) >= 1:
                                                tmp272 = subjects271.popleft()
                                                subst7 = Substitution(subst6)
                                                try:
                                                    subst7.try_add_variable('i2.2.1.1', tmp272)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 37159
                                                    if len(subjects271) >= 1:
                                                        tmp274 = subjects271.popleft()
                                                        subst8 = Substitution(subst7)
                                                        try:
                                                            subst8.try_add_variable('i2.2.1.2', tmp274)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            # State 37160
                                                            if len(subjects271) == 0:
                                                                pass
                                                                # State 37161
                                                                subst9 = Substitution(subst8)
                                                                try:
                                                                    subst9.try_add_variable('i2.2.1.2.2.2', 1)
                                                                except ValueError:
                                                                    pass
                                                                else:
                                                                    pass
                                                                    # State 37162
                                                                    if len(subjects267) == 0:
                                                                        pass
                                                                        # State 37163
                                                                        if len(subjects247) == 0:
                                                                            pass
                                                                            # State 37164
                                                                            if len(subjects) == 0:
                                                                                pass
                                                                                # 47: b*log(c*(d*(x**j*f + e)**p)**q)
                                                                if len(subjects267) >= 1:
                                                                    tmp277 = subjects267.popleft()
                                                                    subst9 = Substitution(subst8)
                                                                    try:
                                                                        subst9.try_add_variable('i2.2.1.2.2.2', tmp277)
                                                                    except ValueError:
                                                                        pass
                                                                    else:
                                                                        pass
                                                                        # State 37162
                                                                        if len(subjects267) == 0:
                                                                            pass
                                                                            # State 37163
                                                                            if len(subjects247) == 0:
                                                                                pass
                                                                                # State 37164
                                                                                if len(subjects) == 0:
                                                                                    pass
                                                                                    # 47: b*log(c*(d*(x**j*f + e)**p)**q)
                                                                    subjects267.appendleft(tmp277)
                                                        subjects271.appendleft(tmp274)
                                                subjects271.appendleft(tmp272)
                                            subjects267.appendleft(tmp270)
                                    if len(subjects267) >= 1 and isinstance(subjects267[0], Mul):
                                        tmp279 = subjects267.popleft()
                                        associative1 = tmp279
                                        associative_type1 = type(tmp279)
                                        subjects280 = deque(tmp279._args)
                                        matcher = CommutativeMatcher37166.get()
                                        tmp281 = subjects280
                                        subjects280 = []
                                        for s in tmp281:
                                            matcher.add_subject(s)
                                        for pattern_index, subst6 in matcher.match(tmp281, subst5):
                                            pass
                                            if pattern_index == 0:
                                                pass
                                                # State 37171
                                                subst7 = Substitution(subst6)
                                                try:
                                                    subst7.try_add_variable('i2.2.1.2.2.2', 1)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 37172
                                                    if len(subjects267) == 0:
                                                        pass
                                                        # State 37173
                                                        if len(subjects247) == 0:
                                                            pass
                                                            # State 37174
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 47: b*log(c*(d*(x**j*f + e)**p)**q)
                                                if len(subjects267) >= 1:
                                                    tmp283 = []
                                                    tmp283.append(subjects267.popleft())
                                                    while True:
                                                        if len(tmp283) > 1:
                                                            tmp284 = create_operation_expression(associative1, tmp283)
                                                        elif len(tmp283) == 1:
                                                            tmp284 = tmp283[0]
                                                        else:
                                                            assert False, "Unreachable"
                                                        subst7 = Substitution(subst6)
                                                        try:
                                                            subst7.try_add_variable('i2.2.1.2.2.2', tmp284)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            # State 37172
                                                            if len(subjects267) == 0:
                                                                pass
                                                                # State 37173
                                                                if len(subjects247) == 0:
                                                                    pass
                                                                    # State 37174
                                                                    if len(subjects) == 0:
                                                                        pass
                                                                        # 47: b*log(c*(d*(x**j*f + e)**p)**q)
                                                        if len(subjects267) == 0:
                                                            break
                                                        tmp283.append(subjects267.popleft())
                                                    subjects267.extendleft(reversed(tmp283))
                                        subjects267.appendleft(tmp279)
                                if len(subjects267) >= 1 and isinstance(subjects267[0], Add):
                                    tmp286 = subjects267.popleft()
                                    associative1 = tmp286
                                    associative_type1 = type(tmp286)
                                    subjects287 = deque(tmp286._args)
                                    matcher = CommutativeMatcher37176.get()
                                    tmp288 = subjects287
                                    subjects287 = []
                                    for s in tmp288:
                                        matcher.add_subject(s)
                                    for pattern_index, subst5 in matcher.match(tmp288, subst4):
                                        pass
                                        if pattern_index == 0:
                                            pass
                                            # State 37189
                                            subst6 = Substitution(subst5)
                                            try:
                                                subst6.try_add_variable('i2.2.1.2.2.2', 1)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 37190
                                                if len(subjects267) == 0:
                                                    pass
                                                    # State 37191
                                                    if len(subjects247) == 0:
                                                        pass
                                                        # State 37192
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 47: b*log(c*(d*(x**j*f + e)**p)**q)
                                            if len(subjects267) >= 1:
                                                tmp290 = []
                                                tmp290.append(subjects267.popleft())
                                                while True:
                                                    if len(tmp290) > 1:
                                                        tmp291 = create_operation_expression(associative1, tmp290)
                                                    elif len(tmp290) == 1:
                                                        tmp291 = tmp290[0]
                                                    else:
                                                        assert False, "Unreachable"
                                                    subst6 = Substitution(subst5)
                                                    try:
                                                        subst6.try_add_variable('i2.2.1.2.2.2', tmp291)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 37190
                                                        if len(subjects267) == 0:
                                                            pass
                                                            # State 37191
                                                            if len(subjects247) == 0:
                                                                pass
                                                                # State 37192
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 47: b*log(c*(d*(x**j*f + e)**p)**q)
                                                    if len(subjects267) == 0:
                                                        break
                                                    tmp290.append(subjects267.popleft())
                                                subjects267.extendleft(reversed(tmp290))
                                    subjects267.appendleft(tmp286)
                                subjects247.appendleft(tmp266)
                        if len(subjects247) >= 1 and isinstance(subjects247[0], Mul):
                            tmp293 = subjects247.popleft()
                            associative1 = tmp293
                            associative_type1 = type(tmp293)
                            subjects294 = deque(tmp293._args)
                            matcher = CommutativeMatcher37194.get()
                            tmp295 = subjects294
                            subjects294 = []
                            for s in tmp295:
                                matcher.add_subject(s)
                            for pattern_index, subst4 in matcher.match(tmp295, subst3):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 37259
                                    if len(subjects247) == 0:
                                        pass
                                        # State 37260
                                        if len(subjects) == 0:
                                            pass
                                            # 47: b*log(c*(d*(x**j*f + e)**p)**q)
                            subjects247.appendleft(tmp293)
                    if len(subjects247) >= 1 and isinstance(subjects247[0], Pow):
                        tmp296 = subjects247.popleft()
                        subjects297 = deque(tmp296._args)
                        # State 37261
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.2.2.0', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 37262
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i2.2.1.2.2.2', S(1))
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 37263
                                subst5 = Substitution(subst4)
                                try:
                                    subst5.try_add_variable('i2.2.1.2.2.2.0', S(0))
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 37264
                                    subst6 = Substitution(subst5)
                                    try:
                                        subst6.try_add_variable('i2.2.1.2.2.2.1.0', S(1))
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 37265
                                        if len(subjects297) >= 1 and isinstance(subjects297[0], Pow):
                                            tmp302 = subjects297.popleft()
                                            subjects303 = deque(tmp302._args)
                                            # State 37266
                                            if len(subjects303) >= 1:
                                                tmp304 = subjects303.popleft()
                                                subst7 = Substitution(subst6)
                                                try:
                                                    subst7.try_add_variable('i2.2.1.1', tmp304)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 37267
                                                    if len(subjects303) >= 1:
                                                        tmp306 = subjects303.popleft()
                                                        subst8 = Substitution(subst7)
                                                        try:
                                                            subst8.try_add_variable('i2.2.1.2', tmp306)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            # State 37268
                                                            if len(subjects303) == 0:
                                                                pass
                                                                # State 37269
                                                                subst9 = Substitution(subst8)
                                                                try:
                                                                    subst9.try_add_variable('i2.2.1.2.2', 1)
                                                                except ValueError:
                                                                    pass
                                                                else:
                                                                    pass
                                                                    # State 37270
                                                                    if len(subjects297) == 0:
                                                                        pass
                                                                        # State 37271
                                                                        if len(subjects247) == 0:
                                                                            pass
                                                                            # State 37272
                                                                            if len(subjects) == 0:
                                                                                pass
                                                                                # 47: b*log(c*(d*(x**j*f + e)**p)**q)
                                                                if len(subjects297) >= 1:
                                                                    tmp309 = subjects297.popleft()
                                                                    subst9 = Substitution(subst8)
                                                                    try:
                                                                        subst9.try_add_variable('i2.2.1.2.2', tmp309)
                                                                    except ValueError:
                                                                        pass
                                                                    else:
                                                                        pass
                                                                        # State 37270
                                                                        if len(subjects297) == 0:
                                                                            pass
                                                                            # State 37271
                                                                            if len(subjects247) == 0:
                                                                                pass
                                                                                # State 37272
                                                                                if len(subjects) == 0:
                                                                                    pass
                                                                                    # 47: b*log(c*(d*(x**j*f + e)**p)**q)
                                                                    subjects297.appendleft(tmp309)
                                                        subjects303.appendleft(tmp306)
                                                subjects303.appendleft(tmp304)
                                            subjects297.appendleft(tmp302)
                                    if len(subjects297) >= 1 and isinstance(subjects297[0], Mul):
                                        tmp311 = subjects297.popleft()
                                        associative1 = tmp311
                                        associative_type1 = type(tmp311)
                                        subjects312 = deque(tmp311._args)
                                        matcher = CommutativeMatcher37274.get()
                                        tmp313 = subjects312
                                        subjects312 = []
                                        for s in tmp313:
                                            matcher.add_subject(s)
                                        for pattern_index, subst6 in matcher.match(tmp313, subst5):
                                            pass
                                            if pattern_index == 0:
                                                pass
                                                # State 37279
                                                subst7 = Substitution(subst6)
                                                try:
                                                    subst7.try_add_variable('i2.2.1.2.2', 1)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 37280
                                                    if len(subjects297) == 0:
                                                        pass
                                                        # State 37281
                                                        if len(subjects247) == 0:
                                                            pass
                                                            # State 37282
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 47: b*log(c*(d*(x**j*f + e)**p)**q)
                                                if len(subjects297) >= 1:
                                                    tmp315 = []
                                                    tmp315.append(subjects297.popleft())
                                                    while True:
                                                        if len(tmp315) > 1:
                                                            tmp316 = create_operation_expression(associative1, tmp315)
                                                        elif len(tmp315) == 1:
                                                            tmp316 = tmp315[0]
                                                        else:
                                                            assert False, "Unreachable"
                                                        subst7 = Substitution(subst6)
                                                        try:
                                                            subst7.try_add_variable('i2.2.1.2.2', tmp316)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            # State 37280
                                                            if len(subjects297) == 0:
                                                                pass
                                                                # State 37281
                                                                if len(subjects247) == 0:
                                                                    pass
                                                                    # State 37282
                                                                    if len(subjects) == 0:
                                                                        pass
                                                                        # 47: b*log(c*(d*(x**j*f + e)**p)**q)
                                                        if len(subjects297) == 0:
                                                            break
                                                        tmp315.append(subjects297.popleft())
                                                    subjects297.extendleft(reversed(tmp315))
                                        subjects297.appendleft(tmp311)
                                if len(subjects297) >= 1 and isinstance(subjects297[0], Add):
                                    tmp318 = subjects297.popleft()
                                    associative1 = tmp318
                                    associative_type1 = type(tmp318)
                                    subjects319 = deque(tmp318._args)
                                    matcher = CommutativeMatcher37284.get()
                                    tmp320 = subjects319
                                    subjects319 = []
                                    for s in tmp320:
                                        matcher.add_subject(s)
                                    for pattern_index, subst5 in matcher.match(tmp320, subst4):
                                        pass
                                        if pattern_index == 0:
                                            pass
                                            # State 37297
                                            subst6 = Substitution(subst5)
                                            try:
                                                subst6.try_add_variable('i2.2.1.2.2', 1)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 37298
                                                if len(subjects297) == 0:
                                                    pass
                                                    # State 37299
                                                    if len(subjects247) == 0:
                                                        pass
                                                        # State 37300
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 47: b*log(c*(d*(x**j*f + e)**p)**q)
                                            if len(subjects297) >= 1:
                                                tmp322 = []
                                                tmp322.append(subjects297.popleft())
                                                while True:
                                                    if len(tmp322) > 1:
                                                        tmp323 = create_operation_expression(associative1, tmp322)
                                                    elif len(tmp322) == 1:
                                                        tmp323 = tmp322[0]
                                                    else:
                                                        assert False, "Unreachable"
                                                    subst6 = Substitution(subst5)
                                                    try:
                                                        subst6.try_add_variable('i2.2.1.2.2', tmp323)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 37298
                                                        if len(subjects297) == 0:
                                                            pass
                                                            # State 37299
                                                            if len(subjects247) == 0:
                                                                pass
                                                                # State 37300
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 47: b*log(c*(d*(x**j*f + e)**p)**q)
                                                    if len(subjects297) == 0:
                                                        break
                                                    tmp322.append(subjects297.popleft())
                                                subjects297.extendleft(reversed(tmp322))
                                    subjects297.appendleft(tmp318)
                            if len(subjects297) >= 1 and isinstance(subjects297[0], Pow):
                                tmp325 = subjects297.popleft()
                                subjects326 = deque(tmp325._args)
                                # State 37301
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.2.1.2.2.2.0', S(0))
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 37302
                                    subst5 = Substitution(subst4)
                                    try:
                                        subst5.try_add_variable('i2.2.1.2.2.2.1.0', S(1))
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 37303
                                        if len(subjects326) >= 1 and isinstance(subjects326[0], Pow):
                                            tmp329 = subjects326.popleft()
                                            subjects330 = deque(tmp329._args)
                                            # State 37304
                                            if len(subjects330) >= 1:
                                                tmp331 = subjects330.popleft()
                                                subst6 = Substitution(subst5)
                                                try:
                                                    subst6.try_add_variable('i2.2.1.1', tmp331)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 37305
                                                    if len(subjects330) >= 1:
                                                        tmp333 = subjects330.popleft()
                                                        subst7 = Substitution(subst6)
                                                        try:
                                                            subst7.try_add_variable('i2.2.1.2', tmp333)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            # State 37306
                                                            if len(subjects330) == 0:
                                                                pass
                                                                # State 37307
                                                                subst8 = Substitution(subst7)
                                                                try:
                                                                    subst8.try_add_variable('i2.2.1.2.2.2', 1)
                                                                except ValueError:
                                                                    pass
                                                                else:
                                                                    pass
                                                                    # State 37308
                                                                    if len(subjects326) == 0:
                                                                        pass
                                                                        # State 37309
                                                                        subst9 = Substitution(subst8)
                                                                        try:
                                                                            subst9.try_add_variable('i2.2.1.2.2', 1)
                                                                        except ValueError:
                                                                            pass
                                                                        else:
                                                                            pass
                                                                            # State 37310
                                                                            if len(subjects297) == 0:
                                                                                pass
                                                                                # State 37311
                                                                                if len(subjects247) == 0:
                                                                                    pass
                                                                                    # State 37312
                                                                                    if len(subjects) == 0:
                                                                                        pass
                                                                                        # 47: b*log(c*(d*(x**j*f + e)**p)**q)
                                                                        if len(subjects297) >= 1:
                                                                            tmp337 = subjects297.popleft()
                                                                            subst9 = Substitution(subst8)
                                                                            try:
                                                                                subst9.try_add_variable('i2.2.1.2.2', tmp337)
                                                                            except ValueError:
                                                                                pass
                                                                            else:
                                                                                pass
                                                                                # State 37310
                                                                                if len(subjects297) == 0:
                                                                                    pass
                                                                                    # State 37311
                                                                                    if len(subjects247) == 0:
                                                                                        pass
                                                                                        # State 37312
                                                                                        if len(subjects) == 0:
                                                                                            pass
                                                                                            # 47: b*log(c*(d*(x**j*f + e)**p)**q)
                                                                            subjects297.appendleft(tmp337)
                                                                if len(subjects326) >= 1:
                                                                    tmp339 = subjects326.popleft()
                                                                    subst8 = Substitution(subst7)
                                                                    try:
                                                                        subst8.try_add_variable('i2.2.1.2.2.2', tmp339)
                                                                    except ValueError:
                                                                        pass
                                                                    else:
                                                                        pass
                                                                        # State 37308
                                                                        if len(subjects326) == 0:
                                                                            pass
                                                                            # State 37309
                                                                            subst9 = Substitution(subst8)
                                                                            try:
                                                                                subst9.try_add_variable('i2.2.1.2.2', 1)
                                                                            except ValueError:
                                                                                pass
                                                                            else:
                                                                                pass
                                                                                # State 37310
                                                                                if len(subjects297) == 0:
                                                                                    pass
                                                                                    # State 37311
                                                                                    if len(subjects247) == 0:
                                                                                        pass
                                                                                        # State 37312
                                                                                        if len(subjects) == 0:
                                                                                            pass
                                                                                            # 47: b*log(c*(d*(x**j*f + e)**p)**q)
                                                                            if len(subjects297) >= 1:
                                                                                tmp342 = subjects297.popleft()
                                                                                subst9 = Substitution(subst8)
                                                                                try:
                                                                                    subst9.try_add_variable('i2.2.1.2.2', tmp342)
                                                                                except ValueError:
                                                                                    pass
                                                                                else:
                                                                                    pass
                                                                                    # State 37310
                                                                                    if len(subjects297) == 0:
                                                                                        pass
                                                                                        # State 37311
                                                                                        if len(subjects247) == 0:
                                                                                            pass
                                                                                            # State 37312
                                                                                            if len(subjects) == 0:
                                                                                                pass
                                                                                                # 47: b*log(c*(d*(x**j*f + e)**p)**q)
                                                                                subjects297.appendleft(tmp342)
                                                                    subjects326.appendleft(tmp339)
                                                        subjects330.appendleft(tmp333)
                                                subjects330.appendleft(tmp331)
                                            subjects326.appendleft(tmp329)
                                    if len(subjects326) >= 1 and isinstance(subjects326[0], Mul):
                                        tmp344 = subjects326.popleft()
                                        associative1 = tmp344
                                        associative_type1 = type(tmp344)
                                        subjects345 = deque(tmp344._args)
                                        matcher = CommutativeMatcher37314.get()
                                        tmp346 = subjects345
                                        subjects345 = []
                                        for s in tmp346:
                                            matcher.add_subject(s)
                                        for pattern_index, subst5 in matcher.match(tmp346, subst4):
                                            pass
                                            if pattern_index == 0:
                                                pass
                                                # State 37319
                                                subst6 = Substitution(subst5)
                                                try:
                                                    subst6.try_add_variable('i2.2.1.2.2.2', 1)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 37320
                                                    if len(subjects326) == 0:
                                                        pass
                                                        # State 37321
                                                        subst7 = Substitution(subst6)
                                                        try:
                                                            subst7.try_add_variable('i2.2.1.2.2', 1)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            # State 37322
                                                            if len(subjects297) == 0:
                                                                pass
                                                                # State 37323
                                                                if len(subjects247) == 0:
                                                                    pass
                                                                    # State 37324
                                                                    if len(subjects) == 0:
                                                                        pass
                                                                        # 47: b*log(c*(d*(x**j*f + e)**p)**q)
                                                        if len(subjects297) >= 1:
                                                            tmp349 = subjects297.popleft()
                                                            subst7 = Substitution(subst6)
                                                            try:
                                                                subst7.try_add_variable('i2.2.1.2.2', tmp349)
                                                            except ValueError:
                                                                pass
                                                            else:
                                                                pass
                                                                # State 37322
                                                                if len(subjects297) == 0:
                                                                    pass
                                                                    # State 37323
                                                                    if len(subjects247) == 0:
                                                                        pass
                                                                        # State 37324
                                                                        if len(subjects) == 0:
                                                                            pass
                                                                            # 47: b*log(c*(d*(x**j*f + e)**p)**q)
                                                            subjects297.appendleft(tmp349)
                                                if len(subjects326) >= 1:
                                                    tmp351 = []
                                                    tmp351.append(subjects326.popleft())
                                                    while True:
                                                        if len(tmp351) > 1:
                                                            tmp352 = create_operation_expression(associative1, tmp351)
                                                        elif len(tmp351) == 1:
                                                            tmp352 = tmp351[0]
                                                        else:
                                                            assert False, "Unreachable"
                                                        subst6 = Substitution(subst5)
                                                        try:
                                                            subst6.try_add_variable('i2.2.1.2.2.2', tmp352)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            # State 37320
                                                            if len(subjects326) == 0:
                                                                pass
                                                                # State 37321
                                                                subst7 = Substitution(subst6)
                                                                try:
                                                                    subst7.try_add_variable('i2.2.1.2.2', 1)
                                                                except ValueError:
                                                                    pass
                                                                else:
                                                                    pass
                                                                    # State 37322
                                                                    if len(subjects297) == 0:
                                                                        pass
                                                                        # State 37323
                                                                        if len(subjects247) == 0:
                                                                            pass
                                                                            # State 37324
                                                                            if len(subjects) == 0:
                                                                                pass
                                                                                # 47: b*log(c*(d*(x**j*f + e)**p)**q)
                                                                if len(subjects297) >= 1:
                                                                    tmp355 = subjects297.popleft()
                                                                    subst7 = Substitution(subst6)
                                                                    try:
                                                                        subst7.try_add_variable('i2.2.1.2.2', tmp355)
                                                                    except ValueError:
                                                                        pass
                                                                    else:
                                                                        pass
                                                                        # State 37322
                                                                        if len(subjects297) == 0:
                                                                            pass
                                                                            # State 37323
                                                                            if len(subjects247) == 0:
                                                                                pass
                                                                                # State 37324
                                                                                if len(subjects) == 0:
                                                                                    pass
                                                                                    # 47: b*log(c*(d*(x**j*f + e)**p)**q)
                                                                    subjects297.appendleft(tmp355)
                                                        if len(subjects326) == 0:
                                                            break
                                                        tmp351.append(subjects326.popleft())
                                                    subjects326.extendleft(reversed(tmp351))
                                        subjects326.appendleft(tmp344)
                                if len(subjects326) >= 1 and isinstance(subjects326[0], Add):
                                    tmp357 = subjects326.popleft()
                                    associative1 = tmp357
                                    associative_type1 = type(tmp357)
                                    subjects358 = deque(tmp357._args)
                                    matcher = CommutativeMatcher37326.get()
                                    tmp359 = subjects358
                                    subjects358 = []
                                    for s in tmp359:
                                        matcher.add_subject(s)
                                    for pattern_index, subst4 in matcher.match(tmp359, subst3):
                                        pass
                                        if pattern_index == 0:
                                            pass
                                            # State 37339
                                            subst5 = Substitution(subst4)
                                            try:
                                                subst5.try_add_variable('i2.2.1.2.2.2', 1)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 37340
                                                if len(subjects326) == 0:
                                                    pass
                                                    # State 37341
                                                    subst6 = Substitution(subst5)
                                                    try:
                                                        subst6.try_add_variable('i2.2.1.2.2', 1)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 37342
                                                        if len(subjects297) == 0:
                                                            pass
                                                            # State 37343
                                                            if len(subjects247) == 0:
                                                                pass
                                                                # State 37344
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 47: b*log(c*(d*(x**j*f + e)**p)**q)
                                                    if len(subjects297) >= 1:
                                                        tmp362 = subjects297.popleft()
                                                        subst6 = Substitution(subst5)
                                                        try:
                                                            subst6.try_add_variable('i2.2.1.2.2', tmp362)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            # State 37342
                                                            if len(subjects297) == 0:
                                                                pass
                                                                # State 37343
                                                                if len(subjects247) == 0:
                                                                    pass
                                                                    # State 37344
                                                                    if len(subjects) == 0:
                                                                        pass
                                                                        # 47: b*log(c*(d*(x**j*f + e)**p)**q)
                                                        subjects297.appendleft(tmp362)
                                            if len(subjects326) >= 1:
                                                tmp364 = []
                                                tmp364.append(subjects326.popleft())
                                                while True:
                                                    if len(tmp364) > 1:
                                                        tmp365 = create_operation_expression(associative1, tmp364)
                                                    elif len(tmp364) == 1:
                                                        tmp365 = tmp364[0]
                                                    else:
                                                        assert False, "Unreachable"
                                                    subst5 = Substitution(subst4)
                                                    try:
                                                        subst5.try_add_variable('i2.2.1.2.2.2', tmp365)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 37340
                                                        if len(subjects326) == 0:
                                                            pass
                                                            # State 37341
                                                            subst6 = Substitution(subst5)
                                                            try:
                                                                subst6.try_add_variable('i2.2.1.2.2', 1)
                                                            except ValueError:
                                                                pass
                                                            else:
                                                                pass
                                                                # State 37342
                                                                if len(subjects297) == 0:
                                                                    pass
                                                                    # State 37343
                                                                    if len(subjects247) == 0:
                                                                        pass
                                                                        # State 37344
                                                                        if len(subjects) == 0:
                                                                            pass
                                                                            # 47: b*log(c*(d*(x**j*f + e)**p)**q)
                                                            if len(subjects297) >= 1:
                                                                tmp368 = subjects297.popleft()
                                                                subst6 = Substitution(subst5)
                                                                try:
                                                                    subst6.try_add_variable('i2.2.1.2.2', tmp368)
                                                                except ValueError:
                                                                    pass
                                                                else:
                                                                    pass
                                                                    # State 37342
                                                                    if len(subjects297) == 0:
                                                                        pass
                                                                        # State 37343
                                                                        if len(subjects247) == 0:
                                                                            pass
                                                                            # State 37344
                                                                            if len(subjects) == 0:
                                                                                pass
                                                                                # 47: b*log(c*(d*(x**j*f + e)**p)**q)
                                                                subjects297.appendleft(tmp368)
                                                    if len(subjects326) == 0:
                                                        break
                                                    tmp364.append(subjects326.popleft())
                                                subjects326.extendleft(reversed(tmp364))
                                    subjects326.appendleft(tmp357)
                                subjects297.appendleft(tmp325)
                        if len(subjects297) >= 1 and isinstance(subjects297[0], Mul):
                            tmp370 = subjects297.popleft()
                            associative1 = tmp370
                            associative_type1 = type(tmp370)
                            subjects371 = deque(tmp370._args)
                            matcher = CommutativeMatcher37346.get()
                            tmp372 = subjects371
                            subjects371 = []
                            for s in tmp372:
                                matcher.add_subject(s)
                            for pattern_index, subst3 in matcher.match(tmp372, subst2):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 37411
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i2.2.1.2.2', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 37412
                                        if len(subjects297) == 0:
                                            pass
                                            # State 37413
                                            if len(subjects247) == 0:
                                                pass
                                                # State 37414
                                                if len(subjects) == 0:
                                                    pass
                                                    # 47: b*log(c*(d*(x**j*f + e)**p)**q)
                                    if len(subjects297) >= 1:
                                        tmp374 = []
                                        tmp374.append(subjects297.popleft())
                                        while True:
                                            if len(tmp374) > 1:
                                                tmp375 = create_operation_expression(associative1, tmp374)
                                            elif len(tmp374) == 1:
                                                tmp375 = tmp374[0]
                                            else:
                                                assert False, "Unreachable"
                                            subst4 = Substitution(subst3)
                                            try:
                                                subst4.try_add_variable('i2.2.1.2.2', tmp375)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 37412
                                                if len(subjects297) == 0:
                                                    pass
                                                    # State 37413
                                                    if len(subjects247) == 0:
                                                        pass
                                                        # State 37414
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 47: b*log(c*(d*(x**j*f + e)**p)**q)
                                            if len(subjects297) == 0:
                                                break
                                            tmp374.append(subjects297.popleft())
                                        subjects297.extendleft(reversed(tmp374))
                            subjects297.appendleft(tmp370)
                        subjects247.appendleft(tmp296)
                if len(subjects247) >= 1 and isinstance(subjects247[0], Mul):
                    tmp377 = subjects247.popleft()
                    associative1 = tmp377
                    associative_type1 = type(tmp377)
                    subjects378 = deque(tmp377._args)
                    matcher = CommutativeMatcher37416.get()
                    tmp379 = subjects378
                    subjects378 = []
                    for s in tmp379:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp379, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 37697
                            if len(subjects247) == 0:
                                pass
                                # State 37698
                                if len(subjects) == 0:
                                    pass
                                    # 47: b*log(c*(d*(x**j*f + e)**p)**q)
                    subjects247.appendleft(tmp377)
                subjects.appendleft(tmp246)
            if len(subjects) >= 1 and isinstance(subjects[0], sin):
                tmp380 = subjects.popleft()
                subjects381 = deque(tmp380._args)
                # State 60157
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 60158
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.2.1.2.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 60159
                        if len(subjects381) >= 1:
                            tmp384 = subjects381.popleft()
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i2.2.1.2.1.0', tmp384)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 60160
                                if len(subjects381) == 0:
                                    pass
                                    # State 60161
                                    if len(subjects) == 0:
                                        pass
                                        # 52: d*sin(c + x*d)
                            subjects381.appendleft(tmp384)
                    if len(subjects381) >= 1 and isinstance(subjects381[0], Mul):
                        tmp386 = subjects381.popleft()
                        associative1 = tmp386
                        associative_type1 = type(tmp386)
                        subjects387 = deque(tmp386._args)
                        matcher = CommutativeMatcher60163.get()
                        tmp388 = subjects387
                        subjects387 = []
                        for s in tmp388:
                            matcher.add_subject(s)
                        for pattern_index, subst3 in matcher.match(tmp388, subst2):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 60164
                                if len(subjects381) == 0:
                                    pass
                                    # State 60165
                                    if len(subjects) == 0:
                                        pass
                                        # 52: d*sin(c + x*d)
                        subjects381.appendleft(tmp386)
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.3.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 61917
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.2.1.3.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 61918
                        if len(subjects381) >= 1:
                            tmp391 = subjects381.popleft()
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i2.2.1.3.1.0', tmp391)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 61919
                                if len(subjects381) == 0:
                                    pass
                                    # State 61920
                                    if len(subjects) == 0:
                                        pass
                                        # 56: b*sin(e + x*f)
                            subjects381.appendleft(tmp391)
                    if len(subjects381) >= 1 and isinstance(subjects381[0], Mul):
                        tmp393 = subjects381.popleft()
                        associative1 = tmp393
                        associative_type1 = type(tmp393)
                        subjects394 = deque(tmp393._args)
                        matcher = CommutativeMatcher61922.get()
                        tmp395 = subjects394
                        subjects394 = []
                        for s in tmp395:
                            matcher.add_subject(s)
                        for pattern_index, subst3 in matcher.match(tmp395, subst2):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 61923
                                if len(subjects381) == 0:
                                    pass
                                    # State 61924
                                    if len(subjects) == 0:
                                        pass
                                        # 56: b*sin(e + x*f)
                        subjects381.appendleft(tmp393)
                if len(subjects381) >= 1 and isinstance(subjects381[0], Add):
                    tmp396 = subjects381.popleft()
                    associative1 = tmp396
                    associative_type1 = type(tmp396)
                    subjects397 = deque(tmp396._args)
                    matcher = CommutativeMatcher60167.get()
                    tmp398 = subjects397
                    subjects397 = []
                    for s in tmp398:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp398, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 60173
                            if len(subjects381) == 0:
                                pass
                                # State 60174
                                if len(subjects) == 0:
                                    pass
                                    # 52: d*sin(c + x*d)
                        if pattern_index == 1:
                            pass
                            # State 61928
                            if len(subjects381) == 0:
                                pass
                                # State 61929
                                if len(subjects) == 0:
                                    pass
                                    # 56: b*sin(e + x*f)
                    subjects381.appendleft(tmp396)
                subjects.appendleft(tmp380)
            if len(subjects) >= 1 and isinstance(subjects[0], cos):
                tmp399 = subjects.popleft()
                subjects400 = deque(tmp399._args)
                # State 60215
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 60216
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.2.1.2.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 60217
                        if len(subjects400) >= 1:
                            tmp403 = subjects400.popleft()
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i2.2.1.2.1.0', tmp403)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 60218
                                if len(subjects400) == 0:
                                    pass
                                    # State 60219
                                    if len(subjects) == 0:
                                        pass
                                        # 53: d*cos(c + x*d)
                            subjects400.appendleft(tmp403)
                    if len(subjects400) >= 1 and isinstance(subjects400[0], Mul):
                        tmp405 = subjects400.popleft()
                        associative1 = tmp405
                        associative_type1 = type(tmp405)
                        subjects406 = deque(tmp405._args)
                        matcher = CommutativeMatcher60221.get()
                        tmp407 = subjects406
                        subjects406 = []
                        for s in tmp407:
                            matcher.add_subject(s)
                        for pattern_index, subst3 in matcher.match(tmp407, subst2):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 60222
                                if len(subjects400) == 0:
                                    pass
                                    # State 60223
                                    if len(subjects) == 0:
                                        pass
                                        # 53: d*cos(c + x*d)
                        subjects400.appendleft(tmp405)
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.3.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 62080
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.2.1.3.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 62081
                        if len(subjects400) >= 1:
                            tmp410 = subjects400.popleft()
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i2.2.1.3.1.0', tmp410)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 62082
                                if len(subjects400) == 0:
                                    pass
                                    # State 62083
                                    if len(subjects) == 0:
                                        pass
                                        # 57: b*cos(e + x*f)
                            subjects400.appendleft(tmp410)
                    if len(subjects400) >= 1 and isinstance(subjects400[0], Mul):
                        tmp412 = subjects400.popleft()
                        associative1 = tmp412
                        associative_type1 = type(tmp412)
                        subjects413 = deque(tmp412._args)
                        matcher = CommutativeMatcher62085.get()
                        tmp414 = subjects413
                        subjects413 = []
                        for s in tmp414:
                            matcher.add_subject(s)
                        for pattern_index, subst3 in matcher.match(tmp414, subst2):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 62086
                                if len(subjects400) == 0:
                                    pass
                                    # State 62087
                                    if len(subjects) == 0:
                                        pass
                                        # 57: b*cos(e + x*f)
                        subjects400.appendleft(tmp412)
                if len(subjects400) >= 1 and isinstance(subjects400[0], Add):
                    tmp415 = subjects400.popleft()
                    associative1 = tmp415
                    associative_type1 = type(tmp415)
                    subjects416 = deque(tmp415._args)
                    matcher = CommutativeMatcher60225.get()
                    tmp417 = subjects416
                    subjects416 = []
                    for s in tmp417:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp417, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 60231
                            if len(subjects400) == 0:
                                pass
                                # State 60232
                                if len(subjects) == 0:
                                    pass
                                    # 53: d*cos(c + x*d)
                        if pattern_index == 1:
                            pass
                            # State 62091
                            if len(subjects400) == 0:
                                pass
                                # State 62092
                                if len(subjects) == 0:
                                    pass
                                    # 57: b*cos(e + x*f)
                    subjects400.appendleft(tmp415)
                subjects.appendleft(tmp399)
            if len(subjects) >= 1 and isinstance(subjects[0], tan):
                tmp418 = subjects.popleft()
                subjects419 = deque(tmp418._args)
                # State 78655
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 78656
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.2.1.2.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 78657
                        if len(subjects419) >= 1:
                            tmp422 = subjects419.popleft()
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i2.2.1.2.1.0', tmp422)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 78658
                                if len(subjects419) == 0:
                                    pass
                                    # State 78659
                                    if len(subjects) == 0:
                                        pass
                                        # 77: d*tan(c + x*d)
                            subjects419.appendleft(tmp422)
                    if len(subjects419) >= 1 and isinstance(subjects419[0], Mul):
                        tmp424 = subjects419.popleft()
                        associative1 = tmp424
                        associative_type1 = type(tmp424)
                        subjects425 = deque(tmp424._args)
                        matcher = CommutativeMatcher78661.get()
                        tmp426 = subjects425
                        subjects425 = []
                        for s in tmp426:
                            matcher.add_subject(s)
                        for pattern_index, subst3 in matcher.match(tmp426, subst2):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 78662
                                if len(subjects419) == 0:
                                    pass
                                    # State 78663
                                    if len(subjects) == 0:
                                        pass
                                        # 77: d*tan(c + x*d)
                        subjects419.appendleft(tmp424)
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.3.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 81006
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.2.1.3.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 81007
                        if len(subjects419) >= 1:
                            tmp429 = subjects419.popleft()
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i2.2.1.3.1.0', tmp429)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 81008
                                if len(subjects419) == 0:
                                    pass
                                    # State 81009
                                    if len(subjects) == 0:
                                        pass
                                        # 82: b*tan(e + x*f)
                            subjects419.appendleft(tmp429)
                    if len(subjects419) >= 1 and isinstance(subjects419[0], Mul):
                        tmp431 = subjects419.popleft()
                        associative1 = tmp431
                        associative_type1 = type(tmp431)
                        subjects432 = deque(tmp431._args)
                        matcher = CommutativeMatcher81011.get()
                        tmp433 = subjects432
                        subjects432 = []
                        for s in tmp433:
                            matcher.add_subject(s)
                        for pattern_index, subst3 in matcher.match(tmp433, subst2):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 81012
                                if len(subjects419) == 0:
                                    pass
                                    # State 81013
                                    if len(subjects) == 0:
                                        pass
                                        # 82: b*tan(e + x*f)
                        subjects419.appendleft(tmp431)
                if len(subjects419) >= 1 and isinstance(subjects419[0], Add):
                    tmp434 = subjects419.popleft()
                    associative1 = tmp434
                    associative_type1 = type(tmp434)
                    subjects435 = deque(tmp434._args)
                    matcher = CommutativeMatcher78665.get()
                    tmp436 = subjects435
                    subjects435 = []
                    for s in tmp436:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp436, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 78671
                            if len(subjects419) == 0:
                                pass
                                # State 78672
                                if len(subjects) == 0:
                                    pass
                                    # 77: d*tan(c + x*d)
                        if pattern_index == 1:
                            pass
                            # State 81017
                            if len(subjects419) == 0:
                                pass
                                # State 81018
                                if len(subjects) == 0:
                                    pass
                                    # 82: b*tan(e + x*f)
                    subjects419.appendleft(tmp434)
                subjects.appendleft(tmp418)
            if len(subjects) >= 1 and isinstance(subjects[0], asin):
                tmp437 = subjects.popleft()
                subjects438 = deque(tmp437._args)
                # State 108834
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.0', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 108835
                    if len(subjects438) >= 1:
                        tmp440 = subjects438.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.1', tmp440)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 108836
                            if len(subjects438) == 0:
                                pass
                                # State 108837
                                if len(subjects) == 0:
                                    pass
                                    # 102: b*asin(x*c)
                        subjects438.appendleft(tmp440)
                    if len(subjects438) >= 1:
                        tmp442 = subjects438.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.0', tmp442)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 109240
                            if len(subjects438) == 0:
                                pass
                                # State 109241
                                if len(subjects) == 0:
                                    pass
                                    # 104: b*asin(x*c)
                        subjects438.appendleft(tmp442)
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 109853
                    if len(subjects438) >= 1:
                        tmp445 = subjects438.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.2.1.1', tmp445)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 109854
                            if len(subjects438) == 0:
                                pass
                                # State 109855
                                if len(subjects) == 0:
                                    pass
                                    # 110: b*asin(c*x)
                        subjects438.appendleft(tmp445)
                if len(subjects438) >= 1 and isinstance(subjects438[0], Mul):
                    tmp447 = subjects438.popleft()
                    associative1 = tmp447
                    associative_type1 = type(tmp447)
                    subjects448 = deque(tmp447._args)
                    matcher = CommutativeMatcher108839.get()
                    tmp449 = subjects448
                    subjects448 = []
                    for s in tmp449:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp449, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 108840
                            if len(subjects438) == 0:
                                pass
                                # State 108841
                                if len(subjects) == 0:
                                    pass
                                    # 102: b*asin(x*c)
                        if pattern_index == 1:
                            pass
                            # State 109242
                            if len(subjects438) == 0:
                                pass
                                # State 109243
                                if len(subjects) == 0:
                                    pass
                                    # 104: b*asin(x*c)
                        if pattern_index == 2:
                            pass
                            # State 109856
                            if len(subjects438) == 0:
                                pass
                                # State 109857
                                if len(subjects) == 0:
                                    pass
                                    # 110: b*asin(c*x)
                    subjects438.appendleft(tmp447)
                subjects.appendleft(tmp437)
            if len(subjects) >= 1 and isinstance(subjects[0], acos):
                tmp450 = subjects.popleft()
                subjects451 = deque(tmp450._args)
                # State 108876
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.0', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 108877
                    if len(subjects451) >= 1:
                        tmp453 = subjects451.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.1', tmp453)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 108878
                            if len(subjects451) == 0:
                                pass
                                # State 108879
                                if len(subjects) == 0:
                                    pass
                                    # 103: b*acos(x*c)
                        subjects451.appendleft(tmp453)
                    if len(subjects451) >= 1:
                        tmp455 = subjects451.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.0', tmp455)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 109274
                            if len(subjects451) == 0:
                                pass
                                # State 109275
                                if len(subjects) == 0:
                                    pass
                                    # 105: b*acos(x*c)
                        subjects451.appendleft(tmp455)
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 109909
                    if len(subjects451) >= 1:
                        tmp458 = subjects451.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.2.1.1', tmp458)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 109910
                            if len(subjects451) == 0:
                                pass
                                # State 109911
                                if len(subjects) == 0:
                                    pass
                                    # 111: b*acos(c*x)
                        subjects451.appendleft(tmp458)
                if len(subjects451) >= 1 and isinstance(subjects451[0], Mul):
                    tmp460 = subjects451.popleft()
                    associative1 = tmp460
                    associative_type1 = type(tmp460)
                    subjects461 = deque(tmp460._args)
                    matcher = CommutativeMatcher108881.get()
                    tmp462 = subjects461
                    subjects461 = []
                    for s in tmp462:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp462, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 108882
                            if len(subjects451) == 0:
                                pass
                                # State 108883
                                if len(subjects) == 0:
                                    pass
                                    # 103: b*acos(x*c)
                        if pattern_index == 1:
                            pass
                            # State 109276
                            if len(subjects451) == 0:
                                pass
                                # State 109277
                                if len(subjects) == 0:
                                    pass
                                    # 105: b*acos(x*c)
                        if pattern_index == 2:
                            pass
                            # State 109912
                            if len(subjects451) == 0:
                                pass
                                # State 109913
                                if len(subjects) == 0:
                                    pass
                                    # 111: b*acos(c*x)
                    subjects451.appendleft(tmp460)
                subjects.appendleft(tmp450)
            if len(subjects) >= 1 and isinstance(subjects[0], atan):
                tmp463 = subjects.popleft()
                subjects464 = deque(tmp463._args)
                # State 113485
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.0', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 113486
                    if len(subjects464) >= 1:
                        tmp466 = subjects464.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.1', tmp466)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 113487
                            if len(subjects464) == 0:
                                pass
                                # State 113488
                                if len(subjects) == 0:
                                    pass
                                    # 114: b*atan(x*c)
                        subjects464.appendleft(tmp466)
                if len(subjects464) >= 1 and isinstance(subjects464[0], Mul):
                    tmp468 = subjects464.popleft()
                    associative1 = tmp468
                    associative_type1 = type(tmp468)
                    subjects469 = deque(tmp468._args)
                    matcher = CommutativeMatcher113490.get()
                    tmp470 = subjects469
                    subjects469 = []
                    for s in tmp470:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp470, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 113491
                            if len(subjects464) == 0:
                                pass
                                # State 113492
                                if len(subjects) == 0:
                                    pass
                                    # 114: b*atan(x*c)
                    subjects464.appendleft(tmp468)
                subjects.appendleft(tmp463)
            if len(subjects) >= 1 and isinstance(subjects[0], acot):
                tmp471 = subjects.popleft()
                subjects472 = deque(tmp471._args)
                # State 113534
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.0', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 113535
                    if len(subjects472) >= 1:
                        tmp474 = subjects472.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.1', tmp474)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 113536
                            if len(subjects472) == 0:
                                pass
                                # State 113537
                                if len(subjects) == 0:
                                    pass
                                    # 115: b*acot(x*c)
                        subjects472.appendleft(tmp474)
                if len(subjects472) >= 1 and isinstance(subjects472[0], Mul):
                    tmp476 = subjects472.popleft()
                    associative1 = tmp476
                    associative_type1 = type(tmp476)
                    subjects477 = deque(tmp476._args)
                    matcher = CommutativeMatcher113539.get()
                    tmp478 = subjects477
                    subjects477 = []
                    for s in tmp478:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp478, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 113540
                            if len(subjects472) == 0:
                                pass
                                # State 113541
                                if len(subjects) == 0:
                                    pass
                                    # 115: b*acot(x*c)
                    subjects472.appendleft(tmp476)
                subjects.appendleft(tmp471)
            if len(subjects) >= 1 and isinstance(subjects[0], asec):
                tmp479 = subjects.popleft()
                subjects480 = deque(tmp479._args)
                # State 119956
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.0', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 119957
                    if len(subjects480) >= 1:
                        tmp482 = subjects480.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.1', tmp482)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 119958
                            if len(subjects480) == 0:
                                pass
                                # State 119959
                                if len(subjects) == 0:
                                    pass
                                    # 116: b*asec(x*c)
                        subjects480.appendleft(tmp482)
                if len(subjects480) >= 1 and isinstance(subjects480[0], Mul):
                    tmp484 = subjects480.popleft()
                    associative1 = tmp484
                    associative_type1 = type(tmp484)
                    subjects485 = deque(tmp484._args)
                    matcher = CommutativeMatcher119961.get()
                    tmp486 = subjects485
                    subjects485 = []
                    for s in tmp486:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp486, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 119962
                            if len(subjects480) == 0:
                                pass
                                # State 119963
                                if len(subjects) == 0:
                                    pass
                                    # 116: b*asec(x*c)
                    subjects480.appendleft(tmp484)
                subjects.appendleft(tmp479)
            if len(subjects) >= 1 and isinstance(subjects[0], acsc):
                tmp487 = subjects.popleft()
                subjects488 = deque(tmp487._args)
                # State 120034
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.0', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 120035
                    if len(subjects488) >= 1:
                        tmp490 = subjects488.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.1', tmp490)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 120036
                            if len(subjects488) == 0:
                                pass
                                # State 120037
                                if len(subjects) == 0:
                                    pass
                                    # 117: b*acsc(x*c)
                        subjects488.appendleft(tmp490)
                if len(subjects488) >= 1 and isinstance(subjects488[0], Mul):
                    tmp492 = subjects488.popleft()
                    associative1 = tmp492
                    associative_type1 = type(tmp492)
                    subjects493 = deque(tmp492._args)
                    matcher = CommutativeMatcher120039.get()
                    tmp494 = subjects493
                    subjects493 = []
                    for s in tmp494:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp494, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 120040
                            if len(subjects488) == 0:
                                pass
                                # State 120041
                                if len(subjects) == 0:
                                    pass
                                    # 117: b*acsc(x*c)
                    subjects488.appendleft(tmp492)
                subjects.appendleft(tmp487)
            if len(subjects) >= 1 and isinstance(subjects[0], acosh):
                tmp495 = subjects.popleft()
                subjects496 = deque(tmp495._args)
                # State 138494
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.0', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 138495
                    if len(subjects496) >= 1:
                        tmp498 = subjects496.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.1', tmp498)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 138496
                            if len(subjects496) == 0:
                                pass
                                # State 138497
                                if len(subjects) == 0:
                                    pass
                                    # 139: b*acosh(x*c)
                        subjects496.appendleft(tmp498)
                if len(subjects496) >= 1 and isinstance(subjects496[0], Mul):
                    tmp500 = subjects496.popleft()
                    associative1 = tmp500
                    associative_type1 = type(tmp500)
                    subjects501 = deque(tmp500._args)
                    matcher = CommutativeMatcher138499.get()
                    tmp502 = subjects501
                    subjects501 = []
                    for s in tmp502:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp502, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 138500
                            if len(subjects496) == 0:
                                pass
                                # State 138501
                                if len(subjects) == 0:
                                    pass
                                    # 139: b*acosh(x*c)
                    subjects496.appendleft(tmp500)
                subjects.appendleft(tmp495)
            if len(subjects) >= 1 and isinstance(subjects[0], asinh):
                tmp503 = subjects.popleft()
                subjects504 = deque(tmp503._args)
                # State 138577
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.0', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 138578
                    if len(subjects504) >= 1:
                        tmp506 = subjects504.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.1', tmp506)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 138579
                            if len(subjects504) == 0:
                                pass
                                # State 138580
                                if len(subjects) == 0:
                                    pass
                                    # 140: b*asinh(x*c)
                        subjects504.appendleft(tmp506)
                    if len(subjects504) >= 1:
                        tmp508 = subjects504.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.0', tmp508)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 139029
                            if len(subjects504) == 0:
                                pass
                                # State 139030
                                if len(subjects) == 0:
                                    pass
                                    # 141: b*asinh(x*c)
                        subjects504.appendleft(tmp508)
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 139616
                    if len(subjects504) >= 1:
                        tmp511 = subjects504.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.2.1.1', tmp511)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 139617
                            if len(subjects504) == 0:
                                pass
                                # State 139618
                                if len(subjects) == 0:
                                    pass
                                    # 142: b*asinh(c*x)
                        subjects504.appendleft(tmp511)
                if len(subjects504) >= 1 and isinstance(subjects504[0], Mul):
                    tmp513 = subjects504.popleft()
                    associative1 = tmp513
                    associative_type1 = type(tmp513)
                    subjects514 = deque(tmp513._args)
                    matcher = CommutativeMatcher138582.get()
                    tmp515 = subjects514
                    subjects514 = []
                    for s in tmp515:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp515, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 138583
                            if len(subjects504) == 0:
                                pass
                                # State 138584
                                if len(subjects) == 0:
                                    pass
                                    # 140: b*asinh(x*c)
                        if pattern_index == 1:
                            pass
                            # State 139031
                            if len(subjects504) == 0:
                                pass
                                # State 139032
                                if len(subjects) == 0:
                                    pass
                                    # 141: b*asinh(x*c)
                        if pattern_index == 2:
                            pass
                            # State 139619
                            if len(subjects504) == 0:
                                pass
                                # State 139620
                                if len(subjects) == 0:
                                    pass
                                    # 142: b*asinh(c*x)
                    subjects504.appendleft(tmp513)
                subjects.appendleft(tmp503)
            if len(subjects) >= 1 and isinstance(subjects[0], atanh):
                tmp516 = subjects.popleft()
                subjects517 = deque(tmp516._args)
                # State 143110
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.0', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 143111
                    if len(subjects517) >= 1:
                        tmp519 = subjects517.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.1', tmp519)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 143112
                            if len(subjects517) == 0:
                                pass
                                # State 143113
                                if len(subjects) == 0:
                                    pass
                                    # 144: b*atanh(x*c)
                        subjects517.appendleft(tmp519)
                if len(subjects517) >= 1 and isinstance(subjects517[0], Mul):
                    tmp521 = subjects517.popleft()
                    associative1 = tmp521
                    associative_type1 = type(tmp521)
                    subjects522 = deque(tmp521._args)
                    matcher = CommutativeMatcher143115.get()
                    tmp523 = subjects522
                    subjects522 = []
                    for s in tmp523:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp523, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 143116
                            if len(subjects517) == 0:
                                pass
                                # State 143117
                                if len(subjects) == 0:
                                    pass
                                    # 144: b*atanh(x*c)
                    subjects517.appendleft(tmp521)
                subjects.appendleft(tmp516)
            if len(subjects) >= 1 and isinstance(subjects[0], acoth):
                tmp524 = subjects.popleft()
                subjects525 = deque(tmp524._args)
                # State 143159
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.0', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 143160
                    if len(subjects525) >= 1:
                        tmp527 = subjects525.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.1', tmp527)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 143161
                            if len(subjects525) == 0:
                                pass
                                # State 143162
                                if len(subjects) == 0:
                                    pass
                                    # 145: b*acoth(x*c)
                        subjects525.appendleft(tmp527)
                if len(subjects525) >= 1 and isinstance(subjects525[0], Mul):
                    tmp529 = subjects525.popleft()
                    associative1 = tmp529
                    associative_type1 = type(tmp529)
                    subjects530 = deque(tmp529._args)
                    matcher = CommutativeMatcher143164.get()
                    tmp531 = subjects530
                    subjects530 = []
                    for s in tmp531:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp531, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 143165
                            if len(subjects525) == 0:
                                pass
                                # State 143166
                                if len(subjects) == 0:
                                    pass
                                    # 145: b*acoth(x*c)
                    subjects525.appendleft(tmp529)
                subjects.appendleft(tmp524)
            if len(subjects) >= 1 and isinstance(subjects[0], asech):
                tmp532 = subjects.popleft()
                subjects533 = deque(tmp532._args)
                # State 149132
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.0', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 149133
                    if len(subjects533) >= 1:
                        tmp535 = subjects533.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.1', tmp535)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 149134
                            if len(subjects533) == 0:
                                pass
                                # State 149135
                                if len(subjects) == 0:
                                    pass
                                    # 146: b*asech(x*c)
                        subjects533.appendleft(tmp535)
                if len(subjects533) >= 1 and isinstance(subjects533[0], Mul):
                    tmp537 = subjects533.popleft()
                    associative1 = tmp537
                    associative_type1 = type(tmp537)
                    subjects538 = deque(tmp537._args)
                    matcher = CommutativeMatcher149137.get()
                    tmp539 = subjects538
                    subjects538 = []
                    for s in tmp539:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp539, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 149138
                            if len(subjects533) == 0:
                                pass
                                # State 149139
                                if len(subjects) == 0:
                                    pass
                                    # 146: b*asech(x*c)
                    subjects533.appendleft(tmp537)
                subjects.appendleft(tmp532)
            if len(subjects) >= 1 and isinstance(subjects[0], acsch):
                tmp540 = subjects.popleft()
                subjects541 = deque(tmp540._args)
                # State 149210
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.0', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 149211
                    if len(subjects541) >= 1:
                        tmp543 = subjects541.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.1', tmp543)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 149212
                            if len(subjects541) == 0:
                                pass
                                # State 149213
                                if len(subjects) == 0:
                                    pass
                                    # 147: b*acsch(x*c)
                        subjects541.appendleft(tmp543)
                if len(subjects541) >= 1 and isinstance(subjects541[0], Mul):
                    tmp545 = subjects541.popleft()
                    associative1 = tmp545
                    associative_type1 = type(tmp545)
                    subjects546 = deque(tmp545._args)
                    matcher = CommutativeMatcher149215.get()
                    tmp547 = subjects546
                    subjects546 = []
                    for s in tmp547:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp547, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 149216
                            if len(subjects541) == 0:
                                pass
                                # State 149217
                                if len(subjects) == 0:
                                    pass
                                    # 147: b*acsch(x*c)
                    subjects541.appendleft(tmp545)
                subjects.appendleft(tmp540)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.0', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 3263
            if len(subjects) >= 1:
                tmp549 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.0', tmp549)
                except ValueError:
                    pass
                else:
                    pass
                    # State 3264
                    if len(subjects) == 0:
                        pass
                        # 2: x*d
                subjects.appendleft(tmp549)
            subst2 = Substitution(subst1)
            try:
                subst2.try_add_variable('i2.2.1.2', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 7216
                if len(subjects) >= 1:
                    tmp552 = subjects.popleft()
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.2.0', tmp552)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 7217
                        if len(subjects) == 0:
                            pass
                            # 14: x**non2*b1
                    subjects.appendleft(tmp552)
                if len(subjects) >= 1:
                    tmp554 = subjects.popleft()
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.2.0_1', tmp554)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 7464
                        if len(subjects) == 0:
                            pass
                            # 16: x**mn*d
                    subjects.appendleft(tmp554)
            if len(subjects) >= 1:
                tmp556 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.3.1.1.0', tmp556)
                except ValueError:
                    pass
                else:
                    pass
                    # State 14651
                    if len(subjects) == 0:
                        pass
                        # 39: d*x
                subjects.appendleft(tmp556)
            subst2 = Substitution(subst1)
            try:
                subst2.try_add_variable('i2.4', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 15750
                if len(subjects) >= 1 and isinstance(subjects[0], Pow):
                    tmp559 = subjects.popleft()
                    subjects560 = deque(tmp559._args)
                    # State 15751
                    if len(subjects560) >= 1:
                        tmp561 = subjects560.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2', tmp561)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 15752
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i2.4.0', S(1))
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 15753
                                subst5 = Substitution(subst4)
                                try:
                                    subst5.try_add_variable('i2.4.1.0', S(0))
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 15754
                                    subst6 = Substitution(subst5)
                                    try:
                                        subst6.try_add_variable('i2.4.1.1.0_1', S(1))
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 15755
                                        if len(subjects560) >= 1:
                                            tmp566 = subjects560.popleft()
                                            subst7 = Substitution(subst6)
                                            try:
                                                subst7.try_add_variable('i2.4.1.1.0', tmp566)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 15756
                                                if len(subjects560) == 0:
                                                    pass
                                                    # State 15757
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 42: b*(F**(g*(e + x*f)))**n
                                            subjects560.appendleft(tmp566)
                                    if len(subjects560) >= 1 and isinstance(subjects560[0], Mul):
                                        tmp568 = subjects560.popleft()
                                        associative1 = tmp568
                                        associative_type1 = type(tmp568)
                                        subjects569 = deque(tmp568._args)
                                        matcher = CommutativeMatcher15759.get()
                                        tmp570 = subjects569
                                        subjects569 = []
                                        for s in tmp570:
                                            matcher.add_subject(s)
                                        for pattern_index, subst6 in matcher.match(tmp570, subst5):
                                            pass
                                            if pattern_index == 0:
                                                pass
                                                # State 15760
                                                if len(subjects560) == 0:
                                                    pass
                                                    # State 15761
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 42: b*(F**(g*(e + x*f)))**n
                                        subjects560.appendleft(tmp568)
                                if len(subjects560) >= 1 and isinstance(subjects560[0], Add):
                                    tmp571 = subjects560.popleft()
                                    associative1 = tmp571
                                    associative_type1 = type(tmp571)
                                    subjects572 = deque(tmp571._args)
                                    matcher = CommutativeMatcher15763.get()
                                    tmp573 = subjects572
                                    subjects572 = []
                                    for s in tmp573:
                                        matcher.add_subject(s)
                                    for pattern_index, subst5 in matcher.match(tmp573, subst4):
                                        pass
                                        if pattern_index == 0:
                                            pass
                                            # State 15769
                                            if len(subjects560) == 0:
                                                pass
                                                # State 15770
                                                if len(subjects) == 0:
                                                    pass
                                                    # 42: b*(F**(g*(e + x*f)))**n
                                    subjects560.appendleft(tmp571)
                            if len(subjects560) >= 1 and isinstance(subjects560[0], Mul):
                                tmp574 = subjects560.popleft()
                                associative1 = tmp574
                                associative_type1 = type(tmp574)
                                subjects575 = deque(tmp574._args)
                                matcher = CommutativeMatcher15772.get()
                                tmp576 = subjects575
                                subjects575 = []
                                for s in tmp576:
                                    matcher.add_subject(s)
                                for pattern_index, subst4 in matcher.match(tmp576, subst3):
                                    pass
                                    if pattern_index == 0:
                                        pass
                                        # State 15787
                                        if len(subjects560) == 0:
                                            pass
                                            # State 15788
                                            if len(subjects) == 0:
                                                pass
                                                # 42: b*(F**(g*(e + x*f)))**n
                                subjects560.appendleft(tmp574)
                        subjects560.appendleft(tmp561)
                    subjects.appendleft(tmp559)
            subst2 = Substitution(subst1)
            try:
                subst2.try_add_variable('i2.2.1.4', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 16305
                if len(subjects) >= 1 and isinstance(subjects[0], Pow):
                    tmp578 = subjects.popleft()
                    subjects579 = deque(tmp578._args)
                    # State 16306
                    if len(subjects579) >= 1:
                        tmp580 = subjects579.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.2', tmp580)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 16307
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i2.2.1.4.0', S(1))
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 16308
                                subst5 = Substitution(subst4)
                                try:
                                    subst5.try_add_variable('i2.2.1.4.1.0', S(0))
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 16309
                                    subst6 = Substitution(subst5)
                                    try:
                                        subst6.try_add_variable('i2.2.1.4.1.1.0', S(1))
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 16310
                                        if len(subjects579) >= 1:
                                            tmp585 = subjects579.popleft()
                                            subst7 = Substitution(subst6)
                                            try:
                                                subst7.try_add_variable('i2.2.3.1.1.0', tmp585)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 16311
                                                if len(subjects579) == 0:
                                                    pass
                                                    # State 16312
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 43: b*(F**(g*(e + f*x)))**n
                                            subjects579.appendleft(tmp585)
                                    if len(subjects579) >= 1 and isinstance(subjects579[0], Mul):
                                        tmp587 = subjects579.popleft()
                                        associative1 = tmp587
                                        associative_type1 = type(tmp587)
                                        subjects588 = deque(tmp587._args)
                                        matcher = CommutativeMatcher16314.get()
                                        tmp589 = subjects588
                                        subjects588 = []
                                        for s in tmp589:
                                            matcher.add_subject(s)
                                        for pattern_index, subst6 in matcher.match(tmp589, subst5):
                                            pass
                                            if pattern_index == 0:
                                                pass
                                                # State 16315
                                                if len(subjects579) == 0:
                                                    pass
                                                    # State 16316
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 43: b*(F**(g*(e + f*x)))**n
                                        subjects579.appendleft(tmp587)
                                if len(subjects579) >= 1 and isinstance(subjects579[0], Add):
                                    tmp590 = subjects579.popleft()
                                    associative1 = tmp590
                                    associative_type1 = type(tmp590)
                                    subjects591 = deque(tmp590._args)
                                    matcher = CommutativeMatcher16318.get()
                                    tmp592 = subjects591
                                    subjects591 = []
                                    for s in tmp592:
                                        matcher.add_subject(s)
                                    for pattern_index, subst5 in matcher.match(tmp592, subst4):
                                        pass
                                        if pattern_index == 0:
                                            pass
                                            # State 16324
                                            if len(subjects579) == 0:
                                                pass
                                                # State 16325
                                                if len(subjects) == 0:
                                                    pass
                                                    # 43: b*(F**(g*(e + f*x)))**n
                                    subjects579.appendleft(tmp590)
                            if len(subjects579) >= 1 and isinstance(subjects579[0], Mul):
                                tmp593 = subjects579.popleft()
                                associative1 = tmp593
                                associative_type1 = type(tmp593)
                                subjects594 = deque(tmp593._args)
                                matcher = CommutativeMatcher16327.get()
                                tmp595 = subjects594
                                subjects594 = []
                                for s in tmp595:
                                    matcher.add_subject(s)
                                for pattern_index, subst4 in matcher.match(tmp595, subst3):
                                    pass
                                    if pattern_index == 0:
                                        pass
                                        # State 16342
                                        if len(subjects579) == 0:
                                            pass
                                            # State 16343
                                            if len(subjects) == 0:
                                                pass
                                                # 43: b*(F**(g*(e + f*x)))**n
                                subjects579.appendleft(tmp593)
                        subjects579.appendleft(tmp580)
                    subjects.appendleft(tmp578)
            if len(subjects) >= 1:
                tmp596 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.2.1.0', tmp596)
                except ValueError:
                    pass
                else:
                    pass
                    # State 72131
                    if len(subjects) == 0:
                        pass
                        # 62: d*x
                subjects.appendleft(tmp596)
            if len(subjects) >= 1:
                tmp598 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.3.1.0', tmp598)
                except ValueError:
                    pass
                else:
                    pass
                    # State 86707
                    if len(subjects) == 0:
                        pass
                        # 83: d*x
                subjects.appendleft(tmp598)
            if len(subjects) >= 1 and isinstance(subjects[0], Pow):
                tmp600 = subjects.popleft()
                subjects601 = deque(tmp600._args)
                # State 5248
                if len(subjects601) >= 1:
                    tmp602 = subjects601.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.0', tmp602)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 5249
                        if len(subjects601) >= 1 and subjects601[0] == 2:
                            tmp604 = subjects601.popleft()
                            # State 5250
                            if len(subjects601) == 0:
                                pass
                                # State 5251
                                if len(subjects) == 0:
                                    pass
                                    # 7: v**2*c
                            subjects601.appendleft(tmp604)
                        if len(subjects601) >= 1:
                            tmp605 = subjects601.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.2', tmp605)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 6551
                                if len(subjects601) == 0:
                                    pass
                                    # State 6552
                                    if len(subjects) == 0:
                                        pass
                                        # 11: x**n*b1
                            subjects601.appendleft(tmp605)
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.2', 1)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 7218
                            if len(subjects601) == 0:
                                pass
                                # State 7219
                                if len(subjects) == 0:
                                    pass
                                    # 14: x**non2*b1
                        if len(subjects601) >= 1:
                            tmp608 = subjects601.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.2', tmp608)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 7218
                                if len(subjects601) == 0:
                                    pass
                                    # State 7219
                                    if len(subjects) == 0:
                                        pass
                                        # 14: x**non2*b1
                            subjects601.appendleft(tmp608)
                    subjects601.appendleft(tmp602)
                if len(subjects601) >= 1:
                    tmp610 = subjects601.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.0_1', tmp610)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 7170
                        if len(subjects601) >= 1:
                            tmp612 = subjects601.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.2', tmp612)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 7171
                                if len(subjects601) == 0:
                                    pass
                                    # State 7172
                                    if len(subjects) == 0:
                                        pass
                                        # 13: x**n*b
                            subjects601.appendleft(tmp612)
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.2', 1)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 7465
                            if len(subjects601) == 0:
                                pass
                                # State 7466
                                if len(subjects) == 0:
                                    pass
                                    # 16: x**mn*d
                        if len(subjects601) >= 1:
                            tmp615 = subjects601.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.2', tmp615)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 7465
                                if len(subjects601) == 0:
                                    pass
                                    # State 7466
                                    if len(subjects) == 0:
                                        pass
                                        # 16: x**mn*d
                            subjects601.appendleft(tmp615)
                    subjects601.appendleft(tmp610)
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.0', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 10766
                    if len(subjects601) >= 1 and isinstance(subjects601[0], Pow):
                        tmp618 = subjects601.popleft()
                        subjects619 = deque(tmp618._args)
                        # State 10767
                        if len(subjects619) >= 1:
                            tmp620 = subjects619.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.0', tmp620)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 10768
                                if len(subjects619) >= 1 and subjects619[0] == -1:
                                    tmp622 = subjects619.popleft()
                                    # State 10769
                                    if len(subjects619) == 0:
                                        pass
                                        # State 10770
                                        if len(subjects601) >= 1:
                                            tmp623 = subjects601.popleft()
                                            subst4 = Substitution(subst3)
                                            try:
                                                subst4.try_add_variable('i2.2.1.2', tmp623)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 10771
                                                if len(subjects601) == 0:
                                                    pass
                                                    # State 10772
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 31: b*(c/x)**n
                                            subjects601.appendleft(tmp623)
                                    subjects619.appendleft(tmp622)
                            subjects619.appendleft(tmp620)
                        subjects601.appendleft(tmp618)
                if len(subjects601) >= 1 and isinstance(subjects601[0], Mul):
                    tmp625 = subjects601.popleft()
                    associative1 = tmp625
                    associative_type1 = type(tmp625)
                    subjects626 = deque(tmp625._args)
                    matcher = CommutativeMatcher10774.get()
                    tmp627 = subjects626
                    subjects626 = []
                    for s in tmp627:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp627, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 10779
                            if len(subjects601) >= 1:
                                tmp628 = []
                                tmp628.append(subjects601.popleft())
                                while True:
                                    if len(tmp628) > 1:
                                        tmp629 = create_operation_expression(associative1, tmp628)
                                    elif len(tmp628) == 1:
                                        tmp629 = tmp628[0]
                                    else:
                                        assert False, "Unreachable"
                                    subst3 = Substitution(subst2)
                                    try:
                                        subst3.try_add_variable('i2.2.1.2', tmp629)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 10780
                                        if len(subjects601) == 0:
                                            pass
                                            # State 10781
                                            if len(subjects) == 0:
                                                pass
                                                # 31: b*(c/x)**n
                                    if len(subjects601) == 0:
                                        break
                                    tmp628.append(subjects601.popleft())
                                subjects601.extendleft(reversed(tmp628))
                    subjects601.appendleft(tmp625)
                if len(subjects601) >= 1 and isinstance(subjects601[0], Pow):
                    tmp631 = subjects601.popleft()
                    subjects632 = deque(tmp631._args)
                    # State 15789
                    if len(subjects632) >= 1:
                        tmp633 = subjects632.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2', tmp633)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 15790
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.4.0', S(1))
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 15791
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.4.1.0', S(0))
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 15792
                                    subst5 = Substitution(subst4)
                                    try:
                                        subst5.try_add_variable('i2.4.1.1.0_1', S(1))
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 15793
                                        if len(subjects632) >= 1:
                                            tmp638 = subjects632.popleft()
                                            subst6 = Substitution(subst5)
                                            try:
                                                subst6.try_add_variable('i2.4.1.1.0', tmp638)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 15794
                                                if len(subjects632) == 0:
                                                    pass
                                                    # State 15795
                                                    subst7 = Substitution(subst6)
                                                    try:
                                                        subst7.try_add_variable('i2.4', 1)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 15796
                                                        if len(subjects601) == 0:
                                                            pass
                                                            # State 15797
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 42: b*(F**(g*(e + x*f)))**n
                                                    if len(subjects601) >= 1:
                                                        tmp641 = subjects601.popleft()
                                                        subst7 = Substitution(subst6)
                                                        try:
                                                            subst7.try_add_variable('i2.4', tmp641)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            # State 15796
                                                            if len(subjects601) == 0:
                                                                pass
                                                                # State 15797
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 42: b*(F**(g*(e + x*f)))**n
                                                        subjects601.appendleft(tmp641)
                                            subjects632.appendleft(tmp638)
                                    if len(subjects632) >= 1 and isinstance(subjects632[0], Mul):
                                        tmp643 = subjects632.popleft()
                                        associative1 = tmp643
                                        associative_type1 = type(tmp643)
                                        subjects644 = deque(tmp643._args)
                                        matcher = CommutativeMatcher15799.get()
                                        tmp645 = subjects644
                                        subjects644 = []
                                        for s in tmp645:
                                            matcher.add_subject(s)
                                        for pattern_index, subst5 in matcher.match(tmp645, subst4):
                                            pass
                                            if pattern_index == 0:
                                                pass
                                                # State 15800
                                                if len(subjects632) == 0:
                                                    pass
                                                    # State 15801
                                                    subst6 = Substitution(subst5)
                                                    try:
                                                        subst6.try_add_variable('i2.4', 1)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 15802
                                                        if len(subjects601) == 0:
                                                            pass
                                                            # State 15803
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 42: b*(F**(g*(e + x*f)))**n
                                                    if len(subjects601) >= 1:
                                                        tmp647 = subjects601.popleft()
                                                        subst6 = Substitution(subst5)
                                                        try:
                                                            subst6.try_add_variable('i2.4', tmp647)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            # State 15802
                                                            if len(subjects601) == 0:
                                                                pass
                                                                # State 15803
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 42: b*(F**(g*(e + x*f)))**n
                                                        subjects601.appendleft(tmp647)
                                        subjects632.appendleft(tmp643)
                                if len(subjects632) >= 1 and isinstance(subjects632[0], Add):
                                    tmp649 = subjects632.popleft()
                                    associative1 = tmp649
                                    associative_type1 = type(tmp649)
                                    subjects650 = deque(tmp649._args)
                                    matcher = CommutativeMatcher15805.get()
                                    tmp651 = subjects650
                                    subjects650 = []
                                    for s in tmp651:
                                        matcher.add_subject(s)
                                    for pattern_index, subst4 in matcher.match(tmp651, subst3):
                                        pass
                                        if pattern_index == 0:
                                            pass
                                            # State 15811
                                            if len(subjects632) == 0:
                                                pass
                                                # State 15812
                                                subst5 = Substitution(subst4)
                                                try:
                                                    subst5.try_add_variable('i2.4', 1)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 15813
                                                    if len(subjects601) == 0:
                                                        pass
                                                        # State 15814
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 42: b*(F**(g*(e + x*f)))**n
                                                if len(subjects601) >= 1:
                                                    tmp653 = subjects601.popleft()
                                                    subst5 = Substitution(subst4)
                                                    try:
                                                        subst5.try_add_variable('i2.4', tmp653)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 15813
                                                        if len(subjects601) == 0:
                                                            pass
                                                            # State 15814
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 42: b*(F**(g*(e + x*f)))**n
                                                    subjects601.appendleft(tmp653)
                                    subjects632.appendleft(tmp649)
                            if len(subjects632) >= 1 and isinstance(subjects632[0], Mul):
                                tmp655 = subjects632.popleft()
                                associative1 = tmp655
                                associative_type1 = type(tmp655)
                                subjects656 = deque(tmp655._args)
                                matcher = CommutativeMatcher15816.get()
                                tmp657 = subjects656
                                subjects656 = []
                                for s in tmp657:
                                    matcher.add_subject(s)
                                for pattern_index, subst3 in matcher.match(tmp657, subst2):
                                    pass
                                    if pattern_index == 0:
                                        pass
                                        # State 15831
                                        if len(subjects632) == 0:
                                            pass
                                            # State 15832
                                            subst4 = Substitution(subst3)
                                            try:
                                                subst4.try_add_variable('i2.4', 1)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 15833
                                                if len(subjects601) == 0:
                                                    pass
                                                    # State 15834
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 42: b*(F**(g*(e + x*f)))**n
                                            if len(subjects601) >= 1:
                                                tmp659 = subjects601.popleft()
                                                subst4 = Substitution(subst3)
                                                try:
                                                    subst4.try_add_variable('i2.4', tmp659)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 15833
                                                    if len(subjects601) == 0:
                                                        pass
                                                        # State 15834
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 42: b*(F**(g*(e + x*f)))**n
                                                subjects601.appendleft(tmp659)
                                subjects632.appendleft(tmp655)
                        subjects632.appendleft(tmp633)
                    if len(subjects632) >= 1:
                        tmp661 = subjects632.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.1.2', tmp661)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 16344
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.4.0', S(1))
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 16345
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.2.1.4.1.0', S(0))
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 16346
                                    subst5 = Substitution(subst4)
                                    try:
                                        subst5.try_add_variable('i2.2.1.4.1.1.0', S(1))
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 16347
                                        if len(subjects632) >= 1:
                                            tmp666 = subjects632.popleft()
                                            subst6 = Substitution(subst5)
                                            try:
                                                subst6.try_add_variable('i2.2.3.1.1.0', tmp666)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 16348
                                                if len(subjects632) == 0:
                                                    pass
                                                    # State 16349
                                                    subst7 = Substitution(subst6)
                                                    try:
                                                        subst7.try_add_variable('i2.2.1.4', 1)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 16350
                                                        if len(subjects601) == 0:
                                                            pass
                                                            # State 16351
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 43: b*(F**(g*(e + f*x)))**n
                                                    if len(subjects601) >= 1:
                                                        tmp669 = subjects601.popleft()
                                                        subst7 = Substitution(subst6)
                                                        try:
                                                            subst7.try_add_variable('i2.2.1.4', tmp669)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            # State 16350
                                                            if len(subjects601) == 0:
                                                                pass
                                                                # State 16351
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 43: b*(F**(g*(e + f*x)))**n
                                                        subjects601.appendleft(tmp669)
                                            subjects632.appendleft(tmp666)
                                    if len(subjects632) >= 1 and isinstance(subjects632[0], Mul):
                                        tmp671 = subjects632.popleft()
                                        associative1 = tmp671
                                        associative_type1 = type(tmp671)
                                        subjects672 = deque(tmp671._args)
                                        matcher = CommutativeMatcher16353.get()
                                        tmp673 = subjects672
                                        subjects672 = []
                                        for s in tmp673:
                                            matcher.add_subject(s)
                                        for pattern_index, subst5 in matcher.match(tmp673, subst4):
                                            pass
                                            if pattern_index == 0:
                                                pass
                                                # State 16354
                                                if len(subjects632) == 0:
                                                    pass
                                                    # State 16355
                                                    subst6 = Substitution(subst5)
                                                    try:
                                                        subst6.try_add_variable('i2.2.1.4', 1)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 16356
                                                        if len(subjects601) == 0:
                                                            pass
                                                            # State 16357
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 43: b*(F**(g*(e + f*x)))**n
                                                    if len(subjects601) >= 1:
                                                        tmp675 = subjects601.popleft()
                                                        subst6 = Substitution(subst5)
                                                        try:
                                                            subst6.try_add_variable('i2.2.1.4', tmp675)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            # State 16356
                                                            if len(subjects601) == 0:
                                                                pass
                                                                # State 16357
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 43: b*(F**(g*(e + f*x)))**n
                                                        subjects601.appendleft(tmp675)
                                        subjects632.appendleft(tmp671)
                                if len(subjects632) >= 1 and isinstance(subjects632[0], Add):
                                    tmp677 = subjects632.popleft()
                                    associative1 = tmp677
                                    associative_type1 = type(tmp677)
                                    subjects678 = deque(tmp677._args)
                                    matcher = CommutativeMatcher16359.get()
                                    tmp679 = subjects678
                                    subjects678 = []
                                    for s in tmp679:
                                        matcher.add_subject(s)
                                    for pattern_index, subst4 in matcher.match(tmp679, subst3):
                                        pass
                                        if pattern_index == 0:
                                            pass
                                            # State 16365
                                            if len(subjects632) == 0:
                                                pass
                                                # State 16366
                                                subst5 = Substitution(subst4)
                                                try:
                                                    subst5.try_add_variable('i2.2.1.4', 1)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 16367
                                                    if len(subjects601) == 0:
                                                        pass
                                                        # State 16368
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 43: b*(F**(g*(e + f*x)))**n
                                                if len(subjects601) >= 1:
                                                    tmp681 = subjects601.popleft()
                                                    subst5 = Substitution(subst4)
                                                    try:
                                                        subst5.try_add_variable('i2.2.1.4', tmp681)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 16367
                                                        if len(subjects601) == 0:
                                                            pass
                                                            # State 16368
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 43: b*(F**(g*(e + f*x)))**n
                                                    subjects601.appendleft(tmp681)
                                    subjects632.appendleft(tmp677)
                            if len(subjects632) >= 1 and isinstance(subjects632[0], Mul):
                                tmp683 = subjects632.popleft()
                                associative1 = tmp683
                                associative_type1 = type(tmp683)
                                subjects684 = deque(tmp683._args)
                                matcher = CommutativeMatcher16370.get()
                                tmp685 = subjects684
                                subjects684 = []
                                for s in tmp685:
                                    matcher.add_subject(s)
                                for pattern_index, subst3 in matcher.match(tmp685, subst2):
                                    pass
                                    if pattern_index == 0:
                                        pass
                                        # State 16385
                                        if len(subjects632) == 0:
                                            pass
                                            # State 16386
                                            subst4 = Substitution(subst3)
                                            try:
                                                subst4.try_add_variable('i2.2.1.4', 1)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 16387
                                                if len(subjects601) == 0:
                                                    pass
                                                    # State 16388
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 43: b*(F**(g*(e + f*x)))**n
                                            if len(subjects601) >= 1:
                                                tmp687 = subjects601.popleft()
                                                subst4 = Substitution(subst3)
                                                try:
                                                    subst4.try_add_variable('i2.2.1.4', tmp687)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 16387
                                                    if len(subjects601) == 0:
                                                        pass
                                                        # State 16388
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 43: b*(F**(g*(e + f*x)))**n
                                                subjects601.appendleft(tmp687)
                                subjects632.appendleft(tmp683)
                        subjects632.appendleft(tmp661)
                    subjects601.appendleft(tmp631)
                if len(subjects601) >= 1 and isinstance(subjects601[0], sin):
                    tmp689 = subjects601.popleft()
                    subjects690 = deque(tmp689._args)
                    # State 63778
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.2.0', S(0))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 63779
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.2.1.0_1', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 63780
                            if len(subjects690) >= 1:
                                tmp693 = subjects690.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.2.2.1.0', tmp693)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 63781
                                    if len(subjects690) == 0:
                                        pass
                                        # State 63782
                                        if len(subjects601) >= 1 and subjects601[0] == -1:
                                            tmp695 = subjects601.popleft()
                                            # State 63783
                                            if len(subjects601) == 0:
                                                pass
                                                # State 63784
                                                if len(subjects) == 0:
                                                    pass
                                                    # 58: b/sin(e + x*f)
                                            subjects601.appendleft(tmp695)
                                subjects690.appendleft(tmp693)
                        if len(subjects690) >= 1 and isinstance(subjects690[0], Mul):
                            tmp696 = subjects690.popleft()
                            associative1 = tmp696
                            associative_type1 = type(tmp696)
                            subjects697 = deque(tmp696._args)
                            matcher = CommutativeMatcher63786.get()
                            tmp698 = subjects697
                            subjects697 = []
                            for s in tmp698:
                                matcher.add_subject(s)
                            for pattern_index, subst3 in matcher.match(tmp698, subst2):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 63787
                                    if len(subjects690) == 0:
                                        pass
                                        # State 63788
                                        if len(subjects601) >= 1 and subjects601[0] == -1:
                                            tmp699 = subjects601.popleft()
                                            # State 63789
                                            if len(subjects601) == 0:
                                                pass
                                                # State 63790
                                                if len(subjects) == 0:
                                                    pass
                                                    # 58: b/sin(e + x*f)
                                            subjects601.appendleft(tmp699)
                            subjects690.appendleft(tmp696)
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.3.0', S(0))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 64413
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.3.1.0_1', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 64414
                            if len(subjects690) >= 1:
                                tmp702 = subjects690.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.2.3.1.0', tmp702)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 64415
                                    if len(subjects690) == 0:
                                        pass
                                        # State 64416
                                        if len(subjects601) >= 1 and subjects601[0] == -1:
                                            tmp704 = subjects601.popleft()
                                            # State 64417
                                            if len(subjects601) == 0:
                                                pass
                                                # State 64418
                                                if len(subjects) == 0:
                                                    pass
                                                    # 60: d/sin(e + x*f)
                                            subjects601.appendleft(tmp704)
                                subjects690.appendleft(tmp702)
                        if len(subjects690) >= 1 and isinstance(subjects690[0], Mul):
                            tmp705 = subjects690.popleft()
                            associative1 = tmp705
                            associative_type1 = type(tmp705)
                            subjects706 = deque(tmp705._args)
                            matcher = CommutativeMatcher64420.get()
                            tmp707 = subjects706
                            subjects706 = []
                            for s in tmp707:
                                matcher.add_subject(s)
                            for pattern_index, subst3 in matcher.match(tmp707, subst2):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 64421
                                    if len(subjects690) == 0:
                                        pass
                                        # State 64422
                                        if len(subjects601) >= 1 and subjects601[0] == -1:
                                            tmp708 = subjects601.popleft()
                                            # State 64423
                                            if len(subjects601) == 0:
                                                pass
                                                # State 64424
                                                if len(subjects) == 0:
                                                    pass
                                                    # 60: d/sin(e + x*f)
                                            subjects601.appendleft(tmp708)
                            subjects690.appendleft(tmp705)
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.4.0', S(0))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 91124
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.4.1.0_1', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 91125
                            if len(subjects690) >= 1:
                                tmp711 = subjects690.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.2.4.1.0', tmp711)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 91126
                                    if len(subjects690) == 0:
                                        pass
                                        # State 91127
                                        if len(subjects601) >= 1 and subjects601[0] == -1:
                                            tmp713 = subjects601.popleft()
                                            # State 91128
                                            if len(subjects601) == 0:
                                                pass
                                                # State 91129
                                                if len(subjects) == 0:
                                                    pass
                                                    # 90: b/sin(c + x*d)
                                            subjects601.appendleft(tmp713)
                                subjects690.appendleft(tmp711)
                        if len(subjects690) >= 1 and isinstance(subjects690[0], Mul):
                            tmp714 = subjects690.popleft()
                            associative1 = tmp714
                            associative_type1 = type(tmp714)
                            subjects715 = deque(tmp714._args)
                            matcher = CommutativeMatcher91131.get()
                            tmp716 = subjects715
                            subjects715 = []
                            for s in tmp716:
                                matcher.add_subject(s)
                            for pattern_index, subst3 in matcher.match(tmp716, subst2):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 91132
                                    if len(subjects690) == 0:
                                        pass
                                        # State 91133
                                        if len(subjects601) >= 1 and subjects601[0] == -1:
                                            tmp717 = subjects601.popleft()
                                            # State 91134
                                            if len(subjects601) == 0:
                                                pass
                                                # State 91135
                                                if len(subjects) == 0:
                                                    pass
                                                    # 90: b/sin(c + x*d)
                                            subjects601.appendleft(tmp717)
                            subjects690.appendleft(tmp714)
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.2.3.0', S(0))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 92027
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.2.3.1.0_1', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 92028
                            if len(subjects690) >= 1:
                                tmp720 = subjects690.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.2.2.3.1.0', tmp720)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 92029
                                    if len(subjects690) == 0:
                                        pass
                                        # State 92030
                                        if len(subjects601) >= 1 and subjects601[0] == -1:
                                            tmp722 = subjects601.popleft()
                                            # State 92031
                                            if len(subjects601) == 0:
                                                pass
                                                # State 92032
                                                if len(subjects) == 0:
                                                    pass
                                                    # 94: b/sin(e + x*f)
                                            subjects601.appendleft(tmp722)
                                subjects690.appendleft(tmp720)
                        if len(subjects690) >= 1 and isinstance(subjects690[0], Mul):
                            tmp723 = subjects690.popleft()
                            associative1 = tmp723
                            associative_type1 = type(tmp723)
                            subjects724 = deque(tmp723._args)
                            matcher = CommutativeMatcher92034.get()
                            tmp725 = subjects724
                            subjects724 = []
                            for s in tmp725:
                                matcher.add_subject(s)
                            for pattern_index, subst3 in matcher.match(tmp725, subst2):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 92035
                                    if len(subjects690) == 0:
                                        pass
                                        # State 92036
                                        if len(subjects601) >= 1 and subjects601[0] == -1:
                                            tmp726 = subjects601.popleft()
                                            # State 92037
                                            if len(subjects601) == 0:
                                                pass
                                                # State 92038
                                                if len(subjects) == 0:
                                                    pass
                                                    # 94: b/sin(e + x*f)
                                            subjects601.appendleft(tmp726)
                            subjects690.appendleft(tmp723)
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.3.0', S(0))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 99208
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.3.1.0', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 99209
                            if len(subjects690) >= 1 and isinstance(subjects690[0], Pow):
                                tmp729 = subjects690.popleft()
                                subjects730 = deque(tmp729._args)
                                # State 99210
                                if len(subjects730) >= 1:
                                    tmp731 = subjects730.popleft()
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i2.2.0_1', tmp731)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 99211
                                        if len(subjects730) >= 1:
                                            tmp733 = subjects730.popleft()
                                            subst5 = Substitution(subst4)
                                            try:
                                                subst5.try_add_variable('i2.2.1.3.1.2', tmp733)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 99212
                                                if len(subjects730) == 0:
                                                    pass
                                                    # State 99213
                                                    if len(subjects690) == 0:
                                                        pass
                                                        # State 99214
                                                        if len(subjects601) >= 1 and subjects601[0] == -1:
                                                            tmp735 = subjects601.popleft()
                                                            # State 99215
                                                            if len(subjects601) == 0:
                                                                pass
                                                                # State 99216
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 96: b/sin(x**n*d + c)
                                                            subjects601.appendleft(tmp735)
                                            subjects730.appendleft(tmp733)
                                    subjects730.appendleft(tmp731)
                                subjects690.appendleft(tmp729)
                        if len(subjects690) >= 1 and isinstance(subjects690[0], Mul):
                            tmp736 = subjects690.popleft()
                            associative1 = tmp736
                            associative_type1 = type(tmp736)
                            subjects737 = deque(tmp736._args)
                            matcher = CommutativeMatcher99218.get()
                            tmp738 = subjects737
                            subjects737 = []
                            for s in tmp738:
                                matcher.add_subject(s)
                            for pattern_index, subst3 in matcher.match(tmp738, subst2):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 99223
                                    if len(subjects690) == 0:
                                        pass
                                        # State 99224
                                        if len(subjects601) >= 1 and subjects601[0] == -1:
                                            tmp739 = subjects601.popleft()
                                            # State 99225
                                            if len(subjects601) == 0:
                                                pass
                                                # State 99226
                                                if len(subjects) == 0:
                                                    pass
                                                    # 96: b/sin(x**n*d + c)
                                            subjects601.appendleft(tmp739)
                            subjects690.appendleft(tmp736)
                    if len(subjects690) >= 1:
                        tmp740 = subjects690.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.1.2', tmp740)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 99455
                            if len(subjects690) == 0:
                                pass
                                # State 99456
                                if len(subjects601) >= 1 and subjects601[0] == -1:
                                    tmp742 = subjects601.popleft()
                                    # State 99457
                                    if len(subjects601) == 0:
                                        pass
                                        # State 99458
                                        if len(subjects) == 0:
                                            pass
                                            # 98: b/sin(v)
                                    subjects601.appendleft(tmp742)
                        subjects690.appendleft(tmp740)
                    if len(subjects690) >= 1 and isinstance(subjects690[0], Add):
                        tmp743 = subjects690.popleft()
                        associative1 = tmp743
                        associative_type1 = type(tmp743)
                        subjects744 = deque(tmp743._args)
                        matcher = CommutativeMatcher63792.get()
                        tmp745 = subjects744
                        subjects744 = []
                        for s in tmp745:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp745, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 63798
                                if len(subjects690) == 0:
                                    pass
                                    # State 63799
                                    if len(subjects601) >= 1 and subjects601[0] == -1:
                                        tmp746 = subjects601.popleft()
                                        # State 63800
                                        if len(subjects601) == 0:
                                            pass
                                            # State 63801
                                            if len(subjects) == 0:
                                                pass
                                                # 58: b/sin(e + x*f)
                                        subjects601.appendleft(tmp746)
                            if pattern_index == 1:
                                pass
                                # State 64428
                                if len(subjects690) == 0:
                                    pass
                                    # State 64429
                                    if len(subjects601) >= 1 and subjects601[0] == -1:
                                        tmp747 = subjects601.popleft()
                                        # State 64430
                                        if len(subjects601) == 0:
                                            pass
                                            # State 64431
                                            if len(subjects) == 0:
                                                pass
                                                # 60: d/sin(e + x*f)
                                        subjects601.appendleft(tmp747)
                            if pattern_index == 2:
                                pass
                                # State 91139
                                if len(subjects690) == 0:
                                    pass
                                    # State 91140
                                    if len(subjects601) >= 1 and subjects601[0] == -1:
                                        tmp748 = subjects601.popleft()
                                        # State 91141
                                        if len(subjects601) == 0:
                                            pass
                                            # State 91142
                                            if len(subjects) == 0:
                                                pass
                                                # 90: b/sin(c + x*d)
                                        subjects601.appendleft(tmp748)
                            if pattern_index == 3:
                                pass
                                # State 92042
                                if len(subjects690) == 0:
                                    pass
                                    # State 92043
                                    if len(subjects601) >= 1 and subjects601[0] == -1:
                                        tmp749 = subjects601.popleft()
                                        # State 92044
                                        if len(subjects601) == 0:
                                            pass
                                            # State 92045
                                            if len(subjects) == 0:
                                                pass
                                                # 94: b/sin(e + x*f)
                                        subjects601.appendleft(tmp749)
                            if pattern_index == 4:
                                pass
                                # State 99237
                                if len(subjects690) == 0:
                                    pass
                                    # State 99238
                                    if len(subjects601) >= 1 and subjects601[0] == -1:
                                        tmp750 = subjects601.popleft()
                                        # State 99239
                                        if len(subjects601) == 0:
                                            pass
                                            # State 99240
                                            if len(subjects) == 0:
                                                pass
                                                # 96: b/sin(x**n*d + c)
                                        subjects601.appendleft(tmp750)
                        subjects690.appendleft(tmp743)
                    subjects601.appendleft(tmp689)
                if len(subjects601) >= 1 and isinstance(subjects601[0], cos):
                    tmp751 = subjects601.popleft()
                    subjects752 = deque(tmp751._args)
                    # State 64057
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.2.0', S(0))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 64058
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.2.1.0_1', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 64059
                            if len(subjects752) >= 1:
                                tmp755 = subjects752.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.2.2.1.0', tmp755)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 64060
                                    if len(subjects752) == 0:
                                        pass
                                        # State 64061
                                        if len(subjects601) >= 1 and subjects601[0] == -1:
                                            tmp757 = subjects601.popleft()
                                            # State 64062
                                            if len(subjects601) == 0:
                                                pass
                                                # State 64063
                                                if len(subjects) == 0:
                                                    pass
                                                    # 59: b/cos(e + x*f)
                                            subjects601.appendleft(tmp757)
                                subjects752.appendleft(tmp755)
                        if len(subjects752) >= 1 and isinstance(subjects752[0], Mul):
                            tmp758 = subjects752.popleft()
                            associative1 = tmp758
                            associative_type1 = type(tmp758)
                            subjects759 = deque(tmp758._args)
                            matcher = CommutativeMatcher64065.get()
                            tmp760 = subjects759
                            subjects759 = []
                            for s in tmp760:
                                matcher.add_subject(s)
                            for pattern_index, subst3 in matcher.match(tmp760, subst2):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 64066
                                    if len(subjects752) == 0:
                                        pass
                                        # State 64067
                                        if len(subjects601) >= 1 and subjects601[0] == -1:
                                            tmp761 = subjects601.popleft()
                                            # State 64068
                                            if len(subjects601) == 0:
                                                pass
                                                # State 64069
                                                if len(subjects) == 0:
                                                    pass
                                                    # 59: b/cos(e + x*f)
                                            subjects601.appendleft(tmp761)
                            subjects752.appendleft(tmp758)
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.3.0', S(0))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 64498
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.3.1.0_1', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 64499
                            if len(subjects752) >= 1:
                                tmp764 = subjects752.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.2.3.1.0', tmp764)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 64500
                                    if len(subjects752) == 0:
                                        pass
                                        # State 64501
                                        if len(subjects601) >= 1 and subjects601[0] == -1:
                                            tmp766 = subjects601.popleft()
                                            # State 64502
                                            if len(subjects601) == 0:
                                                pass
                                                # State 64503
                                                if len(subjects) == 0:
                                                    pass
                                                    # 61: d/cos(e + x*f)
                                            subjects601.appendleft(tmp766)
                                subjects752.appendleft(tmp764)
                        if len(subjects752) >= 1 and isinstance(subjects752[0], Mul):
                            tmp767 = subjects752.popleft()
                            associative1 = tmp767
                            associative_type1 = type(tmp767)
                            subjects768 = deque(tmp767._args)
                            matcher = CommutativeMatcher64505.get()
                            tmp769 = subjects768
                            subjects768 = []
                            for s in tmp769:
                                matcher.add_subject(s)
                            for pattern_index, subst3 in matcher.match(tmp769, subst2):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 64506
                                    if len(subjects752) == 0:
                                        pass
                                        # State 64507
                                        if len(subjects601) >= 1 and subjects601[0] == -1:
                                            tmp770 = subjects601.popleft()
                                            # State 64508
                                            if len(subjects601) == 0:
                                                pass
                                                # State 64509
                                                if len(subjects) == 0:
                                                    pass
                                                    # 61: d/cos(e + x*f)
                                            subjects601.appendleft(tmp770)
                            subjects752.appendleft(tmp767)
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.2.3.0', S(0))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 91846
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.2.3.1.0_1', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 91847
                            if len(subjects752) >= 1:
                                tmp773 = subjects752.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.2.2.3.1.0', tmp773)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 91848
                                    if len(subjects752) == 0:
                                        pass
                                        # State 91849
                                        if len(subjects601) >= 1 and subjects601[0] == -1:
                                            tmp775 = subjects601.popleft()
                                            # State 91850
                                            if len(subjects601) == 0:
                                                pass
                                                # State 91851
                                                if len(subjects) == 0:
                                                    pass
                                                    # 93: b/cos(e + x*f)
                                            subjects601.appendleft(tmp775)
                                subjects752.appendleft(tmp773)
                        if len(subjects752) >= 1 and isinstance(subjects752[0], Mul):
                            tmp776 = subjects752.popleft()
                            associative1 = tmp776
                            associative_type1 = type(tmp776)
                            subjects777 = deque(tmp776._args)
                            matcher = CommutativeMatcher91853.get()
                            tmp778 = subjects777
                            subjects777 = []
                            for s in tmp778:
                                matcher.add_subject(s)
                            for pattern_index, subst3 in matcher.match(tmp778, subst2):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 91854
                                    if len(subjects752) == 0:
                                        pass
                                        # State 91855
                                        if len(subjects601) >= 1 and subjects601[0] == -1:
                                            tmp779 = subjects601.popleft()
                                            # State 91856
                                            if len(subjects601) == 0:
                                                pass
                                                # State 91857
                                                if len(subjects) == 0:
                                                    pass
                                                    # 93: b/cos(e + x*f)
                                            subjects601.appendleft(tmp779)
                            subjects752.appendleft(tmp776)
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.3.0', S(0))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 98931
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.3.1.0', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 98932
                            if len(subjects752) >= 1 and isinstance(subjects752[0], Pow):
                                tmp782 = subjects752.popleft()
                                subjects783 = deque(tmp782._args)
                                # State 98933
                                if len(subjects783) >= 1:
                                    tmp784 = subjects783.popleft()
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i2.2.0_1', tmp784)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 98934
                                        if len(subjects783) >= 1:
                                            tmp786 = subjects783.popleft()
                                            subst5 = Substitution(subst4)
                                            try:
                                                subst5.try_add_variable('i2.2.1.3.1.2', tmp786)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 98935
                                                if len(subjects783) == 0:
                                                    pass
                                                    # State 98936
                                                    if len(subjects752) == 0:
                                                        pass
                                                        # State 98937
                                                        if len(subjects601) >= 1 and subjects601[0] == -1:
                                                            tmp788 = subjects601.popleft()
                                                            # State 98938
                                                            if len(subjects601) == 0:
                                                                pass
                                                                # State 98939
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 95: b/cos(x**n*d + c)
                                                            subjects601.appendleft(tmp788)
                                            subjects783.appendleft(tmp786)
                                    subjects783.appendleft(tmp784)
                                subjects752.appendleft(tmp782)
                        if len(subjects752) >= 1 and isinstance(subjects752[0], Mul):
                            tmp789 = subjects752.popleft()
                            associative1 = tmp789
                            associative_type1 = type(tmp789)
                            subjects790 = deque(tmp789._args)
                            matcher = CommutativeMatcher98941.get()
                            tmp791 = subjects790
                            subjects790 = []
                            for s in tmp791:
                                matcher.add_subject(s)
                            for pattern_index, subst3 in matcher.match(tmp791, subst2):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 98946
                                    if len(subjects752) == 0:
                                        pass
                                        # State 98947
                                        if len(subjects601) >= 1 and subjects601[0] == -1:
                                            tmp792 = subjects601.popleft()
                                            # State 98948
                                            if len(subjects601) == 0:
                                                pass
                                                # State 98949
                                                if len(subjects) == 0:
                                                    pass
                                                    # 95: b/cos(x**n*d + c)
                                            subjects601.appendleft(tmp792)
                            subjects752.appendleft(tmp789)
                    if len(subjects752) >= 1:
                        tmp793 = subjects752.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.1.2', tmp793)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 99417
                            if len(subjects752) == 0:
                                pass
                                # State 99418
                                if len(subjects601) >= 1 and subjects601[0] == -1:
                                    tmp795 = subjects601.popleft()
                                    # State 99419
                                    if len(subjects601) == 0:
                                        pass
                                        # State 99420
                                        if len(subjects) == 0:
                                            pass
                                            # 97: b/cos(v)
                                    subjects601.appendleft(tmp795)
                        subjects752.appendleft(tmp793)
                    if len(subjects752) >= 1 and isinstance(subjects752[0], Add):
                        tmp796 = subjects752.popleft()
                        associative1 = tmp796
                        associative_type1 = type(tmp796)
                        subjects797 = deque(tmp796._args)
                        matcher = CommutativeMatcher64071.get()
                        tmp798 = subjects797
                        subjects797 = []
                        for s in tmp798:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp798, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 64077
                                if len(subjects752) == 0:
                                    pass
                                    # State 64078
                                    if len(subjects601) >= 1 and subjects601[0] == -1:
                                        tmp799 = subjects601.popleft()
                                        # State 64079
                                        if len(subjects601) == 0:
                                            pass
                                            # State 64080
                                            if len(subjects) == 0:
                                                pass
                                                # 59: b/cos(e + x*f)
                                        subjects601.appendleft(tmp799)
                            if pattern_index == 1:
                                pass
                                # State 64513
                                if len(subjects752) == 0:
                                    pass
                                    # State 64514
                                    if len(subjects601) >= 1 and subjects601[0] == -1:
                                        tmp800 = subjects601.popleft()
                                        # State 64515
                                        if len(subjects601) == 0:
                                            pass
                                            # State 64516
                                            if len(subjects) == 0:
                                                pass
                                                # 61: d/cos(e + x*f)
                                        subjects601.appendleft(tmp800)
                            if pattern_index == 2:
                                pass
                                # State 91861
                                if len(subjects752) == 0:
                                    pass
                                    # State 91862
                                    if len(subjects601) >= 1 and subjects601[0] == -1:
                                        tmp801 = subjects601.popleft()
                                        # State 91863
                                        if len(subjects601) == 0:
                                            pass
                                            # State 91864
                                            if len(subjects) == 0:
                                                pass
                                                # 93: b/cos(e + x*f)
                                        subjects601.appendleft(tmp801)
                            if pattern_index == 3:
                                pass
                                # State 98960
                                if len(subjects752) == 0:
                                    pass
                                    # State 98961
                                    if len(subjects601) >= 1 and subjects601[0] == -1:
                                        tmp802 = subjects601.popleft()
                                        # State 98962
                                        if len(subjects601) == 0:
                                            pass
                                            # State 98963
                                            if len(subjects) == 0:
                                                pass
                                                # 95: b/cos(x**n*d + c)
                                        subjects601.appendleft(tmp802)
                        subjects752.appendleft(tmp796)
                    subjects601.appendleft(tmp751)
                if len(subjects601) >= 1 and isinstance(subjects601[0], tan):
                    tmp803 = subjects601.popleft()
                    subjects804 = deque(tmp803._args)
                    # State 78040
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.3.0', S(0))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 78041
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.3.1.0_1', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 78042
                            if len(subjects804) >= 1:
                                tmp807 = subjects804.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.2.3.1.0', tmp807)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 78043
                                    if len(subjects804) == 0:
                                        pass
                                        # State 78044
                                        if len(subjects601) >= 1 and subjects601[0] == -1:
                                            tmp809 = subjects601.popleft()
                                            # State 78045
                                            if len(subjects601) == 0:
                                                pass
                                                # State 78046
                                                if len(subjects) == 0:
                                                    pass
                                                    # 74: b/tan(e + x*f)
                                            subjects601.appendleft(tmp809)
                                subjects804.appendleft(tmp807)
                        if len(subjects804) >= 1 and isinstance(subjects804[0], Mul):
                            tmp810 = subjects804.popleft()
                            associative1 = tmp810
                            associative_type1 = type(tmp810)
                            subjects811 = deque(tmp810._args)
                            matcher = CommutativeMatcher78048.get()
                            tmp812 = subjects811
                            subjects811 = []
                            for s in tmp812:
                                matcher.add_subject(s)
                            for pattern_index, subst3 in matcher.match(tmp812, subst2):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 78049
                                    if len(subjects804) == 0:
                                        pass
                                        # State 78050
                                        if len(subjects601) >= 1 and subjects601[0] == -1:
                                            tmp813 = subjects601.popleft()
                                            # State 78051
                                            if len(subjects601) == 0:
                                                pass
                                                # State 78052
                                                if len(subjects) == 0:
                                                    pass
                                                    # 74: b/tan(e + x*f)
                                            subjects601.appendleft(tmp813)
                            subjects804.appendleft(tmp810)
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.2.0', S(0))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 78298
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.2.1.0_1', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 78299
                            if len(subjects804) >= 1:
                                tmp816 = subjects804.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.2.2.1.0', tmp816)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 78300
                                    if len(subjects804) == 0:
                                        pass
                                        # State 78301
                                        if len(subjects601) >= 1 and subjects601[0] == -1:
                                            tmp818 = subjects601.popleft()
                                            # State 78302
                                            if len(subjects601) == 0:
                                                pass
                                                # State 78303
                                                if len(subjects) == 0:
                                                    pass
                                                    # 76: b/tan(e + x*f)
                                            subjects601.appendleft(tmp818)
                                subjects804.appendleft(tmp816)
                        if len(subjects804) >= 1 and isinstance(subjects804[0], Mul):
                            tmp819 = subjects804.popleft()
                            associative1 = tmp819
                            associative_type1 = type(tmp819)
                            subjects820 = deque(tmp819._args)
                            matcher = CommutativeMatcher78305.get()
                            tmp821 = subjects820
                            subjects820 = []
                            for s in tmp821:
                                matcher.add_subject(s)
                            for pattern_index, subst3 in matcher.match(tmp821, subst2):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 78306
                                    if len(subjects804) == 0:
                                        pass
                                        # State 78307
                                        if len(subjects601) >= 1 and subjects601[0] == -1:
                                            tmp822 = subjects601.popleft()
                                            # State 78308
                                            if len(subjects601) == 0:
                                                pass
                                                # State 78309
                                                if len(subjects) == 0:
                                                    pass
                                                    # 76: b/tan(e + x*f)
                                            subjects601.appendleft(tmp822)
                            subjects804.appendleft(tmp819)
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.2.3.0', S(0))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 80327
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.2.3.1.0_1', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 80328
                            if len(subjects804) >= 1:
                                tmp825 = subjects804.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.2.2.3.1.0', tmp825)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 80329
                                    if len(subjects804) == 0:
                                        pass
                                        # State 80330
                                        if len(subjects601) >= 1 and subjects601[0] == -1:
                                            tmp827 = subjects601.popleft()
                                            # State 80331
                                            if len(subjects601) == 0:
                                                pass
                                                # State 80332
                                                if len(subjects) == 0:
                                                    pass
                                                    # 80: b/tan(e + x*f)
                                            subjects601.appendleft(tmp827)
                                subjects804.appendleft(tmp825)
                        if len(subjects804) >= 1 and isinstance(subjects804[0], Mul):
                            tmp828 = subjects804.popleft()
                            associative1 = tmp828
                            associative_type1 = type(tmp828)
                            subjects829 = deque(tmp828._args)
                            matcher = CommutativeMatcher80334.get()
                            tmp830 = subjects829
                            subjects829 = []
                            for s in tmp830:
                                matcher.add_subject(s)
                            for pattern_index, subst3 in matcher.match(tmp830, subst2):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 80335
                                    if len(subjects804) == 0:
                                        pass
                                        # State 80336
                                        if len(subjects601) >= 1 and subjects601[0] == -1:
                                            tmp831 = subjects601.popleft()
                                            # State 80337
                                            if len(subjects601) == 0:
                                                pass
                                                # State 80338
                                                if len(subjects) == 0:
                                                    pass
                                                    # 80: b/tan(e + x*f)
                                            subjects601.appendleft(tmp831)
                            subjects804.appendleft(tmp828)
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.4.0', S(0))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 80775
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.4.1.0_1', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 80776
                            if len(subjects804) >= 1:
                                tmp834 = subjects804.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.2.4.1.0', tmp834)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 80777
                                    if len(subjects804) == 0:
                                        pass
                                        # State 80778
                                        if len(subjects601) >= 1 and subjects601[0] == -1:
                                            tmp836 = subjects601.popleft()
                                            # State 80779
                                            if len(subjects601) == 0:
                                                pass
                                                # State 80780
                                                if len(subjects) == 0:
                                                    pass
                                                    # 81: b/tan(e + x*f)
                                            subjects601.appendleft(tmp836)
                                subjects804.appendleft(tmp834)
                        if len(subjects804) >= 1 and isinstance(subjects804[0], Mul):
                            tmp837 = subjects804.popleft()
                            associative1 = tmp837
                            associative_type1 = type(tmp837)
                            subjects838 = deque(tmp837._args)
                            matcher = CommutativeMatcher80782.get()
                            tmp839 = subjects838
                            subjects838 = []
                            for s in tmp839:
                                matcher.add_subject(s)
                            for pattern_index, subst3 in matcher.match(tmp839, subst2):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 80783
                                    if len(subjects804) == 0:
                                        pass
                                        # State 80784
                                        if len(subjects601) >= 1 and subjects601[0] == -1:
                                            tmp840 = subjects601.popleft()
                                            # State 80785
                                            if len(subjects601) == 0:
                                                pass
                                                # State 80786
                                                if len(subjects) == 0:
                                                    pass
                                                    # 81: b/tan(e + x*f)
                                            subjects601.appendleft(tmp840)
                            subjects804.appendleft(tmp837)
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.3.0', S(0))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 88762
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.3.1.0', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 88763
                            if len(subjects804) >= 1 and isinstance(subjects804[0], Pow):
                                tmp843 = subjects804.popleft()
                                subjects844 = deque(tmp843._args)
                                # State 88764
                                if len(subjects844) >= 1:
                                    tmp845 = subjects844.popleft()
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i2.2.0_1', tmp845)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 88765
                                        if len(subjects844) >= 1:
                                            tmp847 = subjects844.popleft()
                                            subst5 = Substitution(subst4)
                                            try:
                                                subst5.try_add_variable('i2.2.1.3.1.2', tmp847)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 88766
                                                if len(subjects844) == 0:
                                                    pass
                                                    # State 88767
                                                    if len(subjects804) == 0:
                                                        pass
                                                        # State 88768
                                                        if len(subjects601) >= 1 and subjects601[0] == -1:
                                                            tmp849 = subjects601.popleft()
                                                            # State 88769
                                                            if len(subjects601) == 0:
                                                                pass
                                                                # State 88770
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 87: b/tan(x**n*d + c)
                                                            subjects601.appendleft(tmp849)
                                            subjects844.appendleft(tmp847)
                                    subjects844.appendleft(tmp845)
                                subjects804.appendleft(tmp843)
                        if len(subjects804) >= 1 and isinstance(subjects804[0], Mul):
                            tmp850 = subjects804.popleft()
                            associative1 = tmp850
                            associative_type1 = type(tmp850)
                            subjects851 = deque(tmp850._args)
                            matcher = CommutativeMatcher88772.get()
                            tmp852 = subjects851
                            subjects851 = []
                            for s in tmp852:
                                matcher.add_subject(s)
                            for pattern_index, subst3 in matcher.match(tmp852, subst2):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 88777
                                    if len(subjects804) == 0:
                                        pass
                                        # State 88778
                                        if len(subjects601) >= 1 and subjects601[0] == -1:
                                            tmp853 = subjects601.popleft()
                                            # State 88779
                                            if len(subjects601) == 0:
                                                pass
                                                # State 88780
                                                if len(subjects) == 0:
                                                    pass
                                                    # 87: b/tan(x**n*d + c)
                                            subjects601.appendleft(tmp853)
                            subjects804.appendleft(tmp850)
                    if len(subjects804) >= 1:
                        tmp854 = subjects804.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.1.2', tmp854)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 89002
                            if len(subjects804) == 0:
                                pass
                                # State 89003
                                if len(subjects601) >= 1 and subjects601[0] == -1:
                                    tmp856 = subjects601.popleft()
                                    # State 89004
                                    if len(subjects601) == 0:
                                        pass
                                        # State 89005
                                        if len(subjects) == 0:
                                            pass
                                            # 89: b/tan(v)
                                    subjects601.appendleft(tmp856)
                        subjects804.appendleft(tmp854)
                    if len(subjects804) >= 1 and isinstance(subjects804[0], Add):
                        tmp857 = subjects804.popleft()
                        associative1 = tmp857
                        associative_type1 = type(tmp857)
                        subjects858 = deque(tmp857._args)
                        matcher = CommutativeMatcher78054.get()
                        tmp859 = subjects858
                        subjects858 = []
                        for s in tmp859:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp859, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 78060
                                if len(subjects804) == 0:
                                    pass
                                    # State 78061
                                    if len(subjects601) >= 1 and subjects601[0] == -1:
                                        tmp860 = subjects601.popleft()
                                        # State 78062
                                        if len(subjects601) == 0:
                                            pass
                                            # State 78063
                                            if len(subjects) == 0:
                                                pass
                                                # 74: b/tan(e + x*f)
                                        subjects601.appendleft(tmp860)
                            if pattern_index == 1:
                                pass
                                # State 78313
                                if len(subjects804) == 0:
                                    pass
                                    # State 78314
                                    if len(subjects601) >= 1 and subjects601[0] == -1:
                                        tmp861 = subjects601.popleft()
                                        # State 78315
                                        if len(subjects601) == 0:
                                            pass
                                            # State 78316
                                            if len(subjects) == 0:
                                                pass
                                                # 76: b/tan(e + x*f)
                                        subjects601.appendleft(tmp861)
                            if pattern_index == 2:
                                pass
                                # State 80342
                                if len(subjects804) == 0:
                                    pass
                                    # State 80343
                                    if len(subjects601) >= 1 and subjects601[0] == -1:
                                        tmp862 = subjects601.popleft()
                                        # State 80344
                                        if len(subjects601) == 0:
                                            pass
                                            # State 80345
                                            if len(subjects) == 0:
                                                pass
                                                # 80: b/tan(e + x*f)
                                        subjects601.appendleft(tmp862)
                            if pattern_index == 3:
                                pass
                                # State 80790
                                if len(subjects804) == 0:
                                    pass
                                    # State 80791
                                    if len(subjects601) >= 1 and subjects601[0] == -1:
                                        tmp863 = subjects601.popleft()
                                        # State 80792
                                        if len(subjects601) == 0:
                                            pass
                                            # State 80793
                                            if len(subjects) == 0:
                                                pass
                                                # 81: b/tan(e + x*f)
                                        subjects601.appendleft(tmp863)
                            if pattern_index == 4:
                                pass
                                # State 88791
                                if len(subjects804) == 0:
                                    pass
                                    # State 88792
                                    if len(subjects601) >= 1 and subjects601[0] == -1:
                                        tmp864 = subjects601.popleft()
                                        # State 88793
                                        if len(subjects601) == 0:
                                            pass
                                            # State 88794
                                            if len(subjects) == 0:
                                                pass
                                                # 87: b/tan(x**n*d + c)
                                        subjects601.appendleft(tmp864)
                        subjects804.appendleft(tmp857)
                    subjects601.appendleft(tmp803)
                if len(subjects601) >= 1 and isinstance(subjects601[0], tanh):
                    tmp865 = subjects601.popleft()
                    subjects866 = deque(tmp865._args)
                    # State 128300
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.3.0', S(0))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 128301
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.3.1.0', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 128302
                            if len(subjects866) >= 1 and isinstance(subjects866[0], Pow):
                                tmp869 = subjects866.popleft()
                                subjects870 = deque(tmp869._args)
                                # State 128303
                                if len(subjects870) >= 1:
                                    tmp871 = subjects870.popleft()
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i2.2.0_1', tmp871)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 128304
                                        if len(subjects870) >= 1:
                                            tmp873 = subjects870.popleft()
                                            subst5 = Substitution(subst4)
                                            try:
                                                subst5.try_add_variable('i2.2.1.3.1.2', tmp873)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 128305
                                                if len(subjects870) == 0:
                                                    pass
                                                    # State 128306
                                                    if len(subjects866) == 0:
                                                        pass
                                                        # State 128307
                                                        if len(subjects601) >= 1 and subjects601[0] == -1:
                                                            tmp875 = subjects601.popleft()
                                                            # State 128308
                                                            if len(subjects601) == 0:
                                                                pass
                                                                # State 128309
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 129: b/tanh(x**n*d + c)
                                                            subjects601.appendleft(tmp875)
                                            subjects870.appendleft(tmp873)
                                    subjects870.appendleft(tmp871)
                                subjects866.appendleft(tmp869)
                        if len(subjects866) >= 1 and isinstance(subjects866[0], Mul):
                            tmp876 = subjects866.popleft()
                            associative1 = tmp876
                            associative_type1 = type(tmp876)
                            subjects877 = deque(tmp876._args)
                            matcher = CommutativeMatcher128311.get()
                            tmp878 = subjects877
                            subjects877 = []
                            for s in tmp878:
                                matcher.add_subject(s)
                            for pattern_index, subst3 in matcher.match(tmp878, subst2):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 128316
                                    if len(subjects866) == 0:
                                        pass
                                        # State 128317
                                        if len(subjects601) >= 1 and subjects601[0] == -1:
                                            tmp879 = subjects601.popleft()
                                            # State 128318
                                            if len(subjects601) == 0:
                                                pass
                                                # State 128319
                                                if len(subjects) == 0:
                                                    pass
                                                    # 129: b/tanh(x**n*d + c)
                                            subjects601.appendleft(tmp879)
                            subjects866.appendleft(tmp876)
                    if len(subjects866) >= 1:
                        tmp880 = subjects866.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.1.2', tmp880)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 128553
                            if len(subjects866) == 0:
                                pass
                                # State 128554
                                if len(subjects601) >= 1 and subjects601[0] == -1:
                                    tmp882 = subjects601.popleft()
                                    # State 128555
                                    if len(subjects601) == 0:
                                        pass
                                        # State 128556
                                        if len(subjects) == 0:
                                            pass
                                            # 131: b/tanh(v)
                                    subjects601.appendleft(tmp882)
                        subjects866.appendleft(tmp880)
                    if len(subjects866) >= 1 and isinstance(subjects866[0], Add):
                        tmp883 = subjects866.popleft()
                        associative1 = tmp883
                        associative_type1 = type(tmp883)
                        subjects884 = deque(tmp883._args)
                        matcher = CommutativeMatcher128321.get()
                        tmp885 = subjects884
                        subjects884 = []
                        for s in tmp885:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp885, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 128334
                                if len(subjects866) == 0:
                                    pass
                                    # State 128335
                                    if len(subjects601) >= 1 and subjects601[0] == -1:
                                        tmp886 = subjects601.popleft()
                                        # State 128336
                                        if len(subjects601) == 0:
                                            pass
                                            # State 128337
                                            if len(subjects) == 0:
                                                pass
                                                # 129: b/tanh(x**n*d + c)
                                        subjects601.appendleft(tmp886)
                        subjects866.appendleft(tmp883)
                    subjects601.appendleft(tmp865)
                if len(subjects601) >= 1 and isinstance(subjects601[0], cosh):
                    tmp887 = subjects601.popleft()
                    subjects888 = deque(tmp887._args)
                    # State 131244
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.3.0', S(0))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 131245
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.3.1.0', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 131246
                            if len(subjects888) >= 1 and isinstance(subjects888[0], Pow):
                                tmp891 = subjects888.popleft()
                                subjects892 = deque(tmp891._args)
                                # State 131247
                                if len(subjects892) >= 1:
                                    tmp893 = subjects892.popleft()
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i2.2.0_1', tmp893)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 131248
                                        if len(subjects892) >= 1:
                                            tmp895 = subjects892.popleft()
                                            subst5 = Substitution(subst4)
                                            try:
                                                subst5.try_add_variable('i2.2.1.3.1.2', tmp895)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 131249
                                                if len(subjects892) == 0:
                                                    pass
                                                    # State 131250
                                                    if len(subjects888) == 0:
                                                        pass
                                                        # State 131251
                                                        if len(subjects601) >= 1 and subjects601[0] == -1:
                                                            tmp897 = subjects601.popleft()
                                                            # State 131252
                                                            if len(subjects601) == 0:
                                                                pass
                                                                # State 131253
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 132: b/cosh(x**n*d + c)
                                                            subjects601.appendleft(tmp897)
                                            subjects892.appendleft(tmp895)
                                    subjects892.appendleft(tmp893)
                                subjects888.appendleft(tmp891)
                        if len(subjects888) >= 1 and isinstance(subjects888[0], Mul):
                            tmp898 = subjects888.popleft()
                            associative1 = tmp898
                            associative_type1 = type(tmp898)
                            subjects899 = deque(tmp898._args)
                            matcher = CommutativeMatcher131255.get()
                            tmp900 = subjects899
                            subjects899 = []
                            for s in tmp900:
                                matcher.add_subject(s)
                            for pattern_index, subst3 in matcher.match(tmp900, subst2):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 131260
                                    if len(subjects888) == 0:
                                        pass
                                        # State 131261
                                        if len(subjects601) >= 1 and subjects601[0] == -1:
                                            tmp901 = subjects601.popleft()
                                            # State 131262
                                            if len(subjects601) == 0:
                                                pass
                                                # State 131263
                                                if len(subjects) == 0:
                                                    pass
                                                    # 132: b/cosh(x**n*d + c)
                                            subjects601.appendleft(tmp901)
                            subjects888.appendleft(tmp898)
                    if len(subjects888) >= 1:
                        tmp902 = subjects888.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.1.2', tmp902)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 131766
                            if len(subjects888) == 0:
                                pass
                                # State 131767
                                if len(subjects601) >= 1 and subjects601[0] == -1:
                                    tmp904 = subjects601.popleft()
                                    # State 131768
                                    if len(subjects601) == 0:
                                        pass
                                        # State 131769
                                        if len(subjects) == 0:
                                            pass
                                            # 134: b/cosh(u)
                                    subjects601.appendleft(tmp904)
                        subjects888.appendleft(tmp902)
                    if len(subjects888) >= 1 and isinstance(subjects888[0], Add):
                        tmp905 = subjects888.popleft()
                        associative1 = tmp905
                        associative_type1 = type(tmp905)
                        subjects906 = deque(tmp905._args)
                        matcher = CommutativeMatcher131265.get()
                        tmp907 = subjects906
                        subjects906 = []
                        for s in tmp907:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp907, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 131278
                                if len(subjects888) == 0:
                                    pass
                                    # State 131279
                                    if len(subjects601) >= 1 and subjects601[0] == -1:
                                        tmp908 = subjects601.popleft()
                                        # State 131280
                                        if len(subjects601) == 0:
                                            pass
                                            # State 131281
                                            if len(subjects) == 0:
                                                pass
                                                # 132: b/cosh(x**n*d + c)
                                        subjects601.appendleft(tmp908)
                        subjects888.appendleft(tmp905)
                    subjects601.appendleft(tmp887)
                if len(subjects601) >= 1 and isinstance(subjects601[0], sinh):
                    tmp909 = subjects601.popleft()
                    subjects910 = deque(tmp909._args)
                    # State 131539
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.3.0', S(0))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 131540
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.3.1.0', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 131541
                            if len(subjects910) >= 1 and isinstance(subjects910[0], Pow):
                                tmp913 = subjects910.popleft()
                                subjects914 = deque(tmp913._args)
                                # State 131542
                                if len(subjects914) >= 1:
                                    tmp915 = subjects914.popleft()
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i2.2.0_1', tmp915)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 131543
                                        if len(subjects914) >= 1:
                                            tmp917 = subjects914.popleft()
                                            subst5 = Substitution(subst4)
                                            try:
                                                subst5.try_add_variable('i2.2.1.3.1.2', tmp917)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 131544
                                                if len(subjects914) == 0:
                                                    pass
                                                    # State 131545
                                                    if len(subjects910) == 0:
                                                        pass
                                                        # State 131546
                                                        if len(subjects601) >= 1 and subjects601[0] == -1:
                                                            tmp919 = subjects601.popleft()
                                                            # State 131547
                                                            if len(subjects601) == 0:
                                                                pass
                                                                # State 131548
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 133: b/sinh(x**n*d + c)
                                                            subjects601.appendleft(tmp919)
                                            subjects914.appendleft(tmp917)
                                    subjects914.appendleft(tmp915)
                                subjects910.appendleft(tmp913)
                        if len(subjects910) >= 1 and isinstance(subjects910[0], Mul):
                            tmp920 = subjects910.popleft()
                            associative1 = tmp920
                            associative_type1 = type(tmp920)
                            subjects921 = deque(tmp920._args)
                            matcher = CommutativeMatcher131550.get()
                            tmp922 = subjects921
                            subjects921 = []
                            for s in tmp922:
                                matcher.add_subject(s)
                            for pattern_index, subst3 in matcher.match(tmp922, subst2):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 131555
                                    if len(subjects910) == 0:
                                        pass
                                        # State 131556
                                        if len(subjects601) >= 1 and subjects601[0] == -1:
                                            tmp923 = subjects601.popleft()
                                            # State 131557
                                            if len(subjects601) == 0:
                                                pass
                                                # State 131558
                                                if len(subjects) == 0:
                                                    pass
                                                    # 133: b/sinh(x**n*d + c)
                                            subjects601.appendleft(tmp923)
                            subjects910.appendleft(tmp920)
                    if len(subjects910) >= 1:
                        tmp924 = subjects910.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.1.2', tmp924)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 131813
                            if len(subjects910) == 0:
                                pass
                                # State 131814
                                if len(subjects601) >= 1 and subjects601[0] == -1:
                                    tmp926 = subjects601.popleft()
                                    # State 131815
                                    if len(subjects601) == 0:
                                        pass
                                        # State 131816
                                        if len(subjects) == 0:
                                            pass
                                            # 135: b/sinh(u)
                                    subjects601.appendleft(tmp926)
                        subjects910.appendleft(tmp924)
                    if len(subjects910) >= 1 and isinstance(subjects910[0], Add):
                        tmp927 = subjects910.popleft()
                        associative1 = tmp927
                        associative_type1 = type(tmp927)
                        subjects928 = deque(tmp927._args)
                        matcher = CommutativeMatcher131560.get()
                        tmp929 = subjects928
                        subjects928 = []
                        for s in tmp929:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp929, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 131573
                                if len(subjects910) == 0:
                                    pass
                                    # State 131574
                                    if len(subjects601) >= 1 and subjects601[0] == -1:
                                        tmp930 = subjects601.popleft()
                                        # State 131575
                                        if len(subjects601) == 0:
                                            pass
                                            # State 131576
                                            if len(subjects) == 0:
                                                pass
                                                # 133: b/sinh(x**n*d + c)
                                        subjects601.appendleft(tmp930)
                        subjects910.appendleft(tmp927)
                    subjects601.appendleft(tmp909)
                subjects.appendleft(tmp600)
            if len(subjects) >= 1 and isinstance(subjects[0], sin):
                tmp931 = subjects.popleft()
                subjects932 = deque(tmp931._args)
                # State 58837
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.2.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 58838
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.2.2.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 58839
                        if len(subjects932) >= 1:
                            tmp935 = subjects932.popleft()
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i2.2.2.1.0', tmp935)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 58840
                                if len(subjects932) == 0:
                                    pass
                                    # State 58841
                                    if len(subjects) == 0:
                                        pass
                                        # 48: b*sin(e + x*f)
                            subjects932.appendleft(tmp935)
                    if len(subjects932) >= 1 and isinstance(subjects932[0], Mul):
                        tmp937 = subjects932.popleft()
                        associative1 = tmp937
                        associative_type1 = type(tmp937)
                        subjects938 = deque(tmp937._args)
                        matcher = CommutativeMatcher58843.get()
                        tmp939 = subjects938
                        subjects938 = []
                        for s in tmp939:
                            matcher.add_subject(s)
                        for pattern_index, subst3 in matcher.match(tmp939, subst2):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 58844
                                if len(subjects932) == 0:
                                    pass
                                    # State 58845
                                    if len(subjects) == 0:
                                        pass
                                        # 48: b*sin(e + x*f)
                        subjects932.appendleft(tmp937)
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.3.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 59019
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.2.3.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 59020
                        if len(subjects932) >= 1:
                            tmp942 = subjects932.popleft()
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i2.2.3.1.0', tmp942)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 59021
                                if len(subjects932) == 0:
                                    pass
                                    # State 59022
                                    if len(subjects) == 0:
                                        pass
                                        # 50: b*sin(e + x*f)
                            subjects932.appendleft(tmp942)
                    if len(subjects932) >= 1 and isinstance(subjects932[0], Mul):
                        tmp944 = subjects932.popleft()
                        associative1 = tmp944
                        associative_type1 = type(tmp944)
                        subjects945 = deque(tmp944._args)
                        matcher = CommutativeMatcher59024.get()
                        tmp946 = subjects945
                        subjects945 = []
                        for s in tmp946:
                            matcher.add_subject(s)
                        for pattern_index, subst3 in matcher.match(tmp946, subst2):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 59025
                                if len(subjects932) == 0:
                                    pass
                                    # State 59026
                                    if len(subjects) == 0:
                                        pass
                                        # 50: b*sin(e + x*f)
                        subjects932.appendleft(tmp944)
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.2.2.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 61490
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.2.2.2.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 61491
                        if len(subjects932) >= 1:
                            tmp949 = subjects932.popleft()
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i2.2.2.2.1.0', tmp949)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 61492
                                if len(subjects932) == 0:
                                    pass
                                    # State 61493
                                    if len(subjects) == 0:
                                        pass
                                        # 54: b*sin(e + x*f)
                            subjects932.appendleft(tmp949)
                    if len(subjects932) >= 1 and isinstance(subjects932[0], Mul):
                        tmp951 = subjects932.popleft()
                        associative1 = tmp951
                        associative_type1 = type(tmp951)
                        subjects952 = deque(tmp951._args)
                        matcher = CommutativeMatcher61495.get()
                        tmp953 = subjects952
                        subjects952 = []
                        for s in tmp953:
                            matcher.add_subject(s)
                        for pattern_index, subst3 in matcher.match(tmp953, subst2):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 61496
                                if len(subjects932) == 0:
                                    pass
                                    # State 61497
                                    if len(subjects) == 0:
                                        pass
                                        # 54: b*sin(e + x*f)
                        subjects932.appendleft(tmp951)
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 74120
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.2.1.2.1.0', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 74121
                        if len(subjects932) >= 1 and isinstance(subjects932[0], Pow):
                            tmp956 = subjects932.popleft()
                            subjects957 = deque(tmp956._args)
                            # State 74122
                            if len(subjects957) >= 1:
                                tmp958 = subjects957.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.2.0_1', tmp958)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 74123
                                    if len(subjects957) >= 1:
                                        tmp960 = subjects957.popleft()
                                        subst5 = Substitution(subst4)
                                        try:
                                            subst5.try_add_variable('i2.2.1.2.1.2', tmp960)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 74124
                                            if len(subjects957) == 0:
                                                pass
                                                # State 74125
                                                if len(subjects932) == 0:
                                                    pass
                                                    # State 74126
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 65: b*sin(x**n*d + c)
                                        subjects957.appendleft(tmp960)
                                subjects957.appendleft(tmp958)
                            if len(subjects957) >= 1:
                                tmp962 = subjects957.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.2.0', tmp962)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 74730
                                    if len(subjects957) >= 1:
                                        tmp964 = subjects957.popleft()
                                        subst5 = Substitution(subst4)
                                        try:
                                            subst5.try_add_variable('i2.2.1.2.1.2', tmp964)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 74731
                                            if len(subjects957) == 0:
                                                pass
                                                # State 74732
                                                if len(subjects932) == 0:
                                                    pass
                                                    # State 74733
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 67: b*sin(x**n*d + c)
                                        subjects957.appendleft(tmp964)
                                subjects957.appendleft(tmp962)
                            if len(subjects957) >= 1:
                                tmp966 = subjects957.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.2.1.2.1.1', tmp966)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 75154
                                    if len(subjects957) >= 1:
                                        tmp968 = subjects957.popleft()
                                        subst5 = Substitution(subst4)
                                        try:
                                            subst5.try_add_variable('i2.2.1.2.1.2', tmp968)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 75155
                                            if len(subjects957) == 0:
                                                pass
                                                # State 75156
                                                if len(subjects932) == 0:
                                                    pass
                                                    # State 75157
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 69: b*sin(c + d*x**n)
                                        subjects957.appendleft(tmp968)
                                subjects957.appendleft(tmp966)
                            subjects932.appendleft(tmp956)
                    if len(subjects932) >= 1 and isinstance(subjects932[0], Mul):
                        tmp970 = subjects932.popleft()
                        associative1 = tmp970
                        associative_type1 = type(tmp970)
                        subjects971 = deque(tmp970._args)
                        matcher = CommutativeMatcher74128.get()
                        tmp972 = subjects971
                        subjects971 = []
                        for s in tmp972:
                            matcher.add_subject(s)
                        for pattern_index, subst3 in matcher.match(tmp972, subst2):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 74133
                                if len(subjects932) == 0:
                                    pass
                                    # State 74134
                                    if len(subjects) == 0:
                                        pass
                                        # 65: b*sin(x**n*d + c)
                            if pattern_index == 1:
                                pass
                                # State 74737
                                if len(subjects932) == 0:
                                    pass
                                    # State 74738
                                    if len(subjects) == 0:
                                        pass
                                        # 67: b*sin(x**n*d + c)
                            if pattern_index == 2:
                                pass
                                # State 75161
                                if len(subjects932) == 0:
                                    pass
                                    # State 75162
                                    if len(subjects) == 0:
                                        pass
                                        # 69: b*sin(c + d*x**n)
                        subjects932.appendleft(tmp970)
                if len(subjects932) >= 1:
                    tmp973 = subjects932.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.1', tmp973)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 75374
                        if len(subjects932) == 0:
                            pass
                            # State 75375
                            if len(subjects) == 0:
                                pass
                                # 71: b*sin(v)
                    subjects932.appendleft(tmp973)
                if len(subjects932) >= 1 and isinstance(subjects932[0], Add):
                    tmp975 = subjects932.popleft()
                    associative1 = tmp975
                    associative_type1 = type(tmp975)
                    subjects976 = deque(tmp975._args)
                    matcher = CommutativeMatcher58847.get()
                    tmp977 = subjects976
                    subjects976 = []
                    for s in tmp977:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp977, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 58853
                            if len(subjects932) == 0:
                                pass
                                # State 58854
                                if len(subjects) == 0:
                                    pass
                                    # 48: b*sin(e + x*f)
                        if pattern_index == 1:
                            pass
                            # State 59030
                            if len(subjects932) == 0:
                                pass
                                # State 59031
                                if len(subjects) == 0:
                                    pass
                                    # 50: b*sin(e + x*f)
                        if pattern_index == 2:
                            pass
                            # State 61501
                            if len(subjects932) == 0:
                                pass
                                # State 61502
                                if len(subjects) == 0:
                                    pass
                                    # 54: b*sin(e + x*f)
                        if pattern_index == 3:
                            pass
                            # State 74145
                            if len(subjects932) == 0:
                                pass
                                # State 74146
                                if len(subjects) == 0:
                                    pass
                                    # 65: b*sin(x**n*d + c)
                        if pattern_index == 4:
                            pass
                            # State 74746
                            if len(subjects932) == 0:
                                pass
                                # State 74747
                                if len(subjects) == 0:
                                    pass
                                    # 67: b*sin(x**n*d + c)
                        if pattern_index == 5:
                            pass
                            # State 75170
                            if len(subjects932) == 0:
                                pass
                                # State 75171
                                if len(subjects) == 0:
                                    pass
                                    # 69: b*sin(c + d*x**n)
                    subjects932.appendleft(tmp975)
                subjects.appendleft(tmp931)
            if len(subjects) >= 1 and isinstance(subjects[0], cos):
                tmp978 = subjects.popleft()
                subjects979 = deque(tmp978._args)
                # State 58880
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.2.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 58881
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.2.2.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 58882
                        if len(subjects979) >= 1:
                            tmp982 = subjects979.popleft()
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i2.2.2.1.0', tmp982)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 58883
                                if len(subjects979) == 0:
                                    pass
                                    # State 58884
                                    if len(subjects) == 0:
                                        pass
                                        # 49: b*cos(e + x*f)
                            subjects979.appendleft(tmp982)
                    if len(subjects979) >= 1 and isinstance(subjects979[0], Mul):
                        tmp984 = subjects979.popleft()
                        associative1 = tmp984
                        associative_type1 = type(tmp984)
                        subjects985 = deque(tmp984._args)
                        matcher = CommutativeMatcher58886.get()
                        tmp986 = subjects985
                        subjects985 = []
                        for s in tmp986:
                            matcher.add_subject(s)
                        for pattern_index, subst3 in matcher.match(tmp986, subst2):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 58887
                                if len(subjects979) == 0:
                                    pass
                                    # State 58888
                                    if len(subjects) == 0:
                                        pass
                                        # 49: b*cos(e + x*f)
                        subjects979.appendleft(tmp984)
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.3.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 59080
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.2.3.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 59081
                        if len(subjects979) >= 1:
                            tmp989 = subjects979.popleft()
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i2.2.3.1.0', tmp989)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 59082
                                if len(subjects979) == 0:
                                    pass
                                    # State 59083
                                    if len(subjects) == 0:
                                        pass
                                        # 51: b*cos(e + x*f)
                            subjects979.appendleft(tmp989)
                    if len(subjects979) >= 1 and isinstance(subjects979[0], Mul):
                        tmp991 = subjects979.popleft()
                        associative1 = tmp991
                        associative_type1 = type(tmp991)
                        subjects992 = deque(tmp991._args)
                        matcher = CommutativeMatcher59085.get()
                        tmp993 = subjects992
                        subjects992 = []
                        for s in tmp993:
                            matcher.add_subject(s)
                        for pattern_index, subst3 in matcher.match(tmp993, subst2):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 59086
                                if len(subjects979) == 0:
                                    pass
                                    # State 59087
                                    if len(subjects) == 0:
                                        pass
                                        # 51: b*cos(e + x*f)
                        subjects979.appendleft(tmp991)
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.2.2.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 61719
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.2.2.2.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 61720
                        if len(subjects979) >= 1:
                            tmp996 = subjects979.popleft()
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i2.2.2.2.1.0', tmp996)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 61721
                                if len(subjects979) == 0:
                                    pass
                                    # State 61722
                                    if len(subjects) == 0:
                                        pass
                                        # 55: b*cos(e + x*f)
                            subjects979.appendleft(tmp996)
                    if len(subjects979) >= 1 and isinstance(subjects979[0], Mul):
                        tmp998 = subjects979.popleft()
                        associative1 = tmp998
                        associative_type1 = type(tmp998)
                        subjects999 = deque(tmp998._args)
                        matcher = CommutativeMatcher61724.get()
                        tmp1000 = subjects999
                        subjects999 = []
                        for s in tmp1000:
                            matcher.add_subject(s)
                        for pattern_index, subst3 in matcher.match(tmp1000, subst2):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 61725
                                if len(subjects979) == 0:
                                    pass
                                    # State 61726
                                    if len(subjects) == 0:
                                        pass
                                        # 55: b*cos(e + x*f)
                        subjects979.appendleft(tmp998)
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 74347
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.2.1.2.1.0', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 74348
                        if len(subjects979) >= 1 and isinstance(subjects979[0], Pow):
                            tmp1003 = subjects979.popleft()
                            subjects1004 = deque(tmp1003._args)
                            # State 74349
                            if len(subjects1004) >= 1:
                                tmp1005 = subjects1004.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.2.0_1', tmp1005)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 74350
                                    if len(subjects1004) >= 1:
                                        tmp1007 = subjects1004.popleft()
                                        subst5 = Substitution(subst4)
                                        try:
                                            subst5.try_add_variable('i2.2.1.2.1.2', tmp1007)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 74351
                                            if len(subjects1004) == 0:
                                                pass
                                                # State 74352
                                                if len(subjects979) == 0:
                                                    pass
                                                    # State 74353
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 66: b*cos(x**n*d + c)
                                        subjects1004.appendleft(tmp1007)
                                subjects1004.appendleft(tmp1005)
                            if len(subjects1004) >= 1:
                                tmp1009 = subjects1004.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.2.0', tmp1009)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 74893
                                    if len(subjects1004) >= 1:
                                        tmp1011 = subjects1004.popleft()
                                        subst5 = Substitution(subst4)
                                        try:
                                            subst5.try_add_variable('i2.2.1.2.1.2', tmp1011)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 74894
                                            if len(subjects1004) == 0:
                                                pass
                                                # State 74895
                                                if len(subjects979) == 0:
                                                    pass
                                                    # State 74896
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 68: b*cos(x**n*d + c)
                                        subjects1004.appendleft(tmp1011)
                                subjects1004.appendleft(tmp1009)
                            if len(subjects1004) >= 1:
                                tmp1013 = subjects1004.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.2.1.2.1.1', tmp1013)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 75280
                                    if len(subjects1004) >= 1:
                                        tmp1015 = subjects1004.popleft()
                                        subst5 = Substitution(subst4)
                                        try:
                                            subst5.try_add_variable('i2.2.1.2.1.2', tmp1015)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 75281
                                            if len(subjects1004) == 0:
                                                pass
                                                # State 75282
                                                if len(subjects979) == 0:
                                                    pass
                                                    # State 75283
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 70: b*cos(c + d*x**n)
                                        subjects1004.appendleft(tmp1015)
                                subjects1004.appendleft(tmp1013)
                            subjects979.appendleft(tmp1003)
                    if len(subjects979) >= 1 and isinstance(subjects979[0], Mul):
                        tmp1017 = subjects979.popleft()
                        associative1 = tmp1017
                        associative_type1 = type(tmp1017)
                        subjects1018 = deque(tmp1017._args)
                        matcher = CommutativeMatcher74355.get()
                        tmp1019 = subjects1018
                        subjects1018 = []
                        for s in tmp1019:
                            matcher.add_subject(s)
                        for pattern_index, subst3 in matcher.match(tmp1019, subst2):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 74360
                                if len(subjects979) == 0:
                                    pass
                                    # State 74361
                                    if len(subjects) == 0:
                                        pass
                                        # 66: b*cos(x**n*d + c)
                            if pattern_index == 1:
                                pass
                                # State 74900
                                if len(subjects979) == 0:
                                    pass
                                    # State 74901
                                    if len(subjects) == 0:
                                        pass
                                        # 68: b*cos(x**n*d + c)
                            if pattern_index == 2:
                                pass
                                # State 75287
                                if len(subjects979) == 0:
                                    pass
                                    # State 75288
                                    if len(subjects) == 0:
                                        pass
                                        # 70: b*cos(c + d*x**n)
                        subjects979.appendleft(tmp1017)
                if len(subjects979) >= 1:
                    tmp1020 = subjects979.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.1', tmp1020)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 75400
                        if len(subjects979) == 0:
                            pass
                            # State 75401
                            if len(subjects) == 0:
                                pass
                                # 72: b*cos(v)
                    subjects979.appendleft(tmp1020)
                if len(subjects979) >= 1 and isinstance(subjects979[0], Add):
                    tmp1022 = subjects979.popleft()
                    associative1 = tmp1022
                    associative_type1 = type(tmp1022)
                    subjects1023 = deque(tmp1022._args)
                    matcher = CommutativeMatcher58890.get()
                    tmp1024 = subjects1023
                    subjects1023 = []
                    for s in tmp1024:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp1024, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 58896
                            if len(subjects979) == 0:
                                pass
                                # State 58897
                                if len(subjects) == 0:
                                    pass
                                    # 49: b*cos(e + x*f)
                        if pattern_index == 1:
                            pass
                            # State 59091
                            if len(subjects979) == 0:
                                pass
                                # State 59092
                                if len(subjects) == 0:
                                    pass
                                    # 51: b*cos(e + x*f)
                        if pattern_index == 2:
                            pass
                            # State 61730
                            if len(subjects979) == 0:
                                pass
                                # State 61731
                                if len(subjects) == 0:
                                    pass
                                    # 55: b*cos(e + x*f)
                        if pattern_index == 3:
                            pass
                            # State 74372
                            if len(subjects979) == 0:
                                pass
                                # State 74373
                                if len(subjects) == 0:
                                    pass
                                    # 66: b*cos(x**n*d + c)
                        if pattern_index == 4:
                            pass
                            # State 74909
                            if len(subjects979) == 0:
                                pass
                                # State 74910
                                if len(subjects) == 0:
                                    pass
                                    # 68: b*cos(x**n*d + c)
                        if pattern_index == 5:
                            pass
                            # State 75296
                            if len(subjects979) == 0:
                                pass
                                # State 75297
                                if len(subjects) == 0:
                                    pass
                                    # 70: b*cos(c + d*x**n)
                    subjects979.appendleft(tmp1022)
                subjects.appendleft(tmp978)
            if len(subjects) >= 1 and isinstance(subjects[0], tan):
                tmp1025 = subjects.popleft()
                subjects1026 = deque(tmp1025._args)
                # State 77997
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.3.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 77998
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.2.3.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 77999
                        if len(subjects1026) >= 1:
                            tmp1029 = subjects1026.popleft()
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i2.2.3.1.0', tmp1029)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 78000
                                if len(subjects1026) == 0:
                                    pass
                                    # State 78001
                                    if len(subjects) == 0:
                                        pass
                                        # 73: b*tan(e + x*f)
                            subjects1026.appendleft(tmp1029)
                    if len(subjects1026) >= 1 and isinstance(subjects1026[0], Mul):
                        tmp1031 = subjects1026.popleft()
                        associative1 = tmp1031
                        associative_type1 = type(tmp1031)
                        subjects1032 = deque(tmp1031._args)
                        matcher = CommutativeMatcher78003.get()
                        tmp1033 = subjects1032
                        subjects1032 = []
                        for s in tmp1033:
                            matcher.add_subject(s)
                        for pattern_index, subst3 in matcher.match(tmp1033, subst2):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 78004
                                if len(subjects1026) == 0:
                                    pass
                                    # State 78005
                                    if len(subjects) == 0:
                                        pass
                                        # 73: b*tan(e + x*f)
                        subjects1026.appendleft(tmp1031)
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.2.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 78265
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.2.2.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 78266
                        if len(subjects1026) >= 1:
                            tmp1036 = subjects1026.popleft()
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i2.2.2.1.0', tmp1036)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 78267
                                if len(subjects1026) == 0:
                                    pass
                                    # State 78268
                                    if len(subjects) == 0:
                                        pass
                                        # 75: b*tan(e + x*f)
                            subjects1026.appendleft(tmp1036)
                    if len(subjects1026) >= 1 and isinstance(subjects1026[0], Mul):
                        tmp1038 = subjects1026.popleft()
                        associative1 = tmp1038
                        associative_type1 = type(tmp1038)
                        subjects1039 = deque(tmp1038._args)
                        matcher = CommutativeMatcher78270.get()
                        tmp1040 = subjects1039
                        subjects1039 = []
                        for s in tmp1040:
                            matcher.add_subject(s)
                        for pattern_index, subst3 in matcher.match(tmp1040, subst2):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 78271
                                if len(subjects1026) == 0:
                                    pass
                                    # State 78272
                                    if len(subjects) == 0:
                                        pass
                                        # 75: b*tan(e + x*f)
                        subjects1026.appendleft(tmp1038)
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.2.2.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 80067
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.2.2.2.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 80068
                        if len(subjects1026) >= 1:
                            tmp1043 = subjects1026.popleft()
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i2.2.2.2.1.0', tmp1043)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 80069
                                if len(subjects1026) == 0:
                                    pass
                                    # State 80070
                                    if len(subjects) == 0:
                                        pass
                                        # 79: b*tan(e + x*f)
                            subjects1026.appendleft(tmp1043)
                    if len(subjects1026) >= 1 and isinstance(subjects1026[0], Mul):
                        tmp1045 = subjects1026.popleft()
                        associative1 = tmp1045
                        associative_type1 = type(tmp1045)
                        subjects1046 = deque(tmp1045._args)
                        matcher = CommutativeMatcher80072.get()
                        tmp1047 = subjects1046
                        subjects1046 = []
                        for s in tmp1047:
                            matcher.add_subject(s)
                        for pattern_index, subst3 in matcher.match(tmp1047, subst2):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 80073
                                if len(subjects1026) == 0:
                                    pass
                                    # State 80074
                                    if len(subjects) == 0:
                                        pass
                                        # 79: b*tan(e + x*f)
                        subjects1026.appendleft(tmp1045)
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 88518
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.2.1.2.1.0', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 88519
                        if len(subjects1026) >= 1 and isinstance(subjects1026[0], Pow):
                            tmp1050 = subjects1026.popleft()
                            subjects1051 = deque(tmp1050._args)
                            # State 88520
                            if len(subjects1051) >= 1:
                                tmp1052 = subjects1051.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.2.0_1', tmp1052)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 88521
                                    if len(subjects1051) >= 1:
                                        tmp1054 = subjects1051.popleft()
                                        subst5 = Substitution(subst4)
                                        try:
                                            subst5.try_add_variable('i2.2.1.2.1.2', tmp1054)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 88522
                                            if len(subjects1051) == 0:
                                                pass
                                                # State 88523
                                                if len(subjects1026) == 0:
                                                    pass
                                                    # State 88524
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 86: b*tan(x**n*d + c)
                                        subjects1051.appendleft(tmp1054)
                                subjects1051.appendleft(tmp1052)
                            subjects1026.appendleft(tmp1050)
                    if len(subjects1026) >= 1 and isinstance(subjects1026[0], Mul):
                        tmp1056 = subjects1026.popleft()
                        associative1 = tmp1056
                        associative_type1 = type(tmp1056)
                        subjects1057 = deque(tmp1056._args)
                        matcher = CommutativeMatcher88526.get()
                        tmp1058 = subjects1057
                        subjects1057 = []
                        for s in tmp1058:
                            matcher.add_subject(s)
                        for pattern_index, subst3 in matcher.match(tmp1058, subst2):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 88531
                                if len(subjects1026) == 0:
                                    pass
                                    # State 88532
                                    if len(subjects) == 0:
                                        pass
                                        # 86: b*tan(x**n*d + c)
                        subjects1026.appendleft(tmp1056)
                if len(subjects1026) >= 1:
                    tmp1059 = subjects1026.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.1', tmp1059)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 88972
                        if len(subjects1026) == 0:
                            pass
                            # State 88973
                            if len(subjects) == 0:
                                pass
                                # 88: b*tan(v)
                    subjects1026.appendleft(tmp1059)
                if len(subjects1026) >= 1 and isinstance(subjects1026[0], Add):
                    tmp1061 = subjects1026.popleft()
                    associative1 = tmp1061
                    associative_type1 = type(tmp1061)
                    subjects1062 = deque(tmp1061._args)
                    matcher = CommutativeMatcher78007.get()
                    tmp1063 = subjects1062
                    subjects1062 = []
                    for s in tmp1063:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp1063, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 78013
                            if len(subjects1026) == 0:
                                pass
                                # State 78014
                                if len(subjects) == 0:
                                    pass
                                    # 73: b*tan(e + x*f)
                        if pattern_index == 1:
                            pass
                            # State 78276
                            if len(subjects1026) == 0:
                                pass
                                # State 78277
                                if len(subjects) == 0:
                                    pass
                                    # 75: b*tan(e + x*f)
                        if pattern_index == 2:
                            pass
                            # State 80078
                            if len(subjects1026) == 0:
                                pass
                                # State 80079
                                if len(subjects) == 0:
                                    pass
                                    # 79: b*tan(e + x*f)
                        if pattern_index == 3:
                            pass
                            # State 88543
                            if len(subjects1026) == 0:
                                pass
                                # State 88544
                                if len(subjects) == 0:
                                    pass
                                    # 86: b*tan(x**n*d + c)
                    subjects1026.appendleft(tmp1061)
                subjects.appendleft(tmp1025)
            if len(subjects) >= 1 and isinstance(subjects[0], asin):
                tmp1064 = subjects.popleft()
                subjects1065 = deque(tmp1064._args)
                # State 108377
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.0', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 108378
                    if len(subjects1065) >= 1:
                        tmp1067 = subjects1065.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.0', tmp1067)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 108379
                            if len(subjects1065) == 0:
                                pass
                                # State 108380
                                if len(subjects) == 0:
                                    pass
                                    # 100: b*asin(x*c)
                        subjects1065.appendleft(tmp1067)
                if len(subjects1065) >= 1 and isinstance(subjects1065[0], Mul):
                    tmp1069 = subjects1065.popleft()
                    associative1 = tmp1069
                    associative_type1 = type(tmp1069)
                    subjects1070 = deque(tmp1069._args)
                    matcher = CommutativeMatcher108382.get()
                    tmp1071 = subjects1070
                    subjects1070 = []
                    for s in tmp1071:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp1071, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 108383
                            if len(subjects1065) == 0:
                                pass
                                # State 108384
                                if len(subjects) == 0:
                                    pass
                                    # 100: b*asin(x*c)
                    subjects1065.appendleft(tmp1069)
                subjects.appendleft(tmp1064)
            if len(subjects) >= 1 and isinstance(subjects[0], acos):
                tmp1072 = subjects.popleft()
                subjects1073 = deque(tmp1072._args)
                # State 108452
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.0', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 108453
                    if len(subjects1073) >= 1:
                        tmp1075 = subjects1073.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.0', tmp1075)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 108454
                            if len(subjects1073) == 0:
                                pass
                                # State 108455
                                if len(subjects) == 0:
                                    pass
                                    # 101: b*acos(x*c)
                        subjects1073.appendleft(tmp1075)
                if len(subjects1073) >= 1 and isinstance(subjects1073[0], Mul):
                    tmp1077 = subjects1073.popleft()
                    associative1 = tmp1077
                    associative_type1 = type(tmp1077)
                    subjects1078 = deque(tmp1077._args)
                    matcher = CommutativeMatcher108457.get()
                    tmp1079 = subjects1078
                    subjects1078 = []
                    for s in tmp1079:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp1079, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 108458
                            if len(subjects1073) == 0:
                                pass
                                # State 108459
                                if len(subjects) == 0:
                                    pass
                                    # 101: b*acos(x*c)
                    subjects1073.appendleft(tmp1077)
                subjects.appendleft(tmp1072)
            if len(subjects) >= 1 and isinstance(subjects[0], sinh):
                tmp1080 = subjects.popleft()
                subjects1081 = deque(tmp1080._args)
                # State 124038
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 124039
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.2.1.2.1.0', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 124040
                        if len(subjects1081) >= 1 and isinstance(subjects1081[0], Pow):
                            tmp1084 = subjects1081.popleft()
                            subjects1085 = deque(tmp1084._args)
                            # State 124041
                            if len(subjects1085) >= 1:
                                tmp1086 = subjects1085.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.2.0_1', tmp1086)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 124042
                                    if len(subjects1085) >= 1:
                                        tmp1088 = subjects1085.popleft()
                                        subst5 = Substitution(subst4)
                                        try:
                                            subst5.try_add_variable('i2.2.1.2.1.2', tmp1088)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 124043
                                            if len(subjects1085) == 0:
                                                pass
                                                # State 124044
                                                if len(subjects1081) == 0:
                                                    pass
                                                    # State 124045
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 119: b*sinh(x**n*d + c)
                                        subjects1085.appendleft(tmp1088)
                                subjects1085.appendleft(tmp1086)
                            if len(subjects1085) >= 1:
                                tmp1090 = subjects1085.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.2.0', tmp1090)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 124640
                                    if len(subjects1085) >= 1:
                                        tmp1092 = subjects1085.popleft()
                                        subst5 = Substitution(subst4)
                                        try:
                                            subst5.try_add_variable('i2.2.1.2.1.2', tmp1092)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 124641
                                            if len(subjects1085) == 0:
                                                pass
                                                # State 124642
                                                if len(subjects1081) == 0:
                                                    pass
                                                    # State 124643
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 121: b*sinh(x**n*d + c)
                                        subjects1085.appendleft(tmp1092)
                                subjects1085.appendleft(tmp1090)
                            if len(subjects1085) >= 1:
                                tmp1094 = subjects1085.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.2.1.2.1.1', tmp1094)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 125064
                                    if len(subjects1085) >= 1:
                                        tmp1096 = subjects1085.popleft()
                                        subst5 = Substitution(subst4)
                                        try:
                                            subst5.try_add_variable('i2.2.1.2.1.2', tmp1096)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 125065
                                            if len(subjects1085) == 0:
                                                pass
                                                # State 125066
                                                if len(subjects1081) == 0:
                                                    pass
                                                    # State 125067
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 123: b*sinh(c + d*x**n)
                                        subjects1085.appendleft(tmp1096)
                                subjects1085.appendleft(tmp1094)
                            subjects1081.appendleft(tmp1084)
                    if len(subjects1081) >= 1 and isinstance(subjects1081[0], Mul):
                        tmp1098 = subjects1081.popleft()
                        associative1 = tmp1098
                        associative_type1 = type(tmp1098)
                        subjects1099 = deque(tmp1098._args)
                        matcher = CommutativeMatcher124047.get()
                        tmp1100 = subjects1099
                        subjects1099 = []
                        for s in tmp1100:
                            matcher.add_subject(s)
                        for pattern_index, subst3 in matcher.match(tmp1100, subst2):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 124052
                                if len(subjects1081) == 0:
                                    pass
                                    # State 124053
                                    if len(subjects) == 0:
                                        pass
                                        # 119: b*sinh(x**n*d + c)
                            if pattern_index == 1:
                                pass
                                # State 124647
                                if len(subjects1081) == 0:
                                    pass
                                    # State 124648
                                    if len(subjects) == 0:
                                        pass
                                        # 121: b*sinh(x**n*d + c)
                            if pattern_index == 2:
                                pass
                                # State 125071
                                if len(subjects1081) == 0:
                                    pass
                                    # State 125072
                                    if len(subjects) == 0:
                                        pass
                                        # 123: b*sinh(c + d*x**n)
                        subjects1081.appendleft(tmp1098)
                if len(subjects1081) >= 1:
                    tmp1101 = subjects1081.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.1', tmp1101)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 125284
                        if len(subjects1081) == 0:
                            pass
                            # State 125285
                            if len(subjects) == 0:
                                pass
                                # 125: b*sinh(v)
                    subjects1081.appendleft(tmp1101)
                if len(subjects1081) >= 1 and isinstance(subjects1081[0], Add):
                    tmp1103 = subjects1081.popleft()
                    associative1 = tmp1103
                    associative_type1 = type(tmp1103)
                    subjects1104 = deque(tmp1103._args)
                    matcher = CommutativeMatcher124055.get()
                    tmp1105 = subjects1104
                    subjects1104 = []
                    for s in tmp1105:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp1105, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 124068
                            if len(subjects1081) == 0:
                                pass
                                # State 124069
                                if len(subjects) == 0:
                                    pass
                                    # 119: b*sinh(x**n*d + c)
                        if pattern_index == 1:
                            pass
                            # State 124656
                            if len(subjects1081) == 0:
                                pass
                                # State 124657
                                if len(subjects) == 0:
                                    pass
                                    # 121: b*sinh(x**n*d + c)
                        if pattern_index == 2:
                            pass
                            # State 125080
                            if len(subjects1081) == 0:
                                pass
                                # State 125081
                                if len(subjects) == 0:
                                    pass
                                    # 123: b*sinh(c + d*x**n)
                    subjects1081.appendleft(tmp1103)
                subjects.appendleft(tmp1080)
            if len(subjects) >= 1 and isinstance(subjects[0], cosh):
                tmp1106 = subjects.popleft()
                subjects1107 = deque(tmp1106._args)
                # State 124275
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 124276
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.2.1.2.1.0', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 124277
                        if len(subjects1107) >= 1 and isinstance(subjects1107[0], Pow):
                            tmp1110 = subjects1107.popleft()
                            subjects1111 = deque(tmp1110._args)
                            # State 124278
                            if len(subjects1111) >= 1:
                                tmp1112 = subjects1111.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.2.0_1', tmp1112)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 124279
                                    if len(subjects1111) >= 1:
                                        tmp1114 = subjects1111.popleft()
                                        subst5 = Substitution(subst4)
                                        try:
                                            subst5.try_add_variable('i2.2.1.2.1.2', tmp1114)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 124280
                                            if len(subjects1111) == 0:
                                                pass
                                                # State 124281
                                                if len(subjects1107) == 0:
                                                    pass
                                                    # State 124282
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 120: b*cosh(x**n*d + c)
                                        subjects1111.appendleft(tmp1114)
                                subjects1111.appendleft(tmp1112)
                            if len(subjects1111) >= 1:
                                tmp1116 = subjects1111.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.2.0', tmp1116)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 124803
                                    if len(subjects1111) >= 1:
                                        tmp1118 = subjects1111.popleft()
                                        subst5 = Substitution(subst4)
                                        try:
                                            subst5.try_add_variable('i2.2.1.2.1.2', tmp1118)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 124804
                                            if len(subjects1111) == 0:
                                                pass
                                                # State 124805
                                                if len(subjects1107) == 0:
                                                    pass
                                                    # State 124806
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 122: b*cosh(x**n*d + c)
                                        subjects1111.appendleft(tmp1118)
                                subjects1111.appendleft(tmp1116)
                            if len(subjects1111) >= 1:
                                tmp1120 = subjects1111.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.2.1.2.1.1', tmp1120)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 125190
                                    if len(subjects1111) >= 1:
                                        tmp1122 = subjects1111.popleft()
                                        subst5 = Substitution(subst4)
                                        try:
                                            subst5.try_add_variable('i2.2.1.2.1.2', tmp1122)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 125191
                                            if len(subjects1111) == 0:
                                                pass
                                                # State 125192
                                                if len(subjects1107) == 0:
                                                    pass
                                                    # State 125193
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 124: b*cosh(c + d*x**n)
                                        subjects1111.appendleft(tmp1122)
                                subjects1111.appendleft(tmp1120)
                            subjects1107.appendleft(tmp1110)
                    if len(subjects1107) >= 1 and isinstance(subjects1107[0], Mul):
                        tmp1124 = subjects1107.popleft()
                        associative1 = tmp1124
                        associative_type1 = type(tmp1124)
                        subjects1125 = deque(tmp1124._args)
                        matcher = CommutativeMatcher124284.get()
                        tmp1126 = subjects1125
                        subjects1125 = []
                        for s in tmp1126:
                            matcher.add_subject(s)
                        for pattern_index, subst3 in matcher.match(tmp1126, subst2):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 124289
                                if len(subjects1107) == 0:
                                    pass
                                    # State 124290
                                    if len(subjects) == 0:
                                        pass
                                        # 120: b*cosh(x**n*d + c)
                            if pattern_index == 1:
                                pass
                                # State 124810
                                if len(subjects1107) == 0:
                                    pass
                                    # State 124811
                                    if len(subjects) == 0:
                                        pass
                                        # 122: b*cosh(x**n*d + c)
                            if pattern_index == 2:
                                pass
                                # State 125197
                                if len(subjects1107) == 0:
                                    pass
                                    # State 125198
                                    if len(subjects) == 0:
                                        pass
                                        # 124: b*cosh(c + d*x**n)
                        subjects1107.appendleft(tmp1124)
                if len(subjects1107) >= 1:
                    tmp1127 = subjects1107.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.1', tmp1127)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 125310
                        if len(subjects1107) == 0:
                            pass
                            # State 125311
                            if len(subjects) == 0:
                                pass
                                # 126: b*cosh(v)
                    subjects1107.appendleft(tmp1127)
                if len(subjects1107) >= 1 and isinstance(subjects1107[0], Add):
                    tmp1129 = subjects1107.popleft()
                    associative1 = tmp1129
                    associative_type1 = type(tmp1129)
                    subjects1130 = deque(tmp1129._args)
                    matcher = CommutativeMatcher124292.get()
                    tmp1131 = subjects1130
                    subjects1130 = []
                    for s in tmp1131:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp1131, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 124305
                            if len(subjects1107) == 0:
                                pass
                                # State 124306
                                if len(subjects) == 0:
                                    pass
                                    # 120: b*cosh(x**n*d + c)
                        if pattern_index == 1:
                            pass
                            # State 124819
                            if len(subjects1107) == 0:
                                pass
                                # State 124820
                                if len(subjects) == 0:
                                    pass
                                    # 122: b*cosh(x**n*d + c)
                        if pattern_index == 2:
                            pass
                            # State 125206
                            if len(subjects1107) == 0:
                                pass
                                # State 125207
                                if len(subjects) == 0:
                                    pass
                                    # 124: b*cosh(c + d*x**n)
                    subjects1107.appendleft(tmp1129)
                subjects.appendleft(tmp1106)
            if len(subjects) >= 1 and isinstance(subjects[0], tanh):
                tmp1132 = subjects.popleft()
                subjects1133 = deque(tmp1132._args)
                # State 128051
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 128052
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.2.1.2.1.0', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 128053
                        if len(subjects1133) >= 1 and isinstance(subjects1133[0], Pow):
                            tmp1136 = subjects1133.popleft()
                            subjects1137 = deque(tmp1136._args)
                            # State 128054
                            if len(subjects1137) >= 1:
                                tmp1138 = subjects1137.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.2.0_1', tmp1138)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 128055
                                    if len(subjects1137) >= 1:
                                        tmp1140 = subjects1137.popleft()
                                        subst5 = Substitution(subst4)
                                        try:
                                            subst5.try_add_variable('i2.2.1.2.1.2', tmp1140)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 128056
                                            if len(subjects1137) == 0:
                                                pass
                                                # State 128057
                                                if len(subjects1133) == 0:
                                                    pass
                                                    # State 128058
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 128: b*tanh(x**n*d + c)
                                        subjects1137.appendleft(tmp1140)
                                subjects1137.appendleft(tmp1138)
                            subjects1133.appendleft(tmp1136)
                    if len(subjects1133) >= 1 and isinstance(subjects1133[0], Mul):
                        tmp1142 = subjects1133.popleft()
                        associative1 = tmp1142
                        associative_type1 = type(tmp1142)
                        subjects1143 = deque(tmp1142._args)
                        matcher = CommutativeMatcher128060.get()
                        tmp1144 = subjects1143
                        subjects1143 = []
                        for s in tmp1144:
                            matcher.add_subject(s)
                        for pattern_index, subst3 in matcher.match(tmp1144, subst2):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 128065
                                if len(subjects1133) == 0:
                                    pass
                                    # State 128066
                                    if len(subjects) == 0:
                                        pass
                                        # 128: b*tanh(x**n*d + c)
                        subjects1133.appendleft(tmp1142)
                if len(subjects1133) >= 1:
                    tmp1145 = subjects1133.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.1', tmp1145)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 128523
                        if len(subjects1133) == 0:
                            pass
                            # State 128524
                            if len(subjects) == 0:
                                pass
                                # 130: b*tanh(v)
                    subjects1133.appendleft(tmp1145)
                if len(subjects1133) >= 1 and isinstance(subjects1133[0], Add):
                    tmp1147 = subjects1133.popleft()
                    associative1 = tmp1147
                    associative_type1 = type(tmp1147)
                    subjects1148 = deque(tmp1147._args)
                    matcher = CommutativeMatcher128068.get()
                    tmp1149 = subjects1148
                    subjects1148 = []
                    for s in tmp1149:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp1149, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 128081
                            if len(subjects1133) == 0:
                                pass
                                # State 128082
                                if len(subjects) == 0:
                                    pass
                                    # 128: b*tanh(x**n*d + c)
                    subjects1133.appendleft(tmp1147)
                subjects.appendleft(tmp1132)
            if len(subjects) >= 1 and isinstance(subjects[0], asinh):
                tmp1150 = subjects.popleft()
                subjects1151 = deque(tmp1150._args)
                # State 138113
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.0', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 138114
                    if len(subjects1151) >= 1:
                        tmp1153 = subjects1151.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.0', tmp1153)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 138115
                            if len(subjects1151) == 0:
                                pass
                                # State 138116
                                if len(subjects) == 0:
                                    pass
                                    # 137: b*asinh(x*c)
                        subjects1151.appendleft(tmp1153)
                if len(subjects1151) >= 1 and isinstance(subjects1151[0], Mul):
                    tmp1155 = subjects1151.popleft()
                    associative1 = tmp1155
                    associative_type1 = type(tmp1155)
                    subjects1156 = deque(tmp1155._args)
                    matcher = CommutativeMatcher138118.get()
                    tmp1157 = subjects1156
                    subjects1156 = []
                    for s in tmp1157:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp1157, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 138119
                            if len(subjects1151) == 0:
                                pass
                                # State 138120
                                if len(subjects) == 0:
                                    pass
                                    # 137: b*asinh(x*c)
                    subjects1151.appendleft(tmp1155)
                subjects.appendleft(tmp1150)
            if len(subjects) >= 1 and isinstance(subjects[0], acosh):
                tmp1158 = subjects.popleft()
                subjects1159 = deque(tmp1158._args)
                # State 138188
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.0', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 138189
                    if len(subjects1159) >= 1:
                        tmp1161 = subjects1159.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.0', tmp1161)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 138190
                            if len(subjects1159) == 0:
                                pass
                                # State 138191
                                if len(subjects) == 0:
                                    pass
                                    # 138: b*acosh(x*c)
                        subjects1159.appendleft(tmp1161)
                if len(subjects1159) >= 1 and isinstance(subjects1159[0], Mul):
                    tmp1163 = subjects1159.popleft()
                    associative1 = tmp1163
                    associative_type1 = type(tmp1163)
                    subjects1164 = deque(tmp1163._args)
                    matcher = CommutativeMatcher138193.get()
                    tmp1165 = subjects1164
                    subjects1164 = []
                    for s in tmp1165:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp1165, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 138194
                            if len(subjects1159) == 0:
                                pass
                                # State 138195
                                if len(subjects) == 0:
                                    pass
                                    # 138: b*acosh(x*c)
                    subjects1159.appendleft(tmp1163)
                subjects.appendleft(tmp1158)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.0_3', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 3318
            if len(subjects) >= 1:
                tmp1167 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.0', tmp1167)
                except ValueError:
                    pass
                else:
                    pass
                    # State 3319
                    if len(subjects) == 0:
                        pass
                        # 3: x*f
                subjects.appendleft(tmp1167)
            if len(subjects) >= 1:
                tmp1169 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.1', tmp1169)
                except ValueError:
                    pass
                else:
                    pass
                    # State 5297
                    if len(subjects) == 0:
                        pass
                        # 9: e*x
                subjects.appendleft(tmp1169)
            subst2 = Substitution(subst1)
            try:
                subst2.try_add_variable('i2.2.1.2_2', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 7569
                if len(subjects) >= 1:
                    tmp1172 = subjects.popleft()
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.2.1.1', tmp1172)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 7570
                        if len(subjects) == 0:
                            pass
                            # 18: e*x**r
                    subjects.appendleft(tmp1172)
            if len(subjects) >= 1:
                tmp1174 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.1.1', tmp1174)
                except ValueError:
                    pass
                else:
                    pass
                    # State 13956
                    if len(subjects) == 0:
                        pass
                        # 37: h*x
                subjects.appendleft(tmp1174)
            if len(subjects) >= 1:
                tmp1176 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.0', tmp1176)
                except ValueError:
                    pass
                else:
                    pass
                    # State 109634
                    if len(subjects) == 0:
                        pass
                        # 108: g*x
                subjects.appendleft(tmp1176)
            if len(subjects) >= 1:
                tmp1178 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.0_2', tmp1178)
                except ValueError:
                    pass
                else:
                    pass
                    # State 151659
                    if len(subjects) == 0:
                        pass
                        # 148: y*b
                subjects.appendleft(tmp1178)
            if len(subjects) >= 1 and isinstance(subjects[0], Pow):
                tmp1180 = subjects.popleft()
                subjects1181 = deque(tmp1180._args)
                # State 7571
                if len(subjects1181) >= 1:
                    tmp1182 = subjects1181.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.1', tmp1182)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 7572
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.2_2', 1)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 7573
                            if len(subjects1181) == 0:
                                pass
                                # State 7574
                                if len(subjects) == 0:
                                    pass
                                    # 18: e*x**r
                        if len(subjects1181) >= 1:
                            tmp1185 = subjects1181.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.2_2', tmp1185)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 7573
                                if len(subjects1181) == 0:
                                    pass
                                    # State 7574
                                    if len(subjects) == 0:
                                        pass
                                        # 18: e*x**r
                            subjects1181.appendleft(tmp1185)
                        if len(subjects1181) >= 1:
                            tmp1187 = subjects1181.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.2_2', tmp1187)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 9109
                                if len(subjects1181) == 0:
                                    pass
                                    # State 9110
                                    if len(subjects) == 0:
                                        pass
                                        # 27: c*x**n2
                            subjects1181.appendleft(tmp1187)
                    subjects1181.appendleft(tmp1182)
                subjects.appendleft(tmp1180)
        if len(subjects) >= 1 and isinstance(subjects[0], Mul):
            tmp1189 = subjects.popleft()
            associative1 = tmp1189
            associative_type1 = type(tmp1189)
            subjects1190 = deque(tmp1189._args)
            matcher = CommutativeMatcher2617.get()
            tmp1191 = subjects1190
            subjects1190 = []
            for s in tmp1191:
                matcher.add_subject(s)
            for pattern_index, subst1 in matcher.match(tmp1191, subst0):
                pass
                if pattern_index == 0:
                    pass
                    # State 2618
                    if len(subjects) == 0:
                        pass
                        # 0: v*b
                if pattern_index == 1:
                    pass
                    # State 2678
                    if len(subjects) == 0:
                        pass
                        # 1: b*x**n
                if pattern_index == 2:
                    pass
                    # State 3265
                    if len(subjects) == 0:
                        pass
                        # 2: x*d
                if pattern_index == 3:
                    pass
                    # State 3320
                    if len(subjects) == 0:
                        pass
                        # 3: x*f
                if pattern_index == 4:
                    pass
                    # State 4065
                    if len(subjects) == 0:
                        pass
                        # 4: v**2*c
                if pattern_index == 5:
                    pass
                    # State 4078
                    if len(subjects) == 0:
                        pass
                        # 5: b*x
                if pattern_index == 6:
                    pass
                    # State 4694
                    if len(subjects) == 0:
                        pass
                        # 6: e*x
                if pattern_index == 7:
                    pass
                    # State 5255
                    if len(subjects) == 0:
                        pass
                        # 7: v**2*c
                if pattern_index == 8:
                    pass
                    # State 5296
                    if len(subjects) == 0:
                        pass
                        # 8: f*x**2
                if pattern_index == 9:
                    pass
                    # State 5298
                    if len(subjects) == 0:
                        pass
                        # 9: e*x
                if pattern_index == 10:
                    pass
                    # State 5386
                    if len(subjects) == 0:
                        pass
                        # 10: c*x**2
                if pattern_index == 11:
                    pass
                    # State 6555
                    if len(subjects) == 0:
                        pass
                        # 11: x**n*b1
                if pattern_index == 12:
                    pass
                    # State 6915
                    if len(subjects) == 0:
                        pass
                        # 12: b2*x**j
                if pattern_index == 13:
                    pass
                    # State 7176
                    if len(subjects) == 0:
                        pass
                        # 13: x**n*b
                if pattern_index == 14:
                    pass
                    # State 7224
                    if len(subjects) == 0:
                        pass
                        # 14: x**non2*b1
                if pattern_index == 15:
                    pass
                    # State 7241
                    if len(subjects) == 0:
                        pass
                        # 15: x**non2*b2
                if pattern_index == 16:
                    pass
                    # State 7470
                    if len(subjects) == 0:
                        pass
                        # 16: x**mn*d
                if pattern_index == 17:
                    pass
                    # State 7556
                    if len(subjects) == 0:
                        pass
                        # 17: b2*x**n
                if pattern_index == 18:
                    pass
                    # State 7579
                    if len(subjects) == 0:
                        pass
                        # 18: e*x**r
                if pattern_index == 19:
                    pass
                    # State 7773
                    if len(subjects) == 0:
                        pass
                        # 19: d*v**n
                if pattern_index == 20:
                    pass
                    # State 8351
                    if len(subjects) == 0:
                        pass
                        # 20: x**n2*c
                if pattern_index == 21:
                    pass
                    # State 8454
                    if len(subjects) == 0:
                        pass
                        # 21: x**n*b
                if pattern_index == 22:
                    pass
                    # State 8657
                    if len(subjects) == 0:
                        pass
                        # 22: f*x**j
                if pattern_index == 23:
                    pass
                    # State 8675
                    if len(subjects) == 0:
                        pass
                        # 23: c*x**n2
                if pattern_index == 24:
                    pass
                    # State 8684
                    if len(subjects) == 0:
                        pass
                        # 24: c*x**n2
                if pattern_index == 25:
                    pass
                    # State 9011
                    if len(subjects) == 0:
                        pass
                        # 25: c*x**r
                if pattern_index == 26:
                    pass
                    # State 9049
                    if len(subjects) == 0:
                        pass
                        # 26: c*x**n
                if pattern_index == 27:
                    pass
                    # State 9113
                    if len(subjects) == 0:
                        pass
                        # 27: c*x**n2
                if pattern_index == 28:
                    pass
                    # State 9347
                    if len(subjects) == 0:
                        pass
                        # 28: x**n2*c
                if pattern_index == 29:
                    pass
                    # State 9522
                    if len(subjects) == 0:
                        pass
                        # 29: x**n*b2
                if pattern_index == 30:
                    pass
                    # State 9527
                    if len(subjects) == 0:
                        pass
                        # 30: x**n2*f1
                if pattern_index == 31:
                    pass
                    # State 10798
                    if len(subjects) == 0:
                        pass
                        # 31: b*(c/x)**n
                if pattern_index == 32:
                    pass
                    # State 11126
                    if len(subjects) == 0:
                        pass
                        # 32: c*(c/x)**n2
                if pattern_index == 33:
                    pass
                    # State 12203
                    if len(subjects) == 0:
                        pass
                        # 33: d*x**n2
                if pattern_index == 34:
                    pass
                    # State 13096
                    if len(subjects) == 0:
                        pass
                        # 34: x*h
                if pattern_index == 35:
                    pass
                    # State 13883
                    if len(subjects) == 0:
                        pass
                        # 35: h*x
                if pattern_index == 36:
                    pass
                    # State 13923
                    if len(subjects) == 0:
                        pass
                        # 36: i*x**2
                if pattern_index == 37:
                    pass
                    # State 13957
                    if len(subjects) == 0:
                        pass
                        # 37: h*x
                if pattern_index == 38:
                    pass
                    # State 14001
                    if len(subjects) == 0:
                        pass
                        # 38: f*sqrt(x**2*c + a)
                if pattern_index == 39:
                    pass
                    # State 14652
                    if len(subjects) == 0:
                        pass
                        # 39: d*x
                if pattern_index == 40:
                    pass
                    # State 15088
                    if len(subjects) == 0:
                        pass
                        # 40: d*x
                if pattern_index == 41:
                    pass
                    # State 15560
                    if len(subjects) == 0:
                        pass
                        # 41: d*x
                if pattern_index == 42:
                    pass
                    # State 15920
                    if len(subjects) == 0:
                        pass
                        # 42: b*(F**(g*(e + x*f)))**n
                if pattern_index == 43:
                    pass
                    # State 16473
                    if len(subjects) == 0:
                        pass
                        # 43: b*(F**(g*(e + f*x)))**n
                if pattern_index == 44:
                    pass
                    # State 23653
                    if len(subjects) == 0:
                        pass
                        # 44: h*x
                if pattern_index == 45:
                    pass
                    # State 26295
                    if len(subjects) == 0:
                        pass
                        # 45: j*x
                if pattern_index == 46:
                    pass
                    # State 26314
                    if len(subjects) == 0:
                        pass
                        # 46: j*x
                if pattern_index == 47:
                    pass
                    # State 38279
                    if len(subjects) == 0:
                        pass
                        # 47: b*log(c*(d*(x**j*f + e)**p)**q)
                if pattern_index == 48:
                    pass
                    # State 58873
                    if len(subjects) == 0:
                        pass
                        # 48: b*sin(e + x*f)
                if pattern_index == 49:
                    pass
                    # State 58916
                    if len(subjects) == 0:
                        pass
                        # 49: b*cos(e + x*f)
                if pattern_index == 50:
                    pass
                    # State 59045
                    if len(subjects) == 0:
                        pass
                        # 50: b*sin(e + x*f)
                if pattern_index == 51:
                    pass
                    # State 59106
                    if len(subjects) == 0:
                        pass
                        # 51: b*cos(e + x*f)
                if pattern_index == 52:
                    pass
                    # State 60188
                    if len(subjects) == 0:
                        pass
                        # 52: d*sin(c + x*d)
                if pattern_index == 53:
                    pass
                    # State 60246
                    if len(subjects) == 0:
                        pass
                        # 53: d*cos(c + x*d)
                if pattern_index == 54:
                    pass
                    # State 61516
                    if len(subjects) == 0:
                        pass
                        # 54: b*sin(e + x*f)
                if pattern_index == 55:
                    pass
                    # State 61745
                    if len(subjects) == 0:
                        pass
                        # 55: b*cos(e + x*f)
                if pattern_index == 56:
                    pass
                    # State 61943
                    if len(subjects) == 0:
                        pass
                        # 56: b*sin(e + x*f)
                if pattern_index == 57:
                    pass
                    # State 62106
                    if len(subjects) == 0:
                        pass
                        # 57: b*cos(e + x*f)
                if pattern_index == 58:
                    pass
                    # State 63826
                    if len(subjects) == 0:
                        pass
                        # 58: b/sin(e + x*f)
                if pattern_index == 59:
                    pass
                    # State 64105
                    if len(subjects) == 0:
                        pass
                        # 59: b/cos(e + x*f)
                if pattern_index == 60:
                    pass
                    # State 64451
                    if len(subjects) == 0:
                        pass
                        # 60: d/sin(e + x*f)
                if pattern_index == 61:
                    pass
                    # State 64536
                    if len(subjects) == 0:
                        pass
                        # 61: d/cos(e + x*f)
                if pattern_index == 62:
                    pass
                    # State 72132
                    if len(subjects) == 0:
                        pass
                        # 62: d*x
                if pattern_index == 63:
                    pass
                    # State 72174
                    if len(subjects) == 0:
                        pass
                        # 63: b*sin(x*f + e)
                if pattern_index == 64:
                    pass
                    # State 72206
                    if len(subjects) == 0:
                        pass
                        # 64: d*x
                if pattern_index == 65:
                    pass
                    # State 74169
                    if len(subjects) == 0:
                        pass
                        # 65: b*sin(x**n*d + c)
                if pattern_index == 66:
                    pass
                    # State 74398
                    if len(subjects) == 0:
                        pass
                        # 66: b*cos(x**n*d + c)
                if pattern_index == 67:
                    pass
                    # State 74766
                    if len(subjects) == 0:
                        pass
                        # 67: b*sin(x**n*d + c)
                if pattern_index == 68:
                    pass
                    # State 74929
                    if len(subjects) == 0:
                        pass
                        # 68: b*cos(x**n*d + c)
                if pattern_index == 69:
                    pass
                    # State 75190
                    if len(subjects) == 0:
                        pass
                        # 69: b*sin(c + d*x**n)
                if pattern_index == 70:
                    pass
                    # State 75316
                    if len(subjects) == 0:
                        pass
                        # 70: b*cos(c + d*x**n)
                if pattern_index == 71:
                    pass
                    # State 75378
                    if len(subjects) == 0:
                        pass
                        # 71: b*sin(v)
                if pattern_index == 72:
                    pass
                    # State 75404
                    if len(subjects) == 0:
                        pass
                        # 72: b*cos(v)
                if pattern_index == 73:
                    pass
                    # State 78033
                    if len(subjects) == 0:
                        pass
                        # 73: b*tan(e + x*f)
                if pattern_index == 74:
                    pass
                    # State 78088
                    if len(subjects) == 0:
                        pass
                        # 74: b/tan(e + x*f)
                if pattern_index == 75:
                    pass
                    # State 78291
                    if len(subjects) == 0:
                        pass
                        # 75: b*tan(e + x*f)
                if pattern_index == 76:
                    pass
                    # State 78336
                    if len(subjects) == 0:
                        pass
                        # 76: b/tan(e + x*f)
                if pattern_index == 77:
                    pass
                    # State 78686
                    if len(subjects) == 0:
                        pass
                        # 77: d*tan(c + x*d)
                if pattern_index == 78:
                    pass
                    # State 78751
                    if len(subjects) == 0:
                        pass
                        # 78: d/tan(e + x*f)
                if pattern_index == 79:
                    pass
                    # State 80093
                    if len(subjects) == 0:
                        pass
                        # 79: b*tan(e + x*f)
                if pattern_index == 80:
                    pass
                    # State 80365
                    if len(subjects) == 0:
                        pass
                        # 80: b/tan(e + x*f)
                if pattern_index == 81:
                    pass
                    # State 80813
                    if len(subjects) == 0:
                        pass
                        # 81: b/tan(e + x*f)
                if pattern_index == 82:
                    pass
                    # State 81032
                    if len(subjects) == 0:
                        pass
                        # 82: b*tan(e + x*f)
                if pattern_index == 83:
                    pass
                    # State 86708
                    if len(subjects) == 0:
                        pass
                        # 83: d*x
                if pattern_index == 84:
                    pass
                    # State 86758
                    if len(subjects) == 0:
                        pass
                        # 84: b*tan(x*f + e)
                if pattern_index == 85:
                    pass
                    # State 86798
                    if len(subjects) == 0:
                        pass
                        # 85: d*x
                if pattern_index == 86:
                    pass
                    # State 88567
                    if len(subjects) == 0:
                        pass
                        # 86: b*tan(x**n*d + c)
                if pattern_index == 87:
                    pass
                    # State 88825
                    if len(subjects) == 0:
                        pass
                        # 87: b/tan(x**n*d + c)
                if pattern_index == 88:
                    pass
                    # State 88976
                    if len(subjects) == 0:
                        pass
                        # 88: b*tan(v)
                if pattern_index == 89:
                    pass
                    # State 89010
                    if len(subjects) == 0:
                        pass
                        # 89: b/tan(v)
                if pattern_index == 90:
                    pass
                    # State 91162
                    if len(subjects) == 0:
                        pass
                        # 90: b/sin(c + x*d)
                if pattern_index == 91:
                    pass
                    # State 91278
                    if len(subjects) == 0:
                        pass
                        # 91: d/cos(e + x*f)
                if pattern_index == 92:
                    pass
                    # State 91328
                    if len(subjects) == 0:
                        pass
                        # 92: d/sin(e + x*f)
                if pattern_index == 93:
                    pass
                    # State 91884
                    if len(subjects) == 0:
                        pass
                        # 93: b/cos(e + x*f)
                if pattern_index == 94:
                    pass
                    # State 92065
                    if len(subjects) == 0:
                        pass
                        # 94: b/sin(e + x*f)
                if pattern_index == 95:
                    pass
                    # State 98994
                    if len(subjects) == 0:
                        pass
                        # 95: b/cos(x**n*d + c)
                if pattern_index == 96:
                    pass
                    # State 99271
                    if len(subjects) == 0:
                        pass
                        # 96: b/sin(x**n*d + c)
                if pattern_index == 97:
                    pass
                    # State 99425
                    if len(subjects) == 0:
                        pass
                        # 97: b/cos(v)
                if pattern_index == 98:
                    pass
                    # State 99463
                    if len(subjects) == 0:
                        pass
                        # 98: b/sin(v)
                if pattern_index == 99:
                    pass
                    # State 107263
                    if len(subjects) == 0:
                        pass
                        # 99: b*sin(x*f + e)*cos(x*d + c)
                if pattern_index == 100:
                    pass
                    # State 108393
                    if len(subjects) == 0:
                        pass
                        # 100: b*asin(x*c)
                if pattern_index == 101:
                    pass
                    # State 108468
                    if len(subjects) == 0:
                        pass
                        # 101: b*acos(x*c)
                if pattern_index == 102:
                    pass
                    # State 108846
                    if len(subjects) == 0:
                        pass
                        # 102: b*asin(x*c)
                if pattern_index == 103:
                    pass
                    # State 108888
                    if len(subjects) == 0:
                        pass
                        # 103: b*acos(x*c)
                if pattern_index == 104:
                    pass
                    # State 109244
                    if len(subjects) == 0:
                        pass
                        # 104: b*asin(x*c)
                if pattern_index == 105:
                    pass
                    # State 109278
                    if len(subjects) == 0:
                        pass
                        # 105: b*acos(x*c)
                if pattern_index == 106:
                    pass
                    # State 109469
                    if len(subjects) == 0:
                        pass
                        # 106: e*x
                if pattern_index == 107:
                    pass
                    # State 109633
                    if len(subjects) == 0:
                        pass
                        # 107: h*x**2
                if pattern_index == 108:
                    pass
                    # State 109635
                    if len(subjects) == 0:
                        pass
                        # 108: g*x
                if pattern_index == 109:
                    pass
                    # State 109806
                    if len(subjects) == 0:
                        pass
                        # 109: g*x
                if pattern_index == 110:
                    pass
                    # State 109863
                    if len(subjects) == 0:
                        pass
                        # 110: b*asin(c*x)
                if pattern_index == 111:
                    pass
                    # State 109919
                    if len(subjects) == 0:
                        pass
                        # 111: b*acos(c*x)
                if pattern_index == 112:
                    pass
                    # State 110626
                    if len(subjects) == 0:
                        pass
                        # 112: C*x**2
                if pattern_index == 113:
                    pass
                    # State 110628
                    if len(subjects) == 0:
                        pass
                        # 113: B*x
                if pattern_index == 114:
                    pass
                    # State 113501
                    if len(subjects) == 0:
                        pass
                        # 114: b*atan(x*c)
                if pattern_index == 115:
                    pass
                    # State 113550
                    if len(subjects) == 0:
                        pass
                        # 115: b*acot(x*c)
                if pattern_index == 116:
                    pass
                    # State 119972
                    if len(subjects) == 0:
                        pass
                        # 116: b*asec(x*c)
                if pattern_index == 117:
                    pass
                    # State 120050
                    if len(subjects) == 0:
                        pass
                        # 117: b*acsc(x*c)
                if pattern_index == 118:
                    pass
                    # State 121861
                    if len(subjects) == 0:
                        pass
                        # 118: b*sinh(x*b + a)
                if pattern_index == 119:
                    pass
                    # State 124092
                    if len(subjects) == 0:
                        pass
                        # 119: b*sinh(x**n*d + c)
                if pattern_index == 120:
                    pass
                    # State 124339
                    if len(subjects) == 0:
                        pass
                        # 120: b*cosh(x**n*d + c)
                if pattern_index == 121:
                    pass
                    # State 124676
                    if len(subjects) == 0:
                        pass
                        # 121: b*sinh(x**n*d + c)
                if pattern_index == 122:
                    pass
                    # State 124839
                    if len(subjects) == 0:
                        pass
                        # 122: b*cosh(x**n*d + c)
                if pattern_index == 123:
                    pass
                    # State 125100
                    if len(subjects) == 0:
                        pass
                        # 123: b*sinh(c + d*x**n)
                if pattern_index == 124:
                    pass
                    # State 125226
                    if len(subjects) == 0:
                        pass
                        # 124: b*cosh(c + d*x**n)
                if pattern_index == 125:
                    pass
                    # State 125288
                    if len(subjects) == 0:
                        pass
                        # 125: b*sinh(v)
                if pattern_index == 126:
                    pass
                    # State 125314
                    if len(subjects) == 0:
                        pass
                        # 126: b*cosh(v)
                if pattern_index == 127:
                    pass
                    # State 125990
                    if len(subjects) == 0:
                        pass
                        # 127: d*tanh(x*b + a)
                if pattern_index == 128:
                    pass
                    # State 128105
                    if len(subjects) == 0:
                        pass
                        # 128: b*tanh(x**n*d + c)
                if pattern_index == 129:
                    pass
                    # State 128376
                    if len(subjects) == 0:
                        pass
                        # 129: b/tanh(x**n*d + c)
                if pattern_index == 130:
                    pass
                    # State 128527
                    if len(subjects) == 0:
                        pass
                        # 130: b*tanh(v)
                if pattern_index == 131:
                    pass
                    # State 128561
                    if len(subjects) == 0:
                        pass
                        # 131: b/tanh(v)
                if pattern_index == 132:
                    pass
                    # State 131320
                    if len(subjects) == 0:
                        pass
                        # 132: b/cosh(x**n*d + c)
                if pattern_index == 133:
                    pass
                    # State 131615
                    if len(subjects) == 0:
                        pass
                        # 133: b/sinh(x**n*d + c)
                if pattern_index == 134:
                    pass
                    # State 131774
                    if len(subjects) == 0:
                        pass
                        # 134: b/cosh(u)
                if pattern_index == 135:
                    pass
                    # State 131821
                    if len(subjects) == 0:
                        pass
                        # 135: b/sinh(u)
                if pattern_index == 136:
                    pass
                    # State 136868
                    if len(subjects) == 0:
                        pass
                        # 136: b*sinh(x*b + a)*cosh(x*b + a)
                if pattern_index == 137:
                    pass
                    # State 138129
                    if len(subjects) == 0:
                        pass
                        # 137: b*asinh(x*c)
                if pattern_index == 138:
                    pass
                    # State 138204
                    if len(subjects) == 0:
                        pass
                        # 138: b*acosh(x*c)
                if pattern_index == 139:
                    pass
                    # State 138506
                    if len(subjects) == 0:
                        pass
                        # 139: b*acosh(x*c)
                if pattern_index == 140:
                    pass
                    # State 138589
                    if len(subjects) == 0:
                        pass
                        # 140: b*asinh(x*c)
                if pattern_index == 141:
                    pass
                    # State 139033
                    if len(subjects) == 0:
                        pass
                        # 141: b*asinh(x*c)
                if pattern_index == 142:
                    pass
                    # State 139626
                    if len(subjects) == 0:
                        pass
                        # 142: b*asinh(c*x)
                if pattern_index == 143:
                    pass
                    # State 139672
                    if len(subjects) == 0:
                        pass
                        # 143: g*(x*e2 + d2)**p*(x*e1 + d1)**p
                if pattern_index == 144:
                    pass
                    # State 143126
                    if len(subjects) == 0:
                        pass
                        # 144: b*atanh(x*c)
                if pattern_index == 145:
                    pass
                    # State 143175
                    if len(subjects) == 0:
                        pass
                        # 145: b*acoth(x*c)
                if pattern_index == 146:
                    pass
                    # State 149148
                    if len(subjects) == 0:
                        pass
                        # 146: b*asech(x*c)
                if pattern_index == 147:
                    pass
                    # State 149226
                    if len(subjects) == 0:
                        pass
                        # 147: b*acsch(x*c)
                if pattern_index == 148:
                    pass
                    # State 151660
                    if len(subjects) == 0:
                        pass
                        # 148: y*b
            subjects.appendleft(tmp1189)
        return
        yield


from matchpy.utils import VariableWithCount
from matchpy.matching.many_to_one import CommutativeMatcher
from multiset import Multiset
from collections import deque
