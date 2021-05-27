from lib.processor import Processor

p = Processor()
p.setVariable("x")

def newtonRaphson_method(function = None, x0 = None, tol = None, maxIters = None):
	if tol is None:
		tol = 10e-6

	if maxIters is None:
		maxIters = 5

	if (not isinstance(tol, int) and not isinstance(tol, float)) or not isinstance(maxIters, int):
		raise Exception("[invalid tolerance/max iterations parameters passed]")

	if maxIters < 0 or maxIters > 100:
		raise Exception("[max iterations can only range between 0 to 100]")

	if (not isinstance(x0, int)) and (not isinstance(x0, float)):
		raise Exception("[invalid x0 parameter passed]")

	p.setFunc(function)
	p.derivate("x", 1)
	p.clearResults()

	prevX = x0
	nextX = None

	i = 0
	result = None
	y_prime = None

	while i < maxIters:
		result = p.solveFunction({ "x": prevX })
		y_prime = p.solveDerivative("x", { "x": prevX }, 1)

		nextX = calcNextLimit(prevX, result, y_prime)

		p.addResult({
			"x": prevX,
			"x'": nextX,
			"y": result,
			"y'": y_prime,
			"absolute error": calcAbsoluteError(prevX, i - 1)
		})

		if i != 0 and calcAbsoluteError(nextX, i - 1) < tol:
			break

		prevX = nextX
		i += 1

	p.printResults(("x", "x'", "y", "y'", "absolute error"))

def calcAbsoluteError(x, index):
	prevX = None

	try:
		prevX = p.getResultAtIndex(index).get("x")
	except:
		return 0

	return abs(x - prevX)

def calcNextLimit(x, y, yPrime):
	return x - (y / yPrime)
