from config import *
import ClassGameSprite


# 子弹类
class Bullet(ClassGameSprite.GameSprite):
    def __init__(self, bullet_image_path):
        super().__init__(bullet_image_path, BULLET_SPEED)  # 子弹图片

    def update(self, *args):
        super().update()
        if self.rect.bottom <= SCREEN_RECT.top:
            self.kill()
