class Surface:
    def __init__(self, li: list):
        """

        :param li: 16*16 blocks
        """
        self.li = li

    def __getitem__(self, item):
        return self.li[item]

    def __setitem__(self, key, value):
        self.li[key] = value

    def __contains__(self, item):
        return item in self.li

    def __str__(self):
        return str(self.li)

    def put(self, pl, data):
        self[pl] = data

    def destroy(self, pl):
        self[pl] = 0
