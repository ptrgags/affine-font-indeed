import numpy

class Layout(object):
    """
    The Layout class handles arranging letters
    in world space given a font and a set of desired
    text.
    """
    # The font was based on cells of this size
    CHAR_WIDTH = 3.0
    CHAR_HEIGHT = 5.0
    
    # Space between rows
    X_SPACE = 1.0
    Y_SPACE = 2.0

    def __init__(self, font, text):
        self.font = font
        self.text = text

    @property
    def width(self):
        """Compute the width of the entire layout"""
        N = self.text.cols
        return N * self.CHAR_WIDTH + (N - 1) * self.X_SPACE

    @property
    def height(self):
        """Compute the height of the entire layout"""
        M = self.text.rows
        return M * self.CHAR_HEIGHT + (M - 1) * self.Y_SPACE

    @property
    def bounding_box(self):
        """
        Compute three points of the bounding box
        as a numpy array in the form.

        The bounding box is centered around the origin. Y is upwards

        Y-------+
        |       |
        O-------X

        [O_x, X_x, Y_x]
        [O_y, X_y, Y_y]
        """
        half_w = self.width / 2.0
        half_h = self.height / 2.0

        return numpy.array([
            [-half_w, half_w, -half_w],
            [-half_h, -half_h, half_h]
        ])
