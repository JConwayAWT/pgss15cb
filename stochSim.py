#!/usr/bin/env python
"""Main function"""

from Parser import Parser
import sys
if len(sys.argv)!=3:
	raise ValueError("This program needs 2 arguments: input file (.react) and output file (.csv)")

p = Parser()
model = p.get_model(sys.argv[1], sys.argv[2])
model.iterate()
