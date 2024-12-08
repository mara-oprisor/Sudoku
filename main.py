import pygame
from board import *
from file_creator import *
from sudoku_generator import generate_random_sudoku

if __name__ == "__main__":
    pygame.init()
    run = True

    board = Board()
    board.draw_grid()
    pygame.display.update()
    
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

    pygame.quit()
