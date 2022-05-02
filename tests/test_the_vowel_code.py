import codewars_test as test  # https://github.com/codewars/python-test-framework

import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))  # add parent directory to system path (to import test objects from ../solution/)

from solution.kyu_6.the_vowel_code import encode, decode


test.assert_equals(encode('hello'), 'h2ll4')
test.assert_equals(encode('How are you today?'), 'H4w 1r2 y45 t4d1y?')
test.assert_equals(encode('This is an encoding test.'), 'Th3s 3s 1n 2nc4d3ng t2st.')
test.assert_equals(decode('h2ll4'), 'hello')
