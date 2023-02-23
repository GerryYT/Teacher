import pygame
import control
import gif

class Player(pygame.sprite.Sprite):
    def __init__(self, sc):
        pygame.sprite.Sprite.__init__(self)
        self.sc = sc
        self.image = pygame.image.load('player2.png')
        self.rect = self.image.get_rect()
        self.sc_rect = sc.get_rect()
        self.rect.centerx = self.sc_rect.centerx
        self.rect.bottom = self.sc_rect.bottom
        self.move_left = True
        self.move_right = False
        self.move_up = True
        self.move_down = False

    def output(self):
        self.sc.blit(self.image, self.rect)

    def update_player(self, wall_1):
        print(self.rect.bottom, wall_1.rect.bottom)
        if self.rect.centerx < control.x_new:
            control.WalkStop = False
            control.Walk_right = True
            self.rect.centerx += 1
            if control.Walk_right:
                self.image = gif.WalkRight[control.WalckanimCount // 15]
                control.WalckanimCount += 1
                if control.WalckanimCount + 1 >= 60:
                    control.WalckanimCount = 0
        if self.rect.left > 170 and self.rect.centerx > control.x_new and self.rect.left > wall_1.rect.right:
            control.WalkStop = False
            control.Walk_left = True
            self.rect.centerx -= 1
            if control.Walk_left:
                self.image = gif.WalkLeft[control.WalckanimCount // 15]
                control.WalckanimCount += 1
                if control.WalckanimCount + 1 >= 60:
                    control.WalckanimCount = 0
        if self.rect.bottom < self.sc_rect.bottom and self.rect.centery < control.y_new:
            control.WalkStop = False
            control.Walk_back = True
            self.rect.centery += 1
            if control.Walk_back:
                self.image = gif.WalkBack[control.WalckanimCount // 15]
                control.WalckanimCount += 1
                if control.WalckanimCount + 1 >= 60:
                    control.WalckanimCount = 0
        if self.rect.top > 120 and self.rect.centery > control.y_new:
            control.WalkStop = False
            control.Walk_forward = True
            self.rect.centery -= 1
            if control.Walk_forward:
                self.image = gif.WalkForward[control.WalckanimCount // 15]
                control.WalckanimCount += 1
                if control.WalckanimCount + 1 >= 60:
                    control.WalckanimCount = 0
        if self.rect.centery == control.y_new  and self.rect.centerx == control.x_new:
            self.image = pygame.image.load('player2.png')
            print('asd')
        if control.WalkStop:
            self.image = pygame.image.load('player2.png')