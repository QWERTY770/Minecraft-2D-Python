BLOCKS = {0: "air", 1: "stone", 2: "grass_block", 3: "dirt", 4: "cobblestone", 5: "log_1", 6: "sapling_1",
          7: "bedrock", 12: "sand", 15: "iron_ore", 18: "leaves_1"}


def getBlockNum():
    return len(BLOCKS)


def getBlockImage(data):
    return "block\\image\\" + (BLOCKS[data] if data in BLOCKS else "null") + ".png"
