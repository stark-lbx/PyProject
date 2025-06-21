# 本文件包含了游戏所需的所有图片资源 及 初始化变量
import pygame

BACKGROUND1 = "images/background.png"  # 背景图片-经典背景
BACKGROUND2 = "images/bg2.jpg"  # 背景图片-河流山脉
BACKGROUND3 = "images/bg3.jpg"  # 背景图片-天空之城
BACKGROUND_SPEED = 1  # 背景速度

IMAGE_HERO1 = "images/hero.png"  # 英雄图片-经典飞机
IMAGE_HERO2 = "images/hero2.png"  # 英雄图片-科幻飞机

IMAGE_BULLET = "images/bullet.png"  # 武器图片-经典子弹
IMAGE_BULLET2 = "images/bullet2.png"  # 武器图片-激光弹
BULLET_SPEED = -4  # 子弹速度

IMAGE_ENEMY = "images/enemy.png"  # 敌人图片-经典敌机
IMAGE_ENEMY2 = "images/enemy2.png"  # 敌人图片-科幻敌机
ENEMY_SPEED = 0  # 敌机速度

CREATE_ENEMY_EVENT = pygame.USEREVENT + 1
CREATE_ENEMY_EVENT_TIME = 700

SCREEN_RECT = pygame.Rect(0, 0, 512, 768)  # 屏幕尺寸
