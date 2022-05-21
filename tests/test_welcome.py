import codewars_test as test  # https://github.com/codewars/python-test-framework

import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))  # add parent directory to system path (to import test objects from ../solution/)

from solution.kyu_8.welcome import greet


test.describe("Basic tests")
test.assert_equals(greet('english'), 'Welcome')
test.assert_equals(greet('dutch'), 'Welkom')
test.assert_equals(greet('IP_ADDRESS_INVALID'), 'Welcome')
test.assert_equals(greet(''), 'Welcome')
test.assert_equals(greet(2), 'Welcome')
