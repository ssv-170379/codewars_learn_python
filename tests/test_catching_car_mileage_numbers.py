import codewars_test as test  # https://github.com/codewars/python-test-framework

import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))  # add parent directory to system path (to import test objects from ../solution/)

from solution.kyu_4.catching_car_mileage_numbers import is_interesting


@test.describe("Car Mileage numbers")
def desc1():
    @test.it("Sample tests")
    def it1():
        tests = [
            {'n': 3, 'interesting': [1337, 256], 'expected': 0},
            {'n': 1336, 'interesting': [1337, 256], 'expected': 1},
            {'n': 1337, 'interesting': [1337, 256], 'expected': 2},
            {'n': 11208, 'interesting': [1337, 256], 'expected': 0},
            {'n': 11209, 'interesting': [1337, 256], 'expected': 1},
            {'n': 11211, 'interesting': [1337, 256], 'expected': 2},
        ]
        for t in tests:
            test.assert_equals(is_interesting(t['n'], t['interesting']), t['expected'])
