

class setDefaults:
    def __init__(self):

        self.game_active = False

        #Screen Defaults
        self.screen_width = 1024
        self.screen_height = 600
        self.bg_color = (0,0,0)

        #Player Height, Width
        self.playCharH = 30
        self.playCharW = 30

        #Player HSpeed and Gravity
        self.playChar_speed = .5
        self.playChar_accel = .002

        #Tile System
        self.tileColor = (255,0,0)
        self.tileWidth = 128
        self.tileHeight = 64
        self.flagColor = (0,127,127)
