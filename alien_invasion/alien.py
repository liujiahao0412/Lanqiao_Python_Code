import pygame,random
from pygame.sprite import Sprite
class Alien(Sprite):
    def __init__(self,ai_game):
        super().__init__()
        self.settings = ai_game.settings
        self.screen = ai_game.screen
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        #速度
        self.speed_x = random.uniform(1.5,3.0)
        self.speed_y = random.uniform(0.1,2.0)
        self.direction = random.choice([-1,1])
    def update(self):
        self.x += self.speed_x*self.direction
        self.y += self.speed_y
        if self.x <= 0:
            self.x = 0
            self.direction *= -1
        if self.x >= self.settings.screen_width-self.rect.width:
            self.x = self.settings.screen_width - self.rect.width
            self.direction *= -1
        if self.y >= self.settings.screen_height:
            self.kill()
        self.rect.x = self.x
        self.rect.y = self.y
