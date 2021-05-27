import numpy
from sympy import *

from Chapter02_ApproximatedRoots.Bisection_method import \
    Bisection as bisection
from Chapter02_ApproximatedRoots.Falseposition_method import \
    FalsePosition as false_position
from Chapter02_ApproximatedRoots.Newtonraphson_method import \
    NewtonRaphson as newton_raphson

x = symbols('x')
r = sympify('3*x').subs(x, 1).evalf()

print(f"R = {r}")

#Input Format: x^2+4*x-2:
# equation = input('f(x): ')
# Handling equation for eval()
# equation = equation.replace("^", "**")

# a = float(input('Lower Limit: '))
# b = float(input('Upper limit: '))

# obj = bisection(equation, a, b)
# obj.iterations()

