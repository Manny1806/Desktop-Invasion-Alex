import sys

import pygame

def run_game():
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Desktop Invasion")

    while True:
        for event in pygame.event.get():
            sys.exit()
        
        pygame.display.flip()

run_game()