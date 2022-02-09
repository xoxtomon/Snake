import pygame
import random


class Fruit:
    def __init__(self, screen, squareSize, scale):
        self.screen = screen
        self.posx = 0
        self.posy = 0
        self.fruitSize = squareSize/2
        self.scale = scale

    def drawFruit(self):
        circle = (self.posx + 25, self.posy + 25)
        pygame.draw.circle(self.screen, (248, 60, 71), circle,
                           self.fruitSize*self.scale)

    def update_X_and_Y(self):
        self.posx = random.randrange(0, 500, 50)
        self.posy = random.randrange(0, 500, 50)

    def newFruit(self):
        self.update_X_and_Y()
        self.drawFruit()
