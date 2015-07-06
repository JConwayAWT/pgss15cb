"""
This file gives a class that defines a reaction object
"""

class Reaction(super):

    def __init__(self, state_ref, react_form_data, k):
        """Initializes reaction class

        state_ref:       reference to state
        react_form_data: list of tuples that describes how to increment or
                         decrement each molecule count
        k:               reaction rate
        """
        self.state_ref = state_ref
        self.react_form_data = react_form_data

    def propensity_update(self):

        raise NotImplementedError

    def reaction_update(self):

        raise NotImplementedError

