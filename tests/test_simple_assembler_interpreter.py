import codewars_test as test  # https://github.com/codewars/python-test-framework

import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))  # add parent directory to system path (to import test objects from ../solution/)

from solution.kyu_5.simple_assembler_interpreter import simple_assembler


code = '''\
mov a 5
inc a
dec a
dec a
jnz a -1
inc a'''
test.assert_equals(simple_assembler(code.splitlines()), {'a': 1})

code = '''\
mov c 12
mov b 0
mov a 200
dec a
inc b
jnz a -2
dec c
mov a b
jnz c -5
jnz 0 1
mov c a'''
test.assert_equals(simple_assembler(code.splitlines()), {'a': 409600, 'c': 409600, 'b': 409600})
