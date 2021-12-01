# Mare Nostrum

import pygame as pg
import numpy as np
import os

#initialisation
pg.init()
display_width = 1920
display_height = 1200

gameDisplay = pg.display.set_mode((display_width,display_height))
pg.display.set_caption('Mare Nostrum')
clock = pg.time.Clock()


islandSummer = pg.image.load(r'C:\\Program Files (x86)\\MareNostrum\\gfx\\town\\background\\rank_5\\Capital_R5.jpg')

homeDirectory = os.getcwd()


def Background(x,y):
    gameDisplay.blit(islandSummer, (x,y))


class Building:
    def __init__(self, buildingType, name, location, level):
        self.buildingType = buildingType
        self.name = name
        self.location = location
        self.level = level
        
    def buildingGFX (self):
        buildingImage = pg.image.load( os.path.join(homeDirectory, 'gfx\\town\\buildings\\', self.name + '.png') ).convert_alpha()
        return buildingImage

townHall = Building('standard','townHall',(838,398), 1)

#clickable area
click_rect  = townHall.buildingGFX().get_rect()

crashed = False

while not crashed:
    for event in pg.event.get():
        mouse_position = pg.mouse.get_pos()
        Background(0,0)
        if event.type == pg.QUIT:
            crashed = True
        
        elif ( event.type == pg.MOUSEBUTTONUP ):
           # mouse_position = pg.mouse.get_pos()             # Location of the mouse-click
            if ( click_rect.collidepoint( np.subtract(mouse_position, (840,400) ) ) ):   # Was that click inside our rectangle 
                display_width = 1386
                display_height = 924
                gameDisplay = pg.display.set_mode((display_width,display_height))
                islandSummer = pg.image.load(r'C:\Program Files (x86)\MareNostrum\gfx\island\background\Island1_Summer(1386x924).jpg')
                
            else:
                pass
        
        elif ( click_rect.collidepoint( np.subtract(mouse_position, (840,400) ) ) ):
            gameDisplay.blit(townHall.buildingGFX(), (838,398)) # paint to screen
            townHall_glow = pg.image.load(r'C:\Program Files (x86)\MareNostrum\gfx\town\buildings\Glow\townHallGlow.png').convert_alpha()
            gameDisplay.blit(townHall_glow, (838,398)) # paint to screen
        
        else:
            gameDisplay.blit(townHall.buildingGFX(), (838,398)) # paint to screen
            
        
    pg.display.update()
    clock.tick(60)



pg.quit()