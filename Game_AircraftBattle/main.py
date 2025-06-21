import pygame
import game
import config

# 游戏主循环
while True:
    # 刷新帧率
    game.clock.tick(60)

    # 事件处理
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # 退出事件
            pygame.quit()  # pygame退出
            exit()  # 程序退出
        elif event.type == config.CREATE_ENEMY_EVENT:  # 生成敌机事件
            game.enemy_group.add(game.Enemy(config.IMAGE_ENEMY2))

        if event.type == pygame.KEYDOWN:  # 键盘按下事件
            if event.key == pygame.K_SPACE:
                game.hero.fire()
            if event.key == pygame.K_RIGHT:
                game.right_move = True
            if event.key == pygame.K_LEFT:
                game.left_move = True
        elif event.type == pygame.KEYUP and (event.key in (pygame.K_RIGHT, pygame.K_LEFT)):  # 键盘抬起事件
            if event.key == pygame.K_LEFT:
                game.left_move = False
            if event.key == pygame.K_RIGHT:
                game.right_move = False

    # 移动方向检测
    if game.left_move:
        game.hero.speed = -3
    if game.right_move:
        game.hero.speed = 3
    if game.left_move and game.right_move or (not game.left_move and not game.right_move):
        game.hero.speed = 0

    # 碰撞检测
    isCount = pygame.sprite.groupcollide(game.hero.bullet_group, game.enemy_group, True, True)
    if isCount:
        game.number += 1
        text_surface = game.score.render(f"当前得分: {str(game.number)}", True, (0, 0, 0))

    isEnd = pygame.sprite.groupcollide(game.hero_group, game.enemy_group, True, True)
    if isEnd:
        game.hero.kill()
        pygame.quit()
        exit()

    # 背景更新
    game.background_group.update()
    game.background_group.draw(game.screen)

    # 角色更新
    game.hero.update()
    game.hero_group.draw(game.screen)
    # 武器更新
    game.hero.bullet_group.update()
    game.hero.bullet_group.draw(game.screen)

    # 敌人更新
    game.enemy_group.update()
    game.enemy_group.draw(game.screen)

    # 分数更新
    game.screen.blit(game.text_surface, game.text_rect)

    # 重新绘制
    pygame.display.update()
    pygame.display.flip()
