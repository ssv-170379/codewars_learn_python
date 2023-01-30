import codewars_test as test  # https://github.com/codewars/python-test-framework
import add_parent_folder_to_sys_path
from solution.kyu_7.coloured_triangles import triangle

test.assert_equals(triangle('GB'), 'R')
test.assert_equals(triangle('RRR'), 'R')
test.assert_equals(triangle('RGBG'), 'B')
test.assert_equals(triangle('RBRGBRB'), 'G')
test.assert_equals(triangle('RBRGBRBGGRRRBGBBBGG'), 'G')
test.assert_equals(triangle('B'), 'B')
