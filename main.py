import sys

import pygame as p
from Chess import engine
from pygame.locals import *

p.init()
WIDTH = HEIGHT = 512
DIMENSION = 8
SQ_SIZE = HEIGHT // DIMENSION
MAX_FPS = 15
IMAGES = {}

"""
white = {Rook: 8, Knight: 7, Bishop: 6, Queen: 5, King: 4, Pawn: 3}
Black = {Rook: 13, Knight: 12, Bishop: 11, Queen: 10, King: 9, Pawn: 2}
"""


def load_images():
    pieces = ["wh_rook", "wh_knight", "wh_bishop", "wh_queen", "wh_king", "wh_pawn",
              "blk_rook", "blk_knight", "blk_bishop", "blk_queen", "blk_king", "blk_pawn"]
    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load("images/" + piece + ".png"), (SQ_SIZE, SQ_SIZE))


def main():
    screen = p.display.set_mode((WIDTH, HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color("white"))
    p.display.set_caption("CHESS")
    board = engine.ChessBoard()
    load_images()
    # print(board.chess_board)
    position_selected = ()
    player_click = []  # consist tuple of clicked locations
    game_active = True
    while game_active:
        for event in p.event.get():
            if event.type == QUIT:
                game_active = False
                p.quit()
                # sys.exit()
            elif event.type == p.MOUSEBUTTONDOWN:
                location = p.mouse.get_pos()
                col = location[0] // SQ_SIZE
                row = location[1] // SQ_SIZE
                if position_selected == (row, col):
                    position_selected = ()
                    player_click = []
                else:
                    position_selected = (row, col)
                    player_click.append(position_selected)
                if len(player_click) == 2:
                    pass

        draw_board_state(screen, board)
        clock.tick(MAX_FPS)
        p.display.flip()


def draw_board_state(screen, board):
    draw_board(screen)
    draw_pieces(screen, board.chess_board)


def draw_board(screen):
    colors = [p.Color("white"), p.Color("gray")]
    for rows in range(DIMENSION):
        for cols in range(DIMENSION):
            color = colors[((rows + cols) % 2)]
            p.draw.rect(screen, color, p.Rect(rows * SQ_SIZE, cols * SQ_SIZE, SQ_SIZE, SQ_SIZE))


def draw_pieces(screen, chess_board):
    for rows in range(DIMENSION):
        for cols in range(DIMENSION):
            piece = chess_board[cols][rows]
            if piece:
                screen.blit(IMAGES[piece], p.Rect(rows * SQ_SIZE, cols * SQ_SIZE, SQ_SIZE, SQ_SIZE))


if __name__ == '__main__':
    main()
