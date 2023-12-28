

class Settings():

    # Класс для хранения всех настроек игры
    def __init__(self):
        # Инициализация настроек игры
        # Параметры игры
        self.screen_width = 1366/2
        self.screen_height = 768/2
        # Назначение цвета фона.
        self.bg_color = (200, 200, 255)
        self.ship_speed_factor = 0.1

        # Настройки пули
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)

