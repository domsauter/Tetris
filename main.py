import pygame
import sys
from pygame.locals import *
from game_board import GameBoard
from game_piece import GamePiece
from game_pieces import *
from random_piece import *

# KONSTANTEN
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

BOARD_MARGIN_RIGHT = 200  # Abstand zwischen Spielfeld und Fensterrand

WHITE = (255, 255, 255)
DARK_BLUE = (47, 50, 90)

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tetris")

clock = pygame.time.Clock()

# Game-Klasse erstellen.

game_board = GameBoard()

game_piece = create_random_stone()

game_board.print_board()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_LEFT:
                game_piece.move(0, -1)
            elif event.key == K_RIGHT:
                game_piece.move(0, 1)
            elif event.key == K_DOWN:
                game_piece.move(1, 0)
            elif event.key == K_UP:
                if not isinstance(game_piece, OShape):
                    game_piece.rotate()

    screen.fill(DARK_BLUE)
    game_board.draw_board(screen)
    game_piece.draw_piece(screen)

    pygame.display.update()

    # Spielgeschwindigkeit festlegen
    clock.tick(60)

pygame.quit()