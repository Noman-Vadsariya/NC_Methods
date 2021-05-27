from math import *
from sympy import Symbol, sympify

class Bisection:
    def __init__(self, equation, a, b, tolerance):
        self.equation = equation
        self.a = a
        self.b = b
        self.tolerance = tolerance

    def iterations(self):
        x = Symbol('x')
        print("A\tF(A)\tB\tF(B)\tC\tF(C)\tAbsolute error")
        midpoint = (self.a+self.b)/2
        Xo = self.a
        Yo = self.b
        # F_X = float(sympify(self.equation).subs('x',midpoint).evalf())
        # F_A = float(sympify(self.equation).subs('x',self.a).evalf())
        # F_B = float(sympify(self.equation).subs('x',self.b).evalf())

        while abs(self.b-self.a) > tolerance:
            F_A = float(sympify(self.equation).subs('x',self.a).evalf())
            F_B = float(sympify(self.equation).subs('x',self.b).evalf())
            F_X = float(sympify(self.equation).subs('x',midpoint).evalf())
            if(F_X > 0):
                # print(f"{round(self.a,2)}\t{round(F_A,2)}\t{round(self.b,2)}\t{round(F_B,2)}\t{round(midpoint,2)}\t{round(F_X,2)}\t{round(self.b-self.a,5)}\t")
                Yo = self.b
                self.b = midpoint
            else:
                # print(f"{round(self.a,2)}\t{round(F_A,2)}\t{round(self.b,2)}\t{round(F_B,2)}\t{round(midpoint,2)}\t{round(F_X,2)}\t{round(self.b-self.a,5)}\t")
                Xo = self.a
                self.a = midpoint       
            print(f"{round(Xo,2)}\t{round(F_A,2)}\t{round(Yo,2)}\t{round(F_B,2)}\t{round(midpoint,2)}\t{round(F_X,2)}\t{round(self.b-self.a,5)}\t")     
            midpoint = (self.a+self.b)/2

        print('******** BISECTION METHOD ********')
<<<<<<< HEAD
        print('Approximated root: ', midpoint)


if __name__ == "__main__":
    #Input Format: x^2+4*x-2:
    equation = input('f(x): ')
    #Handling equation for eval()
    equation = equation.replace("^", "**")

    a = float(input('Lower Limit: '))
    b = float(input('Upper limit: '))
    tolerance = float(input('Input the toleramce level: '))

    obj = Bisection(equation,a,b,tolerance)
    obj.iterations()
    
=======
        print('Approximated root: ', x)
>>>>>>> 5d3a9f821955612fd5a41531db74d7f45ff5fdab
