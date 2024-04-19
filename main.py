
import pygame

class GamePiece:
    def __init__(self, shape, color):
        self.shape = shape
        self.color = color

# Formen der Spielsteine
I_SHAPE = [
    [(0, 0), (1, 0), (2, 0), (3, 0)],
]

J_SHAPE = [
    [(0, 0), (0, 1), (1, 1), (2, 1)],
]

L_SHAPE = [
    [(0, 1), (1, 1), (2, 1), (2, 0)],
]

O_SHAPE = [
    [(0, 0), (0, 1), (1, 0), (1, 1)],
]

S_SHAPE = [
    [(1, 0), (2, 0), (0, 1), (1, 1)],
]

T_SHAPE = [
    [(0, 1), (1, 0), (1, 1), (2, 1)],
]

Z_SHAPE = [
    [(0, 0), (1, 0), (1, 1), (2, 1)],
]

# Farben der Spielsteine
COLORS = {
    'I': (0, 255, 255),  # Cyan
    'J': (0, 0, 255),    # Blau
    'L': (255, 165, 0),  # Orange
    'O': (255, 255, 0),  # Gelb
    'S': (0, 255, 0),    # Grün
    'T': (128, 0, 128),  # Lila
    'Z': (255, 0, 0),    # Rot
}

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

class GameBoard:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = [[0] * width for _ in range(height)] # Erstelle ein leeres Spielfeld

    def clear(self):
        self.grid = [[0] * self.width for _ in range(self.height)]

    def print(self):
        for row in self.grid:
            print(row)

def main():
    pygame.init()

    # KONSTANTEN
    WINDOW_WIDTH = 500
    WINDOW_HEIGHT = 500

    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)

    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Tetris")

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()