#!/usr/bin/env python
from text import Text
from font import Font
from layout import Layout

txt = Text('Hello Cruel\n World!')
print(txt)
fnt = Font()
txt.sanitize(fnt.alphabet)
print(txt)

lyt = Layout(fnt, txt)
print(lyt.bounding_box)
