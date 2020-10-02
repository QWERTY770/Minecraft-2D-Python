from block import block as bk


class Player:
    def __init__(self, x=0, y=64, block=1):
        self.x = x
        self.y = y
        self.block = block  # the order of block, not id

    def get_pos(self):
        return self.x, self.y

    def inc_block(self):
        if self.block == bk.get_block_num() - 1:
            self.block = 1
        else:
            self.block += 1

    def dec_block(self):
        if self.block == 1:
            self.block = bk.get_block_num() - 1
        else:
            self.block -= 1
