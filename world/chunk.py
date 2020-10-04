class Chunk:
    def __init__(self, surface_li, pos):
        """
        Create a 16*256*1 chunk.
        li=surface*16 button to top
        pos:The position of the leftmost block.
        """
        self.li = surface_li
        self.pos = pos

    def __getItem__(self, item):
        return self.li[item]

    def put(self, h, pl, data):
        self[h].put(pl, data)

    def destroy(self, h, pl):
        self[h].destroy(pl)
