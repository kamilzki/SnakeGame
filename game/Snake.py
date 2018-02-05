

class Snake:

    def __init__(self, x,y):
        self.body = [(x,y)]
        self.score = 0

    def scoreMore(self, x, y):
        self.score += 1
        self.body += (x,y)

