from .chunk import Chunk
from .surface import Surface
from gene.gene_main import *
RANDOM = 1


class World:
    def __init__(self, chunk_li):
        """
        The core of game.
        chunk_li=[chunk, chunk, ... , chunk](from negative to positive)
        """
        self.li = chunk_li
        self.hli = []

    def gene_negative(self):
        if RANDOM:
            f = gene_chunk(self.li[0].pos - 16 if self.li != [] else -16)
            self.li, self.hli = [f[0]] + self.li, f[1] + self.hli
        if not RANDOM:
            self.li = [Chunk([
                Surface([0] * 16 + [1] * 240),
                Surface([1] * 256),
                Surface([1] * 256),
                Surface([1] * 192 + [3] * 48 + [2] * 16),
                Surface([0] * 256),
                Surface([0] * 256),
                Surface([0] * 256),
                Surface([0] * 256),
                Surface([0] * 256),
                Surface([0] * 256),
                Surface([0] * 256),
                Surface([0] * 256),
                Surface([0] * 256),
                Surface([0] * 256),
                Surface([0] * 256),
                Surface([0] * 256),
            ], self.li[0].pos - 16 if self.li != [] else -16
            )] + self.li
            self.hli = [64] * 16 + self.hli
            print(self.hli)

    def gene_positive(self):
        if RANDOM:
            f = gene_chunk(self.li[0].pos + 16 if self.li != [] else 0)
            self.li, self.hli = self.li + [f[0]], self.hli + f[1]
        if not RANDOM:
            self.li = self.li + [Chunk([
                Surface([0] * 16 + [1] * 240),
                Surface([1] * 256),
                Surface([1] * 256),
                Surface([1] * 192 + [3] * 48 + [2] * 16),
                Surface([0] * 256),
                Surface([0] * 256),
                Surface([0] * 256),
                Surface([0] * 256),
                Surface([0] * 256),
                Surface([0] * 256),
                Surface([0] * 256),
                Surface([0] * 256),
                Surface([0] * 256),
                Surface([0] * 256),
                Surface([0] * 256),
                Surface([0] * 256),
            ], self.li[-1].pos + 16 if self.li != [] else 0
            )]
            self.hli = self.hli + [64] * 16

    def get_block(self, pos: tuple):
        """
        pos: (x,y)
        Return the block in this position.
        """
        quo = (pos[0] - self.li[0].pos) // 16
        if quo < 0:
            raise IndexError
        return self.li[quo][pos[1] // 16][pos[1] % 16 * 16 + (pos[0] - self.li[0].pos) % 16]

    def get_block_debug(self, pos):  # debug
        lm = self.li[0].pos  # leftmost
        quo, rem = (pos[0] - lm) // 16, (pos[0] - lm) % 16
        ch = self.li[quo]
        print(f"leftmost:{lm}\nquotient:{quo}\nreminder:{rem}\n"
              f"chunk_pos:{ch.pos}\ninfo:{pos[1] // 16}\n"
              f"result:{ch[pos[1] // 16][pos[1] % 16 * 16 + rem]}")

    def set_block(self, pos: tuple, data: int):
        lm = self.li[0].pos  # leftmost
        ch = self.li[(pos[0] - lm) // 16]
        ch[pos[1] // 16][pos[1] % 16 * 16 + (pos[0] - lm) % 16] = data

    def get_blocks(self, player_pos: tuple):
        """
        player_pos: (x,y)
        Return blocks around the player.(64*48)
        """
        try:
            self.get_block((player_pos[0] - 32, player_pos[1] - 28))
        except IndexError:
            self.gene_negative()
            self.gene_negative()
        try:
            self.get_block((player_pos[0] + 31, player_pos[1] - 28))
        except IndexError:
            self.gene_positive()
            self.gene_positive()
        result = []
        append = result.append
        get_block = self.get_block
        for y in range(player_pos[1] - 28, player_pos[1] + 20):
            for x in range(player_pos[0] - 32, player_pos[0] + 32):
                if y < 0 or y > 255:
                    append(0)  # void
                    continue
                append(get_block((x, y)))
        # print(len(result))
        return result
