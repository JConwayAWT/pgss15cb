import itertools

numbs = [-13, 20, 14, 53, 31, -22, 42, 60, -15, 7, 65, -34, 26]
goal = int(raw_input("What is the target value? "))
done = False


def findsubsets(list, size):
    return set(itertools.combinations(list, size))

for n in range(1, len(numbs)+1):
    if done:
        break
    for l in (findsubsets(numbs, n)):
        if sum(l) == goal:
            print (l)
            print ("There is a solution!")
            done = True
            break

    if (n == len(numbs)) and done is False:
        print ("No Solution!")