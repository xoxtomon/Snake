import pygame


class Snake:
    def __init__(self, screen, posxHead, posyHead, squareSize):
        self.body = [(posxHead, posyHead),
                     (posxHead-squareSize, posyHead),
                     (posxHead-squareSize*2, posyHead)]
        self.bodySize = squareSize * 0.75
        self.bodyColor = (51, 53, 156)
        self.screen = screen
        self.currDirection = 'none'

    def drawSnake(self):
        for part in self.body:
            rect = (part[0], part[1], self.bodySize, self.bodySize)
            pygame.draw.rect(self.screen, self.bodyColor, rect)

    def move(self, direction):
        if direction == 'right':
            self.body.insert(
                0, (self.body[0][0] + (self.bodySize/0.75), self.body[0][1]))
        elif direction == 'left':
            self.body.insert(
                0, (self.body[0][0] - (self.bodySize/0.75), self.body[0][1]))
        elif direction == 'up':
            self.body.insert(
                0, (self.body[0][0], self.body[0][1] - (self.bodySize/0.75)))
        elif direction == 'down':
            self.body.insert(
                0, (self.body[0][0], self.body[0][1] + (self.bodySize/0.75)))
        self.body.pop()
        print(f'Body: {self.body}\nDirection: {self.currDirection}')

    def setCurrDir(self, direction):
        self.currDirection = direction
