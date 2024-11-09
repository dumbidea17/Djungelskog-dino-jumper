import pygame


class Ikeadrone:
    def __init__ (self):
        self.Ikeadrone_sprite = pygame.image.load("Ikeadrone.png")
        self.Ikeadrone_sprite = pygame.transform.scale(self.Ikeadrone_sprite, (100, 100))
        self.Ikeadrone_sprite_rect = self.Ikeadrone_sprite.get_rect()
        self.Ikeadrone_sprite_rect.x = 500
        self.Ikeadrone_sprite_rect.y = 350

    def update (self,screen):
        screen.blit(self.Ikeadrone_sprite, self.Ikeadrone_sprite_rect)
