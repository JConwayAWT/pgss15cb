


#updated version, using better data structure


import os
from lottka_volterra_sim import *

class Result():
    def __init__(self, result = False, name = None, description = None, status = None):
        self.result = result
        self.name = name
        self.description = description
        self.status = status

    def run_test( self, test_function ):
        self.result = test_function()
        if self.result.result == True:
            print self.result.name
            print "PASS / "
        else:
            print self.result.name
            print self.result.description
            print self.result.status

def check_for_negatives(list_molecule_numbers, result_object):
    counter = 0
    for number in list_molecule_numbers:
        if number < 0:
            result_object.result = False
            result_object.status = "FAIL: Test failed at iteration {} in output {}.".format(counter, list_molecule_numbers) 
        else:
            result_object.result = True
            result_object.status = "PASS / "
        counter = counter + 1
    return result_object

def neg_output():
    result = Result()
    result.name = "Negative Output"
    result.description = "Checks to see if the output has negative numbers. If they are negative, the output will describe where."
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

    result = check_for_negatives(list_molecule_numbersR, result)
    if result.result == False:
        return result

    result = check_for_negatives(list_molecule_numbersW, result)

    if result.result == False:
        return result
    else:
        result.result = True
        result.status = "PASS / "

    return result


r = Result()
r.run_test( neg_output )

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
