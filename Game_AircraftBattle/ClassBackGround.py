from config import *
import ClassGameSprite


# 背景类
class BackGround(ClassGameSprite.GameSprite):
    def __init__(self, background_path):
        super().__init__(background_path)  # 背景图片
        self.old_rect = pygame.Rect(self.rect)
        self.speed = BACKGROUND_SPEED

    def update(self, *args):
        self.rect.top += self.speed  # 图片下移
        if self.rect.top >= self.old_rect.bottom:
            self.rect.bottom = pygame.Rect(self.old_rect).top  # 如果完全越界，重置
