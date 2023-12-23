
resolution = {
    'horizontal': 1366,
    'vertical': 768
}

scale = 0.7

x = resolution['horizontal']
y = resolution['vertical']

class Settings():

    # Класс для хранения всех настроек игры
    def __init__(self):
        # Инициализация настроек игры
        # Параметры игры
        self.screen_width = 1366/2
        self.screen_height = 768/2
        # Назначение цвета фона.
        self.bg_color = (200, 200, 255)

