"""
Character with longest consecutive repetition
https://www.codewars.com/kata/586d6cefbcc21eed7a001155
"""
"""
For a given string s find the character c (or C) with longest consecutive repetition and return:

(c, l)

where l (or L) is the length of the repetition. If there are two or more characters with the same l return the first in order of appearance.

For empty string return:

('', 0)

In JavaScript: If you use Array.sort in your solution, you might experience issues with the random tests as Array.sort is not stable in the Node.js version used by CodeWars. This is not a kata issue.

Happy coding! :)
"""


# import itertools
#
#
# imo this realization is too clever and harder to read than uncommented code below
# def longest_repetition(chars: str) -> tuple[str, int]:
#     groups = itertools.groupby(chars)  # roughly 'aabaaa' -> (('a', 'aa'), ('b', 'b'), ('a', 'aaa')), but packed into iterators, see https://docs.python.org/3/library/itertools.html#itertools.groupby
#     letters_with_count = [(letter, len(list(letter_group))) for letter, letter_group in groups]  # (('a', 'aa'), ('b', 'b'), ('a', 'aaa')) -> [('a', 2), ('b', 1), ('a', 3)]
#     return max(letters_with_count,
#                key=lambda x: x[1], default=('', 0))  # return first tuple with maximum count, or ('', 0) for empty list (in case of empty input string)


def longest_repetition(chars: str) -> tuple[str, int]:
    current = {'char': '', 'count': 0}  # track sequences of letters inside string
    longest = {'char': '', 'count': 0}  # store longest sequence
    for ch in chars:
        if ch == current['char']:  # sequence continues
            current['count'] += 1  # count character
        else:  # sequence ended
            current = {'char': ch, 'count': 1}  # start new sequence from current character
        if current['count'] > longest['count']:  # if current sequence longer than previously registered maximum length
            longest = current.copy()  # update longest sequence
    return longest['char'], longest['count']
