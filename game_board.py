import pygame
from colors import Colors

class GameBoard:
    def __init__(self):
        """Initialisiert das Spielfeld"""
        self.rows = 20
        self.cols = 10
        self.cell_size = 30
        self.grid = [[0 for j in range(self.cols)] for i in range(self.rows)] # Erstelle ein leeres Spielfeld
        self.colors = Colors.get_color()

    def print_board(self):
        for row in range(self.rows):
            for col in range(self.cols):
                print(self.grid[row][col], end = " ")
            print()

    def draw_board(self, screen, score):
        for row in range(self.rows):
            for col in range(self.cols):
                cell_value = self.grid[row][col]
                cell_rect = pygame.Rect(col * self.cell_size + 1, row * self.cell_size + 1,
                                        self.cell_size - 1, self.cell_size - 1)
                pygame.draw.rect(screen, self.colors[cell_value], cell_rect)

        # Draw the score
        font = pygame.font.SysFont(None, 36)
        score_text = font.render(f"Score: {score}", True, (255, 255, 255))
        screen.blit(score_text, (self.cols * self.cell_size + 20, 20))

    def lock_piece(self, game_piece):
        for position in game_piece.get_cell_positions():
            self.grid[position.row][position.col] = game_piece.shape
        self.clear_full_rows()

    def clear_full_rows(self):
        full_rows = 0
        for row in range(self.rows):
            if all(cell != 0 for cell in self.grid[row]):
                full_rows += 1
                del self.grid[row]
                self.grid.insert(0, [0 for _ in range(self.cols)])
        return full_rows

    def is_game_over(self):
        return any(cell != 0 for cell in self.grid[0])