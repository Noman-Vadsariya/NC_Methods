# main entry point

from lib.input_parser import InputParser

from Chapter02_ApproximatedRoots.bisection import bisection_method
from Chapter02_ApproximatedRoots.false_position import falsePosition_method
from Chapter02_ApproximatedRoots.newton_raphson import newtonRaphson_method
from Chapter02_ApproximatedRoots.secant import secant_method

from Chapter03_Interpolation.Backward_Diff import Backward_Difference
from Chapter03_Interpolation.DivDiff import DividedDifference
from Chapter03_Interpolation.Forward_Diff import Forward_Difference
from Chapter03_Interpolation.Lagrange import Lagrange

from Chapter04_Diff_Int.Differentiation.threepoint import ThreePoint
from Chapter04_Diff_Int.Differentiation.fivepoint import FivePoint
from Chapter04_Diff_Int.Differentiation.Forward_Backward import Forward_Backward

from Chapter04_Diff_Int.Integration.Gsimpsons_onethird_method import simpson_1_3rd
from Chapter04_Diff_Int.Integration.Gsimpsons_threeeigth_method import simpson_3_8th
from Chapter04_Diff_Int.Integration.Trapezium_method import trapezium_method

from Chapter05_DE.Euler import Euler
from Chapter05_DE.four_rk import FourthOrder
from Chapter05_DE.Heuns import Heuns
from Chapter05_DE.Midpoint import Midpoint
from Chapter05_DE.Modified_Euler import Modified_Euler

if __name__ == "main":
	print("\n")

ip = InputParser()
opt = 0
keepRunning = True

result = None

equation = None
lowerLimit = None
upperLimit = None

x_points = None
y_points = None
y_matrix = None
interpolation_target = None

h = None
intervals = None

diffEquation = None
x0 = None
y0 = None

o = None # for class objects

print("==========================")
print("Numerical Analysis Methods")
print("==========================")
print("\n")

