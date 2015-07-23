"""Defines model class"""
import random as rng
import math
import csv

class Model(object):

    def __init__(self, states, reactions, output_freq, output_reagents,
                                            num_iterations, seed, outFile):
        self.states          = states  # [('A',Reagent object of A)]
        # for state in states:
        #   self.states.append(state)
        #  
        self.reactions       = reactions  # list of Reaction objects
        self.output_freq     = output_freq  # How often to log to file
        self.num_iterations  = num_iterations  # Number of iterations to run
        self.output_reagents = output_reagents  # Which reagents to output
        self.seed = seed
        self.outFile = outFile  #string of output file (ants.csv)

    def iterate(self):


        seed = self.seed
        while seed < 0:
            seed = rng.random() * 10000
        rng.seed(seed)
        
        time = 0
        reagentNames = []
        reagents = []

        #Reagents is an imported list of objects that contain reagent values
        for names, reags in self.states.iteritems():
            reagentNames.append(names)
            reagents.append(reags)

        fileWriter = csv.writer(self.outFile, delimiter = ',')
        fileWriter.writerow(["Time"] + reagentNames)
        
        i = 0
        while time < self.num_iterations:

            i += 1
            sumProp = 0
            propen = []
            for p in self.reactions:
                propen.append(p.get_propensity())
                sumProp += p.get_propensity()
            #print time, propen
            r1 = rng.random()
            while r1 == 0:
                r1 = rng.random()
            r2 = rng.random()
            if sumProp != 0:
                #print sumProp
                t = (1/(float(sumProp)))*math.log(1/(r1*1.0)) * 1
            else:
                print "Invalid propensity sum."
                break
            time += t
            subsum = 0
            nextReact = -1
            thres = r2 * sumProp
            for n in propen:
                nextReact+=1
                subsum += n
                if subsum >= thres:
                    break
            if i % 100 == 0:
                self.reactions[nextReact].reaction_update()
                reagentCounts = []
                for r in reagents:
                    reagentCounts.append(r.count)
                fileWriter.writerow([time] + reagentCounts)
            if i % 1000 == 0:
                print [time] + reagentCounts
