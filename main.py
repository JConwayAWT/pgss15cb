#!/usr/bin/env python
"""Main function"""

from Parser import Parser

p = Parser()
model = p.get_model("./lv.react")
model.iterate()