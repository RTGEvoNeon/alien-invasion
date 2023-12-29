
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
import game_functions as gf
from pygame.sprite import Group
from alien import Alien



def run_game():
    #Инициализирует игру и создает объект экрана
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption('Alien Invasion')

    ship = Ship(screen, ai_settings)

    bullets = Group()
    aliens = Group()
    gf.create_fleet(aliens=aliens, ai_settings=ai_settings, screen=screen, ship=ship)
    #запуск основного цикла игры
    while True:

        gf.check_events(ai_settings=ai_settings, ship=ship, screen=screen, bullets=bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings=ai_settings, ship=ship, screen=screen, bullets=bullets, aliens=aliens)

run_game()
