class Settings():
    # Класс для хранения всех настроек игры
    def __init__(self):
        # Инициализация настроек игры
        # Параметры игры

        # Настройки экрана
        self.screen_width = 1366
        self.screen_height = 700
        self.bg_color = (200, 200, 255)

        # Настройки корабля
        self.ship_limit = 3
        self.ship_speed_factor = 3

        # Настройки пуль
        self.bullets_allowed = 30
        self.bullet_width = 5
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)


        # Настройки пришельцев
        self.fleet_drop_speed = 10


        # Темп ускорения игры
        self.speedup_scale = 1.1
        # Темп роста стоимости пришельцев
        self.score_scale = 1.5
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1
        self.ship_speed_factor = 3
        self.alien_points = 50
        self.fleet_direction = 1

    def increase_speed(self):
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.ship_speed_factor *= self.speedup_scale
        self.alien_points = int(self.score_scale * self.alien_points)

