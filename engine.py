class ChessBoard:
    def __init__(self):
        """

        """
        self.chess_board = [
            ["wh_rook", "wh_knight", "wh_bishop", "wh_queen", "wh_king", "wh_bishop", "wh_knight", "wh_rook"], 
            ["wh_pawn", "wh_pawn", "wh_pawn", "wh_pawn", "wh_pawn", "wh_pawn", "wh_pawn", "wh_pawn"],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            ["blk_rook", "blk_knight", "blk_bishop", "blk_queen", "blk_king", "blk_bishop", "blk_knight", "blk_rook"],
            ["blk_pawn", "blk_pawn", "blk_pawn", "blk_pawn", "blk_pawn", "blk_pawn", "blk_pawn", "blk_pawn"],
            ]
        self.wh_to_move = True
        self.move_log = []

class Move:

    def __init__(self, curr_position, destination, board):
        self.curr_row = curr_position[0]
        self.curr_col = curr_position[1]
        self.dest_row = destination[0]
        self.dest_col = destination[1]
        self.piece_moved = board[self.curr_row][self.curr_col]
        self.piece_captured = board[self.dest_row][self.dest_col]




# class Knight:
#
# class Rook:
#
# class Bishop:
#
# class Queen:
#
# class King:
#
# class Pawn:
#
# class Character:
#
#     curr_pos
#
#     def move(self):
#         if isValid(self.curr_pos, dest):
#             curr_pos = dest
#
#     def isValid(self, curr_pos, dest):
#
#         temp.make_move(self, end)
#         if check(temp):
#             return False
#         else:
#             return isValidMove
#
#     def isValidMove(self):
#
#
