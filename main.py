import pygame
import control
import button
from player import Player
import gif
from rect import Wall

sc = pygame.display.set_mode((1920, 1080))
clock=pygame.time.Clock()
bg = pygame.image.load('class.jpg')

aptechka = pygame.image.load('Aptechka.png')
book = pygame.image.load('book.png')
pen = pygame.image.load('pen.png')

pen_button = button.Button(990, 410, pen)
aptechka_button = button.Button(1520, 220, aptechka)
BackanimCount = 0
player = Player(sc)

wall_1 = Wall(0, 0, 0, 160, 150, 500, 260, sc)

pygame.mixer.init()

while control.game:
    control.events(player)
    sc.blit(bg, (0, 0))
    sc.blit(book, (920, 400))
    if pen_button.draw(sc) or control.Loading:
        control.Loading = True
        if control.Loading:
            if BackanimCount == 1:
                pygame.mixer.Sound('sounds/pen.mp3').play()
            if BackanimCount + 1 >= 155:
                BackanimCount = 0
                control.Loading = False
            sc.blit(gif.LoadingGif[BackanimCount // 5], (945, 335))
            BackanimCount += 1
    if aptechka_button.draw(sc) or control.Loading2:
        control.Loading2 = True
        if control.Loading2:
            if BackanimCount == 1:
                pygame.mixer.Sound('sounds/laz.mp3').play()
            if BackanimCount + 1 >= 155:
                BackanimCount = 0
                control.Loading2 = False
            sc.blit(gif.LoadingGif[BackanimCount // 5], (1500, 145))
            BackanimCount += 1
    player.output()
    player.update_player(wall_1)
    pygame.display.update()
    clock.tick(120)
pygame.quit()