import pygame
import random

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 128, 0)


window_width = 800
window_height = 600

block_size = 10
apple_size = 10

gameDisplay = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Sneks kek")

clock = pygame.time.Clock()
FPS = 15

font = pygame.font.SysFont(None, 25)

# snake function


def snake(block_size, snakeList):
    for XnY in snakeList:
        pygame.draw.rect(gameDisplay, white, [XnY[0], XnY[1], block_size, block_size])


# displays text on the screen


def screen_message(msg, color):
    text = font.render(msg, True, color)
    gameDisplay.blit(text, [window_width / 5, window_height / 3])

# main block of the game which has game loop


def main():
    gameExit = False
    gameOver = False

    x_coord = window_width / 2
    y_coord = window_height / 2

    x_change = 0
    y_change = 0


    snakeList = []
    snakeLength = 1

    randAppleX = round(random.randrange(0, window_width - block_size) / 10.0) * 10.0
    randAppleY = round(random.randrange(0, window_height - block_size) / 10.0) * 10.0

    while not gameExit:
        while gameOver is True:
            gameDisplay.fill(white)
            screen_message('Game Over, press F/Enter to play again or press esc to quit', green)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameOver = False
                    gameExit = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        gameExit = True
                        gameOver = False
                    if event.key == pygame.K_f or event.key == pygame.K_RETURN:
                        main()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    x_change = -block_size
                    y_change = 0
                if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    x_change = block_size
                    y_change = 0
                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    y_change = -block_size
                    x_change = 0
                if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    y_change = block_size
                    x_change = 0
        if x_coord >= window_width or x_coord <= 0 or y_coord >= window_height or y_coord <= 0:
            gameOver = True

        x_coord += x_change
        y_coord += y_change
        gameDisplay.fill(black)
        pygame.draw.rect(gameDisplay, red, [randAppleX, randAppleY, apple_size, apple_size])

        snakeHead = []
        snakeHead.append(x_coord)
        snakeHead.append(y_coord)
        snakeList.append(snakeHead)

        if len(snakeList) > snakeLength:
             del snakeList[0]

        for body in snakeList[:-1]:
            if body == snakeHead:
                gameOver = True

        snake(block_size, snakeList)
        pygame.display.update()

        if x_coord == randAppleX and y_coord == randAppleY:
            randAppleX = round(random.randrange(0, window_width - 20) / 10.0) * 10.0
            randAppleY = round(random.randrange(0, window_height - block_size) / 10.0) * 10.0
            snakeLength += 1
        clock.tick(FPS)


# executes the game


if __name__ == '__main__':
    main()
    pygame.quit()
    quit()
