#!/usr/bin/env python
from text import Text
from font import Font
from layout import Layout
from affine_finder import AffineFinder

txt = Text('Peter')
print(txt)
fnt = Font()
txt.sanitize(fnt.alphabet)
print(txt)

lyt = Layout(fnt, txt)

finder = AffineFinder(lyt.bounding_box)

for xform in finder.find_xforms(lyt.geometry):
    print(xform)

