import pygame

from world.chunk import Chunk
from world.world import World
from world.surface import Surface
from block.block import *
from entity.player import *
from world.saves import *
import tkinter as tk
import tkinter.filedialog as tkfd

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
bg_bg_font = pygame.font.SysFont("simhei", 100)
clock = pygame.time.Clock()
pygame.display.set_caption("Minecraft 2D Python 0.2.1 (v6)")
pygame.display.set_icon(pygame.image.load("block\\image\\grass_block.png"))
long_press = False

block_keys = list(BLOCKS.keys())
player = Player(0, 64)
screen = pygame.display.set_mode((1500, 750))
condition = 0
world_path = ""


def show_world(li):
    r = 0
    for y in range(50, 818, 16):
        for x in range(50, 1074, 16):
            if li[r] == 0:
                r += 1
                continue
            screen.blit(pygame.image.load(get_block_image(li[r])), (x, 800 - y))
            r += 1
    x, y = 562, 302  # the position of entity
    pygame.draw.line(screen, green, (x, y), (x, y + 16), 2)
    pygame.draw.line(screen, green, (x, y), (x + 16, y), 2)
    pygame.draw.line(screen, green, (x + 16, y), (x + 16, y + 16), 2)
    pygame.draw.line(screen, green, (x, y + 16), (x + 16, y + 16), 2)
    block_im = pygame.image.load("block\\image\\" + BLOCKS[block_keys[player.block]] + ".png")
    screen.blit(pygame.transform.scale(block_im, (50, 50)), (1450, 0))


def show(tp, word, color1, color2=None):
    return tp.render(word, True, color1, color2)


def buttons():
    if long_press:
        screen.blit(show(font, "关闭长按", black, white), (1150, 350))
    else:
        screen.blit(show(font, "开启长按", black, white), (1150, 350))
    screen.blit(show(font, "保存存档", black, white), (1150, 400))
    screen.blit(show(font, "回到菜单", black, white), (1150, 450))


def start_menu_blit():
    _i = pygame.image.load(get_block_image(3))
    for y in range(0, 768, 16):
        for x in range(0, 1516, 16):
            screen.blit(_i, (x, y))
    del _i
    screen.blit(show(bg_bg_font, "Minecraft 2D", (165, 165, 165)), (400, 50))
    screen.blit(show(bg_font, "Python Edition", (135, 135, 135)), (480, 150))
    screen.blit(show(font, "          打开存档          ", white, grey), (480, 300))  # 10 spaces
    screen.blit(show(font, "          新的存档          ", white, grey), (480, 350))  # 10 spaces
    screen.blit(show(font, "          退出游戏          ", white, grey), (480, 400))


def show_tk():
    global condition, world_path
    condition = 1
    main_box = tk.Tk()
    path = tk.StringVar()
    tk.Label(main_box, text="目标路径:").grid(row=0, column=0)
    tk.Entry(main_box, textvariable=path).grid(row=0, column=1)
    tk.Button(main_box, text="路径选择",
              command=path.set(tkfd.askopenfilename().replace("/", "\\\\"))).grid(row=0, column=2)
    condition = 2
    world_path = path.get()
    main_box.destroy()


# mainloop
while True:
    clock.tick(60)
    pygame.display.update()
    screen.fill(blue)
    if condition == 2:
        show_world(world.get_blocks(player.get_pos()))
        buttons()
        screen.blit(show(font, str(player.get_pos()), white), (0, 0))
    else:
        start_menu_blit()
    if long_press and condition == 2:
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_w]:  # w
            player.y += 1 if player.y < 255 else 0
        elif keys_pressed[pygame.K_s]:  # s
            player.y -= 1 if player.y > 0 else 0
        elif keys_pressed[pygame.K_a]:  # a
            player.x -= 1
        elif keys_pressed[pygame.K_d]:  # d
            player.x += 1
        elif keys_pressed[pygame.K_EQUALS]:  # =
            player.inc_block()
        elif keys_pressed[pygame.K_MINUS]:  # -
            player.dec_block()
        elif keys_pressed[pygame.K_F12]:
            world.get_block_debug(player.get_pos())
    for event in pygame.event.get():
        if condition == 2:
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 1150 < pygame.mouse.get_pos()[0] < 1270:
                    if 350 < pygame.mouse.get_pos()[1] < 380:
                        long_press = not long_press
                        break
                    if 400 < pygame.mouse.get_pos()[1] < 430:
                        write_save(world_path, str(world))
                        break
                    if 450 < pygame.mouse.get_pos()[1] < 480:
                        condition = 0
                        break
                if event.button == 1:  # mouse left click
                    world.set_block(player.get_pos(), 0)
                if event.button == 3:  # mouse right click
                    world.set_block(player.get_pos(), block_keys[player.block])
            if not long_press and event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    player.y += 1 if player.y < 255 else 0
                elif event.key == pygame.K_s:
                    player.y -= 1 if player.y > 0 else 0
                elif event.key == pygame.K_a:
                    player.x -= 1
                elif event.key == pygame.K_d:
                    player.x += 1
                elif event.key == pygame.K_EQUALS:
                    player.inc_block()
                elif event.key == pygame.K_MINUS:
                    player.dec_block()
                elif event.key == pygame.K_F12:
                    world.get_block_debug(player.get_pos())
        elif condition == 0:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 400 < pygame.mouse.get_pos()[0] < 900:
                    if 300 < pygame.mouse.get_pos()[1] < 330:
                        show_tk()
                        world = str_to_world(read_save(world_path))
                        break
                    if 350 < pygame.mouse.get_pos()[1] < 380:
                        world = World([])
                        world.gene_positive()
                        world.gene_positive()
                        world.gene_negative()
                        world.gene_negative()
                        write_save("saves\\not_named.mc2d", str(world))
                        world_path = "saves\\not_named.mc2d"
                        condition = 2
                    if 400 < pygame.mouse.get_pos()[1] < 430:
                        exit()
            if event.type == pygame.QUIT:
                exit()
