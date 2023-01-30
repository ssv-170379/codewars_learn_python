import codewars_test as test  # https://github.com/codewars/python-test-framework
import add_parent_folder_to_sys_path
from solution.kyu_8.beginner_series_2_clock import past


@test.describe("Fixed Tests")
def basic_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(past(0, 1, 1), 61000)
        test.assert_equals(past(1, 1, 1), 3661000)
        test.assert_equals(past(0, 0, 0), 0)
        test.assert_equals(past(1, 0, 1), 3601000)
        test.assert_equals(past(1, 0, 0), 3600000)
