import pygame
import sys
from settings import Settings
from bullet import Bullet
def check_events(ai_settings, screen, ship, bullets):
    # Обрабатывает нажатия клавиш и события мыши
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        # Движение
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event=event, ship=ship, ai_settings=ai_settings, screen=screen, bullets=bullets)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
def update_screen(ai_settings, screen, ship, bullets):
    screen.fill(ai_settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    pygame.display.flip()

def check_keydown_events(event, ship, ai_settings, screen, bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    if event.key == pygame.K_UP:
        ship.moving_up = True
    elif event.key == pygame.K_DOWN:
        ship.moving_down = True

    if event.key == pygame.K_SPACE:
        new_bullet = Bullet(ai_settings=ai_settings, ship=ship, screen=screen)
        bullets.add(new_bullet)


    """if event.key == pygame.K_KP6:
        bullet.moving_right = True
    elif event.key == pygame.K_KP4:
        bullet.moving_left = True
    if event.key == pygame.K_KP8:
        bullet.moving_up = True
    elif event.key == pygame.K_KP5:
        bullet.moving_down = True"""

def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

    if event.key == pygame.K_UP:
        ship.moving_up = False
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False

    """if event.key == pygame.K_KP6:
        bullet.moving_right = False
    elif event.key == pygame.K_KP4:
        bullet.moving_left = False
    if event.key == pygame.K_KP8:
        bullet.moving_up = False
    elif event.key == pygame.K_KP5:
        bullet.moving_down = False"""

