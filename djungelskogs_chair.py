
import pygame

'''
TODO:
make it move foward towards djungelskog.
make it go faster the longer you play.
make it kill djugnelskog on touch.
make it spawn.

Code stuff
while True:
    def djungelskogchairmove (self):
        djugnelskgchair_sprite_rect.x -= -1 


'''

class djungelskogschair:
    def __init__ (self):
        self.djungelskogschair_sprite = pygame.image.load("Djungelskogschair.png")
        self.djungelskogschair_sprite = pygame.transform.scale(self.djungelskogschair_sprite,(100,100))
        self.djungelskogschair_sprite_rect = self.djungelskogschair_sprite.get_rect()
        self.djungelskogschair_sprite_rect.x = 500
        self.djungelskogschair_sprite_rect.y = 400
    '''
    parameter: a placeholder variable with no data. Think of it as a template
    '''
    def djungelskogschairmovement(self, list):
        self.djungelskogschair_sprite_rect.x -= 10
        if self.djungelskogschair_sprite_rect.x == 0:
            list.remove(self)


    def update(self,screen):
        screen.blit(self.djungelskogschair_sprite,self.djungelskogschair_sprite_rect)
        






















