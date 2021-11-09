import pygame as pg
import settings

class Player:

    def __init__(self):
        self.pos = settings.PLAYER_START_POS
        self.player_img = settings.PLAYER_IMG

    def render(self,screen):
        screen.blit(self.player_img,(self.pos[0],self.pos[1]))

class World:

    def __init__(self):
        self.grid = settings.GRID
        self.tile_img = settings.TILE_IMG
        self.tilesize = settings.TILESIZE

    def render(self,screen):
        for i, row in enumerate(self.grid):
            y = i * self.tilesize
            for j,tile_value in enumerate(row):
                x = j * self.tilesize
                screen.blit(self.tile_img[tile_value],(x,y))
