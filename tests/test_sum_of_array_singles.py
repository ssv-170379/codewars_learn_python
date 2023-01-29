import codewars_test as test  # https://github.com/codewars/python-test-framework
import add_parent_folder_to_sys_path
from solution.kyu_7.sum_of_array_singles import repeats

test.it("Basic tests")
test.assert_equals(repeats([4, 5, 7, 5, 4, 8]), 15)
test.assert_equals(repeats([9, 10, 19, 13, 19, 13]), 19)
test.assert_equals(repeats([16, 0, 11, 4, 8, 16, 0, 11]), 12)
test.assert_equals(repeats([5, 17, 18, 11, 13, 18, 11, 13]), 22)
test.assert_equals(repeats([5, 10, 19, 13, 10, 13]), 24)
