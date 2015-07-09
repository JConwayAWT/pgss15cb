"""
This file gives a class that defines an arbitrary reagent
"""

class Reagent(object):

    def __init__(self, count, name):
        """Initializes Reagent class

        count:     number of Reagent components
        abb_name:  abbreviated reagent name
        """

        self.count = count
        self.name = name