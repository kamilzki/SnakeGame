import random

import pygame

class Apple:

    def __init__(self, score, pos_x, pos_y, gameDisplay):
        self.score = score
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.game_display = gameDisplay
        self.refreshWidthAndImage()

    def refreshWidthAndImage(self):
        if self.score == 1:
            self.img = pygame.image.load('images/apple_green.png')
            self.width = 30
        elif self.score == 2:
            self.img = pygame.image.load('images/apple_red.png')
            self.width = 25
        elif self.score == 3:
            self.img = pygame.image.load('images/apple_gold.png')
            self.width = 15

    def printApple(self):
        self.game_display.blit(self.img, (self.pos_x, self.pos_y))

    def getPosition(self):
        return (self.pos_x, self.pos_x)

    def newRandomApple(self, pos_x, pos_y):
        # self.score = random.randrange(1,4)
        self.score = self.chooseApple()
        self.pos_x = pos_x
        self.pos_y = pos_y

        self.refreshWidthAndImage()

    def collisionWithApple(self, obj_width, obj_pos_x, obj_pos_y_):
            if ((self.pos_x + obj_width >= obj_pos_x and self.pos_x <= obj_pos_x + self.width)
                and (self.pos_y + obj_width >= obj_pos_y_ and self.pos_y <= obj_pos_y_ + self.width)):
                return True
            else:
                return False

    def chooseApple(self):
        rand_num = random.randrange(0, 100)
        if rand_num < 45:
            return 1
        elif rand_num < 75:
            return 2
        else:
            return 3

