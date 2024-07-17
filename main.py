import pygame
import sys
from pygame.locals import *
from game_board import GameBoard
from game_pieces import *
from random_piece import *

# Initialize pygame and sounds
pygame.init()
pygame.mixer.init()

# Load sounds
try:
    line_clear_sound = pygame.mixer.Sound("sounds/line_clear.mp3")
except pygame.error as e:
    print(f"Error loading sound: {e}")
    line_clear_sound = None

# Constants
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
BOARD_MARGIN_RIGHT = 200
WHITE = (255, 255, 255)
DARK_BLUE = (47, 50, 90)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tetris")

clock = pygame.time.Clock()

# Game setup
game_board = GameBoard()
game_piece = create_random_stone()
next_piece = create_random_stone()
score = 0

game_board.print_board()

# Timer event for piece falling
FALL_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(FALL_EVENT, 1000)

def lock_and_update(game_piece):
    global score, running
    game_board.lock_piece(game_piece)
    cleared_rows = game_board.clear_full_rows()
    print(f"Rows cleared: {cleared_rows}")  # Debugging-Ausgabe
    if cleared_rows > 0:
        if line_clear_sound:
            line_clear_sound.play()
        score += cleared_rows * 100
        print(f"Score updated to: {score}")  # Debugging-Ausgabe
    if game_board.is_game_over():
        running = False

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_LEFT:
                game_piece.move(0, -1, game_board)
            elif event.key == K_RIGHT:
                game_piece.move(0, 1, game_board)
            elif event.key == K_DOWN:
                if not game_piece.move(1, 0, game_board):
                    lock_and_update(game_piece)
                    game_piece = next_piece
                    next_piece = create_random_stone()
            elif event.key == K_UP:
                if not isinstance(game_piece, OShape):
                    game_piece.rotate(game_board)
        elif event.type == FALL_EVENT:
            if not game_piece.move(1, 0, game_board):
                lock_and_update(game_piece)
                game_piece = next_piece
                next_piece = create_random_stone()

    screen.fill(DARK_BLUE)
    game_board.draw_board(screen, score)
    game_piece.draw_piece(screen)
    next_piece.draw_piece(screen, offset_x=game_board.cols * game_board.cell_size + 50, offset_y=100)

    pygame.display.update()

    clock.tick(60)

pygame.quit()
