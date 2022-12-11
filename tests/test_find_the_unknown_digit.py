import codewars_test as test  # https://github.com/codewars/python-test-framework

import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))  # add parent directory to system path (to import test objects from ../solution/)

from solution.kyu_4.find_the_unknown_digit import solve_runes


test.assert_equals(solve_runes("1+1=?"), 2, "Answer for expression '1+1=?' ")
test.assert_equals(solve_runes("123*45?=5?088"), 6, "Answer for expression '123*45?=5?088' ")
test.assert_equals(solve_runes("-5?*-1=5?"), 0, "Answer for expression '-5?*-1=5?' ")
test.assert_equals(solve_runes("19--45=5?"), -1, "Answer for expression '19--45=5?' ")
test.assert_equals(solve_runes("??*??=302?"), 5, "Answer for expression '??*??=302?' ")
test.assert_equals(solve_runes("?*11=??"), 2, "Answer for expression '?*11=??' ")
test.assert_equals(solve_runes("??*1=??"), 2, "Answer for expression '??*11=??' ")
test.assert_equals(solve_runes("123?45*?=?"), 0, "Answer for expression '123?45*?=?' ")
test.assert_equals(solve_runes("7216+22824=3??4?"), 0, "Answer for expression '7216+22824=3??4?' ")
