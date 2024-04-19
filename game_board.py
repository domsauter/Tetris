class GameBoard:
    def __init__(self, width, height):
        """Initialisiert das Spielfeld"""
        self.width = width
        self.height = height
        self.grid = [[0] * width for _ in range(height)] # Erstelle ein leeres Spielfeld

    def clear(self):
        """Leert dsd Spielfeld"""
        self.grid = [[0] * self.width for _ in range(self.height)]

    def __str__(self):
        """Gibt eine formatierte Zeichenfolge des Spielfelds zurück."""
        board_str = ""
        for row in self.grid:
            row_str = ""
            for cell in row:
                if cell == 0:
                    row_str += " "
                else:
                    row_str += "X"
            board_str += row_str + "\n"
        return board_str