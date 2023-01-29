import codewars_test as test  # https://github.com/codewars/python-test-framework
import add_parent_folder_to_sys_path
from solution.kyu_6.character_with_longest_consecutive_repetition import longest_repetition


test.describe("Example Tests")

tests = [
    # [input, expected],
    ["aaaabbcccc", ('a', 4)],
    ["bbbaaabaaaa", ('a', 4)],
    ["cbdeuuu900", ('u', 3)],
    ["abbbbb", ('b', 5)],
    ["aabb", ('a', 2)],
    ["ba", ('b', 1)],
    ["", ('', 0)],
]

for inp, exp in tests:
    test.assert_equals(longest_repetition(inp), exp)
