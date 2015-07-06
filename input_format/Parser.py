"""Parser for .react files"""

class Parser(super):

    def get_model(self, f):
        """Returns a model for a given input file

        f: input .react file name
        """
        data = [states, reactions, output_freq, num_iterations]
        states = {}
        reactions = []
        reaction_file = open(f, "r")
        for line in reaction_file:
            if line.startswith("#"):
                continue
            elif line.startswith("["):
                section_title = line
            elif 'Iterations' in section_title:
                num_iterations = int(line.strip())
            elif 'Reagents' in section_title:
                name, count = line.split(':')










