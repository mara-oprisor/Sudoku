import pygame
from board import *
from file_creator import *
from sudoku_generator import generate_random_sudoku

if __name__ == "__main__":
    pygame.init()

    grid = generate_random_sudoku(20)
    file_creator = FileCreator(grid)

    file_creator.create_file()
    file_creator.run_mace4()
    result = file_creator.parse_mace4_output()

    if result["success"] == "1":
        print("Process was successful.")
        print("Generated Sudoku Grid:")
        for row in result["sudoku_grid"]:
            print(row)
    else:
        print("Process was not successful.")

    run = True

    board = Board()
    board.draw_grid()
    pygame.display.update()

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                selected_cell = board.select_cell(mouse_pos)

            if event.type == pygame.KEYDOWN and selected_cell:
                if pygame.K_1 <= event.key <= pygame.K_9:
                    number = event.key - pygame.K_0
                    row, col = selected_cell
                    board.set_cell(row, col, number)
                    board.update_display()

            if event.type == pygame.K_SPACE:
                pass

        board.update_display()

    pygame.quit()
