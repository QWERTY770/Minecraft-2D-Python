from .chunk import Chunk
from .surface import Surface


class World:
    def __init__(self, chunk_li):
        """
        The core of game.
        chunk_li=[chunk, chunk, ... , chunk](from negative to positive)
        """
        self.li = chunk_li

    def add_negative(self, chunk):
        self.li = [chunk] + self.li

    def add_positive(self, chunk):
        self.li.append(chunk)

    def gene_negative(self):
        self.add_negative(Chunk([
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
        ))

    def gene_positive(self):
        self.add_positive(Chunk([
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
        ))

    def get_block(self, pos: tuple):
        """
        pos: (x,y)
        Return the block in this position.
        """
        lm = self.li[0].pos  # leftmost
        quo, rem = (pos[0] - lm) // 16, (pos[0] - lm) % 16
        ch = self.li[quo]
        return ch[pos[1] // 16][pos[1] % 16 * 16 + rem]

    def set_block(self, pos: tuple, data: int):
        lm = self.li[0].pos  # leftmost
        quo, rem = (pos[0] - lm) // 16, (pos[0] - lm) % 16
        ch = self.li[quo]
        ch[pos[1] // 16][pos[1] % 16 * 16 + rem] = data

    def get_blocks(self, player_pos: tuple):
        """
        player_pos: (x,y)
        Return blocks around the player.(64*40)
        """
        result = []
        for y in range(player_pos[1] - 32, player_pos[1] + 32):
            for x in range(player_pos[0] - 32, player_pos[0] + 32):
                if y < 0 or y > 255:
                    result.append(0)  # void
                    continue
                try:
                    result.append(self.get_block((x, y)))
                except IndexError:
                    self.gene_positive()
                    self.gene_negative()
                    result.append(self.get_block((x, y)))
        # print(len(result))
        return result
