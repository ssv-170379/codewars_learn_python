"""
Snail Sort
https://www.codewars.com/kata/521c2db8ddc89b9b7a0000c1
"""
"""
Snail Sort

Given an n x n array, return the array elements arranged from outermost elements to the middle element, traveling clockwise.

array = [[1,2,3],
         [4,5,6],
         [7,8,9]]
snail(array) #=> [1,2,3,6,9,8,7,4,5]

For better understanding, please follow the numbers of the next array consecutively:

array = [[1,2,3],
         [8,9,4],
         [7,6,5]]
snail(array) #=> [1,2,3,4,5,6,7,8,9]

This image will illustrate things more clearly: http://www.haan.lu/files/2513/8347/2456/snail.png

NOTE: The idea is not sort the elements from the lowest value to the highest; the idea is to traverse the 2-d array in a clockwise snailshell pattern.

NOTE 2: The 0x0 (empty matrix) is represented as en empty array inside an array [[]].
"""


def vectors_generator():
    while True:  # infinitely
        for vector in ((0, 1), (1, 0), (0, -1), (-1, 0)):  # cycle through directions - y,x increment for: right, down, left, up
            yield vector


def snail(array: list[list[int]]) -> list[int]:
    sampled_values = []  # sampled values
    sampled_path = []  # sampled cells coords
    coords = (0, 0)  # coords of starting cell to sample
    vectors = vectors_generator()  # initialize direction vectors generator
    vect = next(vectors)  # starting direction (right)

    while len(sampled_path) < len(array) * len(array[0]):  # while not all cells are sampled

        if coords not in sampled_path \
                and -1 < coords[0] < len(array) \
                and -1 < coords[1] < len(array[0]):  # if cell was not sampled earlier and it's coordinates are within array dimensions
            sampled_values.append(array[coords[0]][coords[1]])  # sample value
            sampled_path.append(coords)  # store sampled coordinates

        else:  # cell is already sampled or has invalid coordinates
            vect = next(vectors)  # change direction vector

        coords = (sampled_path[-1][0] + vect[0], sampled_path[-1][1] + vect[1])  # calculate next cell to sample based on the last sampled cell and direction.

    return sampled_values  # all cells are sampled, return sorted values
