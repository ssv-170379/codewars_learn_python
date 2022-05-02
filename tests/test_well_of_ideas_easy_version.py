import codewars_test as test  # https://github.com/codewars/python-test-framework

import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))  # add parent directory to system path (to import test objects from ../solution/)

from solution.kyu_8.well_of_ideas_easy_version import well


@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(well(['bad', 'bad', 'bad']), 'Fail!')
        test.assert_equals(well(['good', 'bad', 'bad', 'bad', 'bad']), 'Publish!')
        test.assert_equals(well(['good', 'bad', 'bad', 'bad', 'bad', 'good', 'bad', 'bad', 'good']), 'I smell a series!')
