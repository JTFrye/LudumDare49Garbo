from setView import setDefaults
from playerAvatar import playerCharacter
from levelMaker import tileMapper
from pygame.sprite import Sprite
from genButton import Button
import pygame
import sys


class UnstablePlatformEngine:
    def __init__(self):
        pygame.init()
        self.settings = setDefaults()

        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.Group()        
        
        #WINDOW MODE
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        #FULLSCREEN MODE
        #self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)        
        #self.settings.screen_width = self.screen.get_rect().width
        #self.settings.screen_height = self.screen.get_rect().height


        pygame.display.set_caption('Unstable Platformer')
        self.playChar = playerCharacter(self)
        self.player.add(self.playChar)
        self.tileMap = tileMapper(self)
        self._create_floor()
        
        self.play_button = Button(self, 'Play')



    def _check_events(self):
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    self._check_keydown_events(event)
                elif event.type == pygame.KEYUP:
                    self._check_keyup_events(event)
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    self._check_play_button(mouse_pos)

    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.playChar.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.playChar.moving_left = True
        elif event.key == pygame.K_UP:
            self.playChar.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.playChar.moving_down = True
        elif event.key == pygame.K_q:
            pygame.quit()
            sys.exit()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.playChar.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.playChar.moving_left = False
        elif event.key == pygame.K_UP:
            self.playChar.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.playChar.moving_down = False

    def _check_play_button(self, mouse_pos):
        if self.play_button.rect.collidepoint(mouse_pos):
            self.settings.game_active = True
            print('play hit')


    def _create_floor(self):
       
        total_length = self.settings.screen_width // self.settings.tileWidth
        for xed in range(total_length + 1):
            tile = tileMapper(self)
            tile.rect.x = xed * self.settings.tileWidth
            #tile.renderGround()
            self.tiles.add(tile)
        self.flagT = tileMapper(self)
        self.flagT.flagTile()
        self.tiles.add(self.flagT)

    def _render_floor(self):
        for yed in self.tiles.sprites():
            if yed.isFlag == True:
                yed.flagTile()
            else:
                yed.renderGround()

    def _set_inactive(self):
        self.settings.game_active = False

    def _collision(self):
        collisions = pygame.sprite.groupcollide(self.tiles, self.player, False, False)

        if collisions:
            self.playChar.gravity = False
            for xed in collisions:
                if xed.isFlag == True:
                    print('flag found')
                    self.playChar.rect.x = 0
                    self.playChar.rectX = 0
                    self.playChar.rect.y = 0
                    self.playChar.rectY = 0
                    self._set_inactive()
                else :
                    pass
        else:
            self.playChar.gravity = True

        #Alternate Option
        #if pygame.sprite.spritecollideany(self.playChar, self.tiles):
            #self.playChar.gravity = False
        #else:
            #self.playChar.gravity = True

        

    def _update_screen(self):
        
        self.screen.fill(self.settings.bg_color)



        self.playChar.blitme()

        #self._create_floor()
        self._render_floor()
#        self.play_button.draw_button()
        if not self.settings.game_active:
            self.play_button.draw_button()

        pygame.display.flip()
        

    def run_game(self):

        while True:
            self._check_events()


            if self.settings.game_active:
                self._collision()
                self.playChar.update()


            self._update_screen()



if __name__ == '__main__':
    print('mnr')
    UnstablePlatform = UnstablePlatformEngine()
    UnstablePlatform.run_game()
