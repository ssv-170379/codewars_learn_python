import codewars_test as test  # https://github.com/codewars/python-test-framework
import add_parent_folder_to_sys_path
from solution.kyu_2.insane_coloured_triangles import triangle


def _test(cases):
    for _in, _out in cases:
        test.assert_equals(triangle(_in), _out)


test.describe('Insane Coloured Triangles')
basic_cases = [
    ['B', 'B'],
    ['GB', 'R'],
    ['RRR', 'R'],
    ['RGBG', 'B'],
    ['RBRGBRB', 'G'],
    ['RBRGBRBGGRRRBGBBBGG', 'G']
]
test.it('Basic Tests')
_test(basic_cases)
