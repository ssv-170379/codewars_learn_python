"""
Find the unknown digit
https://www.codewars.com/kata/546d15cebed2e10334000ed9
"""
"""
To give credit where credit is due: This problem was taken from the ACMICPC-Northwest Regional Programming Contest. Thank you problem writers.

You are helping an archaeologist decipher some runes. He knows that this ancient society used a Base 10 system, and that they never start a number with a leading zero. He's figured out most of the digits as well as a few operators, but he needs your help to figure out the rest.

The professor will give you a simple math expression, of the form

[number][op][number]=[number]

He has converted all of the runes he knows into digits. The only operators he knows are addition (+),subtraction(-), and multiplication (*), so those are the only ones that will appear. Each number will be in the range from -1000000 to 1000000, and will consist of only the digits 0-9, possibly a leading -, and maybe a few ?s. If there are ?s in an expression, they represent a digit rune that the professor doesn't know (never an operator, and never a leading -). All of the ?s in an expression will represent the same digit (0-9), and it won't be one of the other given digits in the expression. No number will begin with a 0 unless the number itself is 0, therefore 00 would not be a valid number.

Given an expression, figure out the value of the rune represented by the question mark. If more than one digit works, give the lowest one. If no digit works, well, that's bad news for the professor - it means that he's got some of his runes wrong. output -1 in that case.

Complete the method to solve the expression to find the value of the unknown rune. The method takes a string as a paramater repressenting the expression and will return an int value representing the unknown rune or -1 if no such rune exists.
"""

import re


def solve_runes(runes: str) -> int:
    runes = re.sub(r'([\d?]+)', r' \1 ', runes)  # add spaces around numbers to make it easier to check for invalid leading '0's

    for digit_candidate in '0123456789':
        if digit_candidate in runes:  # current digit already in runes, so it can't be the unknown one
            continue  # skip digit
        runes_expr = (runes.replace('?', digit_candidate).replace('=', '=='))  # substitute '?' for digit candidate, and '=' for '==' to be able to evaluate expression
        if not re.search(r' 0\d', runes_expr) and eval(runes_expr):  # if no leading '0's present and the expression evaluates correctly
            return int(digit_candidate)  # we found unknown digit, return it

    return -1  # after trying every possible digit the equation can not be solved
