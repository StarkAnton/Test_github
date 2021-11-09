import settings




def draw_grid(self):
        for row in range(0,self.background_grid_size + 1):
            y = row * settings.TILESIZE
            for tile in range(0,self.background_grid_size + 1):
                x = tile*settings.TILESIZE
                pg.draw.rect(self.screen, settings.BLACK,pg.Rect(x, y, settings.TILESIZE, settings.TILESIZE))
