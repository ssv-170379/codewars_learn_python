import codewars_test as test  # https://github.com/codewars/python-test-framework
import add_parent_folder_to_sys_path
from solution.kyu_6.backspaces_in_string import clean_string

test.assert_equals(clean_string('abc#d##c'), "ac")
test.assert_equals(clean_string('abc####d##c#'), "")
test.assert_equals(clean_string("#######"), "")
test.assert_equals(clean_string(""), "")
