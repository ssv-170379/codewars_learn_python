"""
Dots and Boxes Validator
https://www.codewars.com/kata/5d81d8571c6411001a40ba66
"""
"""
Dots and Boxes (https://en.wikipedia.org/wiki/Dots_and_Boxes) is a game typically played by two players. It starts with an empty square grid of equally-spaced dots. Two players take turns adding a single horizontal or vertical line between two unjoined adjacent dots. A player who completes the fourth side of a 1 x 1 box earns one point and takes another turn. The game ends when no more lines can be placed.

Your task is to return the scores of the two players of a finished game.
Input

Your function will receive an array/tuple of integer pairs, each representing a link between two dots. Dots are denoted by a sequence of integers that increases left to right and top to bottom, like shown below.

for a 3 x 3 square

0  1  2

3  4  5

6  7  8

Output

Your function should return an array/tuple consisting of two non-negative integers representing the scores of both players.
Test Example
https://i.imgur.com/kwS3rDy.png

moves = ((0,1),(7,8),(1,2),(6,7),(0,3),(8,5),(3,4),(4,1),(4,5),(2,5),(7,4),(3,6))
dots_and_boxes(moves) # should return (3,1)

Additional Details

    All inputs will be valid
    n x n board size range: 3 <= n <= 12
    Full Test Suite: 10 fixed tests and 100 random tests
    Use Python 3+ for the Python translation
    For JavaScript, module and require are disabled

If you enjoyed this kata, be sure to check out my other katas (https://www.codewars.com/users/docgunthrop/authored)
"""


def dots_and_boxes(moves: tuple[tuple[int, int]], players=2) -> tuple[int]:
    # describe all possible quads within the grid
    dots_count = max(dot_index for edge in moves for dot_index in edge) + 1  # total dots in grid = maximum dot index + 1
    grid_size = int(dots_count ** .5)  # height (and width) of the square grid
    quads = []  # init list for describing every possible quad for a given grid
    for row in range(grid_size - 1):  # dot index of rows (omit lowest)
        for column in range(grid_size - 1):  # dot index of columns (omit rightest)
            corner = row * grid_size + column  # upper-left corners of each possible quad of the grid
            quads.append([(corner, corner + 1), (corner + 1, corner + grid_size + 1), (corner + grid_size, corner + grid_size + 1), (corner, corner + grid_size)])  # describe quad edges: top, right, bottom, left - each is a pair of dot indexes

    # init game state
    scores = [0] * players  # score for each player: [0, 0] for 2 players etc
    active_player = 0  # index of player who will make next move

    for move in moves:  # game loop
        edge = tuple(sorted(move))  # sort vertex indexes of edge to match edges of quad descriptions
        score = 0  # score for current move
        for quad in quads:  # iterate all quads
            if edge in quad:  # if edge belongs to a certain quad
                quad.remove(edge)  # remove edge from quad description
                if not quad:  # removed last edge = quad claimed by active player
                    score += 1  # count score
        scores[active_player] += score  # update score for active player
        if not score:  # if no score earned during current move - set next player active
            active_player = (active_player + 1) % players  # cyclically iterate players, e.g. for 3 players: 0 -> 1 -> 2 -> 0 -> 1 ...

    return tuple(scores)  # return result
