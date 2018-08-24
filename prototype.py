#!/usr/bin/env python
from text import Text
from font import Font

txt = Text('Hello Cruel\n World!')
print(txt)
fnt = Font()
txt.sanitize(fnt.alphabet)
print(txt)
