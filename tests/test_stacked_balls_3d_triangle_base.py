import codewars_test as test  # https://github.com/codewars/python-test-framework
import add_parent_folder_to_sys_path
from solution.kyu_7.stacked_balls_3d_triangle_base import stack_height_3d


@test.describe('Example Tests')
def example_tests():
    @test.it('Example Test Cases')
    def example_test_cases():
        test.assert_equals(stack_height_3d(1), 1)
        test.assert_approx_equals(stack_height_3d(2), 1.816, margin=0.001, message=None)
