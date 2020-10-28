from .height import *


def gene_chunk(pos):
    f = get_height_16()
    return get_chunk(f, pos), f
