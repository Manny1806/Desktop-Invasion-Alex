import sys
from bullet import Bullet
from shortcut import Shortcut
from clippy import Clippy
from time import sleep
import pygame

def check_events(ai_settings, screen, stats, play_button, ship, shortcuts, bullets, pygame, clippy):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats, play_button, ship, shortcuts, bullets, mouse_x, mouse_y, pygame, clippy)
            
def check_play_button(ai_settings, screen, stats, play_button, ship, shortcuts, bullets, mouse_x, mouse_y, pygame, clippy):
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        ai_settings.initialize_dynamic_settings()

        pygame.mouse.set_visible(False)

        stats.reset_stats()
        stats.game_active = True

        shortcuts.empty()
        bullets.empty()

        clippy.empty()
        clip = Clippy(ai_settings, screen)
        clippy.add(clip)

        create_fleet(ai_settings, screen, ship, shortcuts)
        ship.center_ship()

        pygame.mixer.music.load('game.mp3')
        pygame.mixer.music.play(-1)
        
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

def update_bullets(ai_settings, screen, stats, sb, ship, shortcuts, bullets, clippy):
    bullets.update()
    #get rid of bullets that leave screen
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    check_bullet_shortcut_collisions(ai_settings, screen, stats, sb, ship, shortcuts, bullets, clippy)

def check_bullet_shortcut_collisions(ai_settings, screen, stats, sb, ship, shortcuts, bullets, clippy):
    collisions = pygame.sprite.groupcollide(bullets, shortcuts, True, True)
    collisions2 = pygame.sprite.groupcollide(bullets, clippy, True, True)

    if collisions:
        stats.score += ai_settings.shortcut_points
        sb.prep_score()

    if collisions2:
        stats.score += ai_settings.clippy_points
        sb.prep_score()

    if len(shortcuts) == 0:
        clippy.empty()
        clip = Clippy(ai_settings, screen)
        clippy.add(clip)
        ai_settings.clippy_moving = False
        bullets.empty()
        ai_settings.increase_speed()
        create_fleet(ai_settings, screen, ship, shortcuts)
    
    if len(shortcuts) == 15:
        ai_settings.clippy_moving = True



def update_screen(bg, screen, stats, sb, ship, shortcuts, bullets, play_button, clippy):
    screen.blit(bg, (0, 0))
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    shortcuts.draw(screen)
    clippy.draw(screen)
    sb.show_score()
    if not stats.game_active:
        play_button.draw_button()

    pygame.display.flip()

def get_number_shortcuts_x(ai_settings, shortcut_width):
    available_space_x = ai_settings.screen_width - 2 * shortcut_width
    number_shortcuts_x = int(available_space_x / (2 * shortcut_width))
    return number_shortcuts_x

def create_shortcut(ai_settings, screen, shortcuts, shortcut_number, row_number):
    shortcut = Shortcut(ai_settings, screen)
    shortcut_width = shortcut.rect.width
    shortcut.x = shortcut_width + 2 * shortcut_width * shortcut_number
    shortcut.rect.x = shortcut.x
    shortcut.rect.y = shortcut.rect.height + 2 * shortcut.rect.height * row_number
    shortcuts.add(shortcut)

def create_fleet(ai_settings, screen, ship, shortcuts):
    shortcut = Shortcut(ai_settings, screen)
    number_shortcuts_x = get_number_shortcuts_x(ai_settings, shortcut.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height, shortcut.rect.height)
    
    #create first row of shortcuts
    for row_number in range(number_rows):
        for shortcut_number in range(number_shortcuts_x):
            create_shortcut(ai_settings, screen, shortcuts, shortcut_number, row_number)

def get_number_rows(ai_settings, ship_height, shortcut_height):
    available_space_y = (ai_settings.screen_height - (3 * shortcut_height) - ship_height)
    number_rows = int(available_space_y / (2 * shortcut_height))
    return number_rows

def check_fleet_edges(ai_settings, shortcuts):
    for shortcut in shortcuts.sprites():
        if shortcut.check_edges():
            change_fleet_direction(ai_settings, shortcuts)
            break

def change_fleet_direction(ai_settings, shortcuts):
    for shortcut in shortcuts.sprites():
        shortcut.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1

def ship_hit(ai_settings, stats, screen, ship, shortcuts, bullets):
    if stats.ships_left > 0:
        stats.ships_left -= 1

        shortcuts.empty()
        bullets.empty()

        create_fleet(ai_settings, screen, ship, shortcuts)
        ship.center_ship()

        sleep(0.5)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)
        pygame.mixer.music.load('menu.mp3')
        pygame.mixer.music.play(-1)   

def update_shortcuts(ai_settings, stats, screen, ship, shortcuts, bullets):
    check_shortcuts_bottom(ai_settings, stats, screen, ship, shortcuts, bullets)
    check_fleet_edges(ai_settings, shortcuts)
    shortcuts.update()

    if pygame.sprite.spritecollideany(ship, shortcuts):
        ship_hit(ai_settings, stats, screen, ship, shortcuts, bullets)
        print("Recycle Ship Hit!!!")

def check_shortcuts_bottom(ai_settings, stats, screen, ship, shortcuts, bullets):
    screen_rect = screen.get_rect()
    for shortcut in shortcuts.sprites():
        if shortcut.rect.bottom >= screen_rect.bottom:
            ship_hit(ai_settings, stats, screen, ship, shortcuts, bullets)
            break

#  def activate_clippy():
#      if state.ships_left < 10:


