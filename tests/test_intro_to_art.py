import codewars_test as test  # https://github.com/codewars/python-test-framework
import add_parent_folder_to_sys_path
from solution.kyu_6.intro_to_art import get_w


@test.describe('Sample tests')
def sample_tests():
    test.assert_equals(get_w(-5), [])
    test.assert_equals(get_w(1), [])
    test.assert_equals(get_w(3), [
        '*   *   *',
        ' * * * * ',
        '  *   *  '])
    test.assert_equals(get_w(7), [
        '*           *           *',
        ' *         * *         * ',
        '  *       *   *       *  ',
        '   *     *     *     *   ',
        '    *   *       *   *    ',
        '     * *         * *     ',
        '      *           *      '])
