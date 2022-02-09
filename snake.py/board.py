import sys, pygame

class Board:
	def __init__(self,screen,height, width, sqr_size):
		self.screen = screen
		self.boardH = height
		self.boardW = width
		self.sqr_size = sqr_size
		self.primaryC = (17, 182, 107) #(159, 226, 191)
		self.secondaryC = (92, 182, 17) #(64, 224, 208)

	def printBoard(self):
		for i in range(10):
			for j in range(10):
				rect = pygame.Rect(j*self.sqr_size, i*self.sqr_size, self.sqr_size, self.sqr_size)
				if i % 2:
					if j % 2:
						pygame.draw.rect(self.screen, self.primaryC, rect)
					else:
						pygame.draw.rect(self.screen, self.secondaryC, rect)
				else:
					if j % 2:
						pygame.draw.rect(self.screen, self.secondaryC, rect)
					else:
						pygame.draw.rect(self.screen, self.primaryC, rect)