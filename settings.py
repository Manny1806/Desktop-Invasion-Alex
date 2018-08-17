class Settings():
    def __init__(self):
        
        self.ship_speed_factor = 3.5
        self.ship_limit = 1

        #bullet-settings
        self.bullet_speed_factor = 4 
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 6
        self.screen_width = 1200
        self.screen_height = 700

        #shortcut settings
        # self.shortcut_speed_factor = 1
        self.fleet_drop_speed = 10
        

        #clippy setting
        self.clippy_speed_factor = 2.5
        self.clippy_direction = 1
        self.clippy_moving = False

        self.speedup_scale = 1.2

        self.bg_color = (230, 230, 230)

        self.initialize_dynamic_settings()
    
    def initialize_dynamic_settings(self):
        self.shortcut_speed_factor = 1
        self.fleet_direction = 1

        self.shortcut_points = 50
        self.clippy_points = 200

    
    def increase_speed(self):
        self.shortcut_speed_factor *= self.speedup_scale