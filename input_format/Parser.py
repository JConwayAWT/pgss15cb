"""Parser for .react files"""

from Reagent import Reagent
from Reaction import Reaction
class Parser(object):

    def get_model(self, f):
        """Returns a model for a given input file

        f: input .react file name
        """
        states = {}
        reactions = []
        reaction_file = open(f, "r")
        output_reagents = []
        for line in reaction_file:
            if line.strip() == "":
                continue
            elif line.startswith("#"):
                continue
            elif line.startswith("["):
                section_title = line
            elif '[Iterations' in section_title:
                num_iterations = int(line.strip())
            elif '[Reagents' in section_title:
                name, count = line.split(':')
                name = name.strip()
                count = int(count.strip())
                states[name] = Reagent(count, name)
            elif '[Reactions' in section_title:
                reaction, k = line.split("|")
                k = float(k)
                reactant_str, product_str = reaction.split("->")
                if "$" not in reactant_str:
                    reactants = [reactant.strip()
                                 for reactant in reactant_str.split("+")]
                    reactants = [(reactant[1:], -int(reactant[0]))
                                  for reactant in reactants]
                else:
                    reactants = []
                if "$" not in product_str:
                    products = [product.strip()
                                for product in product_str.split("+")]
                    products = [(product[1:], int(product[0]))
                                  for product in products]
                else:
                    products = []
                reactions.append(Reaction(states, reactants + products, k))
            elif '[Output_Reagents' in section_title:
                output_reagents.append(line.strip())
            elif "[Output_Frequency" in section_title:
                output_frequency = int(line.strip())
            else:
                raise ValueError("Bad File")
        print states
        print states['Berries'].__dict__
        print reactions[0].__dict__
        print reactions[1].__dict__
        print num_iterations
        print output_frequency
        print output_reagents



if __name__ == "__main__":
    print Parser().get_model("./InputFileFormat.react")









