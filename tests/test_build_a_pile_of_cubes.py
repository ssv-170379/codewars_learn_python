import codewars_test as test  # https://github.com/codewars/python-test-framework

import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))  # add parent directory to system path (to import test objects from ../solution/)

from solution.kyu_6.build_a_pile_of_cubes import find_nb


test.assert_equals(find_nb(4183059834009), 2022)
test.assert_equals(find_nb(24723578342962), -1)
test.assert_equals(find_nb(135440716410000), 4824)
test.assert_equals(find_nb(40539911473216), 3568)
test.assert_equals(find_nb(26825883955641), 3218)
