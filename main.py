# main entry point

# from src.app import run, root

from src.ch_2.secant import secant_method
from lib.input_parser import InputParser
from src.ch_3.backward_diff import backwardDiff_method
from src.ch_2.bisection import bisection_method
from src.ch_2.false_position import falsePosition_method
from src.ch_2.newton_raphson import newtonRaphson_method

if __name__ == "main":
	print("Hello World!")

# bisection_method("x^3 + 3x^2 + 12x + 8", -5, 5, maxIters=99)
# falsePosition_method("x^3 + 3x^2 + 12x + 8", -5, 5, maxIters=99)
# newtonRaphson_method("x^3 + 3x^2 + 12x + 8", -5, maxIters=99)
# backwardDiff_method("3x + 2", [1891, 1901, 1911, 1921, 1931], [46, 66, 81, 93, 101], 1925)
secant_method("x^3 + 3x^2 + 12x + 8", -5, 5, maxIters=99)

# run(root)
