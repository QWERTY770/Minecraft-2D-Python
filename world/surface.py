class Surface:
    def __init__(self, li):
        """
        Create a 16*16*1 surface.
        li=[data, data, data, ..., data,
        data, data, data, ..., data,
        ...
        data, data, data, ..., data,] button to top

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
