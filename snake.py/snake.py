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
        increment = (self.bodySize/self.bodyScale)
        if direction == 'right':
            self.body.insert(
                0, (self.body[0][0] + increment, self.body[0][1]))
        elif direction == 'left':
            self.body.insert(
                0, (self.body[0][0] - increment, self.body[0][1]))
        elif direction == 'up':
            self.body.insert(
                0, (self.body[0][0], self.body[0][1] - increment))
        elif direction == 'down':
            self.body.insert(
                0, (self.body[0][0], self.body[0][1] + increment))
        self.body.pop()
        # print(f'Body: {self.body}\nDirection: {self.currDirection}')

    def setCurrDir(self, direction):
        self.currDirection = direction

    def checkEatFruit(self, posx, posy):
        return (posx + 6.25) == self.body[0][0] and (posy + 6.25) == self.body[0][1]

    def grow(self):
        if self.currDirection == 'right':
            self.body.append(
                (self.body[0][0] - self.bodySize, self.body[0][1]))
        elif self.currDirection == 'left':
            self.body.append(
                (self.body[0][0] + self.bodySize, self.body[0][1]))
        elif self.currDirection == 'up':
            self.body.append(
                (self.body[0][0], self.body[0][1] + self.bodySize))
        else:
            self.body.append(
                (self.body[0][0], self.body[0][1] - self.bodySize))

    def checkDeath(self, WINDOW_H, WINDOW_W):
        # TODO: KILL WITH BOUNDARIES
        snakeHead = self.body[0]

        eatMyself = snakeHead in self.body[1:]
        
        passWidth = snakeHead[0] > WINDOW_W or snakeHead[0] < 0
        passHeight = snakeHead[1] > WINDOW_H or snakeHead[1] < 0 

        # return eatMyself and not passWidth and not passHeight
        return eatMyself and not passHeight and not passWidth

