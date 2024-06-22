import pygame
import random
import game_board
from colors import Colors
from position import Position

class GamePiece:
    """Initiiert die Spielsteine"""
    def __init__(self, shape):
        self.shape = shape
        self.cells = {}
        self.cell_size = 30
        self.row_offset = 0
        self.col_offset = 0
        self.rotation_state = 0
        self.colors = Colors.get_color()

    def move(self, rows, cols, game_board=None):
        self.row_offset += rows
        self.col_offset += cols
        if game_board and self.check_collision(game_board):
            self.row_offset -= rows
            self.col_offset -= cols
            return False
        return True

    def get_cell_positions(self):
        tiles = self.cells[self.rotation_state]
        moved_tiles = []
        for position in tiles:
            position = Position(position.row + self.row_offset, position.col + self.col_offset)
            moved_tiles.append(position)
        return moved_tiles

    def draw_piece(self, screen, offset_x=0, offset_y=0):
        tiles = self.get_cell_positions()
        for tile in tiles:
            tile_rect = pygame.Rect(tile.col * self.cell_size + 1 + offset_x, tile.row * self.cell_size + 1 + offset_y,
                                    self.cell_size - 1, self.cell_size - 1)
            pygame.draw.rect(screen, self.colors[self.shape], tile_rect)
            
    def rotate(self, game_board):
        original_rotation_state = self.rotation_state
        self.rotation_state = (self.rotation_state + 1) % 4
        if self.check_collision(game_board):
            self.rotation_state = original_rotation_state
            return False
        return True
    
    def check_collision(self, game_board):
        for position in self.get_cell_positions():
            if position.row >= game_board.rows or position.col >= game_board.cols or position.col < 0 or game_board.grid[position.row][position.col] != 0:
                return True
        return False

    def draw_next_piece(self, screen, start_col, start_row):
        tiles = self.cells[self.rotation_state]
        for tile in tiles:
            tile_rect = pygame.Rect(
                (tile.col + start_col) * self.cell_size + 1, 
                (tile.row + start_row) * self.cell_size + 1,
                self.cell_size - 1, self.cell_size - 1
            )
            pygame.draw.rect(screen, self.colors[self.shape], tile_rect)