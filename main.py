# main entry point

from lib.processor import Processor
# from src.app import run, root

if __name__ == "main":
	print("Hello World!")

a = Processor()
a.setVariable('x')
print(a.x)
a.setLimits(0, 2)
print(a.getUpperLimit())
a.setPoints("x", [1, 2, 3, 4])
print(a.pointsOnX)
print(a.pointsOnY)
a.setFunc("exp(2x)")
print(a.function)
print(a.parsedFunction)
print(a.sympyFunction)
a.derivate("x", 3)
print(a.derivations)
a.derivate("x", 5)
print(a.derivations)
print(a.solveFunction({ "x": 2 }))
print(a.solveDerivative("x", { "x": 2 }, 3))
# run(root)
