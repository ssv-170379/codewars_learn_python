import codewars_test as test  # https://github.com/codewars/python-test-framework

import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))  # add parent directory to system path (to import test objects from ../solution/)

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
