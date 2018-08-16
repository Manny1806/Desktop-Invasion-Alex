import pygame
from pygame.sprite import Sprite

class Shortcut(Sprite):
    def __init__(self, ai_settings, screen):
        super(Shortcut, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        #load the shortcut images
        self.image = pygame.image.load('images/ie.png')
        self.rect = self.image.get_rect()

        #start each new shortcut near the top left of screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #store the shortcut's exact position
        self.x = float(self.rect.x)
    
    def blitme(self):
        self.screen.blit(self.image, self.rect)