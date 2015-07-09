import random as rng
import math
import csv

rng.seed(seed)
propen = []
sumProp = 0
time = 0
reagentNames = []

#Reagents is an imported list of objects that contain reagent values
for r in reagents:
    reagentNames.append(r)

with open("data.csv", "w+") as dataFile:
    fileWriter = csv.writer(dataFile, delimiter = ',')
    fileWriter.writerow(["Time"] + reagentNames)


while time < Model.num_iterations:
    for p in reactions:
        propen.append(p.get_propensity())
        sumProp += p.get_propensity()
    r1 = rng.rand()
    while r1 == 0:
        r1 = rng.rand()
    r2 = rng.rand()
    print "sumPropr"
    print sumProp
    if sumProp != 0:
        t = (1/(sumProp*1.0))*math.log(1/(r1*1.0)) * 10^500
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
    reactions[nextReact].reaction_update()

    with open("data.csv", "w+") as dataFile:
        fileWriter = csv.writer(dataFile, delimiter = ',')
        reagentCounts = []
        for r in reagents:
            reagentCounts.append(r.count)
        fileWriter.writerow([time] + reagentCounts)

