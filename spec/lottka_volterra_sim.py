#!/usr/bin/env python3 

"""
This file contains a Gillespie simulator for the Lottka-Volterra
reaction

         F + R -> 2R   [k1]
         R + W -> 2W   [k2]
         W     -> nil  [k3]

"""

# import pythons random number generator
# NOTE: for production code you need to make sure to have
# a very good random number generator.
import random as rng
import math

###############################################################
# initial conditions and variables
###############################################################

R0 = 100   # initial number of rabbits
W0 = 200  # initial number of wolfs

# initial rates
k1 = 10           
k2 = 0.01        
k3 = 10

# parameters
maxTime = 0.01   # maximum simulation time



#############################################################
# helper functions
#############################################################

def react1_updater(molCount):
    """
    This function updates the molecule count should reaction
    number 1 happen. Input parameter is the list of current
    molecule counts and we return the new molecule counts.
    """

    molCount[0] += 1      # update R

    return molCount



def react2_updater(molCount):
    """
    This function updates the molecule count should reaction
    number 2 happen. Input parameter is the list of current
    molecule counts and we return the new molecule counts.
    """

    molCount[0] -= 1      # update R
    molCount[1] += 1      # update W

    return molCount


def react3_updater(molCount):
    """
    This function updates the molecule count should reaction
    number 3 happen. Input parameter is the list of current
    molecule counts and we return the new molecule counts.
    """

    molCount[1] -= 1      # update W

    return molCount



def compute_propensities(molCount,rates):
    """
    This function returns the reaction propensities according
    to the current molecule counts (step 1 on 2345 in Gillespie's
    paper 1977 paper). Since we have two reactions we return
    a list with two values. Per definition of the propensities
    in Gillespie's paper we return the propensity k1*A*B for 
    reaction 1 and k2*C for reaction 2 where A, B, and C are the 
    instantaneous molecule counts and k1, k2 the reaction rates.
    """
    
    return (rates[0]*molCount[0], 
            rates[1]*molCount[0]*molCount[1],
            rates[2]*molCount[1])    
    


def open_output_files():
    """
    This function opens the output files and returns file
    handles to each.
    """

    outfile_A = open("R.dat","w")
    outfile_B = open("W.dat","w")

    return [outfile_A, outfile_B]



def write_data_to_output(fileHandles, time, data):
    """
    This function writes a (time, data) pair to the
    corresponding output file. We write concentrations
    not molecule counts.
    """

    for i in range(0,len(fileHandles)):
        fileHandles[i].write("%5.4e  %8.7f\n" %(time, data[i]))
    


def close_output_files(fileHandles):
    """
    This function closes all output files.
    """

    for i in range(0,len(fileHandles)):
        fileHandles[i].close()
    

    
    

################################################################
# start of main simulation
################################################################

def main():

    # initialize time, random number generator,
    # initial molecule counts, and molecule count update
    # functions
    rng.seed(124213)
    time       = 0.0
    iteration  = 0                               # iteration count
    outputFreq = 1000                            # output frequency
    molCounts  = [R0,W0]
    rates      = [k1,k2,k3]           # need to convert 
    updaters   = [react1_updater,react2_updater,react3_updater]

    # open output files
    fileHandles = open_output_files() 
    
    # we simulate until we hit our maximum simulation time
    while time < maxTime:
        print "Time = {}".format(time)
        print "mtme = {}".format(maxTime)
        
        # compute the propensities a_i for each reaction
        # and the sum a_0
        a_i = compute_propensities(molCounts, rates)
        a_0 = sum(a_i)

        # pick a random number, compute the time increment
        # and update t (equation 21a in Gillespie's paper)
        rand_1 = rng.random()
        tau    = 1.0/a_0 * math.log(1/rand_1)
        time  += tau

        # find the reaction to execute (equation 21b in
        # Gillespie's paper). We need a second random number
        # here. We don't really need the while loop here since
        # we only have two possible reactions but we do it anyway
        # to keep it more general. 
        rand_2    = rng.random()
        threshold = a_0 * rand_2
        
        summation = 0
        count     = 0
        while threshold > summation:
            summation += a_i[count]
            count += 1
            
        # update molecule counts by calling the proper updater
        # function. Note, arrays in python are zero index based
        # hence we need count-1 to access the proper updater.
        molCounts = updaters[count-1](molCounts)

        # dump data every outputFreq iteration
        # we also print a short progess message 
        if (iteration % outputFreq) == 0:
            write_data_to_output(fileHandles, time, molCounts)
            #print("iteration %d   time %5.4g" % (iteration, time))   

        iteration += 1    

    
    # cleanup
    close_output_files(fileHandles)



# entry point for execution
if __name__ == "__main__":
    main()
