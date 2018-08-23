#!/usr/bin/env python
import numpy as np

def find_xform(before, after):
    """
    Before is a 2x3 matrix of 3
    column vectors in the preimage

    After is a 2x3 matrix of 3 column
    vectors in the image.

    This returns A and b that satisfies

    A * before + b = after
    """
    NUM_VECTORS = 3
    NUM_DIMS = 2

    # Transpose the before matrix and
    # add a 1s column so we can solve for A and B.
    biased = np.zeros((NUM_VECTORS, NUM_VECTORS))
    biased[:, :NUM_DIMS] = before.T
    biased[:, -1] = 1

    # Solve for a 3x2 matrix of the form
    # [A.T]
    # [b.T]
    coeffs = np.linalg.solve(biased, after.T)

    # Return A and b, transposing them back the way they should be
    A = coeffs[:NUM_DIMS, :].T
    b = coeffs[-1, :].T
    return A, b

# Test this out
big = np.array([
    [10, 10, 26],
    [5, 21, 21]
])

left = np.array([
    [10, 2, 10],
    [5, 13, 21]
])

right = np.array([
    [26, 18, 10],
    [21, 13, 21]
])

A1, b1 = find_xform(big, left)
print 'A_left', A1
print 'b_left', b1

A2, b2 = find_xform(big, right)
print 'A_right', A2
print 'b_right', b2
