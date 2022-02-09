import sys, pygame
import window
import board

WINDOW_W , WINDOW_H = 500, 500
SCREEN = pygame.display.set_mode((WINDOW_W, WINDOW_H))
SQUARE_SIZE = 50

def main():
	window.window(WINDOW_W , WINDOW_H)
	myBoard = board.Board(SCREEN,WINDOW_H,WINDOW_W,SQUARE_SIZE)
	myBoard.printBoard()

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

		pygame.display.update()

if __name__ == '__main__':
	main()