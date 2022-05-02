import codewars_test as test  # https://github.com/codewars/python-test-framework

import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))  # add parent directory to system path (to import test objects from ../solution/)

from solution.kyu_7.categorize_new_member import openOrSenior


test.assert_equals(openOrSenior([[45, 12], [55, 21], [19, -2], [104, 20]]), ['Open', 'Senior', 'Open', 'Senior'])
test.assert_equals(openOrSenior([[16, 23], [73, 1], [56, 20], [1, -1]]), ['Open', 'Open', 'Senior', 'Open'])