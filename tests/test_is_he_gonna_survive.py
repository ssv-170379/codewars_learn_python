import codewars_test as test  # https://github.com/codewars/python-test-framework

import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))  # add parent directory to system path (to import test objects from ../solution/)

from solution.kyu_8.is_he_gonna_survive import hero


@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(hero(10, 5), True)
        test.assert_equals(hero(7, 4), False)
        test.assert_equals(hero(4, 5), False)
        test.assert_equals(hero(100, 40), True)
        test.assert_equals(hero(1500, 751), False)
        test.assert_equals(hero(0, 1), False)
