"""
Backspaces in string
https://www.codewars.com/kata/5727bb0fe81185ae62000ae3
"""
"""
Assume "#" is like a backspace in string. This means that string "a#bc#d" actually is "bd"

Your task is to process a string with "#" symbols.
Examples

"abc#d##c"      ==>  "ac"
"abc##d######"  ==>  ""
"#######"       ==>  ""
""              ==>  ""
"""

import re


def clean_string(string: str) -> str:
    """Treat '#' as backspace, i.e. transform 'a#bc#d' to 'bd'"""
    while '#' in string:
        string = string.lstrip('#')  # remove leading '#'
        string = re.sub('[^#]#', '', string)  # remove 'x#' s from the string, where x is any non-# character
    return string
