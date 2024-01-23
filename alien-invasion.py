
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats
from button import Button



def run_game():
    #Инициализирует игру и создает объект экрана
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption('Alien Invasion')

    ship = Ship(screen, ai_settings)
    stats = GameStats(ai_settings)

    bullets = Group()
    aliens = Group()

    gf.create_fleet(aliens=aliens, screen=screen, ai_settings=ai_settings, ship=ship)
    play_button = Button(ai_settings, screen, "Play")
    #запуск основного цикла игры
    while True:
        gf.check_events(ai_settings=ai_settings, stats= stats, play_button=play_button, ship=ship, screen=screen, bullets=bullets, aliens=aliens)

        if stats.game_active:
            ship.update()
            gf.update_bullets(bullets=bullets, aliens=aliens, ai_settings=ai_settings, screen=screen, ship=ship)
            gf.update_aliens(ai_settings=ai_settings, aliens=aliens, ship=ship, stats=stats, screen=screen,
                             bullets=bullets)

        gf.update_screen(ai_settings=ai_settings, ship=ship, stats=stats, screen=screen, bullets=bullets, aliens=aliens,
                         play_button=play_button)
run_game()
