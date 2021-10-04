import pygame
from pygame.sprite import Sprite

class tileMapper(Sprite):
    def __init__(self, UnstablePlatform):
        super().__init__()
        self.isFlag = False
        self.screen = UnstablePlatform.screen
        self.settings = UnstablePlatform.settings
        self.screen_rect = UnstablePlatform.screen.get_rect()
    
        self.rect = pygame.Rect(0,400,self.settings.tileWidth,self.settings.tileHeight)

        self.tileX = float(self.rect.x)
        self.tileY = float(self.rect.y)

        
        #Basic Draw
        #pygame.draw.rect(self.screen, self.settings.tileColor, self.baseTile)

    def updateTile(self):
        self.rect.x = self.tileX

    def retFlag(self):
        return self.isFlag

    def flagTile(self):
        self.isFlag = True
        self.rect.x = 700
        self.rect.y = 300
        pygame.draw.rect(self.screen, self.settings.flagColor, self.rect)


        
    def renderGround(self):
        pygame.draw.rect(self.screen, self.settings.tileColor, self.rect)
