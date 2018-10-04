import pygame
import sys

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)


width = 800
height = 600

gameDisplay = pygame.display.set_mode((width, height))
pygame.display.set_caption("Sneks kek")

gameExit = False

pygame.time.Clock()

x_coord = 300
y_coord = 300


while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True
        if event.type == pygame.KEYDOWN:
            if event == pygame.K_a:
                x_coord -= 20
            if event == pygame.K_d:
                x_coord += 20

    gameDisplay.fill(white)
    pygame.draw.rect(gameDisplay, black, [x_coord, y_coord, 20, 20])
    pygame.display.update()


pygame.quit()
quit()
