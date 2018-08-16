import sys
from ship import RecycleShip
from settings import Settings
from pygame.sprite import Group
# from shortcut import Shortcut
import pygame
import game_functions as gf


bg = pygame.image.load("images/background.jpg")

def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((1200, 700))
    pygame.display.set_caption("Desktop Invasion")

    #create a recycle ship
    ship = RecycleShip(ai_settings, screen)

    #create group of bullets and shortcuts
    bullets = Group()
    shortcuts = Group()

    #creat a shortcut
    # shortcut = Shortcut(ai_settings, screen)

    #create fleet 
    gf.create_fleet(ai_settings, screen, shortcuts)

    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(bg, screen, ship, shortcuts, bullets)

run_game()