import pygame
import sys
from settings import Settings
from bullet import Bullet
from alien import Alien
from time import sleep

number = 0
def check_events(ai_settings, screen, stats, play_button, ship, bullets, aliens):
    # Обрабатывает нажатия клавиш и события мыши
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        # Движение
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event=event, ship=ship, ai_settings=ai_settings, screen=screen, bullets=bullets)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats, play_button, ship, aliens,
 bullets, mouse_x, mouse_y)
def check_play_button(ai_settings, screen, stats, play_button, ship, aliens,
 bullets, mouse_x, mouse_y):
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        stats.reset_stats()
        stats.game_active = True
        pygame.mouse.set_visible(False)


        aliens.empty()
        bullets.empty()

        create_fleet(aliens, screen, ai_settings, ship)
        ship.center_ship()


def update_screen(ai_settings, screen, stats, ship, bullets, aliens, play_button):

    screen.fill(ai_settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()
    aliens.draw(screen)
    if not stats.game_active:
        play_button.draw_button()
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
def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

    if event.key == pygame.K_UP:
        ship.moving_up = False
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False
def update_bullets(ai_settings, screen, ship, aliens, bullets):
    bullets.update()

    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    check_bullet_alien_collisions(bullets=bullets, aliens=aliens, ai_settings=ai_settings, screen=screen, ship=ship)
def check_bullet_alien_collisions(bullets, aliens, ai_settings, screen, ship):
    collisions = pygame.sprite.groupcollide(bullets, aliens, False, True)
    if len(aliens) == 0:
        bullets.empty()
        create_fleet(ai_settings=ai_settings, aliens=aliens, screen=screen, ship=ship)
def fire_bullet(bullets, ai_settings, ship, screen):
    if (len(bullets) < ai_settings.bullets_allowed):
        new_bullet = Bullet(ai_settings=ai_settings, ship=ship, screen=screen)
        bullets.add(new_bullet)
def create_fleet(aliens, screen, ai_settings, ship):
    alien = Alien(screen=screen, ai_settings=ai_settings)
    alien_number_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings=ai_settings, ship_height=ship.rect.height, alien_height=alien.rect.height)

    for row_number in range(number_rows):
        for alien_number in range(alien_number_x):
            create_alien(alien_number=alien_number, ai_settings=ai_settings, aliens=aliens, screen=screen, row_number=row_number)
def get_number_aliens_x(ai_settings, alien_width):
    available_space_x = ai_settings.screen_width - alien_width * 2
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x
def create_alien(alien_number, ai_settings, screen, aliens, row_number):
    global number
    alien = Alien(screen, ai_settings)
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

def check_fleet_edges(ai_settings, aliens):
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings=ai_settings, aliens=aliens)
            break

def change_fleet_direction(ai_settings, aliens):
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1

def update_aliens(ai_settings, aliens, ship, stats, screen, bullets):
    check_fleet_edges(ai_settings=ai_settings, aliens=aliens)
    aliens.update()
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings=ai_settings, stats=stats, screen=screen, ship=ship, aliens=aliens, bullets=bullets)

    check_aliens_bottom(ai_settings, stats, screen, ship, aliens,
 bullets)
def check_aliens_bottom(ai_settings, stats, screen, ship, aliens,
 bullets):
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(ai_settings, stats, screen, ship, aliens, bullets)
            break
def ship_hit(ai_settings, stats, screen, ship, aliens, bullets):
    if stats.ships_left > 0:
        stats.ships_left -= 1
        aliens.empty()
        bullets.empty()
        create_fleet(aliens, screen, ai_settings, ship)
        ship.center_ship()
        sleep(0.5)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)

