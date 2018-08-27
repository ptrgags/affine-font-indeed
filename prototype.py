#!/usr/bin/env python
from text import Text
from font import Font
from layout import Layout
from affine_finder import AffineFinder
from flame_writer import FlameWriter

txt = Text('Peter')
print(txt)
fnt = Font()
txt.sanitize(fnt.alphabet)
print(txt)

lyt = Layout(fnt, txt)

finder = AffineFinder(lyt.bounding_box)

xforms = finder.find_xforms(lyt.geometry)

writer = FlameWriter()
writer.write('output/test.flame', 'Peter', xforms)
