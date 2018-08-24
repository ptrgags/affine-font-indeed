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

    @property
    def corner(self):
        """
        Compute the bottom-left corner of the bounding box as a 
        2x1 column array
        """
        half_w = self.width / 2.0
        half_h = self.height / 2.0
        return numpy.array([
            [-half_w],
            [-half_h]
        ]) 

    @property
    def geometry(self):
        """
        Compute the geometry of each letter in "world space".
        This is a generator of Numpy arrays
        """
        # These quantities do not change in the loop
        corner = self.corner
        x_spacing = self.CHAR_WIDTH + self.X_SPACE
        y_spacing = self.CHAR_HEIGHT + self.Y_SPACE

        for i, j, letter in self.text:
            # Compute the offset for this letter relative to the
            # corner of the bounding box
            x_offset = j * x_spacing
            y_offset = i * y_spacing
            offset_vector = numpy.array([
                [x_offset],
                [y_offset]
            ])
                
            # Now we know where the corner of the letter is in world
            # space
            letter_corner = corner + offset_vector

            # Now, go through each of the letter strokes and translate the 
            # geometry
            for stroke in self.font[letter]:
                yield letter_corner + stroke 
            
