import pygame
import sys
from settings import Settings
from bullet import Bullet
from alien import Alien

number = 0
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
def update_screen(ai_settings, screen, ship, bullets, aliens):
    screen.fill(ai_settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()
    aliens.draw(screen)
    pygame.display.flip()

def check_keydown_events(event, ship, ai_settings, screen, bullets):
    if event.key == pygame.K_q:
        sys.exit()
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    if event.key == pygame.K_UP:
        ship.moving_up = True
    elif event.key == pygame.K_DOWN:
        ship.moving_down = True

    if event.key == pygame.K_SPACE:
        fire_bullet(bullets=bullets, ai_settings=ai_settings, ship=ship, screen=screen)


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

def update_bullets(bullets):
    bullets.update()

    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

def fire_bullet(bullets, ai_settings, ship, screen):
    if (len(bullets) < ai_settings.bullets_allowed):
        new_bullet = Bullet(ai_settings=ai_settings, ship=ship, screen=screen)
        bullets.add(new_bullet)

def create_fleet(aliens, screen, ai_settings, ship):
    alien = Alien(screen, ai_settings)
    alien_number_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship_height=ship.rect.height, alien_height=alien.rect.height)

    for row_number in range(number_rows):
        print('row_number', str(row_number))
        for alien_number in range(alien_number_x):
            print(alien_number, end=' ')
            create_alien(alien_number=alien_number, ai_settings=ai_settings, aliens=aliens, screen=screen, row_number=row_number)



def get_number_aliens_x(ai_settings, alien_width):
    available_space_x = ai_settings.screen_width - alien_width * 2
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x

def create_alien(alien_number, ai_settings, screen, aliens, row_number):
    global number
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width

    alien.x = alien_width + 2 * alien_width * alien_number
    alien.y = alien.rect.height + 2 * alien.rect.height * row_number

    alien.rect.x = alien.x
    alien.rect.y = alien.y
    aliens.add(alien)

def get_number_rows(ai_settings, ship_height, alien_height):
    available_space_y = ai_settings.screen_height - 3 * alien_height - ship_height
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows
