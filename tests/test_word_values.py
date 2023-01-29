import codewars_test as test  # https://github.com/codewars/python-test-framework

import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))  # add parent directory to system path (to import test objects from ../solution/)

from solution.kyu_7.word_values import name_value


test.assert_equals(name_value(["abc", "abc", "abc", "abc"]), [6, 12, 18, 24])
test.assert_equals(name_value(["codewars", "abc", "xyz"]), [88, 12, 225])
