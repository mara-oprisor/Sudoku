import pygame

from square import Square

ROWS = 9
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
BLUE = (0, 0, 255)
LIGHT_BLUE = (100, 100, 255)
SIZE = 600


class Board:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((SIZE, SIZE))
        self.cell_size = SIZE // ROWS
        self.font = pygame.font.SysFont("calibri", 50)
        self.cells = []  # This will hold Square objects.
        self.selected_cell = None  # Stores the currently selected cell as (row, col)
        self.init_cells()

    def init_cells(self):
        """
        Initializes the cells of the Sudoku board as 81 Square objects.
        Each square is associated with its position on the grid.
        """
        self.cells = []
        for row in range(ROWS):
            for col in range(ROWS):
                start_x = col * self.cell_size
                start_y = row * self.cell_size
                end_x = start_x + self.cell_size
                end_y = start_y + self.cell_size
                # Create a Square object for each cell and append it to the cells list.
                self.cells.append(Square(start_x, start_y, end_x, end_y))

    def draw_grid(self):
        """
        Draws the Sudoku grid on the screen.
        """
        self.window.fill(WHITE)
        pygame.display.set_caption("Sudoku 9x9")

        # Draw cells with the selected cell highlighted
        for row in range(ROWS):
            for col in range(ROWS):
                cell_rect = pygame.Rect(col * self.cell_size, row * self.cell_size, self.cell_size, self.cell_size)
                if self.selected_cell == (row, col):
                    pygame.draw.rect(self.window, LIGHT_BLUE, cell_rect)  # Highlight the selected cell
                pygame.draw.rect(self.window, GRAY, cell_rect, 1)

        # Draw thicker lines for the 3x3 subgrids.
        for i in range(ROWS + 1):
            if i % 3 == 0:
                thickness = 4
            else:
                thickness = 1

            pygame.draw.line(self.window, BLACK, (0, i * self.cell_size), (SIZE, i * self.cell_size), thickness)
            pygame.draw.line(self.window, BLACK, (i * self.cell_size, 0), (i * self.cell_size, SIZE), thickness)

    def draw_numbers(self):
        """
        Draws the numbers from the cells on the grid.
        """
        for idx, square in enumerate(self.cells):
            if not square.is_empty():
                x = square.start[0] + self.cell_size // 2
                y = square.start[1] + self.cell_size // 2
                number_surface = self.font.render(str(square.number), True, BLACK)
                # Center the number on the square.
                number_rect = number_surface.get_rect(center=(x, y))
                self.window.blit(number_surface, number_rect)

    def select_cell(self, pos):
        """
        Selects a cell based on the given mouse position and highlights it.

        Args:
            pos (tuple): The (x, y) position of the mouse click.
        """
        x, y = pos
        if x < 0 or x >= SIZE or y < 0 or y >= SIZE:
            self.selected_cell = None
        else:
            col = x // self.cell_size
            row = y // self.cell_size
            self.selected_cell = (row, col)

    def set_cell(self, row, col, number):
        """
        Sets the number for a specific cell.

        Args:
            row (int): The row of the cell.
            col (int): The column of the cell.
            number (int): The number to set in the cell.
        """
        index = row * ROWS + col
        self.cells[index].set_number(number)

    def update_display(self):
        """
        Updates the display to show the current state of the board.
        """
        self.draw_grid()
        self.draw_numbers()
        pygame.display.update()



