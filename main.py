import pygame
import sys
from game_board import GameBoard
from game_piece import GamePiece
from game_pieces import *

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

game_board = GameBoard()

game_piece = LShape()

game_board.print_board()

# Aktuell fallender Spielstein
# current_piece = GamePiece(I_SHAPE, COLORS['I']) # Beispiel: Starte mit einem I-Stück
# current_piece.x = GAME_BOARD_WIDTH // 2 - 2
# current_piece.y = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(DARK_BLUE)
    game_board.draw_board(screen)
    game_piece.draw_piece(screen)



    # Spiellogik hier einfügen (z.B. Spielsteine bewegen, Kollisionen überprüfen, etc.)

    # Spielfeldgrenzen zeichnen (optional)
    # pygame.draw.rect(window, BLACK, pygame.Rect(0, 0, WINDOW_WIDTH, WINDOW_HEIGHT), 1)

    # pygame.display.update() # Kein Update innerhalb der Schleife, um die Performance zu verbessern

    pygame.display.update()

    # Spielgeschwindigkeit festlegen
    clock.tick(60)

pygame.quit()