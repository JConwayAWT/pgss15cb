#model_tester.py
#updated version of model tests
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
            print self.result.statustesting to work with model.py

r = Result()
r.run_test( neg_output )
