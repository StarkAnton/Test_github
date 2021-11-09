import pygame as pg
import settings
import assets


class Game:

    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode(settings.WINSIZE)
        pg.display.set_caption(settings.GAMENAME)
        self.clock = pg.time.Clock()
    def run(self):
        self.playing = True
        while self.playing:
            self.check_events()
            self.update()
            world.render(self.screen)
            player.render(self.screen)
    def check_events(self):
        #player.move(pg.event.get())
        self.events = pg.event.get()
        for event in self.events:
            if event.type == pg.QUIT:
                self.playing = False

    def update(self):
        pg.display.update()
        self.clock.tick(settings.FPS)

    def quit(self):
        if not self.playing:
            pg.quit()

world = assets.World()
player = assets.Player()
game = Game()
game.run()
game.quit()
