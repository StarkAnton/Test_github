
import pygame as pg

GAMENAME = "Platformer"
WINSIZE = (160,128)
FPS = 60

##Player##
PLAYER_START_POS = [32,32]
PLAYER_IMG = pg.image.load("player.png")

##World##
TILE_IMG = {"0":pg.image.load("tile.png"),"1":pg.image.load("tile_2.png")}
TILESIZE = 16
GRID = [["0","0","0","0","0","0","0","0","0","0"],
        ["0","0","0","0","0","0","0","0","0","0"],
        ["0","0","0","0","0","0","0","0","0","0"],
        ["0","0","0","0","0","0","0","0","0","0"],
        ["0","0","0","0","0","0","0","0","0","0"],
        ["0","0","0","0","0","0","0","0","0","0"],
        ["0","0","0","0","0","0","0","0","0","0"],
        ["0","0","0","1","1","1","0","0","0","0"]]
#TILESIZE =
