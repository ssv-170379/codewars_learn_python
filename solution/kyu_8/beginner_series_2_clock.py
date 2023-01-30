"""
Beginner Series #2 Clock
https://www.codewars.com/kata/55f9bca8ecaa9eac7100004a
"""
"""
Clock shows h hours, m minutes and s seconds after midnight.

Your task is to write a function which returns the time since midnight in milliseconds.
Example:

h = 0
m = 1
s = 1

result = 61000

Input constraints:

    0 <= h <= 23
    0 <= m <= 59
    0 <= s <= 59
"""

SECONDS_IN_MINUTE = 60
SECONDS_IN_HOUR = 3600
MILLISECONDS_IN_SECOND = 1000


def past(hours: int, minutes: int, seconds: int) -> int:
    """Convert input time to milliseconds"""
    return ((hours * SECONDS_IN_HOUR) + (minutes * SECONDS_IN_MINUTE) + seconds) * MILLISECONDS_IN_SECOND
