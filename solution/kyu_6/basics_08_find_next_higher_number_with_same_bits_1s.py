"""
Basics 08: Find next higher number with same Bits (1's)
https://www.codewars.com/kata/56bdd0aec5dc03d7780010a5
"""
"""
Your task is to find the next higher number (int) with same '1'- Bits.

I.e. as much 1 bits as before and output next higher than input. Input is always an int in between 1 and 1<<30 (inclusive). No bad cases or special tricks...
Some easy examples:

Input: 129  => Output: 130 (10000001 => 10000010)
Input: 127 => Output: 191 (01111111 => 10111111)
Input: 1 => Output: 2 (01 => 10)
Input: 323423 => Output: 323439 (1001110111101011111 => 1001110111101101111)

First some static tests, later on many random tests too;-)!
Hope you have fun! :-)
"""


def next_higher(value: int) -> int:
    value = f"0{value:b}"  # add leading zero, convert value to string of '0' and '1' bits
    index = value.rfind('01')  # find lowest '01'
    value = value[:index] + '10' + ''.join(sorted(value[index+2:]))  # leave higher bits intact. swap found '01' to '10' (so the final number is guaranteed to increase). sort all '1's of lower part bits into lowest possible positions (to get closest higher number)
    return int(value, base=2)  # convert bits string to int and return

