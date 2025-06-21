from random import randrange
from config import *
import ClassGameSprite


# 敌人类
class Enemy(ClassGameSprite.GameSprite):
    def __init__(self, enemy_image_path):
        super().__init__(enemy_image_path, ENEMY_SPEED + randrange(3, 6))  # 敌机图片
        self.rect.bottom = 0
        self.rect.x = randrange(0, SCREEN_RECT.right - self.rect.width + 1)

    def update(self, *args):
        super().update()
        if self.rect.y > SCREEN_RECT.bottom:
            self.kill()
