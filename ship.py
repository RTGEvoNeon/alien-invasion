import pygame
import settings
class Ship():
    def __init__(self, screen, ai_settings):
        # Инициализирует корабль и задает его начальную позицию
        self.screen = screen
        self.ai_settings = ai_settings

        # Загрузка изображения корабля и получение прямоугольника.
        self.image = pygame.image.load('static/images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Каждый новый корабль появляется у нижнего края экрана.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.center_x = float(self.rect.centerx)
        self.center_y = float(self.rect.centery)

        self.moving_right = False
        self.moving_up = False
        self.moving_down = False
        self.moving_left = False

    def blitme(self):
        """Рисует корабль в текущей позиции."""
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center_x += self.ai_settings.ship_speed_factor

        if self.moving_left and self.rect.left > 0:
            self.center_x -= self.ai_settings.ship_speed_factor

        if self.moving_up and self.rect.top > 0:
            self.center_y -= self.ai_settings.ship_speed_factor

        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.center_y += self.ai_settings.ship_speed_factor

        self.rect.centerx = self.center_x
        self.rect.centery = self.center_y