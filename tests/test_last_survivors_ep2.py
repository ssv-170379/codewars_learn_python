import codewars_test as test  # https://github.com/codewars/python-test-framework

import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))  # add parent directory to system path (to import test objects from ../solution/)

from solution.kyu_6.last_survivors_ep2 import last_survivors


def is_valid(v):
    if not isinstance(v, str):
        test.fail(f"expected a string but got {v}")
    return v


def fix(s):
    return ''.join(sorted(list(s)))


@test.describe("Sample Tests")
def sample():
    @test.it("Given abaa")
    def _():
        user_result = is_valid(last_survivors('abaa'))
        test.assert_equals(fix(user_result), 'ac')

    @test.it("Given zzab")
    def _():
        user_result = is_valid(last_survivors('zzab'))
        test.assert_equals(fix(user_result), 'c')


@test.describe("Zero Length")
def zero_length():
    @test.it("Given ''")
    def _():
        user_result = is_valid(last_survivors(''))
        test.assert_equals(fix(user_result), '')


@test.describe("New Edge")
def new_edge():
    @test.it("Given xsdlafqpcmjytoikojsecamgdkehrqqgfknlhoudqygkbxftivfbpxhxtqgpkvsrfflpgrlhkbfnyftwkdebwfidmpauoteahyh")
    def _():
        user_result = is_valid(last_survivors('xsdlafqpcmjytoikojsecamgdkehrqqgfknlhoudqygkbxftivfbpxhxtqgpkvsrfflpgrlhkbfnyftwkdebwfidmpauoteahyh'))
        test.assert_equals(fix(user_result), 'acdeghlmnqrvyz')
