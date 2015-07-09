from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plot1

wolfFile = open("W.dat", "r")
RabbitFile = open("R.dat", "r")

wolves = []
rabbits = []
times = []

for line in open("W.dat", "r"):
    countStart = False
    adder = ""
    for c in line:
        if countStart:
            adder += c
        elif c == " ":
            countStart = True
    wolves.append(adder)

for line in open("R.dat", "r"):
    countStart = False
    adder = ""
    for c in line:
        if countStart:
            adder += c
        elif c == " ":
            countStart = True
    rabbits.append(adder)

for line in open("R.dat", "r"):
    addNum = ""
    for c in line:
        if c == " ":
            break
        else:
            addNum += c
    times.append(float(addNum) * 20)

plot1.scatter(wolves, rabbits, c=times)
plot1.ylim((0, 7000))
plot1.xlim((0, 7000))
plot1.show()