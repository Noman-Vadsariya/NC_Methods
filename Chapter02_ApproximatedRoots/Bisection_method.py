from math import *

class Bisection:
    def __init__(self, equation, a, b):
        self.equation = equation
        self.a = a
        self.b = b


    def iterations(self):
        x = (self.a+self.b)/2
        while abs(self.b-self.a) > 0.00001: #Corrected upto 10^-6
            if(eval(self.equation) > 0):
                self.b = x
            else:
                self.a = x
            x = (self.a+self.b)/2

        print('******** BISECTION METHOD ********')
        print('Approximated root: ', x)
