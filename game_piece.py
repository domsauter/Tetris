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