while keepRunning:
	print("Select any one of the chapter options below to see what methods of that chapter can be utilized\n")
	print("2 - Chapter 02 [Approximated Roots]\n3 - Chapter 03 [Interpolation]\n4 - Chapter 04 [Differentiation & Integration]\n5 - Chapter 05 [Differential Equations]\n")
	print("(You can press 0 to Exit the program)\n")

	opt = ip.getNumInput("Enter option number: ")

	if opt < 2 or opt > 5:
		if (opt == 0):
			keepRunning = False
		else:
			print("Invalid chapter number selected, try again\n")
		continue

	if opt == 2:
		print("Select any one of the method options below to utilize that method\n")
		print("0 - Bisection\n1 - False Position\n2 - Newton Raphson\n3 - Secant\n")

		opt = ip.getNumInput("Enter option number: ")

		equation = ip.sanitizeInput(ip.getInputStr("Enter equation = "))
		lowerLimit = ip.getNumInput("Lower Limit = ")
		upperLimit = ip.getNumInput("Upper Limit = ")

		if opt == 0:
			bisection_method(equation, lowerLimit, upperLimit, maxIters = 99)
		elif opt == 1:
			falsePosition_method(equation, lowerLimit, upperLimit, maxIters = 99)
		elif opt == 2:
			newtonRaphson_method(equation, lowerLimit, upperLimit, maxIters = 99)
		elif opt == 3:
			secant_method(equation, lowerLimit, upperLimit, maxIters = 99)
		else:
			print("Invalid option; returning back to menu")
			continue
	elif opt == 3:
		print("Select any one of the method options below to utilize that method\n")
		print("0 - Backward Difference\n1 - Forward Difference\n2 - Divided Difference\n3 - Lagrange\n")

		opt = ip.getNumInput("Enter option number: ")

		x_points = list(map(float, (ip.getInputStr("Enter points on x (space-sep) = ")).split(" ")))
		y_matrix = [[0 for i in range(len(x_points))] for i in range(len(x_points))]
		y_points = list(map(float, (ip.getInputStr("Enter points on y (space-sep) = ")).split(" ")))

		for i in range(len(y_points)):
			y_matrix[i][0] = y_points[i]

		interpolation_target = ip.getNumInput("Enter value to interpolate = ")

		if opt == 0:
			o = Backward_Difference(x_points, y_matrix)
			o.Construct_Backward_Difference_Table()
			o.print_table()
			result = o.interpolate(interpolation_target)
		elif opt == 1:
			o = Forward_Difference(x_points, y_matrix)
			o.Construct_Forward_Difference_Table()
			o.print_table()
			result = o.interpolate(interpolation_target)
		elif opt == 2:
			o = DividedDifference(x_points, y_points)
			result = o.newton_polynomial(interpolation_target)
		elif opt == 3:
			o = Lagrange(x_points, y_points)
			result = o.interpolate(interpolation_target)
		else:
			print("Invalid option; returning back to menu")
			continue
			
		# print(f"Final Interpolated Value = {result}")
	elif opt == 4:
		print("Select any one of the method options below to utilize that method\n")
		print("0 - 3-Point (Diff.)\n1 - 5-Point (Diff.)\n2 - Forward/Backward (Diff.)\n3 - Simpson's 1/3rd (Integration)\n4 - Simpson's 3/8th (Integration)\n5 - Trapezium (Integration)")

		opt = ip.getNumInput("Enter option number: ")

		equation = ip.sanitizeInput(ip.getInputStr("Enter equation = "))
		
		if opt >= 0 and opt <= 2:
			h = ip.getNumInput("Enter h = ")
			x_points = list(map(float, (ip.getInputStr("Enter points on x (space-sep) = ")).split(" ")))
			y_points = list(map(float, (ip.getInputStr("Enter points on y (space-sep) = ")).split(" ")))
			if (len(x_points) != len(y_points)):
				print("Uneven x, f(x) values provided; try again")
				continue
		else:
			lowerLimit = ip.getNumInput("Lower Limit = ")
			upperLimit = ip.getNumInput("Upper Limit = ")
			intervals = ip.getNumInput("Intervals = ")
		if opt == 0:
			if (len(x_points) < 3):
				print("\nAt least 3 points need to be entered; try again\n")
				continue
	
			o = ThreePoint(x_points, y_points, h, equation)
			o.Differentiate()
			o.print_table()
		elif opt == 1:
			if (len(x_points) < 5):
				print("\nAt least 5 points need to be entered; try again\n")
				continue

			o = FivePoint(x_points, y_points, h, equation)
			o.Differentiate()
			o.print_table()
		elif opt == 2:
			if (len(x_points) < 2):
				print("\nAt least 2 points need to be entered; try again\n")
				continue

			o = Forward_Backward(x_points, y_points, h, equation)
			o.Differentiate()
			o.print_table()
		elif opt == 3:
			simpson_1_3rd(equation, lowerLimit, upperLimit, intervals, maxIters = 99)
		elif opt == 4:
			simpson_3_8th(equation, lowerLimit, upperLimit, intervals, maxIters = 99)
		elif opt == 5:
			trapezium_method(equation, lowerLimit, upperLimit, intervals, maxIters = 99)
		else:
			print("Invalid option; returning back to menu")
			continue

	elif opt == 5:
		print("Select any one of the method options below to utilize that method\n")
		print("0 - Euler\n1 - 4RK\n2 - Heuns\n3 - Midpoint\n4 - Modified-Euler\n")

		opt = ip.getNumInput("Enter option number: ")

		equation = ip.sanitizeInput(ip.getInputStr("Enter equation = "))
		diffEquation = ip.sanitizeInput(ip.getInputStr("Enter differentiation equation = "))
		lowerLimit = ip.getNumInput("Lower Limit = ")
		upperLimit = ip.getNumInput("Upper Limit = ")
		h = ip.getNumInput("Enter h = ")
		x0 = ip.getNumInput("Enter x0 = ")
		y0 = ip.getNumInput("Enter y0 = ")

		if opt == 0:
			o = Euler(equation, h, lowerLimit, upperLimit, x0, y0, diffEquation)
			o.iteration()
		elif opt == 1:
			o = FourthOrder(equation, h, lowerLimit, upperLimit, x0, y0, diffEquation)
			o.iterations()
		elif opt == 2:
			o = Heuns(equation, h, lowerLimit, upperLimit, x0, y0, diffEquation)
			o.iterations()
		elif opt == 3:
			o = Midpoint(equation, h, lowerLimit, upperLimit, x0, y0, diffEquation)
			o.iterations()
		elif opt == 4:
			o = Modified_Euler(equation, h, lowerLimit, upperLimit, x0, y0, diffEquation)
			o.iterations()
		else:
			print("Invalid option; returning back to menu")
			continue
