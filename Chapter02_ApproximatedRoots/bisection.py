from lib.processor import Processor

p = Processor()
p.setVariable("x")

def bisection_method(function = None, lowerLimit = None, upperLimit = None, tol = None, maxIters = None):
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

	x = calcNextLimit()

	i = 0
	result = None

	while (abs(p.getUpperLimit() - p.getLowerLimit()) > tol) and (i < maxIters):
		result = p.solveFunction({ "x": x })

		p.addResult({
			"lower limit": p.getLowerLimit(),
			"upper limit": p.getUpperLimit(),
			"x": x,
			"y": result,
			"absolute error": calcAbsoluteError(x, i - 1)
		})

		if i != 0 and calcAbsoluteError(x, i - 1) < tol:
			break

		if result > 0:
			p.setLimits(p.getLowerLimit(), x)
		else:
			p.setLimits(x, p.getUpperLimit())
		
		x = calcNextLimit()
		i += 1

	p.printResults(("lower limit", "upper limit", "x", "y", "absolute error"))

def calcAbsoluteError(x, index):
	prevX = None

	try:
		prevX = p.getResultAtIndex(index).get("x")
	except:
		return 0

	return abs(x - prevX)

def calcNextLimit():
	return (p.getLowerLimit() + p.getUpperLimit()) / 2
