# constants.py
import time

NUM_TALENT_SLOTS = 27
CONST_529 = [5,2,3,5,5,3,2,3,2,5,2,3,5,5,3,2,3,2,5,2,3,5,5,3,2,3,2]
CLASS_118_CONST_127 = 6
const_228 = 4
GAME_CONST_209 = 4
ENTITY_CONST_244    = 2
Entity_const_172 = 3
class_9_const_28 = 5
class_1_const_254 = 7
class_64_const_499 = 2
class_64_const_218 = 5
class_111_const_432 = 9
class_10_const_665 = 4
ENT_MAX_SLOTS = 7
GS_BITS = 2
MAX_CHAR_LEVEL_BITS = 6
Game_const_646     = 4
EntType_MAX_SLOTS = 7
class_21_const_763 = 250
class_10_const_83  = 7
class_66_const_409 = 6
class_16_const_167 = 6
class_7_const_19 = 7
quest_val = None
class_9_const_129 = 5
class_66_const_571 = 2
class_7_const_75 = 6
GEARTYPE_BITS = 11

SLOT_BIT_WIDTHS = []
for x in CONST_529:
    w = 0
    if x <= 2:
        w = 1
    if x <= 4:
        w = 2
    if x <= 5:
        w = 3
    SLOT_BIT_WIDTHS.append(w)

class Mission:
    const_213 = 0
    const_58  = 1
    const_72  = 2

class class_119:
    const_228 = 4

CLASS_NAME_TO_ID = {
    "Paladin": 0,
    "Rogue":   1,
    "Mage":    2,
}

class class_111 :
    const_286 = 1
    const_509 = 0
    const_432 = 9
    const_1101 = 511
    const_264 = 2

class LockboxType:
    ID_BITS = 8

class EntType:
    MAX_SLOTS = 7

class DyeType:
    BITS = 8

class class_118:
    const_43 = 27

class class_64:
    const_101 = 16

class GearType:
    GEARTYPE_BITSTOSEND = 11
    const_348          = 3
    const_176          = 2
