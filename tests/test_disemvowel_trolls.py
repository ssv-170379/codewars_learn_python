import codewars_test as test  # https://github.com/codewars/python-test-framework
import add_parent_folder_to_sys_path
from solution.kyu_7.disemvowel_trolls import disemvowel


test.assert_equals(disemvowel("This website is for losers LOL!"),
                   "Ths wbst s fr lsrs LL!")
