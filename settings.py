class Settings():

    def __init__(self):
        self.screen_widh = 1200
        self.screen_height = 800
        self.bg_color = (255, 255, 255)
        self.ship_speed_factor = 1.5
        # Параметры пули.
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3