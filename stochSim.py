#!/usr/bin/env python
"""Main function"""

from Parser import Parser
import sys

p = Parser()
print sys.argv
model = p.get_model(sys.argv[1])
model.iterate()
