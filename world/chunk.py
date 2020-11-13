class Chunk:
    def __init__(self, surface_li: list, pos: int):
        """

        :param surface_li: 16 surfaces (world.surface.Surface object)
        :param pos: position of the leftmost block
        """
        self.li = surface_li
        self.pos = pos

    def __getitem__(self, item):
        return self.li[item]

    def put(self, h, pl, data):
        self[h].put(pl, data)

    def destroy(self, h, pl):
        self[h].destroy(pl)
