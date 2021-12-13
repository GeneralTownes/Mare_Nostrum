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

buildingSlots = 16

sites = [None] * 16

def Background(x,y):
    gameDisplay.blit(islandSummer, (x,y))
    
Locations = ((838,398), (600,394))


class Building:
    
    def __init__(self, buildingType, name, location, level):
        
        self.buildingType = buildingType
        self.name = name
        self.location = location
        self.level = level
        
    def buildingGFX (self):
        buildingImage = pg.image.load( os.path.join(homeDirectory, 'gfx\\town\\buildings\\', self.name + '.png') ).convert_alpha()
        return buildingImage
    
# creating build list
buildingOrder = ["townHall", "palace"]

buildings = { }

for i in range(len(buildingOrder)):
    site = buildingOrder[i]
    buildings[site] = Building('standard', site, Locations[i], 1)
        
    
    

print (buildings)

#clickable area
click_rect  = buildings['townHall'].buildingGFX().get_rect()

crashed = False

while not crashed:
    for event in pg.event.get():
        mouse_position = pg.mouse.get_pos()
        Background(0,0)
        if event.type == pg.QUIT:
            crashed = True
        
        
        for house in buildings.values():  
            gameDisplay.blit(house.buildingGFX(), house.location) # paint to screen
                
            if( click_rect.collidepoint( np.subtract(mouse_position, house.location ) ) ):
                #gameDisplay.blit(townHall.buildingGFX(), townHall.location) # paint to screen
                imageGlow = pg.image.load( os.path.join(homeDirectory, 'gfx\\town\\buildings\\glow', house.name + 'Glow.png') ).convert_alpha()
                gameDisplay.blit(imageGlow, house.location) # paint to screen
            
        if ( event.type == pg.MOUSEBUTTONUP ):
            if ( click_rect.collidepoint( np.subtract(mouse_position, (840,400) ) ) ):   # Was that click inside our rectangle 
                display_width = 1386
                display_height = 924
                gameDisplay = pg.display.set_mode((display_width,display_height))
                islandSummer = pg.image.load(r'C:\Program Files (x86)\MareNostrum\gfx\island\background\Island1_Summer(1386x924).jpg')
        
        #print (event)
        
    pg.display.update()
    clock.tick(60)


pg.quit()