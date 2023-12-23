import pygame
import sys
from setting import Settings
def check_events(ship):
    # Обрабатывает нажатия клавиш и события мыши
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                ship.rect.centerx += 5
            if event.key == pygame.K_LEFT:
                ship.rect.centerx -= 5

def update_screen(ai_settings, screen, ship, warrior):
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    warrior.blitme()
    pygame.display.flip()
