"""Main function"""

from Parser import Parser

p = Parser()
model = p.get_model("./InputFileFormat.react")
model.iterate()