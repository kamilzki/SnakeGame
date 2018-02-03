import pygame
import time
import random


pygame.init()

display_width = 800
display_height = 600
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Snake")
FPS = 30

background = (0, 30, 0)
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 150, 0)

block_size = 10
clock = pygame.time.Clock()

display_center = (display_width / 2, display_height / 2)
font_size = 25
font = pygame.font.SysFont(None, font_size)

def message_to_screen(msg, color):
    screen_text = font.render(msg, True, color)

    gameDisplay.blit(screen_text, [display_center[0]-((len(msg)*8)/2), display_center[1]])
    pygame.display.update()
    display_center


def gameLoop():
    gameExit = False
    gameOver = False

    lead_x = display_width / 2
    lead_y = display_height / 2
    lead_x_change = 0
    lead_y_change = 0

    randAppleX = 0
    randAppleY = 0
    def randomApple():
        global randAppleX
        global randAppleY
        randAppleX = round(random.randrange(0, display_width-block_size)/10.0)*10.0
        randAppleY = round(random.randrange(0, display_height-block_size)/10.0)*10.0
        print(randAppleX)
        print(randAppleY)


    while not gameExit:

        while gameOver == True:
            message_to_screen("GAME OVER! Press 'P' to play again! or 'Q' to quit", red)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameOver = False
                    gameExit = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        gameLoop()
                    elif event.key == pygame.K_q:
                        gameOver = False
                        gameExit = True


        for event in pygame.event.get():
            print(event)

            if event.type == pygame.QUIT:
                gameExit = True

            # control snake
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and lead_x_change != block_size:
                    lead_y_change = 0
                    lead_x_change = -block_size
                elif event.key == pygame.K_RIGHT and lead_x_change != -block_size:
                    lead_y_change = 0
                    lead_x_change = block_size
                elif event.key == pygame.K_UP and lead_y_change != block_size:
                    lead_x_change = 0
                    lead_y_change = -block_size
                elif event.key == pygame.K_DOWN and lead_y_change != -block_size:
                    lead_x_change = 0
                    lead_y_change = block_size

                    # if event.type == pygame.KEYUP:
                    #     if event.key == pygame.K_LEFT or event.key ==  pygame.K_RIGHT:
                    #         lead_x_change = 0
                    #     if event.key == pygame.K_UP or event.key ==  pygame.K_DOWN:
                    #         lead_y_change = 0

        lead_x += lead_x_change
        lead_y += lead_y_change

        # go on wall = game over
        if (lead_x < 0 or lead_x >= display_width) or (lead_y < 0 or lead_y >= display_height):
            gameOver = True
            # pygame.quit()
        else:
            randomApple()
            gameDisplay.fill(background)
            gameDisplay.fill(red, rect=[randAppleX, randAppleY, 10, 10])
            pygame.draw.rect(gameDisplay, green, [lead_x, lead_y, block_size, block_size])

        clock.tick(FPS)
        pygame.display.update()

    pygame.quit()
    quit()


def main():
    gameLoop()


if __name__ == "__main__":
    main()
