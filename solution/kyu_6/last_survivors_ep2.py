"""
Last Survivors Ep.2
https://www.codewars.com/kata/60a1aac7d5a5fc0046c89651
"""
"""
Substitute two equal letters by the next letter of the alphabet (two letters convert to one):

"aa" => "b", "bb" => "c", .. "zz" => "a".

The equal letters do not have to be adjacent.
Repeat this operation until there are no possible substitutions left.
Return a string.

Example:

let str = "zzzab"
    str = "azab"
    str = "bzb"
    str = "cz"
return "cz"

Notes

    The order of letters in the result is not important.
    The letters "zz" transform into "a".
    There will only be lowercase letters.

If you like this kata, check out another one: Last Survivor Ep.3 https://www.codewars.com/kata/60a2d7f50eee95000d34f414
"""


def last_survivors(string: str) -> str:
    string = list(string)
    i = 0  # index of current letter in string
    while i < len(string) - 1:
        try:  # search for first duplicate of the current letter in the remainder of the string
            duplicate_index = string[i+1:].index(string[i]) + i + 1  # '+ i + 1' to compensate start index of the slice
        except ValueError:  # # no duplicate found
            i += 1  # current letter is unique - skip to the next letter
        else:  # duplicate found
            del string[duplicate_index]  # delete duplicate
            string[i] = 'a' if string[i] == 'z' else chr(ord(string[i])+1)  # shift current letter alphabetically, a->b ... z->a
            i = 0  # iterate whole string again because current letter changed, and it might become a duplicate for previously processed letters
    return ''.join(string)  # return remained unique letters
