import codewars_test as test  # https://github.com/codewars/python-test-framework
import add_parent_folder_to_sys_path
from solution.kyu_8.welcome import greet


test.describe("Basic tests")
test.assert_equals(greet('english'), 'Welcome')
test.assert_equals(greet('dutch'), 'Welkom')
test.assert_equals(greet('IP_ADDRESS_INVALID'), 'Welcome')
test.assert_equals(greet(''), 'Welcome')
test.assert_equals(greet(2), 'Welcome')
