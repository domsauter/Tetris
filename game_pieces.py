from game_piece import GamePiece
from position import Position

class IShape(GamePiece):
    def __init__(self):
        super().__init__(shape = 1)
        self.cells = {
            0: [Position(1, 0), Position(1, 1), Position(1, 2), Position(1, 3)],
            1: [Position(0, 2), Position(1, 2), Position(2, 2), Position(3, 2)],
            2: [Position(3, 0), Position(3, 1), Position(3, 2), Position(3, 3)],
            3: [Position(0, 1), Position(1, 1), Position(2, 1), Position(3, 1)]
        }
        self.move(-1, 3)

class JShape(GamePiece):
    def __init__(self):
        super().__init__(shape=2)
        self.cells = {
            0: [Position(0, 0), Position(1, 0), Position(1, 1), Position(1, 2)],
            1: [Position(0, 1), Position(0, 2), Position(1, 1), Position(2, 1)],
            2: [Position(1, 0), Position(1, 1), Position(1, 2), Position(2, 2)],
            3: [Position(2, 0), Position(2, 1), Position(1, 1), Position(0, 1)]
        }
        self.move(0, 3)

class LShape(GamePiece):
    def __init__(self):
        super().__init__(shape=3)
        self.cells = {
            0: [Position(1, 0), Position(1, 1), Position(1, 2), Position(0, 2)],
            1: [Position(0, 1), Position(1, 1), Position(2, 1), Position(2, 2)],
            2: [Position(1, 0), Position(2, 0), Position(1, 1), Position(1, 2)],
            3: [Position(0, 0), Position(0, 1), Position(1, 1), Position(2, 1)]
        }
        self.move(0,3)

class OShape(GamePiece):
    def __init__(self):
        super().__init__(shape=4)
        self.cells = {
            0: [Position(1, 1), Position(2, 1), Position(1, 2), Position(2, 2)]
        }
        self.move(-1, 3)

class SShape(GamePiece):
    def __init__(self):
        super().__init__(shape=5)
        self.cells = {
            0: [Position(1, 0), Position(1, 1), Position(0, 1), Position(0, 2)],
            1: [Position(0, 1), Position(1, 1), Position(1, 2), Position(2, 2)],
            2: [Position(1, 1), Position(1, 2), Position(2, 1), Position(2, 0)],
            3: [Position(0, 0), Position(1, 0), Position(1, 1), Position(2, 1)]
        }
        self.move(0, 3)

class TShape(GamePiece):
    def __init__(self):
        super().__init__(shape=6)
        self.cells = {
            0: [Position(1, 0), Position(1, 1), Position(1, 2), Position(2, 1)],
            1: [Position(0, 1), Position(1, 1), Position(2, 1), Position(1, 0)],
            2: [Position(1, 0), Position(1, 1), Position(1, 2), Position(0, 1)],
            3: [Position(0, 1), Position(1, 1), Position(2, 1), Position(1, 2)]
        }
        self.move(-1, 3)

class ZShape(GamePiece):
    def __init__(self):
        super().__init__(shape=7)
        self.cells = {
            0: [Position(0, 0), Position(0, 1), Position(1, 1), Position(1, 2)],
            1: [Position(0, 2), Position(1, 2), Position(1, 1), Position(2, 1)],
            2: [Position(1, 0), Position(1, 1), Position(2, 1), Position(2, 2)],
            3: [Position(0, 1), Position(1, 1), Position(1, 0), Position(2, 0)]
        }
        self.move(0, 3)