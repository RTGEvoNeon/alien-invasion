
import pygame
from setting import Settings
from ship import Ship
from warrior import Warrior
import game_functions as gf



def run_game():
    #Инициализирует игру и создает объект экрана
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption('Alien Invasion')

    ship = Ship(screen)
    warrior = Warrior(screen)

    #запуск основного цикла игры
    while True:
        gf.update_screen(ai_settings, screen, ship, warrior)
        gf.check_events(ship)


run_game()
