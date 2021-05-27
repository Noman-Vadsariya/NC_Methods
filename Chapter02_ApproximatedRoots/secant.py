from lib.processor import Processor

p = Processor()
p.setVariable("x")

def secant_method(function = None, lowerLimit = None, upperLimit = None, tol = None, maxIters = None):
	if tol is None:
		tol = 10e-6

	if maxIters is None:
		maxIters = 5

	if (not isinstance(tol, int) and not isinstance(tol, float)) or not isinstance(maxIters, int):
		raise Exception("[invalid tolerance/max iterations parameters passed]")

	if maxIters < 0 or maxIters > 100:
		raise Exception("[max iterations can only range between 0 to 100]")

	p.setFunc(function)
	p.setLimits(lowerLimit, upperLimit)
	p.clearResults()

	y_upperLimit = p.solveFunction({ "x": p.getUpperLimit() })
	y_lowerLimit = p.solveFunction({ "x": p.getLowerLimit() })

	x = calcNextLimit(y_upperLimit, y_lowerLimit)

	i = 0
	result = None

	while (abs(p.getUpperLimit() - p.getLowerLimit()) > tol) and (i < maxIters):
		result = p.solveFunction({ "x": x })

		p.addResult({
			"lower limit": p.getLowerLimit(),
			"upper limit": p.getUpperLimit(),
			"f(upper limit)": y_upperLimit,
			"f(lower limit)": y_lowerLimit,
			"x": x,
			"y": result,
			"absolute error": calcAbsoluteError(x, i - 1)
		})

		p.setLimits(p.getUpperLimit(), x)

		if i != 0 and calcAbsoluteError(x, i - 1) < tol:
			break

		y_upperLimit = p.solveFunction({ "x": p.getUpperLimit() })
		y_lowerLimit = p.solveFunction({ "x": p.getLowerLimit() })

		x = calcNextLimit(y_upperLimit, y_lowerLimit)

		i += 1

	p.printResults(("lower limit", "upper limit", "f(upper limit)", "f(lower limit)", "x", "y", "absolute error"))

def calcAbsoluteError(x, index):
	prevX = None

	try:
		prevX = p.getResultAtIndex(index).get("x")
	except:
		return 0

	return abs(x - prevX)

def calcNextLimit(yWithUpperLimit, yWithLowerLimit):
	return ((p.getLowerLimit() * yWithUpperLimit) - (p.getUpperLimit() * yWithLowerLimit)) / (yWithUpperLimit - yWithLowerLimit)
