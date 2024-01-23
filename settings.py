class Settings():
    # Класс для хранения всех настроек игры
    def __init__(self):
        # Инициализация настроек игры
        # Параметры игры
        self.screen_width = 1366
        self.screen_height = 700
        # Назначение цвета фона.
        self.bg_color = (200, 200, 255)

        # Настройки скорости
        self.ship_speed_factor = 3
        self.alien_speed_factor = 1
        self.bullet_speed_factor = 3
        self.fleet_drop_speed = 10
        self.fleet_direction = 1


        self.bullets_allowed = 30
        self.bullet_width = 5
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.ship_limit = 3
