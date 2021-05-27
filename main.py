# main entry point

# from src.app import run, root

from Chapter04_Diff_Int.Integration.Trapezium_method import trapezium_method
from lib.input_parser import InputParser
from Chapter04_Diff_Int.Integration.Gsimpsons_onethird_method import simpson_1_3rd
from Chapter04_Diff_Int.Integration.Gsimpsons_threeeigth_method import simpson_3_8th
from Chapter02_ApproximatedRoots.secant import secant_method
from Chapter03_Interpolation.Lagrange import Lagrange

if __name__ == "main":
	print("Hello World!")

# bisection_method("x^3 + 3x^2 + 12x + 8", -5, 5, maxIters=99)
# falsePosition_method("x^3 + 3x^2 + 12x + 8", -5, 5, maxIters=99)
# newtonRaphson_method("x^3 + 3x^2 + 12x + 8", -5, maxIters=99)
# backwardDiff_method("3x + 2", [1891, 1901, 1911, 1921, 1931], [46, 66, 81, 93, 101], 1925)
# secant_method("x^3 + 3x^2 + 12x + 8", -5, 5, maxIters=99)
# a = InputParser()
# b = a.sanitizeInput(a.getInputStr("Equation = "))
# c = a.getNumInput("Lower Limit = ")
# d = a.getNumInput("Upper Limit = ")
# e = a.getNumInput("Intervals = ")

# simpson_1_3rd(b, float(c), float(d), int(e), maxIters = 99)
# simpson_3_8th(b, float(c), float(d), int(e), maxIters = 99)
# trapezium_method(b, float(c), float(d), int(e), maxIters = 99)


l = Lagrange([0,0.2,0.4,0.6,0.8], [1,1.22140,1.49182,1.82212,2.22554])
l.interpolate(0.65)

"""
Enter Value to be Interpolated: 0.65
Value After 1st Iteration: -0.02197
Value After 1st Iteration: 0.15506
Value After 1st Iteration: 2.08191
Value After 1st Iteration: 0.2119
"""
# run(root)
