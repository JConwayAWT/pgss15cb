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

    def get_propensity(self):

        raise NotImplementedError

    def reaction_update(self):
        """Performs update given internal react_form_data

        Edits state
        """
        for reagent, delta in self.react_form_data:
            self.state_ref[reagent] += delta
