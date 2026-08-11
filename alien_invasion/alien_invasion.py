import sys,pygame,random
from ship import Ship
from settings import Settings
from bullet import Bullet
from alien import Alien

class AlienInvasion:

    def __init__(self):
        pygame.init()
        self.settings=Settings()            #设置类
        self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        pygame.display.set_caption('Alien Invasion')
        self.clock = pygame.time.Clock()
        self.bg_color = self.settings.bg_color
        self.ship = Ship(self)              #飞船类
        self.bullets = pygame.sprite.Group()        #子弹类
        self.aliens = pygame.sprite.Group()         #外星人
        self.create_fleet()

#主程序
    def run_game(self):
        while True:
            self.check_events()
            self.ship.update()
            self.update_bullets()
            self.update_aliens()
            self.upgrade_screen()
            self.clock.tick(50)
#获取按键操作
    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self.check_keydown_events(event)

            elif event.type == pygame.KEYUP:
                self.check_keyup_events(event)


    def check_keydown_events(self,event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        elif event.key == pygame.K_ESCAPE:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self.fire_bullet()

    def check_keyup_events(self,event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        elif event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False

    def update_aliens(self):
        self.aliens.update()
        #重生
        max_alien = 10
        while len(self.aliens) < max_alien:
            while True:
                new_alien = Alien(self)
                new_alien.rect.x = random.randint(0,self.settings.screen_width-new_alien.rect.width)
                new_alien.rect.y = -new_alien.rect.height
                new_alien.x = float(new_alien.rect.x)
                new_alien.y = float(new_alien.rect.y)
                if not pygame.sprite.spritecollideany(new_alien,self.aliens):
                    break
            self.aliens.add(new_alien)

#创建军队
    def create_fleet(self):
        alien = Alien(self)
        alien_num = 10
        while len(self.aliens) < alien_num:
            new_alien = Alien(self)
            new_alien.rect.x = random.randint(new_alien.rect.width//3,self.settings.screen_width-new_alien.rect.width)
            new_alien.rect.y = random.randint(0,self.settings.screen_height//4)
            new_alien.x = float(new_alien.rect.x)
            new_alien.y = float(new_alien.rect.y)
            collision_test = pygame.sprite.spritecollideany(new_alien,self.aliens)
            if not collision_test:
                self.aliens.add(new_alien)

#这个只能做到间隔x随机
    def create_alien(self,x_position,y_position):
        new_alien = Alien(self)
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position
        self.aliens.add(new_alien)

    # 更新子弹
    def update_bullets(self):
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        self.check_bullet_alien_collisions()

    def check_bullet_alien_collisions(self):
        collisions = pygame.sprite.groupcollide(self.bullets,self.aliens,True,True)


#点射子弹
    def fire_bullet(self):
        if len(self.bullets) < self.settings.bullet_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

#更新屏幕
    def upgrade_screen(self):
        self.screen.fill(self.bg_color)
        self.ship.blitme()
        self.aliens.draw(self.screen)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        pygame.display.flip()
if __name__ == '__main__':
    ai=AlienInvasion()
    ai.run_game()