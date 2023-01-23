"""
Shortest Knight Path (Infinite Chessboard)
https://www.codewars.com/kata/62287e1766b26a0024b9e806
"""
"""
I hope you enjoy this kata, and if you want, there's a more challenging version(with obstacles) https://www.codewars.com/kata/58e6d83e19af2cb8840000b5 .

Task
Given two positions on an infinite chessboard, find the shortest path for a knight moving from one to the other.

Input
Two arguments start and end represent the start and end positions of the knight's path respectively.

Output
A list/array contains all the positions of the shortest path.

Examples
knight_path((1, -1), (1, -1)) #[(1, -1)]
knight_path((0, 0), (1, 1)) #[(0, 0), (2, -1), (1, 1)]
knight_path((0, 0), (1, 2)) #[(0, 0), (1, 2)]
knight_path((0, 0), (1, 3)) #[(0, 0), (-1, 2), (1, 3)]
knight_path((1, -3), (3, 2)) #[(1, -3), (2, -1), (1, 1), (3, 2)]
knight_path((-5, -7), (8, 7)) #[(-5, -7), (-4, -5), (-2, -4), (-1, -2), (1, -1), (2, 1), (4, 2), (5, 4), (7, 5), (8, 7)]

Note
    The start position may duplicate the end position.
    There are no obstacles on the chessboard, so the knight can go anywhere.
    There may be multiple shortest paths, you only need to return one of them.
    Find the right algorithm and pay attention to the performance.
    Returned path should be a list and nonempty(obviously).
    All positions should be a tuple of two ints.

Tests
    410 fixed tests, including 6 example tests, 400 mini tests and 4 big tests.
    100 small random tests, shortest path length in [90,100).
    50 medium random tests, shortest path length in [9 000,10 000).
    20 big random tests, shortest path length in [90 000,100 000).
    One Last Test, shortest path length in [499 900,500 000).
"""


knight_vectors = ((-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1))  # all possible moves (-2, 1) = "2 cells up & 1 cell right" etc.

add_coords = lambda c1, c2: (c1[0] + c2[0], c1[1] + c2[1])  # add two 2d coordinates
sub_coords = lambda c1, c2: (c1[0] - c2[0], c1[1] - c2[1])  # subtract two 2d coordinates
dist_coords = lambda c1, c2: ((c1[1] - c2[1]) ** 2 + (c1[0] - c2[0]) ** 2) ** 0.5  # distance between two 2d coordinates

def knight_path(position: tuple[int, int], destination: tuple[int, int]) -> list[tuple[int, int]]:
    path = [position]  # first step equals start position
    while position != destination:  # while destination not reached

        delta_yx = sub_coords(destination, position)  # current y,x delta to destination
        if abs(delta_yx[0]) > 4 or abs(delta_yx[1]) > 4:  # destination is further than 4 cells on any axis - use fast algorythm which approaches destination by shortest path
            v_dir = -1 if delta_yx[0] < 0 else 1  # go left or right?
            h_dir = -1 if delta_yx[1] < 0 else 1  # go up or down?
            v_coef, h_coef = (2, 1) if abs(delta_yx[0]) > abs(delta_yx[1]) else (1, 2)  # which axis to travel longer?
            vector = (v_dir * v_coef, h_dir * h_coef)  # (y, x) increment for the next move, (-2, 1) = "2 cells up & 1 cell right" etc.
            position = add_coords(position, vector)  # calculate new position

        else:  # destination within 4 cells, direct route is not always the shortest one, use more precise algorythm
            possible_moves = [add_coords(position, vect) for vect in knight_vectors]  # get all possible positions to move to ...
            possible_distances = [round(dist_coords(position, destination), 3) for position in possible_moves]  # ... and their respective distances to destination

            possible_dict = {dist: move for dist, move in zip(possible_distances, possible_moves)}  # create dict where keys for moves are the distances to destination if that move is made
            for dist in (0, 2.236, 3.162, min(possible_dict.keys())):  # pick move by best distance to destination (see scheme below): 0 = reach; 2.236 = one step to go; 3.162 = two steps to go; min() = just move towards destination, it's guaranteed, that one of the (0, 2.236, 3.162) options will be available on the next step
                position = possible_dict.setdefault(dist, None)
                if position: break  # distance found in dictionary, break cycle

        path.append(position)

    return path

# . . . . . . . . .
# . . . 2 . 2 . . .
# . . . 1 . 1 . . .
# . 2 1 . . . 1 2 .
# . . . . 0 . . . .
# . 2 1 . . . 1 2 .
# . . . 1 . 1 . . .
# . . . 2 . 2 . . .
# . . . . . . . . .

# area for which second algorythm is used
# 0 - destination (distance = 0)
# 1 - one step to destination (distance ~ 2.236)
# 2 - two steps to destination (distance ~ 3.162)
