import codewars_test as test  # https://github.com/codewars/python-test-framework
import add_parent_folder_to_sys_path
from solution.kyu_7.search_for_letters import change


@test.describe('Example Tests')
def example_tests():
    test.assert_equals(change("a **&  bZ"), "11000000000000000000000001")
    test.assert_equals(change('Abc e  $$  z'), "11101000000000000000000001")
    test.assert_equals(change("!!a$%&RgTT"), "10000010000000000101000000")
    test.assert_equals(change(""), "00000000000000000000000000", "empty string should return 26 '0'")
    test.assert_equals(change("abcdefghijklmnopqrstuvwxyz"), "11111111111111111111111111")
    test.assert_equals(change("aaaaaaaaaaa"), "10000000000000000000000000")
    test.assert_equals(change("&%&%/$%$%$%$%GYtf67fg34678hgfdyd"), "00010111000000000001000010")
