from lib.processor import Processor

p = Processor()
p.setVariable("x")

def simpson_3_8th(function = None, lowerLimit = None, upperLimit = None, intervals = None, tol = None, maxIters = None):
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

	y_lowerLimit = p.solveFunction({ "x": p.getLowerLimit() })
	y_upperLimit = p.solveFunction({ "x": p.getUpperLimit() })

	h = (p.getUpperLimit() - p.getLowerLimit()) / intervals
	p.setAttr("h", h)

	result = y_lowerLimit
	y_next = None

	three_counter = 0

	for i in range(1, intervals, 1):

		y_next = p.solveFunction({ "x": (p.getLowerLimit() + (i * h)) })

		p.addResult({
			"lower limit": p.getLowerLimit(),
			"f(lower limit)": y_next
		})

		if three_counter < 2:
			result += (3 * y_next)
			three_counter += 1
		else:
			result += (2 * y_next)
			three_counter = 0

	area = ((3 * h) / 8) * (result + y_upperLimit)
	print(f"Area Under The Curve = {area}")

	p.printResults(("lower limit", "f(lower limit)"))
