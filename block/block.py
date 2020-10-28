BLOCKS = {0: "air", 1: "stone", 2: "grass_block", 3: "dirt", 4: "cobblestone", 5: "log_1", 6: "sapling_1",
          7: "bedrock", 9: "water", 12: "sand", 13: "gravel", 14: "gold_ore", 15: "iron_ore", 16: "coal_ore", 18: "leaves_1",
          56: "diamond_ore"}


def get_block_num():
    return len(BLOCKS)


def get_block_image(data):
    return "block\\image\\" + (BLOCKS[data] if data in BLOCKS else "null") + ".png"
