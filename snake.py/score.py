import pygame


class Score():
    def __init__(self, x, y, fontSize, fontColor, font):
        self.currentScore = 0
        self.font = pygame.font.SysFont(font, fontSize)
        self.text_Pos_x = x
        self.text_Pos_y = y

    def updateScore(self, score):
        self.currentScore += score

    def drawScore(self, screen):
        text = self.font.render(str(self.currentScore), True, (0, 0, 0))
        screen.blit(text, (self.text_Pos_x, self.text_Pos_y))
