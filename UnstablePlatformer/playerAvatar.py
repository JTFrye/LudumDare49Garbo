import pygame
from pygame.sprite import Sprite

class playerCharacter(Sprite):
    def __init__(self, UnstablePlatform):
        super().__init__()

        self.screen = UnstablePlatform.screen
        self.settings = UnstablePlatform.settings
        self.screen_rect = UnstablePlatform.screen.get_rect()

        #Movement Flags
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        self.gravity = True

        self.pcbg_color = (255,255,255)
        self.yVel = 0

        self.rect = pygame.Rect(0,0, self.settings.playCharH,self.settings.playCharW)
        self.rectY = float(self.rect.y)
        self.rectX = float(self.rect.x)


    def update(self):
        if self.moving_right:
            self.rectX += self.settings.playChar_speed
            self.rect.x = self.rectX
        if self.moving_left:
            self.rectX -= self.settings.playChar_speed
            self.rect.x = self.rectX
        if self.moving_up:
            self.rectY -= self.settings.playChar_speed
            self.rect.y = self.rectY
        if self.moving_down:
            self.rectY += self.settings.playChar_speed
            self.rect.y = self.rectY

        if self.gravity:
            self.yVel = self.yVel + self.settings.playChar_accel
            self.rect.y += self.yVel

 
    def blitme(self):
        pygame.draw.rect(self.screen, self.pcbg_color, self.rect)

 
