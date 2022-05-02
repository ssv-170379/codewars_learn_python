import codewars_test as test  # https://github.com/codewars/python-test-framework

import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))  # add parent directory to system path (to import test objects from ../solution/)

from solution.kyu_7.disemvowel_trolls import disemvowel


test.assert_equals(disemvowel("This website is for losers LOL!"),
                   "Ths wbst s fr lsrs LL!")
