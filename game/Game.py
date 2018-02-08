import pygame
import time
import random

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 150, 0)
FPS = 15

font_size = 25
main_font = pygame.font.SysFont(None, font_size)


class Game:

    def __init__(self, display_width=800, display_height=600, background=(0, 30, 0)):
        self.display_width = display_width
        self.display_height = display_height
        self.background = background
        pygame.init()
        gameDisplay = pygame.display.set_mode((self.display_width, self.display_height))
        display_center = (display_width / 2, display_height / 2)

    pygame.display.set_caption("Snake")

    block_size = 20
    clock = pygame.time.Clock()

    # display_width = 800
    # display_height = 600

    def message_to_screen(self, msg, color):
        screen_text = main_font.render(msg, True, color)
        self.gameDisplay.blit(screen_text, [self.display_center[0] - ((len(msg) * 8) / 2), self.display_center[1]])
        pygame.display.update()
        self.display_center

    def randomApple(self):
        randAppleX = round(
            random.randrange(0, self.display_width - self.block_size) / self.block_size) * self.block_size
        randAppleY = round(
            random.randrange(0, self.display_height - self.block_size) / self.block_size) * self.block_size
        return (randAppleX, randAppleY)

    def gameLoop(self):
        gameExit = False
        gameOver = False

        lead_x = self.display_width / 2
        lead_y = self.display_height / 2
        lead_x_change = 0
        lead_y_change = 0
        score = 0

        randAppleX, randAppleY = self.randomApple()

        while not gameExit:

            while gameOver == True:
                self.message_to_screen("GAME OVER! Press 'P' to play again! or 'Q' to quit", red)

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        gameOver = False
                        gameExit = True
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_p:
                            self.gameLoop()
                        elif event.key == pygame.K_q:
                            gameOver = False
                            gameExit = True

                            # game
            for event in pygame.event.get():
                # print(event)

                if event.type == pygame.QUIT:
                    gameExit = True

                    # control snake
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT and lead_x_change != self.block_size:
                        lead_y_change = 0
                        lead_x_change = -self.block_size
                    elif event.key == pygame.K_RIGHT and lead_x_change != -self.block_size:
                        lead_y_change = 0
                        lead_x_change = self.block_size
                    elif event.key == pygame.K_UP and lead_y_change != self.block_size:
                        lead_x_change = 0
                        lead_y_change = -self.block_size
                    elif event.key == pygame.K_DOWN and lead_y_change != -self.block_size:
                        lead_x_change = 0
                        lead_y_change = self.block_size

                        # if event.type == pygame.KEYUP:
                        #     if event.key == pygame.K_LEFT or event.key ==  pygame.K_RIGHT:
                        #         lead_x_change = 0
                        #     if event.key == pygame.K_UP or event.key ==  pygame.K_DOWN:
                        #         lead_y_change = 0

            lead_x += lead_x_change
            lead_y += lead_y_change

            # go on wall = game over
            if (lead_x < 0 or lead_x >= self.display_width) or (lead_y < 0 or lead_y >= self.display_height):
                gameOver = True
                # pygame.quit()
            else:
                if (randAppleX == lead_x and randAppleY == lead_y):
                    randAppleX, randAppleY = self.randomApple()
                    score += 1
                    self.randomApple()

                self.gameDisplay.fill(self.background)
                self.gameDisplay.fill(red, rect=[randAppleX, randAppleY, self.block_size, self.block_size])
                pygame.draw.rect(self.gameDisplay, green, [lead_x, lead_y, self.block_size, self.block_size])

            self.clock.tick(FPS)
            pygame.display.update()

        pygame.quit()
        quit()