from config import *


# 精灵类
class GameSprite(pygame.sprite.Sprite):
    def __init__(self, image_path, move_speed=0):
        super().__init__()  # 调用父类构造
        self.image = pygame.image.load(image_path)  # 加载图片
        self.rect = self.image.get_rect()  # 设置尺寸
        self.speed = move_speed  # 记录速度

    def update(self, *args):
        self.rect.y += self.speed  # 沿y轴移动
