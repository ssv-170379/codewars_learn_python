import codewars_test as test  # https://github.com/codewars/python-test-framework
import add_parent_folder_to_sys_path
from solution.kyu_4.space_invaders_underdog import blast_sequence

test.describe('3 Example Tests')
example_aliens = [
    [[3, 1, 2, -2, 2, 3, 6, -3, 7, 1]],
    [[5, 2, -2, 3, 1, 0, 4, 8, 3, -2, 5], [1, 4, -1, 0, 3, 6, 1, -3, 1, 2, -4]],
    [[4, 1, -7, -5, 1, 6, 3, -2, 1, 0, 2, 6, 5], [2, 0, 3, -4, 0, 2, -1, 5, -8, -3, -2, -5, 1], [1, 2, 0, -6, 4, 7, -2, 4, -4, 2, -5, 0, 4]]]
example_positions = [[6, 4], [10, 2], [15, 6]]
example_solutions = [
    [0, 2, 3, 4, 5, 9, 10, 13, 19, 22],
    [1, 4, 5, 6, 8, 9, 10, 12, 14, 15, 16, 18, 19, 20, 21, 26, 27, 30, 32, 36],
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 14, 15, 17, 18, 19, 21, 22, 23, 25, 27, 30, 31, 32, 35, 36, 38, 40, 43, 45, 56, 58]]

for aliens, pos, sol in zip(example_aliens, example_positions, example_solutions):
    test.assert_equals(blast_sequence(aliens, pos), sol)
