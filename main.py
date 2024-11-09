#importing essential libraries
import pygame
import sys
from djungelskogs_chair import djungelskogschair 
from Ikea_drone import Ikeadrone

import pygame.ftfont   
#start game
pygame.init()

#screen size
DISPLAYSURF = pygame.display.set_mode((600,500), pygame.RESIZABLE)

pygame.display.set_caption("Djungelskog")
# loads images on your projects
djungelskog_sprite = pygame.image.load("Djungelskog.png")
djungelskog_sprite = pygame.transform.flip(djungelskog_sprite,True,False)
djungelskog_sprite = pygame.transform.scale(djungelskog_sprite, (100, 100))
djungelskog_sprite_rect = djungelskog_sprite.get_rect()
djungelskog_sprite_rect.x = 0
djungelskog_sprite_rect.y = 400

pygame.display.set_icon(djungelskog_sprite)

Ikeabackground_sprite = pygame.image.load("Ikeabackground.PNG")
Ikeabackground_sprite = pygame.transform.scale(Ikeabackground_sprite, (600, 600))


Ikeadrone_name = Ikeadrone()
#Ikeadrone_name.Ikeadrone_sprite_rect.x

# how the game runs continuously


djungelskogschairlist = [djungelskogschair()] 
















jumpswitch = False
gravity = 2
velocity = 0
def jumping ():
  global velocity, jumpswitch
  djungelskog_sprite_rect.y -= velocity
  velocity -= gravity
  if djungelskog_sprite_rect.y >= 400:
    velocity = 0 
    djungelskog_sprite_rect.y = 399   
    jumpswitch = False
  







Fullscreencheck = False
FPS = pygame.time.Clock()
#all code ends here
while True:
  # covers all possible events in the game (controls, etc.)
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()
    if event.type == pygame.KEYUP:
      if Fullscreencheck == False and event.key == pygame.K_f:
        DISPLAYSURF = pygame.display.set_mode((600,500),pygame.FULLSCREEN)
        Fullscreencheck = True
  
      elif Fullscreencheck == True and event.key == pygame.K_f:
        DISPLAYSURF = pygame.display.set_mode((600,500)), pygame.RESIZABLE
        Fullscreencheck = False
    
  keys = pygame.key.get_pressed()

  if keys[pygame.K_SPACE] and jumpswitch == False:
    jumpswitch = True
    velocity = 30
  if keys[pygame.K_DOWN]:
    pass

  if jumpswitch == True:
    jumping()
  
  
  DISPLAYSURF.blit(Ikeabackground_sprite,(0,0))
  DISPLAYSURF.blit(djungelskog_sprite,djungelskog_sprite_rect)
  Ikeadrone_name.update(DISPLAYSURF)


  
  djungelskogschairlist[0].update(DISPLAYSURF)
  djungelskogschairlist[0].djungelskogschairmovement(djungelskogschairlist)


  FPS.tick(30) 

  pygame.display.update()




