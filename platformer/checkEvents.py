import pygame as pg
def check(events):
    #print("hej")
    #print(events)
    for event in events:
        if event.type == pg.QUIT:
            return False
        else:
            return True
