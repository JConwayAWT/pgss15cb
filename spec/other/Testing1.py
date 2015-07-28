


#see testing2 file



import os
from lottka_volterra_sim import *

def openFile():
    # try:
        main()
        LottkaVolterraR = open('R.dat', 'r')
        lv_textR = LottkaVolterraR.read()
        LottkaVolterraW = open('W.dat', 'r')
        lv_textW = LottkaVolterraW.read()

        list_molecule_numbersR = []
        list_molecule_numbersW = []

        for line in LottkaVolterraR:
            all_dataR = line.split()
            molecule_numbersR = float(all_data[-1])
            list_molecule_numbersR.append(molecule_numbersR)
        
        for line in LottkaVolterraW:
            all_dataW = line.split()
            molecule_numbersW = float(all_dataW[-1])
            list_molecule_numbersW.append(molecule_numbersW)

        def check_for_negatives(list_molecule_numbers):
            counter = 0
            for number in list_molecule_numbersR:
                if number < 0:
            		print "Test failed at iteration {} in output {}.".format(counter, list_molecule_numbers)
                counter = counter + 1

        print check_for_negatives(list_molecule_numbersR)
        print check_for_negatives(list_molecule_numbersW)


openFile()

#         list_molecule_numbers = []

#         for line in LottkaVolterra:
#             all_data = line.split()
#             molecule_numbers = float(all_data[-1])
#             list_molecule_numbers.append(molecule_numbers)

#         def check_for_negatives(list_molecule_numbers):
#             counter = 0
#             for number in list_molecule_numbers:
#                 if number < 0:
#             print "Test failed at {}".format(counter)
#                 counter = counter + 1

#         print check_for_negatives(list_molecule_numbers)

#     except Exception, e:
#         print str(e)

# def closeFile():
#     try:
#         os.system('TASKKILL /F /IM python.exe')
#     except Exception, e:
#         print str(e)

# LottkaVolterra = open('C:\Users\Me\Desktop\R.dat', 'r')
# print LottkaVolterra

# list_molecule_numbers = []

# for line in LottkaVolterra:
#     all_data = line.split()
#     molecule_numbers = float(all_data[-1])
#     list_molecule_numbers.append(molecule_numbers)

# def check_for_negatives(list_molecule_numbers):
#     counter = 0
#     for number in list_molecule_numbers:
#         if number < 0:
#             print "Test failed at {}".format(counter)
#         counter = counter + 1

# print check_for_negatives(list_molecule_numbers)
