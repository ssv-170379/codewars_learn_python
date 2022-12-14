"""
Range Extraction
https://www.codewars.com/kata/51ba717bb08c1cd60f00002f
"""
"""
A format for expressing an ordered list of integers is to use a comma separated list of either

    individual integers
    or a range of integers denoted by the starting integer separated from the end integer in the range by a dash, '-'. The range includes all integers in the interval including both endpoints. It is not considered a range unless it spans at least 3 numbers. For example "12,13,15-17"

Complete the solution so that it takes a list of integers in increasing order and returns a correctly formatted string in the range format.

Example:

solution([-10, -9, -8, -6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20])
# returns "-10--8,-6,-3-1,3-5,7-11,14,15,17-20"
"""


def solution(args: list[int]) -> str:
    result = []
    seq = [args[0]]

    for x in args[1:] + [None]:  # [None] is the stopper to process last element of the sequence inside the loop
        if x == seq[-1] + 1:  # sequence continues
            seq.append(x)
        else:  # sequence break, flatten current sequence and add to the result
            if len(seq) < 3:  # current sequence shorter than 3 elements
                result.extend(map(str, seq))  # add str of individual elements of the sequence to the result
            else:
                result.append(f'{seq[0]}-{seq[-1]}')  # add str of the sequence formatted as 'start-end' to the result
            seq = [x]  # start new sequence

    return ','.join(result)  # return combined string
