from __future__ import print_function
import yaml

def read_font():
    """
    Read in the yaml font
    """
    with open('font.yaml', 'r') as f:
        return yaml.load(f)

def display_geom(font, letter):
    strokes = font[letter]
    print(letter)
    for i, stroke in enumerate(strokes):
        print('Stroke {}:'.format(i))
        print(stroke)

font = read_font()
display_geom(font, 'A')
display_geom(font, 'B')
display_geom(font, 'D')

