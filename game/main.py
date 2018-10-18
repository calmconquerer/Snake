import pygame
import time
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
FPS = 30

font = pygame.font.SysFont(None, 25)

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

    randAppleX = random.randrange(0, window_width - 20)
    randAppleY = random.randrange(0, window_height - block_size)

    while not gameExit:
        while gameOver is True:
            gameDisplay.fill(white)
            screen_message('Game Over, press F to play again or press esc to quit', red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        gameExit = True
                        gameOver = False
                    if event.key == pygame.K_f:
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
        pygame.draw.rect(gameDisplay, white, [x_coord, y_coord, 20, block_size])
        pygame.display.update()
        clock.tick(FPS)


# executes the game


if __name__ == '__main__':
    main()
    pygame.quit()
    quit()
