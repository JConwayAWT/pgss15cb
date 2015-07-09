"""Defines model class"""

class Model(super):

    def __init__(self, states, reactions, output_freq, output_reagents,
                                                         num_iterations):
    	self.states 		 = states  # [('A',Reagent object of A)]
    	self.reactions 		 = reactions  # list of Reaction objects
    	self.output_freq 	 = output_freq	# How often to log to file
    	self.num_iterations  = num_iterations  # Number of iterations to run
        self.output_reagents = output_reagents  # Which reagents to output
    	
        raise NotImplementedError

    def iterate():

    	raise NotImplementedError