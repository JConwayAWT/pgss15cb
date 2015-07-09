"""Parser for .react files"""

from Reagent import Reagent
from Reaction import Reaction
from Model import Model
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
            line = line.strip()
            if line.startswith("#") or line == "":
                continue
            elif line.startswith("["):
                section_title = line
            elif '[Iterations' in section_title:
                num_iterations = int(float(line.strip()))
                if num_iterations <= 0:
                    raise ValueError("Number of iterations must be positive")
            elif '[Reagents' in section_title:
                name, count = line.split(':')
                name = name.strip()
                count = int(count.strip())
                if count < 0:
                    raise ValueError("Count can't be negative: " + line)
                states[name] = Reagent(count, name)
            elif '[Reactions' in section_title:
                reaction, k = line.split("|")
                k = float(k)
                reactant_str, product_str = reaction.split("->")
                reactants = []
                products = []
                if "$" not in reactant_str:
                    for reactant in reactant_str.split("+"):
                        reactant = reactant.strip()
                        for i in xrange(len(reactant)):
                            if reactant[i].isalpha():
                                coeff = -int(float(reactant[:i]))
                                if coeff >= 0: 
                                    raise ValueError(
                                        "Coefficient must be positive: " + \
                                                                        line)
                                reactants.append((reactant[i:], coeff))
                                break
                if "$" not in product_str:
                    for product in product_str.split("+"):
                        product = product.strip()
                        for i in xrange(len(product)):
                            if product[i].isalpha():
                                coeff = int(float(product[:i]))
                                if coeff <= 0:
                                    raise ValueError(
                                        "Coefficient must be positive: " + \
                                                                        line)
                                products.append((product[i:], coeff))
                                break
                reactions.append(Reaction(states, reactants + products, k))
            elif '[Output_Reagents' in section_title:
                output_reagents.append(line.strip())
            elif "[Output_Frequency" in section_title:
                output_frequency = int(float(line.strip()))
                if output_frequency <= 0:
                    raise ValueError("Output frequency must be positive")
            elif "[RNG_Seed" in section_title:
                rng_seed = line.strip()
                if rng_seed != "r":
                    rng_seed = int(float(rng_seed))
                    if rng_seed <= 0:
                        raise ValueError("RNG seed must be positive")
                else:
                    rng_seed = -1
            else:
                raise ValueError("Bad File")
        for reaction in reactions:
            for reagent in reaction.react_form_data:
                if reagent[0] not in states:
                    raise ValueError("Reagent {} not defined".format(
                                     reagent[0]))
        for reagent in output_reagents:
            if reagent not in states:
               raise ValueError("Ouput Reagent {} not defined".format(
                                reagent))
        return Model(states, reactions, output_frequency, output_reagents,
                                            num_iterations, rng_seed)



if __name__ == "__main__":
    print Parser().get_model("./InputFileFormat.react")









