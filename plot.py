import sys
import csv
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

if len(sys.argv) !=2:
	raise ValueError("This program needs 1 argument: input file (.csv)")


header = []
data = []

with open(sys.argv[1], 'r') as inFile:
    reader = csv.reader(inFile)
    header = next(inFile).split(',')
    for i in range(len(header)):
    	data.append([])

    for line in reader:
    	for i, element in enumerate(line):
    		element = float(element.strip())
        	data[i].append(element)

ax = plt.axes()
for i in range(1, len(data)):
	ax.plot(data[0], data[i], "-", label=header[i].strip())
# fig = plt.figure()
# ax = plt.axes(projection = '3d')
# ax.plot(x, y, time, '-b')
plt.legend()
plt.show()
