from math import factorial
from lib.processor import Processor

p = Processor()
p.setVariable("x")

def backwardDiff_method(function = None, pointsOnX = None, pointsOnY = None, interpolationDegree = None, tol = None, maxIters = None):
	if tol is None:
		tol = 10e-6

	if maxIters is None:
		maxIters = 5

	if (not isinstance(tol, int) and not isinstance(tol, float)) or not isinstance(maxIters, int):
		raise Exception("[invalid tolerance/max iterations parameters passed]")

	if maxIters < 0 or maxIters > 100:
		raise Exception("[max iterations can only range between 0 to 100]")

	p.setFunc(function)
	p.setPoints("x", pointsOnX)
	p.setPoints("y", pointsOnY)

	yCount = len(pointsOnY)

	# 2D array for managing y and difference columns
	p.setAttr("diffMatrix", [([0] * yCount) for i in range(yCount)])

	p.clearResults()

	constructDiffTable()
	printDiffTable()

	diffMatrix = p.getAttr("diffMatrix")

	sum = diffMatrix[yCount - 1][0]
	s = (interpolationDegree - pointsOnX[len(pointsOnX) - 1]) / (pointsOnX[1] - pointsOnX[0])

	for i in range(1, yCount):
		sum += (calcS(s, i) * diffMatrix[yCount - 1][i]) / factorial(i)

	print(f"Interpolated Value = {round(sum, 5)}")

def constructDiffTable():
	pointsOnX = p.getAttr("pointsOnX")
	pointsOnY = p.getAttr("pointsOnY")
	diffMatrix = p.getAttr("diffMatrix")

	xCount = len(pointsOnX)

	for i in range(len(pointsOnY)):
		diffMatrix[i][0] = pointsOnY[i]
	
	for i in range(1, xCount):
		for j in range((xCount - 1), (i - 1), -1):
			diffMatrix[j][i] = diffMatrix[j][(i - 1)] - diffMatrix[(j - 1)][(i - 1)]

def printDiffTable():
	p.clearResults()

	pointsOnY = p.getAttr("pointsOnY")
	yCount = len(pointsOnY)

	diffMatrix = p.getAttr("diffMatrix")

	result = None
	key = "Δy"

	columns = list()
	columns.append("y")
	columns.append(key)

	key_index = 0

	for i in range(yCount):
		result = {}
		for j in range(yCount):
			if j == 0:
				result["y"] = diffMatrix[i][j]
			else:
				if j > 1:
					if diffMatrix[i][j] == 0:
						result[key + "^" + str(j)] = ""
					else:
						result[key + "^" + str(j)] = diffMatrix[i][j]
					if key_index < j:
						key_index = j
						columns.append(key + "^" + str(j))
				else:
					if diffMatrix[i][j] == 0:
						result[key] = ""
					else:
						result[key] = diffMatrix[i][j]
				
		p.addResult(result)
	
	p.printResults(tuple(columns))

def calcAbsoluteError(x, index):
	prevX = None

	try:
		prevX = p.getResultAtIndex(index).get("x")
	except:
		return 0

	return abs(x - prevX)

def calcS(s, n):
	temp = s

	for i in range(1, n):
		temp *= (s + i)

	return temp
