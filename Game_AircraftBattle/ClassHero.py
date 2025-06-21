from ClassBullet import *
from config import *
from ClassGameSprite import *


# 英雄类
class Hero(ClassGameSprite.GameSprite):
    def __init__(self, hero_image_path):
        super().__init__(hero_image_path)  # 英雄图片
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.bottom = SCREEN_RECT.bottom - 100
        self.bullet_group = pygame.sprite.Group()

    def update(self, *args):
        self.rect.x += self.speed  # 重写:角色沿着x轴移动
        if self.rect.left <= SCREEN_RECT.left:
            self.rect.left = SCREEN_RECT.left
        if self.rect.right >= SCREEN_RECT.right:
            self.rect.right = SCREEN_RECT.right

    def fire(self):
        for i in range(1):
            hero_bullet = Bullet(IMAGE_BULLET2)  # 装载子弹2
            hero_bullet.rect.centerx = self.rect.centerx
            hero_bullet.rect.bottom = self.rect.y - i * 20
            self.bullet_group.add(hero_bullet)
