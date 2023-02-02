import codewars_test as test  # https://github.com/codewars/python-test-framework
import add_parent_folder_to_sys_path
from solution.kyu_4.decode_the_morse_code_advanced import decode_morse, decode_bits


def test_and_print(got, expected):
    if got == expected:
        test.expect(True)
    else:
        print("<pre style='display:inline'>Got '%s', expected '%s'</pre>" % (got, expected))
        test.expect(False)


test.describe("Example from description")
test_and_print(decode_morse(decode_bits('1100110011001100000011000000111111001100111111001111110000000000000011001111110011111100111111000000110011001111110000001111110011001100000011')), 'HEY JUDE')

test.describe("Your own tests")
# Add more tests here
