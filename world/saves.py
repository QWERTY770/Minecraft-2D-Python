from .chunk import Chunk
from .surface import Surface
from .world import World
from os import listdir


def str_to_world(s: str):
    surfaces = []
    surface_list = s.split("\n")[:-2]
    lm = int(s.split("\n")[-2]) - 16
    hli = eval(s.split("\n")[-1])
    for i in surface_list:
        surfaces.append(eval(i))
    _c = []
    chunks = []
    for i, j in enumerate(surfaces):
        if i != 0 and not i % 16:
            chunks.append(Chunk(_c, lm + i // 16 * 16))
            _c = [Surface(j)]
        else:
            _c.append(Surface(j))
    chunks.append(Chunk(_c, (lm + len(surfaces) - 1) // 16 * 16))
    res = World(chunks)
    res.hli = hli
    return res


def find_all_saves():
    return ["saves\\" + i for i in listdir("saves") if ".mc2d" in i]


def read_save(path):
    with open(path, "r", encoding="utf-8") as f:
        r = f.read()
    return r


def write_save(path, s):
    with open(path, "w", encoding="utf-8") as f:
        f.write(s)
