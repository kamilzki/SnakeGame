import pygame
import time
import random
from game.Snake import Snake
from game.Apple import Apple

pygame.init()

display_width = 800
display_height = 600
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Snake")
FPS = 20

background = (0, 30, 0)
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
head_color = (0, 100, 0)
body_color = (0, 175, 0)

block_size = 20
apple_size = 25

# snakeHead_img = pygame.image.load('/home/kamil/PycharmProjects/SnakeGame/images/snake_head.png')


clock = pygame.time.Clock()

display_center = (display_width / 2, display_height / 2)
font_size = 25
font = pygame.font.SysFont("arial", font_size)


def text_objects(text, color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()

def message_to_screen_on_center(msg, color):
    textSurf, textRect = text_objects(msg, color)
    textRect.center = display_width/2 ,  display_height/2
    gameDisplay.blit(textSurf, textRect)
    pygame.display.update()

def message_to_screen(msg, color, posX, posY):
    # screen_text = font.render(msg, True, color)
    # gameDisplay.blit(screen_text, [x, y])
    # pygame.display.update()
    textSurf, textRect = text_objects(msg, color)
    textRect.center = posX, posY
    gameDisplay.blit(textSurf, textRect)
    pygame.display.update()

def random_pos():
    randAppleX = round(random.randrange(0, display_width - apple_size)) # / block_size) * block_size
    randAppleY = round(random.randrange(0, display_height - apple_size)) # / block_size) * block_size

    return randAppleX, randAppleY

def collisionWithWall(snake):
    if (snake.head_x < 0 or snake.head_x >= display_width) or (snake.head_y < 0 or snake.head_y >= display_height):
        return True
    else:
        return False

def gameLoop():
    gameExit = False
    gameOver = False

    direction = "up"
    snake = Snake(display_width/2, display_height/2, gameDisplay, block_size, direction)

    rand_apple_x, rand_apple_y = random_pos()
    # rand_apple_x, rand_apple_y = 400, 200
    apple1 = Apple(2, rand_apple_x, rand_apple_y, gameDisplay)
    apples = [apple1]

    # snakes = [snake]
    lead_x_change = 0
    lead_y_change = -block_size
    change_pos = False
    # rand_apple_x, rand_apple_y = randomApple()

    while not gameExit:
        message_to_screen(str(snake.score), (0,0,170), display_width-50, 50)
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
                    direction = "left"
                    lead_y_change = 0
                    lead_x_change = -block_size
                    change_pos = True
                elif event.key == pygame.K_RIGHT and lead_x_change != -block_size and not change_pos:
                    direction = "right"
                    lead_y_change = 0
                    lead_x_change = block_size
                    change_pos = True
                elif event.key == pygame.K_UP and lead_y_change != block_size and not change_pos:
                    direction = "up"
                    lead_x_change = 0
                    lead_y_change = -block_size
                    change_pos = True
                elif event.key == pygame.K_DOWN and lead_y_change != -block_size and not change_pos:
                    direction = "down"
                    lead_x_change = 0
                    lead_y_change = block_size
                    change_pos = True

                    # if event.type == pygame.KEYUP:
                    #     if event.key == pygame.K_LEFT or event.key ==  pygame.K_RIGHT:
                    #         lead_x_change = 0
                    #     if event.key == pygame.K_UP or event.key ==  pygame.K_DOWN:
                    #         lead_y_change = 0

        snake.addToPosition(lead_x_change, lead_y_change, direction)

        if collisionWithWall(snake) or snake.headCollisionWithBody():
            gameOver = True
        else:
            for apple in apples:
                if apple.collisionWithApple(snake.width, snake.head_x, snake.head_y):
                        snake.grow(apple.score)
                        rand_apple_x, rand_apple_y = random_pos()
                        apple.newRandomApple(rand_apple_x, rand_apple_y)

            gameDisplay.fill(background)

            for apple in apples:
                apple.printApple()


            snake.printSnake()

        clock.tick(FPS)
        pygame.display.update()

    pygame.quit()
    quit()


def main():
    gameLoop()


if __name__ == "__main__":
    main()
