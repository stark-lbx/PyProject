import pygame
from config import *
from ClassGameSprite import *
from ClassBackGround import *
from ClassBullet import *
from ClassHero import *
from ClassEnemy import *

# 初始化pygame库-确保pygame的各个模块能够正常工作
pygame.init()

# 创建游戏主窗口以及游戏时钟
screen = pygame.display.set_mode(SCREEN_RECT.size)
clock = pygame.time.Clock()

# 定时器事件
pygame.time.set_timer(CREATE_ENEMY_EVENT, CREATE_ENEMY_EVENT_TIME)

# 加载游戏背景
background_group = pygame.sprite.Group()
background = BackGround(BACKGROUND3)
background_group.add(background)

background2 = BackGround(BACKGROUND3)
background2.rect.bottom = 0
background_group.add(background2)

# 创建英雄
hero = Hero(IMAGE_HERO2)
hero_group = pygame.sprite.Group(hero)

# 创建敌机
enemy_group = pygame.sprite.Group()

# 本局分数
number = 0
score = pygame.font.SysFont(None, 72)
text_surface = score.render(f"当前得分: {str(number)}", True, (0, 0, 0))
text_rect = text_surface.get_rect()
text_rect.centerx = screen.get_rect().centerx
text_rect.bottom = screen.get_rect().bottom

# 移动方向
left_move = False
right_move = False