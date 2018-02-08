import pygame

snake_head_img = pygame.image.load('images/snake_head.png')
snake_body_img = pygame.image.load('images/snake_body.png')
snakeBodyBend_img = pygame.image.load('images/snake_body_bend.png')
snakeTail_img = pygame.image.load('images/snake_tail.png')


class Snake:
    def __init__(self, head_x, head_y, gameDisplay, width, direction="up"):
        self.head_x, self.head_y = head_x, head_y
        self.body = []
        self.score = 0
        self.length = self.score
        self.direction = direction
        tmpY = self.head_y
        for i in range(self.score):
            tmpY += 20
            self.body.append((self.head_x, tmpY, self.direction))
            # self.body.insert(i, (self.head_x-20, self.head_y-20))
        self.gameDisplay = gameDisplay
        self.width = width

    def grow(self, score):
        self.score += score

    def addToPosition(self, newX, newY, direction):
        if self.score > 0:
            if self.score > self.length:
                print("dodajemy...")
                self.body.insert(0, (self.head_x, self.head_y, direction))
                self.length += 1
            else:
                print("pop")
                self.body.pop()
                self.body.insert(0, (self.head_x, self.head_y, direction))

        self.head_x += newX
        self.head_y += newY
        self.direction = direction

    def headCollisionWithBody(self):
        print("len body: "+ str(len(self.body)))

        for body_block in self.body:
            if (body_block[0], body_block[1]) == (self.head_x, self.head_y):
                print(str(body_block[0]) +", "+ str(body_block[1]) + " == " + str(self.head_x) +", "+ str(self.head_y))

                # if (self.head_x + 20 > body_block[0] and self.head_x < body_block[0] + 20) \
                #         and (self.head_y + 20 > body_block[1] and self.head_y < body_block[1] + 20):

                return True
        return False

    def collisionWithBody(self, pos_x, pos_y, size_obj):
        for body_block in self.body:

            # if (body_block[0], body_block[1]) == (posX, posY):
            if (pos_x + size_obj >= body_block[0] and pos_x <= body_block[0] + self.width) \
                    and (pos_y + size_obj >= body_block[1] and pos_y <= body_block[1] + self.width):
                print(str(body_block) + " == " + str(pos_x) + ", " + str(pos_y))
                print("TRUE")
                return True
        return False

    def printSnake(self):

        head_img = snake_head_img

        if self.direction == "right":
            head_img = pygame.transform.rotate(snake_head_img, 270)
        elif self.direction == "left":
            head_img = pygame.transform.rotate(snake_head_img, 90)
        elif self.direction == "down":
            head_img = pygame.transform.rotate(snake_head_img, 180)

        # draw snake's head
        self.gameDisplay.blit(head_img, (self.head_x, self.head_y))

        # draw snake's body
        for i in range(self.length):
            # pygame.draw.rect(gameDisplay, body_color, [snake.body[i][0], snake.body[i][1], block_size, block_size])

            if i < self.length - 1:
                # if (self.body[i][0], self.body[i][1]) != (self.body[i + 1][0], self.body[i + 1][1]):

                    direction_body = self.body[i][2]
                    further_direction = self.body[i + 1][2]

                    if direction_body == further_direction:
                        if direction_body == "right":
                            body_img = pygame.transform.rotate(snake_body_img, 270)
                        elif direction_body == "left":
                            body_img = pygame.transform.rotate(snake_body_img, 90)
                        elif direction_body == "down":
                            body_img = pygame.transform.rotate(snake_body_img, 180)
                        else:
                            body_img = snake_body_img

                        self.gameDisplay.blit(body_img, (self.body[i][0], self.body[i][1]))
                    else:
                        if direction_body == "up":
                            if further_direction == "left":
                                body_bend_img = pygame.transform.rotate(snakeBodyBend_img, 90)
                            else:  # right
                                body_bend_img = pygame.transform.rotate(snakeBodyBend_img, 180)
                        elif direction_body == "down":
                            if further_direction == "left":
                                body_bend_img = snakeBodyBend_img
                            else:  # right
                                body_bend_img = pygame.transform.rotate(snakeBodyBend_img, -90)
                        elif direction_body == "left":
                            if further_direction == "up":
                                body_bend_img = pygame.transform.rotate(snakeBodyBend_img, -90)
                            else:  # down
                                body_bend_img = pygame.transform.rotate(snakeBodyBend_img, 180)
                        else:  # direction_body == "right"
                            if further_direction == "up":
                                body_bend_img = snakeBodyBend_img
                            else:  # down
                                body_bend_img = pygame.transform.rotate(snakeBodyBend_img, 90)

                        self.gameDisplay.blit(body_bend_img, (self.body[i][0], self.body[i][1]))

            else:
                before_direction = self.body[i][2]
                if before_direction == "right":
                    tail_img = pygame.transform.rotate(snakeTail_img, -90)
                elif before_direction == "left":
                    tail_img = pygame.transform.rotate(snakeTail_img, 90)
                elif before_direction == "down":
                    tail_img = pygame.transform.rotate(snakeTail_img, 180)
                else:
                    tail_img = snakeTail_img

                self.gameDisplay.blit(tail_img, (self.body[i][0], self.body[i][1]))
