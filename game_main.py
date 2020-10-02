import pygame

from world.chunk import Chunk
from world.world import World
from world.surface import Surface
from block.block import *
from player.player_main import *

yellow = (255, 255, 0)
blue = (0, 200, 200)
white = (255, 255, 255)
orange = (255, 165, 0)
dark_orange = (150, 80, 0)
green = (0, 255, 0)
red = (255, 0, 0)
grey = (150, 150, 150)
black = (0, 0, 0)
# color

pygame.init()
sm_font = pygame.font.SysFont("simhei", 20)
font = pygame.font.SysFont("simhei", 30)
bg_font = pygame.font.SysFont("simhei", 60)
clock = pygame.time.Clock()
pygame.display.set_caption("Minecraft 2D Python 0.0.1")

block_keys = list(BLOCKS.keys())
player = Player(0, 64)
screen = pygame.display.set_mode((1500, 800))
world = World([])
world.gene_negative()
world.gene_negative()
world.gene_positive()
world.gene_positive()
# -32 to 32


def show_world(li):
    r = 0
    for y in range(50, 1074, 16):
        for x in range(50, 1074, 16):
            if li[r] == 0:
                r += 1
                continue
            screen.blit(pygame.image.load(get_block_image(li[r])), (x, 800 - y))
            r += 1
    x, y = 562, 238  # the position of player
    pygame.draw.line(screen, green, (x, y), (x, y + 16), 2)
    pygame.draw.line(screen, green, (x, y), (x + 16, y), 2)
    pygame.draw.line(screen, green, (x + 16, y), (x + 16, y + 16), 2)
    pygame.draw.line(screen, green, (x, y + 16), (x + 16, y + 16), 2)
    block_im = pygame.image.load("block\\image\\" + BLOCKS[block_keys[player.block]] + ".png")
    screen.blit(pygame.transform.scale(block_im, (32, 32)), (1300, 100))


# mainloop
while True:
    clock.tick(45)
    pygame.display.update()
    screen.fill(blue)
    show_world(world.get_blocks(player.get_pos()))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_w:  # w
            player.y += 1 if player.y < 255 else 0
        if event.type == pygame.KEYDOWN and event.key == pygame.K_s:  # s
            player.y -= 1 if player.y > 0 else 0
        if event.type == pygame.KEYDOWN and event.key == pygame.K_a:  # a
            player.x -= 1
        if event.type == pygame.KEYDOWN and event.key == pygame.K_d:  # d
            player.x += 1
        if event.type == pygame.KEYDOWN and event.key == pygame.K_EQUALS:  # =
            player.inc_block()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_MINUS:  # -
            player.dec_block()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # mouse left click
            world.set_block(player.get_pos(), 0)
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:  # mouse right click
            world.set_block(player.get_pos(), block_keys[player.block])
