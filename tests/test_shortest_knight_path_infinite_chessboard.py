import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))  # add parent directory to system path (to import test objects from ../solution/)

from solution.kyu_4.shortest_knight_path_infinite_chessboard import knight_path


import datetime
def timer(func):
    def wrapper(*args, **kwargs):
        t1 = datetime.datetime.now()
        result = func(*args, **kwargs)
        t2 = datetime.datetime.now() - t1
        print(t2.total_seconds())
        return result
    return wrapper

for start, end, expected_len in (
        ((0, 0), (-4, -4), 5),
        ((1, -1), (1, -1), 1),
        ((0, 0), (1, 1), 3),
        ((0, 0), (1, 2), 2),
        ((0, 0), (1, 3), 3),
        ((1, -3), (3, 2), 4),
        ((-5, -7), (8, 7), 10),
        ((81637, 87565), (-87963, -33866), 97012),
        ((-231421, 552540), (468265, -247682), 499971),
):
    path = timer(knight_path)(start, end)
    assert len(path) == expected_len, f'Wrong path length ({len(path)}). Expected {expected_len}.'