import sys
import pygame
import window
import board
import snake
import fruit
import time
import score

WINDOW_W, WINDOW_H = 500, 500
SCREEN = pygame.display.set_mode((WINDOW_W, WINDOW_H))
# TODO BOARD LIMITS
# BOARD_LIMITS =
SQUARE_SIZE = 50
SNAKE_SCALE = 0.75
SNAKE_STEP = 0.15
FRUIT_SCALE = 0.80


def main():
    pygame.init()
    myBoard = board.Board(SCREEN, WINDOW_H, WINDOW_W, SQUARE_SIZE)
    mySnake = snake.Snake(SCREEN, 206.25, 206.25, SQUARE_SIZE, SNAKE_SCALE)
    myFruit = fruit.Fruit(SCREEN, SQUARE_SIZE, FRUIT_SCALE)
    myScore = score.Score(12, 0, 25, (255, 82, 0), 'arial')
    window.window(WINDOW_W, WINDOW_H)
    myBoard.printBoard()
    mySnake.drawSnake()
    myFruit.newFruit()
    myScore.drawScore(SCREEN)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT and mySnake.currDirection != 'left':
                    mySnake.move('right')
                    mySnake.setCurrDir('right')
                elif event.key == pygame.K_LEFT and mySnake.currDirection != 'right':
                    mySnake.move('left')
                    mySnake.setCurrDir('left')
                elif event.key == pygame.K_UP and mySnake.currDirection != 'down':
                    mySnake.move('up')
                    mySnake.setCurrDir('up')
                elif event.key == pygame.K_DOWN and mySnake.currDirection != 'up':
                    mySnake.move('down')
                    mySnake.setCurrDir('down')

                time.sleep(SNAKE_STEP)
                myBoard.printBoard()
                myFruit.drawFruit()

                if mySnake.checkEatFruit(myFruit.posx, myFruit.posy):
                    myFruit.newFruit()
                    mySnake.grow()
                    myScore.updateScore(100)

                mySnake.drawSnake()
                myScore.drawScore(SCREEN)
                pygame.display.update()

                if mySnake.checkDeath(WINDOW_H, WINDOW_W):
                    print(f"Score:{myScore.currentScore}")
                    sys.exit()

        mySnake.move(mySnake.currDirection)
        myBoard.printBoard()
        myFruit.drawFruit()

        if mySnake.checkEatFruit(myFruit.posx, myFruit.posy):
            myFruit.newFruit()
            mySnake.grow()
            myScore.updateScore(100)
        myScore.drawScore(SCREEN)

        if mySnake.checkDeath(WINDOW_H, WINDOW_W):
            print(f"Score:{myScore.currentScore}")
            sys.exit()

        mySnake.drawSnake()

        time.sleep(SNAKE_STEP)
        pygame.display.update()


if __name__ == '__main__':
    main()
