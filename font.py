from future.utils import iteritems

import numpy
import yaml

class Font(object):
    """
    a Font holds the geometry for every letter and the corresponding
    strokes.
    """
    def __init__(self, fname='font.yaml'):
        """
        Initialize the font from a YAML file
        """
        self.font_data = self.parse_font(fname)

    def __getitem__(self, key):
        """
        Allow subscript access to the underlying font data.
        """
        return self.font_data[key]

    def __len__(self):
        """
        How many letters are in this font?
        """
        return len(self.font_data)

    @property
    def alphabet(self):
        """
        See what symbols are supported in this font file.
        """
        return set(self.font_data.keys())

    @classmethod
    def parse_font(cls, fname):
        """
        Parse the font from a YAML file. 
        This produces a dictionary of the form
        
        letter -> list of strokes

        A "Stroke" is a triangle in object space that 
        defines one of the strokes of the letter.
        Each stroke is a 2x3 matrix that defines the
        origin, and two legs of the triangle. See the following
        diagram for the data format for a single stroke

        Y
        |
        |
        |
        O------X

        [O_x, X_x, Y_x]
        [O_y, X_y, Y_y]

        This method calls Font.process_font() which
        converts these nested lists into NumPy arrays
        for later calculations.
        """
        with open(fname, 'r') as yaml_file:
            raw_font = yaml.load(yaml_file)
            return dict(cls.process_font(raw_font))

    @classmethod
    def process_font(cls, raw_font):
        """
        Go through the font dictionary
        and make the strokes into 
        """
        for letter, strokes in iteritems(raw_font):
            stroke_arrays = [numpy.array(stroke) for stroke in strokes]
            yield letter, stroke_arrays 
