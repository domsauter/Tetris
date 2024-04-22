class Colors:
    DARK_BLUE = (37, 40, 80)
    CYAN = (0, 255, 255)
    BLUE = (0, 0, 255)
    ORANGE = (255, 165, 0)
    YELLOW = (255, 255, 0)
    GREEN = (0, 255, 0)
    PURPLE = (128, 0, 128)
    RED = (255, 0, 0)

    @classmethod
    def get_color(cls):
        return [cls.DARK_BLUE, cls.CYAN, cls.BLUE, cls.ORANGE, cls.YELLOW, cls.GREEN, cls.PURPLE, cls.RED]
