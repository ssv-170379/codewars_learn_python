"""
Stacked Balls - 3D (triangle base)
https://www.codewars.com/kata/5bbad1082ce5333f8b000006
"""
"""
Background

I have stacked some cannon balls in a triangle-based pyramid.

Like this,
https://i.imgur.com/ut4ejG1.png [cannon balls triangle base]
Kata Task

Given the number of layers of my stack, what is the total height?

Return the height as multiple of the ball diameter.
Example

The image above shows a stack of 3 layers.
Notes

    layers >= 0
    approximate answers (within 0.001) are good enough

"""


def stack_height_3d(layers: int, diameter: int = 1) -> float:
    if not layers:
        return 0
    else:
        # Bottom layer height = diameter. Every upper layer height = sqrt(diameter * 2/3)
        return diameter + ((diameter * 2/3) ** 0.5) * (layers - 1)  # https://mathforums.com/threads/height-of-stack-of-spheres-in-pyramid-fashion.19971/post-82714
