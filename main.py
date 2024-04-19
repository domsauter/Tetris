
import pygame
from game_board import GameBoard
from game_piece import *

def main():
    pygame.init()
    clock = pygame.time.Clock()

    # KONSTANTEN
    WINDOW_WIDTH = 500
    WINDOW_HEIGHT = 500
    GAME_BOARD_WIDTH = 10
    GAME_BOARD_HEIGHT = 20

    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)

    # Erstelle die Spielsteine
    game_pieces = {
        'I': GamePiece(I_SHAPE, COLORS['I']),
        'J': GamePiece(J_SHAPE, COLORS['J']),
        'L': GamePiece(L_SHAPE, COLORS['L']),
        'O': GamePiece(O_SHAPE, COLORS['O']),
        'S': GamePiece(S_SHAPE, COLORS['S']),
        'T': GamePiece(T_SHAPE, COLORS['T']),
        'Z': GamePiece(Z_SHAPE, COLORS['Z']),
    }

    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Tetris")
    game_board = GameBoard(GAME_BOARD_WIDTH, GAME_BOARD_HEIGHT)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Spiellogik hier einfügen (z.B. Spielsteine bewegen, Kollisionen überprüfen, etc.)

        # Spielfeld zeichnen
        window.fill((0, 0, 0))  # Hintergrund löschen

        # Spielfeld zeichnen
        for y in range(GAME_BOARD_HEIGHT):
            for x in range(GAME_BOARD_WIDTH):
                # Die Position jedes Rechtecks berechnen
                rect = pygame.Rect(x * (WINDOW_WIDTH // GAME_BOARD_WIDTH),
                                   y * (WINDOW_HEIGHT // GAME_BOARD_HEIGHT),
                                   WINDOW_WIDTH // GAME_BOARD_WIDTH,
                                   WINDOW_HEIGHT // GAME_BOARD_HEIGHT)
                # Wenn die Zelle leer ist, zeichne ein weißes Rechteck, ansonsten fülle es mit der Farbe des Tetrominos
                if game_board.grid[y][x] == 0:
                    pygame.draw.rect(window, WHITE, rect)
                else:
                    pygame.draw.rect(window, game_board.grid[y][x], rect)

                # Zeichne Trennlinien zwischen den Zellen
                pygame.draw.rect(window, BLACK, rect, 1)

        # Spielfeldgrenzen zeichnen (optional)
        # pygame.draw.rect(window, BLACK, pygame.Rect(0, 0, WINDOW_WIDTH, WINDOW_HEIGHT), 1)

        # pygame.display.update() # Kein Update innerhalb der Schleife, um die Performance zu verbessern

        pygame.display.update()

        # Spielgeschwindigkeit festlegen
        clock.tick(30)  # Hier 30 FPS (Frames per Second)

    pygame.quit()

if __name__ == "__main__":
    main()