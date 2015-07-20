#checks to make sure input is not negative

from lottka_volterra_sim import *

R0_status = False
W0_status = False
maxTime_status = False


def check_input:
    if R0 < 0:
        return R0_status
    else:
        R0_status = True
        
    if W0 < 0:
        return W0_status
    else:
        W0_status = True
        
    if maxTime < 0:
        return maxTime_status
    else:
        maxTime_status = True
        
if R0_status == True and W0_status == True and maxTime_status == True:
    print "PASS: No inputs are less than 0."
else:
    if R0_status == False:
        print "FAILED: R0 is less than zero."
    if W0_status == False:
        print "FAILED: W0 is less than zero."
    if maxTime_status == False:
        print "FAILED: maxTime is less than zero."


