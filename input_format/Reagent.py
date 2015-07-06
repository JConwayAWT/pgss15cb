"""
This file gives a class that defines an arbitrary reagent
"""

class Reagent(super):

    def __init__(self, count, full_name, abb_name):
        """Initializes Reagent class

        count:     number of Reagent components
        full_name: full name of reagent
        abb_name:  abbreviated reagent name
        """

        self.count = count
        self.full_name = full_name
        self.abb_name = abb_name