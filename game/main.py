import pygame
import time

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 128, 0)


window_width = 800
window_height = 600

gameDisplay = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Sneks kek")

clock = pygame.time.Clock()
FPS = 30

font = pygame.font.SysFont(None, 25)


def screen_message(msg, color):
    text = font.render(msg, True, color)
    gameDisplay.blit(text, [window_width / 2, window_height / 2])


def main():
    gameExit = False
    gameOver = False


    x_coord = window_width / 2
    y_coord = window_height / 2

    x_change = 0
    y_change = 0
    block_size = 10

    while not gameExit:
        while gameOver is True:
            gameDisplay.fill(white)
            screen_message('Game Over, press Enter to play again or press esc to quit', red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        gameExit = True
                        gameOver = False
                    if event.key == pygame.K_KP_ENTER:
                        



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
            gameExit = True

        x_coord += x_change
        y_coord += y_change
        gameDisplay.fill(black)
        pygame.draw.rect(gameDisplay, white, [x_coord, y_coord, 20, block_size])
        pygame.display.update()
        clock.tick(FPS)



if __name__ == '__main__':
    main()
    screen_message('Game Over', green)
    pygame.display.update()
    time.sleep(2)
    pygame.quit()
    quit()
