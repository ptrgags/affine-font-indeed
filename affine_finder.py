import numpy

from xform import XForm

class AffineFinder(object):
    """
    Find affine transforms that map a large triangle
    to one or more smaller triangles. This yields
    XForm objects
    """
    def __init__(self, large_triangle):
        """
        Constructor. Pass in the definition of the large
        triangle that represents the bounding box of the text

        This should be a matrix like this:

        [Ox Xx Yx]
        [Oy Xy Yy]

        For triangle

        Y
        |
        |
        |
        O----X
        """
        self.before = self.prep_before_matrix(large_triangle)

    def find_xforms(self, small_triangles):
        """
        yield an XForm for every after triangle desired
       
        small_triangles should be a sequence
        
        of (triangle, label)

        where triangle is a 2x3 matrix in the same format
        as the one passed in to __init__()

        Label is a brief description of what the triangle represents
        This will usually be something like "A0" for the first stroke
        in letter A

        """
        for tri, label in small_triangles:
            mat = self.find_affine_xform(tri)
            yield XForm(label, mat)

    def find_affine_xform(self, after):
        """
        Find the coefficients
        a, b, c, d, e, f such that

        [a b] * before + [e] = after
        [c d]            [f] 

        This returns the results in the form

        [a c]
        [b d]
        [e f]

        by solving the equation
        [before.T, 1] [a c] = after
                      [b d]
                      [e f]
        """
        return numpy.linalg.solve(self.before, after.T)

    @classmethod
    def prep_before_matrix(cls, before_geom):
        """
        Convert a matrix of column vectors from

        [O_x, X_x, Y_x] (before)
        [O_y, X_y, Y_y]
        
        to

        [O_x O_y 1]
        [X_x X_y 1]  (same as [before.T 1])
        [Y_x Y_y 1]

        This matrix can be used to solve for the affine parameters
        """ 
        NUM_VECTORS = 3
        NUM_DIMS = 2

        # Transpose the before matrix and
        # add a 1s column
        biased = numpy.zeros((NUM_VECTORS, NUM_VECTORS))
        biased[:, :NUM_DIMS] = before_geom.T
        biased[:, -1] = 1

        return biased
