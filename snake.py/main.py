import sys
import pygame
import window
import board
import snake

WINDOW_W, WINDOW_H = 500, 500
SCREEN = pygame.display.set_mode((WINDOW_W, WINDOW_H))
SQUARE_SIZE = 50


def main():
    window.window(WINDOW_W, WINDOW_H)
    myBoard = board.Board(SCREEN, WINDOW_H, WINDOW_W, SQUARE_SIZE)
    myBoard.printBoard()
    mySnake = snake.Snake(SCREEN, 206.25, 206.25, SQUARE_SIZE)
    mySnake.drawSnake()
    playing = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if not playing:
                    playing = True
                    mySnake.setCurrDir(event.key)

                if event.key == pygame.K_RIGHT:
                    mySnake.move('right')
                elif event.key == pygame.K_LEFT:
                    mySnake.move('left')
                elif event.key == pygame.K_UP:
                    mySnake.move('up')
                elif event.key == pygame.K_DOWN:
                    mySnake.move('down')
                myBoard.printBoard()
                mySnake.drawSnake()
            pygame.display.update()


if __name__ == '__main__':
    main()
