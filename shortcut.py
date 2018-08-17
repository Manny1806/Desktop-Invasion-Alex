import pygame
import random
from pygame.sprite import Sprite
from icon_list import IconList


class Shortcut(Sprite):
    def __init__(self, ai_settings, screen):
        super(Shortcut, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        icon_list = IconList()
        #load the shortcut images
        self.image = pygame.image.load('images/icons/' + random.choice(icon_list.icon_list))
        self.rect = self.image.get_rect()

        #start each new shortcut near the top left of screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #store the shortcut's exact position
        self.x = float(self.rect.x)
    
    def update(self):
        self.x += (self.ai_settings.shortcut_speed_factor * self.ai_settings.fleet_direction)
        self.rect.x = self.x

    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True
    
    def blitme(self):
        self.screen.blit(self.image, self.rect)