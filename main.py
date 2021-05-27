# main entry point

# from src.app import run, root

from Chapter02_ApproximatedRoots.secant import secant_method

if __name__ == "main":
	print("Hello World!")

# bisection_method("x^3 + 3x^2 + 12x + 8", -5, 5, maxIters=99)
# falsePosition_method("x^3 + 3x^2 + 12x + 8", -5, 5, maxIters=99)
# newtonRaphson_method("x^3 + 3x^2 + 12x + 8", -5, maxIters=99)
# backwardDiff_method("3x + 2", [1891, 1901, 1911, 1921, 1931], [46, 66, 81, 93, 101], 1925)
secant_method("x^3 + 3x^2 + 12x + 8", -5, 5, maxIters=99)

# run(root)
