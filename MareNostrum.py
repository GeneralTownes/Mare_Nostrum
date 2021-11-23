# Mare Nostrum

import pygame as pg
import numpy as np

#initialisation
pg.init()
display_width = 1920
display_height = 1200

gameDisplay = pg.display.set_mode((display_width,display_height))
pg.display.set_caption('Mare Nostrum')
clock = pg.time.Clock()


islandSummer = pg.image.load(r'C:\Program Files (x86)\MareNostrum\gfx\backgrounds\CapitalBackgound.jpg')



def Background(x,y):
    gameDisplay.blit(islandSummer, (x,y))




Background(0,0)



townHall = pg.image.load(r'C:\Program Files (x86)\MareNostrum\gfx\town\TownHall.png').convert_alpha()

gameDisplay.blit(townHall, (840,400)) # paint to screen
pg.display.flip() # paint screen one time

#clickable area
click_rect  = townHall.get_rect()

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
                #print( "hit" )
                display_width = 1386
                display_height = 924
                gameDisplay = pg.display.set_mode((display_width,display_height))
                islandSummer = pg.image.load(r'C:\Program Files (x86)\MareNostrum\gfx\backgrounds\Island1_Summer(1386x924).jpg')
                
            else:
                print( "click-outside!" )
        
        elif ( click_rect.collidepoint( np.subtract(mouse_position, (840,400) ) ) ):
            print( "hover" )
            townHall = pg.image.load(r'C:\Program Files (x86)\MareNostrum\gfx\town\GovernorsResidence.png').convert_alpha()
            gameDisplay.blit(townHall, (828,395)) # paint to screen
        
        else:
            print( "not hover" )
            townHall = pg.image.load(r'C:\Program Files (x86)\MareNostrum\gfx\town\TownHall.png').convert_alpha()
            gameDisplay.blit(townHall, (840,400)) # paint to screen
            
        
       # print (event)
        
    pg.display.update()
    clock.tick(60)

pg.quit()