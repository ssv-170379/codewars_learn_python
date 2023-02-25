"""
Tracking pawns
https://www.codewars.com/kata/56b012bbee8829c4ea00002c
"""
"""
A chess board is normally played with 16 pawns and 16 other pieces, for this kata a variant will be played with only the pawns. All other pieces will not be on the board.
For information on how pawns move, refer here http://www.chesscorner.com/tutorial/basic/pawn/pawn.htm

Write a function that can turn a list of pawn moves into a visual representation of the resulting board.
A chess move will be represented by a string,

"c3"

This move represents a pawn moving to c3. If it was white to move, the move would represent a pawn from c2 moving to c3. If it was black to move, a pawn would move from c4 to c3, because black moves in the other direction.
The first move in the list and every other move will be for white's pieces.

The letter represents the column, while the number represents the row of the square where the piece is moving

Captures are represented differently from normal moves:

"bxc3"

represents a pawn on the column represented by 'b' (the second column) capturing a pawn on c3.

For the sake of this kata a chess board will be represented by a list like this one:

[[".",".",".",".",".",".",".","."],
 ["p","p","p","p","p","p","p","p"],
 [".",".",".",".",".",".",".","."],
 [".",".",".",".",".",".",".","."],
 [".",".",".",".",".",".",".","."],
 [".",".",".",".",".",".",".","."],
 ["P","P","P","P","P","P","P","P"],
 [".",".",".",".",".",".",".","."]]

Here is an example of the board with the squares labeled:

[["a8","b8","c8","d8","e8","f8","g8","h8"],
 ["a7","b7","c7","d7","e7","f7","g7","h7"],
 ["a6","b6","c6","d6","e6","f6","g6","h6"],
 ["a5","b5","c5","d5","e5","f5","g5","h5"],
 ["a4","b4","c4","d4","e4","f4","g4","h4"],
 ["a3","b3","c3","d3","e3","f3","g3","h3"],
 ["a2","b2","c2","d2","e2","f2","g2","h2"],
 ["a1","b1","c1","d1","e1","f1","g1","h1"]]

White pawns are represented by capital 'P' while black pawns are lowercase 'p'.

A few examples

If the list/array of moves is: ["c3"]
>>>
[[".",".",".",".",".",".",".","."],
 ["p","p","p","p","p","p","p","p"],
 [".",".",".",".",".",".",".","."],
 [".",".",".",".",".",".",".","."],
 [".",".",".",".",".",".",".","."],
 [".",".","P",".",".",".",".","."],
 ["P","P",".","P","P","P","P","P"],
 [".",".",".",".",".",".",".","."]]

add a few more moves,

If the list/array of moves is: ["d4", "d5", "f3", "c6", "f4"]
>>>
[[".",".",".",".",".",".",".","."],
 ["p","p",".",".","p","p","p","p"],
 [".",".","p",".",".",".",".","."],
 [".",".",".","p",".",".",".","."],
 [".",".",".","P",".","P",".","."],
 [".",".",".",".",".",".",".","."],
 ["P","P","P",".","P",".","P","P"],
 [".",".",".",".",".",".",".","."]]

now to add a capture...

If the list/array of moves is: ["d4", "d5", "f3", "c6", "f4", "c5", "dxc5"]
>>>
[[".",".",".",".",".",".",".","."],
 ["p","p",".",".","p","p","p","p"],
 [".",".",".",".",".",".",".","."],
 [".",".","P","p",".",".",".","."],
 [".",".",".",".",".","P",".","."],
 [".",".",".",".",".",".",".","."],
 ["P","P","P",".","P",".","P","P"],
 [".",".",".",".",".",".",".","."]]

If an invalid move (a move is added that no pawn could perform, a capture where there is no piece, a move to a square where there is already a piece, etc.) is found in the list of moves, return '(move) is invalid'.

If the list/array of moves is: ["e6"]
>>>
"e6 is invalid"

If the list/array of moves is: ["e4", "d5", "exf5"]
>>>
"exf5 is invalid"

The list passed to pawn_move_tracker / PawnMoveTracker.movePawns will always be a list of strings in the form (regex pattern): [a-h][1-8] or [a-h]x[a-h][1-8].

Notes:
    In the case of a capture, the first lowercase letter will always be adjacent to the second in the alphabet, a move like axc5 will never be passed.
    A pawn can move two spaces on its first move
    There are no cases with the 'en-passant' rule.
"""

from abc import ABC, abstractmethod


class ChessPiece(ABC):  # just for consistent hierarchy
    def __init__(self, row, column, colour, symbol):
        self.row = row
        self.column = column
        self.colour = colour
        self.symbol = symbol

    def move(self, row: int, column: int):
        self.row = row
        self.column = column

    @abstractmethod
    def check_can_reach_coords(self, dest_row, dest_column, active_colour):
        pass

    @abstractmethod
    def check_can_take_piece(self, piece_to_take, taker_column, active_colour):
        pass


