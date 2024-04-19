
import pygame
from game_board import GameBoard
from game_piece import GamePiece

def main():
    pygame.init()

    # KONSTANTEN
    WINDOW_WIDTH = 500
    WINDOW_HEIGHT = 500

    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)

    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Tetris")

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

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()