class Settings:
    def __init__(self):
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (100, 200, 100)

        self.ship_speed = 1.5

        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullet_allowed = 300000

        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        self.fleet_direction = 1
