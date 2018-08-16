import sys
from bullet import Bullet
from shortcut import Shortcut
import pygame

def check_events(ai_settings, screen, ship, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        
def check_keydown_events(event, ai_settings, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)

def fire_bullet(ai_settings, screen, ship, bullets):
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def update_bullets(bullets):
    bullets.update()
    #get rid of bullets that leave screen
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

def update_screen(bg, screen, ship, shortcuts, bullets):
    screen.blit(bg, (0, 0))
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    shortcuts.draw(screen)
    pygame.display.flip()

def get_number_shortcuts_x(ai_settings, shortcut_width):
    available_space_x = ai_settings.screen_width - 2 * shortcut_width
    number_shortcuts_x = int(available_space_x / (2 * shortcut_width))
    return number_shortcuts_x

def create_shortcut(ai_settings, screen, shortcuts, shortcut_number):
    shortcut = Shortcut(ai_settings, screen)
    shortcut_width = shortcut.rect.width
    shortcut.x = shortcut_width + 2 * shortcut_width * shortcut_number
    shortcut.rect.x = shortcut.x
    shortcuts.add(shortcut)

def create_fleet(ai_settings, screen, shortcuts):
    shortcut = Shortcut(ai_settings, screen)
    number_shortcuts_x = get_number_shortcuts_x(ai_settings, shortcut.rect.width)
    # shortcut_width = shortcut.rect.width
    
    #create first row of shortcuts
    for shortcut_number in range(number_shortcuts_x):
        create_shortcut(ai_settings, screen, shortcuts, shortcut_number)