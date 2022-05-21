"""
Ordered Count of Characters
https://www.codewars.com/kata/57a6633153ba33189e000074
"""
"""
Count the number of occurrences of each character and return it as a list of tuples in order of appearance. For empty output return an empty list.

Example:

ordered_count("abracadabra") == [('a', 5), ('b', 2), ('r', 2), ('c', 1), ('d', 1)]
"""

from collections import Counter


def ordered_count(inp: str) -> list[tuple[str, int]]:
    # count_dict = dict.fromkeys(inp, 0)  # hack to get unique values and maintain order. convert iterable to dict keys and set initial counter to zero
    # for ch in inp:
    #     count_dict[ch] += 1
    count_dict = Counter(inp)  # 'aaabcc' -> {'a': 3, 'b': 1, 'c': 2}, see https://docs.python.org/3/library/collections.html#counter-objects
    return list(count_dict.items())
