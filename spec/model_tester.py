#model_tester.py
#updated version of model tests

import os

test_path = os.getcwd()

def get_models(directory):
    model_list=[]
    for file in os.listdir(directory):
        path_name = "%s/Tests/%s"%(test_path, file)
        if os.path.isdir(path_name):
            model_list.append(file)
    return model_list

def clear_outputs(directory,models):
    pass

def non_negative(iterations,model):
    print '***running the non negative test on the %s model'%(model)
    test_successful = True
    for i in range(iterations):
        output_file_name = "%s/Tests/%s/out%s.csv"%(test_path,model,str(i))
        output_file = open(output_file_name,"r")
        column_headers = output_file.readline().rstrip().split(',')[1:]

        output_data = output_file.readlines()

        output_list=[]
        for line in output_data:
            new_line = [x.strip() for x in line.split(',')][1:]
            output_list.append(new_line)
        if i == 6:
            output_list.append([5,5,5,5,-5])

        for k in range(len(output_list)):
            for j in range(len(column_headers)):
                if int(output_list[k][j]) < 0:
                    test_successful = False
                    badLine = k
                    #Instead of breaking, return where the error ocurred
                    return "Test failed. Negative number found in out%s.csv at line %i" %(str(i),badLine)
    #return "Test succeeded", since this step will only be reached if the test succeeded
    return "Test succeeded."

def average(iterations,model):
    print '***running the average test on the %s model'%(model)


'''class Result():
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
            print self.result.status'''

models = get_models("%s/Tests"%(test_path))
#clear_outputs(test_path,models)

for model in models:
    description = open("%s/Tests/%s/%s.txt"%(test_path,model,model),"r")
    iterations = int(description.readline())
    print "testing on the %s model now"%(model)
    input_file = "%s/Tests/%s/%s.react"%(test_path,model,model)

    #runs the engine a specified number of times and writes output files to test folders
    for i in range(iterations):
        output_file = "out%s.csv"%(str(i))

        #will change with new engine model
        string = "./stochSim.py %s %s"%(input_file,output_file)
        print "--running simulation number %s for the %s model (%s)"%(str(i),model,output_file)
        os.system(string)
        os.rename("%s/%s"%(test_path,output_file),"%s/Tests/%s/%s"%(test_path,model,output_file))

    print
    functions = list(description)
    for line in range(len(functions)):
        functions[line] = functions[line].rstrip()
        exec("print %s(%s,'%s')"%(functions[line],str(iterations),str(model)))

    print
    print
print "done!"