"""
class MissionDef:
    def __init__(self, var_1775: bool, var_908: int, var_134: bool):
        self.var_1775 = var_1775
        self.var_908   = var_908
        self.var_134   = var_134

# Index 0 is unused, so we put a dummy placeholder
var_238 = [
    None,  # index 0 unused
    MissionDef(False, 1, True),  # ID 1
    MissionDef(False, 2, True),  # ID 2
    MissionDef(False, 3, True),  # ID 3
    MissionDef(False, 4, True),  # ID 4
    MissionDef(False, 5, True),  # ID 5
    MissionDef(False, 6, True),  # ID 6
    MissionDef(False, 7, True),  # ID 7
    MissionDef(False, 8, True),  # ID 8
    MissionDef(False, 9, True),  # ID 9
    MissionDef(False, 10, True),  # ID 10
    MissionDef(False, 11, True),  # ID 11
    MissionDef(False, 12, True),  # ID 12
    MissionDef(False, 13, True),  # ID 13
    MissionDef(False, 14, True),  # ID 14
    MissionDef(False, 15, True),  # ID 15
    MissionDef(False, 16, True),  # ID 16
    MissionDef(False, 17, True),  # ID 17
    MissionDef(False, 18, True),  # ID 18
    MissionDef(False, 19, True),  # ID 19
    MissionDef(False, 20, True),  # ID 20
    MissionDef(False, 21, True),  # ID 21
    MissionDef(False, 22, True),  # ID 22
    MissionDef(False, 23, True),  # ID 23
    MissionDef(False, 24, True),  # ID 24
    MissionDef(False, 25, True),  # ID 25
    MissionDef(False, 26, True),  # ID 26
    MissionDef(False, 27, True),  # ID 27
    MissionDef(False, 28, True),  # ID 28
    MissionDef(False, 29, True),  # ID 29
    MissionDef(False, 30, True),  # ID 30
    MissionDef(False, 31, True),  # ID 31
    MissionDef(False, 32, True),  # ID 32
    MissionDef(False, 33, True),  # ID 33
    MissionDef(False, 34, True),  # ID 34
    MissionDef(False, 35, True),  # ID 35
    MissionDef(False, 36, True),  # ID 36
    MissionDef(False, 37, True),  # ID 37
    MissionDef(False, 38, True),  # ID 38
    MissionDef(False, 39, True),  # ID 39
    MissionDef(False, 40, True),  # ID 40
    MissionDef(False, 41, True),  # ID 41
    MissionDef(False, 42, True),  # ID 42
    MissionDef(False, 43, True),  # ID 43
    MissionDef(False, 44, True),  # ID 44
    MissionDef(False, 45, True),  # ID 45
    MissionDef(False, 46, True),  # ID 46
    MissionDef(False, 47, True),  # ID 47
    MissionDef(False, 48, True),  # ID 48
    MissionDef(False, 49, True),  # ID 49
    MissionDef(False, 50, True),  # ID 50
    MissionDef(False, 51, True),  # ID 51
    MissionDef(False, 52, True),  # ID 52
    MissionDef(False, 53, True),  # ID 53
    MissionDef(False, 54, True),  # ID 54
    MissionDef(False, 55, True),  # ID 55
    MissionDef(False, 56, True),  # ID 56
    MissionDef(False, 57, True),  # ID 57
    MissionDef(False, 58, True),  # ID 58
    MissionDef(False, 59, True),  # ID 59
    MissionDef(False, 60, True),  # ID 60
    MissionDef(False, 61, True),  # ID 61
    MissionDef(False, 62, True),  # ID 62
    MissionDef(False, 63, True),  # ID 63
    MissionDef(False, 64, True),  # ID 64
    MissionDef(False, 65, True),  # ID 65
    MissionDef(False, 66, True),  # ID 66
    MissionDef(False, 67, True),  # ID 67
    MissionDef(False, 68, True),  # ID 68
    MissionDef(False, 69, True),  # ID 69
    MissionDef(False, 70, True),  # ID 70
    MissionDef(False, 71, True),  # ID 71
    MissionDef(False, 72, True),  # ID 72
    MissionDef(False, 73, True),  # ID 73
    MissionDef(False, 74, True),  # ID 74
    MissionDef(False, 75, True),  # ID 75
    MissionDef(False, 76, True),  # ID 76
    MissionDef(False, 77, True),  # ID 77
    MissionDef(False, 78, True),  # ID 78
    MissionDef(False, 79, True),  # ID 79
    MissionDef(False, 80, True),  # ID 80
    MissionDef(False, 81, True),  # ID 81
    MissionDef(False, 82, True),  # ID 82
    MissionDef(False, 83, True),  # ID 83
    MissionDef(False, 84, True),  # ID 84
    MissionDef(False, 85, True),  # ID 85
    MissionDef(False, 86, True),  # ID 86
    MissionDef(False, 87, True),  # ID 87
    MissionDef(False, 88, True),  # ID 88
    MissionDef(False, 89, True),  # ID 89
    MissionDef(False, 90, True),  # ID 90
    MissionDef(False, 91, True),  # ID 91
    MissionDef(False, 92, True),  # ID 92
    MissionDef(False, 93, True),  # ID 93
    MissionDef(False, 94, True),  # ID 94
    MissionDef(False, 95, True),  # ID 95
    MissionDef(False, 96, True),  # ID 96
    MissionDef(False, 97, True),  # ID 97
    MissionDef(False, 98, True),  # ID 98
    MissionDef(False, 99, True),  # ID 99
    MissionDef(False, 100, True),  # ID 100
    MissionDef(False, 101, True),  # ID 101
    MissionDef(False, 102, True),  # ID 102
    MissionDef(False, 103, True),  # ID 103
    MissionDef(False, 104, True),  # ID 104
    MissionDef(False, 105, True),  # ID 105
    MissionDef(False, 106, True),  # ID 106
    MissionDef(False, 107, True),  # ID 107
    MissionDef(False, 108, True),  # ID 108
    MissionDef(False, 109, True),  # ID 109
    MissionDef(False, 110, True),  # ID 110
    MissionDef(False, 111, True),  # ID 111
    MissionDef(False, 112, True),  # ID 112
    MissionDef(False, 113, True),  # ID 113
    MissionDef(False, 114, True),  # ID 114
    MissionDef(False, 115, True),  # ID 115
    MissionDef(False, 116, True),  # ID 116
    MissionDef(False, 117, True),  # ID 117
    MissionDef(False, 118, True),  # ID 118
    MissionDef(False, 119, True),  # ID 119
    MissionDef(False, 120, True),  # ID 120
    MissionDef(False, 121, True),  # ID 121
    MissionDef(False, 122, True),  # ID 122
    MissionDef(False, 123, True),  # ID 123
    MissionDef(False, 124, True),  # ID 124
    MissionDef(False, 125, True),  # ID 125
    MissionDef(False, 126, True),  # ID 126
    MissionDef(False, 127, True),  # ID 127
    MissionDef(False, 128, True),  # ID 128
    MissionDef(False, 129, True),  # ID 129
    MissionDef(False, 130, True),  # ID 130
    MissionDef(False, 131, True),  # ID 131
    MissionDef(False, 132, True),  # ID 132
    MissionDef(False, 133, True),  # ID 133
    MissionDef(False, 134, True),  # ID 134
    MissionDef(False, 135, True),  # ID 135
    MissionDef(False, 136, True),  # ID 136
    MissionDef(False, 137, True),  # ID 137
    MissionDef(False, 138, True),  # ID 138
    MissionDef(False, 139, True),  # ID 139
    MissionDef(False, 140, True),  # ID 140
    MissionDef(False, 141, True),  # ID 141
    MissionDef(False, 142, True),  # ID 142
    MissionDef(False, 143, True),  # ID 143
    MissionDef(False, 144, True),  # ID 144
    MissionDef(False, 145, True),  # ID 145
    MissionDef(False, 146, True),  # ID 146
    MissionDef(False, 147, True),  # ID 147
    MissionDef(False, 148, True),  # ID 148
    MissionDef(False, 149, True),  # ID 149
    MissionDef(False, 150, True),  # ID 150
    MissionDef(False, 151, True),  # ID 151
    MissionDef(False, 152, True),  # ID 152
    MissionDef(False, 153, True),  # ID 153
    MissionDef(False, 154, True),  # ID 154
    MissionDef(False, 155, True),  # ID 155
    MissionDef(False, 156, True),  # ID 156
    MissionDef(False, 157, True),  # ID 157
    MissionDef(False, 158, True),  # ID 158
    MissionDef(False, 159, True),  # ID 159
    MissionDef(False, 160, True),  # ID 160
    MissionDef(False, 161, True),  # ID 161
    MissionDef(False, 162, True),  # ID 162
    MissionDef(False, 163, True),  # ID 163
    MissionDef(False, 164, True),  # ID 164
    MissionDef(False, 165, True),  # ID 165
    MissionDef(False, 166, True),  # ID 166
    MissionDef(False, 167, True),  # ID 167
    MissionDef(False, 168, True),  # ID 168
    MissionDef(False, 169, True),  # ID 169
    MissionDef(False, 170, True),  # ID 170
    MissionDef(False, 171, True),  # ID 171
    MissionDef(False, 172, True),  # ID 172
    MissionDef(False, 173, True),  # ID 173
    MissionDef(False, 174, True),  # ID 174
    MissionDef(False, 175, True),  # ID 175
    MissionDef(False, 176, True),  # ID 176
    MissionDef(False, 177, True),  # ID 177
    MissionDef(False, 178, True),  # ID 178
    MissionDef(False, 179, True),  # ID 179
    MissionDef(False, 180, True),  # ID 180
    MissionDef(False, 181, True),  # ID 181
    MissionDef(False, 182, True),  # ID 182
    MissionDef(False, 183, True),  # ID 183
    MissionDef(False, 184, True),  # ID 184
    MissionDef(False, 185, True),  # ID 185
    MissionDef(False, 186, True),  # ID 186
    MissionDef(False, 187, True),  # ID 187
    MissionDef(False, 188, True),  # ID 188
    MissionDef(False, 189, True),  # ID 189
    MissionDef(False, 190, True),  # ID 190
    MissionDef(False, 191, True),  # ID 191
    MissionDef(False, 192, True),  # ID 192
    MissionDef(False, 193, True),  # ID 193
    MissionDef(False, 194, True),  # ID 194
    MissionDef(False, 195, True),  # ID 195
    MissionDef(False, 196, True),  # ID 196
    MissionDef(False, 197, True),  # ID 197
    MissionDef(False, 198, True),  # ID 198
    MissionDef(False, 199, True),  # ID 199
    MissionDef(False, 200, True),  # ID 200
    MissionDef(False, 201, True),  # ID 201
    MissionDef(False, 202, True),  # ID 202
    MissionDef(False, 203, True),  # ID 203
    MissionDef(False, 204, True),  # ID 204
    MissionDef(False, 205, True),  # ID 205
    MissionDef(False, 206, True),  # ID 206
    MissionDef(False, 207, True),  # ID 207
    MissionDef(False, 208, True),  # ID 208
    MissionDef(False, 209, True),  # ID 209
    MissionDef(False, 210, True),  # ID 210
    MissionDef(False, 211, True),  # ID 211
    MissionDef(False, 212, True),  # ID 212
    MissionDef(False, 213, True),  # ID 213
    MissionDef(False, 214, True),  # ID 214
    MissionDef(False, 215, True),  # ID 215
    MissionDef(False, 216, True),  # ID 216
    MissionDef(False, 217, True),  # ID 217
    MissionDef(False, 218, True),  # ID 218
    MissionDef(False, 219, True),  # ID 219
    MissionDef(False, 220, True),  # ID 220
    MissionDef(False, 221, True),  # ID 221
    MissionDef(False, 222, True),  # ID 222
    MissionDef(False, 223, True),  # ID 223
    MissionDef(False, 224, True),  # ID 224
    MissionDef(False, 225, True),  # ID 225
    MissionDef(False, 226, True),  # ID 226
    MissionDef(False, 227, True),  # ID 227
    MissionDef(False, 228, True),  # ID 228
    MissionDef(False, 229, True),  # ID 229
    MissionDef(False, 230, True),  # ID 230
    MissionDef(False, 231, True),  # ID 231
    MissionDef(False, 232, True),  # ID 232
    MissionDef(False, 233, True),  # ID 233
    MissionDef(False, 234, True),  # ID 234
    MissionDef(False, 235, True),  # ID 235
    MissionDef(False, 236, True),  # ID 236
    MissionDef(False, 237, True),  # ID 237
    MissionDef(False, 238, True),  # ID 238
    MissionDef(False, 239, True),  # ID 239
    MissionDef(False, 240, True),  # ID 240
    MissionDef(False, 241, True),  # ID 241
    MissionDef(False, 242, True),  # ID 242
    MissionDef(False, 243, True),  # ID 243
    MissionDef(False, 244, True),  # ID 244
    MissionDef(False, 245, True),  # ID 245
    MissionDef(False, 246, True),  # ID 246
    MissionDef(False, 247, True),  # ID 247
    MissionDef(False, 248, True),  # ID 248
    MissionDef(False, 249, True),  # ID 249
    MissionDef(False, 250, True),  # ID 250
    MissionDef(False, 251, True),  # ID 251
    MissionDef(False, 252, True),  # ID 252
    MissionDef(False, 253, True),  # ID 253
    MissionDef(False, 254, True),  # ID 254
    MissionDef(False, 255, True),  # ID 255
    MissionDef(False, 256, True),  # ID 256
    MissionDef(False, 257, True),  # ID 257
    MissionDef(False, 258, True),  # ID 258
    MissionDef(False, 259, True),  # ID 259
    MissionDef(False, 260, True),  # ID 260
    MissionDef(False, 261, True),  # ID 261
    MissionDef(False, 262, True),  # ID 262
    MissionDef(False, 263, True),  # ID 263
    MissionDef(False, 264, True),  # ID 264
    MissionDef(False, 265, True),  # ID 265
    MissionDef(False, 266, True),  # ID 266
    MissionDef(False, 267, True),  # ID 267
    MissionDef(False, 268, True),  # ID 268
    MissionDef(False, 269, True),  # ID 269
    MissionDef(False, 270, True),  # ID 270
    MissionDef(False, 271, True),  # ID 271
    MissionDef(False, 272, True),  # ID 272
    MissionDef(False, 273, True),  # ID 273
    MissionDef(False, 274, True),  # ID 274
    MissionDef(False, 275, True),  # ID 275
    MissionDef(False, 276, True),  # ID 276
    MissionDef(False, 277, True),  # ID 277
    MissionDef(False, 278, True),  # ID 278
    MissionDef(False, 279, True),  # ID 279
    MissionDef(False, 280, True),  # ID 280
    MissionDef(False, 281, True),  # ID 281
    MissionDef(False, 282, True),  # ID 282
    MissionDef(False, 283, True),  # ID 283
    MissionDef(False, 284, True),  # ID 284
    MissionDef(False, 285, True),  # ID 285
    MissionDef(False, 286, True),  # ID 286
    MissionDef(False, 287, True),  # ID 287
    MissionDef(False, 288, True),  # ID 288
    MissionDef(False, 289, True),  # ID 289
    MissionDef(False, 290, True),  # ID 290
    MissionDef(False, 291, True),  # ID 291
    MissionDef(False, 292, True),  # ID 292
    MissionDef(False, 293, True),  # ID 293
]
"""


NEWS_EVENTS = {
    1: ["a_NewsGoldIcon",      "Double Gold Event",     "While this event is in place all gold will be doubled world wide",       "http://www.dungeonblitz.com/", 1387602000],
    2: ["a_NewsGearIcon",      "Double Gear Event",     "While this event is in place all gear drops will be doubled world wide",  "http://www.dungeonblitz.com/", 1387602000],
    3: ["a_NewsMatsIcon",      "Double Material Event", "While this event is in place all material drops will be doubled world wide","http://www.dungeonblitz.com/",1387602000],
    4: ["a_NewsXPIcon",        "Double XP Event",       "While this event is in place all XP gained will be doubled world wide",     "http://www.dungeonblitz.com/",1387602000],
    5: ["a_NewsPetXPIcon",     "Double Pet XP Event",   "While this event is in place all pet XP gained will be doubled world wide", "http://www.dungeonblitz.com/",1387602000],
}

