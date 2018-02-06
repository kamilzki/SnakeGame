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
head_color = (0, 100, 0)
body_color = (0, 175, 0)

block_size = 20
apple_size = 10
clock = pygame.time.Clock()

display_center = (display_width / 2, display_height / 2)
font_size = 25
font = pygame.font.SysFont(None, font_size)


def message_to_screen_on_center(msg, color):
    screen_text = font.render(msg, True, color)

    gameDisplay.blit(screen_text, [display_center[0] - ((len(msg) * 8) / 2), display_center[1]])
    pygame.display.update()

def message_to_screen(msg, color, x=display_width-50, y=50):
    screen_text = font.render(msg, True, color)
    gameDisplay.blit(screen_text, [x, y])
    pygame.display.update()



def gameLoop():
    gameExit = False
    gameOver = False

    from game.Snake import Snake

    snake = Snake(display_width/2, display_height/2)

    # snakes = [snake]
    # lead_x = display_width / 2
    # lead_y = display_height / 2
    lead_x_change = 0
    lead_y_change = 0
    change_pos = False
    score = 0

    def randomApple():
        randAppleX = round(random.randrange(0, display_width - apple_size)) # / block_size) * block_size
        randAppleY = round(random.randrange(0, display_height - apple_size)) # / block_size) * block_size
        return randAppleX, randAppleY

    randAppleX, randAppleY = randomApple()

    while not gameExit:
        message_to_screen(str(snake.score), (0,0,170))
        change_pos = False
        while gameOver == True:
            message_to_screen_on_center("GAME OVER! Press 'P' to play again! or 'Q' to quit", red)

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
            # print(event)

            if event.type == pygame.QUIT:
                gameExit = True
                gameOver = False

            # control snake
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and lead_x_change != block_size and not change_pos:
                    lead_y_change = 0
                    lead_x_change = -block_size
                    change_pos = True
                elif event.key == pygame.K_RIGHT and lead_x_change != -block_size and not change_pos:
                    lead_y_change = 0
                    lead_x_change = block_size
                    change_pos = True
                elif event.key == pygame.K_UP and lead_y_change != block_size and not change_pos:
                    lead_x_change = 0
                    lead_y_change = -block_size
                    change_pos = True
                elif event.key == pygame.K_DOWN and lead_y_change != -block_size and not change_pos:
                    lead_x_change = 0
                    lead_y_change = block_size
                    change_pos = True

                    # if event.type == pygame.KEYUP:
                    #     if event.key == pygame.K_LEFT or event.key ==  pygame.K_RIGHT:
                    #         lead_x_change = 0
                    #     if event.key == pygame.K_UP or event.key ==  pygame.K_DOWN:
                    #         lead_y_change = 0

        snake.addToPosition(lead_x_change, lead_y_change)

        # go on wall = game over
        if (snake.head_x < 0 or snake.head_x >= display_width) or (snake.head_y < 0 or snake.head_y >= display_height) \
                or snake.collisionWithBody():
            gameOver = True
            # pygame.quit()
        else:
            # eating apple
            if ((snake.head_x + block_size >= randAppleX and snake.head_x <= randAppleX + apple_size)
                and (snake.head_y + block_size >= randAppleY and snake.head_y <= randAppleY + apple_size)):
                    snake.scoreMore(snake.head_x, snake.head_y)
                    randAppleX, randAppleY = randomApple()

            gameDisplay.fill(background)
            #draw apple
            gameDisplay.fill(red, rect=[randAppleX, randAppleY, apple_size, apple_size])

            # draw snake's head
            pygame.draw.rect(gameDisplay, head_color, [snake.head_x, snake.head_y, block_size, block_size])
            # draw snake's body
            for body_block in snake.body:
                pygame.draw.rect(gameDisplay, body_color, [body_block[0], body_block[1], block_size, block_size])


        clock.tick(FPS)
        pygame.display.update()

    pygame.quit()
    quit()


def main():
    gameLoop()


if __name__ == "__main__":
    main()
