from colors import Colors
import pygame

class GamePiece:
    """Initiiert die Spielsteine"""
    def __init__(self, shape):
        self.shape = shape
        self.cells = {}
        self.cell_size = 30
        self.rotation_state = 0
        self.colors = Colors.get_color()

    def draw_piece(self, screen):
        tiles = self.cells[self.rotation_state]
        for tile in tiles:
            tile_rect = pygame.Rect(tile.col * self.cell_size + 1, tile.row * self.cell_size + 1,
            self.cell_size - 1, self.cell_size - 1)
            pygame.draw.rect(screen, self.colors[self.shape], tile_rect)
