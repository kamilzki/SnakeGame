
class Snake:

    def __init__(self, head_x,head_y):
        self.head_x, self.head_y = head_x, head_y
        self.body = []
        self.score = 0

    def scoreMore(self, x, y):
        self.body.append((x, y))
        self.score += 1

    def addToPosition(self, newX, newY):
        prev_head_x, prev_head_y = self.head_x, self.head_y
        if self.score > 0:
            self.body.pop()
            self.body.insert(0, (self.head_x, self.head_y))

        self.head_x += newX
        self.head_y += newY
        # for i in range(self.score):
        #     print(self.body[i])
        #     tmp_x, tmp_y = self.body[i]
        #     self.body[i] = (prev_head_x, prev_head_y)
        #     prev_head_x, prev_head_y = tmp_x, tmp_y

    def collisionWithBody(self):
        for body_block in self.body:
            if body_block == (self.head_x, self.head_y):
                return True
        return False

