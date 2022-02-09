import pygame


class Snake:
    def __init__(self, screen, posxHead, posyHead, squareSize, scale):
        self.body = [(posxHead, posyHead),
                     (posxHead-squareSize, posyHead),
                     (posxHead-squareSize*2, posyHead)]
        self.bodySize = squareSize * scale
        self.bodyScale = scale
        self.bodyColor = (51, 53, 156)
        self.screen = screen
        self.currDirection = 'right'

    def drawSnake(self):
        for part in self.body:
            rect = (part[0], part[1], self.bodySize, self.bodySize)
            pygame.draw.rect(self.screen, self.bodyColor, rect)

    def move(self, direction):
        if direction == 'right':
            self.body.insert(
                0, (self.body[0][0] + (self.bodySize/self.bodyScale), self.body[0][1]))
        elif direction == 'left':
            self.body.insert(
                0, (self.body[0][0] - (self.bodySize/self.bodyScale), self.body[0][1]))
        elif direction == 'up':
            self.body.insert(
                0, (self.body[0][0], self.body[0][1] - (self.bodySize/self.bodyScale)))
        elif direction == 'down':
            self.body.insert(
                0, (self.body[0][0], self.body[0][1] + (self.bodySize/self.bodyScale)))
        self.body.pop()
        print(f'Body: {self.body}\nDirection: {self.currDirection}')

    def setCurrDir(self, direction):
        self.currDirection = direction

    def getNextmove(self, dir):
        if dir == 'right':
            return self.body[0][0] + (self.bodySize/self.bodyScale)
        if dir == 'left':
            return self.body[0][0] - (self.bodySize/self.bodyScale)
        if dir == 'up':
            return self.body[0][1] - (self.bodySize/self.bodyScale)
        if dir == 'down':
            return self.body[0][1] + (self.bodySize/self.bodyScale)
