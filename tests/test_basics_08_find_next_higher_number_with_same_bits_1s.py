import codewars_test as test  # https://github.com/codewars/python-test-framework
import add_parent_folder_to_sys_path
from solution.kyu_6.basics_08_find_next_higher_number_with_same_bits_1s import next_higher


test.assert_equals(next_higher(128), 256)
test.assert_equals(next_higher(1), 2)
test.assert_equals(next_higher(1022), 1279)
test.assert_equals(next_higher(127), 191)
test.assert_equals(next_higher(1253343), 1253359)
