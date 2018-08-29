#!/usr/bin/env python
from __future__ import print_function
import argparse

from text import Text
from font import Font
from layout import Layout
from affine_finder import AffineFinder
from flame_writer import FlameWriter

def make_flame(args):
    """
    Use the arguments to make a flame file.
    """
    # Select the padding style
    pad_char = '█' if args.block_padding else ' '
    text = Text(args.text, pad_char)

    # Read in the font and sanitize the text
    font = Font()
    text.sanitize(font.alphabet)

    print("Making fractal for the following text:")
    print(text)


    # The Layout handles positioning each character of text
    layout = Layout(font, text)

    # The AffineFinder calculates the necessary transformation
    # matricies. It returns XForm Objects
    finder = AffineFinder(layout.bounding_box)
    xforms = list(finder.find_xforms(layout.geometry))

    print("This fractal will use {} xforms + final xform".format(len(xforms)))


    writer = FlameWriter()
    writer.write(args.fname, args.flame_name, xforms)

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'fname',
        help='Enter a path to the output .flame file')
    parser.add_argument(
        'flame_name',
        help='Enter a name for the flame inside the pack')
    parser.add_argument(
        'text',
        help='Text of the fractal. Use $\'these\\nstrings\' for multiline')
    parser.add_argument(
        '-b', 
        '--block-padding', 
        action='store_true', 
        help='Use █ to fill out the empty spaces in the text')
    return parser.parse_args()

if __name__ == '__main__':
    args = get_args()
    make_flame(args)
