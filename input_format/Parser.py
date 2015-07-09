"""Parser for .react files"""

from Reagent import Reagent

class Parser(super):

    def get_model(self, f):
        """Returns a model for a given input file

        f: input .react file name
        """
        states = {}
        data = [states, reactions, output_freq, num_iterations, output_reagents]
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
                name = name.strip()
                count = int(count.strip())
                states[name] = Reagent(count, name)
            elif 'Reactions' in section_title:
                reaction, k = line.split("|")
                reactant_str, product_str = reaction.split("->")


            elif 'Output_Reagents' in section_title:
                output_reagents.append(line.strip())
            elif "Output_Frequency" in section_title:
                output_frequency = int(line.strip())
            else:
                raise ValueError("Bad File")













