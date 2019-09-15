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


class CommutativeMatcher2915(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({0: 1}), [
      (VariableWithCount('i3.0', 1, 1, None), Add)
]),
    1: (1, Multiset({1: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    2: (2, Multiset({2: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    3: (3, Multiset({3: 1, 4: 1}), [
      (VariableWithCount('i3.0', 1, 1, None), Add)
]),
    4: (4, Multiset({5: 1, 6: 1}), [
      (VariableWithCount('i3.0', 1, 1, None), Add)
]),
    5: (5, Multiset({7: 1, 8: 1}), [
      (VariableWithCount('i3.0', 1, 1, None), Add)
]),
    6: (6, Multiset({9: 1, 10: 1}), [
      (VariableWithCount('i3.0', 1, 1, None), Add)
]),
    7: (7, Multiset({11: 1, 12: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    8: (8, Multiset({13: 1, 14: 1}), [
      (VariableWithCount('i3.0', 1, 1, None), Add)
]),
    9: (9, Multiset({15: 1, 16: 1}), [
      (VariableWithCount('i3.0', 1, 1, None), Add)
]),
    10: (10, Multiset({11: 1, 12: 1}), [
      (VariableWithCount('i3.0', 1, 1, None), Add)
]),
    11: (11, Multiset({17: 1, 18: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    12: (12, Multiset({19: 1, 20: 1}), [
      
]),
    13: (13, Multiset({21: 1, 22: 1}), [
      
]),
    14: (14, Multiset({23: 1, 24: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    15: (15, Multiset({25: 1, 26: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    16: (16, Multiset({27: 1, 28: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    17: (17, Multiset({29: 1}), [
      (VariableWithCount('i3.0', 1, 1, None), Add)
]),
    18: (18, Multiset({30: 1}), [
      (VariableWithCount('i3.0', 1, 1, None), Add)
]),
    19: (19, Multiset({31: 1}), [
      (VariableWithCount('i3.0', 1, 1, None), Add)
]),
    20: (20, Multiset({32: 1}), [
      (VariableWithCount('i3.0', 1, 1, None), Add)
]),
    21: (21, Multiset({33: 1}), [
      (VariableWithCount('i3.0', 1, 1, None), Add)
]),
    22: (22, Multiset({34: 1}), [
      (VariableWithCount('i3.0', 1, 1, None), Add)
]),
    23: (23, Multiset({35: 1}), [
      (VariableWithCount('i3.0', 1, 1, None), Add)
]),
    24: (24, Multiset({36: 1}), [
      (VariableWithCount('i3.0', 1, 1, None), Add)
]),
    25: (25, Multiset({37: 1}), [
      (VariableWithCount('i3.0', 1, 1, None), Add)
]),
    26: (26, Multiset({38: 1}), [
      (VariableWithCount('i3.0', 1, 1, None), Add)
]),
    27: (27, Multiset({39: 1}), [
      (VariableWithCount('i3.0', 1, 1, None), Add)
]),
    28: (28, Multiset({40: 1}), [
      (VariableWithCount('i3.0', 1, 1, None), Add)
]),
    29: (29, Multiset({41: 1}), [
      (VariableWithCount('i3.0', 1, 1, None), Add)
]),
    30: (30, Multiset({42: 1}), [
      (VariableWithCount('i3.0', 1, 1, None), Add)
]),
    31: (31, Multiset({43: 1}), [
      (VariableWithCount('i3.0', 1, 1, None), Add)
]),
    32: (32, Multiset({44: 1}), [
      (VariableWithCount('i3.0', 1, 1, None), Add)
]),
    33: (33, Multiset({45: 1}), [
      (VariableWithCount('i3.0', 1, 1, None), Add)
]),
    34: (34, Multiset({46: 1}), [
      (VariableWithCount('i3.0', 1, 1, None), Add)
]),
    35: (35, Multiset({47: 1}), [
      (VariableWithCount('i3.0', 1, 1, None), Add)
]),
    36: (36, Multiset({48: 1}), [
      (VariableWithCount('i3.0', 1, 1, None), Add)
]),
    37: (37, Multiset({49: 1}), [
      (VariableWithCount('i3.0', 1, 1, None), Add)
]),
    38: (38, Multiset({50: 1}), [
      (VariableWithCount('i3.0', 1, 1, None), Add)
]),
    39: (39, Multiset({51: 1}), [
      (VariableWithCount('i3.0', 1, 1, None), Add)
]),
    40: (40, Multiset({52: 1}), [
      (VariableWithCount('i3.0', 1, 1, None), Add)
]),
    41: (41, Multiset({53: 1}), [
      (VariableWithCount('i3.0', 1, 1, None), Add)
]),
    42: (42, Multiset({54: 1}), [
      (VariableWithCount('i3.0', 1, 1, None), Add)
]),
    43: (43, Multiset({55: 1}), [
      (VariableWithCount('i3.0', 1, 1, None), Add)
]),
    44: (44, Multiset({56: 1}), [
      (VariableWithCount('i3.0', 1, 1, None), Add)
]),
    45: (45, Multiset({57: 1}), [
      (VariableWithCount('i3.0', 1, 1, None), Add)
]),
    46: (46, Multiset({58: 1}), [
      (VariableWithCount('i3.0', 1, 1, None), Add)
]),
    47: (47, Multiset({59: 1}), [
      (VariableWithCount('i3.0', 1, 1, None), Add)
]),
    48: (48, Multiset({60: 1}), [
      (VariableWithCount('i3.0', 1, 1, None), Add)
]),
    49: (49, Multiset({61: 1}), [
      (VariableWithCount('i3.0', 1, 1, None), Add)
]),
    50: (50, Multiset({62: 1}), [
      (VariableWithCount('i3.0', 1, 1, None), Add)
]),
    51: (51, Multiset({63: 1}), [
      (VariableWithCount('i3.0', 1, 1, None), Add)
]),
    52: (52, Multiset({64: 1}), [
      (VariableWithCount('i3.0', 1, 1, None), Add)
]),
    53: (53, Multiset({65: 1}), [
      (VariableWithCount('i3.0', 1, 1, None), Add)
]),
    54: (54, Multiset({66: 1}), [
      (VariableWithCount('i3.0', 1, 1, None), Add)
]),
    55: (55, Multiset({67: 1}), [
      (VariableWithCount('i3.0', 1, 1, None), Add)
]),
    56: (56, Multiset({68: 1}), [
      (VariableWithCount('i3.0', 1, 1, None), Add)
]),
    57: (57, Multiset({69: 1}), [
      (VariableWithCount('i3.0', 1, 1, None), Add)
]),
    58: (58, Multiset({70: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    59: (59, Multiset({71: 1, 72: 1}), [
      (VariableWithCount('i3.0', 1, 1, None), Add)
]),
    60: (60, Multiset({73: 1, 74: 1}), [
      (VariableWithCount('i3.0', 1, 1, None), Add)
]),
    61: (61, Multiset({75: 1, 76: 1}), [
      (VariableWithCount('i3.0', 1, 1, None), Add)
]),
    62: (62, Multiset({77: 1, 76: 1}), [
      (VariableWithCount('i3.0', 1, 1, None), Add)
]),
    63: (63, Multiset({78: 1, 79: 1}), [
      (VariableWithCount('i3.0', 1, 1, None), Add)
]),
    64: (64, Multiset({80: 1, 81: 1}), [
      (VariableWithCount('i3.0', 1, 1, None), Add)
]),
    65: (65, Multiset({82: 1, 83: 1}), [
      (VariableWithCount('i3.0', 1, 1, None), Add)
]),
    66: (66, Multiset({84: 1, 79: 1}), [
      (VariableWithCount('i3.0', 1, 1, None), Add)
]),
    67: (67, Multiset({85: 1, 79: 1}), [
      (VariableWithCount('i3.0', 1, 1, None), Add)
]),
    68: (68, Multiset({86: 1, 76: 1}), [
      (VariableWithCount('i3.0', 1, 1, None), Add)
]),
    69: (69, Multiset({87: 1, 74: 1}), [
      (VariableWithCount('i3.0', 1, 1, None), Add)
]),
    70: (70, Multiset({88: 1, 89: 1}), [
      (VariableWithCount('i3.0', 1, 1, None), Add)
]),
    71: (71, Multiset({90: 1, 89: 1}), [
      (VariableWithCount('i3.0', 1, 1, None), Add)
]),
    72: (72, Multiset({91: 1, 89: 1}), [
      (VariableWithCount('i3.0', 1, 1, None), Add)
]),
    73: (73, Multiset({92: 1, 93: 1}), [
      (VariableWithCount('i3.0', 1, 1, None), Add)
]),
    74: (74, Multiset({94: 1, 95: 1}), [
      (VariableWithCount('i3.0', 1, 1, None), Add)
]),
    75: (75, Multiset({96: 1, 97: 1}), [
      (VariableWithCount('i3.0', 1, 1, None), Add)
]),
    76: (76, Multiset({98: 1, 99: 1}), [
      (VariableWithCount('i3.0', 1, 1, None), Add)
]),
    77: (77, Multiset({100: 1, 101: 1}), [
      (VariableWithCount('i3.0', 1, 1, None), Add)
]),
    78: (78, Multiset({96: 1, 102: 1}), [
      (VariableWithCount('i3.0', 1, 1, None), Add)
]),
    79: (79, Multiset({103: 1, 104: 1}), [
      (VariableWithCount('i3.0', 1, 1, None), Add)
]),
    80: (80, Multiset({105: 1, 106: 1}), [
      (VariableWithCount('i3.0', 1, 1, None), Add)
]),
    81: (81, Multiset({107: 1, 108: 1}), [
      (VariableWithCount('i3.0', 1, 1, None), Add)
]),
    82: (82, Multiset({109: 1, 110: 1}), [
      (VariableWithCount('i3.0', 1, 1, None), Add)
]),
    83: (83, Multiset({111: 1, 112: 1}), [
      (VariableWithCount('i3.0', 1, 1, None), Add)
]),
    84: (84, Multiset({111: 1, 113: 1}), [
      (VariableWithCount('i3.0', 1, 1, None), Add)
]),
    85: (85, Multiset({114: 1, 115: 1}), [
      (VariableWithCount('i3.0', 1, 1, None), Add)
]),
    86: (86, Multiset({116: 1, 117: 1}), [
      (VariableWithCount('i3.0', 1, 1, None), Add)
]),
    87: (87, Multiset({118: 1, 119: 1}), [
      (VariableWithCount('i3.0', 1, 1, None), Add)
]),
    88: (88, Multiset({120: 1, 121: 1}), [
      (VariableWithCount('i3.0', 1, 1, None), Add)
]),
    89: (89, Multiset({122: 1, 123: 1, 124: 1}), [
      
]),
    90: (90, Multiset({125: 1, 126: 1, 127: 1}), [
      
]),
    91: (91, Multiset({128: 1, 129: 1, 130: 1}), [
      
]),
    92: (92, Multiset({131: 1, 132: 1, 130: 1}), [
      
]),
    93: (93, Multiset({133: 1, 134: 1, 135: 1}), [
      
]),
    94: (94, Multiset({136: 1, 137: 1, 135: 1}), [
      
]),
    95: (95, Multiset({138: 1, 139: 1, 140: 1}), [
      
]),
    96: (96, Multiset({141: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    97: (97, Multiset({142: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    98: (98, Multiset({143: 1, 144: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    99: (99, Multiset({145: 1, 146: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    100: (100, Multiset({147: 1, 148: 1}), [
      
]),
    101: (101, Multiset({149: 1, 150: 1}), [
      
]),
    102: (102, Multiset({151: 1, 152: 1}), [
      
]),
    103: (103, Multiset({153: 1, 154: 1}), [
      
]),
    104: (104, Multiset({155: 1, 156: 1}), [
      
]),
    105: (105, Multiset({157: 1, 158: 1}), [
      
]),
    106: (106, Multiset({155: 1, 154: 1}), [
      
]),
    107: (107, Multiset({159: 1, 160: 1}), [
      
]),
    108: (108, Multiset({161: 1, 162: 1}), [
      
]),
    109: (109, Multiset({163: 1, 164: 1}), [
      
]),
    110: (110, Multiset({165: 1, 166: 1}), [
      
]),
    111: (111, Multiset({167: 1, 168: 1}), [
      
]),
    112: (112, Multiset({169: 1, 170: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    113: (113, Multiset({171: 1, 172: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    114: (114, Multiset({173: 1, 174: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    115: (115, Multiset({175: 1, 176: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    116: (116, Multiset({177: 1, 178: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    117: (117, Multiset({179: 1, 180: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    118: (118, Multiset({181: 1, 182: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    119: (119, Multiset({183: 1, 184: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    120: (120, Multiset({185: 1, 186: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    121: (121, Multiset({187: 1, 188: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    122: (122, Multiset({189: 1, 190: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    123: (123, Multiset({191: 1, 192: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    124: (124, Multiset({193: 1, 194: 1, 195: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    125: (125, Multiset({196: 1, 194: 1, 197: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    126: (126, Multiset({198: 1, 199: 1, 200: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    127: (127, Multiset({201: 1, 199: 1, 202: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    128: (128, Multiset({203: 1, 204: 1, 205: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    129: (129, Multiset({206: 1, 207: 1, 208: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    130: (130, Multiset({209: 1, 207: 1, 210: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    131: (131, Multiset({211: 1, 212: 1, 213: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    132: (132, Multiset({214: 1, 215: 1, 216: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    133: (133, Multiset({217: 1, 212: 1, 218: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    134: (134, Multiset({219: 1, 220: 1, 221: 1, 222: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    135: (135, Multiset({223: 1, 224: 1, 225: 1, 226: 1}), [
      (VariableWithCount('i3.0', 1, 1, None), Add)
]),
    136: (136, Multiset({227: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    137: (137, Multiset({228: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    138: (138, Multiset({229: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    139: (139, Multiset({230: 1}), [
      (VariableWithCount('i3.0', 1, 1, None), Add)
]),
    140: (140, Multiset({231: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    141: (141, Multiset({232: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    142: (142, Multiset({233: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    143: (143, Multiset({234: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    144: (144, Multiset({235: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    145: (145, Multiset({236: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    146: (146, Multiset({237: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    147: (147, Multiset({238: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, None), Add)
]),
    148: (148, Multiset({239: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, None), Add)
]),
    149: (149, Multiset({240: 1}), [
      (VariableWithCount('i3.0', 1, 1, None), Add)
]),
    150: (150, Multiset({241: 1}), [
      (VariableWithCount('i3.0', 1, 1, None), Add)
]),
    151: (151, Multiset({242: 1}), [
      (VariableWithCount('i3.0', 1, 1, None), Add)
]),
    152: (152, Multiset({243: 1}), [
      (VariableWithCount('i3.0', 1, 1, None), Add)
]),
    153: (153, Multiset({244: 1}), [
      (VariableWithCount('i3.0', 1, 1, None), Add)
]),
    154: (154, Multiset({245: 1}), [
      (VariableWithCount('i3.0', 1, 1, None), Add)
]),
    155: (155, Multiset({246: 1}), [
      (VariableWithCount('i3.0', 1, 1, None), Add)
]),
    156: (156, Multiset({247: 1}), [
      (VariableWithCount('i3.0', 1, 1, None), Add)
]),
    157: (157, Multiset({248: 1}), [
      (VariableWithCount('i3.0', 1, 1, None), Add)
]),
    158: (158, Multiset({249: 1}), [
      (VariableWithCount('i3.0', 1, 1, None), Add)
]),
    159: (159, Multiset({250: 1}), [
      (VariableWithCount('i3.0', 1, 1, None), Add)
]),
    160: (160, Multiset({251: 1}), [
      (VariableWithCount('i3.0', 1, 1, None), Add)
]),
    161: (161, Multiset({252: 1}), [
      (VariableWithCount('i3.0', 1, 1, None), Add)
]),
    162: (162, Multiset({253: 1}), [
      (VariableWithCount('i3.0', 1, 1, None), Add)
]),
    163: (163, Multiset({254: 1}), [
      (VariableWithCount('i3.0', 1, 1, None), Add)
]),
    164: (164, Multiset({255: 1}), [
      (VariableWithCount('i3.0', 1, 1, None), Add)
]),
    165: (165, Multiset({256: 1}), [
      (VariableWithCount('i3.0', 1, 1, None), Add)
]),
    166: (166, Multiset({257: 1}), [
      (VariableWithCount('i3.0', 1, 1, None), Add)
]),
    167: (167, Multiset({258: 1}), [
      (VariableWithCount('i3.0', 1, 1, None), Add)
]),
    168: (168, Multiset({259: 1}), [
      (VariableWithCount('i3.0', 1, 1, None), Add)
]),
    169: (169, Multiset({260: 1, 261: 1}), [
      
]),
    170: (170, Multiset({262: 1, 263: 1}), [
      
]),
    171: (171, Multiset({264: 1, 265: 1}), [
      
]),
    172: (172, Multiset({266: 1, 267: 1}), [
      
]),
    173: (173, Multiset({268: 1, 269: 1}), [
      (VariableWithCount('i3.0', 1, 1, None), Add)
]),
    174: (174, Multiset({270: 1, 271: 1}), [
      (VariableWithCount('i3.0', 1, 1, None), Add)
]),
    175: (175, Multiset({272: 1, 273: 1}), [
      (VariableWithCount('i3.0', 1, 1, None), Add)
]),
    176: (176, Multiset({274: 1, 275: 1}), [
      (VariableWithCount('i3.0', 1, 1, None), Add)
]),
    177: (177, Multiset({276: 1, 277: 1}), [
      (VariableWithCount('i3.0', 1, 1, None), Add)
]),
    178: (178, Multiset({278: 1, 279: 1}), [
      (VariableWithCount('i3.0', 1, 1, None), Add)
]),
    179: (179, Multiset({280: 1, 281: 1}), [
      (VariableWithCount('i3.0', 1, 1, None), Add)
]),
    180: (180, Multiset({282: 1, 283: 1}), [
      (VariableWithCount('i3.0', 1, 1, None), Add)
]),
    181: (181, Multiset({284: 1, 285: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    182: (182, Multiset({286: 1, 287: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    183: (183, Multiset({288: 1}), [
      (VariableWithCount('i3.0', 1, 1, None), Add)
]),
    184: (184, Multiset({289: 1}), [
      (VariableWithCount('i3.0', 1, 1, None), Add)
]),
    185: (185, Multiset({290: 1}), [
      (VariableWithCount('i3.0', 1, 1, None), Add)
]),
    186: (186, Multiset({291: 1}), [
      (VariableWithCount('i3.0', 1, 1, None), Add)
]),
    187: (187, Multiset({292: 1}), [
      (VariableWithCount('i3.0', 1, 1, None), Add)
]),
    188: (188, Multiset({293: 1}), [
      (VariableWithCount('i3.0', 1, 1, None), Add)
]),
    189: (189, Multiset({294: 1}), [
      (VariableWithCount('i3.0', 1, 1, None), Add)
]),
    190: (190, Multiset({295: 1}), [
      (VariableWithCount('i3.0', 1, 1, None), Add)
]),
    191: (191, Multiset({296: 1}), [
      (VariableWithCount('i3.0', 1, 1, None), Add)
]),
    192: (192, Multiset({297: 1}), [
      (VariableWithCount('i3.0', 1, 1, None), Add)
]),
    193: (193, Multiset({298: 1}), [
      (VariableWithCount('i3.0', 1, 1, None), Add)
]),
    194: (194, Multiset({299: 1}), [
      (VariableWithCount('i3.0', 1, 1, None), Add)
]),
    195: (195, Multiset({300: 1, 301: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    196: (196, Multiset({302: 1, 303: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    197: (197, Multiset({304: 1, 305: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    198: (198, Multiset({306: 1, 307: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    199: (199, Multiset({308: 1, 309: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    200: (200, Multiset({310: 1, 311: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    201: (201, Multiset({312: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    202: (202, Multiset({313: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    203: (203, Multiset({314: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    204: (204, Multiset({315: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    205: (205, Multiset({316: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    206: (206, Multiset({317: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    207: (207, Multiset({318: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    208: (208, Multiset({319: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    209: (209, Multiset({320: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    210: (210, Multiset({321: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    211: (211, Multiset({322: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    212: (212, Multiset({323: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    213: (213, Multiset({324: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    214: (214, Multiset({325: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    215: (215, Multiset({326: 1}), [
      (VariableWithCount('i3.0', 1, 1, None), Add)
]),
    216: (216, Multiset({327: 1}), [
      (VariableWithCount('i3.0', 1, 1, None), Add)
]),
    217: (217, Multiset({328: 1}), [
      (VariableWithCount('i3.0', 1, 1, None), Add)
]),
    218: (218, Multiset({329: 1}), [
      (VariableWithCount('i3.0', 1, 1, None), Add)
]),
    219: (219, Multiset({330: 1}), [
      (VariableWithCount('i3.0', 1, 1, None), Add)
]),
    220: (220, Multiset({331: 1}), [
      (VariableWithCount('i3.0', 1, 1, None), Add)
]),
    221: (221, Multiset({332: 1}), [
      (VariableWithCount('i3.0', 1, 1, None), Add)
]),
    222: (222, Multiset({333: 1}), [
      (VariableWithCount('i3.0', 1, 1, None), Add)
]),
    223: (223, Multiset({334: 1}), [
      (VariableWithCount('i3.0', 1, 1, None), Add)
]),
    224: (224, Multiset({335: 1}), [
      (VariableWithCount('i3.0', 1, 1, None), Add)
]),
    225: (225, Multiset({336: 1}), [
      (VariableWithCount('i3.0', 1, 1, None), Add)
]),
    226: (226, Multiset({337: 1}), [
      (VariableWithCount('i3.0', 1, 1, None), Add)
]),
    227: (227, Multiset({338: 1}), [
      (VariableWithCount('i3.0', 1, 1, None), Add)
]),
    228: (228, Multiset({339: 1}), [
      (VariableWithCount('i3.0', 1, 1, None), Add)
]),
    229: (229, Multiset({340: 1}), [
      (VariableWithCount('i3.0', 1, 1, None), Add)
]),
    230: (230, Multiset({341: 1}), [
      (VariableWithCount('i3.0', 1, 1, None), Add)
]),
    231: (231, Multiset({342: 1, 343: 1}), [
      (VariableWithCount('i3.0', 1, 1, None), Add)
]),
    232: (232, Multiset({344: 1, 345: 1}), [
      (VariableWithCount('i3.0', 1, 1, None), Add)
]),
    233: (233, Multiset({346: 1, 347: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    234: (234, Multiset({348: 1, 349: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    235: (235, Multiset({350: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    236: (236, Multiset({351: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    237: (237, Multiset({352: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    238: (238, Multiset({353: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    239: (239, Multiset({354: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    240: (240, Multiset({355: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    241: (241, Multiset({356: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    242: (242, Multiset({357: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    243: (243, Multiset({358: 1}), [
      (VariableWithCount('i3.0', 1, 1, None), Add)
]),
    244: (244, Multiset({359: 1}), [
      (VariableWithCount('i3.0', 1, 1, None), Add)
]),
    245: (245, Multiset({360: 1}), [
      (VariableWithCount('i3.0', 1, 1, None), Add)
]),
    246: (246, Multiset({361: 1}), [
      (VariableWithCount('i3.0', 1, 1, None), Add)
]),
    247: (247, Multiset({362: 1}), [
      (VariableWithCount('i3.0', 1, 1, None), Add)
]),
    248: (248, Multiset({363: 1}), [
      (VariableWithCount('i3.0', 1, 1, None), Add)
]),
    249: (249, Multiset({364: 1}), [
      (VariableWithCount('i3.0', 1, 1, None), Add)
]),
    250: (250, Multiset({365: 1}), [
      (VariableWithCount('i3.0', 1, 1, None), Add)
]),
    251: (251, Multiset({366: 1}), [
      (VariableWithCount('i3.0', 1, 1, None), Add)
]),
    252: (252, Multiset({367: 1}), [
      (VariableWithCount('i3.0', 1, 1, None), Add)
]),
    253: (253, Multiset({368: 1}), [
      (VariableWithCount('i3.0', 1, 1, None), Add)
]),
    254: (254, Multiset({369: 1}), [
      (VariableWithCount('i3.0', 1, 1, None), Add)
]),
    255: (255, Multiset({370: 1}), [
      (VariableWithCount('i3.0', 1, 1, None), Add)
]),
    256: (256, Multiset({371: 1}), [
      (VariableWithCount('i3.0', 1, 1, None), Add)
]),
    257: (257, Multiset({372: 1}), [
      (VariableWithCount('i3.0', 1, 1, None), Add)
]),
    258: (258, Multiset({373: 1}), [
      (VariableWithCount('i3.0', 1, 1, None), Add)
]),
    259: (259, Multiset({374: 1, 375: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    260: (260, Multiset({376: 1, 377: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    261: (261, Multiset({378: 1, 379: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    262: (262, Multiset({380: 1, 381: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    263: (263, Multiset({382: 1, 383: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    264: (264, Multiset({384: 1, 385: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    265: (265, Multiset({386: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    266: (266, Multiset({387: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    267: (267, Multiset({388: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    268: (268, Multiset({389: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    269: (269, Multiset({390: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    270: (270, Multiset({391: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    271: (271, Multiset({392: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    272: (272, Multiset({393: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    273: (273, Multiset({394: 1}), [
      (VariableWithCount('i3.0', 1, 1, None), Add)
]),
    274: (274, Multiset({395: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    275: (275, Multiset({396: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    276: (276, Multiset({397: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    277: (277, Multiset({398: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    278: (278, Multiset({399: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    279: (279, Multiset({400: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    280: (280, Multiset({401: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    281: (281, Multiset({402: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    282: (282, Multiset({403: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    283: (283, Multiset({404: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    284: (284, Multiset({405: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    285: (285, Multiset({406: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    286: (286, Multiset({407: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    287: (287, Multiset({408: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    288: (288, Multiset({409: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    289: (289, Multiset({410: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    290: (290, Multiset({411: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    291: (291, Multiset({412: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    292: (292, Multiset({413: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    293: (293, Multiset({414: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    294: (294, Multiset({415: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    295: (295, Multiset({416: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    296: (296, Multiset({417: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    297: (297, Multiset({418: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    298: (298, Multiset({419: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    299: (299, Multiset({420: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    300: (300, Multiset({421: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    301: (301, Multiset({422: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    302: (302, Multiset({423: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    303: (303, Multiset({424: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    304: (304, Multiset({425: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    305: (305, Multiset({426: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    306: (306, Multiset({427: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    307: (307, Multiset({428: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    308: (308, Multiset({429: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    309: (309, Multiset({430: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    310: (310, Multiset({431: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    311: (311, Multiset({432: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    312: (312, Multiset({433: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    313: (313, Multiset({434: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    314: (314, Multiset({435: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    315: (315, Multiset({436: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    316: (316, Multiset({437: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    317: (317, Multiset({438: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    318: (318, Multiset({439: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    319: (319, Multiset({440: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    320: (320, Multiset({441: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    321: (321, Multiset({442: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    322: (322, Multiset({443: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    323: (323, Multiset({444: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    324: (324, Multiset({445: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    325: (325, Multiset({446: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    326: (326, Multiset({447: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    327: (327, Multiset({448: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    328: (328, Multiset({449: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    329: (329, Multiset({450: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    330: (330, Multiset({451: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    331: (331, Multiset({452: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    332: (332, Multiset({453: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    333: (333, Multiset({454: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    334: (334, Multiset({455: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    335: (335, Multiset({456: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    336: (336, Multiset({457: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    337: (337, Multiset({458: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    338: (338, Multiset({459: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    339: (339, Multiset({460: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    340: (340, Multiset({461: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    341: (341, Multiset({462: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    342: (342, Multiset({463: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    343: (343, Multiset({464: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    344: (344, Multiset({465: 1}), [
      (VariableWithCount('i3.0', 1, 1, None), Add)
]),
    345: (345, Multiset({466: 1}), [
      (VariableWithCount('i3.0', 1, 1, None), Add)
]),
    346: (346, Multiset({467: 1}), [
      (VariableWithCount('i3.0', 1, 1, None), Add)
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
        if CommutativeMatcher2915._instance is None:
            CommutativeMatcher2915._instance = CommutativeMatcher2915()
        return CommutativeMatcher2915._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 2914
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i3.1.0_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 2916
            if len(subjects) >= 1:
                tmp2 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i3.1.0', tmp2)
                except ValueError:
                    pass
                else:
                    pass
                    # State 2917
                    if len(subjects) == 0:
                        pass
                        # 0: x*b /; (cons_f2) and (cons_f3) and (cons_f69)
                        yield 0, subst2
                        # 1: x*b /; (cons_f2) and (cons_f3) and (cons_f19)
                        yield 1, subst2
                        # 2: x*b /; (cons_f3) and (cons_f70) and (cons_f71)
                        yield 2, subst2
                subjects.appendleft(tmp2)
            if len(subjects) >= 1:
                tmp4 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i3.1.1', tmp4)
                except ValueError:
                    pass
                else:
                    pass
                    # State 3899
                    if len(subjects) == 0:
                        pass
                        # 4: b*x /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f47)
                        yield 4, subst2
                        # 6: b*x /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f5) and (cons_f47)
                        yield 6, subst2
                        # 8: b*x /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f228) and (cons_f229)
                        yield 8, subst2
                        # 10: b*x /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f228) and (cons_f230)
                        yield 10, subst2
                        # 12: b*x /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f228)
                        yield 12, subst2
                        # 14: b*x /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f228) and (cons_f233) and (cons_f229)
                        yield 14, subst2
                        # 16: b*x /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f228) and (With200)
                        yield 16, subst2
                        # 18: b*x /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f5) and (cons_f234)
                        yield 18, subst2
                        # 20: b*x /; (cons_f3) and (cons_f8) and (cons_f235)
                        yield 20, subst2
                        # 22: b*x /; (cons_f3) and (cons_f8)
                        yield 22, subst2
                        # 24: b*x /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f228) and (With206)
                        yield 24, subst2
                        # 26: b*x /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f5) and (cons_f228)
                        yield 26, subst2
                        # 28: b*x /; (cons_f3) and (cons_f70) and (cons_f71)
                        yield 28, subst2
                        # 170: b*x /; (cons_f2) and (cons_f3) and (cons_f29) and (cons_f1001)
                        yield 170, subst2
                        # 172: b*x /; (cons_f2) and (cons_f3) and (cons_f29) and (cons_f1002)
                        yield 172, subst2
                        # 174: b*x /; (cons_f2) and (cons_f3) and (cons_f29) and (cons_f1002) and (With1747)
                        yield 174, subst2
                        # 176: b*x /; (cons_f2) and (cons_f3) and (cons_f29) and (cons_f5) and (cons_f1001)
                        yield 176, subst2
                        # 178: b*x /; (cons_f2) and (cons_f3) and (cons_f29) and (cons_f5) and (cons_f1002) and (With1750)
                        yield 178, subst2
                        # 180: b*x /; (cons_f2) and (cons_f3) and (cons_f29) and (cons_f5) and (cons_f1002)
                        yield 180, subst2
                subjects.appendleft(tmp4)
            subst2 = Substitution(subst1)
            try:
                subst2.try_add_variable('i3.1.2_1', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 8170
                if len(subjects) >= 1:
                    tmp7 = subjects.popleft()
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i3.1.1', tmp7)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 8171
                        if len(subjects) == 0:
                            pass
                            # 129: c*x**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f52) and (cons_f754) and (cons_f755) and (cons_f228) and (cons_f756)
                            yield 129, subst3
                            # 132: c*x**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f52) and (cons_f754) and (cons_f755) and (cons_f228)
                            yield 132, subst3
                            # 134: c*x**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f52) and (cons_f754) and (cons_f755)
                            yield 134, subst3
                            # 137: c*x**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f52) and (cons_f754)
                            yield 137, subst3
                            # 139: c*x**n2 /; (cons_f2) and (cons_f52) and (cons_f754) and (cons_f70) and (cons_f71)
                            yield 139, subst3
                            # 148: c*x**n2 /; (cons_f2) and (cons_f3) and (cons_f798) and (cons_f4) and (cons_f5) and (cons_f954) and (cons_f955)
                            yield 148, subst3
                            # 150: c*x**n2 /; (cons_f2) and (cons_f3) and (cons_f798) and (cons_f4) and (cons_f954) and (cons_f956)
                            yield 150, subst3
                            # 152: c*x**n2 /; (cons_f2) and (cons_f3) and (cons_f798) and (cons_f4) and (cons_f5) and (cons_f954) and (cons_f956)
                            yield 152, subst3
                            # 154: c*x**n2 /; (cons_f2) and (cons_f3) and (cons_f958) and (cons_f959)
                            yield 154, subst3
                            # 156: c*x**n2 /; (cons_f2) and (cons_f3) and (cons_f958) and (cons_f959) and (cons_f961)
                            yield 156, subst3
                            # 158: c*x**n2 /; (cons_f2) and (cons_f3) and (cons_f958) and (cons_f959) and (cons_f962)
                            yield 158, subst3
                            # 160: c*x**n2 /; (cons_f2) and (cons_f3) and (cons_f798) and (cons_f4) and (cons_f954)
                            yield 160, subst3
                            # 164: c*x**n2 /; (cons_f2) and (cons_f3) and (cons_f966) and (cons_f967)
                            yield 164, subst3
                            # 166: c*x**n2 /; (cons_f2) and (cons_f3) and (cons_f798) and (cons_f4) and (cons_f5) and (cons_f954) and (cons_f968)
                            yield 166, subst3
                            # 168: c*x**n2 /; (cons_f3) and (cons_f4) and (cons_f70) and (cons_f71)
                            yield 168, subst3
                            # 72: c*x**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f48)
                            yield 72, subst3
                            # 74: c*x**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f5) and (cons_f48)
                            yield 74, subst3
                            # 76: c*x**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f48) and (cons_f47)
                            yield 76, subst3
                            # 79: c*x**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f48) and (cons_f47)
                            yield 79, subst3
                            # 83: c*x**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f5) and (cons_f48) and (cons_f47)
                            yield 83, subst3
                            # 89: c*x**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f48) and (cons_f228)
                            yield 89, subst3
                            # 115: c*x**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f682)
                            yield 115, subst3
                            # 117: c*x**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f587) and (cons_f683)
                            yield 117, subst3
                            # 119: c*x**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f587) and (cons_f683)
                            yield 119, subst3
                            # 121: c*x**n2 /; (cons_f8) and (cons_f48) and (cons_f70) and (cons_f71)
                            yield 121, subst3
                            # 123: c*x**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f752)
                            yield 123, subst3
                            # 126: c*x**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f52) and (cons_f754) and (cons_f755)
                            yield 126, subst3
                    subjects.appendleft(tmp7)
                subst3 = Substitution(subst2)
                try:
                    subst3.try_add_variable('i3.1.2.0', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 10935
                    if len(subjects) >= 1 and isinstance(subjects[0], Pow):
                        tmp10 = subjects.popleft()
                        subjects11 = deque(tmp10._args)
                        # State 10936
                        if len(subjects11) >= 1:
                            tmp12 = subjects11.popleft()
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i3.1.2.1', tmp12)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 10937
                                if len(subjects11) >= 1 and subjects11[0] == Integer(-1):
                                    tmp14 = subjects11.popleft()
                                    # State 10938
                                    if len(subjects11) == 0:
                                        pass
                                        # State 10939
                                        if len(subjects) == 0:
                                            pass
                                            # 144: c*(c/x)**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f5) and (cons_f48)
                                            yield 144, subst4
                                    subjects11.appendleft(tmp14)
                            subjects11.appendleft(tmp12)
                        subjects.appendleft(tmp10)
                if len(subjects) >= 1:
                    tmp15 = subjects.popleft()
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i3.1.2.1', tmp15)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 11176
                        if len(subjects) == 0:
                            pass
                            # 146: c*x**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f5) and (cons_f809)
                            yield 146, subst3
                    subjects.appendleft(tmp15)
                if len(subjects) >= 1 and isinstance(subjects[0], Mul):
                    tmp17 = subjects.popleft()
                    associative1 = tmp17
                    associative_type1 = type(tmp17)
                    subjects18 = deque(tmp17._args)
                    matcher = CommutativeMatcher10941.get()
                    tmp19 = subjects18
                    subjects18 = []
                    for s in tmp19:
                        matcher.add_subject(s)
                    for pattern_index, subst3 in matcher.match(tmp19, subst2):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 10946
                            if len(subjects) == 0:
                                pass
                                # 144: c*(c/x)**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f5) and (cons_f48)
                                yield 144, subst3
                    subjects.appendleft(tmp17)
            subst2 = Substitution(subst1)
            try:
                subst2.try_add_variable('i3.1.2', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 12099
                if len(subjects) >= 1:
                    tmp21 = subjects.popleft()
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i3.1.1', tmp21)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 12100
                        if len(subjects) == 0:
                            pass
                            # 162: b*x**n /; (cons_f2) and (cons_f3) and (cons_f4) and (cons_f965)
                            yield 162, subst3
                    subjects.appendleft(tmp21)
            subst2 = Substitution(subst1)
            try:
                subst2.try_add_variable('i3.1.3_1', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 68943
                if len(subjects) >= 1 and isinstance(subjects[0], sin):
                    tmp24 = subjects.popleft()
                    subjects25 = deque(tmp24._args)
                    # State 68944
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i3.1.3.0', S(0))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 68945
                        subst4 = Substitution(subst3)
                        try:
                            subst4.try_add_variable('i3.1.3.1.0_1', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 68946
                            if len(subjects25) >= 1:
                                tmp28 = subjects25.popleft()
                                subst5 = Substitution(subst4)
                                try:
                                    subst5.try_add_variable('i3.1.3.1.0', tmp28)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 68947
                                    if len(subjects25) == 0:
                                        pass
                                        # State 68948
                                        if len(subjects) == 0:
                                            pass
                                            # 305: c*sin(d + x*e)**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f5) and (cons_f48) and (cons_f47)
                                            yield 305, subst5
                                            # 301: c*sin(d + x*e)**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                                            yield 301, subst5
                                            # 309: c*sin(d + x*e)**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f228)
                                            yield 309, subst5
                                subjects25.appendleft(tmp28)
                        if len(subjects25) >= 1 and isinstance(subjects25[0], Mul):
                            tmp30 = subjects25.popleft()
                            associative1 = tmp30
                            associative_type1 = type(tmp30)
                            subjects31 = deque(tmp30._args)
                            matcher = CommutativeMatcher68950.get()
                            tmp32 = subjects31
                            subjects31 = []
                            for s in tmp32:
                                matcher.add_subject(s)
                            for pattern_index, subst4 in matcher.match(tmp32, subst3):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 68951
                                    if len(subjects25) == 0:
                                        pass
                                        # State 68952
                                        if len(subjects) == 0:
                                            pass
                                            # 305: c*sin(d + x*e)**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f5) and (cons_f48) and (cons_f47)
                                            yield 305, subst4
                                            # 301: c*sin(d + x*e)**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                                            yield 301, subst4
                                            # 309: c*sin(d + x*e)**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f228)
                                            yield 309, subst4
                            subjects25.appendleft(tmp30)
                    if len(subjects25) >= 1 and isinstance(subjects25[0], Add):
                        tmp33 = subjects25.popleft()
                        associative1 = tmp33
                        associative_type1 = type(tmp33)
                        subjects34 = deque(tmp33._args)
                        matcher = CommutativeMatcher68954.get()
                        tmp35 = subjects34
                        subjects34 = []
                        for s in tmp35:
                            matcher.add_subject(s)
                        for pattern_index, subst3 in matcher.match(tmp35, subst2):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 68960
                                if len(subjects25) == 0:
                                    pass
                                    # State 68961
                                    if len(subjects) == 0:
                                        pass
                                        # 305: c*sin(d + x*e)**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f5) and (cons_f48) and (cons_f47)
                                        yield 305, subst3
                                        # 301: c*sin(d + x*e)**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                                        yield 301, subst3
                                        # 309: c*sin(d + x*e)**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f228)
                                        yield 309, subst3
                        subjects25.appendleft(tmp33)
                    subjects.appendleft(tmp24)
                if len(subjects) >= 1 and isinstance(subjects[0], cos):
                    tmp36 = subjects.popleft()
                    subjects37 = deque(tmp36._args)
                    # State 69221
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i3.1.3.0', S(0))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 69222
                        subst4 = Substitution(subst3)
                        try:
                            subst4.try_add_variable('i3.1.3.1.0_1', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 69223
                            if len(subjects37) >= 1:
                                tmp40 = subjects37.popleft()
                                subst5 = Substitution(subst4)
                                try:
                                    subst5.try_add_variable('i3.1.3.1.0', tmp40)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 69224
                                    if len(subjects37) == 0:
                                        pass
                                        # State 69225
                                        if len(subjects) == 0:
                                            pass
                                            # 307: c*cos(d + x*e)**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f5) and (cons_f48) and (cons_f47)
                                            yield 307, subst5
                                            # 303: c*cos(d + x*e)**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                                            yield 303, subst5
                                            # 311: c*cos(d + x*e)**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f228)
                                            yield 311, subst5
                                subjects37.appendleft(tmp40)
                        if len(subjects37) >= 1 and isinstance(subjects37[0], Mul):
                            tmp42 = subjects37.popleft()
                            associative1 = tmp42
                            associative_type1 = type(tmp42)
                            subjects43 = deque(tmp42._args)
                            matcher = CommutativeMatcher69227.get()
                            tmp44 = subjects43
                            subjects43 = []
                            for s in tmp44:
                                matcher.add_subject(s)
                            for pattern_index, subst4 in matcher.match(tmp44, subst3):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 69228
                                    if len(subjects37) == 0:
                                        pass
                                        # State 69229
                                        if len(subjects) == 0:
                                            pass
                                            # 307: c*cos(d + x*e)**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f5) and (cons_f48) and (cons_f47)
                                            yield 307, subst4
                                            # 303: c*cos(d + x*e)**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                                            yield 303, subst4
                                            # 311: c*cos(d + x*e)**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f228)
                                            yield 311, subst4
                            subjects37.appendleft(tmp42)
                    if len(subjects37) >= 1 and isinstance(subjects37[0], Add):
                        tmp45 = subjects37.popleft()
                        associative1 = tmp45
                        associative_type1 = type(tmp45)
                        subjects46 = deque(tmp45._args)
                        matcher = CommutativeMatcher69231.get()
                        tmp47 = subjects46
                        subjects46 = []
                        for s in tmp47:
                            matcher.add_subject(s)
                        for pattern_index, subst3 in matcher.match(tmp47, subst2):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 69237
                                if len(subjects37) == 0:
                                    pass
                                    # State 69238
                                    if len(subjects) == 0:
                                        pass
                                        # 307: c*cos(d + x*e)**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f5) and (cons_f48) and (cons_f47)
                                        yield 307, subst3
                                        # 303: c*cos(d + x*e)**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                                        yield 303, subst3
                                        # 311: c*cos(d + x*e)**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f228)
                                        yield 311, subst3
                        subjects37.appendleft(tmp45)
                    subjects.appendleft(tmp36)
                if len(subjects) >= 1 and isinstance(subjects[0], tan):
                    tmp48 = subjects.popleft()
                    subjects49 = deque(tmp48._args)
                    # State 83544
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i3.1.3.0', S(0))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 83545
                        subst4 = Substitution(subst3)
                        try:
                            subst4.try_add_variable('i3.1.3.1.0_1', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 83546
                            if len(subjects49) >= 1:
                                tmp52 = subjects49.popleft()
                                subst5 = Substitution(subst4)
                                try:
                                    subst5.try_add_variable('i3.1.3.1.0', tmp52)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 83547
                                    if len(subjects49) == 0:
                                        pass
                                        # State 83548
                                        if len(subjects) == 0:
                                            pass
                                            # 347: c*tan(d + x*e)**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f228)
                                            yield 347, subst5
                                            # 343: c*tan(d + x*e)**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                                            yield 343, subst5
                                subjects49.appendleft(tmp52)
                        if len(subjects49) >= 1 and isinstance(subjects49[0], Mul):
                            tmp54 = subjects49.popleft()
                            associative1 = tmp54
                            associative_type1 = type(tmp54)
                            subjects55 = deque(tmp54._args)
                            matcher = CommutativeMatcher83550.get()
                            tmp56 = subjects55
                            subjects55 = []
                            for s in tmp56:
                                matcher.add_subject(s)
                            for pattern_index, subst4 in matcher.match(tmp56, subst3):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 83551
                                    if len(subjects49) == 0:
                                        pass
                                        # State 83552
                                        if len(subjects) == 0:
                                            pass
                                            # 347: c*tan(d + x*e)**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f228)
                                            yield 347, subst4
                                            # 343: c*tan(d + x*e)**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                                            yield 343, subst4
                            subjects49.appendleft(tmp54)
                    if len(subjects49) >= 1 and isinstance(subjects49[0], Add):
                        tmp57 = subjects49.popleft()
                        associative1 = tmp57
                        associative_type1 = type(tmp57)
                        subjects58 = deque(tmp57._args)
                        matcher = CommutativeMatcher83554.get()
                        tmp59 = subjects58
                        subjects58 = []
                        for s in tmp59:
                            matcher.add_subject(s)
                        for pattern_index, subst3 in matcher.match(tmp59, subst2):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 83560
                                if len(subjects49) == 0:
                                    pass
                                    # State 83561
                                    if len(subjects) == 0:
                                        pass
                                        # 347: c*tan(d + x*e)**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f228)
                                        yield 347, subst3
                                        # 343: c*tan(d + x*e)**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                                        yield 343, subst3
                        subjects49.appendleft(tmp57)
                    subjects.appendleft(tmp48)
            subst2 = Substitution(subst1)
            try:
                subst2.try_add_variable('i3.1.5_1', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 83921
                if len(subjects) >= 1 and isinstance(subjects[0], Pow):
                    tmp61 = subjects.popleft()
                    subjects62 = deque(tmp61._args)
                    # State 83922
                    if len(subjects62) >= 1 and isinstance(subjects62[0], tan):
                        tmp63 = subjects62.popleft()
                        subjects64 = deque(tmp63._args)
                        # State 83923
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i3.1.4.0', S(0))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 83924
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i3.1.4.1.0_1', S(1))
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 83925
                                if len(subjects64) >= 1:
                                    tmp67 = subjects64.popleft()
                                    subst5 = Substitution(subst4)
                                    try:
                                        subst5.try_add_variable('i3.1.4.1.0', tmp67)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 83926
                                        if len(subjects64) == 0:
                                            pass
                                            # State 83927
                                            if len(subjects62) >= 1 and subjects62[0] == Integer(-1):
                                                tmp69 = subjects62.popleft()
                                                # State 83928
                                                if len(subjects62) == 0:
                                                    pass
                                                    # State 83929
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 345: c*(1/tan(d + x*e))**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                                                        yield 345, subst5
                                                        # 349: c*(1/tan(d + x*e))**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f228)
                                                        yield 349, subst5
                                                subjects62.appendleft(tmp69)
                                    subjects64.appendleft(tmp67)
                            if len(subjects64) >= 1 and isinstance(subjects64[0], Mul):
                                tmp70 = subjects64.popleft()
                                associative1 = tmp70
                                associative_type1 = type(tmp70)
                                subjects71 = deque(tmp70._args)
                                matcher = CommutativeMatcher83931.get()
                                tmp72 = subjects71
                                subjects71 = []
                                for s in tmp72:
                                    matcher.add_subject(s)
                                for pattern_index, subst4 in matcher.match(tmp72, subst3):
                                    pass
                                    if pattern_index == 0:
                                        pass
                                        # State 83932
                                        if len(subjects64) == 0:
                                            pass
                                            # State 83933
                                            if len(subjects62) >= 1 and subjects62[0] == Integer(-1):
                                                tmp73 = subjects62.popleft()
                                                # State 83934
                                                if len(subjects62) == 0:
                                                    pass
                                                    # State 83935
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 345: c*(1/tan(d + x*e))**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                                                        yield 345, subst4
                                                        # 349: c*(1/tan(d + x*e))**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f228)
                                                        yield 349, subst4
                                                subjects62.appendleft(tmp73)
                                subjects64.appendleft(tmp70)
                        if len(subjects64) >= 1 and isinstance(subjects64[0], Add):
                            tmp74 = subjects64.popleft()
                            associative1 = tmp74
                            associative_type1 = type(tmp74)
                            subjects75 = deque(tmp74._args)
                            matcher = CommutativeMatcher83937.get()
                            tmp76 = subjects75
                            subjects75 = []
                            for s in tmp76:
                                matcher.add_subject(s)
                            for pattern_index, subst3 in matcher.match(tmp76, subst2):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 83943
                                    if len(subjects64) == 0:
                                        pass
                                        # State 83944
                                        if len(subjects62) >= 1 and subjects62[0] == Integer(-1):
                                            tmp77 = subjects62.popleft()
                                            # State 83945
                                            if len(subjects62) == 0:
                                                pass
                                                # State 83946
                                                if len(subjects) == 0:
                                                    pass
                                                    # 345: c*(1/tan(d + x*e))**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                                                    yield 345, subst3
                                                    # 349: c*(1/tan(d + x*e))**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f228)
                                                    yield 349, subst3
                                            subjects62.appendleft(tmp77)
                            subjects64.appendleft(tmp74)
                        subjects62.appendleft(tmp63)
                    if len(subjects62) >= 1 and isinstance(subjects62[0], cos):
                        tmp78 = subjects62.popleft()
                        subjects79 = deque(tmp78._args)
                        # State 95626
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i3.1.4.0', S(0))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 95627
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i3.1.4.1.0_1', S(1))
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 95628
                                if len(subjects79) >= 1:
                                    tmp82 = subjects79.popleft()
                                    subst5 = Substitution(subst4)
                                    try:
                                        subst5.try_add_variable('i3.1.4.1.0', tmp82)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 95629
                                        if len(subjects79) == 0:
                                            pass
                                            # State 95630
                                            if len(subjects62) >= 1 and subjects62[0] == Integer(-1):
                                                tmp84 = subjects62.popleft()
                                                # State 95631
                                                if len(subjects62) == 0:
                                                    pass
                                                    # State 95632
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 379: c*(1/cos(d + x*e))**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f5) and (cons_f48) and (cons_f47)
                                                        yield 379, subst5
                                                        # 375: c*(1/cos(d + x*e))**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                                                        yield 375, subst5
                                                        # 383: c*(1/cos(d + x*e))**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f228)
                                                        yield 383, subst5
                                                subjects62.appendleft(tmp84)
                                    subjects79.appendleft(tmp82)
                            if len(subjects79) >= 1 and isinstance(subjects79[0], Mul):
                                tmp85 = subjects79.popleft()
                                associative1 = tmp85
                                associative_type1 = type(tmp85)
                                subjects86 = deque(tmp85._args)
                                matcher = CommutativeMatcher95634.get()
                                tmp87 = subjects86
                                subjects86 = []
                                for s in tmp87:
                                    matcher.add_subject(s)
                                for pattern_index, subst4 in matcher.match(tmp87, subst3):
                                    pass
                                    if pattern_index == 0:
                                        pass
                                        # State 95635
                                        if len(subjects79) == 0:
                                            pass
                                            # State 95636
                                            if len(subjects62) >= 1 and subjects62[0] == Integer(-1):
                                                tmp88 = subjects62.popleft()
                                                # State 95637
                                                if len(subjects62) == 0:
                                                    pass
                                                    # State 95638
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 379: c*(1/cos(d + x*e))**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f5) and (cons_f48) and (cons_f47)
                                                        yield 379, subst4
                                                        # 375: c*(1/cos(d + x*e))**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                                                        yield 375, subst4
                                                        # 383: c*(1/cos(d + x*e))**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f228)
                                                        yield 383, subst4
                                                subjects62.appendleft(tmp88)
                                subjects79.appendleft(tmp85)
                        if len(subjects79) >= 1 and isinstance(subjects79[0], Add):
                            tmp89 = subjects79.popleft()
                            associative1 = tmp89
                            associative_type1 = type(tmp89)
                            subjects90 = deque(tmp89._args)
                            matcher = CommutativeMatcher95640.get()
                            tmp91 = subjects90
                            subjects90 = []
                            for s in tmp91:
                                matcher.add_subject(s)
                            for pattern_index, subst3 in matcher.match(tmp91, subst2):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 95646
                                    if len(subjects79) == 0:
                                        pass
                                        # State 95647
                                        if len(subjects62) >= 1 and subjects62[0] == Integer(-1):
                                            tmp92 = subjects62.popleft()
                                            # State 95648
                                            if len(subjects62) == 0:
                                                pass
                                                # State 95649
                                                if len(subjects) == 0:
                                                    pass
                                                    # 379: c*(1/cos(d + x*e))**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f5) and (cons_f48) and (cons_f47)
                                                    yield 379, subst3
                                                    # 375: c*(1/cos(d + x*e))**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                                                    yield 375, subst3
                                                    # 383: c*(1/cos(d + x*e))**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f228)
                                                    yield 383, subst3
                                            subjects62.appendleft(tmp92)
                            subjects79.appendleft(tmp89)
                        subjects62.appendleft(tmp78)
                    if len(subjects62) >= 1 and isinstance(subjects62[0], sin):
                        tmp93 = subjects62.popleft()
                        subjects94 = deque(tmp93._args)
                        # State 96022
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i3.1.4.0', S(0))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 96023
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i3.1.4.1.0_1', S(1))
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 96024
                                if len(subjects94) >= 1:
                                    tmp97 = subjects94.popleft()
                                    subst5 = Substitution(subst4)
                                    try:
                                        subst5.try_add_variable('i3.1.4.1.0', tmp97)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 96025
                                        if len(subjects94) == 0:
                                            pass
                                            # State 96026
                                            if len(subjects62) >= 1 and subjects62[0] == Integer(-1):
                                                tmp99 = subjects62.popleft()
                                                # State 96027
                                                if len(subjects62) == 0:
                                                    pass
                                                    # State 96028
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 377: c*(1/sin(d + x*e))**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                                                        yield 377, subst5
                                                        # 385: c*(1/sin(d + x*e))**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f228)
                                                        yield 385, subst5
                                                        # 381: c*(1/sin(d + x*e))**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f5) and (cons_f48) and (cons_f47)
                                                        yield 381, subst5
                                                subjects62.appendleft(tmp99)
                                    subjects94.appendleft(tmp97)
                            if len(subjects94) >= 1 and isinstance(subjects94[0], Mul):
                                tmp100 = subjects94.popleft()
                                associative1 = tmp100
                                associative_type1 = type(tmp100)
                                subjects101 = deque(tmp100._args)
                                matcher = CommutativeMatcher96030.get()
                                tmp102 = subjects101
                                subjects101 = []
                                for s in tmp102:
                                    matcher.add_subject(s)
                                for pattern_index, subst4 in matcher.match(tmp102, subst3):
                                    pass
                                    if pattern_index == 0:
                                        pass
                                        # State 96031
                                        if len(subjects94) == 0:
                                            pass
                                            # State 96032
                                            if len(subjects62) >= 1 and subjects62[0] == Integer(-1):
                                                tmp103 = subjects62.popleft()
                                                # State 96033
                                                if len(subjects62) == 0:
                                                    pass
                                                    # State 96034
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 377: c*(1/sin(d + x*e))**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                                                        yield 377, subst4
                                                        # 385: c*(1/sin(d + x*e))**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f228)
                                                        yield 385, subst4
                                                        # 381: c*(1/sin(d + x*e))**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f5) and (cons_f48) and (cons_f47)
                                                        yield 381, subst4
                                                subjects62.appendleft(tmp103)
                                subjects94.appendleft(tmp100)
                        if len(subjects94) >= 1 and isinstance(subjects94[0], Add):
                            tmp104 = subjects94.popleft()
                            associative1 = tmp104
                            associative_type1 = type(tmp104)
                            subjects105 = deque(tmp104._args)
                            matcher = CommutativeMatcher96036.get()
                            tmp106 = subjects105
                            subjects105 = []
                            for s in tmp106:
                                matcher.add_subject(s)
                            for pattern_index, subst3 in matcher.match(tmp106, subst2):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 96042
                                    if len(subjects94) == 0:
                                        pass
                                        # State 96043
                                        if len(subjects62) >= 1 and subjects62[0] == Integer(-1):
                                            tmp107 = subjects62.popleft()
                                            # State 96044
                                            if len(subjects62) == 0:
                                                pass
                                                # State 96045
                                                if len(subjects) == 0:
                                                    pass
                                                    # 377: c*(1/sin(d + x*e))**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                                                    yield 377, subst3
                                                    # 385: c*(1/sin(d + x*e))**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f228)
                                                    yield 385, subst3
                                                    # 381: c*(1/sin(d + x*e))**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f5) and (cons_f48) and (cons_f47)
                                                    yield 381, subst3
                                            subjects62.appendleft(tmp107)
                            subjects94.appendleft(tmp104)
                        subjects62.appendleft(tmp93)
                    subjects.appendleft(tmp61)
            if len(subjects) >= 1 and isinstance(subjects[0], Pow):
                tmp108 = subjects.popleft()
                subjects109 = deque(tmp108._args)
                # State 8172
                if len(subjects109) >= 1:
                    tmp110 = subjects109.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i3.1.1', tmp110)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 8173
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i3.1.2_1', 1)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 8174
                            if len(subjects109) == 0:
                                pass
                                # State 8175
                                if len(subjects) == 0:
                                    pass
                                    # 129: c*x**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f52) and (cons_f754) and (cons_f755) and (cons_f228) and (cons_f756)
                                    yield 129, subst3
                                    # 132: c*x**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f52) and (cons_f754) and (cons_f755) and (cons_f228)
                                    yield 132, subst3
                                    # 134: c*x**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f52) and (cons_f754) and (cons_f755)
                                    yield 134, subst3
                                    # 137: c*x**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f52) and (cons_f754)
                                    yield 137, subst3
                                    # 139: c*x**n2 /; (cons_f2) and (cons_f52) and (cons_f754) and (cons_f70) and (cons_f71)
                                    yield 139, subst3
                                    # 148: c*x**n2 /; (cons_f2) and (cons_f3) and (cons_f798) and (cons_f4) and (cons_f5) and (cons_f954) and (cons_f955)
                                    yield 148, subst3
                                    # 150: c*x**n2 /; (cons_f2) and (cons_f3) and (cons_f798) and (cons_f4) and (cons_f954) and (cons_f956)
                                    yield 150, subst3
                                    # 152: c*x**n2 /; (cons_f2) and (cons_f3) and (cons_f798) and (cons_f4) and (cons_f5) and (cons_f954) and (cons_f956)
                                    yield 152, subst3
                                    # 154: c*x**n2 /; (cons_f2) and (cons_f3) and (cons_f958) and (cons_f959)
                                    yield 154, subst3
                                    # 156: c*x**n2 /; (cons_f2) and (cons_f3) and (cons_f958) and (cons_f959) and (cons_f961)
                                    yield 156, subst3
                                    # 158: c*x**n2 /; (cons_f2) and (cons_f3) and (cons_f958) and (cons_f959) and (cons_f962)
                                    yield 158, subst3
                                    # 160: c*x**n2 /; (cons_f2) and (cons_f3) and (cons_f798) and (cons_f4) and (cons_f954)
                                    yield 160, subst3
                                    # 164: c*x**n2 /; (cons_f2) and (cons_f3) and (cons_f966) and (cons_f967)
                                    yield 164, subst3
                                    # 166: c*x**n2 /; (cons_f2) and (cons_f3) and (cons_f798) and (cons_f4) and (cons_f5) and (cons_f954) and (cons_f968)
                                    yield 166, subst3
                                    # 168: c*x**n2 /; (cons_f3) and (cons_f4) and (cons_f70) and (cons_f71)
                                    yield 168, subst3
                                    # 72: c*x**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f48)
                                    yield 72, subst3
                                    # 74: c*x**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f5) and (cons_f48)
                                    yield 74, subst3
                                    # 76: c*x**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f48) and (cons_f47)
                                    yield 76, subst3
                                    # 79: c*x**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f48) and (cons_f47)
                                    yield 79, subst3
                                    # 83: c*x**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f5) and (cons_f48) and (cons_f47)
                                    yield 83, subst3
                                    # 89: c*x**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f48) and (cons_f228)
                                    yield 89, subst3
                                    # 115: c*x**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f682)
                                    yield 115, subst3
                                    # 117: c*x**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f587) and (cons_f683)
                                    yield 117, subst3
                                    # 119: c*x**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f587) and (cons_f683)
                                    yield 119, subst3
                                    # 121: c*x**n2 /; (cons_f8) and (cons_f48) and (cons_f70) and (cons_f71)
                                    yield 121, subst3
                                    # 123: c*x**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f752)
                                    yield 123, subst3
                                    # 126: c*x**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f52) and (cons_f754) and (cons_f755)
                                    yield 126, subst3
                        if len(subjects109) >= 1:
                            tmp113 = subjects109.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i3.1.2_1', tmp113)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 8174
                                if len(subjects109) == 0:
                                    pass
                                    # State 8175
                                    if len(subjects) == 0:
                                        pass
                                        # 129: c*x**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f52) and (cons_f754) and (cons_f755) and (cons_f228) and (cons_f756)
                                        yield 129, subst3
                                        # 132: c*x**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f52) and (cons_f754) and (cons_f755) and (cons_f228)
                                        yield 132, subst3
                                        # 134: c*x**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f52) and (cons_f754) and (cons_f755)
                                        yield 134, subst3
                                        # 137: c*x**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f52) and (cons_f754)
                                        yield 137, subst3
                                        # 139: c*x**n2 /; (cons_f2) and (cons_f52) and (cons_f754) and (cons_f70) and (cons_f71)
                                        yield 139, subst3
                                        # 148: c*x**n2 /; (cons_f2) and (cons_f3) and (cons_f798) and (cons_f4) and (cons_f5) and (cons_f954) and (cons_f955)
                                        yield 148, subst3
                                        # 150: c*x**n2 /; (cons_f2) and (cons_f3) and (cons_f798) and (cons_f4) and (cons_f954) and (cons_f956)
                                        yield 150, subst3
                                        # 152: c*x**n2 /; (cons_f2) and (cons_f3) and (cons_f798) and (cons_f4) and (cons_f5) and (cons_f954) and (cons_f956)
                                        yield 152, subst3
                                        # 154: c*x**n2 /; (cons_f2) and (cons_f3) and (cons_f958) and (cons_f959)
                                        yield 154, subst3
                                        # 156: c*x**n2 /; (cons_f2) and (cons_f3) and (cons_f958) and (cons_f959) and (cons_f961)
                                        yield 156, subst3
                                        # 158: c*x**n2 /; (cons_f2) and (cons_f3) and (cons_f958) and (cons_f959) and (cons_f962)
                                        yield 158, subst3
                                        # 160: c*x**n2 /; (cons_f2) and (cons_f3) and (cons_f798) and (cons_f4) and (cons_f954)
                                        yield 160, subst3
                                        # 164: c*x**n2 /; (cons_f2) and (cons_f3) and (cons_f966) and (cons_f967)
                                        yield 164, subst3
                                        # 166: c*x**n2 /; (cons_f2) and (cons_f3) and (cons_f798) and (cons_f4) and (cons_f5) and (cons_f954) and (cons_f968)
                                        yield 166, subst3
                                        # 168: c*x**n2 /; (cons_f3) and (cons_f4) and (cons_f70) and (cons_f71)
                                        yield 168, subst3
                                        # 72: c*x**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f48)
                                        yield 72, subst3
                                        # 74: c*x**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f5) and (cons_f48)
                                        yield 74, subst3
                                        # 76: c*x**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f48) and (cons_f47)
                                        yield 76, subst3
                                        # 79: c*x**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f48) and (cons_f47)
                                        yield 79, subst3
                                        # 83: c*x**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f5) and (cons_f48) and (cons_f47)
                                        yield 83, subst3
                                        # 89: c*x**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f48) and (cons_f228)
                                        yield 89, subst3
                                        # 115: c*x**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f682)
                                        yield 115, subst3
                                        # 117: c*x**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f587) and (cons_f683)
                                        yield 117, subst3
                                        # 119: c*x**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f587) and (cons_f683)
                                        yield 119, subst3
                                        # 121: c*x**n2 /; (cons_f8) and (cons_f48) and (cons_f70) and (cons_f71)
                                        yield 121, subst3
                                        # 123: c*x**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f752)
                                        yield 123, subst3
                                        # 126: c*x**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f52) and (cons_f754) and (cons_f755)
                                        yield 126, subst3
                            subjects109.appendleft(tmp113)
                        if len(subjects109) >= 1:
                            tmp115 = subjects109.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i3.1.2_1', tmp115)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 8206
                                if len(subjects109) == 0:
                                    pass
                                    # State 8207
                                    if len(subjects) == 0:
                                        pass
                                        # 81: c*x**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f48) and (cons_f47)
                                        yield 81, subst3
                                        # 93: c*x**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f48) and (cons_f228) and (cons_f415)
                                        yield 93, subst3
                                        # 95: c*x**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f48) and (cons_f228)
                                        yield 95, subst3
                            subjects109.appendleft(tmp115)
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i3.1.2', 1)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 12101
                            if len(subjects109) == 0:
                                pass
                                # State 12102
                                if len(subjects) == 0:
                                    pass
                                    # 162: b*x**n /; (cons_f2) and (cons_f3) and (cons_f4) and (cons_f965)
                                    yield 162, subst3
                        if len(subjects109) >= 1:
                            tmp118 = subjects109.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i3.1.2', tmp118)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 12101
                                if len(subjects109) == 0:
                                    pass
                                    # State 12102
                                    if len(subjects) == 0:
                                        pass
                                        # 162: b*x**n /; (cons_f2) and (cons_f3) and (cons_f4) and (cons_f965)
                                        yield 162, subst3
                            subjects109.appendleft(tmp118)
                        if len(subjects109) >= 1 and subjects109[0] == Integer(4):
                            tmp120 = subjects109.popleft()
                            # State 8266
                            if len(subjects109) == 0:
                                pass
                                # State 8267
                                if len(subjects) == 0:
                                    pass
                                    # 97: c*x**4 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f677) and (cons_f295)
                                    yield 97, subst2
                                    # 99: c*x**4 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f677) and (cons_f678)
                                    yield 99, subst2
                                    # 101: c*x**4 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f677) and (cons_f179) and (With1098)
                                    yield 101, subst2
                                    # 102: c*x**4 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f677) and (cons_f179)
                                    yield 102, subst2
                                    # 104: c*x**4 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f677) and (With1100)
                                    yield 104, subst2
                                    # 106: c*x**4 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f677) and (With1101)
                                    yield 106, subst2
                                    # 108: c*x**4 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f677) and (With1102)
                                    yield 108, subst2
                                    # 110: c*x**4 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f677) and (With1103)
                                    yield 110, subst2
                                    # 112: c*x**4 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f228) and (cons_f680)
                                    yield 112, subst2
                                    # 113: c*x**4 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f228) and (cons_f681)
                                    yield 113, subst2
                            subjects109.appendleft(tmp120)
                        if len(subjects109) >= 1 and subjects109[0] == Integer(3):
                            tmp121 = subjects109.popleft()
                            # State 12359
                            if len(subjects109) == 0:
                                pass
                                # State 12360
                                if len(subjects) == 0:
                                    pass
                                    # 192: d*x**3 /; (cons_f2) and (cons_f8) and (cons_f29) and (cons_f5) and (cons_f1004)
                                    yield 192, subst2
                                    # 224: d*x**3 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f1021)
                                    yield 224, subst2
                                    # 194: d*x**3 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1005)
                                    yield 194, subst2
                                    # 199: d*x**3 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1008)
                                    yield 199, subst2
                                    # 204: d*x**3 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1008) and (With1777)
                                    yield 204, subst2
                                    # 207: d*x**3 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f5) and (cons_f1005)
                                    yield 207, subst2
                                    # 188: d*x**3 /; (cons_f2) and (cons_f8) and (cons_f29) and (cons_f5) and (cons_f1003)
                                    yield 188, subst2
                                    # 212: d*x**3 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f5) and (cons_f1008)
                                    yield 212, subst2
                                    # 182: d*x**3 /; (cons_f2) and (cons_f8) and (cons_f29) and (cons_f1003)
                                    yield 182, subst2
                                    # 215: d*x**3 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f5) and (cons_f1008) and (With1782)
                                    yield 215, subst2
                                    # 184: d*x**3 /; (cons_f2) and (cons_f8) and (cons_f29) and (cons_f1004)
                                    yield 184, subst2
                                    # 186: d*x**3 /; (cons_f2) and (cons_f8) and (cons_f29) and (cons_f1004) and (With1761)
                                    yield 186, subst2
                                    # 220: d*x**3 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f5) and (cons_f1016)
                                    yield 220, subst2
                                    # 190: d*x**3 /; (cons_f2) and (cons_f8) and (cons_f29) and (cons_f5) and (cons_f1004) and (With1764)
                                    yield 190, subst2
                            subjects109.appendleft(tmp121)
                    subjects109.appendleft(tmp110)
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i3.1.2.0', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 10947
                    if len(subjects109) >= 1 and isinstance(subjects109[0], Pow):
                        tmp123 = subjects109.popleft()
                        subjects124 = deque(tmp123._args)
                        # State 10948
                        if len(subjects124) >= 1:
                            tmp125 = subjects124.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i3.1.2.1', tmp125)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 10949
                                if len(subjects124) >= 1 and subjects124[0] == Integer(-1):
                                    tmp127 = subjects124.popleft()
                                    # State 10950
                                    if len(subjects124) == 0:
                                        pass
                                        # State 10951
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i3.1.2_1', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 10952
                                            if len(subjects109) == 0:
                                                pass
                                                # State 10953
                                                if len(subjects) == 0:
                                                    pass
                                                    # 144: c*(c/x)**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f5) and (cons_f48)
                                                    yield 144, subst4
                                        if len(subjects109) >= 1:
                                            tmp129 = subjects109.popleft()
                                            subst4 = Substitution(subst3)
                                            try:
                                                subst4.try_add_variable('i3.1.2_1', tmp129)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 10952
                                                if len(subjects109) == 0:
                                                    pass
                                                    # State 10953
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 144: c*(c/x)**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f5) and (cons_f48)
                                                        yield 144, subst4
                                            subjects109.appendleft(tmp129)
                                    subjects124.appendleft(tmp127)
                            subjects124.appendleft(tmp125)
                        subjects109.appendleft(tmp123)
                if len(subjects109) >= 1:
                    tmp131 = subjects109.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i3.1.2.1', tmp131)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 11177
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i3.1.2_1', 1)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 11178
                            if len(subjects109) == 0:
                                pass
                                # State 11179
                                if len(subjects) == 0:
                                    pass
                                    # 146: c*x**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f5) and (cons_f809)
                                    yield 146, subst3
                        if len(subjects109) >= 1:
                            tmp134 = subjects109.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i3.1.2_1', tmp134)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 11178
                                if len(subjects109) == 0:
                                    pass
                                    # State 11179
                                    if len(subjects) == 0:
                                        pass
                                        # 146: c*x**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f5) and (cons_f809)
                                        yield 146, subst3
                            subjects109.appendleft(tmp134)
                    subjects109.appendleft(tmp131)
                if len(subjects109) >= 1 and isinstance(subjects109[0], Mul):
                    tmp136 = subjects109.popleft()
                    associative1 = tmp136
                    associative_type1 = type(tmp136)
                    subjects137 = deque(tmp136._args)
                    matcher = CommutativeMatcher10955.get()
                    tmp138 = subjects137
                    subjects137 = []
                    for s in tmp138:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp138, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 10960
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i3.1.2_1', 1)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 10961
                                if len(subjects109) == 0:
                                    pass
                                    # State 10962
                                    if len(subjects) == 0:
                                        pass
                                        # 144: c*(c/x)**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f5) and (cons_f48)
                                        yield 144, subst3
                            if len(subjects109) >= 1:
                                tmp140 = []
                                tmp140.append(subjects109.popleft())
                                while True:
                                    if len(tmp140) > 1:
                                        tmp141 = create_operation_expression(associative1, tmp140)
                                    elif len(tmp140) == 1:
                                        tmp141 = tmp140[0]
                                    else:
                                        assert False, "Unreachable"
                                    subst3 = Substitution(subst2)
                                    try:
                                        subst3.try_add_variable('i3.1.2_1', tmp141)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 10961
                                        if len(subjects109) == 0:
                                            pass
                                            # State 10962
                                            if len(subjects) == 0:
                                                pass
                                                # 144: c*(c/x)**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f5) and (cons_f48)
                                                yield 144, subst3
                                    if len(subjects109) == 0:
                                        break
                                    tmp140.append(subjects109.popleft())
                                subjects109.extendleft(reversed(tmp140))
                    subjects109.appendleft(tmp136)
                if len(subjects109) >= 1 and isinstance(subjects109[0], tan):
                    tmp143 = subjects109.popleft()
                    subjects144 = deque(tmp143._args)
                    # State 67229
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i3.1.3.0', S(0))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 67230
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i3.1.3.1.0_1', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 67231
                            if len(subjects144) >= 1:
                                tmp147 = subjects144.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i3.1.3.1.0', tmp147)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 67232
                                    if len(subjects144) == 0:
                                        pass
                                        # State 67233
                                        if len(subjects109) >= 1 and subjects109[0] == Integer(-1):
                                            tmp149 = subjects109.popleft()
                                            # State 67234
                                            if len(subjects109) == 0:
                                                pass
                                                # State 67235
                                                if len(subjects) == 0:
                                                    pass
                                                    # 287: c/tan(d + x*e) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f1045)
                                                    yield 287, subst4
                                            subjects109.appendleft(tmp149)
                                        subst5 = Substitution(subst4)
                                        try:
                                            subst5.try_add_variable('i3.1.3_1', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 83562
                                            if len(subjects109) == 0:
                                                pass
                                                # State 83563
                                                if len(subjects) == 0:
                                                    pass
                                                    # 347: c*tan(d + x*e)**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f228)
                                                    yield 347, subst5
                                                    # 343: c*tan(d + x*e)**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                                                    yield 343, subst5
                                        if len(subjects109) >= 1:
                                            tmp151 = subjects109.popleft()
                                            subst5 = Substitution(subst4)
                                            try:
                                                subst5.try_add_variable('i3.1.3_1', tmp151)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 83562
                                                if len(subjects109) == 0:
                                                    pass
                                                    # State 83563
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 347: c*tan(d + x*e)**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f228)
                                                        yield 347, subst5
                                                        # 343: c*tan(d + x*e)**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                                                        yield 343, subst5
                                            subjects109.appendleft(tmp151)
                                subjects144.appendleft(tmp147)
                        if len(subjects144) >= 1 and isinstance(subjects144[0], Mul):
                            tmp153 = subjects144.popleft()
                            associative1 = tmp153
                            associative_type1 = type(tmp153)
                            subjects154 = deque(tmp153._args)
                            matcher = CommutativeMatcher67237.get()
                            tmp155 = subjects154
                            subjects154 = []
                            for s in tmp155:
                                matcher.add_subject(s)
                            for pattern_index, subst3 in matcher.match(tmp155, subst2):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 67238
                                    if len(subjects144) == 0:
                                        pass
                                        # State 67239
                                        if len(subjects109) >= 1 and subjects109[0] == Integer(-1):
                                            tmp156 = subjects109.popleft()
                                            # State 67240
                                            if len(subjects109) == 0:
                                                pass
                                                # State 67241
                                                if len(subjects) == 0:
                                                    pass
                                                    # 287: c/tan(d + x*e) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f1045)
                                                    yield 287, subst3
                                            subjects109.appendleft(tmp156)
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i3.1.3_1', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 83564
                                            if len(subjects109) == 0:
                                                pass
                                                # State 83565
                                                if len(subjects) == 0:
                                                    pass
                                                    # 347: c*tan(d + x*e)**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f228)
                                                    yield 347, subst4
                                                    # 343: c*tan(d + x*e)**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                                                    yield 343, subst4
                                        if len(subjects109) >= 1:
                                            tmp158 = subjects109.popleft()
                                            subst4 = Substitution(subst3)
                                            try:
                                                subst4.try_add_variable('i3.1.3_1', tmp158)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 83564
                                                if len(subjects109) == 0:
                                                    pass
                                                    # State 83565
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 347: c*tan(d + x*e)**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f228)
                                                        yield 347, subst4
                                                        # 343: c*tan(d + x*e)**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                                                        yield 343, subst4
                                            subjects109.appendleft(tmp158)
                            subjects144.appendleft(tmp153)
                    if len(subjects144) >= 1 and isinstance(subjects144[0], Add):
                        tmp160 = subjects144.popleft()
                        associative1 = tmp160
                        associative_type1 = type(tmp160)
                        subjects161 = deque(tmp160._args)
                        matcher = CommutativeMatcher67243.get()
                        tmp162 = subjects161
                        subjects161 = []
                        for s in tmp162:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp162, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 67249
                                if len(subjects144) == 0:
                                    pass
                                    # State 67250
                                    if len(subjects109) >= 1 and subjects109[0] == Integer(-1):
                                        tmp163 = subjects109.popleft()
                                        # State 67251
                                        if len(subjects109) == 0:
                                            pass
                                            # State 67252
                                            if len(subjects) == 0:
                                                pass
                                                # 287: c/tan(d + x*e) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f1045)
                                                yield 287, subst2
                                        subjects109.appendleft(tmp163)
                                    subst3 = Substitution(subst2)
                                    try:
                                        subst3.try_add_variable('i3.1.3_1', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 83566
                                        if len(subjects109) == 0:
                                            pass
                                            # State 83567
                                            if len(subjects) == 0:
                                                pass
                                                # 347: c*tan(d + x*e)**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f228)
                                                yield 347, subst3
                                                # 343: c*tan(d + x*e)**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                                                yield 343, subst3
                                    if len(subjects109) >= 1:
                                        tmp165 = subjects109.popleft()
                                        subst3 = Substitution(subst2)
                                        try:
                                            subst3.try_add_variable('i3.1.3_1', tmp165)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 83566
                                            if len(subjects109) == 0:
                                                pass
                                                # State 83567
                                                if len(subjects) == 0:
                                                    pass
                                                    # 347: c*tan(d + x*e)**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f228)
                                                    yield 347, subst3
                                                    # 343: c*tan(d + x*e)**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                                                    yield 343, subst3
                                        subjects109.appendleft(tmp165)
                        subjects144.appendleft(tmp160)
                    subjects109.appendleft(tmp143)
                if len(subjects109) >= 1 and isinstance(subjects109[0], sin):
                    tmp167 = subjects109.popleft()
                    subjects168 = deque(tmp167._args)
                    # State 68962
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i3.1.3.0', S(0))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 68963
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i3.1.3.1.0_1', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 68964
                            if len(subjects168) >= 1:
                                tmp171 = subjects168.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i3.1.3.1.0', tmp171)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 68965
                                    if len(subjects168) == 0:
                                        pass
                                        # State 68966
                                        subst5 = Substitution(subst4)
                                        try:
                                            subst5.try_add_variable('i3.1.3_1', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 68967
                                            if len(subjects109) == 0:
                                                pass
                                                # State 68968
                                                if len(subjects) == 0:
                                                    pass
                                                    # 305: c*sin(d + x*e)**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f5) and (cons_f48) and (cons_f47)
                                                    yield 305, subst5
                                                    # 301: c*sin(d + x*e)**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                                                    yield 301, subst5
                                                    # 309: c*sin(d + x*e)**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f228)
                                                    yield 309, subst5
                                        if len(subjects109) >= 1:
                                            tmp174 = subjects109.popleft()
                                            subst5 = Substitution(subst4)
                                            try:
                                                subst5.try_add_variable('i3.1.3_1', tmp174)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 68967
                                                if len(subjects109) == 0:
                                                    pass
                                                    # State 68968
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 305: c*sin(d + x*e)**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f5) and (cons_f48) and (cons_f47)
                                                        yield 305, subst5
                                                        # 301: c*sin(d + x*e)**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                                                        yield 301, subst5
                                                        # 309: c*sin(d + x*e)**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f228)
                                                        yield 309, subst5
                                            subjects109.appendleft(tmp174)
                                subjects168.appendleft(tmp171)
                        if len(subjects168) >= 1 and isinstance(subjects168[0], Mul):
                            tmp176 = subjects168.popleft()
                            associative1 = tmp176
                            associative_type1 = type(tmp176)
                            subjects177 = deque(tmp176._args)
                            matcher = CommutativeMatcher68970.get()
                            tmp178 = subjects177
                            subjects177 = []
                            for s in tmp178:
                                matcher.add_subject(s)
                            for pattern_index, subst3 in matcher.match(tmp178, subst2):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 68971
                                    if len(subjects168) == 0:
                                        pass
                                        # State 68972
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i3.1.3_1', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 68973
                                            if len(subjects109) == 0:
                                                pass
                                                # State 68974
                                                if len(subjects) == 0:
                                                    pass
                                                    # 305: c*sin(d + x*e)**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f5) and (cons_f48) and (cons_f47)
                                                    yield 305, subst4
                                                    # 301: c*sin(d + x*e)**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                                                    yield 301, subst4
                                                    # 309: c*sin(d + x*e)**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f228)
                                                    yield 309, subst4
                                        if len(subjects109) >= 1:
                                            tmp180 = subjects109.popleft()
                                            subst4 = Substitution(subst3)
                                            try:
                                                subst4.try_add_variable('i3.1.3_1', tmp180)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 68973
                                                if len(subjects109) == 0:
                                                    pass
                                                    # State 68974
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 305: c*sin(d + x*e)**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f5) and (cons_f48) and (cons_f47)
                                                        yield 305, subst4
                                                        # 301: c*sin(d + x*e)**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                                                        yield 301, subst4
                                                        # 309: c*sin(d + x*e)**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f228)
                                                        yield 309, subst4
                                            subjects109.appendleft(tmp180)
                            subjects168.appendleft(tmp176)
                    if len(subjects168) >= 1 and isinstance(subjects168[0], Add):
                        tmp182 = subjects168.popleft()
                        associative1 = tmp182
                        associative_type1 = type(tmp182)
                        subjects183 = deque(tmp182._args)
                        matcher = CommutativeMatcher68976.get()
                        tmp184 = subjects183
                        subjects183 = []
                        for s in tmp184:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp184, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 68982
                                if len(subjects168) == 0:
                                    pass
                                    # State 68983
                                    subst3 = Substitution(subst2)
                                    try:
                                        subst3.try_add_variable('i3.1.3_1', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 68984
                                        if len(subjects109) == 0:
                                            pass
                                            # State 68985
                                            if len(subjects) == 0:
                                                pass
                                                # 305: c*sin(d + x*e)**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f5) and (cons_f48) and (cons_f47)
                                                yield 305, subst3
                                                # 301: c*sin(d + x*e)**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                                                yield 301, subst3
                                                # 309: c*sin(d + x*e)**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f228)
                                                yield 309, subst3
                                    if len(subjects109) >= 1:
                                        tmp186 = subjects109.popleft()
                                        subst3 = Substitution(subst2)
                                        try:
                                            subst3.try_add_variable('i3.1.3_1', tmp186)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 68984
                                            if len(subjects109) == 0:
                                                pass
                                                # State 68985
                                                if len(subjects) == 0:
                                                    pass
                                                    # 305: c*sin(d + x*e)**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f5) and (cons_f48) and (cons_f47)
                                                    yield 305, subst3
                                                    # 301: c*sin(d + x*e)**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                                                    yield 301, subst3
                                                    # 309: c*sin(d + x*e)**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f228)
                                                    yield 309, subst3
                                        subjects109.appendleft(tmp186)
                        subjects168.appendleft(tmp182)
                    subjects109.appendleft(tmp167)
                if len(subjects109) >= 1 and isinstance(subjects109[0], cos):
                    tmp188 = subjects109.popleft()
                    subjects189 = deque(tmp188._args)
                    # State 69239
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i3.1.3.0', S(0))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 69240
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i3.1.3.1.0_1', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 69241
                            if len(subjects189) >= 1:
                                tmp192 = subjects189.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i3.1.3.1.0', tmp192)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 69242
                                    if len(subjects189) == 0:
                                        pass
                                        # State 69243
                                        subst5 = Substitution(subst4)
                                        try:
                                            subst5.try_add_variable('i3.1.3_1', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 69244
                                            if len(subjects109) == 0:
                                                pass
                                                # State 69245
                                                if len(subjects) == 0:
                                                    pass
                                                    # 307: c*cos(d + x*e)**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f5) and (cons_f48) and (cons_f47)
                                                    yield 307, subst5
                                                    # 303: c*cos(d + x*e)**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                                                    yield 303, subst5
                                                    # 311: c*cos(d + x*e)**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f228)
                                                    yield 311, subst5
                                        if len(subjects109) >= 1:
                                            tmp195 = subjects109.popleft()
                                            subst5 = Substitution(subst4)
                                            try:
                                                subst5.try_add_variable('i3.1.3_1', tmp195)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 69244
                                                if len(subjects109) == 0:
                                                    pass
                                                    # State 69245
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 307: c*cos(d + x*e)**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f5) and (cons_f48) and (cons_f47)
                                                        yield 307, subst5
                                                        # 303: c*cos(d + x*e)**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                                                        yield 303, subst5
                                                        # 311: c*cos(d + x*e)**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f228)
                                                        yield 311, subst5
                                            subjects109.appendleft(tmp195)
                                subjects189.appendleft(tmp192)
                        if len(subjects189) >= 1 and isinstance(subjects189[0], Mul):
                            tmp197 = subjects189.popleft()
                            associative1 = tmp197
                            associative_type1 = type(tmp197)
                            subjects198 = deque(tmp197._args)
                            matcher = CommutativeMatcher69247.get()
                            tmp199 = subjects198
                            subjects198 = []
                            for s in tmp199:
                                matcher.add_subject(s)
                            for pattern_index, subst3 in matcher.match(tmp199, subst2):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 69248
                                    if len(subjects189) == 0:
                                        pass
                                        # State 69249
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i3.1.3_1', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 69250
                                            if len(subjects109) == 0:
                                                pass
                                                # State 69251
                                                if len(subjects) == 0:
                                                    pass
                                                    # 307: c*cos(d + x*e)**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f5) and (cons_f48) and (cons_f47)
                                                    yield 307, subst4
                                                    # 303: c*cos(d + x*e)**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                                                    yield 303, subst4
                                                    # 311: c*cos(d + x*e)**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f228)
                                                    yield 311, subst4
                                        if len(subjects109) >= 1:
                                            tmp201 = subjects109.popleft()
                                            subst4 = Substitution(subst3)
                                            try:
                                                subst4.try_add_variable('i3.1.3_1', tmp201)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 69250
                                                if len(subjects109) == 0:
                                                    pass
                                                    # State 69251
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 307: c*cos(d + x*e)**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f5) and (cons_f48) and (cons_f47)
                                                        yield 307, subst4
                                                        # 303: c*cos(d + x*e)**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                                                        yield 303, subst4
                                                        # 311: c*cos(d + x*e)**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f228)
                                                        yield 311, subst4
                                            subjects109.appendleft(tmp201)
                            subjects189.appendleft(tmp197)
                    if len(subjects189) >= 1 and isinstance(subjects189[0], Add):
                        tmp203 = subjects189.popleft()
                        associative1 = tmp203
                        associative_type1 = type(tmp203)
                        subjects204 = deque(tmp203._args)
                        matcher = CommutativeMatcher69253.get()
                        tmp205 = subjects204
                        subjects204 = []
                        for s in tmp205:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp205, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 69259
                                if len(subjects189) == 0:
                                    pass
                                    # State 69260
                                    subst3 = Substitution(subst2)
                                    try:
                                        subst3.try_add_variable('i3.1.3_1', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 69261
                                        if len(subjects109) == 0:
                                            pass
                                            # State 69262
                                            if len(subjects) == 0:
                                                pass
                                                # 307: c*cos(d + x*e)**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f5) and (cons_f48) and (cons_f47)
                                                yield 307, subst3
                                                # 303: c*cos(d + x*e)**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                                                yield 303, subst3
                                                # 311: c*cos(d + x*e)**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f228)
                                                yield 311, subst3
                                    if len(subjects109) >= 1:
                                        tmp207 = subjects109.popleft()
                                        subst3 = Substitution(subst2)
                                        try:
                                            subst3.try_add_variable('i3.1.3_1', tmp207)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 69261
                                            if len(subjects109) == 0:
                                                pass
                                                # State 69262
                                                if len(subjects) == 0:
                                                    pass
                                                    # 307: c*cos(d + x*e)**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f5) and (cons_f48) and (cons_f47)
                                                    yield 307, subst3
                                                    # 303: c*cos(d + x*e)**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                                                    yield 303, subst3
                                                    # 311: c*cos(d + x*e)**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f228)
                                                    yield 311, subst3
                                        subjects109.appendleft(tmp207)
                        subjects189.appendleft(tmp203)
                    subjects109.appendleft(tmp188)
                if len(subjects109) >= 1 and isinstance(subjects109[0], Pow):
                    tmp209 = subjects109.popleft()
                    subjects210 = deque(tmp209._args)
                    # State 83947
                    if len(subjects210) >= 1 and isinstance(subjects210[0], tan):
                        tmp211 = subjects210.popleft()
                        subjects212 = deque(tmp211._args)
                        # State 83948
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i3.1.4.0', S(0))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 83949
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i3.1.4.1.0_1', S(1))
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 83950
                                if len(subjects212) >= 1:
                                    tmp215 = subjects212.popleft()
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i3.1.4.1.0', tmp215)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 83951
                                        if len(subjects212) == 0:
                                            pass
                                            # State 83952
                                            if len(subjects210) >= 1 and subjects210[0] == Integer(-1):
                                                tmp217 = subjects210.popleft()
                                                # State 83953
                                                if len(subjects210) == 0:
                                                    pass
                                                    # State 83954
                                                    subst5 = Substitution(subst4)
                                                    try:
                                                        subst5.try_add_variable('i3.1.5_1', 1)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 83955
                                                        if len(subjects109) == 0:
                                                            pass
                                                            # State 83956
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 345: c*(1/tan(d + x*e))**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                                                                yield 345, subst5
                                                                # 349: c*(1/tan(d + x*e))**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f228)
                                                                yield 349, subst5
                                                    if len(subjects109) >= 1:
                                                        tmp219 = subjects109.popleft()
                                                        subst5 = Substitution(subst4)
                                                        try:
                                                            subst5.try_add_variable('i3.1.5_1', tmp219)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            # State 83955
                                                            if len(subjects109) == 0:
                                                                pass
                                                                # State 83956
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 345: c*(1/tan(d + x*e))**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                                                                    yield 345, subst5
                                                                    # 349: c*(1/tan(d + x*e))**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f228)
                                                                    yield 349, subst5
                                                        subjects109.appendleft(tmp219)
                                                subjects210.appendleft(tmp217)
                                    subjects212.appendleft(tmp215)
                            if len(subjects212) >= 1 and isinstance(subjects212[0], Mul):
                                tmp221 = subjects212.popleft()
                                associative1 = tmp221
                                associative_type1 = type(tmp221)
                                subjects222 = deque(tmp221._args)
                                matcher = CommutativeMatcher83958.get()
                                tmp223 = subjects222
                                subjects222 = []
                                for s in tmp223:
                                    matcher.add_subject(s)
                                for pattern_index, subst3 in matcher.match(tmp223, subst2):
                                    pass
                                    if pattern_index == 0:
                                        pass
                                        # State 83959
                                        if len(subjects212) == 0:
                                            pass
                                            # State 83960
                                            if len(subjects210) >= 1 and subjects210[0] == Integer(-1):
                                                tmp224 = subjects210.popleft()
                                                # State 83961
                                                if len(subjects210) == 0:
                                                    pass
                                                    # State 83962
                                                    subst4 = Substitution(subst3)
                                                    try:
                                                        subst4.try_add_variable('i3.1.5_1', 1)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 83963
                                                        if len(subjects109) == 0:
                                                            pass
                                                            # State 83964
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 345: c*(1/tan(d + x*e))**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                                                                yield 345, subst4
                                                                # 349: c*(1/tan(d + x*e))**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f228)
                                                                yield 349, subst4
                                                    if len(subjects109) >= 1:
                                                        tmp226 = subjects109.popleft()
                                                        subst4 = Substitution(subst3)
                                                        try:
                                                            subst4.try_add_variable('i3.1.5_1', tmp226)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            # State 83963
                                                            if len(subjects109) == 0:
                                                                pass
                                                                # State 83964
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 345: c*(1/tan(d + x*e))**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                                                                    yield 345, subst4
                                                                    # 349: c*(1/tan(d + x*e))**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f228)
                                                                    yield 349, subst4
                                                        subjects109.appendleft(tmp226)
                                                subjects210.appendleft(tmp224)
                                subjects212.appendleft(tmp221)
                        if len(subjects212) >= 1 and isinstance(subjects212[0], Add):
                            tmp228 = subjects212.popleft()
                            associative1 = tmp228
                            associative_type1 = type(tmp228)
                            subjects229 = deque(tmp228._args)
                            matcher = CommutativeMatcher83966.get()
                            tmp230 = subjects229
                            subjects229 = []
                            for s in tmp230:
                                matcher.add_subject(s)
                            for pattern_index, subst2 in matcher.match(tmp230, subst1):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 83972
                                    if len(subjects212) == 0:
                                        pass
                                        # State 83973
                                        if len(subjects210) >= 1 and subjects210[0] == Integer(-1):
                                            tmp231 = subjects210.popleft()
                                            # State 83974
                                            if len(subjects210) == 0:
                                                pass
                                                # State 83975
                                                subst3 = Substitution(subst2)
                                                try:
                                                    subst3.try_add_variable('i3.1.5_1', 1)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 83976
                                                    if len(subjects109) == 0:
                                                        pass
                                                        # State 83977
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 345: c*(1/tan(d + x*e))**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                                                            yield 345, subst3
                                                            # 349: c*(1/tan(d + x*e))**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f228)
                                                            yield 349, subst3
                                                if len(subjects109) >= 1:
                                                    tmp233 = subjects109.popleft()
                                                    subst3 = Substitution(subst2)
                                                    try:
                                                        subst3.try_add_variable('i3.1.5_1', tmp233)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 83976
                                                        if len(subjects109) == 0:
                                                            pass
                                                            # State 83977
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 345: c*(1/tan(d + x*e))**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                                                                yield 345, subst3
                                                                # 349: c*(1/tan(d + x*e))**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f228)
                                                                yield 349, subst3
                                                    subjects109.appendleft(tmp233)
                                            subjects210.appendleft(tmp231)
                            subjects212.appendleft(tmp228)
                        subjects210.appendleft(tmp211)
                    if len(subjects210) >= 1 and isinstance(subjects210[0], cos):
                        tmp235 = subjects210.popleft()
                        subjects236 = deque(tmp235._args)
                        # State 95650
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i3.1.4.0', S(0))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 95651
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i3.1.4.1.0_1', S(1))
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 95652
                                if len(subjects236) >= 1:
                                    tmp239 = subjects236.popleft()
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i3.1.4.1.0', tmp239)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 95653
                                        if len(subjects236) == 0:
                                            pass
                                            # State 95654
                                            if len(subjects210) >= 1 and subjects210[0] == Integer(-1):
                                                tmp241 = subjects210.popleft()
                                                # State 95655
                                                if len(subjects210) == 0:
                                                    pass
                                                    # State 95656
                                                    subst5 = Substitution(subst4)
                                                    try:
                                                        subst5.try_add_variable('i3.1.5_1', 1)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 95657
                                                        if len(subjects109) == 0:
                                                            pass
                                                            # State 95658
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 379: c*(1/cos(d + x*e))**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f5) and (cons_f48) and (cons_f47)
                                                                yield 379, subst5
                                                                # 375: c*(1/cos(d + x*e))**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                                                                yield 375, subst5
                                                                # 383: c*(1/cos(d + x*e))**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f228)
                                                                yield 383, subst5
                                                    if len(subjects109) >= 1:
                                                        tmp243 = subjects109.popleft()
                                                        subst5 = Substitution(subst4)
                                                        try:
                                                            subst5.try_add_variable('i3.1.5_1', tmp243)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            # State 95657
                                                            if len(subjects109) == 0:
                                                                pass
                                                                # State 95658
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 379: c*(1/cos(d + x*e))**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f5) and (cons_f48) and (cons_f47)
                                                                    yield 379, subst5
                                                                    # 375: c*(1/cos(d + x*e))**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                                                                    yield 375, subst5
                                                                    # 383: c*(1/cos(d + x*e))**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f228)
                                                                    yield 383, subst5
                                                        subjects109.appendleft(tmp243)
                                                subjects210.appendleft(tmp241)
                                    subjects236.appendleft(tmp239)
                            if len(subjects236) >= 1 and isinstance(subjects236[0], Mul):
                                tmp245 = subjects236.popleft()
                                associative1 = tmp245
                                associative_type1 = type(tmp245)
                                subjects246 = deque(tmp245._args)
                                matcher = CommutativeMatcher95660.get()
                                tmp247 = subjects246
                                subjects246 = []
                                for s in tmp247:
                                    matcher.add_subject(s)
                                for pattern_index, subst3 in matcher.match(tmp247, subst2):
                                    pass
                                    if pattern_index == 0:
                                        pass
                                        # State 95661
                                        if len(subjects236) == 0:
                                            pass
                                            # State 95662
                                            if len(subjects210) >= 1 and subjects210[0] == Integer(-1):
                                                tmp248 = subjects210.popleft()
                                                # State 95663
                                                if len(subjects210) == 0:
                                                    pass
                                                    # State 95664
                                                    subst4 = Substitution(subst3)
                                                    try:
                                                        subst4.try_add_variable('i3.1.5_1', 1)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 95665
                                                        if len(subjects109) == 0:
                                                            pass
                                                            # State 95666
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 379: c*(1/cos(d + x*e))**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f5) and (cons_f48) and (cons_f47)
                                                                yield 379, subst4
                                                                # 375: c*(1/cos(d + x*e))**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                                                                yield 375, subst4
                                                                # 383: c*(1/cos(d + x*e))**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f228)
                                                                yield 383, subst4
                                                    if len(subjects109) >= 1:
                                                        tmp250 = subjects109.popleft()
                                                        subst4 = Substitution(subst3)
                                                        try:
                                                            subst4.try_add_variable('i3.1.5_1', tmp250)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            # State 95665
                                                            if len(subjects109) == 0:
                                                                pass
                                                                # State 95666
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 379: c*(1/cos(d + x*e))**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f5) and (cons_f48) and (cons_f47)
                                                                    yield 379, subst4
                                                                    # 375: c*(1/cos(d + x*e))**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                                                                    yield 375, subst4
                                                                    # 383: c*(1/cos(d + x*e))**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f228)
                                                                    yield 383, subst4
                                                        subjects109.appendleft(tmp250)
                                                subjects210.appendleft(tmp248)
                                subjects236.appendleft(tmp245)
                        if len(subjects236) >= 1 and isinstance(subjects236[0], Add):
                            tmp252 = subjects236.popleft()
                            associative1 = tmp252
                            associative_type1 = type(tmp252)
                            subjects253 = deque(tmp252._args)
                            matcher = CommutativeMatcher95668.get()
                            tmp254 = subjects253
                            subjects253 = []
                            for s in tmp254:
                                matcher.add_subject(s)
                            for pattern_index, subst2 in matcher.match(tmp254, subst1):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 95674
                                    if len(subjects236) == 0:
                                        pass
                                        # State 95675
                                        if len(subjects210) >= 1 and subjects210[0] == Integer(-1):
                                            tmp255 = subjects210.popleft()
                                            # State 95676
                                            if len(subjects210) == 0:
                                                pass
                                                # State 95677
                                                subst3 = Substitution(subst2)
                                                try:
                                                    subst3.try_add_variable('i3.1.5_1', 1)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 95678
                                                    if len(subjects109) == 0:
                                                        pass
                                                        # State 95679
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 379: c*(1/cos(d + x*e))**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f5) and (cons_f48) and (cons_f47)
                                                            yield 379, subst3
                                                            # 375: c*(1/cos(d + x*e))**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                                                            yield 375, subst3
                                                            # 383: c*(1/cos(d + x*e))**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f228)
                                                            yield 383, subst3
                                                if len(subjects109) >= 1:
                                                    tmp257 = subjects109.popleft()
                                                    subst3 = Substitution(subst2)
                                                    try:
                                                        subst3.try_add_variable('i3.1.5_1', tmp257)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 95678
                                                        if len(subjects109) == 0:
                                                            pass
                                                            # State 95679
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 379: c*(1/cos(d + x*e))**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f5) and (cons_f48) and (cons_f47)
                                                                yield 379, subst3
                                                                # 375: c*(1/cos(d + x*e))**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                                                                yield 375, subst3
                                                                # 383: c*(1/cos(d + x*e))**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f228)
                                                                yield 383, subst3
                                                    subjects109.appendleft(tmp257)
                                            subjects210.appendleft(tmp255)
                            subjects236.appendleft(tmp252)
                        subjects210.appendleft(tmp235)
                    if len(subjects210) >= 1 and isinstance(subjects210[0], sin):
                        tmp259 = subjects210.popleft()
                        subjects260 = deque(tmp259._args)
                        # State 96046
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i3.1.4.0', S(0))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 96047
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i3.1.4.1.0_1', S(1))
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 96048
                                if len(subjects260) >= 1:
                                    tmp263 = subjects260.popleft()
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i3.1.4.1.0', tmp263)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 96049
                                        if len(subjects260) == 0:
                                            pass
                                            # State 96050
                                            if len(subjects210) >= 1 and subjects210[0] == Integer(-1):
                                                tmp265 = subjects210.popleft()
                                                # State 96051
                                                if len(subjects210) == 0:
                                                    pass
                                                    # State 96052
                                                    subst5 = Substitution(subst4)
                                                    try:
                                                        subst5.try_add_variable('i3.1.5_1', 1)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 96053
                                                        if len(subjects109) == 0:
                                                            pass
                                                            # State 96054
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 377: c*(1/sin(d + x*e))**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                                                                yield 377, subst5
                                                                # 385: c*(1/sin(d + x*e))**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f228)
                                                                yield 385, subst5
                                                                # 381: c*(1/sin(d + x*e))**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f5) and (cons_f48) and (cons_f47)
                                                                yield 381, subst5
                                                    if len(subjects109) >= 1:
                                                        tmp267 = subjects109.popleft()
                                                        subst5 = Substitution(subst4)
                                                        try:
                                                            subst5.try_add_variable('i3.1.5_1', tmp267)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            # State 96053
                                                            if len(subjects109) == 0:
                                                                pass
                                                                # State 96054
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 377: c*(1/sin(d + x*e))**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                                                                    yield 377, subst5
                                                                    # 385: c*(1/sin(d + x*e))**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f228)
                                                                    yield 385, subst5
                                                                    # 381: c*(1/sin(d + x*e))**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f5) and (cons_f48) and (cons_f47)
                                                                    yield 381, subst5
                                                        subjects109.appendleft(tmp267)
                                                subjects210.appendleft(tmp265)
                                    subjects260.appendleft(tmp263)
                            if len(subjects260) >= 1 and isinstance(subjects260[0], Mul):
                                tmp269 = subjects260.popleft()
                                associative1 = tmp269
                                associative_type1 = type(tmp269)
                                subjects270 = deque(tmp269._args)
                                matcher = CommutativeMatcher96056.get()
                                tmp271 = subjects270
                                subjects270 = []
                                for s in tmp271:
                                    matcher.add_subject(s)
                                for pattern_index, subst3 in matcher.match(tmp271, subst2):
                                    pass
                                    if pattern_index == 0:
                                        pass
                                        # State 96057
                                        if len(subjects260) == 0:
                                            pass
                                            # State 96058
                                            if len(subjects210) >= 1 and subjects210[0] == Integer(-1):
                                                tmp272 = subjects210.popleft()
                                                # State 96059
                                                if len(subjects210) == 0:
                                                    pass
                                                    # State 96060
                                                    subst4 = Substitution(subst3)
                                                    try:
                                                        subst4.try_add_variable('i3.1.5_1', 1)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 96061
                                                        if len(subjects109) == 0:
                                                            pass
                                                            # State 96062
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 377: c*(1/sin(d + x*e))**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                                                                yield 377, subst4
                                                                # 385: c*(1/sin(d + x*e))**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f228)
                                                                yield 385, subst4
                                                                # 381: c*(1/sin(d + x*e))**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f5) and (cons_f48) and (cons_f47)
                                                                yield 381, subst4
                                                    if len(subjects109) >= 1:
                                                        tmp274 = subjects109.popleft()
                                                        subst4 = Substitution(subst3)
                                                        try:
                                                            subst4.try_add_variable('i3.1.5_1', tmp274)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            # State 96061
                                                            if len(subjects109) == 0:
                                                                pass
                                                                # State 96062
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 377: c*(1/sin(d + x*e))**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                                                                    yield 377, subst4
                                                                    # 385: c*(1/sin(d + x*e))**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f228)
                                                                    yield 385, subst4
                                                                    # 381: c*(1/sin(d + x*e))**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f5) and (cons_f48) and (cons_f47)
                                                                    yield 381, subst4
                                                        subjects109.appendleft(tmp274)
                                                subjects210.appendleft(tmp272)
                                subjects260.appendleft(tmp269)
                        if len(subjects260) >= 1 and isinstance(subjects260[0], Add):
                            tmp276 = subjects260.popleft()
                            associative1 = tmp276
                            associative_type1 = type(tmp276)
                            subjects277 = deque(tmp276._args)
                            matcher = CommutativeMatcher96064.get()
                            tmp278 = subjects277
                            subjects277 = []
                            for s in tmp278:
                                matcher.add_subject(s)
                            for pattern_index, subst2 in matcher.match(tmp278, subst1):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 96070
                                    if len(subjects260) == 0:
                                        pass
                                        # State 96071
                                        if len(subjects210) >= 1 and subjects210[0] == Integer(-1):
                                            tmp279 = subjects210.popleft()
                                            # State 96072
                                            if len(subjects210) == 0:
                                                pass
                                                # State 96073
                                                subst3 = Substitution(subst2)
                                                try:
                                                    subst3.try_add_variable('i3.1.5_1', 1)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 96074
                                                    if len(subjects109) == 0:
                                                        pass
                                                        # State 96075
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 377: c*(1/sin(d + x*e))**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                                                            yield 377, subst3
                                                            # 385: c*(1/sin(d + x*e))**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f228)
                                                            yield 385, subst3
                                                            # 381: c*(1/sin(d + x*e))**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f5) and (cons_f48) and (cons_f47)
                                                            yield 381, subst3
                                                if len(subjects109) >= 1:
                                                    tmp281 = subjects109.popleft()
                                                    subst3 = Substitution(subst2)
                                                    try:
                                                        subst3.try_add_variable('i3.1.5_1', tmp281)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 96074
                                                        if len(subjects109) == 0:
                                                            pass
                                                            # State 96075
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 377: c*(1/sin(d + x*e))**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                                                                yield 377, subst3
                                                                # 385: c*(1/sin(d + x*e))**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f228)
                                                                yield 385, subst3
                                                                # 381: c*(1/sin(d + x*e))**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f5) and (cons_f48) and (cons_f47)
                                                                yield 381, subst3
                                                    subjects109.appendleft(tmp281)
                                            subjects210.appendleft(tmp279)
                            subjects260.appendleft(tmp276)
                        subjects210.appendleft(tmp259)
                    subjects109.appendleft(tmp209)
                subjects.appendleft(tmp108)
            if len(subjects) >= 1 and isinstance(subjects[0], sin):
                tmp283 = subjects.popleft()
                subjects284 = deque(tmp283._args)
                # State 66715
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i3.1.2.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 66716
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i3.1.2.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 66717
                        if len(subjects284) >= 1:
                            tmp287 = subjects284.popleft()
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i3.1.2.1.0', tmp287)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 66718
                                if len(subjects284) == 0:
                                    pass
                                    # State 66719
                                    if len(subjects) == 0:
                                        pass
                                        # 261: b*sin(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f1441)
                                        yield 261, subst4
                                        # 263: b*sin(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1442)
                                        yield 263, subst4
                                        # 265: b*sin(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f1446)
                                        yield 265, subst4
                                        # 267: b*sin(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f1447)
                                        yield 267, subst4
                                        # 269: b*sin(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f1450)
                                        yield 269, subst4
                                        # 271: b*sin(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f1451)
                                        yield 271, subst4
                                        # 273: b*sin(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f1452) and (cons_f1453)
                                        yield 273, subst4
                                        # 275: b*sin(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f1454) and (cons_f1452) and (cons_f1455)
                                        yield 275, subst4
                                        # 277: b*sin(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f1454)
                                        yield 277, subst4
                                        # 279: b*sin(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50)
                                        yield 279, subst4
                                        # 281: b*sin(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f78)
                                        yield 281, subst4
                                        # 283: b*sin(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f1457)
                                        yield 283, subst4
                            subjects284.appendleft(tmp287)
                    if len(subjects284) >= 1 and isinstance(subjects284[0], Mul):
                        tmp289 = subjects284.popleft()
                        associative1 = tmp289
                        associative_type1 = type(tmp289)
                        subjects290 = deque(tmp289._args)
                        matcher = CommutativeMatcher66721.get()
                        tmp291 = subjects290
                        subjects290 = []
                        for s in tmp291:
                            matcher.add_subject(s)
                        for pattern_index, subst3 in matcher.match(tmp291, subst2):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 66722
                                if len(subjects284) == 0:
                                    pass
                                    # State 66723
                                    if len(subjects) == 0:
                                        pass
                                        # 261: b*sin(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f1441)
                                        yield 261, subst3
                                        # 263: b*sin(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1442)
                                        yield 263, subst3
                                        # 265: b*sin(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f1446)
                                        yield 265, subst3
                                        # 267: b*sin(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f1447)
                                        yield 267, subst3
                                        # 269: b*sin(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f1450)
                                        yield 269, subst3
                                        # 271: b*sin(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f1451)
                                        yield 271, subst3
                                        # 273: b*sin(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f1452) and (cons_f1453)
                                        yield 273, subst3
                                        # 275: b*sin(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f1454) and (cons_f1452) and (cons_f1455)
                                        yield 275, subst3
                                        # 277: b*sin(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f1454)
                                        yield 277, subst3
                                        # 279: b*sin(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50)
                                        yield 279, subst3
                                        # 281: b*sin(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f78)
                                        yield 281, subst3
                                        # 283: b*sin(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f1457)
                                        yield 283, subst3
                        subjects284.appendleft(tmp289)
                if len(subjects284) >= 1 and isinstance(subjects284[0], Add):
                    tmp292 = subjects284.popleft()
                    associative1 = tmp292
                    associative_type1 = type(tmp292)
                    subjects293 = deque(tmp292._args)
                    matcher = CommutativeMatcher66725.get()
                    tmp294 = subjects293
                    subjects293 = []
                    for s in tmp294:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp294, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 66731
                            if len(subjects284) == 0:
                                pass
                                # State 66732
                                if len(subjects) == 0:
                                    pass
                                    # 261: b*sin(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f1441)
                                    yield 261, subst2
                                    # 263: b*sin(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1442)
                                    yield 263, subst2
                                    # 265: b*sin(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f1446)
                                    yield 265, subst2
                                    # 267: b*sin(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f1447)
                                    yield 267, subst2
                                    # 269: b*sin(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f1450)
                                    yield 269, subst2
                                    # 271: b*sin(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f1451)
                                    yield 271, subst2
                                    # 273: b*sin(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f1452) and (cons_f1453)
                                    yield 273, subst2
                                    # 275: b*sin(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f1454) and (cons_f1452) and (cons_f1455)
                                    yield 275, subst2
                                    # 277: b*sin(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f1454)
                                    yield 277, subst2
                                    # 279: b*sin(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50)
                                    yield 279, subst2
                                    # 281: b*sin(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f78)
                                    yield 281, subst2
                                    # 283: b*sin(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f1457)
                                    yield 283, subst2
                    subjects284.appendleft(tmp292)
                subjects.appendleft(tmp283)
            if len(subjects) >= 1 and isinstance(subjects[0], tan):
                tmp295 = subjects.popleft()
                subjects296 = deque(tmp295._args)
                # State 67138
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i3.1.3.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 67139
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i3.1.3.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 67140
                        if len(subjects296) >= 1:
                            tmp299 = subjects296.popleft()
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i3.1.3.1.0', tmp299)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 67141
                                if len(subjects296) == 0:
                                    pass
                                    # State 67142
                                    if len(subjects) == 0:
                                        pass
                                        # 285: c*tan(d + x*e) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f1045)
                                        yield 285, subst4
                            subjects296.appendleft(tmp299)
                    if len(subjects296) >= 1 and isinstance(subjects296[0], Mul):
                        tmp301 = subjects296.popleft()
                        associative1 = tmp301
                        associative_type1 = type(tmp301)
                        subjects302 = deque(tmp301._args)
                        matcher = CommutativeMatcher67144.get()
                        tmp303 = subjects302
                        subjects302 = []
                        for s in tmp303:
                            matcher.add_subject(s)
                        for pattern_index, subst3 in matcher.match(tmp303, subst2):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 67145
                                if len(subjects296) == 0:
                                    pass
                                    # State 67146
                                    if len(subjects) == 0:
                                        pass
                                        # 285: c*tan(d + x*e) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f1045)
                                        yield 285, subst3
                        subjects296.appendleft(tmp301)
                if len(subjects296) >= 1 and isinstance(subjects296[0], Add):
                    tmp304 = subjects296.popleft()
                    associative1 = tmp304
                    associative_type1 = type(tmp304)
                    subjects305 = deque(tmp304._args)
                    matcher = CommutativeMatcher67148.get()
                    tmp306 = subjects305
                    subjects305 = []
                    for s in tmp306:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp306, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 67154
                            if len(subjects296) == 0:
                                pass
                                # State 67155
                                if len(subjects) == 0:
                                    pass
                                    # 285: c*tan(d + x*e) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f1045)
                                    yield 285, subst2
                    subjects296.appendleft(tmp304)
                subjects.appendleft(tmp295)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i3.1.0', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 3889
            if len(subjects) >= 1 and isinstance(subjects[0], Pow):
                tmp308 = subjects.popleft()
                subjects309 = deque(tmp308._args)
                # State 3890
                if len(subjects309) >= 1:
                    tmp310 = subjects309.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i3.1.1', tmp310)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 3891
                        if len(subjects309) >= 1 and subjects309[0] == Integer(2):
                            tmp312 = subjects309.popleft()
                            # State 3892
                            if len(subjects309) == 0:
                                pass
                                # State 3893
                                if len(subjects) == 0:
                                    pass
                                    # 3: c*x**2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f47)
                                    yield 3, subst2
                                    # 5: c*x**2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f5) and (cons_f47)
                                    yield 5, subst2
                                    # 7: c*x**2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f228) and (cons_f229)
                                    yield 7, subst2
                                    # 9: c*x**2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f228) and (cons_f230)
                                    yield 9, subst2
                                    # 11: c*x**2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f228)
                                    yield 11, subst2
                                    # 13: c*x**2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f228) and (cons_f233) and (cons_f229)
                                    yield 13, subst2
                                    # 15: c*x**2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f228) and (With200)
                                    yield 15, subst2
                                    # 17: c*x**2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f5) and (cons_f234)
                                    yield 17, subst2
                                    # 19: c*x**2 /; (cons_f3) and (cons_f8) and (cons_f235)
                                    yield 19, subst2
                                    # 21: c*x**2 /; (cons_f3) and (cons_f8)
                                    yield 21, subst2
                                    # 23: c*x**2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f228) and (With206)
                                    yield 23, subst2
                                    # 25: c*x**2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f5) and (cons_f228)
                                    yield 25, subst2
                                    # 27: c*x**2 /; (cons_f8) and (cons_f70) and (cons_f71)
                                    yield 27, subst2
                                    # 161: c*x**2 /; (cons_f2) and (cons_f3) and (cons_f4)
                                    yield 161, subst2
                                    # 35: c*x**2 /; (cons_f2) and (cons_f3) and (cons_f468)
                                    yield 35, subst2
                                    # 36: c*x**2 /; (cons_f2) and (cons_f3) and (cons_f69)
                                    yield 36, subst2
                                    # 40: c*x**2 /; (cons_f2) and (cons_f3) and (cons_f470) and (cons_f472)
                                    yield 40, subst2
                                    # 41: c*x**2 /; (cons_f2) and (cons_f3) and (cons_f470) and (cons_f473)
                                    yield 41, subst2
                                    # 42: c*x**2 /; (cons_f2) and (cons_f3) and (cons_f470)
                                    yield 42, subst2
                                    # 43: c*x**2 /; (cons_f2) and (cons_f3) and (cons_f471) and (cons_f474)
                                    yield 43, subst2
                                    # 44: c*x**2 /; (cons_f2) and (cons_f3) and (cons_f471) and (cons_f475)
                                    yield 44, subst2
                                    # 45: c*x**2 /; (cons_f2) and (cons_f3) and (cons_f471)
                                    yield 45, subst2
                                    # 52: c*x**2 /; (cons_f2) and (cons_f3) and (cons_f481)
                                    yield 52, subst2
                                    # 53: c*x**2 /; (cons_f2) and (cons_f3) and (cons_f482)
                                    yield 53, subst2
                                    # 54: c*x**2 /; (cons_f2) and (cons_f3)
                                    yield 54, subst2
                                    # 181: c*x**2 /; (cons_f2) and (cons_f8) and (cons_f29) and (cons_f1003)
                                    yield 181, subst2
                                    # 183: c*x**2 /; (cons_f2) and (cons_f8) and (cons_f29) and (cons_f1004)
                                    yield 183, subst2
                                    # 185: c*x**2 /; (cons_f2) and (cons_f8) and (cons_f29) and (cons_f1004) and (With1761)
                                    yield 185, subst2
                                    # 187: c*x**2 /; (cons_f2) and (cons_f8) and (cons_f29) and (cons_f5) and (cons_f1003)
                                    yield 187, subst2
                                    # 189: c*x**2 /; (cons_f2) and (cons_f8) and (cons_f29) and (cons_f5) and (cons_f1004) and (With1764)
                                    yield 189, subst2
                                    # 62: c*x**2 /; (cons_f2) and (cons_f3) and (cons_f485)
                                    yield 62, subst2
                                    # 191: c*x**2 /; (cons_f2) and (cons_f8) and (cons_f29) and (cons_f5) and (cons_f1004)
                                    yield 191, subst2
                                    # 193: c*x**2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1005) and (cons_f1006)
                                    yield 193, subst2
                                    # 196: c*x**2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1005) and (cons_f1007)
                                    yield 196, subst2
                                    # 198: c*x**2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1008) and (cons_f1006)
                                    yield 198, subst2
                                    # 201: c*x**2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1008) and (cons_f1007)
                                    yield 201, subst2
                                    # 203: c*x**2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1008) and (cons_f1007) and (With1777)
                                    yield 203, subst2
                                    # 206: c*x**2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f5) and (cons_f1005) and (cons_f1006)
                                    yield 206, subst2
                                    # 209: c*x**2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f5) and (cons_f1005) and (cons_f1007)
                                    yield 209, subst2
                                    # 465: b*x**2 /; (cons_f3) and (cons_f69)
                                    yield 465, subst2
                                    # 211: c*x**2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f5) and (cons_f1008) and (cons_f1006)
                                    yield 211, subst2
                                    # 214: c*x**2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f5) and (cons_f1008) and (cons_f1007) and (With1782)
                                    yield 214, subst2
                                    # 217: c*x**2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f5) and (cons_f1008) and (cons_f1007)
                                    yield 217, subst2
                                    # 219: c*x**2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f5) and (cons_f1016)
                                    yield 219, subst2
                                    # 223: c*x**2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f1021)
                                    yield 223, subst2
                                    # 96: c*x**2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f677)
                                    yield 96, subst2
                                    # 98: c*x**2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f677) and (cons_f679)
                                    yield 98, subst2
                                    # 100: c*x**2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f677) and (With1098)
                                    yield 100, subst2
                                    # 103: c*x**2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f677) and (With1100)
                                    yield 103, subst2
                                    # 105: c*x**2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f677) and (With1101)
                                    yield 105, subst2
                                    # 107: c*x**2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f677) and (With1102)
                                    yield 107, subst2
                                    # 109: c*x**2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f677) and (With1103)
                                    yield 109, subst2
                                    # 111: c*x**2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f228)
                                    yield 111, subst2
                            subjects309.appendleft(tmp312)
                        if len(subjects309) >= 1:
                            tmp313 = subjects309.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i3.1.2', tmp313)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 6078
                                if len(subjects309) == 0:
                                    pass
                                    # State 6079
                                    if len(subjects) == 0:
                                        pass
                                        # 29: b*x**n /; (cons_f2) and (cons_f3) and (cons_f4) and (cons_f5) and (cons_f462)
                                        yield 29, subst3
                                        # 30: b*x**n /; (cons_f2) and (cons_f3) and (cons_f4) and (cons_f5) and (cons_f463)
                                        yield 30, subst3
                                        # 31: b*x**n /; (cons_f2) and (cons_f3) and (cons_f4) and (cons_f464)
                                        yield 31, subst3
                                        # 32: b*x**n /; (cons_f2) and (cons_f3) and (cons_f89) and (cons_f465)
                                        yield 32, subst3
                                        # 33: b*x**n /; (cons_f2) and (cons_f3) and (cons_f466)
                                        yield 33, subst3
                                        # 34: b*x**n /; (cons_f2) and (cons_f3) and (cons_f150) and (cons_f467)
                                        yield 34, subst3
                                        # 38: b*x**n /; (cons_f2) and (cons_f3) and (cons_f469) and (cons_f470)
                                        yield 38, subst3
                                        # 39: b*x**n /; (cons_f2) and (cons_f3) and (cons_f469) and (cons_f471)
                                        yield 39, subst3
                                        # 46: b*x**n /; (cons_f2) and (cons_f3) and (cons_f476) and (cons_f470)
                                        yield 46, subst3
                                        # 47: b*x**n /; (cons_f2) and (cons_f3) and (cons_f476) and (cons_f471)
                                        yield 47, subst3
                                        # 50: b*x**n /; (cons_f2) and (cons_f3) and (cons_f479) and (cons_f480)
                                        yield 50, subst3
                                        # 51: b*x**n /; (cons_f2) and (cons_f3) and (cons_f479) and (cons_f478)
                                        yield 51, subst3
                                        # 64: b*x**n /; (cons_f2) and (cons_f3) and (cons_f150) and (cons_f489)
                                        yield 64, subst3
                                        # 65: b*x**n /; (cons_f2) and (cons_f3) and (cons_f150) and (cons_f490)
                                        yield 65, subst3
                                        # 66: b*x**n /; (cons_f2) and (cons_f3) and (cons_f5) and (cons_f198)
                                        yield 66, subst3
                                        # 67: b*x**n /; (cons_f2) and (cons_f3) and (cons_f5) and (cons_f491)
                                        yield 67, subst3
                                        # 68: b*x**n /; (cons_f2) and (cons_f3) and (cons_f4)
                                        yield 68, subst3
                                        # 69: b*x**n /; (cons_f2) and (cons_f3) and (cons_f4) and (cons_f5) and (cons_f492) and (cons_f493)
                                        yield 69, subst3
                                        # 70: b*x**n /; (cons_f3) and (cons_f4) and (cons_f70) and (cons_f71)
                                        yield 70, subst3
                                        # 71: b*x**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f48) and (cons_f89) and (cons_f465)
                                        yield 71, subst3
                                        # 73: b*x**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f5) and (cons_f48) and (cons_f491)
                                        yield 73, subst3
                                        # 75: b*x**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f48) and (cons_f47) and (cons_f666)
                                        yield 75, subst3
                                        # 77: b*x**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f48) and (cons_f47) and (cons_f667) and (cons_f586)
                                        yield 77, subst3
                                        # 78: b*x**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f48) and (cons_f47) and (cons_f668)
                                        yield 78, subst3
                                        # 80: b*x**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f48) and (cons_f47) and (cons_f586) and (cons_f670) and (cons_f464)
                                        yield 80, subst3
                                        # 82: b*x**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f5) and (cons_f48) and (cons_f47) and (cons_f198)
                                        yield 82, subst3
                                        # 466: b*x**n /; (cons_f3) and (cons_f1481) and (cons_f746)
                                        yield 466, subst3
                                        # 84: b*x**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f48) and (cons_f47) and (cons_f671) and (cons_f672)
                                        yield 84, subst3
                                        # 85: b*x**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f48) and (cons_f47) and (cons_f673) and (cons_f674) and (cons_f340)
                                        yield 85, subst3
                                        # 86: b*x**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f48) and (cons_f47)
                                        yield 86, subst3
                                        # 87: b*x**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f5) and (cons_f48) and (cons_f198)
                                        yield 87, subst3
                                        # 88: b*x**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f48) and (cons_f228)
                                        yield 88, subst3
                                        # 467: b*x**n /; (cons_f3) and (cons_f1484) and (cons_f167)
                                        yield 467, subst3
                                        # 90: b*x**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f48) and (cons_f228) and (cons_f671) and (cons_f675)
                                        yield 90, subst3
                                        # 91: b*x**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f48) and (cons_f228) and (cons_f675)
                                        yield 91, subst3
                                        # 92: b*x**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f48) and (cons_f228) and (cons_f676) and (cons_f415)
                                        yield 92, subst3
                                        # 94: b*x**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f48) and (cons_f228)
                                        yield 94, subst3
                                        # 114: b*x**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f682)
                                        yield 114, subst3
                                        # 116: b*x**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f587)
                                        yield 116, subst3
                                        # 118: b*x**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f587)
                                        yield 118, subst3
                                        # 120: b*x**n /; (cons_f3) and (cons_f4) and (cons_f48) and (cons_f70) and (cons_f71)
                                        yield 120, subst3
                            subjects309.appendleft(tmp313)
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i3.1.2', 1)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 9753
                            if len(subjects309) == 0:
                                pass
                                # State 9754
                                if len(subjects) == 0:
                                    pass
                                    # 128: b*x**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f52) and (cons_f754) and (cons_f755) and (cons_f228) and (cons_f756)
                                    yield 128, subst3
                                    # 131: b*x**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f52) and (cons_f754) and (cons_f755) and (cons_f228)
                                    yield 131, subst3
                                    # 163: b*x**n /; (cons_f2) and (cons_f3) and (cons_f966) and (cons_f967)
                                    yield 163, subst3
                                    # 133: b*x**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f52) and (cons_f754) and (cons_f755)
                                    yield 133, subst3
                                    # 165: b*x**n /; (cons_f2) and (cons_f3) and (cons_f798) and (cons_f4) and (cons_f5) and (cons_f954) and (cons_f968)
                                    yield 165, subst3
                                    # 167: b*x**n /; (cons_f2) and (cons_f798) and (cons_f70) and (cons_f71)
                                    yield 167, subst3
                                    # 136: b*x**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f52) and (cons_f754)
                                    yield 136, subst3
                                    # 138: b*x**n /; (cons_f3) and (cons_f4) and (cons_f754) and (cons_f70) and (cons_f71)
                                    yield 138, subst3
                                    # 147: b*x**n /; (cons_f2) and (cons_f3) and (cons_f798) and (cons_f4) and (cons_f5) and (cons_f954) and (cons_f955)
                                    yield 147, subst3
                                    # 149: b*x**n /; (cons_f2) and (cons_f3) and (cons_f798) and (cons_f4) and (cons_f954) and (cons_f956)
                                    yield 149, subst3
                                    # 125: b*x**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f52) and (cons_f754) and (cons_f755)
                                    yield 125, subst3
                                    # 151: b*x**n /; (cons_f2) and (cons_f3) and (cons_f798) and (cons_f4) and (cons_f5) and (cons_f954) and (cons_f956) and (cons_f957)
                                    yield 151, subst3
                                    # 153: b*x**n /; (cons_f2) and (cons_f3) and (cons_f958) and (cons_f959) and (cons_f960)
                                    yield 153, subst3
                                    # 122: b*x**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f752) and (cons_f753)
                                    yield 122, subst3
                                    # 155: b*x**n /; (cons_f2) and (cons_f3) and (cons_f958) and (cons_f959)
                                    yield 155, subst3
                                    # 157: b*x**n /; (cons_f2) and (cons_f3) and (cons_f958) and (cons_f959) and (cons_f962)
                                    yield 157, subst3
                                    # 159: b*x**n /; (cons_f2) and (cons_f3) and (cons_f798) and (cons_f4) and (cons_f954) and (cons_f964)
                                    yield 159, subst3
                        if len(subjects309) >= 1:
                            tmp316 = subjects309.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i3.1.2', tmp316)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 9753
                                if len(subjects309) == 0:
                                    pass
                                    # State 9754
                                    if len(subjects) == 0:
                                        pass
                                        # 128: b*x**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f52) and (cons_f754) and (cons_f755) and (cons_f228) and (cons_f756)
                                        yield 128, subst3
                                        # 131: b*x**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f52) and (cons_f754) and (cons_f755) and (cons_f228)
                                        yield 131, subst3
                                        # 163: b*x**n /; (cons_f2) and (cons_f3) and (cons_f966) and (cons_f967)
                                        yield 163, subst3
                                        # 133: b*x**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f52) and (cons_f754) and (cons_f755)
                                        yield 133, subst3
                                        # 165: b*x**n /; (cons_f2) and (cons_f3) and (cons_f798) and (cons_f4) and (cons_f5) and (cons_f954) and (cons_f968)
                                        yield 165, subst3
                                        # 167: b*x**n /; (cons_f2) and (cons_f798) and (cons_f70) and (cons_f71)
                                        yield 167, subst3
                                        # 136: b*x**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f52) and (cons_f754)
                                        yield 136, subst3
                                        # 138: b*x**n /; (cons_f3) and (cons_f4) and (cons_f754) and (cons_f70) and (cons_f71)
                                        yield 138, subst3
                                        # 147: b*x**n /; (cons_f2) and (cons_f3) and (cons_f798) and (cons_f4) and (cons_f5) and (cons_f954) and (cons_f955)
                                        yield 147, subst3
                                        # 149: b*x**n /; (cons_f2) and (cons_f3) and (cons_f798) and (cons_f4) and (cons_f954) and (cons_f956)
                                        yield 149, subst3
                                        # 125: b*x**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f52) and (cons_f754) and (cons_f755)
                                        yield 125, subst3
                                        # 151: b*x**n /; (cons_f2) and (cons_f3) and (cons_f798) and (cons_f4) and (cons_f5) and (cons_f954) and (cons_f956) and (cons_f957)
                                        yield 151, subst3
                                        # 153: b*x**n /; (cons_f2) and (cons_f3) and (cons_f958) and (cons_f959) and (cons_f960)
                                        yield 153, subst3
                                        # 122: b*x**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f752) and (cons_f753)
                                        yield 122, subst3
                                        # 155: b*x**n /; (cons_f2) and (cons_f3) and (cons_f958) and (cons_f959)
                                        yield 155, subst3
                                        # 157: b*x**n /; (cons_f2) and (cons_f3) and (cons_f958) and (cons_f959) and (cons_f962)
                                        yield 157, subst3
                                        # 159: b*x**n /; (cons_f2) and (cons_f3) and (cons_f798) and (cons_f4) and (cons_f954) and (cons_f964)
                                        yield 159, subst3
                            subjects309.appendleft(tmp316)
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i3.1.3.0', S(0))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 101176
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i3.1.3.1.0_1', S(1))
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 101177
                                if len(subjects309) >= 1:
                                    tmp320 = subjects309.popleft()
                                    subst5 = Substitution(subst4)
                                    try:
                                        subst5.try_add_variable('i3.1.3.1.0', tmp320)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 101178
                                        if len(subjects309) == 0:
                                            pass
                                            # State 101179
                                            if len(subjects) == 0:
                                                pass
                                                # 394: b*F**(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1666)
                                                yield 394, subst5
                                    subjects309.appendleft(tmp320)
                            if len(subjects309) >= 1 and isinstance(subjects309[0], Mul):
                                tmp322 = subjects309.popleft()
                                associative1 = tmp322
                                associative_type1 = type(tmp322)
                                subjects323 = deque(tmp322._args)
                                matcher = CommutativeMatcher101181.get()
                                tmp324 = subjects323
                                subjects323 = []
                                for s in tmp324:
                                    matcher.add_subject(s)
                                for pattern_index, subst4 in matcher.match(tmp324, subst3):
                                    pass
                                    if pattern_index == 0:
                                        pass
                                        # State 101182
                                        if len(subjects309) == 0:
                                            pass
                                            # State 101183
                                            if len(subjects) == 0:
                                                pass
                                                # 394: b*F**(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1666)
                                                yield 394, subst4
                                subjects309.appendleft(tmp322)
                        if len(subjects309) >= 1 and subjects309[0] == Integer(3):
                            tmp325 = subjects309.popleft()
                            # State 6123
                            if len(subjects309) == 0:
                                pass
                                # State 6124
                                if len(subjects) == 0:
                                    pass
                                    # 37: b*x**3 /; (cons_f2) and (cons_f3) and (cons_f69)
                                    yield 37, subst2
                                    # 169: d*x**3 /; (cons_f2) and (cons_f3) and (cons_f29) and (cons_f1001)
                                    yield 169, subst2
                                    # 171: d*x**3 /; (cons_f2) and (cons_f3) and (cons_f29) and (cons_f1002)
                                    yield 171, subst2
                                    # 173: d*x**3 /; (cons_f2) and (cons_f3) and (cons_f29) and (cons_f1002) and (With1747)
                                    yield 173, subst2
                                    # 175: d*x**3 /; (cons_f2) and (cons_f3) and (cons_f29) and (cons_f5) and (cons_f1001)
                                    yield 175, subst2
                                    # 177: d*x**3 /; (cons_f2) and (cons_f3) and (cons_f29) and (cons_f5) and (cons_f1002) and (With1750)
                                    yield 177, subst2
                                    # 179: d*x**3 /; (cons_f2) and (cons_f3) and (cons_f29) and (cons_f5) and (cons_f1002)
                                    yield 179, subst2
                                    # 55: b*x**3 /; (cons_f2) and (cons_f3)
                                    yield 55, subst2
                            subjects309.appendleft(tmp325)
                        if len(subjects309) >= 1 and subjects309[0] == Integer(4):
                            tmp326 = subjects309.popleft()
                            # State 6183
                            if len(subjects309) == 0:
                                pass
                                # State 6184
                                if len(subjects) == 0:
                                    pass
                                    # 48: b*x**4 /; (cons_f2) and (cons_f3) and (cons_f477)
                                    yield 48, subst2
                                    # 49: b*x**4 /; (cons_f2) and (cons_f3) and (cons_f478)
                                    yield 49, subst2
                                    # 56: b*x**4 /; (cons_f2) and (cons_f3) and (cons_f468)
                                    yield 56, subst2
                                    # 57: b*x**4 /; (cons_f2) and (cons_f3) and (cons_f485)
                                    yield 57, subst2
                                    # 58: b*x**4 /; (cons_f2) and (cons_f3) and (cons_f107) and (With725)
                                    yield 58, subst2
                                    # 59: b*x**4 /; (cons_f2) and (cons_f3) and (cons_f107)
                                    yield 59, subst2
                                    # 63: b*x**4 /; (cons_f2) and (cons_f3) and (cons_f69)
                                    yield 63, subst2
                            subjects309.appendleft(tmp326)
                        if len(subjects309) >= 1 and subjects309[0] == Integer(6):
                            tmp327 = subjects309.popleft()
                            # State 6248
                            if len(subjects309) == 0:
                                pass
                                # State 6249
                                if len(subjects) == 0:
                                    pass
                                    # 60: b*x**6 /; (cons_f2) and (cons_f3) and (cons_f69)
                                    yield 60, subst2
                            subjects309.appendleft(tmp327)
                        if len(subjects309) >= 1 and subjects309[0] == Integer(8):
                            tmp328 = subjects309.popleft()
                            # State 6258
                            if len(subjects309) == 0:
                                pass
                                # State 6259
                                if len(subjects) == 0:
                                    pass
                                    # 61: b*x**8 /; (cons_f2) and (cons_f3) and (cons_f69)
                                    yield 61, subst2
                            subjects309.appendleft(tmp328)
                        if len(subjects309) >= 1 and isinstance(subjects309[0], Add):
                            tmp329 = subjects309.popleft()
                            associative1 = tmp329
                            associative_type1 = type(tmp329)
                            subjects330 = deque(tmp329._args)
                            matcher = CommutativeMatcher101185.get()
                            tmp331 = subjects330
                            subjects330 = []
                            for s in tmp331:
                                matcher.add_subject(s)
                            for pattern_index, subst3 in matcher.match(tmp331, subst2):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 101191
                                    if len(subjects309) == 0:
                                        pass
                                        # State 101192
                                        if len(subjects) == 0:
                                            pass
                                            # 394: b*F**(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1666)
                                            yield 394, subst3
                            subjects309.appendleft(tmp329)
                    subjects309.appendleft(tmp310)
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i3.1.2.0', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 10081
                    if len(subjects309) >= 1 and isinstance(subjects309[0], Pow):
                        tmp333 = subjects309.popleft()
                        subjects334 = deque(tmp333._args)
                        # State 10082
                        if len(subjects334) >= 1:
                            tmp335 = subjects334.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i3.1.2.1', tmp335)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 10083
                                if len(subjects334) >= 1:
                                    tmp337 = subjects334.popleft()
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i3.1.2.2', tmp337)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 10084
                                        if len(subjects334) == 0:
                                            pass
                                            # State 10085
                                            if len(subjects309) >= 1:
                                                tmp339 = subjects309.popleft()
                                                subst5 = Substitution(subst4)
                                                try:
                                                    subst5.try_add_variable('i3.1.2', tmp339)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 10086
                                                    if len(subjects309) == 0:
                                                        pass
                                                        # State 10087
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 141: b*(c*x**n)**q /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f52) and (cons_f4) and (cons_f5) and (cons_f800)
                                                            yield 141, subst5
                                                subjects309.appendleft(tmp339)
                                    subjects334.appendleft(tmp337)
                                if len(subjects334) >= 1 and subjects334[0] == Integer(-1):
                                    tmp341 = subjects334.popleft()
                                    # State 10618
                                    if len(subjects334) == 0:
                                        pass
                                        # State 10619
                                        if len(subjects309) >= 1:
                                            tmp342 = subjects309.popleft()
                                            subst4 = Substitution(subst3)
                                            try:
                                                subst4.try_add_variable('i3.1.2', tmp342)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 10620
                                                if len(subjects309) == 0:
                                                    pass
                                                    # State 10621
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 145: b*(c/x)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f5) and (cons_f809) and (cons_f810)
                                                        yield 145, subst4
                                                        # 142: b*(c/x)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f808)
                                                        yield 142, subst4
                                                        # 143: b*(c/x)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f5) and (cons_f48)
                                                        yield 143, subst4
                                            subjects309.appendleft(tmp342)
                                    subjects334.appendleft(tmp341)
                            subjects334.appendleft(tmp335)
                        if len(subjects334) >= 1 and isinstance(subjects334[0], tan):
                            tmp344 = subjects334.popleft()
                            subjects345 = deque(tmp344._args)
                            # State 82247
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i3.1.2.3.0', S(0))
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 82248
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i3.1.2.3.1.0_1', S(1))
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 82249
                                    if len(subjects345) >= 1:
                                        tmp348 = subjects345.popleft()
                                        subst5 = Substitution(subst4)
                                        try:
                                            subst5.try_add_variable('i3.1.2.3.1.0', tmp348)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 82250
                                            if len(subjects345) == 0:
                                                pass
                                                # State 82251
                                                if len(subjects334) >= 1 and subjects334[0] == Integer(-1):
                                                    tmp350 = subjects334.popleft()
                                                    # State 82252
                                                    if len(subjects334) == 0:
                                                        pass
                                                        # State 82253
                                                        if len(subjects309) >= 1:
                                                            tmp351 = subjects309.popleft()
                                                            subst6 = Substitution(subst5)
                                                            try:
                                                                subst6.try_add_variable('i3.1.2', tmp351)
                                                            except ValueError:
                                                                pass
                                                            else:
                                                                pass
                                                                # State 82254
                                                                if len(subjects309) == 0:
                                                                    pass
                                                                    # State 82255
                                                                    if len(subjects) == 0:
                                                                        pass
                                                                        # 341: b*(e/tan(c + x*d))**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f5) and (cons_f1572)
                                                                        yield 341, subst6
                                                            subjects309.appendleft(tmp351)
                                                    subjects334.appendleft(tmp350)
                                        subjects345.appendleft(tmp348)
                                if len(subjects345) >= 1 and isinstance(subjects345[0], Mul):
                                    tmp353 = subjects345.popleft()
                                    associative1 = tmp353
                                    associative_type1 = type(tmp353)
                                    subjects354 = deque(tmp353._args)
                                    matcher = CommutativeMatcher82257.get()
                                    tmp355 = subjects354
                                    subjects354 = []
                                    for s in tmp355:
                                        matcher.add_subject(s)
                                    for pattern_index, subst4 in matcher.match(tmp355, subst3):
                                        pass
                                        if pattern_index == 0:
                                            pass
                                            # State 82258
                                            if len(subjects345) == 0:
                                                pass
                                                # State 82259
                                                if len(subjects334) >= 1 and subjects334[0] == Integer(-1):
                                                    tmp356 = subjects334.popleft()
                                                    # State 82260
                                                    if len(subjects334) == 0:
                                                        pass
                                                        # State 82261
                                                        if len(subjects309) >= 1:
                                                            tmp357 = subjects309.popleft()
                                                            subst5 = Substitution(subst4)
                                                            try:
                                                                subst5.try_add_variable('i3.1.2', tmp357)
                                                            except ValueError:
                                                                pass
                                                            else:
                                                                pass
                                                                # State 82262
                                                                if len(subjects309) == 0:
                                                                    pass
                                                                    # State 82263
                                                                    if len(subjects) == 0:
                                                                        pass
                                                                        # 341: b*(e/tan(c + x*d))**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f5) and (cons_f1572)
                                                                        yield 341, subst5
                                                            subjects309.appendleft(tmp357)
                                                    subjects334.appendleft(tmp356)
                                    subjects345.appendleft(tmp353)
                            if len(subjects345) >= 1 and isinstance(subjects345[0], Add):
                                tmp359 = subjects345.popleft()
                                associative1 = tmp359
                                associative_type1 = type(tmp359)
                                subjects360 = deque(tmp359._args)
                                matcher = CommutativeMatcher82265.get()
                                tmp361 = subjects360
                                subjects360 = []
                                for s in tmp361:
                                    matcher.add_subject(s)
                                for pattern_index, subst3 in matcher.match(tmp361, subst2):
                                    pass
                                    if pattern_index == 0:
                                        pass
                                        # State 82271
                                        if len(subjects345) == 0:
                                            pass
                                            # State 82272
                                            if len(subjects334) >= 1 and subjects334[0] == Integer(-1):
                                                tmp362 = subjects334.popleft()
                                                # State 82273
                                                if len(subjects334) == 0:
                                                    pass
                                                    # State 82274
                                                    if len(subjects309) >= 1:
                                                        tmp363 = subjects309.popleft()
                                                        subst4 = Substitution(subst3)
                                                        try:
                                                            subst4.try_add_variable('i3.1.2', tmp363)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            # State 82275
                                                            if len(subjects309) == 0:
                                                                pass
                                                                # State 82276
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 341: b*(e/tan(c + x*d))**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f5) and (cons_f1572)
                                                                    yield 341, subst4
                                                        subjects309.appendleft(tmp363)
                                                subjects334.appendleft(tmp362)
                                subjects345.appendleft(tmp359)
                            subjects334.appendleft(tmp344)
                        subjects309.appendleft(tmp333)
                    if len(subjects309) >= 1 and isinstance(subjects309[0], tan):
                        tmp365 = subjects309.popleft()
                        subjects366 = deque(tmp365._args)
                        # State 82151
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i3.1.2.2.0', S(0))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 82152
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i3.1.2.2.1.0_1', S(1))
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 82153
                                if len(subjects366) >= 1:
                                    tmp369 = subjects366.popleft()
                                    subst5 = Substitution(subst4)
                                    try:
                                        subst5.try_add_variable('i3.1.2.2.1.0', tmp369)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 82154
                                        if len(subjects366) == 0:
                                            pass
                                            # State 82155
                                            if len(subjects309) >= 1:
                                                tmp371 = subjects309.popleft()
                                                subst6 = Substitution(subst5)
                                                try:
                                                    subst6.try_add_variable('i3.1.2', tmp371)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 82156
                                                    if len(subjects309) == 0:
                                                        pass
                                                        # State 82157
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 340: b*(e*tan(c + x*d))**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f5) and (cons_f1572)
                                                            yield 340, subst6
                                                subjects309.appendleft(tmp371)
                                    subjects366.appendleft(tmp369)
                            if len(subjects366) >= 1 and isinstance(subjects366[0], Mul):
                                tmp373 = subjects366.popleft()
                                associative1 = tmp373
                                associative_type1 = type(tmp373)
                                subjects374 = deque(tmp373._args)
                                matcher = CommutativeMatcher82159.get()
                                tmp375 = subjects374
                                subjects374 = []
                                for s in tmp375:
                                    matcher.add_subject(s)
                                for pattern_index, subst4 in matcher.match(tmp375, subst3):
                                    pass
                                    if pattern_index == 0:
                                        pass
                                        # State 82160
                                        if len(subjects366) == 0:
                                            pass
                                            # State 82161
                                            if len(subjects309) >= 1:
                                                tmp376 = subjects309.popleft()
                                                subst5 = Substitution(subst4)
                                                try:
                                                    subst5.try_add_variable('i3.1.2', tmp376)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 82162
                                                    if len(subjects309) == 0:
                                                        pass
                                                        # State 82163
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 340: b*(e*tan(c + x*d))**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f5) and (cons_f1572)
                                                            yield 340, subst5
                                                subjects309.appendleft(tmp376)
                                subjects366.appendleft(tmp373)
                        if len(subjects366) >= 1 and isinstance(subjects366[0], Add):
                            tmp378 = subjects366.popleft()
                            associative1 = tmp378
                            associative_type1 = type(tmp378)
                            subjects379 = deque(tmp378._args)
                            matcher = CommutativeMatcher82165.get()
                            tmp380 = subjects379
                            subjects379 = []
                            for s in tmp380:
                                matcher.add_subject(s)
                            for pattern_index, subst3 in matcher.match(tmp380, subst2):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 82171
                                    if len(subjects366) == 0:
                                        pass
                                        # State 82172
                                        if len(subjects309) >= 1:
                                            tmp381 = subjects309.popleft()
                                            subst4 = Substitution(subst3)
                                            try:
                                                subst4.try_add_variable('i3.1.2', tmp381)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 82173
                                                if len(subjects309) == 0:
                                                    pass
                                                    # State 82174
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 340: b*(e*tan(c + x*d))**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f5) and (cons_f1572)
                                                        yield 340, subst4
                                            subjects309.appendleft(tmp381)
                            subjects366.appendleft(tmp378)
                        subjects309.appendleft(tmp365)
                if len(subjects309) >= 1 and isinstance(subjects309[0], Mul):
                    tmp383 = subjects309.popleft()
                    associative1 = tmp383
                    associative_type1 = type(tmp383)
                    subjects384 = deque(tmp383._args)
                    matcher = CommutativeMatcher10089.get()
                    tmp385 = subjects384
                    subjects384 = []
                    for s in tmp385:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp385, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 10094
                            if len(subjects309) >= 1:
                                tmp386 = []
                                tmp386.append(subjects309.popleft())
                                while True:
                                    if len(tmp386) > 1:
                                        tmp387 = create_operation_expression(associative1, tmp386)
                                    elif len(tmp386) == 1:
                                        tmp387 = tmp386[0]
                                    else:
                                        assert False, "Unreachable"
                                    subst3 = Substitution(subst2)
                                    try:
                                        subst3.try_add_variable('i3.1.2', tmp387)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 10095
                                        if len(subjects309) == 0:
                                            pass
                                            # State 10096
                                            if len(subjects) == 0:
                                                pass
                                                # 141: b*(c*x**n)**q /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f52) and (cons_f4) and (cons_f5) and (cons_f800)
                                                yield 141, subst3
                                    if len(subjects309) == 0:
                                        break
                                    tmp386.append(subjects309.popleft())
                                subjects309.extendleft(reversed(tmp386))
                        if pattern_index == 1:
                            pass
                            # State 10624
                            if len(subjects309) >= 1:
                                tmp389 = []
                                tmp389.append(subjects309.popleft())
                                while True:
                                    if len(tmp389) > 1:
                                        tmp390 = create_operation_expression(associative1, tmp389)
                                    elif len(tmp389) == 1:
                                        tmp390 = tmp389[0]
                                    else:
                                        assert False, "Unreachable"
                                    subst3 = Substitution(subst2)
                                    try:
                                        subst3.try_add_variable('i3.1.2', tmp390)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 10625
                                        if len(subjects309) == 0:
                                            pass
                                            # State 10626
                                            if len(subjects) == 0:
                                                pass
                                                # 145: b*(c/x)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f5) and (cons_f809) and (cons_f810)
                                                yield 145, subst3
                                                # 142: b*(c/x)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f808)
                                                yield 142, subst3
                                                # 143: b*(c/x)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f5) and (cons_f48)
                                                yield 143, subst3
                                    if len(subjects309) == 0:
                                        break
                                    tmp389.append(subjects309.popleft())
                                subjects309.extendleft(reversed(tmp389))
                        if pattern_index == 2:
                            pass
                            # State 82193
                            if len(subjects309) >= 1:
                                tmp392 = []
                                tmp392.append(subjects309.popleft())
                                while True:
                                    if len(tmp392) > 1:
                                        tmp393 = create_operation_expression(associative1, tmp392)
                                    elif len(tmp392) == 1:
                                        tmp393 = tmp392[0]
                                    else:
                                        assert False, "Unreachable"
                                    subst3 = Substitution(subst2)
                                    try:
                                        subst3.try_add_variable('i3.1.2', tmp393)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 82194
                                        if len(subjects309) == 0:
                                            pass
                                            # State 82195
                                            if len(subjects) == 0:
                                                pass
                                                # 340: b*(e*tan(c + x*d))**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f5) and (cons_f1572)
                                                yield 340, subst3
                                    if len(subjects309) == 0:
                                        break
                                    tmp392.append(subjects309.popleft())
                                subjects309.extendleft(reversed(tmp392))
                        if pattern_index == 3:
                            pass
                            # State 82301
                            if len(subjects309) >= 1:
                                tmp395 = []
                                tmp395.append(subjects309.popleft())
                                while True:
                                    if len(tmp395) > 1:
                                        tmp396 = create_operation_expression(associative1, tmp395)
                                    elif len(tmp395) == 1:
                                        tmp396 = tmp395[0]
                                    else:
                                        assert False, "Unreachable"
                                    subst3 = Substitution(subst2)
                                    try:
                                        subst3.try_add_variable('i3.1.2', tmp396)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 82302
                                        if len(subjects309) == 0:
                                            pass
                                            # State 82303
                                            if len(subjects) == 0:
                                                pass
                                                # 341: b*(e/tan(c + x*d))**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f5) and (cons_f1572)
                                                yield 341, subst3
                                    if len(subjects309) == 0:
                                        break
                                    tmp395.append(subjects309.popleft())
                                subjects309.extendleft(reversed(tmp395))
                    subjects309.appendleft(tmp383)
                if len(subjects309) >= 1 and isinstance(subjects309[0], Add):
                    tmp398 = subjects309.popleft()
                    associative1 = tmp398
                    associative_type1 = type(tmp398)
                    subjects399 = deque(tmp398._args)
                    matcher = CommutativeMatcher13455.get()
                    tmp400 = subjects399
                    subjects399 = []
                    for s in tmp400:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp400, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 13505
                            if len(subjects309) >= 1:
                                tmp401 = []
                                tmp401.append(subjects309.popleft())
                                while True:
                                    if len(tmp401) > 1:
                                        tmp402 = create_operation_expression(associative1, tmp401)
                                    elif len(tmp401) == 1:
                                        tmp402 = tmp401[0]
                                    else:
                                        assert False, "Unreachable"
                                    subst3 = Substitution(subst2)
                                    try:
                                        subst3.try_add_variable('i3.1.2', tmp402)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 13506
                                        if len(subjects309) == 0:
                                            pass
                                            # State 13507
                                            if len(subjects) == 0:
                                                pass
                                                # 227: h*(d + e*x + f*sqrt(a + b*x + c*x**2))**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f210) and (cons_f211) and (cons_f4) and (cons_f1057)
                                                yield 227, subst3
                                    if len(subjects309) == 0:
                                        break
                                    tmp401.append(subjects309.popleft())
                                subjects309.extendleft(reversed(tmp401))
                        if pattern_index == 1:
                            pass
                            # State 13653
                            if len(subjects309) >= 1:
                                tmp404 = []
                                tmp404.append(subjects309.popleft())
                                while True:
                                    if len(tmp404) > 1:
                                        tmp405 = create_operation_expression(associative1, tmp404)
                                    elif len(tmp404) == 1:
                                        tmp405 = tmp404[0]
                                    else:
                                        assert False, "Unreachable"
                                    subst3 = Substitution(subst2)
                                    try:
                                        subst3.try_add_variable('i3.1.2', tmp405)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 13654
                                        if len(subjects309) == 0:
                                            pass
                                            # State 13655
                                            if len(subjects) == 0:
                                                pass
                                                # 228: h*(d + e*x + f*sqrt(a + c*x**2))**n /; (cons_f2) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f210) and (cons_f211) and (cons_f4) and (cons_f1057)
                                                yield 228, subst3
                                    if len(subjects309) == 0:
                                        break
                                    tmp404.append(subjects309.popleft())
                                subjects309.extendleft(reversed(tmp404))
                        if pattern_index == 2:
                            pass
                            # State 13757
                            if len(subjects309) >= 1:
                                tmp407 = []
                                tmp407.append(subjects309.popleft())
                                while True:
                                    if len(tmp407) > 1:
                                        tmp408 = create_operation_expression(associative1, tmp407)
                                    elif len(tmp407) == 1:
                                        tmp408 = tmp407[0]
                                    else:
                                        assert False, "Unreachable"
                                    subst3 = Substitution(subst2)
                                    try:
                                        subst3.try_add_variable('i3.1.2', tmp408)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 13758
                                        if len(subjects309) == 0:
                                            pass
                                            # State 13759
                                            if len(subjects) == 0:
                                                pass
                                                # 229: h*(u + f*sqrt(v))**n /; (cons_f127) and (cons_f211) and (cons_f4) and (cons_f70) and (cons_f820) and (cons_f821) and (cons_f1058)
                                                yield 229, subst3
                                    if len(subjects309) == 0:
                                        break
                                    tmp407.append(subjects309.popleft())
                                subjects309.extendleft(reversed(tmp407))
                        if pattern_index == 3:
                            pass
                            # State 14122
                            if len(subjects309) >= 1 and subjects309[0] == Rational(1, 2):
                                tmp410 = subjects309.popleft()
                                # State 14123
                                if len(subjects309) == 0:
                                    pass
                                    # State 14124
                                    if len(subjects) == 0:
                                        pass
                                        # 230: b*sqrt(c + d*x**2) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1068)
                                        yield 230, subst2
                                subjects309.appendleft(tmp410)
                    subjects309.appendleft(tmp398)
                if len(subjects309) >= 1 and isinstance(subjects309[0], cos):
                    tmp411 = subjects309.popleft()
                    subjects412 = deque(tmp411._args)
                    # State 67089
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i3.1.3.0', S(0))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 67090
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i3.1.3.1.0_1', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 67091
                            if len(subjects412) >= 1:
                                tmp415 = subjects412.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i3.1.3.1.0', tmp415)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 67092
                                    if len(subjects412) == 0:
                                        pass
                                        # State 67093
                                        if len(subjects309) >= 1 and subjects309[0] == Integer(-1):
                                            tmp417 = subjects309.popleft()
                                            # State 67094
                                            if len(subjects309) == 0:
                                                pass
                                                # State 67095
                                                if len(subjects) == 0:
                                                    pass
                                                    # 358: b/cos(d + x*e) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1266)
                                                    yield 358, subst4
                                                    # 360: b/cos(d + x*e) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1267)
                                                    yield 360, subst4
                                                    # 362: b/cos(d + x*e) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f1267)
                                                    yield 362, subst4
                                                    # 364: b/cos(d + x*e) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1269)
                                                    yield 364, subst4
                                                    # 366: b/cos(d + x*e) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f1269)
                                                    yield 366, subst4
                                                    # 284: b/cos(d + x*e) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f1045)
                                                    yield 284, subst4
                                            subjects309.appendleft(tmp417)
                                        if len(subjects309) >= 1 and subjects309[0] == Integer(2):
                                            tmp418 = subjects309.popleft()
                                            # State 67771
                                            if len(subjects309) == 0:
                                                pass
                                                # State 67772
                                                if len(subjects) == 0:
                                                    pass
                                                    # 289: b*cos(d + x*e)**2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1456)
                                                    yield 289, subst4
                                                    # 291: b*cos(d + x*e)**2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f5) and (cons_f1456)
                                                    yield 291, subst4
                                                    # 293: b*cos(d + x*e)**2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29)
                                                    yield 293, subst4
                                                    # 295: b*cos(d + x*e)**2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f5) and (cons_f1480)
                                                    yield 295, subst4
                                            subjects309.appendleft(tmp418)
                                        if len(subjects309) >= 1:
                                            tmp419 = subjects309.popleft()
                                            subst5 = Substitution(subst4)
                                            try:
                                                subst5.try_add_variable('i3.1.3', tmp419)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 67837
                                                if len(subjects309) == 0:
                                                    pass
                                                    # State 67838
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 297: b*cos(d + x*e)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f87)
                                                        yield 297, subst5
                                                        # 299: b*cos(d + x*e)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1481)
                                                        yield 299, subst5
                                            subjects309.appendleft(tmp419)
                                        subst5 = Substitution(subst4)
                                        try:
                                            subst5.try_add_variable('i3.1.3', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 69190
                                            if len(subjects309) == 0:
                                                pass
                                                # State 69191
                                                if len(subjects) == 0:
                                                    pass
                                                    # 302: b*cos(d + x*e)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                                                    yield 302, subst5
                                                    # 306: b*cos(d + x*e)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f5) and (cons_f48) and (cons_f47)
                                                    yield 306, subst5
                                                    # 310: b*cos(d + x*e)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f228)
                                                    yield 310, subst5
                                        if len(subjects309) >= 1:
                                            tmp422 = subjects309.popleft()
                                            subst5 = Substitution(subst4)
                                            try:
                                                subst5.try_add_variable('i3.1.3', tmp422)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 69190
                                                if len(subjects309) == 0:
                                                    pass
                                                    # State 69191
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 302: b*cos(d + x*e)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                                                        yield 302, subst5
                                                        # 306: b*cos(d + x*e)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f5) and (cons_f48) and (cons_f47)
                                                        yield 306, subst5
                                                        # 310: b*cos(d + x*e)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f228)
                                                        yield 310, subst5
                                            subjects309.appendleft(tmp422)
                                        if len(subjects309) >= 1 and subjects309[0] == Integer(-2):
                                            tmp424 = subjects309.popleft()
                                            # State 94779
                                            if len(subjects309) == 0:
                                                pass
                                                # State 94780
                                                if len(subjects) == 0:
                                                    pass
                                                    # 368: b/cos(d + x*e)**2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f5) and (cons_f1456)
                                                    yield 368, subst4
                                                    # 370: b/cos(d + x*e)**2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1480)
                                                    yield 370, subst4
                                                    # 372: b/cos(d + x*e)**2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f5) and (cons_f1480)
                                                    yield 372, subst4
                                            subjects309.appendleft(tmp424)
                                subjects412.appendleft(tmp415)
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i3.1.3.1.0', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 97660
                            if len(subjects412) >= 1 and isinstance(subjects412[0], Pow):
                                tmp426 = subjects412.popleft()
                                subjects427 = deque(tmp426._args)
                                # State 97661
                                if len(subjects427) >= 1:
                                    tmp428 = subjects427.popleft()
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i3.1.3.1.1', tmp428)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 97662
                                        if len(subjects427) >= 1:
                                            tmp430 = subjects427.popleft()
                                            subst5 = Substitution(subst4)
                                            try:
                                                subst5.try_add_variable('i3.1.3.1.2', tmp430)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 97663
                                                if len(subjects427) == 0:
                                                    pass
                                                    # State 97664
                                                    if len(subjects412) == 0:
                                                        pass
                                                        # State 97665
                                                        if len(subjects309) >= 1 and subjects309[0] == Integer(-1):
                                                            tmp432 = subjects309.popleft()
                                                            # State 97666
                                                            if len(subjects309) == 0:
                                                                pass
                                                                # State 97667
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 386: b/cos(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f5) and (cons_f1575)
                                                                    yield 386, subst5
                                                                    # 388: b/cos(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f5) and (cons_f1497)
                                                                    yield 388, subst5
                                                                    # 390: b/cos(c + d*x**n) /; (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f70) and (cons_f71)
                                                                    yield 390, subst5
                                                            subjects309.appendleft(tmp432)
                                            subjects427.appendleft(tmp430)
                                    subjects427.appendleft(tmp428)
                                subjects412.appendleft(tmp426)
                        if len(subjects412) >= 1 and isinstance(subjects412[0], Mul):
                            tmp433 = subjects412.popleft()
                            associative1 = tmp433
                            associative_type1 = type(tmp433)
                            subjects434 = deque(tmp433._args)
                            matcher = CommutativeMatcher67097.get()
                            tmp435 = subjects434
                            subjects434 = []
                            for s in tmp435:
                                matcher.add_subject(s)
                            for pattern_index, subst3 in matcher.match(tmp435, subst2):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 67098
                                    if len(subjects412) == 0:
                                        pass
                                        # State 67099
                                        if len(subjects309) >= 1 and subjects309[0] == Integer(-1):
                                            tmp436 = subjects309.popleft()
                                            # State 67100
                                            if len(subjects309) == 0:
                                                pass
                                                # State 67101
                                                if len(subjects) == 0:
                                                    pass
                                                    # 358: b/cos(d + x*e) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1266)
                                                    yield 358, subst3
                                                    # 360: b/cos(d + x*e) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1267)
                                                    yield 360, subst3
                                                    # 362: b/cos(d + x*e) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f1267)
                                                    yield 362, subst3
                                                    # 364: b/cos(d + x*e) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1269)
                                                    yield 364, subst3
                                                    # 366: b/cos(d + x*e) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f1269)
                                                    yield 366, subst3
                                                    # 284: b/cos(d + x*e) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f1045)
                                                    yield 284, subst3
                                            subjects309.appendleft(tmp436)
                                        if len(subjects309) >= 1 and subjects309[0] == Integer(2):
                                            tmp437 = subjects309.popleft()
                                            # State 67773
                                            if len(subjects309) == 0:
                                                pass
                                                # State 67774
                                                if len(subjects) == 0:
                                                    pass
                                                    # 289: b*cos(d + x*e)**2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1456)
                                                    yield 289, subst3
                                                    # 291: b*cos(d + x*e)**2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f5) and (cons_f1456)
                                                    yield 291, subst3
                                                    # 293: b*cos(d + x*e)**2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29)
                                                    yield 293, subst3
                                                    # 295: b*cos(d + x*e)**2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f5) and (cons_f1480)
                                                    yield 295, subst3
                                            subjects309.appendleft(tmp437)
                                        if len(subjects309) >= 1:
                                            tmp438 = subjects309.popleft()
                                            subst4 = Substitution(subst3)
                                            try:
                                                subst4.try_add_variable('i3.1.3', tmp438)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 67839
                                                if len(subjects309) == 0:
                                                    pass
                                                    # State 67840
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 297: b*cos(d + x*e)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f87)
                                                        yield 297, subst4
                                                        # 299: b*cos(d + x*e)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1481)
                                                        yield 299, subst4
                                            subjects309.appendleft(tmp438)
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i3.1.3', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 69192
                                            if len(subjects309) == 0:
                                                pass
                                                # State 69193
                                                if len(subjects) == 0:
                                                    pass
                                                    # 302: b*cos(d + x*e)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                                                    yield 302, subst4
                                                    # 306: b*cos(d + x*e)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f5) and (cons_f48) and (cons_f47)
                                                    yield 306, subst4
                                                    # 310: b*cos(d + x*e)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f228)
                                                    yield 310, subst4
                                        if len(subjects309) >= 1:
                                            tmp441 = subjects309.popleft()
                                            subst4 = Substitution(subst3)
                                            try:
                                                subst4.try_add_variable('i3.1.3', tmp441)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 69192
                                                if len(subjects309) == 0:
                                                    pass
                                                    # State 69193
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 302: b*cos(d + x*e)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                                                        yield 302, subst4
                                                        # 306: b*cos(d + x*e)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f5) and (cons_f48) and (cons_f47)
                                                        yield 306, subst4
                                                        # 310: b*cos(d + x*e)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f228)
                                                        yield 310, subst4
                                            subjects309.appendleft(tmp441)
                                        if len(subjects309) >= 1 and subjects309[0] == Integer(-2):
                                            tmp443 = subjects309.popleft()
                                            # State 94781
                                            if len(subjects309) == 0:
                                                pass
                                                # State 94782
                                                if len(subjects) == 0:
                                                    pass
                                                    # 368: b/cos(d + x*e)**2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f5) and (cons_f1456)
                                                    yield 368, subst3
                                                    # 370: b/cos(d + x*e)**2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1480)
                                                    yield 370, subst3
                                                    # 372: b/cos(d + x*e)**2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f5) and (cons_f1480)
                                                    yield 372, subst3
                                            subjects309.appendleft(tmp443)
                                if pattern_index == 1:
                                    pass
                                    # State 97672
                                    if len(subjects412) == 0:
                                        pass
                                        # State 97673
                                        if len(subjects309) >= 1 and subjects309[0] == Integer(-1):
                                            tmp444 = subjects309.popleft()
                                            # State 97674
                                            if len(subjects309) == 0:
                                                pass
                                                # State 97675
                                                if len(subjects) == 0:
                                                    pass
                                                    # 386: b/cos(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f5) and (cons_f1575)
                                                    yield 386, subst3
                                                    # 388: b/cos(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f5) and (cons_f1497)
                                                    yield 388, subst3
                                                    # 390: b/cos(c + d*x**n) /; (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f70) and (cons_f71)
                                                    yield 390, subst3
                                            subjects309.appendleft(tmp444)
                            subjects412.appendleft(tmp433)
                    if len(subjects412) >= 1:
                        tmp445 = subjects412.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i3.1.2', tmp445)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 98260
                            if len(subjects412) == 0:
                                pass
                                # State 98261
                                if len(subjects309) >= 1 and subjects309[0] == Integer(-1):
                                    tmp447 = subjects309.popleft()
                                    # State 98262
                                    if len(subjects309) == 0:
                                        pass
                                        # State 98263
                                        if len(subjects) == 0:
                                            pass
                                            # 392: b/cos(u) /; (cons_f3) and (cons_f825) and (cons_f826)
                                            yield 392, subst2
                                    subjects309.appendleft(tmp447)
                        subjects412.appendleft(tmp445)
                    if len(subjects412) >= 1 and isinstance(subjects412[0], Add):
                        tmp448 = subjects412.popleft()
                        associative1 = tmp448
                        associative_type1 = type(tmp448)
                        subjects449 = deque(tmp448._args)
                        matcher = CommutativeMatcher67103.get()
                        tmp450 = subjects449
                        subjects449 = []
                        for s in tmp450:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp450, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 67109
                                if len(subjects412) == 0:
                                    pass
                                    # State 67110
                                    if len(subjects309) >= 1 and subjects309[0] == Integer(-1):
                                        tmp451 = subjects309.popleft()
                                        # State 67111
                                        if len(subjects309) == 0:
                                            pass
                                            # State 67112
                                            if len(subjects) == 0:
                                                pass
                                                # 358: b/cos(d + x*e) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1266)
                                                yield 358, subst2
                                                # 360: b/cos(d + x*e) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1267)
                                                yield 360, subst2
                                                # 362: b/cos(d + x*e) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f1267)
                                                yield 362, subst2
                                                # 364: b/cos(d + x*e) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1269)
                                                yield 364, subst2
                                                # 366: b/cos(d + x*e) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f1269)
                                                yield 366, subst2
                                                # 284: b/cos(d + x*e) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f1045)
                                                yield 284, subst2
                                        subjects309.appendleft(tmp451)
                                    if len(subjects309) >= 1 and subjects309[0] == Integer(2):
                                        tmp452 = subjects309.popleft()
                                        # State 67775
                                        if len(subjects309) == 0:
                                            pass
                                            # State 67776
                                            if len(subjects) == 0:
                                                pass
                                                # 289: b*cos(d + x*e)**2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1456)
                                                yield 289, subst2
                                                # 291: b*cos(d + x*e)**2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f5) and (cons_f1456)
                                                yield 291, subst2
                                                # 293: b*cos(d + x*e)**2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29)
                                                yield 293, subst2
                                                # 295: b*cos(d + x*e)**2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f5) and (cons_f1480)
                                                yield 295, subst2
                                        subjects309.appendleft(tmp452)
                                    if len(subjects309) >= 1:
                                        tmp453 = subjects309.popleft()
                                        subst3 = Substitution(subst2)
                                        try:
                                            subst3.try_add_variable('i3.1.3', tmp453)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 67841
                                            if len(subjects309) == 0:
                                                pass
                                                # State 67842
                                                if len(subjects) == 0:
                                                    pass
                                                    # 297: b*cos(d + x*e)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f87)
                                                    yield 297, subst3
                                                    # 299: b*cos(d + x*e)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1481)
                                                    yield 299, subst3
                                        subjects309.appendleft(tmp453)
                                    subst3 = Substitution(subst2)
                                    try:
                                        subst3.try_add_variable('i3.1.3', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 69194
                                        if len(subjects309) == 0:
                                            pass
                                            # State 69195
                                            if len(subjects) == 0:
                                                pass
                                                # 302: b*cos(d + x*e)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                                                yield 302, subst3
                                                # 306: b*cos(d + x*e)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f5) and (cons_f48) and (cons_f47)
                                                yield 306, subst3
                                                # 310: b*cos(d + x*e)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f228)
                                                yield 310, subst3
                                    if len(subjects309) >= 1:
                                        tmp456 = subjects309.popleft()
                                        subst3 = Substitution(subst2)
                                        try:
                                            subst3.try_add_variable('i3.1.3', tmp456)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 69194
                                            if len(subjects309) == 0:
                                                pass
                                                # State 69195
                                                if len(subjects) == 0:
                                                    pass
                                                    # 302: b*cos(d + x*e)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                                                    yield 302, subst3
                                                    # 306: b*cos(d + x*e)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f5) and (cons_f48) and (cons_f47)
                                                    yield 306, subst3
                                                    # 310: b*cos(d + x*e)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f228)
                                                    yield 310, subst3
                                        subjects309.appendleft(tmp456)
                                    if len(subjects309) >= 1 and subjects309[0] == Integer(-2):
                                        tmp458 = subjects309.popleft()
                                        # State 94783
                                        if len(subjects309) == 0:
                                            pass
                                            # State 94784
                                            if len(subjects) == 0:
                                                pass
                                                # 368: b/cos(d + x*e)**2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f5) and (cons_f1456)
                                                yield 368, subst2
                                                # 370: b/cos(d + x*e)**2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1480)
                                                yield 370, subst2
                                                # 372: b/cos(d + x*e)**2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f5) and (cons_f1480)
                                                yield 372, subst2
                                        subjects309.appendleft(tmp458)
                            if pattern_index == 1:
                                pass
                                # State 97686
                                if len(subjects412) == 0:
                                    pass
                                    # State 97687
                                    if len(subjects309) >= 1 and subjects309[0] == Integer(-1):
                                        tmp459 = subjects309.popleft()
                                        # State 97688
                                        if len(subjects309) == 0:
                                            pass
                                            # State 97689
                                            if len(subjects) == 0:
                                                pass
                                                # 386: b/cos(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f5) and (cons_f1575)
                                                yield 386, subst2
                                                # 388: b/cos(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f5) and (cons_f1497)
                                                yield 388, subst2
                                                # 390: b/cos(c + d*x**n) /; (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f70) and (cons_f71)
                                                yield 390, subst2
                                        subjects309.appendleft(tmp459)
                        subjects412.appendleft(tmp448)
                    subjects309.appendleft(tmp411)
                if len(subjects309) >= 1 and isinstance(subjects309[0], sin):
                    tmp460 = subjects309.popleft()
                    subjects461 = deque(tmp460._args)
                    # State 67180
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i3.1.3.0', S(0))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 67181
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i3.1.3.1.0_1', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 67182
                            if len(subjects461) >= 1:
                                tmp464 = subjects461.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i3.1.3.1.0', tmp464)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 67183
                                    if len(subjects461) == 0:
                                        pass
                                        # State 67184
                                        if len(subjects309) >= 1 and subjects309[0] == Integer(-1):
                                            tmp466 = subjects309.popleft()
                                            # State 67185
                                            if len(subjects309) == 0:
                                                pass
                                                # State 67186
                                                if len(subjects) == 0:
                                                    pass
                                                    # 359: b/sin(d + x*e) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1266)
                                                    yield 359, subst4
                                                    # 361: b/sin(d + x*e) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1267)
                                                    yield 361, subst4
                                                    # 363: b/sin(d + x*e) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f1267)
                                                    yield 363, subst4
                                                    # 365: b/sin(d + x*e) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1269)
                                                    yield 365, subst4
                                                    # 367: b/sin(d + x*e) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f1269)
                                                    yield 367, subst4
                                                    # 286: b/sin(d + x*e) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f1045)
                                                    yield 286, subst4
                                            subjects309.appendleft(tmp466)
                                        if len(subjects309) >= 1 and subjects309[0] == Integer(2):
                                            tmp467 = subjects309.popleft()
                                            # State 67753
                                            if len(subjects309) == 0:
                                                pass
                                                # State 67754
                                                if len(subjects) == 0:
                                                    pass
                                                    # 288: b*sin(d + x*e)**2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1456)
                                                    yield 288, subst4
                                                    # 290: b*sin(d + x*e)**2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f5) and (cons_f1456)
                                                    yield 290, subst4
                                                    # 292: b*sin(d + x*e)**2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29)
                                                    yield 292, subst4
                                                    # 294: b*sin(d + x*e)**2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f5) and (cons_f1480)
                                                    yield 294, subst4
                                            subjects309.appendleft(tmp467)
                                        if len(subjects309) >= 1:
                                            tmp468 = subjects309.popleft()
                                            subst5 = Substitution(subst4)
                                            try:
                                                subst5.try_add_variable('i3.1.3', tmp468)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 67819
                                                if len(subjects309) == 0:
                                                    pass
                                                    # State 67820
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 296: b*sin(d + x*e)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f87)
                                                        yield 296, subst5
                                                        # 298: b*sin(d + x*e)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1481)
                                                        yield 298, subst5
                                            subjects309.appendleft(tmp468)
                                        subst5 = Substitution(subst4)
                                        try:
                                            subst5.try_add_variable('i3.1.3', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 68911
                                            if len(subjects309) == 0:
                                                pass
                                                # State 68912
                                                if len(subjects) == 0:
                                                    pass
                                                    # 304: b*sin(d + x*e)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f5) and (cons_f48) and (cons_f47)
                                                    yield 304, subst5
                                                    # 300: b*sin(d + x*e)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                                                    yield 300, subst5
                                                    # 308: b*sin(d + x*e)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f228)
                                                    yield 308, subst5
                                        if len(subjects309) >= 1:
                                            tmp471 = subjects309.popleft()
                                            subst5 = Substitution(subst4)
                                            try:
                                                subst5.try_add_variable('i3.1.3', tmp471)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 68911
                                                if len(subjects309) == 0:
                                                    pass
                                                    # State 68912
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 304: b*sin(d + x*e)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f5) and (cons_f48) and (cons_f47)
                                                        yield 304, subst5
                                                        # 300: b*sin(d + x*e)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                                                        yield 300, subst5
                                                        # 308: b*sin(d + x*e)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f228)
                                                        yield 308, subst5
                                            subjects309.appendleft(tmp471)
                                        if len(subjects309) >= 1 and subjects309[0] == Integer(-2):
                                            tmp473 = subjects309.popleft()
                                            # State 94797
                                            if len(subjects309) == 0:
                                                pass
                                                # State 94798
                                                if len(subjects) == 0:
                                                    pass
                                                    # 369: b/sin(d + x*e)**2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f5) and (cons_f1456)
                                                    yield 369, subst4
                                                    # 371: b/sin(d + x*e)**2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1480)
                                                    yield 371, subst4
                                                    # 373: b/sin(d + x*e)**2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f5) and (cons_f1480)
                                                    yield 373, subst4
                                            subjects309.appendleft(tmp473)
                                subjects461.appendleft(tmp464)
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i3.1.3.1.0', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 97968
                            if len(subjects461) >= 1 and isinstance(subjects461[0], Pow):
                                tmp475 = subjects461.popleft()
                                subjects476 = deque(tmp475._args)
                                # State 97969
                                if len(subjects476) >= 1:
                                    tmp477 = subjects476.popleft()
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i3.1.3.1.1', tmp477)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 97970
                                        if len(subjects476) >= 1:
                                            tmp479 = subjects476.popleft()
                                            subst5 = Substitution(subst4)
                                            try:
                                                subst5.try_add_variable('i3.1.3.1.2', tmp479)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 97971
                                                if len(subjects476) == 0:
                                                    pass
                                                    # State 97972
                                                    if len(subjects461) == 0:
                                                        pass
                                                        # State 97973
                                                        if len(subjects309) >= 1 and subjects309[0] == Integer(-1):
                                                            tmp481 = subjects309.popleft()
                                                            # State 97974
                                                            if len(subjects309) == 0:
                                                                pass
                                                                # State 97975
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 387: b/sin(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f5) and (cons_f1575)
                                                                    yield 387, subst5
                                                                    # 389: b/sin(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f5) and (cons_f1497)
                                                                    yield 389, subst5
                                                                    # 391: b/sin(c + d*x**n) /; (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f70) and (cons_f71)
                                                                    yield 391, subst5
                                                            subjects309.appendleft(tmp481)
                                            subjects476.appendleft(tmp479)
                                    subjects476.appendleft(tmp477)
                                subjects461.appendleft(tmp475)
                        if len(subjects461) >= 1 and isinstance(subjects461[0], Mul):
                            tmp482 = subjects461.popleft()
                            associative1 = tmp482
                            associative_type1 = type(tmp482)
                            subjects483 = deque(tmp482._args)
                            matcher = CommutativeMatcher67188.get()
                            tmp484 = subjects483
                            subjects483 = []
                            for s in tmp484:
                                matcher.add_subject(s)
                            for pattern_index, subst3 in matcher.match(tmp484, subst2):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 67189
                                    if len(subjects461) == 0:
                                        pass
                                        # State 67190
                                        if len(subjects309) >= 1 and subjects309[0] == Integer(-1):
                                            tmp485 = subjects309.popleft()
                                            # State 67191
                                            if len(subjects309) == 0:
                                                pass
                                                # State 67192
                                                if len(subjects) == 0:
                                                    pass
                                                    # 359: b/sin(d + x*e) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1266)
                                                    yield 359, subst3
                                                    # 361: b/sin(d + x*e) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1267)
                                                    yield 361, subst3
                                                    # 363: b/sin(d + x*e) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f1267)
                                                    yield 363, subst3
                                                    # 365: b/sin(d + x*e) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1269)
                                                    yield 365, subst3
                                                    # 367: b/sin(d + x*e) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f1269)
                                                    yield 367, subst3
                                                    # 286: b/sin(d + x*e) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f1045)
                                                    yield 286, subst3
                                            subjects309.appendleft(tmp485)
                                        if len(subjects309) >= 1 and subjects309[0] == Integer(2):
                                            tmp486 = subjects309.popleft()
                                            # State 67755
                                            if len(subjects309) == 0:
                                                pass
                                                # State 67756
                                                if len(subjects) == 0:
                                                    pass
                                                    # 288: b*sin(d + x*e)**2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1456)
                                                    yield 288, subst3
                                                    # 290: b*sin(d + x*e)**2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f5) and (cons_f1456)
                                                    yield 290, subst3
                                                    # 292: b*sin(d + x*e)**2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29)
                                                    yield 292, subst3
                                                    # 294: b*sin(d + x*e)**2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f5) and (cons_f1480)
                                                    yield 294, subst3
                                            subjects309.appendleft(tmp486)
                                        if len(subjects309) >= 1:
                                            tmp487 = subjects309.popleft()
                                            subst4 = Substitution(subst3)
                                            try:
                                                subst4.try_add_variable('i3.1.3', tmp487)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 67821
                                                if len(subjects309) == 0:
                                                    pass
                                                    # State 67822
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 296: b*sin(d + x*e)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f87)
                                                        yield 296, subst4
                                                        # 298: b*sin(d + x*e)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1481)
                                                        yield 298, subst4
                                            subjects309.appendleft(tmp487)
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i3.1.3', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 68913
                                            if len(subjects309) == 0:
                                                pass
                                                # State 68914
                                                if len(subjects) == 0:
                                                    pass
                                                    # 304: b*sin(d + x*e)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f5) and (cons_f48) and (cons_f47)
                                                    yield 304, subst4
                                                    # 300: b*sin(d + x*e)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                                                    yield 300, subst4
                                                    # 308: b*sin(d + x*e)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f228)
                                                    yield 308, subst4
                                        if len(subjects309) >= 1:
                                            tmp490 = subjects309.popleft()
                                            subst4 = Substitution(subst3)
                                            try:
                                                subst4.try_add_variable('i3.1.3', tmp490)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 68913
                                                if len(subjects309) == 0:
                                                    pass
                                                    # State 68914
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 304: b*sin(d + x*e)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f5) and (cons_f48) and (cons_f47)
                                                        yield 304, subst4
                                                        # 300: b*sin(d + x*e)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                                                        yield 300, subst4
                                                        # 308: b*sin(d + x*e)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f228)
                                                        yield 308, subst4
                                            subjects309.appendleft(tmp490)
                                        if len(subjects309) >= 1 and subjects309[0] == Integer(-2):
                                            tmp492 = subjects309.popleft()
                                            # State 94799
                                            if len(subjects309) == 0:
                                                pass
                                                # State 94800
                                                if len(subjects) == 0:
                                                    pass
                                                    # 369: b/sin(d + x*e)**2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f5) and (cons_f1456)
                                                    yield 369, subst3
                                                    # 371: b/sin(d + x*e)**2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1480)
                                                    yield 371, subst3
                                                    # 373: b/sin(d + x*e)**2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f5) and (cons_f1480)
                                                    yield 373, subst3
                                            subjects309.appendleft(tmp492)
                                if pattern_index == 1:
                                    pass
                                    # State 97980
                                    if len(subjects461) == 0:
                                        pass
                                        # State 97981
                                        if len(subjects309) >= 1 and subjects309[0] == Integer(-1):
                                            tmp493 = subjects309.popleft()
                                            # State 97982
                                            if len(subjects309) == 0:
                                                pass
                                                # State 97983
                                                if len(subjects) == 0:
                                                    pass
                                                    # 387: b/sin(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f5) and (cons_f1575)
                                                    yield 387, subst3
                                                    # 389: b/sin(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f5) and (cons_f1497)
                                                    yield 389, subst3
                                                    # 391: b/sin(c + d*x**n) /; (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f70) and (cons_f71)
                                                    yield 391, subst3
                                            subjects309.appendleft(tmp493)
                            subjects461.appendleft(tmp482)
                    if len(subjects461) >= 1:
                        tmp494 = subjects461.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i3.1.2', tmp494)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 98316
                            if len(subjects461) == 0:
                                pass
                                # State 98317
                                if len(subjects309) >= 1 and subjects309[0] == Integer(-1):
                                    tmp496 = subjects309.popleft()
                                    # State 98318
                                    if len(subjects309) == 0:
                                        pass
                                        # State 98319
                                        if len(subjects) == 0:
                                            pass
                                            # 393: b/sin(u) /; (cons_f3) and (cons_f825) and (cons_f826)
                                            yield 393, subst2
                                    subjects309.appendleft(tmp496)
                        subjects461.appendleft(tmp494)
                    if len(subjects461) >= 1 and isinstance(subjects461[0], Add):
                        tmp497 = subjects461.popleft()
                        associative1 = tmp497
                        associative_type1 = type(tmp497)
                        subjects498 = deque(tmp497._args)
                        matcher = CommutativeMatcher67194.get()
                        tmp499 = subjects498
                        subjects498 = []
                        for s in tmp499:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp499, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 67200
                                if len(subjects461) == 0:
                                    pass
                                    # State 67201
                                    if len(subjects309) >= 1 and subjects309[0] == Integer(-1):
                                        tmp500 = subjects309.popleft()
                                        # State 67202
                                        if len(subjects309) == 0:
                                            pass
                                            # State 67203
                                            if len(subjects) == 0:
                                                pass
                                                # 359: b/sin(d + x*e) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1266)
                                                yield 359, subst2
                                                # 361: b/sin(d + x*e) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1267)
                                                yield 361, subst2
                                                # 363: b/sin(d + x*e) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f1267)
                                                yield 363, subst2
                                                # 365: b/sin(d + x*e) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1269)
                                                yield 365, subst2
                                                # 367: b/sin(d + x*e) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f1269)
                                                yield 367, subst2
                                                # 286: b/sin(d + x*e) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f1045)
                                                yield 286, subst2
                                        subjects309.appendleft(tmp500)
                                    if len(subjects309) >= 1 and subjects309[0] == Integer(2):
                                        tmp501 = subjects309.popleft()
                                        # State 67757
                                        if len(subjects309) == 0:
                                            pass
                                            # State 67758
                                            if len(subjects) == 0:
                                                pass
                                                # 288: b*sin(d + x*e)**2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1456)
                                                yield 288, subst2
                                                # 290: b*sin(d + x*e)**2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f5) and (cons_f1456)
                                                yield 290, subst2
                                                # 292: b*sin(d + x*e)**2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29)
                                                yield 292, subst2
                                                # 294: b*sin(d + x*e)**2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f5) and (cons_f1480)
                                                yield 294, subst2
                                        subjects309.appendleft(tmp501)
                                    if len(subjects309) >= 1:
                                        tmp502 = subjects309.popleft()
                                        subst3 = Substitution(subst2)
                                        try:
                                            subst3.try_add_variable('i3.1.3', tmp502)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 67823
                                            if len(subjects309) == 0:
                                                pass
                                                # State 67824
                                                if len(subjects) == 0:
                                                    pass
                                                    # 296: b*sin(d + x*e)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f87)
                                                    yield 296, subst3
                                                    # 298: b*sin(d + x*e)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1481)
                                                    yield 298, subst3
                                        subjects309.appendleft(tmp502)
                                    subst3 = Substitution(subst2)
                                    try:
                                        subst3.try_add_variable('i3.1.3', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 68915
                                        if len(subjects309) == 0:
                                            pass
                                            # State 68916
                                            if len(subjects) == 0:
                                                pass
                                                # 304: b*sin(d + x*e)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f5) and (cons_f48) and (cons_f47)
                                                yield 304, subst3
                                                # 300: b*sin(d + x*e)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                                                yield 300, subst3
                                                # 308: b*sin(d + x*e)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f228)
                                                yield 308, subst3
                                    if len(subjects309) >= 1:
                                        tmp505 = subjects309.popleft()
                                        subst3 = Substitution(subst2)
                                        try:
                                            subst3.try_add_variable('i3.1.3', tmp505)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 68915
                                            if len(subjects309) == 0:
                                                pass
                                                # State 68916
                                                if len(subjects) == 0:
                                                    pass
                                                    # 304: b*sin(d + x*e)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f5) and (cons_f48) and (cons_f47)
                                                    yield 304, subst3
                                                    # 300: b*sin(d + x*e)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                                                    yield 300, subst3
                                                    # 308: b*sin(d + x*e)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f228)
                                                    yield 308, subst3
                                        subjects309.appendleft(tmp505)
                                    if len(subjects309) >= 1 and subjects309[0] == Integer(-2):
                                        tmp507 = subjects309.popleft()
                                        # State 94801
                                        if len(subjects309) == 0:
                                            pass
                                            # State 94802
                                            if len(subjects) == 0:
                                                pass
                                                # 369: b/sin(d + x*e)**2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f5) and (cons_f1456)
                                                yield 369, subst2
                                                # 371: b/sin(d + x*e)**2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1480)
                                                yield 371, subst2
                                                # 373: b/sin(d + x*e)**2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f5) and (cons_f1480)
                                                yield 373, subst2
                                        subjects309.appendleft(tmp507)
                            if pattern_index == 1:
                                pass
                                # State 97994
                                if len(subjects461) == 0:
                                    pass
                                    # State 97995
                                    if len(subjects309) >= 1 and subjects309[0] == Integer(-1):
                                        tmp508 = subjects309.popleft()
                                        # State 97996
                                        if len(subjects309) == 0:
                                            pass
                                            # State 97997
                                            if len(subjects) == 0:
                                                pass
                                                # 387: b/sin(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f5) and (cons_f1575)
                                                yield 387, subst2
                                                # 389: b/sin(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f5) and (cons_f1497)
                                                yield 389, subst2
                                                # 391: b/sin(c + d*x**n) /; (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f70) and (cons_f71)
                                                yield 391, subst2
                                        subjects309.appendleft(tmp508)
                        subjects461.appendleft(tmp497)
                    subjects309.appendleft(tmp460)
                if len(subjects309) >= 1 and isinstance(subjects309[0], tan):
                    tmp509 = subjects309.popleft()
                    subjects510 = deque(tmp509._args)
                    # State 77488
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i3.1.3.0', S(0))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 77489
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i3.1.3.1.0_1', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 77490
                            if len(subjects510) >= 1:
                                tmp513 = subjects510.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i3.1.3.1.0', tmp513)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 77491
                                    if len(subjects510) == 0:
                                        pass
                                        # State 77492
                                        if len(subjects309) >= 1 and subjects309[0] == Integer(-1):
                                            tmp515 = subjects309.popleft()
                                            # State 77493
                                            if len(subjects309) == 0:
                                                pass
                                                # State 77494
                                                if len(subjects) == 0:
                                                    pass
                                                    # 327: b/tan(d + x*e) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1266)
                                                    yield 327, subst4
                                                    # 329: b/tan(d + x*e) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1441)
                                                    yield 329, subst4
                                                    # 331: b/tan(d + x*e) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f1441)
                                                    yield 331, subst4
                                                    # 333: b/tan(d + x*e) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1442)
                                                    yield 333, subst4
                                                    # 335: b/tan(d + x*e) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f1442)
                                                    yield 335, subst4
                                            subjects309.appendleft(tmp515)
                                        if len(subjects309) >= 1 and subjects309[0] == Integer(2):
                                            tmp516 = subjects309.popleft()
                                            # State 82105
                                            if len(subjects309) == 0:
                                                pass
                                                # State 82106
                                                if len(subjects) == 0:
                                                    pass
                                                    # 336: b*tan(d + x*e)**2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1494)
                                                    yield 336, subst4
                                                    # 338: b*tan(d + x*e)**2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1458)
                                                    yield 338, subst4
                                            subjects309.appendleft(tmp516)
                                        if len(subjects309) >= 1 and subjects309[0] == Integer(-2):
                                            tmp517 = subjects309.popleft()
                                            # State 82123
                                            if len(subjects309) == 0:
                                                pass
                                                # State 82124
                                                if len(subjects) == 0:
                                                    pass
                                                    # 337: b/tan(d + x*e)**2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1494)
                                                    yield 337, subst4
                                                    # 339: b/tan(d + x*e)**2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1458)
                                                    yield 339, subst4
                                            subjects309.appendleft(tmp517)
                                        subst5 = Substitution(subst4)
                                        try:
                                            subst5.try_add_variable('i3.1.3', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 83513
                                            if len(subjects309) == 0:
                                                pass
                                                # State 83514
                                                if len(subjects) == 0:
                                                    pass
                                                    # 346: b*tan(d + x*e)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f228)
                                                    yield 346, subst5
                                                    # 342: b*tan(d + x*e)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                                                    yield 342, subst5
                                        if len(subjects309) >= 1:
                                            tmp519 = subjects309.popleft()
                                            subst5 = Substitution(subst4)
                                            try:
                                                subst5.try_add_variable('i3.1.3', tmp519)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 83513
                                                if len(subjects309) == 0:
                                                    pass
                                                    # State 83514
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 346: b*tan(d + x*e)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f228)
                                                        yield 346, subst5
                                                        # 342: b*tan(d + x*e)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                                                        yield 342, subst5
                                            subjects309.appendleft(tmp519)
                                subjects510.appendleft(tmp513)
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i3.1.3.1.0', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 87605
                            if len(subjects510) >= 1 and isinstance(subjects510[0], Pow):
                                tmp522 = subjects510.popleft()
                                subjects523 = deque(tmp522._args)
                                # State 87606
                                if len(subjects523) >= 1:
                                    tmp524 = subjects523.popleft()
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i3.1.3.1.1', tmp524)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 87607
                                        if len(subjects523) >= 1:
                                            tmp526 = subjects523.popleft()
                                            subst5 = Substitution(subst4)
                                            try:
                                                subst5.try_add_variable('i3.1.3.1.2', tmp526)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 87608
                                                if len(subjects523) == 0:
                                                    pass
                                                    # State 87609
                                                    if len(subjects510) == 0:
                                                        pass
                                                        # State 87610
                                                        if len(subjects309) >= 1 and subjects309[0] == Integer(-1):
                                                            tmp528 = subjects309.popleft()
                                                            # State 87611
                                                            if len(subjects309) == 0:
                                                                pass
                                                                # State 87612
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 353: b/tan(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f5) and (cons_f1497)
                                                                    yield 353, subst5
                                                                    # 355: b/tan(c + d*x**n) /; (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f70) and (cons_f71)
                                                                    yield 355, subst5
                                                                    # 351: b/tan(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f5) and (cons_f1575)
                                                                    yield 351, subst5
                                                            subjects309.appendleft(tmp528)
                                            subjects523.appendleft(tmp526)
                                    subjects523.appendleft(tmp524)
                                subjects510.appendleft(tmp522)
                        if len(subjects510) >= 1 and isinstance(subjects510[0], Mul):
                            tmp529 = subjects510.popleft()
                            associative1 = tmp529
                            associative_type1 = type(tmp529)
                            subjects530 = deque(tmp529._args)
                            matcher = CommutativeMatcher77496.get()
                            tmp531 = subjects530
                            subjects530 = []
                            for s in tmp531:
                                matcher.add_subject(s)
                            for pattern_index, subst3 in matcher.match(tmp531, subst2):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 77497
                                    if len(subjects510) == 0:
                                        pass
                                        # State 77498
                                        if len(subjects309) >= 1 and subjects309[0] == Integer(-1):
                                            tmp532 = subjects309.popleft()
                                            # State 77499
                                            if len(subjects309) == 0:
                                                pass
                                                # State 77500
                                                if len(subjects) == 0:
                                                    pass
                                                    # 327: b/tan(d + x*e) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1266)
                                                    yield 327, subst3
                                                    # 329: b/tan(d + x*e) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1441)
                                                    yield 329, subst3
                                                    # 331: b/tan(d + x*e) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f1441)
                                                    yield 331, subst3
                                                    # 333: b/tan(d + x*e) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1442)
                                                    yield 333, subst3
                                                    # 335: b/tan(d + x*e) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f1442)
                                                    yield 335, subst3
                                            subjects309.appendleft(tmp532)
                                        if len(subjects309) >= 1 and subjects309[0] == Integer(2):
                                            tmp533 = subjects309.popleft()
                                            # State 82107
                                            if len(subjects309) == 0:
                                                pass
                                                # State 82108
                                                if len(subjects) == 0:
                                                    pass
                                                    # 336: b*tan(d + x*e)**2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1494)
                                                    yield 336, subst3
                                                    # 338: b*tan(d + x*e)**2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1458)
                                                    yield 338, subst3
                                            subjects309.appendleft(tmp533)
                                        if len(subjects309) >= 1 and subjects309[0] == Integer(-2):
                                            tmp534 = subjects309.popleft()
                                            # State 82125
                                            if len(subjects309) == 0:
                                                pass
                                                # State 82126
                                                if len(subjects) == 0:
                                                    pass
                                                    # 337: b/tan(d + x*e)**2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1494)
                                                    yield 337, subst3
                                                    # 339: b/tan(d + x*e)**2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1458)
                                                    yield 339, subst3
                                            subjects309.appendleft(tmp534)
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i3.1.3', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 83515
                                            if len(subjects309) == 0:
                                                pass
                                                # State 83516
                                                if len(subjects) == 0:
                                                    pass
                                                    # 346: b*tan(d + x*e)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f228)
                                                    yield 346, subst4
                                                    # 342: b*tan(d + x*e)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                                                    yield 342, subst4
                                        if len(subjects309) >= 1:
                                            tmp536 = subjects309.popleft()
                                            subst4 = Substitution(subst3)
                                            try:
                                                subst4.try_add_variable('i3.1.3', tmp536)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 83515
                                                if len(subjects309) == 0:
                                                    pass
                                                    # State 83516
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 346: b*tan(d + x*e)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f228)
                                                        yield 346, subst4
                                                        # 342: b*tan(d + x*e)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                                                        yield 342, subst4
                                            subjects309.appendleft(tmp536)
                                if pattern_index == 1:
                                    pass
                                    # State 87617
                                    if len(subjects510) == 0:
                                        pass
                                        # State 87618
                                        if len(subjects309) >= 1 and subjects309[0] == Integer(-1):
                                            tmp538 = subjects309.popleft()
                                            # State 87619
                                            if len(subjects309) == 0:
                                                pass
                                                # State 87620
                                                if len(subjects) == 0:
                                                    pass
                                                    # 353: b/tan(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f5) and (cons_f1497)
                                                    yield 353, subst3
                                                    # 355: b/tan(c + d*x**n) /; (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f70) and (cons_f71)
                                                    yield 355, subst3
                                                    # 351: b/tan(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f5) and (cons_f1575)
                                                    yield 351, subst3
                                            subjects309.appendleft(tmp538)
                            subjects510.appendleft(tmp529)
                    if len(subjects510) >= 1:
                        tmp539 = subjects510.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i3.1.2', tmp539)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 87921
                            if len(subjects510) == 0:
                                pass
                                # State 87922
                                if len(subjects309) >= 1 and subjects309[0] == Integer(-1):
                                    tmp541 = subjects309.popleft()
                                    # State 87923
                                    if len(subjects309) == 0:
                                        pass
                                        # State 87924
                                        if len(subjects) == 0:
                                            pass
                                            # 357: b/tan(u) /; (cons_f3) and (cons_f825) and (cons_f826)
                                            yield 357, subst2
                                    subjects309.appendleft(tmp541)
                        subjects510.appendleft(tmp539)
                    if len(subjects510) >= 1 and isinstance(subjects510[0], Add):
                        tmp542 = subjects510.popleft()
                        associative1 = tmp542
                        associative_type1 = type(tmp542)
                        subjects543 = deque(tmp542._args)
                        matcher = CommutativeMatcher77502.get()
                        tmp544 = subjects543
                        subjects543 = []
                        for s in tmp544:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp544, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 77508
                                if len(subjects510) == 0:
                                    pass
                                    # State 77509
                                    if len(subjects309) >= 1 and subjects309[0] == Integer(-1):
                                        tmp545 = subjects309.popleft()
                                        # State 77510
                                        if len(subjects309) == 0:
                                            pass
                                            # State 77511
                                            if len(subjects) == 0:
                                                pass
                                                # 327: b/tan(d + x*e) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1266)
                                                yield 327, subst2
                                                # 329: b/tan(d + x*e) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1441)
                                                yield 329, subst2
                                                # 331: b/tan(d + x*e) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f1441)
                                                yield 331, subst2
                                                # 333: b/tan(d + x*e) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1442)
                                                yield 333, subst2
                                                # 335: b/tan(d + x*e) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f1442)
                                                yield 335, subst2
                                        subjects309.appendleft(tmp545)
                                    if len(subjects309) >= 1 and subjects309[0] == Integer(2):
                                        tmp546 = subjects309.popleft()
                                        # State 82109
                                        if len(subjects309) == 0:
                                            pass
                                            # State 82110
                                            if len(subjects) == 0:
                                                pass
                                                # 336: b*tan(d + x*e)**2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1494)
                                                yield 336, subst2
                                                # 338: b*tan(d + x*e)**2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1458)
                                                yield 338, subst2
                                        subjects309.appendleft(tmp546)
                                    if len(subjects309) >= 1 and subjects309[0] == Integer(-2):
                                        tmp547 = subjects309.popleft()
                                        # State 82127
                                        if len(subjects309) == 0:
                                            pass
                                            # State 82128
                                            if len(subjects) == 0:
                                                pass
                                                # 337: b/tan(d + x*e)**2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1494)
                                                yield 337, subst2
                                                # 339: b/tan(d + x*e)**2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1458)
                                                yield 339, subst2
                                        subjects309.appendleft(tmp547)
                                    subst3 = Substitution(subst2)
                                    try:
                                        subst3.try_add_variable('i3.1.3', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 83517
                                        if len(subjects309) == 0:
                                            pass
                                            # State 83518
                                            if len(subjects) == 0:
                                                pass
                                                # 346: b*tan(d + x*e)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f228)
                                                yield 346, subst3
                                                # 342: b*tan(d + x*e)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                                                yield 342, subst3
                                    if len(subjects309) >= 1:
                                        tmp549 = subjects309.popleft()
                                        subst3 = Substitution(subst2)
                                        try:
                                            subst3.try_add_variable('i3.1.3', tmp549)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 83517
                                            if len(subjects309) == 0:
                                                pass
                                                # State 83518
                                                if len(subjects) == 0:
                                                    pass
                                                    # 346: b*tan(d + x*e)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f228)
                                                    yield 346, subst3
                                                    # 342: b*tan(d + x*e)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                                                    yield 342, subst3
                                        subjects309.appendleft(tmp549)
                            if pattern_index == 1:
                                pass
                                # State 87631
                                if len(subjects510) == 0:
                                    pass
                                    # State 87632
                                    if len(subjects309) >= 1 and subjects309[0] == Integer(-1):
                                        tmp551 = subjects309.popleft()
                                        # State 87633
                                        if len(subjects309) == 0:
                                            pass
                                            # State 87634
                                            if len(subjects) == 0:
                                                pass
                                                # 353: b/tan(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f5) and (cons_f1497)
                                                yield 353, subst2
                                                # 355: b/tan(c + d*x**n) /; (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f70) and (cons_f71)
                                                yield 355, subst2
                                                # 351: b/tan(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f5) and (cons_f1575)
                                                yield 351, subst2
                                        subjects309.appendleft(tmp551)
                        subjects510.appendleft(tmp542)
                    subjects309.appendleft(tmp509)
                if len(subjects309) >= 1 and isinstance(subjects309[0], Pow):
                    tmp552 = subjects309.popleft()
                    subjects553 = deque(tmp552._args)
                    # State 83832
                    if len(subjects553) >= 1 and isinstance(subjects553[0], tan):
                        tmp554 = subjects553.popleft()
                        subjects555 = deque(tmp554._args)
                        # State 83833
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i3.1.4.0', S(0))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 83834
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i3.1.4.1.0_1', S(1))
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 83835
                                if len(subjects555) >= 1:
                                    tmp558 = subjects555.popleft()
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i3.1.4.1.0', tmp558)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 83836
                                        if len(subjects555) == 0:
                                            pass
                                            # State 83837
                                            if len(subjects553) >= 1 and subjects553[0] == Integer(-1):
                                                tmp560 = subjects553.popleft()
                                                # State 83838
                                                if len(subjects553) == 0:
                                                    pass
                                                    # State 83839
                                                    subst5 = Substitution(subst4)
                                                    try:
                                                        subst5.try_add_variable('i3.1.5', 1)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 83840
                                                        if len(subjects309) == 0:
                                                            pass
                                                            # State 83841
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 344: b*(1/tan(d + x*e))**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                                                                yield 344, subst5
                                                                # 348: b*(1/tan(d + x*e))**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f228)
                                                                yield 348, subst5
                                                    if len(subjects309) >= 1:
                                                        tmp562 = subjects309.popleft()
                                                        subst5 = Substitution(subst4)
                                                        try:
                                                            subst5.try_add_variable('i3.1.5', tmp562)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            # State 83840
                                                            if len(subjects309) == 0:
                                                                pass
                                                                # State 83841
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 344: b*(1/tan(d + x*e))**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                                                                    yield 344, subst5
                                                                    # 348: b*(1/tan(d + x*e))**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f228)
                                                                    yield 348, subst5
                                                        subjects309.appendleft(tmp562)
                                                subjects553.appendleft(tmp560)
                                    subjects555.appendleft(tmp558)
                            if len(subjects555) >= 1 and isinstance(subjects555[0], Mul):
                                tmp564 = subjects555.popleft()
                                associative1 = tmp564
                                associative_type1 = type(tmp564)
                                subjects565 = deque(tmp564._args)
                                matcher = CommutativeMatcher83843.get()
                                tmp566 = subjects565
                                subjects565 = []
                                for s in tmp566:
                                    matcher.add_subject(s)
                                for pattern_index, subst3 in matcher.match(tmp566, subst2):
                                    pass
                                    if pattern_index == 0:
                                        pass
                                        # State 83844
                                        if len(subjects555) == 0:
                                            pass
                                            # State 83845
                                            if len(subjects553) >= 1 and subjects553[0] == Integer(-1):
                                                tmp567 = subjects553.popleft()
                                                # State 83846
                                                if len(subjects553) == 0:
                                                    pass
                                                    # State 83847
                                                    subst4 = Substitution(subst3)
                                                    try:
                                                        subst4.try_add_variable('i3.1.5', 1)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 83848
                                                        if len(subjects309) == 0:
                                                            pass
                                                            # State 83849
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 344: b*(1/tan(d + x*e))**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                                                                yield 344, subst4
                                                                # 348: b*(1/tan(d + x*e))**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f228)
                                                                yield 348, subst4
                                                    if len(subjects309) >= 1:
                                                        tmp569 = subjects309.popleft()
                                                        subst4 = Substitution(subst3)
                                                        try:
                                                            subst4.try_add_variable('i3.1.5', tmp569)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            # State 83848
                                                            if len(subjects309) == 0:
                                                                pass
                                                                # State 83849
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 344: b*(1/tan(d + x*e))**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                                                                    yield 344, subst4
                                                                    # 348: b*(1/tan(d + x*e))**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f228)
                                                                    yield 348, subst4
                                                        subjects309.appendleft(tmp569)
                                                subjects553.appendleft(tmp567)
                                subjects555.appendleft(tmp564)
                        if len(subjects555) >= 1 and isinstance(subjects555[0], Add):
                            tmp571 = subjects555.popleft()
                            associative1 = tmp571
                            associative_type1 = type(tmp571)
                            subjects572 = deque(tmp571._args)
                            matcher = CommutativeMatcher83851.get()
                            tmp573 = subjects572
                            subjects572 = []
                            for s in tmp573:
                                matcher.add_subject(s)
                            for pattern_index, subst2 in matcher.match(tmp573, subst1):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 83857
                                    if len(subjects555) == 0:
                                        pass
                                        # State 83858
                                        if len(subjects553) >= 1 and subjects553[0] == Integer(-1):
                                            tmp574 = subjects553.popleft()
                                            # State 83859
                                            if len(subjects553) == 0:
                                                pass
                                                # State 83860
                                                subst3 = Substitution(subst2)
                                                try:
                                                    subst3.try_add_variable('i3.1.5', 1)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 83861
                                                    if len(subjects309) == 0:
                                                        pass
                                                        # State 83862
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 344: b*(1/tan(d + x*e))**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                                                            yield 344, subst3
                                                            # 348: b*(1/tan(d + x*e))**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f228)
                                                            yield 348, subst3
                                                if len(subjects309) >= 1:
                                                    tmp576 = subjects309.popleft()
                                                    subst3 = Substitution(subst2)
                                                    try:
                                                        subst3.try_add_variable('i3.1.5', tmp576)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 83861
                                                        if len(subjects309) == 0:
                                                            pass
                                                            # State 83862
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 344: b*(1/tan(d + x*e))**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                                                                yield 344, subst3
                                                                # 348: b*(1/tan(d + x*e))**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f228)
                                                                yield 348, subst3
                                                    subjects309.appendleft(tmp576)
                                            subjects553.appendleft(tmp574)
                            subjects555.appendleft(tmp571)
                        subjects553.appendleft(tmp554)
                    if len(subjects553) >= 1 and isinstance(subjects553[0], cos):
                        tmp578 = subjects553.popleft()
                        subjects579 = deque(tmp578._args)
                        # State 95541
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i3.1.4.0', S(0))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 95542
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i3.1.4.1.0_1', S(1))
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 95543
                                if len(subjects579) >= 1:
                                    tmp582 = subjects579.popleft()
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i3.1.4.1.0', tmp582)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 95544
                                        if len(subjects579) == 0:
                                            pass
                                            # State 95545
                                            if len(subjects553) >= 1 and subjects553[0] == Integer(-1):
                                                tmp584 = subjects553.popleft()
                                                # State 95546
                                                if len(subjects553) == 0:
                                                    pass
                                                    # State 95547
                                                    subst5 = Substitution(subst4)
                                                    try:
                                                        subst5.try_add_variable('i3.1.5', 1)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 95548
                                                        if len(subjects309) == 0:
                                                            pass
                                                            # State 95549
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 378: b*(1/cos(d + x*e))**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f5) and (cons_f48) and (cons_f47)
                                                                yield 378, subst5
                                                                # 374: b*(1/cos(d + x*e))**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                                                                yield 374, subst5
                                                                # 382: b*(1/cos(d + x*e))**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f228)
                                                                yield 382, subst5
                                                    if len(subjects309) >= 1:
                                                        tmp586 = subjects309.popleft()
                                                        subst5 = Substitution(subst4)
                                                        try:
                                                            subst5.try_add_variable('i3.1.5', tmp586)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            # State 95548
                                                            if len(subjects309) == 0:
                                                                pass
                                                                # State 95549
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 378: b*(1/cos(d + x*e))**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f5) and (cons_f48) and (cons_f47)
                                                                    yield 378, subst5
                                                                    # 374: b*(1/cos(d + x*e))**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                                                                    yield 374, subst5
                                                                    # 382: b*(1/cos(d + x*e))**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f228)
                                                                    yield 382, subst5
                                                        subjects309.appendleft(tmp586)
                                                subjects553.appendleft(tmp584)
                                    subjects579.appendleft(tmp582)
                            if len(subjects579) >= 1 and isinstance(subjects579[0], Mul):
                                tmp588 = subjects579.popleft()
                                associative1 = tmp588
                                associative_type1 = type(tmp588)
                                subjects589 = deque(tmp588._args)
                                matcher = CommutativeMatcher95551.get()
                                tmp590 = subjects589
                                subjects589 = []
                                for s in tmp590:
                                    matcher.add_subject(s)
                                for pattern_index, subst3 in matcher.match(tmp590, subst2):
                                    pass
                                    if pattern_index == 0:
                                        pass
                                        # State 95552
                                        if len(subjects579) == 0:
                                            pass
                                            # State 95553
                                            if len(subjects553) >= 1 and subjects553[0] == Integer(-1):
                                                tmp591 = subjects553.popleft()
                                                # State 95554
                                                if len(subjects553) == 0:
                                                    pass
                                                    # State 95555
                                                    subst4 = Substitution(subst3)
                                                    try:
                                                        subst4.try_add_variable('i3.1.5', 1)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 95556
                                                        if len(subjects309) == 0:
                                                            pass
                                                            # State 95557
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 378: b*(1/cos(d + x*e))**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f5) and (cons_f48) and (cons_f47)
                                                                yield 378, subst4
                                                                # 374: b*(1/cos(d + x*e))**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                                                                yield 374, subst4
                                                                # 382: b*(1/cos(d + x*e))**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f228)
                                                                yield 382, subst4
                                                    if len(subjects309) >= 1:
                                                        tmp593 = subjects309.popleft()
                                                        subst4 = Substitution(subst3)
                                                        try:
                                                            subst4.try_add_variable('i3.1.5', tmp593)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            # State 95556
                                                            if len(subjects309) == 0:
                                                                pass
                                                                # State 95557
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 378: b*(1/cos(d + x*e))**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f5) and (cons_f48) and (cons_f47)
                                                                    yield 378, subst4
                                                                    # 374: b*(1/cos(d + x*e))**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                                                                    yield 374, subst4
                                                                    # 382: b*(1/cos(d + x*e))**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f228)
                                                                    yield 382, subst4
                                                        subjects309.appendleft(tmp593)
                                                subjects553.appendleft(tmp591)
                                subjects579.appendleft(tmp588)
                        if len(subjects579) >= 1 and isinstance(subjects579[0], Add):
                            tmp595 = subjects579.popleft()
                            associative1 = tmp595
                            associative_type1 = type(tmp595)
                            subjects596 = deque(tmp595._args)
                            matcher = CommutativeMatcher95559.get()
                            tmp597 = subjects596
                            subjects596 = []
                            for s in tmp597:
                                matcher.add_subject(s)
                            for pattern_index, subst2 in matcher.match(tmp597, subst1):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 95565
                                    if len(subjects579) == 0:
                                        pass
                                        # State 95566
                                        if len(subjects553) >= 1 and subjects553[0] == Integer(-1):
                                            tmp598 = subjects553.popleft()
                                            # State 95567
                                            if len(subjects553) == 0:
                                                pass
                                                # State 95568
                                                subst3 = Substitution(subst2)
                                                try:
                                                    subst3.try_add_variable('i3.1.5', 1)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 95569
                                                    if len(subjects309) == 0:
                                                        pass
                                                        # State 95570
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 378: b*(1/cos(d + x*e))**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f5) and (cons_f48) and (cons_f47)
                                                            yield 378, subst3
                                                            # 374: b*(1/cos(d + x*e))**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                                                            yield 374, subst3
                                                            # 382: b*(1/cos(d + x*e))**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f228)
                                                            yield 382, subst3
                                                if len(subjects309) >= 1:
                                                    tmp600 = subjects309.popleft()
                                                    subst3 = Substitution(subst2)
                                                    try:
                                                        subst3.try_add_variable('i3.1.5', tmp600)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 95569
                                                        if len(subjects309) == 0:
                                                            pass
                                                            # State 95570
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 378: b*(1/cos(d + x*e))**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f5) and (cons_f48) and (cons_f47)
                                                                yield 378, subst3
                                                                # 374: b*(1/cos(d + x*e))**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                                                                yield 374, subst3
                                                                # 382: b*(1/cos(d + x*e))**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f228)
                                                                yield 382, subst3
                                                    subjects309.appendleft(tmp600)
                                            subjects553.appendleft(tmp598)
                            subjects579.appendleft(tmp595)
                        subjects553.appendleft(tmp578)
                    if len(subjects553) >= 1 and isinstance(subjects553[0], sin):
                        tmp602 = subjects553.popleft()
                        subjects603 = deque(tmp602._args)
                        # State 95937
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i3.1.4.0', S(0))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 95938
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i3.1.4.1.0_1', S(1))
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 95939
                                if len(subjects603) >= 1:
                                    tmp606 = subjects603.popleft()
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i3.1.4.1.0', tmp606)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 95940
                                        if len(subjects603) == 0:
                                            pass
                                            # State 95941
                                            if len(subjects553) >= 1 and subjects553[0] == Integer(-1):
                                                tmp608 = subjects553.popleft()
                                                # State 95942
                                                if len(subjects553) == 0:
                                                    pass
                                                    # State 95943
                                                    subst5 = Substitution(subst4)
                                                    try:
                                                        subst5.try_add_variable('i3.1.5', 1)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 95944
                                                        if len(subjects309) == 0:
                                                            pass
                                                            # State 95945
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 376: b*(1/sin(d + x*e))**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                                                                yield 376, subst5
                                                                # 380: b*(1/sin(d + x*e))**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f5) and (cons_f48) and (cons_f47)
                                                                yield 380, subst5
                                                                # 384: b*(1/sin(d + x*e))**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f228)
                                                                yield 384, subst5
                                                    if len(subjects309) >= 1:
                                                        tmp610 = subjects309.popleft()
                                                        subst5 = Substitution(subst4)
                                                        try:
                                                            subst5.try_add_variable('i3.1.5', tmp610)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            # State 95944
                                                            if len(subjects309) == 0:
                                                                pass
                                                                # State 95945
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 376: b*(1/sin(d + x*e))**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                                                                    yield 376, subst5
                                                                    # 380: b*(1/sin(d + x*e))**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f5) and (cons_f48) and (cons_f47)
                                                                    yield 380, subst5
                                                                    # 384: b*(1/sin(d + x*e))**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f228)
                                                                    yield 384, subst5
                                                        subjects309.appendleft(tmp610)
                                                subjects553.appendleft(tmp608)
                                    subjects603.appendleft(tmp606)
                            if len(subjects603) >= 1 and isinstance(subjects603[0], Mul):
                                tmp612 = subjects603.popleft()
                                associative1 = tmp612
                                associative_type1 = type(tmp612)
                                subjects613 = deque(tmp612._args)
                                matcher = CommutativeMatcher95947.get()
                                tmp614 = subjects613
                                subjects613 = []
                                for s in tmp614:
                                    matcher.add_subject(s)
                                for pattern_index, subst3 in matcher.match(tmp614, subst2):
                                    pass
                                    if pattern_index == 0:
                                        pass
                                        # State 95948
                                        if len(subjects603) == 0:
                                            pass
                                            # State 95949
                                            if len(subjects553) >= 1 and subjects553[0] == Integer(-1):
                                                tmp615 = subjects553.popleft()
                                                # State 95950
                                                if len(subjects553) == 0:
                                                    pass
                                                    # State 95951
                                                    subst4 = Substitution(subst3)
                                                    try:
                                                        subst4.try_add_variable('i3.1.5', 1)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 95952
                                                        if len(subjects309) == 0:
                                                            pass
                                                            # State 95953
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 376: b*(1/sin(d + x*e))**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                                                                yield 376, subst4
                                                                # 380: b*(1/sin(d + x*e))**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f5) and (cons_f48) and (cons_f47)
                                                                yield 380, subst4
                                                                # 384: b*(1/sin(d + x*e))**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f228)
                                                                yield 384, subst4
                                                    if len(subjects309) >= 1:
                                                        tmp617 = subjects309.popleft()
                                                        subst4 = Substitution(subst3)
                                                        try:
                                                            subst4.try_add_variable('i3.1.5', tmp617)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            # State 95952
                                                            if len(subjects309) == 0:
                                                                pass
                                                                # State 95953
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 376: b*(1/sin(d + x*e))**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                                                                    yield 376, subst4
                                                                    # 380: b*(1/sin(d + x*e))**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f5) and (cons_f48) and (cons_f47)
                                                                    yield 380, subst4
                                                                    # 384: b*(1/sin(d + x*e))**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f228)
                                                                    yield 384, subst4
                                                        subjects309.appendleft(tmp617)
                                                subjects553.appendleft(tmp615)
                                subjects603.appendleft(tmp612)
                        if len(subjects603) >= 1 and isinstance(subjects603[0], Add):
                            tmp619 = subjects603.popleft()
                            associative1 = tmp619
                            associative_type1 = type(tmp619)
                            subjects620 = deque(tmp619._args)
                            matcher = CommutativeMatcher95955.get()
                            tmp621 = subjects620
                            subjects620 = []
                            for s in tmp621:
                                matcher.add_subject(s)
                            for pattern_index, subst2 in matcher.match(tmp621, subst1):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 95961
                                    if len(subjects603) == 0:
                                        pass
                                        # State 95962
                                        if len(subjects553) >= 1 and subjects553[0] == Integer(-1):
                                            tmp622 = subjects553.popleft()
                                            # State 95963
                                            if len(subjects553) == 0:
                                                pass
                                                # State 95964
                                                subst3 = Substitution(subst2)
                                                try:
                                                    subst3.try_add_variable('i3.1.5', 1)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 95965
                                                    if len(subjects309) == 0:
                                                        pass
                                                        # State 95966
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 376: b*(1/sin(d + x*e))**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                                                            yield 376, subst3
                                                            # 380: b*(1/sin(d + x*e))**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f5) and (cons_f48) and (cons_f47)
                                                            yield 380, subst3
                                                            # 384: b*(1/sin(d + x*e))**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f228)
                                                            yield 384, subst3
                                                if len(subjects309) >= 1:
                                                    tmp624 = subjects309.popleft()
                                                    subst3 = Substitution(subst2)
                                                    try:
                                                        subst3.try_add_variable('i3.1.5', tmp624)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 95965
                                                        if len(subjects309) == 0:
                                                            pass
                                                            # State 95966
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 376: b*(1/sin(d + x*e))**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                                                                yield 376, subst3
                                                                # 380: b*(1/sin(d + x*e))**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f5) and (cons_f48) and (cons_f47)
                                                                yield 380, subst3
                                                                # 384: b*(1/sin(d + x*e))**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f228)
                                                                yield 384, subst3
                                                    subjects309.appendleft(tmp624)
                                            subjects553.appendleft(tmp622)
                            subjects603.appendleft(tmp619)
                        subjects553.appendleft(tmp602)
                    subjects309.appendleft(tmp552)
                if len(subjects309) >= 1 and isinstance(subjects309[0], tanh):
                    tmp626 = subjects309.popleft()
                    subjects627 = deque(tmp626._args)
                    # State 127084
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i3.1.3.0', S(0))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 127085
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i3.1.3.1.0', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 127086
                            if len(subjects627) >= 1 and isinstance(subjects627[0], Pow):
                                tmp630 = subjects627.popleft()
                                subjects631 = deque(tmp630._args)
                                # State 127087
                                if len(subjects631) >= 1:
                                    tmp632 = subjects631.popleft()
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i3.1.3.1.1', tmp632)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 127088
                                        if len(subjects631) >= 1:
                                            tmp634 = subjects631.popleft()
                                            subst5 = Substitution(subst4)
                                            try:
                                                subst5.try_add_variable('i3.1.3.1.2', tmp634)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 127089
                                                if len(subjects631) == 0:
                                                    pass
                                                    # State 127090
                                                    if len(subjects627) == 0:
                                                        pass
                                                        # State 127091
                                                        if len(subjects309) >= 1 and subjects309[0] == Integer(-1):
                                                            tmp636 = subjects309.popleft()
                                                            # State 127092
                                                            if len(subjects309) == 0:
                                                                pass
                                                                # State 127093
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 432: b/tanh(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f5) and (cons_f1497)
                                                                    yield 432, subst5
                                                                    # 434: b/tanh(c + d*x**n) /; (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f70) and (cons_f71)
                                                                    yield 434, subst5
                                                                    # 430: b/tanh(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f5) and (cons_f1575)
                                                                    yield 430, subst5
                                                            subjects309.appendleft(tmp636)
                                            subjects631.appendleft(tmp634)
                                    subjects631.appendleft(tmp632)
                                subjects627.appendleft(tmp630)
                        if len(subjects627) >= 1 and isinstance(subjects627[0], Mul):
                            tmp637 = subjects627.popleft()
                            associative1 = tmp637
                            associative_type1 = type(tmp637)
                            subjects638 = deque(tmp637._args)
                            matcher = CommutativeMatcher127095.get()
                            tmp639 = subjects638
                            subjects638 = []
                            for s in tmp639:
                                matcher.add_subject(s)
                            for pattern_index, subst3 in matcher.match(tmp639, subst2):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 127100
                                    if len(subjects627) == 0:
                                        pass
                                        # State 127101
                                        if len(subjects309) >= 1 and subjects309[0] == Integer(-1):
                                            tmp640 = subjects309.popleft()
                                            # State 127102
                                            if len(subjects309) == 0:
                                                pass
                                                # State 127103
                                                if len(subjects) == 0:
                                                    pass
                                                    # 432: b/tanh(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f5) and (cons_f1497)
                                                    yield 432, subst3
                                                    # 434: b/tanh(c + d*x**n) /; (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f70) and (cons_f71)
                                                    yield 434, subst3
                                                    # 430: b/tanh(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f5) and (cons_f1575)
                                                    yield 430, subst3
                                            subjects309.appendleft(tmp640)
                            subjects627.appendleft(tmp637)
                    if len(subjects627) >= 1:
                        tmp641 = subjects627.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i3.1.2', tmp641)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 127416
                            if len(subjects627) == 0:
                                pass
                                # State 127417
                                if len(subjects309) >= 1 and subjects309[0] == Integer(-1):
                                    tmp643 = subjects309.popleft()
                                    # State 127418
                                    if len(subjects309) == 0:
                                        pass
                                        # State 127419
                                        if len(subjects) == 0:
                                            pass
                                            # 436: b/tanh(u) /; (cons_f3) and (cons_f825) and (cons_f826)
                                            yield 436, subst2
                                    subjects309.appendleft(tmp643)
                        subjects627.appendleft(tmp641)
                    if len(subjects627) >= 1 and isinstance(subjects627[0], Add):
                        tmp644 = subjects627.popleft()
                        associative1 = tmp644
                        associative_type1 = type(tmp644)
                        subjects645 = deque(tmp644._args)
                        matcher = CommutativeMatcher127105.get()
                        tmp646 = subjects645
                        subjects645 = []
                        for s in tmp646:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp646, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 127118
                                if len(subjects627) == 0:
                                    pass
                                    # State 127119
                                    if len(subjects309) >= 1 and subjects309[0] == Integer(-1):
                                        tmp647 = subjects309.popleft()
                                        # State 127120
                                        if len(subjects309) == 0:
                                            pass
                                            # State 127121
                                            if len(subjects) == 0:
                                                pass
                                                # 432: b/tanh(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f5) and (cons_f1497)
                                                yield 432, subst2
                                                # 434: b/tanh(c + d*x**n) /; (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f70) and (cons_f71)
                                                yield 434, subst2
                                                # 430: b/tanh(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f5) and (cons_f1575)
                                                yield 430, subst2
                                        subjects309.appendleft(tmp647)
                        subjects627.appendleft(tmp644)
                    subjects309.appendleft(tmp626)
                if len(subjects309) >= 1 and isinstance(subjects309[0], cosh):
                    tmp648 = subjects309.popleft()
                    subjects649 = deque(tmp648._args)
                    # State 129861
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i3.1.3.0', S(0))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 129862
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i3.1.3.1.0', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 129863
                            if len(subjects649) >= 1 and isinstance(subjects649[0], Pow):
                                tmp652 = subjects649.popleft()
                                subjects653 = deque(tmp652._args)
                                # State 129864
                                if len(subjects653) >= 1:
                                    tmp654 = subjects653.popleft()
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i3.1.3.1.1', tmp654)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 129865
                                        if len(subjects653) >= 1:
                                            tmp656 = subjects653.popleft()
                                            subst5 = Substitution(subst4)
                                            try:
                                                subst5.try_add_variable('i3.1.3.1.2', tmp656)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 129866
                                                if len(subjects653) == 0:
                                                    pass
                                                    # State 129867
                                                    if len(subjects649) == 0:
                                                        pass
                                                        # State 129868
                                                        if len(subjects309) >= 1 and subjects309[0] == Integer(-1):
                                                            tmp658 = subjects309.popleft()
                                                            # State 129869
                                                            if len(subjects309) == 0:
                                                                pass
                                                                # State 129870
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 441: b/cosh(c + d*x**n) /; (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f70) and (cons_f71)
                                                                    yield 441, subst5
                                                                    # 437: b/cosh(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f5) and (cons_f1575)
                                                                    yield 437, subst5
                                                                    # 439: b/cosh(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f5) and (cons_f1497)
                                                                    yield 439, subst5
                                                            subjects309.appendleft(tmp658)
                                            subjects653.appendleft(tmp656)
                                    subjects653.appendleft(tmp654)
                                subjects649.appendleft(tmp652)
                        if len(subjects649) >= 1 and isinstance(subjects649[0], Mul):
                            tmp659 = subjects649.popleft()
                            associative1 = tmp659
                            associative_type1 = type(tmp659)
                            subjects660 = deque(tmp659._args)
                            matcher = CommutativeMatcher129872.get()
                            tmp661 = subjects660
                            subjects660 = []
                            for s in tmp661:
                                matcher.add_subject(s)
                            for pattern_index, subst3 in matcher.match(tmp661, subst2):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 129877
                                    if len(subjects649) == 0:
                                        pass
                                        # State 129878
                                        if len(subjects309) >= 1 and subjects309[0] == Integer(-1):
                                            tmp662 = subjects309.popleft()
                                            # State 129879
                                            if len(subjects309) == 0:
                                                pass
                                                # State 129880
                                                if len(subjects) == 0:
                                                    pass
                                                    # 441: b/cosh(c + d*x**n) /; (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f70) and (cons_f71)
                                                    yield 441, subst3
                                                    # 437: b/cosh(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f5) and (cons_f1575)
                                                    yield 437, subst3
                                                    # 439: b/cosh(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f5) and (cons_f1497)
                                                    yield 439, subst3
                                            subjects309.appendleft(tmp662)
                            subjects649.appendleft(tmp659)
                    if len(subjects649) >= 1:
                        tmp663 = subjects649.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i3.1.2', tmp663)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 130509
                            if len(subjects649) == 0:
                                pass
                                # State 130510
                                if len(subjects309) >= 1 and subjects309[0] == Integer(-1):
                                    tmp665 = subjects309.popleft()
                                    # State 130511
                                    if len(subjects309) == 0:
                                        pass
                                        # State 130512
                                        if len(subjects) == 0:
                                            pass
                                            # 443: b/cosh(u) /; (cons_f3) and (cons_f825) and (cons_f826)
                                            yield 443, subst2
                                    subjects309.appendleft(tmp665)
                        subjects649.appendleft(tmp663)
                    if len(subjects649) >= 1 and isinstance(subjects649[0], Add):
                        tmp666 = subjects649.popleft()
                        associative1 = tmp666
                        associative_type1 = type(tmp666)
                        subjects667 = deque(tmp666._args)
                        matcher = CommutativeMatcher129882.get()
                        tmp668 = subjects667
                        subjects667 = []
                        for s in tmp668:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp668, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 129895
                                if len(subjects649) == 0:
                                    pass
                                    # State 129896
                                    if len(subjects309) >= 1 and subjects309[0] == Integer(-1):
                                        tmp669 = subjects309.popleft()
                                        # State 129897
                                        if len(subjects309) == 0:
                                            pass
                                            # State 129898
                                            if len(subjects) == 0:
                                                pass
                                                # 441: b/cosh(c + d*x**n) /; (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f70) and (cons_f71)
                                                yield 441, subst2
                                                # 437: b/cosh(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f5) and (cons_f1575)
                                                yield 437, subst2
                                                # 439: b/cosh(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f5) and (cons_f1497)
                                                yield 439, subst2
                                        subjects309.appendleft(tmp669)
                        subjects649.appendleft(tmp666)
                    subjects309.appendleft(tmp648)
                if len(subjects309) >= 1 and isinstance(subjects309[0], sinh):
                    tmp670 = subjects309.popleft()
                    subjects671 = deque(tmp670._args)
                    # State 130201
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i3.1.3.0', S(0))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 130202
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i3.1.3.1.0', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 130203
                            if len(subjects671) >= 1 and isinstance(subjects671[0], Pow):
                                tmp674 = subjects671.popleft()
                                subjects675 = deque(tmp674._args)
                                # State 130204
                                if len(subjects675) >= 1:
                                    tmp676 = subjects675.popleft()
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i3.1.3.1.1', tmp676)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 130205
                                        if len(subjects675) >= 1:
                                            tmp678 = subjects675.popleft()
                                            subst5 = Substitution(subst4)
                                            try:
                                                subst5.try_add_variable('i3.1.3.1.2', tmp678)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 130206
                                                if len(subjects675) == 0:
                                                    pass
                                                    # State 130207
                                                    if len(subjects671) == 0:
                                                        pass
                                                        # State 130208
                                                        if len(subjects309) >= 1 and subjects309[0] == Integer(-1):
                                                            tmp680 = subjects309.popleft()
                                                            # State 130209
                                                            if len(subjects309) == 0:
                                                                pass
                                                                # State 130210
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 440: b/sinh(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f5) and (cons_f1497)
                                                                    yield 440, subst5
                                                                    # 442: b/sinh(c + d*x**n) /; (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f70) and (cons_f71)
                                                                    yield 442, subst5
                                                                    # 438: b/sinh(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f5) and (cons_f1575)
                                                                    yield 438, subst5
                                                            subjects309.appendleft(tmp680)
                                            subjects675.appendleft(tmp678)
                                    subjects675.appendleft(tmp676)
                                subjects671.appendleft(tmp674)
                        if len(subjects671) >= 1 and isinstance(subjects671[0], Mul):
                            tmp681 = subjects671.popleft()
                            associative1 = tmp681
                            associative_type1 = type(tmp681)
                            subjects682 = deque(tmp681._args)
                            matcher = CommutativeMatcher130212.get()
                            tmp683 = subjects682
                            subjects682 = []
                            for s in tmp683:
                                matcher.add_subject(s)
                            for pattern_index, subst3 in matcher.match(tmp683, subst2):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 130217
                                    if len(subjects671) == 0:
                                        pass
                                        # State 130218
                                        if len(subjects309) >= 1 and subjects309[0] == Integer(-1):
                                            tmp684 = subjects309.popleft()
                                            # State 130219
                                            if len(subjects309) == 0:
                                                pass
                                                # State 130220
                                                if len(subjects) == 0:
                                                    pass
                                                    # 440: b/sinh(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f5) and (cons_f1497)
                                                    yield 440, subst3
                                                    # 442: b/sinh(c + d*x**n) /; (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f70) and (cons_f71)
                                                    yield 442, subst3
                                                    # 438: b/sinh(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f5) and (cons_f1575)
                                                    yield 438, subst3
                                            subjects309.appendleft(tmp684)
                            subjects671.appendleft(tmp681)
                    if len(subjects671) >= 1:
                        tmp685 = subjects671.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i3.1.2', tmp685)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 130565
                            if len(subjects671) == 0:
                                pass
                                # State 130566
                                if len(subjects309) >= 1 and subjects309[0] == Integer(-1):
                                    tmp687 = subjects309.popleft()
                                    # State 130567
                                    if len(subjects309) == 0:
                                        pass
                                        # State 130568
                                        if len(subjects) == 0:
                                            pass
                                            # 444: b/sinh(u) /; (cons_f3) and (cons_f825) and (cons_f826)
                                            yield 444, subst2
                                    subjects309.appendleft(tmp687)
                        subjects671.appendleft(tmp685)
                    if len(subjects671) >= 1 and isinstance(subjects671[0], Add):
                        tmp688 = subjects671.popleft()
                        associative1 = tmp688
                        associative_type1 = type(tmp688)
                        subjects689 = deque(tmp688._args)
                        matcher = CommutativeMatcher130222.get()
                        tmp690 = subjects689
                        subjects689 = []
                        for s in tmp690:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp690, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 130235
                                if len(subjects671) == 0:
                                    pass
                                    # State 130236
                                    if len(subjects309) >= 1 and subjects309[0] == Integer(-1):
                                        tmp691 = subjects309.popleft()
                                        # State 130237
                                        if len(subjects309) == 0:
                                            pass
                                            # State 130238
                                            if len(subjects) == 0:
                                                pass
                                                # 440: b/sinh(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f5) and (cons_f1497)
                                                yield 440, subst2
                                                # 442: b/sinh(c + d*x**n) /; (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f70) and (cons_f71)
                                                yield 442, subst2
                                                # 438: b/sinh(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f5) and (cons_f1575)
                                                yield 438, subst2
                                        subjects309.appendleft(tmp691)
                        subjects671.appendleft(tmp688)
                    subjects309.appendleft(tmp670)
                subjects.appendleft(tmp308)
            subst2 = Substitution(subst1)
            try:
                subst2.try_add_variable('i3.1.2', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 9751
                if len(subjects) >= 1:
                    tmp693 = subjects.popleft()
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i3.1.1', tmp693)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 9752
                        if len(subjects) == 0:
                            pass
                            # 128: b*x**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f52) and (cons_f754) and (cons_f755) and (cons_f228) and (cons_f756)
                            yield 128, subst3
                            # 131: b*x**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f52) and (cons_f754) and (cons_f755) and (cons_f228)
                            yield 131, subst3
                            # 163: b*x**n /; (cons_f2) and (cons_f3) and (cons_f966) and (cons_f967)
                            yield 163, subst3
                            # 133: b*x**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f52) and (cons_f754) and (cons_f755)
                            yield 133, subst3
                            # 165: b*x**n /; (cons_f2) and (cons_f3) and (cons_f798) and (cons_f4) and (cons_f5) and (cons_f954) and (cons_f968)
                            yield 165, subst3
                            # 167: b*x**n /; (cons_f2) and (cons_f798) and (cons_f70) and (cons_f71)
                            yield 167, subst3
                            # 136: b*x**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f52) and (cons_f754)
                            yield 136, subst3
                            # 138: b*x**n /; (cons_f3) and (cons_f4) and (cons_f754) and (cons_f70) and (cons_f71)
                            yield 138, subst3
                            # 147: b*x**n /; (cons_f2) and (cons_f3) and (cons_f798) and (cons_f4) and (cons_f5) and (cons_f954) and (cons_f955)
                            yield 147, subst3
                            # 149: b*x**n /; (cons_f2) and (cons_f3) and (cons_f798) and (cons_f4) and (cons_f954) and (cons_f956)
                            yield 149, subst3
                            # 125: b*x**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f52) and (cons_f754) and (cons_f755)
                            yield 125, subst3
                            # 151: b*x**n /; (cons_f2) and (cons_f3) and (cons_f798) and (cons_f4) and (cons_f5) and (cons_f954) and (cons_f956) and (cons_f957)
                            yield 151, subst3
                            # 153: b*x**n /; (cons_f2) and (cons_f3) and (cons_f958) and (cons_f959) and (cons_f960)
                            yield 153, subst3
                            # 122: b*x**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f752) and (cons_f753)
                            yield 122, subst3
                            # 155: b*x**n /; (cons_f2) and (cons_f3) and (cons_f958) and (cons_f959)
                            yield 155, subst3
                            # 157: b*x**n /; (cons_f2) and (cons_f3) and (cons_f958) and (cons_f959) and (cons_f962)
                            yield 157, subst3
                            # 159: b*x**n /; (cons_f2) and (cons_f3) and (cons_f798) and (cons_f4) and (cons_f954) and (cons_f964)
                            yield 159, subst3
                    subjects.appendleft(tmp693)
            subst2 = Substitution(subst1)
            try:
                subst2.try_add_variable('i3.1.3', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 68892
                if len(subjects) >= 1 and isinstance(subjects[0], sin):
                    tmp696 = subjects.popleft()
                    subjects697 = deque(tmp696._args)
                    # State 68893
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i3.1.3.0', S(0))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 68894
                        subst4 = Substitution(subst3)
                        try:
                            subst4.try_add_variable('i3.1.3.1.0_1', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 68895
                            if len(subjects697) >= 1:
                                tmp700 = subjects697.popleft()
                                subst5 = Substitution(subst4)
                                try:
                                    subst5.try_add_variable('i3.1.3.1.0', tmp700)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 68896
                                    if len(subjects697) == 0:
                                        pass
                                        # State 68897
                                        if len(subjects) == 0:
                                            pass
                                            # 304: b*sin(d + x*e)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f5) and (cons_f48) and (cons_f47)
                                            yield 304, subst5
                                            # 300: b*sin(d + x*e)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                                            yield 300, subst5
                                            # 308: b*sin(d + x*e)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f228)
                                            yield 308, subst5
                                subjects697.appendleft(tmp700)
                        if len(subjects697) >= 1 and isinstance(subjects697[0], Mul):
                            tmp702 = subjects697.popleft()
                            associative1 = tmp702
                            associative_type1 = type(tmp702)
                            subjects703 = deque(tmp702._args)
                            matcher = CommutativeMatcher68899.get()
                            tmp704 = subjects703
                            subjects703 = []
                            for s in tmp704:
                                matcher.add_subject(s)
                            for pattern_index, subst4 in matcher.match(tmp704, subst3):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 68900
                                    if len(subjects697) == 0:
                                        pass
                                        # State 68901
                                        if len(subjects) == 0:
                                            pass
                                            # 304: b*sin(d + x*e)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f5) and (cons_f48) and (cons_f47)
                                            yield 304, subst4
                                            # 300: b*sin(d + x*e)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                                            yield 300, subst4
                                            # 308: b*sin(d + x*e)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f228)
                                            yield 308, subst4
                            subjects697.appendleft(tmp702)
                    if len(subjects697) >= 1 and isinstance(subjects697[0], Add):
                        tmp705 = subjects697.popleft()
                        associative1 = tmp705
                        associative_type1 = type(tmp705)
                        subjects706 = deque(tmp705._args)
                        matcher = CommutativeMatcher68903.get()
                        tmp707 = subjects706
                        subjects706 = []
                        for s in tmp707:
                            matcher.add_subject(s)
                        for pattern_index, subst3 in matcher.match(tmp707, subst2):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 68909
                                if len(subjects697) == 0:
                                    pass
                                    # State 68910
                                    if len(subjects) == 0:
                                        pass
                                        # 304: b*sin(d + x*e)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f5) and (cons_f48) and (cons_f47)
                                        yield 304, subst3
                                        # 300: b*sin(d + x*e)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                                        yield 300, subst3
                                        # 308: b*sin(d + x*e)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f228)
                                        yield 308, subst3
                        subjects697.appendleft(tmp705)
                    subjects.appendleft(tmp696)
                if len(subjects) >= 1 and isinstance(subjects[0], cos):
                    tmp708 = subjects.popleft()
                    subjects709 = deque(tmp708._args)
                    # State 69172
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i3.1.3.0', S(0))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 69173
                        subst4 = Substitution(subst3)
                        try:
                            subst4.try_add_variable('i3.1.3.1.0_1', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 69174
                            if len(subjects709) >= 1:
                                tmp712 = subjects709.popleft()
                                subst5 = Substitution(subst4)
                                try:
                                    subst5.try_add_variable('i3.1.3.1.0', tmp712)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 69175
                                    if len(subjects709) == 0:
                                        pass
                                        # State 69176
                                        if len(subjects) == 0:
                                            pass
                                            # 302: b*cos(d + x*e)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                                            yield 302, subst5
                                            # 306: b*cos(d + x*e)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f5) and (cons_f48) and (cons_f47)
                                            yield 306, subst5
                                            # 310: b*cos(d + x*e)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f228)
                                            yield 310, subst5
                                subjects709.appendleft(tmp712)
                        if len(subjects709) >= 1 and isinstance(subjects709[0], Mul):
                            tmp714 = subjects709.popleft()
                            associative1 = tmp714
                            associative_type1 = type(tmp714)
                            subjects715 = deque(tmp714._args)
                            matcher = CommutativeMatcher69178.get()
                            tmp716 = subjects715
                            subjects715 = []
                            for s in tmp716:
                                matcher.add_subject(s)
                            for pattern_index, subst4 in matcher.match(tmp716, subst3):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 69179
                                    if len(subjects709) == 0:
                                        pass
                                        # State 69180
                                        if len(subjects) == 0:
                                            pass
                                            # 302: b*cos(d + x*e)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                                            yield 302, subst4
                                            # 306: b*cos(d + x*e)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f5) and (cons_f48) and (cons_f47)
                                            yield 306, subst4
                                            # 310: b*cos(d + x*e)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f228)
                                            yield 310, subst4
                            subjects709.appendleft(tmp714)
                    if len(subjects709) >= 1 and isinstance(subjects709[0], Add):
                        tmp717 = subjects709.popleft()
                        associative1 = tmp717
                        associative_type1 = type(tmp717)
                        subjects718 = deque(tmp717._args)
                        matcher = CommutativeMatcher69182.get()
                        tmp719 = subjects718
                        subjects718 = []
                        for s in tmp719:
                            matcher.add_subject(s)
                        for pattern_index, subst3 in matcher.match(tmp719, subst2):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 69188
                                if len(subjects709) == 0:
                                    pass
                                    # State 69189
                                    if len(subjects) == 0:
                                        pass
                                        # 302: b*cos(d + x*e)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                                        yield 302, subst3
                                        # 306: b*cos(d + x*e)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f5) and (cons_f48) and (cons_f47)
                                        yield 306, subst3
                                        # 310: b*cos(d + x*e)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f228)
                                        yield 310, subst3
                        subjects709.appendleft(tmp717)
                    subjects.appendleft(tmp708)
                if len(subjects) >= 1 and isinstance(subjects[0], tan):
                    tmp720 = subjects.popleft()
                    subjects721 = deque(tmp720._args)
                    # State 83495
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i3.1.3.0', S(0))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 83496
                        subst4 = Substitution(subst3)
                        try:
                            subst4.try_add_variable('i3.1.3.1.0_1', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 83497
                            if len(subjects721) >= 1:
                                tmp724 = subjects721.popleft()
                                subst5 = Substitution(subst4)
                                try:
                                    subst5.try_add_variable('i3.1.3.1.0', tmp724)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 83498
                                    if len(subjects721) == 0:
                                        pass
                                        # State 83499
                                        if len(subjects) == 0:
                                            pass
                                            # 346: b*tan(d + x*e)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f228)
                                            yield 346, subst5
                                            # 342: b*tan(d + x*e)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                                            yield 342, subst5
                                subjects721.appendleft(tmp724)
                        if len(subjects721) >= 1 and isinstance(subjects721[0], Mul):
                            tmp726 = subjects721.popleft()
                            associative1 = tmp726
                            associative_type1 = type(tmp726)
                            subjects727 = deque(tmp726._args)
                            matcher = CommutativeMatcher83501.get()
                            tmp728 = subjects727
                            subjects727 = []
                            for s in tmp728:
                                matcher.add_subject(s)
                            for pattern_index, subst4 in matcher.match(tmp728, subst3):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 83502
                                    if len(subjects721) == 0:
                                        pass
                                        # State 83503
                                        if len(subjects) == 0:
                                            pass
                                            # 346: b*tan(d + x*e)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f228)
                                            yield 346, subst4
                                            # 342: b*tan(d + x*e)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                                            yield 342, subst4
                            subjects721.appendleft(tmp726)
                    if len(subjects721) >= 1 and isinstance(subjects721[0], Add):
                        tmp729 = subjects721.popleft()
                        associative1 = tmp729
                        associative_type1 = type(tmp729)
                        subjects730 = deque(tmp729._args)
                        matcher = CommutativeMatcher83505.get()
                        tmp731 = subjects730
                        subjects730 = []
                        for s in tmp731:
                            matcher.add_subject(s)
                        for pattern_index, subst3 in matcher.match(tmp731, subst2):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 83511
                                if len(subjects721) == 0:
                                    pass
                                    # State 83512
                                    if len(subjects) == 0:
                                        pass
                                        # 346: b*tan(d + x*e)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f228)
                                        yield 346, subst3
                                        # 342: b*tan(d + x*e)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                                        yield 342, subst3
                        subjects721.appendleft(tmp729)
                    subjects.appendleft(tmp720)
            subst2 = Substitution(subst1)
            try:
                subst2.try_add_variable('i3.1.5', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 83806
                if len(subjects) >= 1 and isinstance(subjects[0], Pow):
                    tmp733 = subjects.popleft()
                    subjects734 = deque(tmp733._args)
                    # State 83807
                    if len(subjects734) >= 1 and isinstance(subjects734[0], tan):
                        tmp735 = subjects734.popleft()
                        subjects736 = deque(tmp735._args)
                        # State 83808
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i3.1.4.0', S(0))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 83809
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i3.1.4.1.0_1', S(1))
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 83810
                                if len(subjects736) >= 1:
                                    tmp739 = subjects736.popleft()
                                    subst5 = Substitution(subst4)
                                    try:
                                        subst5.try_add_variable('i3.1.4.1.0', tmp739)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 83811
                                        if len(subjects736) == 0:
                                            pass
                                            # State 83812
                                            if len(subjects734) >= 1 and subjects734[0] == Integer(-1):
                                                tmp741 = subjects734.popleft()
                                                # State 83813
                                                if len(subjects734) == 0:
                                                    pass
                                                    # State 83814
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 344: b*(1/tan(d + x*e))**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                                                        yield 344, subst5
                                                        # 348: b*(1/tan(d + x*e))**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f228)
                                                        yield 348, subst5
                                                subjects734.appendleft(tmp741)
                                    subjects736.appendleft(tmp739)
                            if len(subjects736) >= 1 and isinstance(subjects736[0], Mul):
                                tmp742 = subjects736.popleft()
                                associative1 = tmp742
                                associative_type1 = type(tmp742)
                                subjects743 = deque(tmp742._args)
                                matcher = CommutativeMatcher83816.get()
                                tmp744 = subjects743
                                subjects743 = []
                                for s in tmp744:
                                    matcher.add_subject(s)
                                for pattern_index, subst4 in matcher.match(tmp744, subst3):
                                    pass
                                    if pattern_index == 0:
                                        pass
                                        # State 83817
                                        if len(subjects736) == 0:
                                            pass
                                            # State 83818
                                            if len(subjects734) >= 1 and subjects734[0] == Integer(-1):
                                                tmp745 = subjects734.popleft()
                                                # State 83819
                                                if len(subjects734) == 0:
                                                    pass
                                                    # State 83820
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 344: b*(1/tan(d + x*e))**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                                                        yield 344, subst4
                                                        # 348: b*(1/tan(d + x*e))**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f228)
                                                        yield 348, subst4
                                                subjects734.appendleft(tmp745)
                                subjects736.appendleft(tmp742)
                        if len(subjects736) >= 1 and isinstance(subjects736[0], Add):
                            tmp746 = subjects736.popleft()
                            associative1 = tmp746
                            associative_type1 = type(tmp746)
                            subjects747 = deque(tmp746._args)
                            matcher = CommutativeMatcher83822.get()
                            tmp748 = subjects747
                            subjects747 = []
                            for s in tmp748:
                                matcher.add_subject(s)
                            for pattern_index, subst3 in matcher.match(tmp748, subst2):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 83828
                                    if len(subjects736) == 0:
                                        pass
                                        # State 83829
                                        if len(subjects734) >= 1 and subjects734[0] == Integer(-1):
                                            tmp749 = subjects734.popleft()
                                            # State 83830
                                            if len(subjects734) == 0:
                                                pass
                                                # State 83831
                                                if len(subjects) == 0:
                                                    pass
                                                    # 344: b*(1/tan(d + x*e))**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                                                    yield 344, subst3
                                                    # 348: b*(1/tan(d + x*e))**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f228)
                                                    yield 348, subst3
                                            subjects734.appendleft(tmp749)
                            subjects736.appendleft(tmp746)
                        subjects734.appendleft(tmp735)
                    if len(subjects734) >= 1 and isinstance(subjects734[0], cos):
                        tmp750 = subjects734.popleft()
                        subjects751 = deque(tmp750._args)
                        # State 95517
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i3.1.4.0', S(0))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 95518
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i3.1.4.1.0_1', S(1))
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 95519
                                if len(subjects751) >= 1:
                                    tmp754 = subjects751.popleft()
                                    subst5 = Substitution(subst4)
                                    try:
                                        subst5.try_add_variable('i3.1.4.1.0', tmp754)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 95520
                                        if len(subjects751) == 0:
                                            pass
                                            # State 95521
                                            if len(subjects734) >= 1 and subjects734[0] == Integer(-1):
                                                tmp756 = subjects734.popleft()
                                                # State 95522
                                                if len(subjects734) == 0:
                                                    pass
                                                    # State 95523
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 378: b*(1/cos(d + x*e))**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f5) and (cons_f48) and (cons_f47)
                                                        yield 378, subst5
                                                        # 374: b*(1/cos(d + x*e))**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                                                        yield 374, subst5
                                                        # 382: b*(1/cos(d + x*e))**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f228)
                                                        yield 382, subst5
                                                subjects734.appendleft(tmp756)
                                    subjects751.appendleft(tmp754)
                            if len(subjects751) >= 1 and isinstance(subjects751[0], Mul):
                                tmp757 = subjects751.popleft()
                                associative1 = tmp757
                                associative_type1 = type(tmp757)
                                subjects758 = deque(tmp757._args)
                                matcher = CommutativeMatcher95525.get()
                                tmp759 = subjects758
                                subjects758 = []
                                for s in tmp759:
                                    matcher.add_subject(s)
                                for pattern_index, subst4 in matcher.match(tmp759, subst3):
                                    pass
                                    if pattern_index == 0:
                                        pass
                                        # State 95526
                                        if len(subjects751) == 0:
                                            pass
                                            # State 95527
                                            if len(subjects734) >= 1 and subjects734[0] == Integer(-1):
                                                tmp760 = subjects734.popleft()
                                                # State 95528
                                                if len(subjects734) == 0:
                                                    pass
                                                    # State 95529
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 378: b*(1/cos(d + x*e))**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f5) and (cons_f48) and (cons_f47)
                                                        yield 378, subst4
                                                        # 374: b*(1/cos(d + x*e))**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                                                        yield 374, subst4
                                                        # 382: b*(1/cos(d + x*e))**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f228)
                                                        yield 382, subst4
                                                subjects734.appendleft(tmp760)
                                subjects751.appendleft(tmp757)
                        if len(subjects751) >= 1 and isinstance(subjects751[0], Add):
                            tmp761 = subjects751.popleft()
                            associative1 = tmp761
                            associative_type1 = type(tmp761)
                            subjects762 = deque(tmp761._args)
                            matcher = CommutativeMatcher95531.get()
                            tmp763 = subjects762
                            subjects762 = []
                            for s in tmp763:
                                matcher.add_subject(s)
                            for pattern_index, subst3 in matcher.match(tmp763, subst2):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 95537
                                    if len(subjects751) == 0:
                                        pass
                                        # State 95538
                                        if len(subjects734) >= 1 and subjects734[0] == Integer(-1):
                                            tmp764 = subjects734.popleft()
                                            # State 95539
                                            if len(subjects734) == 0:
                                                pass
                                                # State 95540
                                                if len(subjects) == 0:
                                                    pass
                                                    # 378: b*(1/cos(d + x*e))**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f5) and (cons_f48) and (cons_f47)
                                                    yield 378, subst3
                                                    # 374: b*(1/cos(d + x*e))**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                                                    yield 374, subst3
                                                    # 382: b*(1/cos(d + x*e))**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f228)
                                                    yield 382, subst3
                                            subjects734.appendleft(tmp764)
                            subjects751.appendleft(tmp761)
                        subjects734.appendleft(tmp750)
                    if len(subjects734) >= 1 and isinstance(subjects734[0], sin):
                        tmp765 = subjects734.popleft()
                        subjects766 = deque(tmp765._args)
                        # State 95913
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i3.1.4.0', S(0))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 95914
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i3.1.4.1.0_1', S(1))
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 95915
                                if len(subjects766) >= 1:
                                    tmp769 = subjects766.popleft()
                                    subst5 = Substitution(subst4)
                                    try:
                                        subst5.try_add_variable('i3.1.4.1.0', tmp769)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 95916
                                        if len(subjects766) == 0:
                                            pass
                                            # State 95917
                                            if len(subjects734) >= 1 and subjects734[0] == Integer(-1):
                                                tmp771 = subjects734.popleft()
                                                # State 95918
                                                if len(subjects734) == 0:
                                                    pass
                                                    # State 95919
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 376: b*(1/sin(d + x*e))**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                                                        yield 376, subst5
                                                        # 380: b*(1/sin(d + x*e))**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f5) and (cons_f48) and (cons_f47)
                                                        yield 380, subst5
                                                        # 384: b*(1/sin(d + x*e))**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f228)
                                                        yield 384, subst5
                                                subjects734.appendleft(tmp771)
                                    subjects766.appendleft(tmp769)
                            if len(subjects766) >= 1 and isinstance(subjects766[0], Mul):
                                tmp772 = subjects766.popleft()
                                associative1 = tmp772
                                associative_type1 = type(tmp772)
                                subjects773 = deque(tmp772._args)
                                matcher = CommutativeMatcher95921.get()
                                tmp774 = subjects773
                                subjects773 = []
                                for s in tmp774:
                                    matcher.add_subject(s)
                                for pattern_index, subst4 in matcher.match(tmp774, subst3):
                                    pass
                                    if pattern_index == 0:
                                        pass
                                        # State 95922
                                        if len(subjects766) == 0:
                                            pass
                                            # State 95923
                                            if len(subjects734) >= 1 and subjects734[0] == Integer(-1):
                                                tmp775 = subjects734.popleft()
                                                # State 95924
                                                if len(subjects734) == 0:
                                                    pass
                                                    # State 95925
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 376: b*(1/sin(d + x*e))**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                                                        yield 376, subst4
                                                        # 380: b*(1/sin(d + x*e))**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f5) and (cons_f48) and (cons_f47)
                                                        yield 380, subst4
                                                        # 384: b*(1/sin(d + x*e))**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f228)
                                                        yield 384, subst4
                                                subjects734.appendleft(tmp775)
                                subjects766.appendleft(tmp772)
                        if len(subjects766) >= 1 and isinstance(subjects766[0], Add):
                            tmp776 = subjects766.popleft()
                            associative1 = tmp776
                            associative_type1 = type(tmp776)
                            subjects777 = deque(tmp776._args)
                            matcher = CommutativeMatcher95927.get()
                            tmp778 = subjects777
                            subjects777 = []
                            for s in tmp778:
                                matcher.add_subject(s)
                            for pattern_index, subst3 in matcher.match(tmp778, subst2):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 95933
                                    if len(subjects766) == 0:
                                        pass
                                        # State 95934
                                        if len(subjects734) >= 1 and subjects734[0] == Integer(-1):
                                            tmp779 = subjects734.popleft()
                                            # State 95935
                                            if len(subjects734) == 0:
                                                pass
                                                # State 95936
                                                if len(subjects) == 0:
                                                    pass
                                                    # 376: b*(1/sin(d + x*e))**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                                                    yield 376, subst3
                                                    # 380: b*(1/sin(d + x*e))**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f5) and (cons_f48) and (cons_f47)
                                                    yield 380, subst3
                                                    # 384: b*(1/sin(d + x*e))**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f228)
                                                    yield 384, subst3
                                            subjects734.appendleft(tmp779)
                            subjects766.appendleft(tmp776)
                        subjects734.appendleft(tmp765)
                    subjects.appendleft(tmp733)
            if len(subjects) >= 1 and isinstance(subjects[0], log):
                tmp780 = subjects.popleft()
                subjects781 = deque(tmp780._args)
                # State 19738
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i3.1.2.0', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 19739
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i3.1.2.2', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 19740
                        subst4 = Substitution(subst3)
                        try:
                            subst4.try_add_variable('i3.1.2.2.0', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 19741
                            subst5 = Substitution(subst4)
                            try:
                                subst5.try_add_variable('i3.1.2.2.2', S(1))
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 19742
                                subst6 = Substitution(subst5)
                                try:
                                    subst6.try_add_variable('i3.1.2.2.2.0', S(0))
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 19743
                                    subst7 = Substitution(subst6)
                                    try:
                                        subst7.try_add_variable('i3.1.2.2.2.1.0_1', S(1))
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 19744
                                        if len(subjects781) >= 1:
                                            tmp788 = subjects781.popleft()
                                            subst8 = Substitution(subst7)
                                            try:
                                                subst8.try_add_variable('i3.1.2.2.2.1.0', tmp788)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 19745
                                                if len(subjects781) == 0:
                                                    pass
                                                    # State 19746
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 232: b*log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f417)
                                                        yield 232, subst8
                                                        # 233: b*log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f1160)
                                                        yield 233, subst8
                                                        # 234: b*log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f1161)
                                                        yield 234, subst8
                                                        # 231: b*log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52)
                                                        yield 231, subst8
                                            subjects781.appendleft(tmp788)
                                    if len(subjects781) >= 1 and isinstance(subjects781[0], Mul):
                                        tmp790 = subjects781.popleft()
                                        associative1 = tmp790
                                        associative_type1 = type(tmp790)
                                        subjects791 = deque(tmp790._args)
                                        matcher = CommutativeMatcher19748.get()
                                        tmp792 = subjects791
                                        subjects791 = []
                                        for s in tmp792:
                                            matcher.add_subject(s)
                                        for pattern_index, subst7 in matcher.match(tmp792, subst6):
                                            pass
                                            if pattern_index == 0:
                                                pass
                                                # State 19749
                                                if len(subjects781) == 0:
                                                    pass
                                                    # State 19750
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 232: b*log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f417)
                                                        yield 232, subst7
                                                        # 233: b*log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f1160)
                                                        yield 233, subst7
                                                        # 234: b*log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f1161)
                                                        yield 234, subst7
                                                        # 231: b*log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52)
                                                        yield 231, subst7
                                        subjects781.appendleft(tmp790)
                                if len(subjects781) >= 1 and isinstance(subjects781[0], Add):
                                    tmp793 = subjects781.popleft()
                                    associative1 = tmp793
                                    associative_type1 = type(tmp793)
                                    subjects794 = deque(tmp793._args)
                                    matcher = CommutativeMatcher19752.get()
                                    tmp795 = subjects794
                                    subjects794 = []
                                    for s in tmp795:
                                        matcher.add_subject(s)
                                    for pattern_index, subst6 in matcher.match(tmp795, subst5):
                                        pass
                                        if pattern_index == 0:
                                            pass
                                            # State 19758
                                            if len(subjects781) == 0:
                                                pass
                                                # State 19759
                                                if len(subjects) == 0:
                                                    pass
                                                    # 232: b*log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f417)
                                                    yield 232, subst6
                                                    # 233: b*log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f1160)
                                                    yield 233, subst6
                                                    # 234: b*log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f1161)
                                                    yield 234, subst6
                                                    # 231: b*log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52)
                                                    yield 231, subst6
                                    subjects781.appendleft(tmp793)
                            if len(subjects781) >= 1 and isinstance(subjects781[0], Pow):
                                tmp796 = subjects781.popleft()
                                subjects797 = deque(tmp796._args)
                                # State 19760
                                subst5 = Substitution(subst4)
                                try:
                                    subst5.try_add_variable('i3.1.2.2.2.0', S(0))
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 19761
                                    subst6 = Substitution(subst5)
                                    try:
                                        subst6.try_add_variable('i3.1.2.2.2.1.0_1', S(1))
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 19762
                                        if len(subjects797) >= 1:
                                            tmp800 = subjects797.popleft()
                                            subst7 = Substitution(subst6)
                                            try:
                                                subst7.try_add_variable('i3.1.2.2.2.1.0', tmp800)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 19763
                                                subst8 = Substitution(subst7)
                                                try:
                                                    subst8.try_add_variable('i3.1.2.2.2', 1)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 19764
                                                    if len(subjects797) == 0:
                                                        pass
                                                        # State 19765
                                                        if len(subjects781) == 0:
                                                            pass
                                                            # State 19766
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 232: b*log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f417)
                                                                yield 232, subst8
                                                                # 233: b*log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f1160)
                                                                yield 233, subst8
                                                                # 234: b*log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f1161)
                                                                yield 234, subst8
                                                                # 231: b*log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52)
                                                                yield 231, subst8
                                                if len(subjects797) >= 1:
                                                    tmp803 = subjects797.popleft()
                                                    subst8 = Substitution(subst7)
                                                    try:
                                                        subst8.try_add_variable('i3.1.2.2.2', tmp803)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 19764
                                                        if len(subjects797) == 0:
                                                            pass
                                                            # State 19765
                                                            if len(subjects781) == 0:
                                                                pass
                                                                # State 19766
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 232: b*log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f417)
                                                                    yield 232, subst8
                                                                    # 233: b*log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f1160)
                                                                    yield 233, subst8
                                                                    # 234: b*log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f1161)
                                                                    yield 234, subst8
                                                                    # 231: b*log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52)
                                                                    yield 231, subst8
                                                    subjects797.appendleft(tmp803)
                                            subjects797.appendleft(tmp800)
                                    if len(subjects797) >= 1 and isinstance(subjects797[0], Mul):
                                        tmp805 = subjects797.popleft()
                                        associative1 = tmp805
                                        associative_type1 = type(tmp805)
                                        subjects806 = deque(tmp805._args)
                                        matcher = CommutativeMatcher19768.get()
                                        tmp807 = subjects806
                                        subjects806 = []
                                        for s in tmp807:
                                            matcher.add_subject(s)
                                        for pattern_index, subst6 in matcher.match(tmp807, subst5):
                                            pass
                                            if pattern_index == 0:
                                                pass
                                                # State 19769
                                                subst7 = Substitution(subst6)
                                                try:
                                                    subst7.try_add_variable('i3.1.2.2.2', 1)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 19770
                                                    if len(subjects797) == 0:
                                                        pass
                                                        # State 19771
                                                        if len(subjects781) == 0:
                                                            pass
                                                            # State 19772
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 232: b*log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f417)
                                                                yield 232, subst7
                                                                # 233: b*log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f1160)
                                                                yield 233, subst7
                                                                # 234: b*log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f1161)
                                                                yield 234, subst7
                                                                # 231: b*log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52)
                                                                yield 231, subst7
                                                if len(subjects797) >= 1:
                                                    tmp809 = []
                                                    tmp809.append(subjects797.popleft())
                                                    while True:
                                                        if len(tmp809) > 1:
                                                            tmp810 = create_operation_expression(associative1, tmp809)
                                                        elif len(tmp809) == 1:
                                                            tmp810 = tmp809[0]
                                                        else:
                                                            assert False, "Unreachable"
                                                        subst7 = Substitution(subst6)
                                                        try:
                                                            subst7.try_add_variable('i3.1.2.2.2', tmp810)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            # State 19770
                                                            if len(subjects797) == 0:
                                                                pass
                                                                # State 19771
                                                                if len(subjects781) == 0:
                                                                    pass
                                                                    # State 19772
                                                                    if len(subjects) == 0:
                                                                        pass
                                                                        # 232: b*log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f417)
                                                                        yield 232, subst7
                                                                        # 233: b*log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f1160)
                                                                        yield 233, subst7
                                                                        # 234: b*log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f1161)
                                                                        yield 234, subst7
                                                                        # 231: b*log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52)
                                                                        yield 231, subst7
                                                        if len(subjects797) == 0:
                                                            break
                                                        tmp809.append(subjects797.popleft())
                                                    subjects797.extendleft(reversed(tmp809))
                                        subjects797.appendleft(tmp805)
                                if len(subjects797) >= 1 and isinstance(subjects797[0], Add):
                                    tmp812 = subjects797.popleft()
                                    associative1 = tmp812
                                    associative_type1 = type(tmp812)
                                    subjects813 = deque(tmp812._args)
                                    matcher = CommutativeMatcher19774.get()
                                    tmp814 = subjects813
                                    subjects813 = []
                                    for s in tmp814:
                                        matcher.add_subject(s)
                                    for pattern_index, subst5 in matcher.match(tmp814, subst4):
                                        pass
                                        if pattern_index == 0:
                                            pass
                                            # State 19780
                                            subst6 = Substitution(subst5)
                                            try:
                                                subst6.try_add_variable('i3.1.2.2.2', 1)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 19781
                                                if len(subjects797) == 0:
                                                    pass
                                                    # State 19782
                                                    if len(subjects781) == 0:
                                                        pass
                                                        # State 19783
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 232: b*log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f417)
                                                            yield 232, subst6
                                                            # 233: b*log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f1160)
                                                            yield 233, subst6
                                                            # 234: b*log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f1161)
                                                            yield 234, subst6
                                                            # 231: b*log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52)
                                                            yield 231, subst6
                                            if len(subjects797) >= 1:
                                                tmp816 = []
                                                tmp816.append(subjects797.popleft())
                                                while True:
                                                    if len(tmp816) > 1:
                                                        tmp817 = create_operation_expression(associative1, tmp816)
                                                    elif len(tmp816) == 1:
                                                        tmp817 = tmp816[0]
                                                    else:
                                                        assert False, "Unreachable"
                                                    subst6 = Substitution(subst5)
                                                    try:
                                                        subst6.try_add_variable('i3.1.2.2.2', tmp817)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 19781
                                                        if len(subjects797) == 0:
                                                            pass
                                                            # State 19782
                                                            if len(subjects781) == 0:
                                                                pass
                                                                # State 19783
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 232: b*log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f417)
                                                                    yield 232, subst6
                                                                    # 233: b*log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f1160)
                                                                    yield 233, subst6
                                                                    # 234: b*log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f1161)
                                                                    yield 234, subst6
                                                                    # 231: b*log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52)
                                                                    yield 231, subst6
                                                    if len(subjects797) == 0:
                                                        break
                                                    tmp816.append(subjects797.popleft())
                                                subjects797.extendleft(reversed(tmp816))
                                    subjects797.appendleft(tmp812)
                                subjects781.appendleft(tmp796)
                        if len(subjects781) >= 1:
                            tmp819 = subjects781.popleft()
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i3.1.2.1', tmp819)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 53183
                                if len(subjects781) == 0:
                                    pass
                                    # State 53184
                                    if len(subjects) == 0:
                                        pass
                                        # 237: b*log(c*RFx**p) /; (cons_f3) and (cons_f8) and (cons_f5) and (cons_f1200)
                                        yield 237, subst4
                            subjects781.appendleft(tmp819)
                        if len(subjects781) >= 1 and isinstance(subjects781[0], Mul):
                            tmp821 = subjects781.popleft()
                            associative1 = tmp821
                            associative_type1 = type(tmp821)
                            subjects822 = deque(tmp821._args)
                            matcher = CommutativeMatcher19785.get()
                            tmp823 = subjects822
                            subjects822 = []
                            for s in tmp823:
                                matcher.add_subject(s)
                            for pattern_index, subst4 in matcher.match(tmp823, subst3):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 19822
                                    if len(subjects781) == 0:
                                        pass
                                        # State 19823
                                        if len(subjects) == 0:
                                            pass
                                            # 232: b*log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f417)
                                            yield 232, subst4
                                            # 233: b*log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f1160)
                                            yield 233, subst4
                                            # 234: b*log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f1161)
                                            yield 234, subst4
                                            # 231: b*log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52)
                                            yield 231, subst4
                            subjects781.appendleft(tmp821)
                        if len(subjects781) >= 1 and isinstance(subjects781[0], Add):
                            tmp824 = subjects781.popleft()
                            associative1 = tmp824
                            associative_type1 = type(tmp824)
                            subjects825 = deque(tmp824._args)
                            matcher = CommutativeMatcher50668.get()
                            tmp826 = subjects825
                            subjects825 = []
                            for s in tmp826:
                                matcher.add_subject(s)
                            for pattern_index, subst4 in matcher.match(tmp826, subst3):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 50681
                                    if len(subjects781) == 0:
                                        pass
                                        # State 50682
                                        if len(subjects) == 0:
                                            pass
                                            # 235: b*log(c*(d + e*x**2)**p) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f5)
                                            yield 235, subst4
                                if pattern_index == 1:
                                    pass
                                    # State 52764
                                    if len(subjects781) == 0:
                                        pass
                                        # State 52765
                                        if len(subjects) == 0:
                                            pass
                                            # 236: b*log(c*(d + e/(f + x*g))**p) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f210) and (cons_f5)
                                            yield 236, subst4
                            subjects781.appendleft(tmp824)
                    if len(subjects781) >= 1 and isinstance(subjects781[0], Pow):
                        tmp827 = subjects781.popleft()
                        subjects828 = deque(tmp827._args)
                        # State 19824
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i3.1.2.2.0', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 19825
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i3.1.2.2.2', S(1))
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 19826
                                subst5 = Substitution(subst4)
                                try:
                                    subst5.try_add_variable('i3.1.2.2.2.0', S(0))
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 19827
                                    subst6 = Substitution(subst5)
                                    try:
                                        subst6.try_add_variable('i3.1.2.2.2.1.0_1', S(1))
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 19828
                                        if len(subjects828) >= 1:
                                            tmp833 = subjects828.popleft()
                                            subst7 = Substitution(subst6)
                                            try:
                                                subst7.try_add_variable('i3.1.2.2.2.1.0', tmp833)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 19829
                                                subst8 = Substitution(subst7)
                                                try:
                                                    subst8.try_add_variable('i3.1.2.2', 1)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 19830
                                                    if len(subjects828) == 0:
                                                        pass
                                                        # State 19831
                                                        if len(subjects781) == 0:
                                                            pass
                                                            # State 19832
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 232: b*log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f417)
                                                                yield 232, subst8
                                                                # 233: b*log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f1160)
                                                                yield 233, subst8
                                                                # 234: b*log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f1161)
                                                                yield 234, subst8
                                                                # 231: b*log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52)
                                                                yield 231, subst8
                                                if len(subjects828) >= 1:
                                                    tmp836 = subjects828.popleft()
                                                    subst8 = Substitution(subst7)
                                                    try:
                                                        subst8.try_add_variable('i3.1.2.2', tmp836)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 19830
                                                        if len(subjects828) == 0:
                                                            pass
                                                            # State 19831
                                                            if len(subjects781) == 0:
                                                                pass
                                                                # State 19832
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 232: b*log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f417)
                                                                    yield 232, subst8
                                                                    # 233: b*log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f1160)
                                                                    yield 233, subst8
                                                                    # 234: b*log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f1161)
                                                                    yield 234, subst8
                                                                    # 231: b*log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52)
                                                                    yield 231, subst8
                                                    subjects828.appendleft(tmp836)
                                            subjects828.appendleft(tmp833)
                                    if len(subjects828) >= 1 and isinstance(subjects828[0], Mul):
                                        tmp838 = subjects828.popleft()
                                        associative1 = tmp838
                                        associative_type1 = type(tmp838)
                                        subjects839 = deque(tmp838._args)
                                        matcher = CommutativeMatcher19834.get()
                                        tmp840 = subjects839
                                        subjects839 = []
                                        for s in tmp840:
                                            matcher.add_subject(s)
                                        for pattern_index, subst6 in matcher.match(tmp840, subst5):
                                            pass
                                            if pattern_index == 0:
                                                pass
                                                # State 19835
                                                subst7 = Substitution(subst6)
                                                try:
                                                    subst7.try_add_variable('i3.1.2.2', 1)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 19836
                                                    if len(subjects828) == 0:
                                                        pass
                                                        # State 19837
                                                        if len(subjects781) == 0:
                                                            pass
                                                            # State 19838
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 232: b*log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f417)
                                                                yield 232, subst7
                                                                # 233: b*log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f1160)
                                                                yield 233, subst7
                                                                # 234: b*log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f1161)
                                                                yield 234, subst7
                                                                # 231: b*log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52)
                                                                yield 231, subst7
                                                if len(subjects828) >= 1:
                                                    tmp842 = []
                                                    tmp842.append(subjects828.popleft())
                                                    while True:
                                                        if len(tmp842) > 1:
                                                            tmp843 = create_operation_expression(associative1, tmp842)
                                                        elif len(tmp842) == 1:
                                                            tmp843 = tmp842[0]
                                                        else:
                                                            assert False, "Unreachable"
                                                        subst7 = Substitution(subst6)
                                                        try:
                                                            subst7.try_add_variable('i3.1.2.2', tmp843)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            # State 19836
                                                            if len(subjects828) == 0:
                                                                pass
                                                                # State 19837
                                                                if len(subjects781) == 0:
                                                                    pass
                                                                    # State 19838
                                                                    if len(subjects) == 0:
                                                                        pass
                                                                        # 232: b*log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f417)
                                                                        yield 232, subst7
                                                                        # 233: b*log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f1160)
                                                                        yield 233, subst7
                                                                        # 234: b*log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f1161)
                                                                        yield 234, subst7
                                                                        # 231: b*log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52)
                                                                        yield 231, subst7
                                                        if len(subjects828) == 0:
                                                            break
                                                        tmp842.append(subjects828.popleft())
                                                    subjects828.extendleft(reversed(tmp842))
                                        subjects828.appendleft(tmp838)
                                if len(subjects828) >= 1 and isinstance(subjects828[0], Add):
                                    tmp845 = subjects828.popleft()
                                    associative1 = tmp845
                                    associative_type1 = type(tmp845)
                                    subjects846 = deque(tmp845._args)
                                    matcher = CommutativeMatcher19840.get()
                                    tmp847 = subjects846
                                    subjects846 = []
                                    for s in tmp847:
                                        matcher.add_subject(s)
                                    for pattern_index, subst5 in matcher.match(tmp847, subst4):
                                        pass
                                        if pattern_index == 0:
                                            pass
                                            # State 19846
                                            subst6 = Substitution(subst5)
                                            try:
                                                subst6.try_add_variable('i3.1.2.2', 1)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 19847
                                                if len(subjects828) == 0:
                                                    pass
                                                    # State 19848
                                                    if len(subjects781) == 0:
                                                        pass
                                                        # State 19849
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 232: b*log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f417)
                                                            yield 232, subst6
                                                            # 233: b*log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f1160)
                                                            yield 233, subst6
                                                            # 234: b*log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f1161)
                                                            yield 234, subst6
                                                            # 231: b*log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52)
                                                            yield 231, subst6
                                            if len(subjects828) >= 1:
                                                tmp849 = []
                                                tmp849.append(subjects828.popleft())
                                                while True:
                                                    if len(tmp849) > 1:
                                                        tmp850 = create_operation_expression(associative1, tmp849)
                                                    elif len(tmp849) == 1:
                                                        tmp850 = tmp849[0]
                                                    else:
                                                        assert False, "Unreachable"
                                                    subst6 = Substitution(subst5)
                                                    try:
                                                        subst6.try_add_variable('i3.1.2.2', tmp850)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 19847
                                                        if len(subjects828) == 0:
                                                            pass
                                                            # State 19848
                                                            if len(subjects781) == 0:
                                                                pass
                                                                # State 19849
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 232: b*log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f417)
                                                                    yield 232, subst6
                                                                    # 233: b*log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f1160)
                                                                    yield 233, subst6
                                                                    # 234: b*log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f1161)
                                                                    yield 234, subst6
                                                                    # 231: b*log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52)
                                                                    yield 231, subst6
                                                    if len(subjects828) == 0:
                                                        break
                                                    tmp849.append(subjects828.popleft())
                                                subjects828.extendleft(reversed(tmp849))
                                    subjects828.appendleft(tmp845)
                            if len(subjects828) >= 1 and isinstance(subjects828[0], Pow):
                                tmp852 = subjects828.popleft()
                                subjects853 = deque(tmp852._args)
                                # State 19850
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i3.1.2.2.2.0', S(0))
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 19851
                                    subst5 = Substitution(subst4)
                                    try:
                                        subst5.try_add_variable('i3.1.2.2.2.1.0_1', S(1))
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 19852
                                        if len(subjects853) >= 1:
                                            tmp856 = subjects853.popleft()
                                            subst6 = Substitution(subst5)
                                            try:
                                                subst6.try_add_variable('i3.1.2.2.2.1.0', tmp856)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 19853
                                                subst7 = Substitution(subst6)
                                                try:
                                                    subst7.try_add_variable('i3.1.2.2.2', 1)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 19854
                                                    if len(subjects853) == 0:
                                                        pass
                                                        # State 19855
                                                        subst8 = Substitution(subst7)
                                                        try:
                                                            subst8.try_add_variable('i3.1.2.2', 1)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            # State 19856
                                                            if len(subjects828) == 0:
                                                                pass
                                                                # State 19857
                                                                if len(subjects781) == 0:
                                                                    pass
                                                                    # State 19858
                                                                    if len(subjects) == 0:
                                                                        pass
                                                                        # 232: b*log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f417)
                                                                        yield 232, subst8
                                                                        # 233: b*log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f1160)
                                                                        yield 233, subst8
                                                                        # 234: b*log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f1161)
                                                                        yield 234, subst8
                                                                        # 231: b*log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52)
                                                                        yield 231, subst8
                                                        if len(subjects828) >= 1:
                                                            tmp860 = subjects828.popleft()
                                                            subst8 = Substitution(subst7)
                                                            try:
                                                                subst8.try_add_variable('i3.1.2.2', tmp860)
                                                            except ValueError:
                                                                pass
                                                            else:
                                                                pass
                                                                # State 19856
                                                                if len(subjects828) == 0:
                                                                    pass
                                                                    # State 19857
                                                                    if len(subjects781) == 0:
                                                                        pass
                                                                        # State 19858
                                                                        if len(subjects) == 0:
                                                                            pass
                                                                            # 232: b*log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f417)
                                                                            yield 232, subst8
                                                                            # 233: b*log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f1160)
                                                                            yield 233, subst8
                                                                            # 234: b*log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f1161)
                                                                            yield 234, subst8
                                                                            # 231: b*log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52)
                                                                            yield 231, subst8
                                                            subjects828.appendleft(tmp860)
                                                if len(subjects853) >= 1:
                                                    tmp862 = subjects853.popleft()
                                                    subst7 = Substitution(subst6)
                                                    try:
                                                        subst7.try_add_variable('i3.1.2.2.2', tmp862)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 19854
                                                        if len(subjects853) == 0:
                                                            pass
                                                            # State 19855
                                                            subst8 = Substitution(subst7)
                                                            try:
                                                                subst8.try_add_variable('i3.1.2.2', 1)
                                                            except ValueError:
                                                                pass
                                                            else:
                                                                pass
                                                                # State 19856
                                                                if len(subjects828) == 0:
                                                                    pass
                                                                    # State 19857
                                                                    if len(subjects781) == 0:
                                                                        pass
                                                                        # State 19858
                                                                        if len(subjects) == 0:
                                                                            pass
                                                                            # 232: b*log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f417)
                                                                            yield 232, subst8
                                                                            # 233: b*log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f1160)
                                                                            yield 233, subst8
                                                                            # 234: b*log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f1161)
                                                                            yield 234, subst8
                                                                            # 231: b*log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52)
                                                                            yield 231, subst8
                                                            if len(subjects828) >= 1:
                                                                tmp865 = subjects828.popleft()
                                                                subst8 = Substitution(subst7)
                                                                try:
                                                                    subst8.try_add_variable('i3.1.2.2', tmp865)
                                                                except ValueError:
                                                                    pass
                                                                else:
                                                                    pass
                                                                    # State 19856
                                                                    if len(subjects828) == 0:
                                                                        pass
                                                                        # State 19857
                                                                        if len(subjects781) == 0:
                                                                            pass
                                                                            # State 19858
                                                                            if len(subjects) == 0:
                                                                                pass
                                                                                # 232: b*log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f417)
                                                                                yield 232, subst8
                                                                                # 233: b*log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f1160)
                                                                                yield 233, subst8
                                                                                # 234: b*log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f1161)
                                                                                yield 234, subst8
                                                                                # 231: b*log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52)
                                                                                yield 231, subst8
                                                                subjects828.appendleft(tmp865)
                                                    subjects853.appendleft(tmp862)
                                            subjects853.appendleft(tmp856)
                                    if len(subjects853) >= 1 and isinstance(subjects853[0], Mul):
                                        tmp867 = subjects853.popleft()
                                        associative1 = tmp867
                                        associative_type1 = type(tmp867)
                                        subjects868 = deque(tmp867._args)
                                        matcher = CommutativeMatcher19860.get()
                                        tmp869 = subjects868
                                        subjects868 = []
                                        for s in tmp869:
                                            matcher.add_subject(s)
                                        for pattern_index, subst5 in matcher.match(tmp869, subst4):
                                            pass
                                            if pattern_index == 0:
                                                pass
                                                # State 19861
                                                subst6 = Substitution(subst5)
                                                try:
                                                    subst6.try_add_variable('i3.1.2.2.2', 1)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 19862
                                                    if len(subjects853) == 0:
                                                        pass
                                                        # State 19863
                                                        subst7 = Substitution(subst6)
                                                        try:
                                                            subst7.try_add_variable('i3.1.2.2', 1)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            # State 19864
                                                            if len(subjects828) == 0:
                                                                pass
                                                                # State 19865
                                                                if len(subjects781) == 0:
                                                                    pass
                                                                    # State 19866
                                                                    if len(subjects) == 0:
                                                                        pass
                                                                        # 232: b*log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f417)
                                                                        yield 232, subst7
                                                                        # 233: b*log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f1160)
                                                                        yield 233, subst7
                                                                        # 234: b*log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f1161)
                                                                        yield 234, subst7
                                                                        # 231: b*log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52)
                                                                        yield 231, subst7
                                                        if len(subjects828) >= 1:
                                                            tmp872 = subjects828.popleft()
                                                            subst7 = Substitution(subst6)
                                                            try:
                                                                subst7.try_add_variable('i3.1.2.2', tmp872)
                                                            except ValueError:
                                                                pass
                                                            else:
                                                                pass
                                                                # State 19864
                                                                if len(subjects828) == 0:
                                                                    pass
                                                                    # State 19865
                                                                    if len(subjects781) == 0:
                                                                        pass
                                                                        # State 19866
                                                                        if len(subjects) == 0:
                                                                            pass
                                                                            # 232: b*log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f417)
                                                                            yield 232, subst7
                                                                            # 233: b*log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f1160)
                                                                            yield 233, subst7
                                                                            # 234: b*log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f1161)
                                                                            yield 234, subst7
                                                                            # 231: b*log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52)
                                                                            yield 231, subst7
                                                            subjects828.appendleft(tmp872)
                                                if len(subjects853) >= 1:
                                                    tmp874 = []
                                                    tmp874.append(subjects853.popleft())
                                                    while True:
                                                        if len(tmp874) > 1:
                                                            tmp875 = create_operation_expression(associative1, tmp874)
                                                        elif len(tmp874) == 1:
                                                            tmp875 = tmp874[0]
                                                        else:
                                                            assert False, "Unreachable"
                                                        subst6 = Substitution(subst5)
                                                        try:
                                                            subst6.try_add_variable('i3.1.2.2.2', tmp875)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            # State 19862
                                                            if len(subjects853) == 0:
                                                                pass
                                                                # State 19863
                                                                subst7 = Substitution(subst6)
                                                                try:
                                                                    subst7.try_add_variable('i3.1.2.2', 1)
                                                                except ValueError:
                                                                    pass
                                                                else:
                                                                    pass
                                                                    # State 19864
                                                                    if len(subjects828) == 0:
                                                                        pass
                                                                        # State 19865
                                                                        if len(subjects781) == 0:
                                                                            pass
                                                                            # State 19866
                                                                            if len(subjects) == 0:
                                                                                pass
                                                                                # 232: b*log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f417)
                                                                                yield 232, subst7
                                                                                # 233: b*log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f1160)
                                                                                yield 233, subst7
                                                                                # 234: b*log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f1161)
                                                                                yield 234, subst7
                                                                                # 231: b*log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52)
                                                                                yield 231, subst7
                                                                if len(subjects828) >= 1:
                                                                    tmp878 = subjects828.popleft()
                                                                    subst7 = Substitution(subst6)
                                                                    try:
                                                                        subst7.try_add_variable('i3.1.2.2', tmp878)
                                                                    except ValueError:
                                                                        pass
                                                                    else:
                                                                        pass
                                                                        # State 19864
                                                                        if len(subjects828) == 0:
                                                                            pass
                                                                            # State 19865
                                                                            if len(subjects781) == 0:
                                                                                pass
                                                                                # State 19866
                                                                                if len(subjects) == 0:
                                                                                    pass
                                                                                    # 232: b*log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f417)
                                                                                    yield 232, subst7
                                                                                    # 233: b*log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f1160)
                                                                                    yield 233, subst7
                                                                                    # 234: b*log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f1161)
                                                                                    yield 234, subst7
                                                                                    # 231: b*log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52)
                                                                                    yield 231, subst7
                                                                    subjects828.appendleft(tmp878)
                                                        if len(subjects853) == 0:
                                                            break
                                                        tmp874.append(subjects853.popleft())
                                                    subjects853.extendleft(reversed(tmp874))
                                        subjects853.appendleft(tmp867)
                                if len(subjects853) >= 1 and isinstance(subjects853[0], Add):
                                    tmp880 = subjects853.popleft()
                                    associative1 = tmp880
                                    associative_type1 = type(tmp880)
                                    subjects881 = deque(tmp880._args)
                                    matcher = CommutativeMatcher19868.get()
                                    tmp882 = subjects881
                                    subjects881 = []
                                    for s in tmp882:
                                        matcher.add_subject(s)
                                    for pattern_index, subst4 in matcher.match(tmp882, subst3):
                                        pass
                                        if pattern_index == 0:
                                            pass
                                            # State 19874
                                            subst5 = Substitution(subst4)
                                            try:
                                                subst5.try_add_variable('i3.1.2.2.2', 1)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 19875
                                                if len(subjects853) == 0:
                                                    pass
                                                    # State 19876
                                                    subst6 = Substitution(subst5)
                                                    try:
                                                        subst6.try_add_variable('i3.1.2.2', 1)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 19877
                                                        if len(subjects828) == 0:
                                                            pass
                                                            # State 19878
                                                            if len(subjects781) == 0:
                                                                pass
                                                                # State 19879
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 232: b*log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f417)
                                                                    yield 232, subst6
                                                                    # 233: b*log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f1160)
                                                                    yield 233, subst6
                                                                    # 234: b*log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f1161)
                                                                    yield 234, subst6
                                                                    # 231: b*log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52)
                                                                    yield 231, subst6
                                                    if len(subjects828) >= 1:
                                                        tmp885 = subjects828.popleft()
                                                        subst6 = Substitution(subst5)
                                                        try:
                                                            subst6.try_add_variable('i3.1.2.2', tmp885)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            # State 19877
                                                            if len(subjects828) == 0:
                                                                pass
                                                                # State 19878
                                                                if len(subjects781) == 0:
                                                                    pass
                                                                    # State 19879
                                                                    if len(subjects) == 0:
                                                                        pass
                                                                        # 232: b*log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f417)
                                                                        yield 232, subst6
                                                                        # 233: b*log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f1160)
                                                                        yield 233, subst6
                                                                        # 234: b*log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f1161)
                                                                        yield 234, subst6
                                                                        # 231: b*log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52)
                                                                        yield 231, subst6
                                                        subjects828.appendleft(tmp885)
                                            if len(subjects853) >= 1:
                                                tmp887 = []
                                                tmp887.append(subjects853.popleft())
                                                while True:
                                                    if len(tmp887) > 1:
                                                        tmp888 = create_operation_expression(associative1, tmp887)
                                                    elif len(tmp887) == 1:
                                                        tmp888 = tmp887[0]
                                                    else:
                                                        assert False, "Unreachable"
                                                    subst5 = Substitution(subst4)
                                                    try:
                                                        subst5.try_add_variable('i3.1.2.2.2', tmp888)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 19875
                                                        if len(subjects853) == 0:
                                                            pass
                                                            # State 19876
                                                            subst6 = Substitution(subst5)
                                                            try:
                                                                subst6.try_add_variable('i3.1.2.2', 1)
                                                            except ValueError:
                                                                pass
                                                            else:
                                                                pass
                                                                # State 19877
                                                                if len(subjects828) == 0:
                                                                    pass
                                                                    # State 19878
                                                                    if len(subjects781) == 0:
                                                                        pass
                                                                        # State 19879
                                                                        if len(subjects) == 0:
                                                                            pass
                                                                            # 232: b*log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f417)
                                                                            yield 232, subst6
                                                                            # 233: b*log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f1160)
                                                                            yield 233, subst6
                                                                            # 234: b*log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f1161)
                                                                            yield 234, subst6
                                                                            # 231: b*log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52)
                                                                            yield 231, subst6
                                                            if len(subjects828) >= 1:
                                                                tmp891 = subjects828.popleft()
                                                                subst6 = Substitution(subst5)
                                                                try:
                                                                    subst6.try_add_variable('i3.1.2.2', tmp891)
                                                                except ValueError:
                                                                    pass
                                                                else:
                                                                    pass
                                                                    # State 19877
                                                                    if len(subjects828) == 0:
                                                                        pass
                                                                        # State 19878
                                                                        if len(subjects781) == 0:
                                                                            pass
                                                                            # State 19879
                                                                            if len(subjects) == 0:
                                                                                pass
                                                                                # 232: b*log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f417)
                                                                                yield 232, subst6
                                                                                # 233: b*log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f1160)
                                                                                yield 233, subst6
                                                                                # 234: b*log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f1161)
                                                                                yield 234, subst6
                                                                                # 231: b*log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52)
                                                                                yield 231, subst6
                                                                subjects828.appendleft(tmp891)
                                                    if len(subjects853) == 0:
                                                        break
                                                    tmp887.append(subjects853.popleft())
                                                subjects853.extendleft(reversed(tmp887))
                                    subjects853.appendleft(tmp880)
                                subjects828.appendleft(tmp852)
                        if len(subjects828) >= 1:
                            tmp893 = subjects828.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i3.1.2.1', tmp893)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 53185
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i3.1.2.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 53186
                                    if len(subjects828) == 0:
                                        pass
                                        # State 53187
                                        if len(subjects781) == 0:
                                            pass
                                            # State 53188
                                            if len(subjects) == 0:
                                                pass
                                                # 237: b*log(c*RFx**p) /; (cons_f3) and (cons_f8) and (cons_f5) and (cons_f1200)
                                                yield 237, subst4
                                if len(subjects828) >= 1:
                                    tmp896 = subjects828.popleft()
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i3.1.2.2', tmp896)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 53186
                                        if len(subjects828) == 0:
                                            pass
                                            # State 53187
                                            if len(subjects781) == 0:
                                                pass
                                                # State 53188
                                                if len(subjects) == 0:
                                                    pass
                                                    # 237: b*log(c*RFx**p) /; (cons_f3) and (cons_f8) and (cons_f5) and (cons_f1200)
                                                    yield 237, subst4
                                    subjects828.appendleft(tmp896)
                            subjects828.appendleft(tmp893)
                        if len(subjects828) >= 1 and isinstance(subjects828[0], Mul):
                            tmp898 = subjects828.popleft()
                            associative1 = tmp898
                            associative_type1 = type(tmp898)
                            subjects899 = deque(tmp898._args)
                            matcher = CommutativeMatcher19881.get()
                            tmp900 = subjects899
                            subjects899 = []
                            for s in tmp900:
                                matcher.add_subject(s)
                            for pattern_index, subst3 in matcher.match(tmp900, subst2):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 19918
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i3.1.2.2', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 19919
                                        if len(subjects828) == 0:
                                            pass
                                            # State 19920
                                            if len(subjects781) == 0:
                                                pass
                                                # State 19921
                                                if len(subjects) == 0:
                                                    pass
                                                    # 232: b*log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f417)
                                                    yield 232, subst4
                                                    # 233: b*log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f1160)
                                                    yield 233, subst4
                                                    # 234: b*log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f1161)
                                                    yield 234, subst4
                                                    # 231: b*log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52)
                                                    yield 231, subst4
                                    if len(subjects828) >= 1:
                                        tmp902 = []
                                        tmp902.append(subjects828.popleft())
                                        while True:
                                            if len(tmp902) > 1:
                                                tmp903 = create_operation_expression(associative1, tmp902)
                                            elif len(tmp902) == 1:
                                                tmp903 = tmp902[0]
                                            else:
                                                assert False, "Unreachable"
                                            subst4 = Substitution(subst3)
                                            try:
                                                subst4.try_add_variable('i3.1.2.2', tmp903)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 19919
                                                if len(subjects828) == 0:
                                                    pass
                                                    # State 19920
                                                    if len(subjects781) == 0:
                                                        pass
                                                        # State 19921
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 232: b*log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f417)
                                                            yield 232, subst4
                                                            # 233: b*log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f1160)
                                                            yield 233, subst4
                                                            # 234: b*log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f1161)
                                                            yield 234, subst4
                                                            # 231: b*log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52)
                                                            yield 231, subst4
                                            if len(subjects828) == 0:
                                                break
                                            tmp902.append(subjects828.popleft())
                                        subjects828.extendleft(reversed(tmp902))
                            subjects828.appendleft(tmp898)
                        if len(subjects828) >= 1 and isinstance(subjects828[0], Add):
                            tmp905 = subjects828.popleft()
                            associative1 = tmp905
                            associative_type1 = type(tmp905)
                            subjects906 = deque(tmp905._args)
                            matcher = CommutativeMatcher50684.get()
                            tmp907 = subjects906
                            subjects906 = []
                            for s in tmp907:
                                matcher.add_subject(s)
                            for pattern_index, subst3 in matcher.match(tmp907, subst2):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 50697
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i3.1.2.2', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 50698
                                        if len(subjects828) == 0:
                                            pass
                                            # State 50699
                                            if len(subjects781) == 0:
                                                pass
                                                # State 50700
                                                if len(subjects) == 0:
                                                    pass
                                                    # 235: b*log(c*(d + e*x**2)**p) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f5)
                                                    yield 235, subst4
                                    if len(subjects828) >= 1:
                                        tmp909 = []
                                        tmp909.append(subjects828.popleft())
                                        while True:
                                            if len(tmp909) > 1:
                                                tmp910 = create_operation_expression(associative1, tmp909)
                                            elif len(tmp909) == 1:
                                                tmp910 = tmp909[0]
                                            else:
                                                assert False, "Unreachable"
                                            subst4 = Substitution(subst3)
                                            try:
                                                subst4.try_add_variable('i3.1.2.2', tmp910)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 50698
                                                if len(subjects828) == 0:
                                                    pass
                                                    # State 50699
                                                    if len(subjects781) == 0:
                                                        pass
                                                        # State 50700
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 235: b*log(c*(d + e*x**2)**p) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f5)
                                                            yield 235, subst4
                                            if len(subjects828) == 0:
                                                break
                                            tmp909.append(subjects828.popleft())
                                        subjects828.extendleft(reversed(tmp909))
                                if pattern_index == 1:
                                    pass
                                    # State 52807
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i3.1.2.2', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 52808
                                        if len(subjects828) == 0:
                                            pass
                                            # State 52809
                                            if len(subjects781) == 0:
                                                pass
                                                # State 52810
                                                if len(subjects) == 0:
                                                    pass
                                                    # 236: b*log(c*(d + e/(f + x*g))**p) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f210) and (cons_f5)
                                                    yield 236, subst4
                                    if len(subjects828) >= 1:
                                        tmp913 = []
                                        tmp913.append(subjects828.popleft())
                                        while True:
                                            if len(tmp913) > 1:
                                                tmp914 = create_operation_expression(associative1, tmp913)
                                            elif len(tmp913) == 1:
                                                tmp914 = tmp913[0]
                                            else:
                                                assert False, "Unreachable"
                                            subst4 = Substitution(subst3)
                                            try:
                                                subst4.try_add_variable('i3.1.2.2', tmp914)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 52808
                                                if len(subjects828) == 0:
                                                    pass
                                                    # State 52809
                                                    if len(subjects781) == 0:
                                                        pass
                                                        # State 52810
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 236: b*log(c*(d + e/(f + x*g))**p) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f210) and (cons_f5)
                                                            yield 236, subst4
                                            if len(subjects828) == 0:
                                                break
                                            tmp913.append(subjects828.popleft())
                                        subjects828.extendleft(reversed(tmp913))
                            subjects828.appendleft(tmp905)
                        subjects781.appendleft(tmp827)
                if len(subjects781) >= 1 and isinstance(subjects781[0], Mul):
                    tmp916 = subjects781.popleft()
                    associative1 = tmp916
                    associative_type1 = type(tmp916)
                    subjects917 = deque(tmp916._args)
                    matcher = CommutativeMatcher19923.get()
                    tmp918 = subjects917
                    subjects917 = []
                    for s in tmp918:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp918, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 20092
                            if len(subjects781) == 0:
                                pass
                                # State 20093
                                if len(subjects) == 0:
                                    pass
                                    # 232: b*log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f417)
                                    yield 232, subst2
                                    # 233: b*log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f1160)
                                    yield 233, subst2
                                    # 234: b*log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f1161)
                                    yield 234, subst2
                                    # 231: b*log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52)
                                    yield 231, subst2
                        if pattern_index == 1:
                            pass
                            # State 50733
                            if len(subjects781) == 0:
                                pass
                                # State 50734
                                if len(subjects) == 0:
                                    pass
                                    # 235: b*log(c*(d + e*x**2)**p) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f5)
                                    yield 235, subst2
                        if pattern_index == 2:
                            pass
                            # State 52897
                            if len(subjects781) == 0:
                                pass
                                # State 52898
                                if len(subjects) == 0:
                                    pass
                                    # 236: b*log(c*(d + e/(f + x*g))**p) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f210) and (cons_f5)
                                    yield 236, subst2
                        if pattern_index == 3:
                            pass
                            # State 53193
                            if len(subjects781) == 0:
                                pass
                                # State 53194
                                if len(subjects) == 0:
                                    pass
                                    # 237: b*log(c*RFx**p) /; (cons_f3) and (cons_f8) and (cons_f5) and (cons_f1200)
                                    yield 237, subst2
                    subjects781.appendleft(tmp916)
                subjects.appendleft(tmp780)
            if len(subjects) >= 1 and subjects[0] == LambertW(Add(Symbol('a'), Mul(Symbol('b'), Symbol('x')))):
                tmp919 = subjects.popleft()
                # State 56773
                if len(subjects) == 0:
                    pass
                    # 238: d*LambertW(a + b*x) /; (cons_f29) and (cons_f1767)
                    yield 238, subst1
                subjects.appendleft(tmp919)
            if len(subjects) >= 1 and subjects[0] == LambertW(Mul(Symbol('a'), Pow(Symbol('x'), Symbol('n')))):
                tmp920 = subjects.popleft()
                # State 56842
                if len(subjects) == 0:
                    pass
                    # 239: d*LambertW(a*x**n) /; (cons_f29)
                    yield 239, subst1
                subjects.appendleft(tmp920)
            if len(subjects) >= 1 and isinstance(subjects[0], sin):
                tmp921 = subjects.popleft()
                subjects922 = deque(tmp921._args)
                # State 58072
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i3.1.2.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 58073
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i3.1.2.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 58074
                        if len(subjects922) >= 1:
                            tmp925 = subjects922.popleft()
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i3.1.2.1.0', tmp925)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 58075
                                if len(subjects922) == 0:
                                    pass
                                    # State 58076
                                    if len(subjects) == 0:
                                        pass
                                        # 256: b*sin(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1269) and (cons_f1274)
                                        yield 256, subst4
                                        # 257: b*sin(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f1269)
                                        yield 257, subst4
                                        # 240: b*sin(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1266)
                                        yield 240, subst4
                                        # 242: b*sin(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f1267)
                                        yield 242, subst4
                                        # 244: b*sin(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1267)
                                        yield 244, subst4
                                        # 246: b*sin(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1269) and (cons_f1270)
                                        yield 246, subst4
                                        # 248: b*sin(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1269) and (cons_f1271)
                                        yield 248, subst4
                                        # 250: b*sin(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1269) and (cons_f1272)
                                        yield 250, subst4
                                        # 252: b*sin(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1269)
                                        yield 252, subst4
                                        # 254: b*sin(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1273)
                                        yield 254, subst4
                            subjects922.appendleft(tmp925)
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i3.1.2.1.0', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 72718
                        if len(subjects922) >= 1 and isinstance(subjects922[0], Pow):
                            tmp928 = subjects922.popleft()
                            subjects929 = deque(tmp928._args)
                            # State 72719
                            if len(subjects929) >= 1:
                                tmp930 = subjects929.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i3.1.2.1.1', tmp930)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 72720
                                    if len(subjects929) >= 1:
                                        tmp932 = subjects929.popleft()
                                        subst5 = Substitution(subst4)
                                        try:
                                            subst5.try_add_variable('i3.1.2.1.2', tmp932)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 72721
                                            if len(subjects929) == 0:
                                                pass
                                                # State 72722
                                                if len(subjects922) == 0:
                                                    pass
                                                    # State 72723
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 320: b*sin(c + d*x**n) /; (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f70) and (cons_f71)
                                                        yield 320, subst5
                                                        # 322: b*sin(c + d*x**n) /; (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f70)
                                                        yield 322, subst5
                                                        # 312: b*sin(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f378) and (cons_f167)
                                                        yield 312, subst5
                                                        # 314: b*sin(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f198)
                                                        yield 314, subst5
                                                        # 316: b*sin(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f491)
                                                        yield 316, subst5
                                                        # 318: b*sin(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4)
                                                        yield 318, subst5
                                        subjects929.appendleft(tmp932)
                                subjects929.appendleft(tmp930)
                            subjects922.appendleft(tmp928)
                    if len(subjects922) >= 1 and isinstance(subjects922[0], Mul):
                        tmp934 = subjects922.popleft()
                        associative1 = tmp934
                        associative_type1 = type(tmp934)
                        subjects935 = deque(tmp934._args)
                        matcher = CommutativeMatcher58078.get()
                        tmp936 = subjects935
                        subjects935 = []
                        for s in tmp936:
                            matcher.add_subject(s)
                        for pattern_index, subst3 in matcher.match(tmp936, subst2):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 58079
                                if len(subjects922) == 0:
                                    pass
                                    # State 58080
                                    if len(subjects) == 0:
                                        pass
                                        # 256: b*sin(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1269) and (cons_f1274)
                                        yield 256, subst3
                                        # 257: b*sin(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f1269)
                                        yield 257, subst3
                                        # 240: b*sin(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1266)
                                        yield 240, subst3
                                        # 242: b*sin(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f1267)
                                        yield 242, subst3
                                        # 244: b*sin(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1267)
                                        yield 244, subst3
                                        # 246: b*sin(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1269) and (cons_f1270)
                                        yield 246, subst3
                                        # 248: b*sin(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1269) and (cons_f1271)
                                        yield 248, subst3
                                        # 250: b*sin(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1269) and (cons_f1272)
                                        yield 250, subst3
                                        # 252: b*sin(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1269)
                                        yield 252, subst3
                                        # 254: b*sin(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1273)
                                        yield 254, subst3
                            if pattern_index == 1:
                                pass
                                # State 72728
                                if len(subjects922) == 0:
                                    pass
                                    # State 72729
                                    if len(subjects) == 0:
                                        pass
                                        # 320: b*sin(c + d*x**n) /; (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f70) and (cons_f71)
                                        yield 320, subst3
                                        # 322: b*sin(c + d*x**n) /; (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f70)
                                        yield 322, subst3
                                        # 312: b*sin(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f378) and (cons_f167)
                                        yield 312, subst3
                                        # 314: b*sin(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f198)
                                        yield 314, subst3
                                        # 316: b*sin(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f491)
                                        yield 316, subst3
                                        # 318: b*sin(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4)
                                        yield 318, subst3
                        subjects922.appendleft(tmp934)
                if len(subjects922) >= 1:
                    tmp937 = subjects922.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i3.1.1', tmp937)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 73531
                        if len(subjects922) == 0:
                            pass
                            # State 73532
                            if len(subjects) == 0:
                                pass
                                # 324: b*sin(u) /; (cons_f3) and (cons_f825) and (cons_f826)
                                yield 324, subst2
                    subjects922.appendleft(tmp937)
                if len(subjects922) >= 1 and isinstance(subjects922[0], Add):
                    tmp939 = subjects922.popleft()
                    associative1 = tmp939
                    associative_type1 = type(tmp939)
                    subjects940 = deque(tmp939._args)
                    matcher = CommutativeMatcher58082.get()
                    tmp941 = subjects940
                    subjects940 = []
                    for s in tmp941:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp941, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 58088
                            if len(subjects922) == 0:
                                pass
                                # State 58089
                                if len(subjects) == 0:
                                    pass
                                    # 256: b*sin(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1269) and (cons_f1274)
                                    yield 256, subst2
                                    # 257: b*sin(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f1269)
                                    yield 257, subst2
                                    # 240: b*sin(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1266)
                                    yield 240, subst2
                                    # 242: b*sin(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f1267)
                                    yield 242, subst2
                                    # 244: b*sin(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1267)
                                    yield 244, subst2
                                    # 246: b*sin(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1269) and (cons_f1270)
                                    yield 246, subst2
                                    # 248: b*sin(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1269) and (cons_f1271)
                                    yield 248, subst2
                                    # 250: b*sin(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1269) and (cons_f1272)
                                    yield 250, subst2
                                    # 252: b*sin(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1269)
                                    yield 252, subst2
                                    # 254: b*sin(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1273)
                                    yield 254, subst2
                        if pattern_index == 1:
                            pass
                            # State 72740
                            if len(subjects922) == 0:
                                pass
                                # State 72741
                                if len(subjects) == 0:
                                    pass
                                    # 320: b*sin(c + d*x**n) /; (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f70) and (cons_f71)
                                    yield 320, subst2
                                    # 322: b*sin(c + d*x**n) /; (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f70)
                                    yield 322, subst2
                                    # 312: b*sin(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f378) and (cons_f167)
                                    yield 312, subst2
                                    # 314: b*sin(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f198)
                                    yield 314, subst2
                                    # 316: b*sin(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f491)
                                    yield 316, subst2
                                    # 318: b*sin(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4)
                                    yield 318, subst2
                    subjects922.appendleft(tmp939)
                subjects.appendleft(tmp921)
            if len(subjects) >= 1 and isinstance(subjects[0], cos):
                tmp942 = subjects.popleft()
                subjects943 = deque(tmp942._args)
                # State 58114
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i3.1.2.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 58115
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i3.1.2.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 58116
                        if len(subjects943) >= 1:
                            tmp946 = subjects943.popleft()
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i3.1.2.1.0', tmp946)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 58117
                                if len(subjects943) == 0:
                                    pass
                                    # State 58118
                                    if len(subjects) == 0:
                                        pass
                                        # 258: b*cos(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f1269)
                                        yield 258, subst4
                                        # 260: a*cos(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f1441)
                                        yield 260, subst4
                                        # 262: a*cos(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1442)
                                        yield 262, subst4
                                        # 264: a*cos(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f1446)
                                        yield 264, subst4
                                        # 266: a*cos(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f1447)
                                        yield 266, subst4
                                        # 268: a*cos(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f1450)
                                        yield 268, subst4
                                        # 270: a*cos(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f1451)
                                        yield 270, subst4
                                        # 272: a*cos(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f1452) and (cons_f1453)
                                        yield 272, subst4
                                        # 274: a*cos(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f1454) and (cons_f1452) and (cons_f1455)
                                        yield 274, subst4
                                        # 276: a*cos(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f1454)
                                        yield 276, subst4
                                        # 278: a*cos(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f1456)
                                        yield 278, subst4
                                        # 280: a*cos(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50)
                                        yield 280, subst4
                                        # 282: a*cos(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f1458)
                                        yield 282, subst4
                                        # 241: b*cos(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1266)
                                        yield 241, subst4
                                        # 243: b*cos(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f1267)
                                        yield 243, subst4
                                        # 245: b*cos(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1267)
                                        yield 245, subst4
                                        # 247: b*cos(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1269) and (cons_f1270)
                                        yield 247, subst4
                                        # 249: b*cos(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1269) and (cons_f1271)
                                        yield 249, subst4
                                        # 251: b*cos(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1269) and (cons_f1272)
                                        yield 251, subst4
                                        # 253: b*cos(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1269)
                                        yield 253, subst4
                                        # 255: b*cos(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1273)
                                        yield 255, subst4
                            subjects943.appendleft(tmp946)
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i3.1.2.1.0', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 72853
                        if len(subjects943) >= 1 and isinstance(subjects943[0], Pow):
                            tmp949 = subjects943.popleft()
                            subjects950 = deque(tmp949._args)
                            # State 72854
                            if len(subjects950) >= 1:
                                tmp951 = subjects950.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i3.1.2.1.1', tmp951)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 72855
                                    if len(subjects950) >= 1:
                                        tmp953 = subjects950.popleft()
                                        subst5 = Substitution(subst4)
                                        try:
                                            subst5.try_add_variable('i3.1.2.1.2', tmp953)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 72856
                                            if len(subjects950) == 0:
                                                pass
                                                # State 72857
                                                if len(subjects943) == 0:
                                                    pass
                                                    # State 72858
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 321: b*cos(c + d*x**n) /; (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f70) and (cons_f71)
                                                        yield 321, subst5
                                                        # 323: b*cos(c + d*x**n) /; (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f70)
                                                        yield 323, subst5
                                                        # 313: b*cos(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f378) and (cons_f167)
                                                        yield 313, subst5
                                                        # 315: b*cos(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f198)
                                                        yield 315, subst5
                                                        # 317: b*cos(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f491)
                                                        yield 317, subst5
                                                        # 319: b*cos(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4)
                                                        yield 319, subst5
                                        subjects950.appendleft(tmp953)
                                subjects950.appendleft(tmp951)
                            subjects943.appendleft(tmp949)
                    if len(subjects943) >= 1 and isinstance(subjects943[0], Mul):
                        tmp955 = subjects943.popleft()
                        associative1 = tmp955
                        associative_type1 = type(tmp955)
                        subjects956 = deque(tmp955._args)
                        matcher = CommutativeMatcher58120.get()
                        tmp957 = subjects956
                        subjects956 = []
                        for s in tmp957:
                            matcher.add_subject(s)
                        for pattern_index, subst3 in matcher.match(tmp957, subst2):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 58121
                                if len(subjects943) == 0:
                                    pass
                                    # State 58122
                                    if len(subjects) == 0:
                                        pass
                                        # 258: b*cos(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f1269)
                                        yield 258, subst3
                                        # 260: a*cos(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f1441)
                                        yield 260, subst3
                                        # 262: a*cos(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1442)
                                        yield 262, subst3
                                        # 264: a*cos(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f1446)
                                        yield 264, subst3
                                        # 266: a*cos(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f1447)
                                        yield 266, subst3
                                        # 268: a*cos(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f1450)
                                        yield 268, subst3
                                        # 270: a*cos(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f1451)
                                        yield 270, subst3
                                        # 272: a*cos(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f1452) and (cons_f1453)
                                        yield 272, subst3
                                        # 274: a*cos(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f1454) and (cons_f1452) and (cons_f1455)
                                        yield 274, subst3
                                        # 276: a*cos(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f1454)
                                        yield 276, subst3
                                        # 278: a*cos(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f1456)
                                        yield 278, subst3
                                        # 280: a*cos(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50)
                                        yield 280, subst3
                                        # 282: a*cos(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f1458)
                                        yield 282, subst3
                                        # 241: b*cos(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1266)
                                        yield 241, subst3
                                        # 243: b*cos(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f1267)
                                        yield 243, subst3
                                        # 245: b*cos(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1267)
                                        yield 245, subst3
                                        # 247: b*cos(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1269) and (cons_f1270)
                                        yield 247, subst3
                                        # 249: b*cos(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1269) and (cons_f1271)
                                        yield 249, subst3
                                        # 251: b*cos(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1269) and (cons_f1272)
                                        yield 251, subst3
                                        # 253: b*cos(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1269)
                                        yield 253, subst3
                                        # 255: b*cos(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1273)
                                        yield 255, subst3
                            if pattern_index == 1:
                                pass
                                # State 72863
                                if len(subjects943) == 0:
                                    pass
                                    # State 72864
                                    if len(subjects) == 0:
                                        pass
                                        # 321: b*cos(c + d*x**n) /; (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f70) and (cons_f71)
                                        yield 321, subst3
                                        # 323: b*cos(c + d*x**n) /; (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f70)
                                        yield 323, subst3
                                        # 313: b*cos(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f378) and (cons_f167)
                                        yield 313, subst3
                                        # 315: b*cos(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f198)
                                        yield 315, subst3
                                        # 317: b*cos(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f491)
                                        yield 317, subst3
                                        # 319: b*cos(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4)
                                        yield 319, subst3
                        subjects943.appendleft(tmp955)
                if len(subjects943) >= 1:
                    tmp958 = subjects943.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i3.1.1', tmp958)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 73571
                        if len(subjects943) == 0:
                            pass
                            # State 73572
                            if len(subjects) == 0:
                                pass
                                # 325: b*cos(u) /; (cons_f3) and (cons_f825) and (cons_f826)
                                yield 325, subst2
                    subjects943.appendleft(tmp958)
                if len(subjects943) >= 1 and isinstance(subjects943[0], Add):
                    tmp960 = subjects943.popleft()
                    associative1 = tmp960
                    associative_type1 = type(tmp960)
                    subjects961 = deque(tmp960._args)
                    matcher = CommutativeMatcher58124.get()
                    tmp962 = subjects961
                    subjects961 = []
                    for s in tmp962:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp962, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 58130
                            if len(subjects943) == 0:
                                pass
                                # State 58131
                                if len(subjects) == 0:
                                    pass
                                    # 258: b*cos(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f1269)
                                    yield 258, subst2
                                    # 260: a*cos(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f1441)
                                    yield 260, subst2
                                    # 262: a*cos(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1442)
                                    yield 262, subst2
                                    # 264: a*cos(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f1446)
                                    yield 264, subst2
                                    # 266: a*cos(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f1447)
                                    yield 266, subst2
                                    # 268: a*cos(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f1450)
                                    yield 268, subst2
                                    # 270: a*cos(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f1451)
                                    yield 270, subst2
                                    # 272: a*cos(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f1452) and (cons_f1453)
                                    yield 272, subst2
                                    # 274: a*cos(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f1454) and (cons_f1452) and (cons_f1455)
                                    yield 274, subst2
                                    # 276: a*cos(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f1454)
                                    yield 276, subst2
                                    # 278: a*cos(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f1456)
                                    yield 278, subst2
                                    # 280: a*cos(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50)
                                    yield 280, subst2
                                    # 282: a*cos(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f1458)
                                    yield 282, subst2
                                    # 241: b*cos(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1266)
                                    yield 241, subst2
                                    # 243: b*cos(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f1267)
                                    yield 243, subst2
                                    # 245: b*cos(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1267)
                                    yield 245, subst2
                                    # 247: b*cos(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1269) and (cons_f1270)
                                    yield 247, subst2
                                    # 249: b*cos(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1269) and (cons_f1271)
                                    yield 249, subst2
                                    # 251: b*cos(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1269) and (cons_f1272)
                                    yield 251, subst2
                                    # 253: b*cos(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1269)
                                    yield 253, subst2
                                    # 255: b*cos(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1273)
                                    yield 255, subst2
                        if pattern_index == 1:
                            pass
                            # State 72875
                            if len(subjects943) == 0:
                                pass
                                # State 72876
                                if len(subjects) == 0:
                                    pass
                                    # 321: b*cos(c + d*x**n) /; (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f70) and (cons_f71)
                                    yield 321, subst2
                                    # 323: b*cos(c + d*x**n) /; (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f70)
                                    yield 323, subst2
                                    # 313: b*cos(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f378) and (cons_f167)
                                    yield 313, subst2
                                    # 315: b*cos(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f198)
                                    yield 315, subst2
                                    # 317: b*cos(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f491)
                                    yield 317, subst2
                                    # 319: b*cos(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4)
                                    yield 319, subst2
                    subjects943.appendleft(tmp960)
                subjects.appendleft(tmp942)
            if len(subjects) >= 1 and isinstance(subjects[0], tan):
                tmp963 = subjects.popleft()
                subjects964 = deque(tmp963._args)
                # State 77451
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i3.1.2.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 77452
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i3.1.2.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 77453
                        if len(subjects964) >= 1:
                            tmp967 = subjects964.popleft()
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i3.1.2.1.0', tmp967)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 77454
                                if len(subjects964) == 0:
                                    pass
                                    # State 77455
                                    if len(subjects) == 0:
                                        pass
                                        # 326: b*tan(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1266)
                                        yield 326, subst4
                                        # 328: b*tan(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1441)
                                        yield 328, subst4
                                        # 330: b*tan(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f1441)
                                        yield 330, subst4
                                        # 332: b*tan(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1442)
                                        yield 332, subst4
                                        # 334: b*tan(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f1442)
                                        yield 334, subst4
                            subjects964.appendleft(tmp967)
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i3.1.2.1.0', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 87309
                        if len(subjects964) >= 1 and isinstance(subjects964[0], Pow):
                            tmp970 = subjects964.popleft()
                            subjects971 = deque(tmp970._args)
                            # State 87310
                            if len(subjects971) >= 1:
                                tmp972 = subjects971.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i3.1.2.1.1', tmp972)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 87311
                                    if len(subjects971) >= 1:
                                        tmp974 = subjects971.popleft()
                                        subst5 = Substitution(subst4)
                                        try:
                                            subst5.try_add_variable('i3.1.2.1.2', tmp974)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 87312
                                            if len(subjects971) == 0:
                                                pass
                                                # State 87313
                                                if len(subjects964) == 0:
                                                    pass
                                                    # State 87314
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 352: b*tan(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f5) and (cons_f1497)
                                                        yield 352, subst5
                                                        # 354: b*tan(c + d*x**n) /; (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f70) and (cons_f71)
                                                        yield 354, subst5
                                                        # 350: b*tan(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f5) and (cons_f1575)
                                                        yield 350, subst5
                                        subjects971.appendleft(tmp974)
                                subjects971.appendleft(tmp972)
                            subjects964.appendleft(tmp970)
                    if len(subjects964) >= 1 and isinstance(subjects964[0], Mul):
                        tmp976 = subjects964.popleft()
                        associative1 = tmp976
                        associative_type1 = type(tmp976)
                        subjects977 = deque(tmp976._args)
                        matcher = CommutativeMatcher77457.get()
                        tmp978 = subjects977
                        subjects977 = []
                        for s in tmp978:
                            matcher.add_subject(s)
                        for pattern_index, subst3 in matcher.match(tmp978, subst2):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 77458
                                if len(subjects964) == 0:
                                    pass
                                    # State 77459
                                    if len(subjects) == 0:
                                        pass
                                        # 326: b*tan(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1266)
                                        yield 326, subst3
                                        # 328: b*tan(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1441)
                                        yield 328, subst3
                                        # 330: b*tan(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f1441)
                                        yield 330, subst3
                                        # 332: b*tan(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1442)
                                        yield 332, subst3
                                        # 334: b*tan(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f1442)
                                        yield 334, subst3
                            if pattern_index == 1:
                                pass
                                # State 87319
                                if len(subjects964) == 0:
                                    pass
                                    # State 87320
                                    if len(subjects) == 0:
                                        pass
                                        # 352: b*tan(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f5) and (cons_f1497)
                                        yield 352, subst3
                                        # 354: b*tan(c + d*x**n) /; (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f70) and (cons_f71)
                                        yield 354, subst3
                                        # 350: b*tan(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f5) and (cons_f1575)
                                        yield 350, subst3
                        subjects964.appendleft(tmp976)
                if len(subjects964) >= 1:
                    tmp979 = subjects964.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i3.1.1', tmp979)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 87869
                        if len(subjects964) == 0:
                            pass
                            # State 87870
                            if len(subjects) == 0:
                                pass
                                # 356: b*tan(u) /; (cons_f3) and (cons_f825) and (cons_f826)
                                yield 356, subst2
                    subjects964.appendleft(tmp979)
                if len(subjects964) >= 1 and isinstance(subjects964[0], Add):
                    tmp981 = subjects964.popleft()
                    associative1 = tmp981
                    associative_type1 = type(tmp981)
                    subjects982 = deque(tmp981._args)
                    matcher = CommutativeMatcher77461.get()
                    tmp983 = subjects982
                    subjects982 = []
                    for s in tmp983:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp983, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 77467
                            if len(subjects964) == 0:
                                pass
                                # State 77468
                                if len(subjects) == 0:
                                    pass
                                    # 326: b*tan(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1266)
                                    yield 326, subst2
                                    # 328: b*tan(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1441)
                                    yield 328, subst2
                                    # 330: b*tan(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f1441)
                                    yield 330, subst2
                                    # 332: b*tan(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1442)
                                    yield 332, subst2
                                    # 334: b*tan(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f1442)
                                    yield 334, subst2
                        if pattern_index == 1:
                            pass
                            # State 87331
                            if len(subjects964) == 0:
                                pass
                                # State 87332
                                if len(subjects) == 0:
                                    pass
                                    # 352: b*tan(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f5) and (cons_f1497)
                                    yield 352, subst2
                                    # 354: b*tan(c + d*x**n) /; (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f70) and (cons_f71)
                                    yield 354, subst2
                                    # 350: b*tan(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f5) and (cons_f1575)
                                    yield 350, subst2
                    subjects964.appendleft(tmp981)
                subjects.appendleft(tmp963)
            if len(subjects) >= 1 and isinstance(subjects[0], asin):
                tmp984 = subjects.popleft()
                subjects985 = deque(tmp984._args)
                # State 108027
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i3.1.2.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 108028
                    if len(subjects985) >= 1:
                        tmp987 = subjects985.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i3.1.2.0', tmp987)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 108029
                            if len(subjects985) == 0:
                                pass
                                # State 108030
                                if len(subjects) == 0:
                                    pass
                                    # 395: b*asin(x*c) /; (cons_f2) and (cons_f3) and (cons_f8)
                                    yield 395, subst3
                                    # 397: b*asin(x*c) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f1581)
                                    yield 397, subst3
                        subjects985.appendleft(tmp987)
                if len(subjects985) >= 1 and isinstance(subjects985[0], Mul):
                    tmp989 = subjects985.popleft()
                    associative1 = tmp989
                    associative_type1 = type(tmp989)
                    subjects990 = deque(tmp989._args)
                    matcher = CommutativeMatcher108032.get()
                    tmp991 = subjects990
                    subjects990 = []
                    for s in tmp991:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp991, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 108033
                            if len(subjects985) == 0:
                                pass
                                # State 108034
                                if len(subjects) == 0:
                                    pass
                                    # 395: b*asin(x*c) /; (cons_f2) and (cons_f3) and (cons_f8)
                                    yield 395, subst2
                                    # 397: b*asin(x*c) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f1581)
                                    yield 397, subst2
                    subjects985.appendleft(tmp989)
                if len(subjects985) >= 1 and isinstance(subjects985[0], Add):
                    tmp992 = subjects985.popleft()
                    associative1 = tmp992
                    associative_type1 = type(tmp992)
                    subjects993 = deque(tmp992._args)
                    matcher = CommutativeMatcher110327.get()
                    tmp994 = subjects993
                    subjects993 = []
                    for s in tmp994:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp994, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 110333
                            if len(subjects985) == 0:
                                pass
                                # State 110334
                                if len(subjects) == 0:
                                    pass
                                    # 399: b*asin(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f1275)
                                    yield 399, subst2
                        if pattern_index == 1:
                            pass
                            # State 110716
                            if len(subjects985) == 0:
                                pass
                                # State 110717
                                if len(subjects) == 0:
                                    pass
                                    # 401: b*asin(c + d*x**2) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1766)
                                    yield 401, subst2
                    subjects985.appendleft(tmp992)
                subjects.appendleft(tmp984)
            if len(subjects) >= 1 and isinstance(subjects[0], acos):
                tmp995 = subjects.popleft()
                subjects996 = deque(tmp995._args)
                # State 108121
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i3.1.2.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 108122
                    if len(subjects996) >= 1:
                        tmp998 = subjects996.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i3.1.2.0', tmp998)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 108123
                            if len(subjects996) == 0:
                                pass
                                # State 108124
                                if len(subjects) == 0:
                                    pass
                                    # 396: b*acos(x*c) /; (cons_f2) and (cons_f3) and (cons_f8)
                                    yield 396, subst3
                                    # 398: b*acos(x*c) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f1581)
                                    yield 398, subst3
                        subjects996.appendleft(tmp998)
                if len(subjects996) >= 1 and isinstance(subjects996[0], Mul):
                    tmp1000 = subjects996.popleft()
                    associative1 = tmp1000
                    associative_type1 = type(tmp1000)
                    subjects1001 = deque(tmp1000._args)
                    matcher = CommutativeMatcher108126.get()
                    tmp1002 = subjects1001
                    subjects1001 = []
                    for s in tmp1002:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp1002, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 108127
                            if len(subjects996) == 0:
                                pass
                                # State 108128
                                if len(subjects) == 0:
                                    pass
                                    # 396: b*acos(x*c) /; (cons_f2) and (cons_f3) and (cons_f8)
                                    yield 396, subst2
                                    # 398: b*acos(x*c) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f1581)
                                    yield 398, subst2
                    subjects996.appendleft(tmp1000)
                if len(subjects996) >= 1 and isinstance(subjects996[0], Add):
                    tmp1003 = subjects996.popleft()
                    associative1 = tmp1003
                    associative_type1 = type(tmp1003)
                    subjects1004 = deque(tmp1003._args)
                    matcher = CommutativeMatcher110423.get()
                    tmp1005 = subjects1004
                    subjects1004 = []
                    for s in tmp1005:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp1005, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 110429
                            if len(subjects996) == 0:
                                pass
                                # State 110430
                                if len(subjects) == 0:
                                    pass
                                    # 400: b*acos(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f1275)
                                    yield 400, subst2
                        if pattern_index == 1:
                            pass
                            # State 110782
                            if len(subjects996) == 0:
                                pass
                                # State 110783
                                if len(subjects) == 0:
                                    pass
                                    # 402: b*acos(d*x**2 + 1) /; (cons_f2) and (cons_f3) and (cons_f29) and (cons_f1767)
                                    yield 402, subst2
                        if pattern_index == 2:
                            pass
                            # State 110819
                            if len(subjects996) == 0:
                                pass
                                # State 110820
                                if len(subjects) == 0:
                                    pass
                                    # 403: b*acos(d*x**2 - 1) /; (cons_f2) and (cons_f3) and (cons_f29) and (cons_f1767)
                                    yield 403, subst2
                        if pattern_index == 3:
                            pass
                            # State 110855
                            if len(subjects996) == 0:
                                pass
                                # State 110856
                                if len(subjects) == 0:
                                    pass
                                    # 404: b*acos(c + d*x**2) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1766)
                                    yield 404, subst2
                    subjects996.appendleft(tmp1003)
                subjects.appendleft(tmp995)
            if len(subjects) >= 1 and isinstance(subjects[0], atan):
                tmp1006 = subjects.popleft()
                subjects1007 = deque(tmp1006._args)
                # State 112662
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i3.1.2.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 112663
                    if len(subjects1007) >= 1:
                        tmp1009 = subjects1007.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i3.1.2.0', tmp1009)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 112664
                            if len(subjects1007) == 0:
                                pass
                                # State 112665
                                if len(subjects) == 0:
                                    pass
                                    # 405: b*atan(x*c) /; (cons_f2) and (cons_f3) and (cons_f8)
                                    yield 405, subst3
                                    # 407: b*atan(x*c) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4)
                                    yield 407, subst3
                        subjects1007.appendleft(tmp1009)
                if len(subjects1007) >= 1 and isinstance(subjects1007[0], Mul):
                    tmp1011 = subjects1007.popleft()
                    associative1 = tmp1011
                    associative_type1 = type(tmp1011)
                    subjects1012 = deque(tmp1011._args)
                    matcher = CommutativeMatcher112667.get()
                    tmp1013 = subjects1012
                    subjects1012 = []
                    for s in tmp1013:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp1013, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 112668
                            if len(subjects1007) == 0:
                                pass
                                # State 112669
                                if len(subjects) == 0:
                                    pass
                                    # 405: b*atan(x*c) /; (cons_f2) and (cons_f3) and (cons_f8)
                                    yield 405, subst2
                                    # 407: b*atan(x*c) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4)
                                    yield 407, subst2
                    subjects1007.appendleft(tmp1011)
                if len(subjects1007) >= 1 and isinstance(subjects1007[0], Add):
                    tmp1014 = subjects1007.popleft()
                    associative1 = tmp1014
                    associative_type1 = type(tmp1014)
                    subjects1015 = deque(tmp1014._args)
                    matcher = CommutativeMatcher115525.get()
                    tmp1016 = subjects1015
                    subjects1015 = []
                    for s in tmp1016:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp1016, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 115531
                            if len(subjects1007) == 0:
                                pass
                                # State 115532
                                if len(subjects) == 0:
                                    pass
                                    # 409: b*atan(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29)
                                    yield 409, subst2
                                    # 411: b*atan(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4)
                                    yield 411, subst2
                    subjects1007.appendleft(tmp1014)
                subjects.appendleft(tmp1006)
            if len(subjects) >= 1 and isinstance(subjects[0], acot):
                tmp1017 = subjects.popleft()
                subjects1018 = deque(tmp1017._args)
                # State 112756
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i3.1.2.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 112757
                    if len(subjects1018) >= 1:
                        tmp1020 = subjects1018.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i3.1.2.0', tmp1020)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 112758
                            if len(subjects1018) == 0:
                                pass
                                # State 112759
                                if len(subjects) == 0:
                                    pass
                                    # 408: b*acot(x*c) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4)
                                    yield 408, subst3
                                    # 406: b*acot(x*c) /; (cons_f2) and (cons_f3) and (cons_f8)
                                    yield 406, subst3
                        subjects1018.appendleft(tmp1020)
                if len(subjects1018) >= 1 and isinstance(subjects1018[0], Mul):
                    tmp1022 = subjects1018.popleft()
                    associative1 = tmp1022
                    associative_type1 = type(tmp1022)
                    subjects1023 = deque(tmp1022._args)
                    matcher = CommutativeMatcher112761.get()
                    tmp1024 = subjects1023
                    subjects1023 = []
                    for s in tmp1024:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp1024, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 112762
                            if len(subjects1018) == 0:
                                pass
                                # State 112763
                                if len(subjects) == 0:
                                    pass
                                    # 408: b*acot(x*c) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4)
                                    yield 408, subst2
                                    # 406: b*acot(x*c) /; (cons_f2) and (cons_f3) and (cons_f8)
                                    yield 406, subst2
                    subjects1018.appendleft(tmp1022)
                if len(subjects1018) >= 1 and isinstance(subjects1018[0], Add):
                    tmp1025 = subjects1018.popleft()
                    associative1 = tmp1025
                    associative_type1 = type(tmp1025)
                    subjects1026 = deque(tmp1025._args)
                    matcher = CommutativeMatcher115621.get()
                    tmp1027 = subjects1026
                    subjects1026 = []
                    for s in tmp1027:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp1027, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 115627
                            if len(subjects1018) == 0:
                                pass
                                # State 115628
                                if len(subjects) == 0:
                                    pass
                                    # 410: b*acot(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29)
                                    yield 410, subst2
                                    # 412: b*acot(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4)
                                    yield 412, subst2
                    subjects1018.appendleft(tmp1025)
                subjects.appendleft(tmp1017)
            if len(subjects) >= 1 and isinstance(subjects[0], asec):
                tmp1028 = subjects.popleft()
                subjects1029 = deque(tmp1028._args)
                # State 119556
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i3.1.2.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 119557
                    if len(subjects1029) >= 1:
                        tmp1031 = subjects1029.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i3.1.2.0', tmp1031)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 119558
                            if len(subjects1029) == 0:
                                pass
                                # State 119559
                                if len(subjects) == 0:
                                    pass
                                    # 413: b*asec(x*c) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f1581)
                                    yield 413, subst3
                        subjects1029.appendleft(tmp1031)
                if len(subjects1029) >= 1 and isinstance(subjects1029[0], Mul):
                    tmp1033 = subjects1029.popleft()
                    associative1 = tmp1033
                    associative_type1 = type(tmp1033)
                    subjects1034 = deque(tmp1033._args)
                    matcher = CommutativeMatcher119561.get()
                    tmp1035 = subjects1034
                    subjects1034 = []
                    for s in tmp1035:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp1035, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 119562
                            if len(subjects1029) == 0:
                                pass
                                # State 119563
                                if len(subjects) == 0:
                                    pass
                                    # 413: b*asec(x*c) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f1581)
                                    yield 413, subst2
                    subjects1029.appendleft(tmp1033)
                subjects.appendleft(tmp1028)
            if len(subjects) >= 1 and isinstance(subjects[0], acsc):
                tmp1036 = subjects.popleft()
                subjects1037 = deque(tmp1036._args)
                # State 119607
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i3.1.2.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 119608
                    if len(subjects1037) >= 1:
                        tmp1039 = subjects1037.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i3.1.2.0', tmp1039)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 119609
                            if len(subjects1037) == 0:
                                pass
                                # State 119610
                                if len(subjects) == 0:
                                    pass
                                    # 414: b*acsc(x*c) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f1581)
                                    yield 414, subst3
                        subjects1037.appendleft(tmp1039)
                if len(subjects1037) >= 1 and isinstance(subjects1037[0], Mul):
                    tmp1041 = subjects1037.popleft()
                    associative1 = tmp1041
                    associative_type1 = type(tmp1041)
                    subjects1042 = deque(tmp1041._args)
                    matcher = CommutativeMatcher119612.get()
                    tmp1043 = subjects1042
                    subjects1042 = []
                    for s in tmp1043:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp1043, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 119613
                            if len(subjects1037) == 0:
                                pass
                                # State 119614
                                if len(subjects) == 0:
                                    pass
                                    # 414: b*acsc(x*c) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f1581)
                                    yield 414, subst2
                    subjects1037.appendleft(tmp1041)
                subjects.appendleft(tmp1036)
            if len(subjects) >= 1 and isinstance(subjects[0], sinh):
                tmp1044 = subjects.popleft()
                subjects1045 = deque(tmp1044._args)
                # State 122547
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i3.1.2.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 122548
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i3.1.2.1.0', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 122549
                        if len(subjects1045) >= 1 and isinstance(subjects1045[0], Pow):
                            tmp1048 = subjects1045.popleft()
                            subjects1049 = deque(tmp1048._args)
                            # State 122550
                            if len(subjects1049) >= 1:
                                tmp1050 = subjects1049.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i3.1.2.1.1', tmp1050)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 122551
                                    if len(subjects1049) >= 1:
                                        tmp1052 = subjects1049.popleft()
                                        subst5 = Substitution(subst4)
                                        try:
                                            subst5.try_add_variable('i3.1.2.1.2', tmp1052)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 122552
                                            if len(subjects1049) == 0:
                                                pass
                                                # State 122553
                                                if len(subjects1045) == 0:
                                                    pass
                                                    # State 122554
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 417: b*sinh(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f198)
                                                        yield 417, subst5
                                                        # 419: b*sinh(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f491)
                                                        yield 419, subst5
                                                        # 421: b*sinh(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4)
                                                        yield 421, subst5
                                                        # 423: b*sinh(c + d*x**n) /; (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f70) and (cons_f71)
                                                        yield 423, subst5
                                                        # 425: b*sinh(c + d*x**n) /; (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f70)
                                                        yield 425, subst5
                                                        # 415: b*sinh(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f378) and (cons_f167)
                                                        yield 415, subst5
                                        subjects1049.appendleft(tmp1052)
                                subjects1049.appendleft(tmp1050)
                            subjects1045.appendleft(tmp1048)
                    if len(subjects1045) >= 1 and isinstance(subjects1045[0], Mul):
                        tmp1054 = subjects1045.popleft()
                        associative1 = tmp1054
                        associative_type1 = type(tmp1054)
                        subjects1055 = deque(tmp1054._args)
                        matcher = CommutativeMatcher122556.get()
                        tmp1056 = subjects1055
                        subjects1055 = []
                        for s in tmp1056:
                            matcher.add_subject(s)
                        for pattern_index, subst3 in matcher.match(tmp1056, subst2):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 122561
                                if len(subjects1045) == 0:
                                    pass
                                    # State 122562
                                    if len(subjects) == 0:
                                        pass
                                        # 417: b*sinh(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f198)
                                        yield 417, subst3
                                        # 419: b*sinh(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f491)
                                        yield 419, subst3
                                        # 421: b*sinh(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4)
                                        yield 421, subst3
                                        # 423: b*sinh(c + d*x**n) /; (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f70) and (cons_f71)
                                        yield 423, subst3
                                        # 425: b*sinh(c + d*x**n) /; (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f70)
                                        yield 425, subst3
                                        # 415: b*sinh(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f378) and (cons_f167)
                                        yield 415, subst3
                        subjects1045.appendleft(tmp1054)
                if len(subjects1045) >= 1:
                    tmp1057 = subjects1045.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i3.1.1', tmp1057)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 123392
                        if len(subjects1045) == 0:
                            pass
                            # State 123393
                            if len(subjects) == 0:
                                pass
                                # 427: b*sinh(u) /; (cons_f3) and (cons_f825) and (cons_f826)
                                yield 427, subst2
                    subjects1045.appendleft(tmp1057)
                if len(subjects1045) >= 1 and isinstance(subjects1045[0], Add):
                    tmp1059 = subjects1045.popleft()
                    associative1 = tmp1059
                    associative_type1 = type(tmp1059)
                    subjects1060 = deque(tmp1059._args)
                    matcher = CommutativeMatcher122564.get()
                    tmp1061 = subjects1060
                    subjects1060 = []
                    for s in tmp1061:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp1061, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 122577
                            if len(subjects1045) == 0:
                                pass
                                # State 122578
                                if len(subjects) == 0:
                                    pass
                                    # 417: b*sinh(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f198)
                                    yield 417, subst2
                                    # 419: b*sinh(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f491)
                                    yield 419, subst2
                                    # 421: b*sinh(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4)
                                    yield 421, subst2
                                    # 423: b*sinh(c + d*x**n) /; (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f70) and (cons_f71)
                                    yield 423, subst2
                                    # 425: b*sinh(c + d*x**n) /; (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f70)
                                    yield 425, subst2
                                    # 415: b*sinh(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f378) and (cons_f167)
                                    yield 415, subst2
                    subjects1045.appendleft(tmp1059)
                subjects.appendleft(tmp1044)
            if len(subjects) >= 1 and isinstance(subjects[0], cosh):
                tmp1062 = subjects.popleft()
                subjects1063 = deque(tmp1062._args)
                # State 122698
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i3.1.2.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 122699
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i3.1.2.1.0', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 122700
                        if len(subjects1063) >= 1 and isinstance(subjects1063[0], Pow):
                            tmp1066 = subjects1063.popleft()
                            subjects1067 = deque(tmp1066._args)
                            # State 122701
                            if len(subjects1067) >= 1:
                                tmp1068 = subjects1067.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i3.1.2.1.1', tmp1068)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 122702
                                    if len(subjects1067) >= 1:
                                        tmp1070 = subjects1067.popleft()
                                        subst5 = Substitution(subst4)
                                        try:
                                            subst5.try_add_variable('i3.1.2.1.2', tmp1070)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 122703
                                            if len(subjects1067) == 0:
                                                pass
                                                # State 122704
                                                if len(subjects1063) == 0:
                                                    pass
                                                    # State 122705
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 416: b*cosh(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f378) and (cons_f167)
                                                        yield 416, subst5
                                                        # 418: b*cosh(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f198)
                                                        yield 418, subst5
                                                        # 420: b*cosh(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f491)
                                                        yield 420, subst5
                                                        # 422: b*cosh(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4)
                                                        yield 422, subst5
                                                        # 424: b*cosh(c + d*x**n) /; (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f70) and (cons_f71)
                                                        yield 424, subst5
                                                        # 426: b*cosh(c + d*x**n) /; (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f70)
                                                        yield 426, subst5
                                        subjects1067.appendleft(tmp1070)
                                subjects1067.appendleft(tmp1068)
                            subjects1063.appendleft(tmp1066)
                    if len(subjects1063) >= 1 and isinstance(subjects1063[0], Mul):
                        tmp1072 = subjects1063.popleft()
                        associative1 = tmp1072
                        associative_type1 = type(tmp1072)
                        subjects1073 = deque(tmp1072._args)
                        matcher = CommutativeMatcher122707.get()
                        tmp1074 = subjects1073
                        subjects1073 = []
                        for s in tmp1074:
                            matcher.add_subject(s)
                        for pattern_index, subst3 in matcher.match(tmp1074, subst2):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 122712
                                if len(subjects1063) == 0:
                                    pass
                                    # State 122713
                                    if len(subjects) == 0:
                                        pass
                                        # 416: b*cosh(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f378) and (cons_f167)
                                        yield 416, subst3
                                        # 418: b*cosh(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f198)
                                        yield 418, subst3
                                        # 420: b*cosh(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f491)
                                        yield 420, subst3
                                        # 422: b*cosh(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4)
                                        yield 422, subst3
                                        # 424: b*cosh(c + d*x**n) /; (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f70) and (cons_f71)
                                        yield 424, subst3
                                        # 426: b*cosh(c + d*x**n) /; (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f70)
                                        yield 426, subst3
                        subjects1063.appendleft(tmp1072)
                if len(subjects1063) >= 1:
                    tmp1075 = subjects1063.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i3.1.1', tmp1075)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 123432
                        if len(subjects1063) == 0:
                            pass
                            # State 123433
                            if len(subjects) == 0:
                                pass
                                # 428: b*cosh(u) /; (cons_f3) and (cons_f825) and (cons_f826)
                                yield 428, subst2
                    subjects1063.appendleft(tmp1075)
                if len(subjects1063) >= 1 and isinstance(subjects1063[0], Add):
                    tmp1077 = subjects1063.popleft()
                    associative1 = tmp1077
                    associative_type1 = type(tmp1077)
                    subjects1078 = deque(tmp1077._args)
                    matcher = CommutativeMatcher122715.get()
                    tmp1079 = subjects1078
                    subjects1078 = []
                    for s in tmp1079:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp1079, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 122728
                            if len(subjects1063) == 0:
                                pass
                                # State 122729
                                if len(subjects) == 0:
                                    pass
                                    # 416: b*cosh(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f378) and (cons_f167)
                                    yield 416, subst2
                                    # 418: b*cosh(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f198)
                                    yield 418, subst2
                                    # 420: b*cosh(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f491)
                                    yield 420, subst2
                                    # 422: b*cosh(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4)
                                    yield 422, subst2
                                    # 424: b*cosh(c + d*x**n) /; (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f70) and (cons_f71)
                                    yield 424, subst2
                                    # 426: b*cosh(c + d*x**n) /; (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f70)
                                    yield 426, subst2
                    subjects1063.appendleft(tmp1077)
                subjects.appendleft(tmp1062)
            if len(subjects) >= 1 and isinstance(subjects[0], tanh):
                tmp1080 = subjects.popleft()
                subjects1081 = deque(tmp1080._args)
                # State 126756
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i3.1.2.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 126757
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i3.1.2.1.0', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 126758
                        if len(subjects1081) >= 1 and isinstance(subjects1081[0], Pow):
                            tmp1084 = subjects1081.popleft()
                            subjects1085 = deque(tmp1084._args)
                            # State 126759
                            if len(subjects1085) >= 1:
                                tmp1086 = subjects1085.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i3.1.2.1.1', tmp1086)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 126760
                                    if len(subjects1085) >= 1:
                                        tmp1088 = subjects1085.popleft()
                                        subst5 = Substitution(subst4)
                                        try:
                                            subst5.try_add_variable('i3.1.2.1.2', tmp1088)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 126761
                                            if len(subjects1085) == 0:
                                                pass
                                                # State 126762
                                                if len(subjects1081) == 0:
                                                    pass
                                                    # State 126763
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 433: b*tanh(c + d*x**n) /; (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f70) and (cons_f71)
                                                        yield 433, subst5
                                                        # 429: b*tanh(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f5) and (cons_f1575)
                                                        yield 429, subst5
                                                        # 431: b*tanh(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f5) and (cons_f1497)
                                                        yield 431, subst5
                                        subjects1085.appendleft(tmp1088)
                                subjects1085.appendleft(tmp1086)
                            subjects1081.appendleft(tmp1084)
                    if len(subjects1081) >= 1 and isinstance(subjects1081[0], Mul):
                        tmp1090 = subjects1081.popleft()
                        associative1 = tmp1090
                        associative_type1 = type(tmp1090)
                        subjects1091 = deque(tmp1090._args)
                        matcher = CommutativeMatcher126765.get()
                        tmp1092 = subjects1091
                        subjects1091 = []
                        for s in tmp1092:
                            matcher.add_subject(s)
                        for pattern_index, subst3 in matcher.match(tmp1092, subst2):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 126770
                                if len(subjects1081) == 0:
                                    pass
                                    # State 126771
                                    if len(subjects) == 0:
                                        pass
                                        # 433: b*tanh(c + d*x**n) /; (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f70) and (cons_f71)
                                        yield 433, subst3
                                        # 429: b*tanh(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f5) and (cons_f1575)
                                        yield 429, subst3
                                        # 431: b*tanh(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f5) and (cons_f1497)
                                        yield 431, subst3
                        subjects1081.appendleft(tmp1090)
                if len(subjects1081) >= 1:
                    tmp1093 = subjects1081.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i3.1.1', tmp1093)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 127364
                        if len(subjects1081) == 0:
                            pass
                            # State 127365
                            if len(subjects) == 0:
                                pass
                                # 435: b*tanh(u) /; (cons_f3) and (cons_f825) and (cons_f826)
                                yield 435, subst2
                    subjects1081.appendleft(tmp1093)
                if len(subjects1081) >= 1 and isinstance(subjects1081[0], Add):
                    tmp1095 = subjects1081.popleft()
                    associative1 = tmp1095
                    associative_type1 = type(tmp1095)
                    subjects1096 = deque(tmp1095._args)
                    matcher = CommutativeMatcher126773.get()
                    tmp1097 = subjects1096
                    subjects1096 = []
                    for s in tmp1097:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp1097, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 126786
                            if len(subjects1081) == 0:
                                pass
                                # State 126787
                                if len(subjects) == 0:
                                    pass
                                    # 433: b*tanh(c + d*x**n) /; (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f70) and (cons_f71)
                                    yield 433, subst2
                                    # 429: b*tanh(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f5) and (cons_f1575)
                                    yield 429, subst2
                                    # 431: b*tanh(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f5) and (cons_f1497)
                                    yield 431, subst2
                    subjects1081.appendleft(tmp1095)
                subjects.appendleft(tmp1080)
            if len(subjects) >= 1 and isinstance(subjects[0], asinh):
                tmp1098 = subjects.popleft()
                subjects1099 = deque(tmp1098._args)
                # State 137766
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i3.1.2.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 137767
                    if len(subjects1099) >= 1:
                        tmp1101 = subjects1099.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i3.1.2.0', tmp1101)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 137768
                            if len(subjects1099) == 0:
                                pass
                                # State 137769
                                if len(subjects) == 0:
                                    pass
                                    # 445: b*asinh(x*c) /; (cons_f2) and (cons_f3) and (cons_f8)
                                    yield 445, subst3
                                    # 447: b*asinh(x*c) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f1581)
                                    yield 447, subst3
                        subjects1099.appendleft(tmp1101)
                if len(subjects1099) >= 1 and isinstance(subjects1099[0], Mul):
                    tmp1103 = subjects1099.popleft()
                    associative1 = tmp1103
                    associative_type1 = type(tmp1103)
                    subjects1104 = deque(tmp1103._args)
                    matcher = CommutativeMatcher137771.get()
                    tmp1105 = subjects1104
                    subjects1104 = []
                    for s in tmp1105:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp1105, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 137772
                            if len(subjects1099) == 0:
                                pass
                                # State 137773
                                if len(subjects) == 0:
                                    pass
                                    # 445: b*asinh(x*c) /; (cons_f2) and (cons_f3) and (cons_f8)
                                    yield 445, subst2
                                    # 447: b*asinh(x*c) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f1581)
                                    yield 447, subst2
                    subjects1099.appendleft(tmp1103)
                if len(subjects1099) >= 1 and isinstance(subjects1099[0], Add):
                    tmp1106 = subjects1099.popleft()
                    associative1 = tmp1106
                    associative_type1 = type(tmp1106)
                    subjects1107 = deque(tmp1106._args)
                    matcher = CommutativeMatcher140062.get()
                    tmp1108 = subjects1107
                    subjects1107 = []
                    for s in tmp1108:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp1108, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 140068
                            if len(subjects1099) == 0:
                                pass
                                # State 140069
                                if len(subjects) == 0:
                                    pass
                                    # 449: b*asinh(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f1275)
                                    yield 449, subst2
                        if pattern_index == 1:
                            pass
                            # State 140410
                            if len(subjects1099) == 0:
                                pass
                                # State 140411
                                if len(subjects) == 0:
                                    pass
                                    # 451: b*asinh(c + d*x**2) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1906)
                                    yield 451, subst2
                    subjects1099.appendleft(tmp1106)
                subjects.appendleft(tmp1098)
            if len(subjects) >= 1 and isinstance(subjects[0], acosh):
                tmp1109 = subjects.popleft()
                subjects1110 = deque(tmp1109._args)
                # State 137860
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i3.1.2.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 137861
                    if len(subjects1110) >= 1:
                        tmp1112 = subjects1110.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i3.1.2.0', tmp1112)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 137862
                            if len(subjects1110) == 0:
                                pass
                                # State 137863
                                if len(subjects) == 0:
                                    pass
                                    # 448: b*acosh(x*c) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f1581)
                                    yield 448, subst3
                                    # 446: b*acosh(x*c) /; (cons_f2) and (cons_f3) and (cons_f8)
                                    yield 446, subst3
                        subjects1110.appendleft(tmp1112)
                if len(subjects1110) >= 1 and isinstance(subjects1110[0], Mul):
                    tmp1114 = subjects1110.popleft()
                    associative1 = tmp1114
                    associative_type1 = type(tmp1114)
                    subjects1115 = deque(tmp1114._args)
                    matcher = CommutativeMatcher137865.get()
                    tmp1116 = subjects1115
                    subjects1115 = []
                    for s in tmp1116:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp1116, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 137866
                            if len(subjects1110) == 0:
                                pass
                                # State 137867
                                if len(subjects) == 0:
                                    pass
                                    # 448: b*acosh(x*c) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f1581)
                                    yield 448, subst2
                                    # 446: b*acosh(x*c) /; (cons_f2) and (cons_f3) and (cons_f8)
                                    yield 446, subst2
                    subjects1110.appendleft(tmp1114)
                if len(subjects1110) >= 1 and isinstance(subjects1110[0], Add):
                    tmp1117 = subjects1110.popleft()
                    associative1 = tmp1117
                    associative_type1 = type(tmp1117)
                    subjects1118 = deque(tmp1117._args)
                    matcher = CommutativeMatcher140158.get()
                    tmp1119 = subjects1118
                    subjects1118 = []
                    for s in tmp1119:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp1119, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 140164
                            if len(subjects1110) == 0:
                                pass
                                # State 140165
                                if len(subjects) == 0:
                                    pass
                                    # 450: b*acosh(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f1275)
                                    yield 450, subst2
                        if pattern_index == 1:
                            pass
                            # State 140536
                            if len(subjects1110) == 0:
                                pass
                                # State 140537
                                if len(subjects) == 0:
                                    pass
                                    # 452: b*acosh(d*x**2 + 1) /; (cons_f2) and (cons_f3) and (cons_f29) and (cons_f1767)
                                    yield 452, subst2
                        if pattern_index == 2:
                            pass
                            # State 140573
                            if len(subjects1110) == 0:
                                pass
                                # State 140574
                                if len(subjects) == 0:
                                    pass
                                    # 453: b*acosh(d*x**2 - 1) /; (cons_f2) and (cons_f3) and (cons_f29) and (cons_f1767)
                                    yield 453, subst2
                        if pattern_index == 3:
                            pass
                            # State 140597
                            if len(subjects1110) == 0:
                                pass
                                # State 140598
                                if len(subjects) == 0:
                                    pass
                                    # 454: b*acosh(c + d*x**2) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1766)
                                    yield 454, subst2
                    subjects1110.appendleft(tmp1117)
                subjects.appendleft(tmp1109)
            if len(subjects) >= 1 and isinstance(subjects[0], atanh):
                tmp1120 = subjects.popleft()
                subjects1121 = deque(tmp1120._args)
                # State 142294
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i3.1.2.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 142295
                    if len(subjects1121) >= 1:
                        tmp1123 = subjects1121.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i3.1.2.0', tmp1123)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 142296
                            if len(subjects1121) == 0:
                                pass
                                # State 142297
                                if len(subjects) == 0:
                                    pass
                                    # 457: b*atanh(x*c) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4)
                                    yield 457, subst3
                                    # 455: b*atanh(x*c) /; (cons_f2) and (cons_f3) and (cons_f8)
                                    yield 455, subst3
                        subjects1121.appendleft(tmp1123)
                if len(subjects1121) >= 1 and isinstance(subjects1121[0], Mul):
                    tmp1125 = subjects1121.popleft()
                    associative1 = tmp1125
                    associative_type1 = type(tmp1125)
                    subjects1126 = deque(tmp1125._args)
                    matcher = CommutativeMatcher142299.get()
                    tmp1127 = subjects1126
                    subjects1126 = []
                    for s in tmp1127:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp1127, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 142300
                            if len(subjects1121) == 0:
                                pass
                                # State 142301
                                if len(subjects) == 0:
                                    pass
                                    # 457: b*atanh(x*c) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4)
                                    yield 457, subst2
                                    # 455: b*atanh(x*c) /; (cons_f2) and (cons_f3) and (cons_f8)
                                    yield 455, subst2
                    subjects1121.appendleft(tmp1125)
                if len(subjects1121) >= 1 and isinstance(subjects1121[0], Add):
                    tmp1128 = subjects1121.popleft()
                    associative1 = tmp1128
                    associative_type1 = type(tmp1128)
                    subjects1129 = deque(tmp1128._args)
                    matcher = CommutativeMatcher144750.get()
                    tmp1130 = subjects1129
                    subjects1129 = []
                    for s in tmp1130:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp1130, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 144756
                            if len(subjects1121) == 0:
                                pass
                                # State 144757
                                if len(subjects) == 0:
                                    pass
                                    # 459: b*atanh(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29)
                                    yield 459, subst2
                                    # 461: b*atanh(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4)
                                    yield 461, subst2
                    subjects1121.appendleft(tmp1128)
                subjects.appendleft(tmp1120)
            if len(subjects) >= 1 and isinstance(subjects[0], acoth):
                tmp1131 = subjects.popleft()
                subjects1132 = deque(tmp1131._args)
                # State 142388
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i3.1.2.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 142389
                    if len(subjects1132) >= 1:
                        tmp1134 = subjects1132.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i3.1.2.0', tmp1134)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 142390
                            if len(subjects1132) == 0:
                                pass
                                # State 142391
                                if len(subjects) == 0:
                                    pass
                                    # 456: b*acoth(x*c) /; (cons_f2) and (cons_f3) and (cons_f8)
                                    yield 456, subst3
                                    # 458: b*acoth(x*c) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4)
                                    yield 458, subst3
                        subjects1132.appendleft(tmp1134)
                if len(subjects1132) >= 1 and isinstance(subjects1132[0], Mul):
                    tmp1136 = subjects1132.popleft()
                    associative1 = tmp1136
                    associative_type1 = type(tmp1136)
                    subjects1137 = deque(tmp1136._args)
                    matcher = CommutativeMatcher142393.get()
                    tmp1138 = subjects1137
                    subjects1137 = []
                    for s in tmp1138:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp1138, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 142394
                            if len(subjects1132) == 0:
                                pass
                                # State 142395
                                if len(subjects) == 0:
                                    pass
                                    # 456: b*acoth(x*c) /; (cons_f2) and (cons_f3) and (cons_f8)
                                    yield 456, subst2
                                    # 458: b*acoth(x*c) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4)
                                    yield 458, subst2
                    subjects1132.appendleft(tmp1136)
                if len(subjects1132) >= 1 and isinstance(subjects1132[0], Add):
                    tmp1139 = subjects1132.popleft()
                    associative1 = tmp1139
                    associative_type1 = type(tmp1139)
                    subjects1140 = deque(tmp1139._args)
                    matcher = CommutativeMatcher144846.get()
                    tmp1141 = subjects1140
                    subjects1140 = []
                    for s in tmp1141:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp1141, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 144852
                            if len(subjects1132) == 0:
                                pass
                                # State 144853
                                if len(subjects) == 0:
                                    pass
                                    # 460: b*acoth(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29)
                                    yield 460, subst2
                                    # 462: b*acoth(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4)
                                    yield 462, subst2
                    subjects1132.appendleft(tmp1139)
                subjects.appendleft(tmp1131)
            if len(subjects) >= 1 and isinstance(subjects[0], asech):
                tmp1142 = subjects.popleft()
                subjects1143 = deque(tmp1142._args)
                # State 148732
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i3.1.2.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 148733
                    if len(subjects1143) >= 1:
                        tmp1145 = subjects1143.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i3.1.2.0', tmp1145)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 148734
                            if len(subjects1143) == 0:
                                pass
                                # State 148735
                                if len(subjects) == 0:
                                    pass
                                    # 463: b*asech(x*c) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f1581)
                                    yield 463, subst3
                        subjects1143.appendleft(tmp1145)
                if len(subjects1143) >= 1 and isinstance(subjects1143[0], Mul):
                    tmp1147 = subjects1143.popleft()
                    associative1 = tmp1147
                    associative_type1 = type(tmp1147)
                    subjects1148 = deque(tmp1147._args)
                    matcher = CommutativeMatcher148737.get()
                    tmp1149 = subjects1148
                    subjects1148 = []
                    for s in tmp1149:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp1149, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 148738
                            if len(subjects1143) == 0:
                                pass
                                # State 148739
                                if len(subjects) == 0:
                                    pass
                                    # 463: b*asech(x*c) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f1581)
                                    yield 463, subst2
                    subjects1143.appendleft(tmp1147)
                subjects.appendleft(tmp1142)
            if len(subjects) >= 1 and isinstance(subjects[0], acsch):
                tmp1150 = subjects.popleft()
                subjects1151 = deque(tmp1150._args)
                # State 148783
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i3.1.2.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 148784
                    if len(subjects1151) >= 1:
                        tmp1153 = subjects1151.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i3.1.2.0', tmp1153)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 148785
                            if len(subjects1151) == 0:
                                pass
                                # State 148786
                                if len(subjects) == 0:
                                    pass
                                    # 464: b*acsch(x*c) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f1581)
                                    yield 464, subst3
                        subjects1151.appendleft(tmp1153)
                if len(subjects1151) >= 1 and isinstance(subjects1151[0], Mul):
                    tmp1155 = subjects1151.popleft()
                    associative1 = tmp1155
                    associative_type1 = type(tmp1155)
                    subjects1156 = deque(tmp1155._args)
                    matcher = CommutativeMatcher148788.get()
                    tmp1157 = subjects1156
                    subjects1156 = []
                    for s in tmp1157:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp1157, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 148789
                            if len(subjects1151) == 0:
                                pass
                                # State 148790
                                if len(subjects) == 0:
                                    pass
                                    # 464: b*acsch(x*c) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f1581)
                                    yield 464, subst2
                    subjects1151.appendleft(tmp1155)
                subjects.appendleft(tmp1150)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i3.1.0_2', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 9760
            subst2 = Substitution(subst1)
            try:
                subst2.try_add_variable('i3.1.2_2', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 9761
                if len(subjects) >= 1:
                    tmp1160 = subjects.popleft()
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i3.1.1', tmp1160)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 9762
                        if len(subjects) == 0:
                            pass
                            # 130: c*x**r /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f52) and (cons_f754) and (cons_f228)
                            yield 130, subst3
                            # 135: c*x**r /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f52) and (cons_f754)
                            yield 135, subst3
                            # 140: c*x**r /; (cons_f8) and (cons_f754) and (cons_f70) and (cons_f71)
                            yield 140, subst3
                            # 124: c*x**r /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f753)
                            yield 124, subst3
                            # 127: c*x**r /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f52) and (cons_f754)
                            yield 127, subst3
                    subjects.appendleft(tmp1160)
            if len(subjects) >= 1:
                tmp1162 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i3.1.1', tmp1162)
                except ValueError:
                    pass
                else:
                    pass
                    # State 12419
                    if len(subjects) == 0:
                        pass
                        # 195: b*x /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1005) and (cons_f1006)
                        yield 195, subst2
                        # 197: b*x /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1005) and (cons_f1007)
                        yield 197, subst2
                        # 200: b*x /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1008) and (cons_f1006)
                        yield 200, subst2
                        # 202: b*x /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1008) and (cons_f1007)
                        yield 202, subst2
                        # 205: b*x /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1008) and (cons_f1007) and (With1777)
                        yield 205, subst2
                        # 208: b*x /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f5) and (cons_f1005) and (cons_f1006)
                        yield 208, subst2
                        # 210: b*x /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f5) and (cons_f1005) and (cons_f1007)
                        yield 210, subst2
                        # 213: b*x /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f5) and (cons_f1008) and (cons_f1006)
                        yield 213, subst2
                        # 216: b*x /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f5) and (cons_f1008) and (cons_f1007) and (With1782)
                        yield 216, subst2
                        # 218: b*x /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f5) and (cons_f1008) and (cons_f1007)
                        yield 218, subst2
                subjects.appendleft(tmp1162)
            if len(subjects) >= 1 and isinstance(subjects[0], Pow):
                tmp1164 = subjects.popleft()
                subjects1165 = deque(tmp1164._args)
                # State 9763
                if len(subjects1165) >= 1:
                    tmp1166 = subjects1165.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i3.1.1', tmp1166)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 9764
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i3.1.2_2', 1)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 9765
                            if len(subjects1165) == 0:
                                pass
                                # State 9766
                                if len(subjects) == 0:
                                    pass
                                    # 130: c*x**r /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f52) and (cons_f754) and (cons_f228)
                                    yield 130, subst3
                                    # 135: c*x**r /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f52) and (cons_f754)
                                    yield 135, subst3
                                    # 140: c*x**r /; (cons_f8) and (cons_f754) and (cons_f70) and (cons_f71)
                                    yield 140, subst3
                                    # 124: c*x**r /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f753)
                                    yield 124, subst3
                                    # 127: c*x**r /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f52) and (cons_f754)
                                    yield 127, subst3
                        if len(subjects1165) >= 1:
                            tmp1169 = subjects1165.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i3.1.2_2', tmp1169)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 9765
                                if len(subjects1165) == 0:
                                    pass
                                    # State 9766
                                    if len(subjects) == 0:
                                        pass
                                        # 130: c*x**r /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f52) and (cons_f754) and (cons_f228)
                                        yield 130, subst3
                                        # 135: c*x**r /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f52) and (cons_f754)
                                        yield 135, subst3
                                        # 140: c*x**r /; (cons_f8) and (cons_f754) and (cons_f70) and (cons_f71)
                                        yield 140, subst3
                                        # 124: c*x**r /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f753)
                                        yield 124, subst3
                                        # 127: c*x**r /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f52) and (cons_f754)
                                        yield 127, subst3
                            subjects1165.appendleft(tmp1169)
                        if len(subjects1165) >= 1 and subjects1165[0] == Integer(4):
                            tmp1171 = subjects1165.popleft()
                            # State 12529
                            if len(subjects1165) == 0:
                                pass
                                # State 12530
                                if len(subjects) == 0:
                                    pass
                                    # 225: e*x**4 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50)
                                    yield 225, subst2
                                    # 221: e*x**4 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f5) and (cons_f1016)
                                    yield 221, subst2
                            subjects1165.appendleft(tmp1171)
                    subjects1165.appendleft(tmp1166)
                subjects.appendleft(tmp1164)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i3.1.0_3', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 12532
            if len(subjects) >= 1:
                tmp1173 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i3.1.1', tmp1173)
                except ValueError:
                    pass
                else:
                    pass
                    # State 12533
                    if len(subjects) == 0:
                        pass
                        # 226: b*x /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f1021)
                        yield 226, subst2
                        # 222: b*x /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f5) and (cons_f1016)
                        yield 222, subst2
                subjects.appendleft(tmp1173)
        if len(subjects) >= 1 and isinstance(subjects[0], Mul):
            tmp1175 = subjects.popleft()
            associative1 = tmp1175
            associative_type1 = type(tmp1175)
            subjects1176 = deque(tmp1175._args)
            matcher = CommutativeMatcher2919.get()
            tmp1177 = subjects1176
            subjects1176 = []
            for s in tmp1177:
                matcher.add_subject(s)
            for pattern_index, subst1 in matcher.match(tmp1177, subst0):
                pass
                if pattern_index == 0:
                    pass
                    # State 2920
                    if len(subjects) == 0:
                        pass
                        # 0: x*b /; (cons_f2) and (cons_f3) and (cons_f69)
                        yield 0, subst1
                        # 1: x*b /; (cons_f2) and (cons_f3) and (cons_f19)
                        yield 1, subst1
                        # 2: x*b /; (cons_f3) and (cons_f70) and (cons_f71)
                        yield 2, subst1
                if pattern_index == 1:
                    pass
                    # State 3898
                    if len(subjects) == 0:
                        pass
                        # 3: c*x**2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f47)
                        yield 3, subst1
                        # 5: c*x**2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f5) and (cons_f47)
                        yield 5, subst1
                        # 7: c*x**2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f228) and (cons_f229)
                        yield 7, subst1
                        # 9: c*x**2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f228) and (cons_f230)
                        yield 9, subst1
                        # 11: c*x**2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f228)
                        yield 11, subst1
                        # 13: c*x**2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f228) and (cons_f233) and (cons_f229)
                        yield 13, subst1
                        # 15: c*x**2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f228) and (With200)
                        yield 15, subst1
                        # 17: c*x**2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f5) and (cons_f234)
                        yield 17, subst1
                        # 19: c*x**2 /; (cons_f3) and (cons_f8) and (cons_f235)
                        yield 19, subst1
                        # 21: c*x**2 /; (cons_f3) and (cons_f8)
                        yield 21, subst1
                        # 23: c*x**2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f228) and (With206)
                        yield 23, subst1
                        # 25: c*x**2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f5) and (cons_f228)
                        yield 25, subst1
                        # 27: c*x**2 /; (cons_f8) and (cons_f70) and (cons_f71)
                        yield 27, subst1
                        # 161: c*x**2 /; (cons_f2) and (cons_f3) and (cons_f4)
                        yield 161, subst1
                        # 35: c*x**2 /; (cons_f2) and (cons_f3) and (cons_f468)
                        yield 35, subst1
                        # 36: c*x**2 /; (cons_f2) and (cons_f3) and (cons_f69)
                        yield 36, subst1
                        # 40: c*x**2 /; (cons_f2) and (cons_f3) and (cons_f470) and (cons_f472)
                        yield 40, subst1
                        # 41: c*x**2 /; (cons_f2) and (cons_f3) and (cons_f470) and (cons_f473)
                        yield 41, subst1
                        # 42: c*x**2 /; (cons_f2) and (cons_f3) and (cons_f470)
                        yield 42, subst1
                        # 43: c*x**2 /; (cons_f2) and (cons_f3) and (cons_f471) and (cons_f474)
                        yield 43, subst1
                        # 44: c*x**2 /; (cons_f2) and (cons_f3) and (cons_f471) and (cons_f475)
                        yield 44, subst1
                        # 45: c*x**2 /; (cons_f2) and (cons_f3) and (cons_f471)
                        yield 45, subst1
                        # 52: c*x**2 /; (cons_f2) and (cons_f3) and (cons_f481)
                        yield 52, subst1
                        # 53: c*x**2 /; (cons_f2) and (cons_f3) and (cons_f482)
                        yield 53, subst1
                        # 54: c*x**2 /; (cons_f2) and (cons_f3)
                        yield 54, subst1
                        # 181: c*x**2 /; (cons_f2) and (cons_f8) and (cons_f29) and (cons_f1003)
                        yield 181, subst1
                        # 183: c*x**2 /; (cons_f2) and (cons_f8) and (cons_f29) and (cons_f1004)
                        yield 183, subst1
                        # 185: c*x**2 /; (cons_f2) and (cons_f8) and (cons_f29) and (cons_f1004) and (With1761)
                        yield 185, subst1
                        # 187: c*x**2 /; (cons_f2) and (cons_f8) and (cons_f29) and (cons_f5) and (cons_f1003)
                        yield 187, subst1
                        # 189: c*x**2 /; (cons_f2) and (cons_f8) and (cons_f29) and (cons_f5) and (cons_f1004) and (With1764)
                        yield 189, subst1
                        # 62: c*x**2 /; (cons_f2) and (cons_f3) and (cons_f485)
                        yield 62, subst1
                        # 191: c*x**2 /; (cons_f2) and (cons_f8) and (cons_f29) and (cons_f5) and (cons_f1004)
                        yield 191, subst1
                        # 193: c*x**2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1005) and (cons_f1006)
                        yield 193, subst1
                        # 196: c*x**2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1005) and (cons_f1007)
                        yield 196, subst1
                        # 198: c*x**2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1008) and (cons_f1006)
                        yield 198, subst1
                        # 201: c*x**2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1008) and (cons_f1007)
                        yield 201, subst1
                        # 203: c*x**2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1008) and (cons_f1007) and (With1777)
                        yield 203, subst1
                        # 206: c*x**2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f5) and (cons_f1005) and (cons_f1006)
                        yield 206, subst1
                        # 209: c*x**2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f5) and (cons_f1005) and (cons_f1007)
                        yield 209, subst1
                        # 465: b*x**2 /; (cons_f3) and (cons_f69)
                        yield 465, subst1
                        # 211: c*x**2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f5) and (cons_f1008) and (cons_f1006)
                        yield 211, subst1
                        # 214: c*x**2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f5) and (cons_f1008) and (cons_f1007) and (With1782)
                        yield 214, subst1
                        # 217: c*x**2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f5) and (cons_f1008) and (cons_f1007)
                        yield 217, subst1
                        # 219: c*x**2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f5) and (cons_f1016)
                        yield 219, subst1
                        # 223: c*x**2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f1021)
                        yield 223, subst1
                        # 96: c*x**2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f677)
                        yield 96, subst1
                        # 98: c*x**2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f677) and (cons_f679)
                        yield 98, subst1
                        # 100: c*x**2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f677) and (With1098)
                        yield 100, subst1
                        # 103: c*x**2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f677) and (With1100)
                        yield 103, subst1
                        # 105: c*x**2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f677) and (With1101)
                        yield 105, subst1
                        # 107: c*x**2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f677) and (With1102)
                        yield 107, subst1
                        # 109: c*x**2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f677) and (With1103)
                        yield 109, subst1
                        # 111: c*x**2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f228)
                        yield 111, subst1
                if pattern_index == 2:
                    pass
                    # State 3900
                    if len(subjects) == 0:
                        pass
                        # 4: b*x /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f47)
                        yield 4, subst1
                        # 6: b*x /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f5) and (cons_f47)
                        yield 6, subst1
                        # 8: b*x /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f228) and (cons_f229)
                        yield 8, subst1
                        # 10: b*x /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f228) and (cons_f230)
                        yield 10, subst1
                        # 12: b*x /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f228)
                        yield 12, subst1
                        # 14: b*x /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f228) and (cons_f233) and (cons_f229)
                        yield 14, subst1
                        # 16: b*x /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f228) and (With200)
                        yield 16, subst1
                        # 18: b*x /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f5) and (cons_f234)
                        yield 18, subst1
                        # 20: b*x /; (cons_f3) and (cons_f8) and (cons_f235)
                        yield 20, subst1
                        # 22: b*x /; (cons_f3) and (cons_f8)
                        yield 22, subst1
                        # 24: b*x /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f228) and (With206)
                        yield 24, subst1
                        # 26: b*x /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f5) and (cons_f228)
                        yield 26, subst1
                        # 28: b*x /; (cons_f3) and (cons_f70) and (cons_f71)
                        yield 28, subst1
                        # 170: b*x /; (cons_f2) and (cons_f3) and (cons_f29) and (cons_f1001)
                        yield 170, subst1
                        # 172: b*x /; (cons_f2) and (cons_f3) and (cons_f29) and (cons_f1002)
                        yield 172, subst1
                        # 174: b*x /; (cons_f2) and (cons_f3) and (cons_f29) and (cons_f1002) and (With1747)
                        yield 174, subst1
                        # 176: b*x /; (cons_f2) and (cons_f3) and (cons_f29) and (cons_f5) and (cons_f1001)
                        yield 176, subst1
                        # 178: b*x /; (cons_f2) and (cons_f3) and (cons_f29) and (cons_f5) and (cons_f1002) and (With1750)
                        yield 178, subst1
                        # 180: b*x /; (cons_f2) and (cons_f3) and (cons_f29) and (cons_f5) and (cons_f1002)
                        yield 180, subst1
                if pattern_index == 3:
                    pass
                    # State 6082
                    if len(subjects) == 0:
                        pass
                        # 29: b*x**n /; (cons_f2) and (cons_f3) and (cons_f4) and (cons_f5) and (cons_f462)
                        yield 29, subst1
                        # 30: b*x**n /; (cons_f2) and (cons_f3) and (cons_f4) and (cons_f5) and (cons_f463)
                        yield 30, subst1
                        # 31: b*x**n /; (cons_f2) and (cons_f3) and (cons_f4) and (cons_f464)
                        yield 31, subst1
                        # 32: b*x**n /; (cons_f2) and (cons_f3) and (cons_f89) and (cons_f465)
                        yield 32, subst1
                        # 33: b*x**n /; (cons_f2) and (cons_f3) and (cons_f466)
                        yield 33, subst1
                        # 34: b*x**n /; (cons_f2) and (cons_f3) and (cons_f150) and (cons_f467)
                        yield 34, subst1
                        # 38: b*x**n /; (cons_f2) and (cons_f3) and (cons_f469) and (cons_f470)
                        yield 38, subst1
                        # 39: b*x**n /; (cons_f2) and (cons_f3) and (cons_f469) and (cons_f471)
                        yield 39, subst1
                        # 46: b*x**n /; (cons_f2) and (cons_f3) and (cons_f476) and (cons_f470)
                        yield 46, subst1
                        # 47: b*x**n /; (cons_f2) and (cons_f3) and (cons_f476) and (cons_f471)
                        yield 47, subst1
                        # 50: b*x**n /; (cons_f2) and (cons_f3) and (cons_f479) and (cons_f480)
                        yield 50, subst1
                        # 51: b*x**n /; (cons_f2) and (cons_f3) and (cons_f479) and (cons_f478)
                        yield 51, subst1
                        # 64: b*x**n /; (cons_f2) and (cons_f3) and (cons_f150) and (cons_f489)
                        yield 64, subst1
                        # 65: b*x**n /; (cons_f2) and (cons_f3) and (cons_f150) and (cons_f490)
                        yield 65, subst1
                        # 66: b*x**n /; (cons_f2) and (cons_f3) and (cons_f5) and (cons_f198)
                        yield 66, subst1
                        # 67: b*x**n /; (cons_f2) and (cons_f3) and (cons_f5) and (cons_f491)
                        yield 67, subst1
                        # 68: b*x**n /; (cons_f2) and (cons_f3) and (cons_f4)
                        yield 68, subst1
                        # 69: b*x**n /; (cons_f2) and (cons_f3) and (cons_f4) and (cons_f5) and (cons_f492) and (cons_f493)
                        yield 69, subst1
                        # 70: b*x**n /; (cons_f3) and (cons_f4) and (cons_f70) and (cons_f71)
                        yield 70, subst1
                        # 71: b*x**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f48) and (cons_f89) and (cons_f465)
                        yield 71, subst1
                        # 73: b*x**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f5) and (cons_f48) and (cons_f491)
                        yield 73, subst1
                        # 75: b*x**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f48) and (cons_f47) and (cons_f666)
                        yield 75, subst1
                        # 77: b*x**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f48) and (cons_f47) and (cons_f667) and (cons_f586)
                        yield 77, subst1
                        # 78: b*x**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f48) and (cons_f47) and (cons_f668)
                        yield 78, subst1
                        # 80: b*x**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f48) and (cons_f47) and (cons_f586) and (cons_f670) and (cons_f464)
                        yield 80, subst1
                        # 82: b*x**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f5) and (cons_f48) and (cons_f47) and (cons_f198)
                        yield 82, subst1
                        # 466: b*x**n /; (cons_f3) and (cons_f1481) and (cons_f746)
                        yield 466, subst1
                        # 84: b*x**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f48) and (cons_f47) and (cons_f671) and (cons_f672)
                        yield 84, subst1
                        # 85: b*x**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f48) and (cons_f47) and (cons_f673) and (cons_f674) and (cons_f340)
                        yield 85, subst1
                        # 86: b*x**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f48) and (cons_f47)
                        yield 86, subst1
                        # 87: b*x**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f5) and (cons_f48) and (cons_f198)
                        yield 87, subst1
                        # 88: b*x**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f48) and (cons_f228)
                        yield 88, subst1
                        # 467: b*x**n /; (cons_f3) and (cons_f1484) and (cons_f167)
                        yield 467, subst1
                        # 90: b*x**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f48) and (cons_f228) and (cons_f671) and (cons_f675)
                        yield 90, subst1
                        # 91: b*x**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f48) and (cons_f228) and (cons_f675)
                        yield 91, subst1
                        # 92: b*x**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f48) and (cons_f228) and (cons_f676) and (cons_f415)
                        yield 92, subst1
                        # 94: b*x**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f48) and (cons_f228)
                        yield 94, subst1
                        # 114: b*x**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f682)
                        yield 114, subst1
                        # 116: b*x**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f587)
                        yield 116, subst1
                        # 118: b*x**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f587)
                        yield 118, subst1
                        # 120: b*x**n /; (cons_f3) and (cons_f4) and (cons_f48) and (cons_f70) and (cons_f71)
                        yield 120, subst1
                if pattern_index == 4:
                    pass
                    # State 6127
                    if len(subjects) == 0:
                        pass
                        # 37: b*x**3 /; (cons_f2) and (cons_f3) and (cons_f69)
                        yield 37, subst1
                        # 169: d*x**3 /; (cons_f2) and (cons_f3) and (cons_f29) and (cons_f1001)
                        yield 169, subst1
                        # 171: d*x**3 /; (cons_f2) and (cons_f3) and (cons_f29) and (cons_f1002)
                        yield 171, subst1
                        # 173: d*x**3 /; (cons_f2) and (cons_f3) and (cons_f29) and (cons_f1002) and (With1747)
                        yield 173, subst1
                        # 175: d*x**3 /; (cons_f2) and (cons_f3) and (cons_f29) and (cons_f5) and (cons_f1001)
                        yield 175, subst1
                        # 177: d*x**3 /; (cons_f2) and (cons_f3) and (cons_f29) and (cons_f5) and (cons_f1002) and (With1750)
                        yield 177, subst1
                        # 179: d*x**3 /; (cons_f2) and (cons_f3) and (cons_f29) and (cons_f5) and (cons_f1002)
                        yield 179, subst1
                        # 55: b*x**3 /; (cons_f2) and (cons_f3)
                        yield 55, subst1
                if pattern_index == 5:
                    pass
                    # State 6187
                    if len(subjects) == 0:
                        pass
                        # 48: b*x**4 /; (cons_f2) and (cons_f3) and (cons_f477)
                        yield 48, subst1
                        # 49: b*x**4 /; (cons_f2) and (cons_f3) and (cons_f478)
                        yield 49, subst1
                        # 56: b*x**4 /; (cons_f2) and (cons_f3) and (cons_f468)
                        yield 56, subst1
                        # 57: b*x**4 /; (cons_f2) and (cons_f3) and (cons_f485)
                        yield 57, subst1
                        # 58: b*x**4 /; (cons_f2) and (cons_f3) and (cons_f107) and (With725)
                        yield 58, subst1
                        # 59: b*x**4 /; (cons_f2) and (cons_f3) and (cons_f107)
                        yield 59, subst1
                        # 63: b*x**4 /; (cons_f2) and (cons_f3) and (cons_f69)
                        yield 63, subst1
                if pattern_index == 6:
                    pass
                    # State 6252
                    if len(subjects) == 0:
                        pass
                        # 60: b*x**6 /; (cons_f2) and (cons_f3) and (cons_f69)
                        yield 60, subst1
                if pattern_index == 7:
                    pass
                    # State 6262
                    if len(subjects) == 0:
                        pass
                        # 61: b*x**8 /; (cons_f2) and (cons_f3) and (cons_f69)
                        yield 61, subst1
                if pattern_index == 8:
                    pass
                    # State 8180
                    if len(subjects) == 0:
                        pass
                        # 129: c*x**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f52) and (cons_f754) and (cons_f755) and (cons_f228) and (cons_f756)
                        yield 129, subst1
                        # 132: c*x**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f52) and (cons_f754) and (cons_f755) and (cons_f228)
                        yield 132, subst1
                        # 134: c*x**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f52) and (cons_f754) and (cons_f755)
                        yield 134, subst1
                        # 137: c*x**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f52) and (cons_f754)
                        yield 137, subst1
                        # 139: c*x**n2 /; (cons_f2) and (cons_f52) and (cons_f754) and (cons_f70) and (cons_f71)
                        yield 139, subst1
                        # 148: c*x**n2 /; (cons_f2) and (cons_f3) and (cons_f798) and (cons_f4) and (cons_f5) and (cons_f954) and (cons_f955)
                        yield 148, subst1
                        # 150: c*x**n2 /; (cons_f2) and (cons_f3) and (cons_f798) and (cons_f4) and (cons_f954) and (cons_f956)
                        yield 150, subst1
                        # 152: c*x**n2 /; (cons_f2) and (cons_f3) and (cons_f798) and (cons_f4) and (cons_f5) and (cons_f954) and (cons_f956)
                        yield 152, subst1
                        # 154: c*x**n2 /; (cons_f2) and (cons_f3) and (cons_f958) and (cons_f959)
                        yield 154, subst1
                        # 156: c*x**n2 /; (cons_f2) and (cons_f3) and (cons_f958) and (cons_f959) and (cons_f961)
                        yield 156, subst1
                        # 158: c*x**n2 /; (cons_f2) and (cons_f3) and (cons_f958) and (cons_f959) and (cons_f962)
                        yield 158, subst1
                        # 160: c*x**n2 /; (cons_f2) and (cons_f3) and (cons_f798) and (cons_f4) and (cons_f954)
                        yield 160, subst1
                        # 164: c*x**n2 /; (cons_f2) and (cons_f3) and (cons_f966) and (cons_f967)
                        yield 164, subst1
                        # 166: c*x**n2 /; (cons_f2) and (cons_f3) and (cons_f798) and (cons_f4) and (cons_f5) and (cons_f954) and (cons_f968)
                        yield 166, subst1
                        # 168: c*x**n2 /; (cons_f3) and (cons_f4) and (cons_f70) and (cons_f71)
                        yield 168, subst1
                        # 72: c*x**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f48)
                        yield 72, subst1
                        # 74: c*x**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f5) and (cons_f48)
                        yield 74, subst1
                        # 76: c*x**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f48) and (cons_f47)
                        yield 76, subst1
                        # 79: c*x**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f48) and (cons_f47)
                        yield 79, subst1
                        # 83: c*x**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f5) and (cons_f48) and (cons_f47)
                        yield 83, subst1
                        # 89: c*x**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f48) and (cons_f228)
                        yield 89, subst1
                        # 115: c*x**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f682)
                        yield 115, subst1
                        # 117: c*x**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f587) and (cons_f683)
                        yield 117, subst1
                        # 119: c*x**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f587) and (cons_f683)
                        yield 119, subst1
                        # 121: c*x**n2 /; (cons_f8) and (cons_f48) and (cons_f70) and (cons_f71)
                        yield 121, subst1
                        # 123: c*x**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f752)
                        yield 123, subst1
                        # 126: c*x**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f52) and (cons_f754) and (cons_f755)
                        yield 126, subst1
                if pattern_index == 9:
                    pass
                    # State 8210
                    if len(subjects) == 0:
                        pass
                        # 81: c*x**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f48) and (cons_f47)
                        yield 81, subst1
                        # 93: c*x**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f48) and (cons_f228) and (cons_f415)
                        yield 93, subst1
                        # 95: c*x**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f48) and (cons_f228)
                        yield 95, subst1
                if pattern_index == 10:
                    pass
                    # State 8268
                    if len(subjects) == 0:
                        pass
                        # 97: c*x**4 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f677) and (cons_f295)
                        yield 97, subst1
                        # 99: c*x**4 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f677) and (cons_f678)
                        yield 99, subst1
                        # 101: c*x**4 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f677) and (cons_f179) and (With1098)
                        yield 101, subst1
                        # 102: c*x**4 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f677) and (cons_f179)
                        yield 102, subst1
                        # 104: c*x**4 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f677) and (With1100)
                        yield 104, subst1
                        # 106: c*x**4 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f677) and (With1101)
                        yield 106, subst1
                        # 108: c*x**4 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f677) and (With1102)
                        yield 108, subst1
                        # 110: c*x**4 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f677) and (With1103)
                        yield 110, subst1
                        # 112: c*x**4 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f228) and (cons_f680)
                        yield 112, subst1
                        # 113: c*x**4 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f228) and (cons_f681)
                        yield 113, subst1
                if pattern_index == 11:
                    pass
                    # State 9759
                    if len(subjects) == 0:
                        pass
                        # 128: b*x**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f52) and (cons_f754) and (cons_f755) and (cons_f228) and (cons_f756)
                        yield 128, subst1
                        # 131: b*x**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f52) and (cons_f754) and (cons_f755) and (cons_f228)
                        yield 131, subst1
                        # 163: b*x**n /; (cons_f2) and (cons_f3) and (cons_f966) and (cons_f967)
                        yield 163, subst1
                        # 133: b*x**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f52) and (cons_f754) and (cons_f755)
                        yield 133, subst1
                        # 165: b*x**n /; (cons_f2) and (cons_f3) and (cons_f798) and (cons_f4) and (cons_f5) and (cons_f954) and (cons_f968)
                        yield 165, subst1
                        # 167: b*x**n /; (cons_f2) and (cons_f798) and (cons_f70) and (cons_f71)
                        yield 167, subst1
                        # 136: b*x**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f52) and (cons_f754)
                        yield 136, subst1
                        # 138: b*x**n /; (cons_f3) and (cons_f4) and (cons_f754) and (cons_f70) and (cons_f71)
                        yield 138, subst1
                        # 147: b*x**n /; (cons_f2) and (cons_f3) and (cons_f798) and (cons_f4) and (cons_f5) and (cons_f954) and (cons_f955)
                        yield 147, subst1
                        # 149: b*x**n /; (cons_f2) and (cons_f3) and (cons_f798) and (cons_f4) and (cons_f954) and (cons_f956)
                        yield 149, subst1
                        # 125: b*x**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f52) and (cons_f754) and (cons_f755)
                        yield 125, subst1
                        # 151: b*x**n /; (cons_f2) and (cons_f3) and (cons_f798) and (cons_f4) and (cons_f5) and (cons_f954) and (cons_f956) and (cons_f957)
                        yield 151, subst1
                        # 153: b*x**n /; (cons_f2) and (cons_f3) and (cons_f958) and (cons_f959) and (cons_f960)
                        yield 153, subst1
                        # 122: b*x**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f752) and (cons_f753)
                        yield 122, subst1
                        # 155: b*x**n /; (cons_f2) and (cons_f3) and (cons_f958) and (cons_f959)
                        yield 155, subst1
                        # 157: b*x**n /; (cons_f2) and (cons_f3) and (cons_f958) and (cons_f959) and (cons_f962)
                        yield 157, subst1
                        # 159: b*x**n /; (cons_f2) and (cons_f3) and (cons_f798) and (cons_f4) and (cons_f954) and (cons_f964)
                        yield 159, subst1
                if pattern_index == 12:
                    pass
                    # State 9771
                    if len(subjects) == 0:
                        pass
                        # 130: c*x**r /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f52) and (cons_f754) and (cons_f228)
                        yield 130, subst1
                        # 135: c*x**r /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f52) and (cons_f754)
                        yield 135, subst1
                        # 140: c*x**r /; (cons_f8) and (cons_f754) and (cons_f70) and (cons_f71)
                        yield 140, subst1
                        # 124: c*x**r /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f753)
                        yield 124, subst1
                        # 127: c*x**r /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f52) and (cons_f754)
                        yield 127, subst1
                if pattern_index == 13:
                    pass
                    # State 10113
                    if len(subjects) == 0:
                        pass
                        # 141: b*(c*x**n)**q /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f52) and (cons_f4) and (cons_f5) and (cons_f800)
                        yield 141, subst1
                if pattern_index == 14:
                    pass
                    # State 10636
                    if len(subjects) == 0:
                        pass
                        # 145: b*(c/x)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f5) and (cons_f809) and (cons_f810)
                        yield 145, subst1
                        # 142: b*(c/x)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f808)
                        yield 142, subst1
                        # 143: b*(c/x)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f5) and (cons_f48)
                        yield 143, subst1
                if pattern_index == 15:
                    pass
                    # State 10979
                    if len(subjects) == 0:
                        pass
                        # 144: c*(c/x)**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f5) and (cons_f48)
                        yield 144, subst1
                if pattern_index == 16:
                    pass
                    # State 11184
                    if len(subjects) == 0:
                        pass
                        # 146: c*x**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f5) and (cons_f809)
                        yield 146, subst1
                if pattern_index == 17:
                    pass
                    # State 12103
                    if len(subjects) == 0:
                        pass
                        # 162: b*x**n /; (cons_f2) and (cons_f3) and (cons_f4) and (cons_f965)
                        yield 162, subst1
                if pattern_index == 18:
                    pass
                    # State 12361
                    if len(subjects) == 0:
                        pass
                        # 192: d*x**3 /; (cons_f2) and (cons_f8) and (cons_f29) and (cons_f5) and (cons_f1004)
                        yield 192, subst1
                        # 224: d*x**3 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f1021)
                        yield 224, subst1
                        # 194: d*x**3 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1005)
                        yield 194, subst1
                        # 199: d*x**3 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1008)
                        yield 199, subst1
                        # 204: d*x**3 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1008) and (With1777)
                        yield 204, subst1
                        # 207: d*x**3 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f5) and (cons_f1005)
                        yield 207, subst1
                        # 188: d*x**3 /; (cons_f2) and (cons_f8) and (cons_f29) and (cons_f5) and (cons_f1003)
                        yield 188, subst1
                        # 212: d*x**3 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f5) and (cons_f1008)
                        yield 212, subst1
                        # 182: d*x**3 /; (cons_f2) and (cons_f8) and (cons_f29) and (cons_f1003)
                        yield 182, subst1
                        # 215: d*x**3 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f5) and (cons_f1008) and (With1782)
                        yield 215, subst1
                        # 184: d*x**3 /; (cons_f2) and (cons_f8) and (cons_f29) and (cons_f1004)
                        yield 184, subst1
                        # 186: d*x**3 /; (cons_f2) and (cons_f8) and (cons_f29) and (cons_f1004) and (With1761)
                        yield 186, subst1
                        # 220: d*x**3 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f5) and (cons_f1016)
                        yield 220, subst1
                        # 190: d*x**3 /; (cons_f2) and (cons_f8) and (cons_f29) and (cons_f5) and (cons_f1004) and (With1764)
                        yield 190, subst1
                if pattern_index == 19:
                    pass
                    # State 12420
                    if len(subjects) == 0:
                        pass
                        # 195: b*x /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1005) and (cons_f1006)
                        yield 195, subst1
                        # 197: b*x /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1005) and (cons_f1007)
                        yield 197, subst1
                        # 200: b*x /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1008) and (cons_f1006)
                        yield 200, subst1
                        # 202: b*x /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1008) and (cons_f1007)
                        yield 202, subst1
                        # 205: b*x /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1008) and (cons_f1007) and (With1777)
                        yield 205, subst1
                        # 208: b*x /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f5) and (cons_f1005) and (cons_f1006)
                        yield 208, subst1
                        # 210: b*x /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f5) and (cons_f1005) and (cons_f1007)
                        yield 210, subst1
                        # 213: b*x /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f5) and (cons_f1008) and (cons_f1006)
                        yield 213, subst1
                        # 216: b*x /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f5) and (cons_f1008) and (cons_f1007) and (With1782)
                        yield 216, subst1
                        # 218: b*x /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f5) and (cons_f1008) and (cons_f1007)
                        yield 218, subst1
                if pattern_index == 20:
                    pass
                    # State 12531
                    if len(subjects) == 0:
                        pass
                        # 225: e*x**4 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50)
                        yield 225, subst1
                        # 221: e*x**4 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f5) and (cons_f1016)
                        yield 221, subst1
                if pattern_index == 21:
                    pass
                    # State 12534
                    if len(subjects) == 0:
                        pass
                        # 226: b*x /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f1021)
                        yield 226, subst1
                        # 222: b*x /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f5) and (cons_f1016)
                        yield 222, subst1
                if pattern_index == 22:
                    pass
                    # State 13562
                    if len(subjects) == 0:
                        pass
                        # 227: h*(d + e*x + f*sqrt(a + b*x + c*x**2))**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f210) and (cons_f211) and (cons_f4) and (cons_f1057)
                        yield 227, subst1
                if pattern_index == 23:
                    pass
                    # State 13666
                    if len(subjects) == 0:
                        pass
                        # 228: h*(d + e*x + f*sqrt(a + c*x**2))**n /; (cons_f2) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f210) and (cons_f211) and (cons_f4) and (cons_f1057)
                        yield 228, subst1
                if pattern_index == 24:
                    pass
                    # State 13770
                    if len(subjects) == 0:
                        pass
                        # 229: h*(u + f*sqrt(v))**n /; (cons_f127) and (cons_f211) and (cons_f4) and (cons_f70) and (cons_f820) and (cons_f821) and (cons_f1058)
                        yield 229, subst1
                if pattern_index == 25:
                    pass
                    # State 14133
                    if len(subjects) == 0:
                        pass
                        # 230: b*sqrt(c + d*x**2) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1068)
                        yield 230, subst1
                if pattern_index == 26:
                    pass
                    # State 20450
                    if len(subjects) == 0:
                        pass
                        # 232: b*log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f417)
                        yield 232, subst1
                        # 233: b*log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f1160)
                        yield 233, subst1
                        # 234: b*log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f1161)
                        yield 234, subst1
                        # 231: b*log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52)
                        yield 231, subst1
                if pattern_index == 27:
                    pass
                    # State 50803
                    if len(subjects) == 0:
                        pass
                        # 235: b*log(c*(d + e*x**2)**p) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f5)
                        yield 235, subst1
                if pattern_index == 28:
                    pass
                    # State 53075
                    if len(subjects) == 0:
                        pass
                        # 236: b*log(c*(d + e/(f + x*g))**p) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f210) and (cons_f5)
                        yield 236, subst1
                if pattern_index == 29:
                    pass
                    # State 53207
                    if len(subjects) == 0:
                        pass
                        # 237: b*log(c*RFx**p) /; (cons_f3) and (cons_f8) and (cons_f5) and (cons_f1200)
                        yield 237, subst1
                if pattern_index == 30:
                    pass
                    # State 56775
                    if len(subjects) == 0:
                        pass
                        # 238: d*LambertW(a + b*x) /; (cons_f29) and (cons_f1767)
                        yield 238, subst1
                if pattern_index == 31:
                    pass
                    # State 56844
                    if len(subjects) == 0:
                        pass
                        # 239: d*LambertW(a*x**n) /; (cons_f29)
                        yield 239, subst1
                if pattern_index == 32:
                    pass
                    # State 58108
                    if len(subjects) == 0:
                        pass
                        # 256: b*sin(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1269) and (cons_f1274)
                        yield 256, subst1
                        # 257: b*sin(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f1269)
                        yield 257, subst1
                        # 240: b*sin(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1266)
                        yield 240, subst1
                        # 242: b*sin(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f1267)
                        yield 242, subst1
                        # 244: b*sin(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1267)
                        yield 244, subst1
                        # 246: b*sin(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1269) and (cons_f1270)
                        yield 246, subst1
                        # 248: b*sin(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1269) and (cons_f1271)
                        yield 248, subst1
                        # 250: b*sin(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1269) and (cons_f1272)
                        yield 250, subst1
                        # 252: b*sin(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1269)
                        yield 252, subst1
                        # 254: b*sin(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1273)
                        yield 254, subst1
                if pattern_index == 33:
                    pass
                    # State 58150
                    if len(subjects) == 0:
                        pass
                        # 258: b*cos(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f1269)
                        yield 258, subst1
                        # 260: a*cos(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f1441)
                        yield 260, subst1
                        # 262: a*cos(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1442)
                        yield 262, subst1
                        # 264: a*cos(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f1446)
                        yield 264, subst1
                        # 266: a*cos(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f1447)
                        yield 266, subst1
                        # 268: a*cos(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f1450)
                        yield 268, subst1
                        # 270: a*cos(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f1451)
                        yield 270, subst1
                        # 272: a*cos(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f1452) and (cons_f1453)
                        yield 272, subst1
                        # 274: a*cos(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f1454) and (cons_f1452) and (cons_f1455)
                        yield 274, subst1
                        # 276: a*cos(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f1454)
                        yield 276, subst1
                        # 278: a*cos(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f1456)
                        yield 278, subst1
                        # 280: a*cos(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50)
                        yield 280, subst1
                        # 282: a*cos(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f1458)
                        yield 282, subst1
                        # 241: b*cos(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1266)
                        yield 241, subst1
                        # 243: b*cos(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f1267)
                        yield 243, subst1
                        # 245: b*cos(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1267)
                        yield 245, subst1
                        # 247: b*cos(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1269) and (cons_f1270)
                        yield 247, subst1
                        # 249: b*cos(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1269) and (cons_f1271)
                        yield 249, subst1
                        # 251: b*cos(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1269) and (cons_f1272)
                        yield 251, subst1
                        # 253: b*cos(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1269)
                        yield 253, subst1
                        # 255: b*cos(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1273)
                        yield 255, subst1
                if pattern_index == 34:
                    pass
                    # State 58297
                    if len(subjects) == 0:
                        pass
                        # 259: b*sin(c + x*d)*cos(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f1275)
                        yield 259, subst1
                if pattern_index == 35:
                    pass
                    # State 66733
                    if len(subjects) == 0:
                        pass
                        # 261: b*sin(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f1441)
                        yield 261, subst1
                        # 263: b*sin(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1442)
                        yield 263, subst1
                        # 265: b*sin(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f1446)
                        yield 265, subst1
                        # 267: b*sin(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f1447)
                        yield 267, subst1
                        # 269: b*sin(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f1450)
                        yield 269, subst1
                        # 271: b*sin(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f1451)
                        yield 271, subst1
                        # 273: b*sin(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f1452) and (cons_f1453)
                        yield 273, subst1
                        # 275: b*sin(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f1454) and (cons_f1452) and (cons_f1455)
                        yield 275, subst1
                        # 277: b*sin(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f1454)
                        yield 277, subst1
                        # 279: b*sin(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50)
                        yield 279, subst1
                        # 281: b*sin(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f78)
                        yield 281, subst1
                        # 283: b*sin(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f1457)
                        yield 283, subst1
                if pattern_index == 36:
                    pass
                    # State 67137
                    if len(subjects) == 0:
                        pass
                        # 358: b/cos(d + x*e) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1266)
                        yield 358, subst1
                        # 360: b/cos(d + x*e) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1267)
                        yield 360, subst1
                        # 362: b/cos(d + x*e) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f1267)
                        yield 362, subst1
                        # 364: b/cos(d + x*e) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1269)
                        yield 364, subst1
                        # 366: b/cos(d + x*e) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f1269)
                        yield 366, subst1
                        # 284: b/cos(d + x*e) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f1045)
                        yield 284, subst1
                if pattern_index == 37:
                    pass
                    # State 67174
                    if len(subjects) == 0:
                        pass
                        # 285: c*tan(d + x*e) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f1045)
                        yield 285, subst1
                if pattern_index == 38:
                    pass
                    # State 67228
                    if len(subjects) == 0:
                        pass
                        # 359: b/sin(d + x*e) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1266)
                        yield 359, subst1
                        # 361: b/sin(d + x*e) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1267)
                        yield 361, subst1
                        # 363: b/sin(d + x*e) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f1267)
                        yield 363, subst1
                        # 365: b/sin(d + x*e) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1269)
                        yield 365, subst1
                        # 367: b/sin(d + x*e) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f1269)
                        yield 367, subst1
                        # 286: b/sin(d + x*e) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f1045)
                        yield 286, subst1
                if pattern_index == 39:
                    pass
                    # State 67277
                    if len(subjects) == 0:
                        pass
                        # 287: c/tan(d + x*e) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f1045)
                        yield 287, subst1
                if pattern_index == 40:
                    pass
                    # State 67765
                    if len(subjects) == 0:
                        pass
                        # 288: b*sin(d + x*e)**2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1456)
                        yield 288, subst1
                        # 290: b*sin(d + x*e)**2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f5) and (cons_f1456)
                        yield 290, subst1
                        # 292: b*sin(d + x*e)**2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29)
                        yield 292, subst1
                        # 294: b*sin(d + x*e)**2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f5) and (cons_f1480)
                        yield 294, subst1
                if pattern_index == 41:
                    pass
                    # State 67783
                    if len(subjects) == 0:
                        pass
                        # 289: b*cos(d + x*e)**2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1456)
                        yield 289, subst1
                        # 291: b*cos(d + x*e)**2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f5) and (cons_f1456)
                        yield 291, subst1
                        # 293: b*cos(d + x*e)**2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29)
                        yield 293, subst1
                        # 295: b*cos(d + x*e)**2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f5) and (cons_f1480)
                        yield 295, subst1
                if pattern_index == 42:
                    pass
                    # State 67831
                    if len(subjects) == 0:
                        pass
                        # 296: b*sin(d + x*e)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f87)
                        yield 296, subst1
                        # 298: b*sin(d + x*e)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1481)
                        yield 298, subst1
                if pattern_index == 43:
                    pass
                    # State 67849
                    if len(subjects) == 0:
                        pass
                        # 297: b*cos(d + x*e)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f87)
                        yield 297, subst1
                        # 299: b*cos(d + x*e)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1481)
                        yield 299, subst1
                if pattern_index == 44:
                    pass
                    # State 68942
                    if len(subjects) == 0:
                        pass
                        # 304: b*sin(d + x*e)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f5) and (cons_f48) and (cons_f47)
                        yield 304, subst1
                        # 300: b*sin(d + x*e)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                        yield 300, subst1
                        # 308: b*sin(d + x*e)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f228)
                        yield 308, subst1
                if pattern_index == 45:
                    pass
                    # State 69011
                    if len(subjects) == 0:
                        pass
                        # 305: c*sin(d + x*e)**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f5) and (cons_f48) and (cons_f47)
                        yield 305, subst1
                        # 301: c*sin(d + x*e)**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                        yield 301, subst1
                        # 309: c*sin(d + x*e)**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f228)
                        yield 309, subst1
                if pattern_index == 46:
                    pass
                    # State 69220
                    if len(subjects) == 0:
                        pass
                        # 302: b*cos(d + x*e)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                        yield 302, subst1
                        # 306: b*cos(d + x*e)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f5) and (cons_f48) and (cons_f47)
                        yield 306, subst1
                        # 310: b*cos(d + x*e)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f228)
                        yield 310, subst1
                if pattern_index == 47:
                    pass
                    # State 69287
                    if len(subjects) == 0:
                        pass
                        # 307: c*cos(d + x*e)**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f5) and (cons_f48) and (cons_f47)
                        yield 307, subst1
                        # 303: c*cos(d + x*e)**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                        yield 303, subst1
                        # 311: c*cos(d + x*e)**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f228)
                        yield 311, subst1
                if pattern_index == 48:
                    pass
                    # State 72766
                    if len(subjects) == 0:
                        pass
                        # 320: b*sin(c + d*x**n) /; (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f70) and (cons_f71)
                        yield 320, subst1
                        # 322: b*sin(c + d*x**n) /; (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f70)
                        yield 322, subst1
                        # 312: b*sin(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f378) and (cons_f167)
                        yield 312, subst1
                        # 314: b*sin(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f198)
                        yield 314, subst1
                        # 316: b*sin(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f491)
                        yield 316, subst1
                        # 318: b*sin(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4)
                        yield 318, subst1
                if pattern_index == 49:
                    pass
                    # State 72901
                    if len(subjects) == 0:
                        pass
                        # 321: b*cos(c + d*x**n) /; (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f70) and (cons_f71)
                        yield 321, subst1
                        # 323: b*cos(c + d*x**n) /; (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f70)
                        yield 323, subst1
                        # 313: b*cos(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f378) and (cons_f167)
                        yield 313, subst1
                        # 315: b*cos(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f198)
                        yield 315, subst1
                        # 317: b*cos(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f491)
                        yield 317, subst1
                        # 319: b*cos(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4)
                        yield 319, subst1
                if pattern_index == 50:
                    pass
                    # State 73535
                    if len(subjects) == 0:
                        pass
                        # 324: b*sin(u) /; (cons_f3) and (cons_f825) and (cons_f826)
                        yield 324, subst1
                if pattern_index == 51:
                    pass
                    # State 73575
                    if len(subjects) == 0:
                        pass
                        # 325: b*cos(u) /; (cons_f3) and (cons_f825) and (cons_f826)
                        yield 325, subst1
                if pattern_index == 52:
                    pass
                    # State 77482
                    if len(subjects) == 0:
                        pass
                        # 326: b*tan(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1266)
                        yield 326, subst1
                        # 328: b*tan(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1441)
                        yield 328, subst1
                        # 330: b*tan(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f1441)
                        yield 330, subst1
                        # 332: b*tan(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1442)
                        yield 332, subst1
                        # 334: b*tan(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f1442)
                        yield 334, subst1
                if pattern_index == 53:
                    pass
                    # State 77512
                    if len(subjects) == 0:
                        pass
                        # 327: b/tan(d + x*e) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1266)
                        yield 327, subst1
                        # 329: b/tan(d + x*e) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1441)
                        yield 329, subst1
                        # 331: b/tan(d + x*e) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f1441)
                        yield 331, subst1
                        # 333: b/tan(d + x*e) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1442)
                        yield 333, subst1
                        # 335: b/tan(d + x*e) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f1442)
                        yield 335, subst1
                if pattern_index == 54:
                    pass
                    # State 82117
                    if len(subjects) == 0:
                        pass
                        # 336: b*tan(d + x*e)**2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1494)
                        yield 336, subst1
                        # 338: b*tan(d + x*e)**2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1458)
                        yield 338, subst1
                if pattern_index == 55:
                    pass
                    # State 82135
                    if len(subjects) == 0:
                        pass
                        # 337: b/tan(d + x*e)**2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1494)
                        yield 337, subst1
                        # 339: b/tan(d + x*e)**2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1458)
                        yield 339, subst1
                if pattern_index == 56:
                    pass
                    # State 82241
                    if len(subjects) == 0:
                        pass
                        # 340: b*(e*tan(c + x*d))**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f5) and (cons_f1572)
                        yield 340, subst1
                if pattern_index == 57:
                    pass
                    # State 82361
                    if len(subjects) == 0:
                        pass
                        # 341: b*(e/tan(c + x*d))**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f5) and (cons_f1572)
                        yield 341, subst1
                if pattern_index == 58:
                    pass
                    # State 83543
                    if len(subjects) == 0:
                        pass
                        # 346: b*tan(d + x*e)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f228)
                        yield 346, subst1
                        # 342: b*tan(d + x*e)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                        yield 342, subst1
                if pattern_index == 59:
                    pass
                    # State 83592
                    if len(subjects) == 0:
                        pass
                        # 347: c*tan(d + x*e)**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f228)
                        yield 347, subst1
                        # 343: c*tan(d + x*e)**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                        yield 343, subst1
                if pattern_index == 60:
                    pass
                    # State 83920
                    if len(subjects) == 0:
                        pass
                        # 344: b*(1/tan(d + x*e))**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                        yield 344, subst1
                        # 348: b*(1/tan(d + x*e))**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f228)
                        yield 348, subst1
                if pattern_index == 61:
                    pass
                    # State 84010
                    if len(subjects) == 0:
                        pass
                        # 345: c*(1/tan(d + x*e))**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                        yield 345, subst1
                        # 349: c*(1/tan(d + x*e))**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f228)
                        yield 349, subst1
                if pattern_index == 62:
                    pass
                    # State 87357
                    if len(subjects) == 0:
                        pass
                        # 352: b*tan(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f5) and (cons_f1497)
                        yield 352, subst1
                        # 354: b*tan(c + d*x**n) /; (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f70) and (cons_f71)
                        yield 354, subst1
                        # 350: b*tan(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f5) and (cons_f1575)
                        yield 350, subst1
                if pattern_index == 63:
                    pass
                    # State 87665
                    if len(subjects) == 0:
                        pass
                        # 353: b/tan(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f5) and (cons_f1497)
                        yield 353, subst1
                        # 355: b/tan(c + d*x**n) /; (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f70) and (cons_f71)
                        yield 355, subst1
                        # 351: b/tan(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f5) and (cons_f1575)
                        yield 351, subst1
                if pattern_index == 64:
                    pass
                    # State 87873
                    if len(subjects) == 0:
                        pass
                        # 356: b*tan(u) /; (cons_f3) and (cons_f825) and (cons_f826)
                        yield 356, subst1
                if pattern_index == 65:
                    pass
                    # State 87929
                    if len(subjects) == 0:
                        pass
                        # 357: b/tan(u) /; (cons_f3) and (cons_f825) and (cons_f826)
                        yield 357, subst1
                if pattern_index == 66:
                    pass
                    # State 94791
                    if len(subjects) == 0:
                        pass
                        # 368: b/cos(d + x*e)**2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f5) and (cons_f1456)
                        yield 368, subst1
                        # 370: b/cos(d + x*e)**2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1480)
                        yield 370, subst1
                        # 372: b/cos(d + x*e)**2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f5) and (cons_f1480)
                        yield 372, subst1
                if pattern_index == 67:
                    pass
                    # State 94809
                    if len(subjects) == 0:
                        pass
                        # 369: b/sin(d + x*e)**2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f5) and (cons_f1456)
                        yield 369, subst1
                        # 371: b/sin(d + x*e)**2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1480)
                        yield 371, subst1
                        # 373: b/sin(d + x*e)**2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f5) and (cons_f1480)
                        yield 373, subst1
                if pattern_index == 68:
                    pass
                    # State 95625
                    if len(subjects) == 0:
                        pass
                        # 378: b*(1/cos(d + x*e))**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f5) and (cons_f48) and (cons_f47)
                        yield 378, subst1
                        # 374: b*(1/cos(d + x*e))**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                        yield 374, subst1
                        # 382: b*(1/cos(d + x*e))**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f228)
                        yield 382, subst1
                if pattern_index == 69:
                    pass
                    # State 95710
                    if len(subjects) == 0:
                        pass
                        # 379: c*(1/cos(d + x*e))**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f5) and (cons_f48) and (cons_f47)
                        yield 379, subst1
                        # 375: c*(1/cos(d + x*e))**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                        yield 375, subst1
                        # 383: c*(1/cos(d + x*e))**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f228)
                        yield 383, subst1
                if pattern_index == 70:
                    pass
                    # State 96021
                    if len(subjects) == 0:
                        pass
                        # 376: b*(1/sin(d + x*e))**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                        yield 376, subst1
                        # 380: b*(1/sin(d + x*e))**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f5) and (cons_f48) and (cons_f47)
                        yield 380, subst1
                        # 384: b*(1/sin(d + x*e))**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f228)
                        yield 384, subst1
                if pattern_index == 71:
                    pass
                    # State 96106
                    if len(subjects) == 0:
                        pass
                        # 377: c*(1/sin(d + x*e))**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                        yield 377, subst1
                        # 385: c*(1/sin(d + x*e))**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f228)
                        yield 385, subst1
                        # 381: c*(1/sin(d + x*e))**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f5) and (cons_f48) and (cons_f47)
                        yield 381, subst1
                if pattern_index == 72:
                    pass
                    # State 97720
                    if len(subjects) == 0:
                        pass
                        # 386: b/cos(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f5) and (cons_f1575)
                        yield 386, subst1
                        # 388: b/cos(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f5) and (cons_f1497)
                        yield 388, subst1
                        # 390: b/cos(c + d*x**n) /; (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f70) and (cons_f71)
                        yield 390, subst1
                if pattern_index == 73:
                    pass
                    # State 98028
                    if len(subjects) == 0:
                        pass
                        # 387: b/sin(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f5) and (cons_f1575)
                        yield 387, subst1
                        # 389: b/sin(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f5) and (cons_f1497)
                        yield 389, subst1
                        # 391: b/sin(c + d*x**n) /; (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f70) and (cons_f71)
                        yield 391, subst1
                if pattern_index == 74:
                    pass
                    # State 98268
                    if len(subjects) == 0:
                        pass
                        # 392: b/cos(u) /; (cons_f3) and (cons_f825) and (cons_f826)
                        yield 392, subst1
                if pattern_index == 75:
                    pass
                    # State 98324
                    if len(subjects) == 0:
                        pass
                        # 393: b/sin(u) /; (cons_f3) and (cons_f825) and (cons_f826)
                        yield 393, subst1
                if pattern_index == 76:
                    pass
                    # State 101210
                    if len(subjects) == 0:
                        pass
                        # 394: b*F**(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1666)
                        yield 394, subst1
                if pattern_index == 77:
                    pass
                    # State 108043
                    if len(subjects) == 0:
                        pass
                        # 395: b*asin(x*c) /; (cons_f2) and (cons_f3) and (cons_f8)
                        yield 395, subst1
                        # 397: b*asin(x*c) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f1581)
                        yield 397, subst1
                if pattern_index == 78:
                    pass
                    # State 108137
                    if len(subjects) == 0:
                        pass
                        # 396: b*acos(x*c) /; (cons_f2) and (cons_f3) and (cons_f8)
                        yield 396, subst1
                        # 398: b*acos(x*c) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f1581)
                        yield 398, subst1
                if pattern_index == 79:
                    pass
                    # State 110344
                    if len(subjects) == 0:
                        pass
                        # 399: b*asin(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f1275)
                        yield 399, subst1
                if pattern_index == 80:
                    pass
                    # State 110440
                    if len(subjects) == 0:
                        pass
                        # 400: b*acos(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f1275)
                        yield 400, subst1
                if pattern_index == 81:
                    pass
                    # State 110730
                    if len(subjects) == 0:
                        pass
                        # 401: b*asin(c + d*x**2) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1766)
                        yield 401, subst1
                if pattern_index == 82:
                    pass
                    # State 110797
                    if len(subjects) == 0:
                        pass
                        # 402: b*acos(d*x**2 + 1) /; (cons_f2) and (cons_f3) and (cons_f29) and (cons_f1767)
                        yield 402, subst1
                if pattern_index == 83:
                    pass
                    # State 110824
                    if len(subjects) == 0:
                        pass
                        # 403: b*acos(d*x**2 - 1) /; (cons_f2) and (cons_f3) and (cons_f29) and (cons_f1767)
                        yield 403, subst1
                if pattern_index == 84:
                    pass
                    # State 110859
                    if len(subjects) == 0:
                        pass
                        # 404: b*acos(c + d*x**2) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1766)
                        yield 404, subst1
                if pattern_index == 85:
                    pass
                    # State 112678
                    if len(subjects) == 0:
                        pass
                        # 405: b*atan(x*c) /; (cons_f2) and (cons_f3) and (cons_f8)
                        yield 405, subst1
                        # 407: b*atan(x*c) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4)
                        yield 407, subst1
                if pattern_index == 86:
                    pass
                    # State 112772
                    if len(subjects) == 0:
                        pass
                        # 408: b*acot(x*c) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4)
                        yield 408, subst1
                        # 406: b*acot(x*c) /; (cons_f2) and (cons_f3) and (cons_f8)
                        yield 406, subst1
                if pattern_index == 87:
                    pass
                    # State 115542
                    if len(subjects) == 0:
                        pass
                        # 409: b*atan(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29)
                        yield 409, subst1
                        # 411: b*atan(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4)
                        yield 411, subst1
                if pattern_index == 88:
                    pass
                    # State 115638
                    if len(subjects) == 0:
                        pass
                        # 410: b*acot(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29)
                        yield 410, subst1
                        # 412: b*acot(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4)
                        yield 412, subst1
                if pattern_index == 89:
                    pass
                    # State 119572
                    if len(subjects) == 0:
                        pass
                        # 413: b*asec(x*c) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f1581)
                        yield 413, subst1
                if pattern_index == 90:
                    pass
                    # State 119623
                    if len(subjects) == 0:
                        pass
                        # 414: b*acsc(x*c) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f1581)
                        yield 414, subst1
                if pattern_index == 91:
                    pass
                    # State 122611
                    if len(subjects) == 0:
                        pass
                        # 417: b*sinh(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f198)
                        yield 417, subst1
                        # 419: b*sinh(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f491)
                        yield 419, subst1
                        # 421: b*sinh(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4)
                        yield 421, subst1
                        # 423: b*sinh(c + d*x**n) /; (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f70) and (cons_f71)
                        yield 423, subst1
                        # 425: b*sinh(c + d*x**n) /; (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f70)
                        yield 425, subst1
                        # 415: b*sinh(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f378) and (cons_f167)
                        yield 415, subst1
                if pattern_index == 92:
                    pass
                    # State 122762
                    if len(subjects) == 0:
                        pass
                        # 416: b*cosh(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f378) and (cons_f167)
                        yield 416, subst1
                        # 418: b*cosh(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f198)
                        yield 418, subst1
                        # 420: b*cosh(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f491)
                        yield 420, subst1
                        # 422: b*cosh(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4)
                        yield 422, subst1
                        # 424: b*cosh(c + d*x**n) /; (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f70) and (cons_f71)
                        yield 424, subst1
                        # 426: b*cosh(c + d*x**n) /; (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f70)
                        yield 426, subst1
                if pattern_index == 93:
                    pass
                    # State 123396
                    if len(subjects) == 0:
                        pass
                        # 427: b*sinh(u) /; (cons_f3) and (cons_f825) and (cons_f826)
                        yield 427, subst1
                if pattern_index == 94:
                    pass
                    # State 123436
                    if len(subjects) == 0:
                        pass
                        # 428: b*cosh(u) /; (cons_f3) and (cons_f825) and (cons_f826)
                        yield 428, subst1
                if pattern_index == 95:
                    pass
                    # State 126820
                    if len(subjects) == 0:
                        pass
                        # 433: b*tanh(c + d*x**n) /; (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f70) and (cons_f71)
                        yield 433, subst1
                        # 429: b*tanh(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f5) and (cons_f1575)
                        yield 429, subst1
                        # 431: b*tanh(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f5) and (cons_f1497)
                        yield 431, subst1
                if pattern_index == 96:
                    pass
                    # State 127160
                    if len(subjects) == 0:
                        pass
                        # 432: b/tanh(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f5) and (cons_f1497)
                        yield 432, subst1
                        # 434: b/tanh(c + d*x**n) /; (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f70) and (cons_f71)
                        yield 434, subst1
                        # 430: b/tanh(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f5) and (cons_f1575)
                        yield 430, subst1
                if pattern_index == 97:
                    pass
                    # State 127368
                    if len(subjects) == 0:
                        pass
                        # 435: b*tanh(u) /; (cons_f3) and (cons_f825) and (cons_f826)
                        yield 435, subst1
                if pattern_index == 98:
                    pass
                    # State 127424
                    if len(subjects) == 0:
                        pass
                        # 436: b/tanh(u) /; (cons_f3) and (cons_f825) and (cons_f826)
                        yield 436, subst1
                if pattern_index == 99:
                    pass
                    # State 129937
                    if len(subjects) == 0:
                        pass
                        # 441: b/cosh(c + d*x**n) /; (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f70) and (cons_f71)
                        yield 441, subst1
                        # 437: b/cosh(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f5) and (cons_f1575)
                        yield 437, subst1
                        # 439: b/cosh(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f5) and (cons_f1497)
                        yield 439, subst1
                if pattern_index == 100:
                    pass
                    # State 130277
                    if len(subjects) == 0:
                        pass
                        # 440: b/sinh(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f5) and (cons_f1497)
                        yield 440, subst1
                        # 442: b/sinh(c + d*x**n) /; (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f70) and (cons_f71)
                        yield 442, subst1
                        # 438: b/sinh(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f5) and (cons_f1575)
                        yield 438, subst1
                if pattern_index == 101:
                    pass
                    # State 130517
                    if len(subjects) == 0:
                        pass
                        # 443: b/cosh(u) /; (cons_f3) and (cons_f825) and (cons_f826)
                        yield 443, subst1
                if pattern_index == 102:
                    pass
                    # State 130573
                    if len(subjects) == 0:
                        pass
                        # 444: b/sinh(u) /; (cons_f3) and (cons_f825) and (cons_f826)
                        yield 444, subst1
                if pattern_index == 103:
                    pass
                    # State 137782
                    if len(subjects) == 0:
                        pass
                        # 445: b*asinh(x*c) /; (cons_f2) and (cons_f3) and (cons_f8)
                        yield 445, subst1
                        # 447: b*asinh(x*c) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f1581)
                        yield 447, subst1
                if pattern_index == 104:
                    pass
                    # State 137876
                    if len(subjects) == 0:
                        pass
                        # 448: b*acosh(x*c) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f1581)
                        yield 448, subst1
                        # 446: b*acosh(x*c) /; (cons_f2) and (cons_f3) and (cons_f8)
                        yield 446, subst1
                if pattern_index == 105:
                    pass
                    # State 140079
                    if len(subjects) == 0:
                        pass
                        # 449: b*asinh(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f1275)
                        yield 449, subst1
                if pattern_index == 106:
                    pass
                    # State 140175
                    if len(subjects) == 0:
                        pass
                        # 450: b*acosh(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f1275)
                        yield 450, subst1
                if pattern_index == 107:
                    pass
                    # State 140424
                    if len(subjects) == 0:
                        pass
                        # 451: b*asinh(c + d*x**2) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1906)
                        yield 451, subst1
                if pattern_index == 108:
                    pass
                    # State 140551
                    if len(subjects) == 0:
                        pass
                        # 452: b*acosh(d*x**2 + 1) /; (cons_f2) and (cons_f3) and (cons_f29) and (cons_f1767)
                        yield 452, subst1
                if pattern_index == 109:
                    pass
                    # State 140578
                    if len(subjects) == 0:
                        pass
                        # 453: b*acosh(d*x**2 - 1) /; (cons_f2) and (cons_f3) and (cons_f29) and (cons_f1767)
                        yield 453, subst1
                if pattern_index == 110:
                    pass
                    # State 140601
                    if len(subjects) == 0:
                        pass
                        # 454: b*acosh(c + d*x**2) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1766)
                        yield 454, subst1
                if pattern_index == 111:
                    pass
                    # State 142310
                    if len(subjects) == 0:
                        pass
                        # 457: b*atanh(x*c) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4)
                        yield 457, subst1
                        # 455: b*atanh(x*c) /; (cons_f2) and (cons_f3) and (cons_f8)
                        yield 455, subst1
                if pattern_index == 112:
                    pass
                    # State 142404
                    if len(subjects) == 0:
                        pass
                        # 456: b*acoth(x*c) /; (cons_f2) and (cons_f3) and (cons_f8)
                        yield 456, subst1
                        # 458: b*acoth(x*c) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4)
                        yield 458, subst1
                if pattern_index == 113:
                    pass
                    # State 144767
                    if len(subjects) == 0:
                        pass
                        # 459: b*atanh(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29)
                        yield 459, subst1
                        # 461: b*atanh(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4)
                        yield 461, subst1
                if pattern_index == 114:
                    pass
                    # State 144863
                    if len(subjects) == 0:
                        pass
                        # 460: b*acoth(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29)
                        yield 460, subst1
                        # 462: b*acoth(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4)
                        yield 462, subst1
                if pattern_index == 115:
                    pass
                    # State 148748
                    if len(subjects) == 0:
                        pass
                        # 463: b*asech(x*c) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f1581)
                        yield 463, subst1
                if pattern_index == 116:
                    pass
                    # State 148799
                    if len(subjects) == 0:
                        pass
                        # 464: b*acsch(x*c) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f1581)
                        yield 464, subst1
            subjects.appendleft(tmp1175)
        return
        yield


from .generated_part009604 import *
from .generated_part009478 import *
from .generated_part009484 import *
from .generated_part009483 import *
from .generated_part009584 import *
from .generated_part009410 import *
from .generated_part009607 import *
from .generated_part009453 import *
from .generated_part009394 import *
from collections import deque
from .generated_part009471 import *
from .generated_part009477 import *
from .generated_part009389 import *
from .generated_part009502 import *
from matchpy.utils import VariableWithCount
from .generated_part009469 import *
from .generated_part009624 import *
from .generated_part009429 import *
from .generated_part009398 import *
from .generated_part009417 import *
from .generated_part009511 import *
from .generated_part009474 import *
from .generated_part009590 import *
from .generated_part009495 import *
from matchpy.matching.many_to_one import CommutativeMatcher
from .generated_part009522 import *
from .generated_part009454 import *
from .generated_part009501 import *
from .generated_part009498 import *
from .generated_part009407 import *
from .generated_part009592 import *
from .generated_part009434 import *
from .generated_part009605 import *
from .generated_part009602 import *
from .generated_part009496 import *
from .generated_part009480 import *
from .generated_part009419 import *
from .generated_part009425 import *
from .generated_part009486 import *
from .generated_part009422 import *
from .generated_part009406 import *
from .generated_part009612 import *
from .generated_part009388 import *
from .generated_part009456 import *
from .generated_part009599 import *
from multiset import Multiset
from .generated_part009387 import *
from .generated_part009420 import *
from .generated_part009463 import *
from .generated_part009613 import *
from .generated_part009447 import *
from .generated_part009610 import *
from .generated_part009397 import *
from .generated_part009587 import *
from .generated_part009628 import *
from .generated_part009432 import *
from .generated_part009583 import *
from .generated_part009504 import *
from .generated_part009621 import *
from .generated_part009615 import *
from .generated_part009459 import *
from .generated_part009400 import *
from .generated_part009593 import *
from .generated_part009625 import *
from .generated_part009540 import *
from .generated_part009609 import *
from .generated_part009596 import *
from .generated_part009431 import *
from .generated_part009468 import *
from .generated_part009525 import *
from .generated_part009589 import *
from .generated_part009395 import *
from .generated_part009492 import *
from .generated_part009629 import *
from .generated_part009401 import *
from .generated_part009466 import *
from .generated_part009520 import *
from .generated_part009618 import *
from .generated_part009601 import *
from .generated_part009462 import *
from .generated_part009411 import *
from .generated_part009519 import *
from .generated_part009616 import *
from .generated_part009391 import *
from .generated_part009437 import *
from .generated_part009490 import *
from .generated_part009457 import *
from .generated_part009438 import *
from .generated_part009414 import *
from .generated_part009499 import *
from .generated_part009460 import *
from .generated_part009428 import *
from .generated_part009435 import *
from .generated_part009475 import *
from .generated_part009481 import *
from .generated_part009487 import *
from .generated_part009413 import *
from .generated_part009606 import *
from .generated_part009465 import *
from .generated_part009493 import *
from .generated_part009426 import *
from .generated_part009489 import *
from .generated_part009627 import *
from .generated_part009403 import *
from .generated_part009408 import *
from .generated_part009595 import *
from .generated_part009423 import *
from .generated_part009598 import *
from .generated_part009404 import *
from .generated_part009440 import *
from .generated_part009392 import *
from .generated_part009416 import *
from .generated_part009619 import *
from .generated_part009532 import *
from .generated_part009586 import *
from .generated_part009622 import *
from .generated_part009472 import *
from .generated_part009523 import *