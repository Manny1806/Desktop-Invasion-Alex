import sys
from ship import RecycleShip
from settings import Settings
from pygame.sprite import Group
from game_stats import GameStats
from button import Button
# from shortcut import Shortcut
import pygame
import game_functions as gf


bg = pygame.image.load("images/background.jpg")

def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((1200, 700))
    pygame.display.set_caption("Desktop Invasion")

    play_button = Button(ai_settings, screen, "Play")

    stats = GameStats(ai_settings)

    #create a recycle ship
    ship = RecycleShip(ai_settings, screen)

    #create group of bullets and shortcuts
    bullets = Group()
    shortcuts = Group()

    #creat a shortcut
    # shortcut = Shortcut(ai_settings, screen)

    #create fleet 
    gf.create_fleet(ai_settings, screen, ship, shortcuts)

    while True:
        gf.check_events(ai_settings, screen, stats, play_button, ship, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, ship, shortcuts, bullets)
            gf.update_shortcuts(ai_settings, stats, screen, ship, shortcuts, bullets)

        gf.update_screen(bg, screen, stats, ship, shortcuts, bullets, play_button)

run_game()