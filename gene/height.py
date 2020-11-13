from random import random
from world.surface import Surface
from world.chunk import Chunk
SEA_LEVEL = 62


def get_height_16():
    """
    heights of 16 blocks (1 chunk)
    """
    result1 = [(0.56 + random() * 0.88) * SEA_LEVEL]
    for i in range(15):
        result1.append(result1[i] * (0.95 + random() * 0.1))
    result2 = [(0.56 + random() * 0.88) * SEA_LEVEL]
    for i in range(15):
        result2.append(result2[i] * (0.95 + random() * 0.1))
    result3 = [(0.56 + random() * 0.88) * SEA_LEVEL]
    for i in range(15):
        result3.append(result1[i] * (0.95 + random() * 0.1))
    result3 = result3[::2] + result3[1:][::2]
    r = [round((x + y + z)/3) for x, y, z in zip(result1, result2, result3)]
    if abs(r[0] - r[1]) > 3:
        r[0] = r[1]
    return r


def get_blocks_1(h):
    """
    return blocks in 256*1*1
    """
    res = []
    for i in range(256):
        if i == 0:
            res.append(7)
            continue
        if i < h - 4:
            res.append(1)
        elif i < h - 1:
            if i >= 58:
                res.append(3)
            else:
                res.append(13)
        elif i < h:
            if i >= 61:
                res.append(2)
            else:
                res.append(13)
        else:
            if i >= 62:
                res.append(0)
            else:
                res.append(9)
    return res


def get_chunk(hli, pos):
    a = [get_blocks_1(i) for i in hli]
    result = []
    temp = []
    for i in range(16):
        for j in range(16):
            temp += [s[i * 16 + j] for s in a]
        result.append(Surface(temp))
        temp = []
    del temp
    return Chunk(result, pos)
