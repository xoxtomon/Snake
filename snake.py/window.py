import pygame

def window(width, height):
	pygame.init()

	size = width, height
	speed = [2, 2]
	black = 0, 0, 0

	screen = pygame.display.set_mode(size)
	