"""Parser for .react files"""

class Parser(super):

    def get_model(self, f):
        """Returns a model for a given input file

        f: input .react file name
        """
        reaction_file = open(f, "r")
        for line in reaction_file:
            if line.startswith("#"):
                continue
            elif line.startswith("["):
                section_title = line
            elif section_title == "[Iterations]":
                int(line.strip())







