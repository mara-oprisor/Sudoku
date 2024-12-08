import pygame
ROWS = 9
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
BLUE = (0, 0 ,255)
LiGHT_BLUE = (100, 100, 255)
SIZE = 600


class Board:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((600, 600))
        self.cell_size = SIZE // ROWS
        self.font = pygame.font.SysFont("calibri", 50)

    def draw_grid(self):
        self.window.fill(WHITE)
        pygame.display.set_caption("Sudoku 9x9")
        for row in range(ROWS):
            for col in range(ROWS):
                cell_rect = pygame.Rect(col * self.cell_size, row * self.cell_size, self.cell_size, self.cell_size)
                pygame.draw.rect(self.window, GRAY, cell_rect, 1)
        

        for i in range(ROWS + 1):
            if i % 3 == 0:
                thickness = 4
            else:
                thickness = 1
            
            pygame.draw.line(self.window, BLACK, (0, i * self.cell_size), (SIZE, i * self.cell_size), thickness)
            pygame.draw.line(self.window, BLACK, (i * self.cell_size, 0), (i * self.cell_size, SIZE), thickness)


    

