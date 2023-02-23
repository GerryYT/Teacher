import pygame
import button
import gif

game = True
Loading = False
Loading2 = False
x_new = 1316
y_new = 951
WalkStop = True
Walk_right = False
Walk_left = False
Walk_forward = False
Walk_back = False
WalckanimCount = 0


def events(player):
    global game
    global Walk_forward
    global Walk_back
    global Walk_left
    global Walk_right
    global y_new
    global x_new
    global xy_new
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x_new, y_new = pygame.mouse.get_pos()
            print(x_new, y_new)
            print(player.rect.centerx, player.rect.centery)
        '''elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                Walk_right = True
                player.move_right = True
            if event.key == pygame.K_a:
                Walk_left = True
                player.move_left = True
            if event.key == pygame.K_s:
                Walk_back = True
                player.move_up = True
            if event.key == pygame.K_w:
                Walk_forward = True
                player.move_down = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                Walk_right = False
                player.move_right = False
            if event.key == pygame.K_a:
                Walk_left = False
                player.move_left = False
            if event.key == pygame.K_s:
                Walk_back = False
                player.move_up = False
            if event.key == pygame.K_w:
                Walk_forward = False
                player.move_down = False'''
