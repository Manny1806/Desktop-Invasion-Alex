class Settings():
    def __init__(self):
        
        self.ship_speed_factor = 3.5
        self.ship_limit = 3

        #bullet-settings
        self.bullet_speed_factor = 4 
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 6
        self.screen_width = 1200
        self.screen_height = 700

        #shortcut settings
        self.shortcut_speed_factor = 1
        self.fleet_drop_speed = 10
        self.fleet_direction = 1
