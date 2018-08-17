import pygame
import random
from pygame.sprite import Sprite
class Clippy(Sprite):

    def __init__(self, ai_settings, screen):
        super(Clippy, self).__init__()
        """Initialize the RecycleShip and set its starting position"""
        self.screen = screen
        self.ai_settings = ai_settings
        #load the recycle ship image and get its rect
        self.image = pygame.image.load('images/clippy.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.moving_right = random.choice([True, False])
        self.moving_left = not self.moving_right

        self.rect.centerx = 0
        if self.moving_right:
            self.rect.centerx = -50
        else:
            self.rect.centerx = 1250
        self.rect.bottom = 100

        self.center = float(self.rect.centerx)

        

    def update(self, ai_settings):
        if ai_settings.clippy_moving:
            if self.moving_right and self.rect.right < self.screen_rect.right + 100:
                self.center += self.ai_settings.clippy_speed_factor
            elif self.moving_right and self.rect.right > self.screen_rect.right + 100:
                self.ai_settings.clippy_moving = False
            if self.moving_left and self.rect.left > -100:
                self.center -= self.ai_settings.clippy_speed_factor
            elif self.moving_left and self.rect.left < -100:
                self.ai_settings.clippy_moving = False


        self.rect.centerx = self.center

    def blitme(self):
        self.screen.blit(self.image, self.rect)