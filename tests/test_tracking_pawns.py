import codewars_test as test  # https://github.com/codewars/python-test-framework
import add_parent_folder_to_sys_path
from solution.kyu_4.tracking_pawns import pawn_move_tracker

test.it("Example tests")

test.assert_equals(pawn_move_tracker(["e3", "d6", "e4", "a6"]), [
    [".", ".", ".", ".", ".", ".", ".", "."],
    [".", "p", "p", ".", "p", "p", "p", "p"],
    ["p", ".", ".", "p", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", "P", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", "."],
    ["P", "P", "P", "P", ".", "P", "P", "P"],
    [".", ".", ".", ".", ".", ".", ".", "."]
])
test.assert_equals(pawn_move_tracker(["e4", "d5", "d3", "dxe4"]), [
    [".", ".", ".", ".", ".", ".", ".", "."],
    ["p", "p", "p", ".", "p", "p", "p", "p"],
    [".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", "p", ".", ".", "."],
    [".", ".", ".", "P", ".", ".", ".", "."],
    ["P", "P", "P", ".", ".", "P", "P", "P"],
    [".", ".", ".", ".", ".", ".", ".", "."]
])
test.assert_equals(pawn_move_tracker(["e4", "d5", "exf5"]), "exf5 is invalid")
