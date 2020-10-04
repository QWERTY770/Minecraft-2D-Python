from block import block as bk


class Player:
    def __init__(self, x=0, y=64, block=1):
        self.X = x
        self.Y = y
        self.block = block  # the order of block, not id

    def getPos(self):
        return self.x, self.y

    def incBlock(self):
        if self.block == bk.getBlockNum() - 1:
            self.block = 1
        else:
            self.block += 1

    def decBlock(self):
        if self.block == 1:
            self.block = bk.getBlockNum() - 1
        else:
            self.block -= 1