class Pawn(ChessPiece):
    def __init__(self, row, column, colour):
        super().__init__(row, column, colour, symbol='P' if colour == 'White' else 'p')

    def check_can_reach_coords(self, dest_row: int, dest_column: int, active_colour: str) -> bool:
        """Return boolean whether self can move to coordinates"""
        # Only pawns of active colour can move. Movement occurs only within current column.
        if self.colour != active_colour or self.column != dest_column:
            return False
        if self.colour == 'White':  # whites move upward the board
            return (dest_row == self.row - 1) or (self.row == 6 and dest_row == 4)  # 6-4 - two-cells first move for white pawn
        if self.colour == 'Black':  # # blacks move downward the board
            return (dest_row == self.row + 1) or (self.row == 1 and dest_row == 3)  # 1-3 - two-cells first move for black pawn

    def check_can_take_piece(self, piece_to_take: ChessPiece, taker_column: int, active_colour: str) -> bool:
        """Return boolean whether self can take the piece"""
        # Only active colour piece can take. Only pieces from provided column can take.
        # Only piece of the opposite colour can be taken. Only pieces in adjacent columns can be taken.
        if (self.colour != active_colour) or (self.column != taker_column) or \
                (piece_to_take.colour == active_colour) or abs(self.column - piece_to_take.column) != 1:
            return False
        if self.colour == 'White':
            return piece_to_take.row == self.row - 1  # whites take piece upward the board
        if self.colour == 'Black':
            return piece_to_take.row == self.row + 1  # blacks take piece downward the board


class Board:
    def __init__(self, pieces: list[ChessPiece], size=8):
        self.size = size
        self.pieces = pieces

    def dump_to_list(self) -> list[list[str]]:
        """Return a list representation of the current board state"""
        board_list = [['.'] * self.size for _ in range(self.size)]  # init board filled with '.' symbols
        for p in self.pieces:
            board_list[p.row][p.column] = p.symbol  # place chess pieces
        return board_list

    def get_cell(self, row: int, column: int) -> list[ChessPiece]:
        """Return content of the cell"""
        return [p for p in self.pieces if (p.row == row) and (p.column == column)]

    def get_pieces_able_to_move_to_coords(self, dest_row: int, dest_column: int, active_colour: str) -> list[ChessPiece]:
        return [p for p in self.pieces if p.check_can_reach_coords(dest_row, dest_column, active_colour)]

    def get_pieces_able_to_take_piece(self, piece_to_take: ChessPiece, taker_column: int, active_colour: str) -> list[ChessPiece]:
        return [p for p in self.pieces if p.check_can_take_piece(piece_to_take, taker_column, active_colour)]

    def take_piece(self, taker, taken):
        taker.move(taken.row, taken.column)
        self.pieces.remove(taken)

    def chess_column_to_index(self, chess_column: str) -> int:
        """Convert chess notation column to 0-based index: 'a' -> 0 etc."""
        return ord(chess_column) - ord('a')

    def chess_notation_to_index(self, chess_notation: str) -> tuple[int, int]:
        """Convert chess notation coordinates like 'e2', to 0-based (row, column), where (0,0) is upper-left corner of the board."""
        column, row = tuple(chess_notation)
        row = self.size - int(row)
        column = self.chess_column_to_index(column)
        return row, column


class Game:
    def __init__(self, board: Board):
        self.board = board
        self.active_colour = 'White'  # 'White' | 'Black'
        self.state = 'In progress'  # 'In progress' | 'Finished' | '{move} is invalid'

    def switch_active_colour(self):
        self.active_colour = 'Black' if self.active_colour == 'White' else 'White'

    def make_moves(self, moves):
        for move in moves:  # iterate moves
            try:
                if not 'x' in move:  # move
                    dest_row, dest_column = self.board.chess_notation_to_index(move)  # destination coordinate
                    assert not self.board.get_cell(dest_row, dest_column)  # assert destination is empty
                    piece = self.board.get_pieces_able_to_move_to_coords(dest_row, dest_column, self.active_colour)[0]
                    piece.move(dest_row, dest_column)

                else:  # take
                    taker_column, taken_coords = move.split('x')
                    taker_column = self.board.chess_column_to_index(taker_column)
                    taken_row, taken_column = self.board.chess_notation_to_index(taken_coords)  # coordinates of piece to take
                    piece_to_take = self.board.get_cell(taken_row, taken_column)[0]
                    piece_taker = self.board.get_pieces_able_to_take_piece(piece_to_take, taker_column, self.active_colour)[0]
                    self.board.take_piece(piece_taker, piece_to_take)

                self.switch_active_colour()

            except (IndexError, AssertionError):  # all kinds of errors: no piece to move, no piece to take, move destination is occupied etc
                self.state = f"{move} is invalid"  # invalid move
                return  # exit immediately

        self.state = 'Finished'  # game finished with all the moves were valid


def pawn_move_tracker(moves: list[str]) -> list[list] | str:
    board_size = 8  # init
    pieces = [Pawn(row=1, column=c, colour='Black') for c in range(board_size)] + \
             [Pawn(row=6, column=c, colour='White') for c in range(board_size)]
    board = Board(pieces, board_size)
    game = Game(board)

    game.make_moves(moves)  # play the game
    return game.board.dump_to_list() if game.state == 'Finished' else game.state
