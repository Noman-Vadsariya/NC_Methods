# from sympy import symbols, sympify
# from sympy.core.function import diff
# from sympy.core.evalf import evalf
from sympy import *
from .input_parser import InputParser

class Processor:
	def __init__(self):
		self.parser = InputParser()

	def __getattr__(self, attribute):
		value = self.__dict__.get(attribute)

		# silence getattr by returning None
		if not value:
			return None
		
		return value

	def setAttr(self, attribute = None, value = None):
		if attribute is None or not isinstance(attribute, str):
			raise Exception("[invalid attribute parameter passed]")
		
		setattr(self, attribute, value)
	
	def getAttr(self, attribute = None):
		if attribute is None or not isinstance(attribute, str):
			raise Exception("[invalid attribute parameter passed]")
		
		return getattr(self, attribute)

	def setVariable(self, variable = "x"):
		if not isinstance(variable, str) or not variable.isalpha() or len(variable) != 1:
			raise Exception("[expected an alphabetical letter as a variable")

		sympyVar = None
		try:
			sympyVar = symbols(variable)
		except:
			raise Exception("[invalid variable passed for sympy conversion]")

		if self.variables is None:
			self.setAttr("variables", dict())

		self.variables[variable] = sympyVar

	def getVariable(self, variable = "x"):
		if not isinstance(variable, str) or not variable.isalpha() or len(variable) != 1:
			raise Exception("[expected an alphabetical letter as a variable")

		if self.variables is None:
			return None

		var = None

		return self.variables.get(variable)

	def setFunc(self, function = None):
		if function is None or not isinstance(function, str):
			raise Exception("[invalid function parameter passed]")

		sympyFunction = None
		parsedFunction = None
		try:
			parsedFunction = self.parser.sanitizeInput(function)
			sympyFunction = sympify(parsedFunction)
		except:
			raise Exception("[unable to parse function]")
		
		self.setAttr("function", function)
		self.setAttr("parsedFunction", parsedFunction)
		self.setAttr("sympyFunction", sympyFunction)

	def getFunc(self):
		return self.function
	
	def setLimits(self, lower = None, upper = None):
		if lower is None or upper is None or (not isinstance(lower, int) and not isinstance(lower, float)) or(not isinstance(upper, int) and not isinstance(upper, float)):
			raise Exception("[invalid lower/upper parameter passed]")
		
		if self.limits is None:
			self.setAttr("limits", dict())

		self.limits["lower"] = lower
		self.limits["upper"] = upper
	
	def getLowerLimit(self):
		if self.limits is None:
			return None

		return self.limits.get("lower")

	def getUpperLimit(self):
		if self.limits is None:
			return None

		return self.limits.get("upper")

	def setPoints(self, axis = None, points = None):
		if axis is None or (axis != "x" and axis != "y"):
			raise Exception("[invalid axis parameter passed]")

		if points is None or not isinstance(points, list):
			raise Exception("[invalid points parameter passed]")
		
		self.setAttr("pointsOn" + axis.upper(), points)

	## processed input parameters
	def derivate(self, variable = None, n = 1):
		if not isinstance(variable, str) or not variable.isalpha() or len(variable) != 1:
			raise Exception("[expected an alphabetical letter as a variable")

		if n <= 0 or n > 6:
			raise Exception("[invalid number of derivations passed]")

		if self.sympyFunction is None or self.getVariable(variable) is None:
			raise Exception("[unable to find function/variable assignments]")

		if self.derivations is None:
			self.setAttr("derivations", list())
		else:
			if len(self.derivations) >= n:
				return self.derivations[n - 1]

		startIndex = 0
		if len(self.derivations) > 0:
			startIndex = len(self.derivations)

		result = None
		var = self.getVariable(variable)

		for i in range(startIndex, n):
			try:
				if i == 0:
					result = diff(self.sympyFunction, var)
				else:
					result = diff(self.derivations[i - 1], var)
			except:
				raise Exception(f"[can not evaluate the {i}th derivative of function]")

			self.derivations.insert(i, result)

	# valueMap => { x: 2, y: 3 ... }
	def solveFunction(self, valueMap = None, function = None):
		if valueMap is None or not isinstance(valueMap, dict):
			raise Exception("[invalid valueMap parameter passed]")

		if function is None:
			function = self.sympyFunction

		if function is None:
			raise Exception("[unable to find function assignment]")

		variables = self.variables.keys()

		for var in valueMap:
			if var not in variables:
				raise Exception(f"[list of variables does not contain {var} as a variable]")

		result = None

		try:
			result = function.subs(valueMap.items())
		except:
			raise Exception("[unable to substitute values in function]")
		
		try:
			result = result.evalf()
		except:
			raise Exception("[unable to evaluate function]")

		return result

	def solveDerivative(self, variable = None, valueMap = None, n = None):
		if not isinstance(variable, str) or not variable.isalpha() or len(variable) != 1:
			raise Exception("[expected an alphabetical letter as a variable")

		if self.getVariable(variable) is None:
			raise Exception("[unable to find variable assignment]")

		if valueMap is None or not isinstance(valueMap, dict):
			raise Exception("[invalid valueMap parameter passed]")

		variables = self.variables.keys()

		for var in valueMap:
			if var not in variables:
				raise Exception(f"[list of variables does not contain {var} as a variable]")

		if n <= 0 or n > 6:
			raise Exception("[invalid number of derivations passed]")

		self.derivate(variable, n)

		if (len(self.derivations) < n):
			raise Exception(f"[unable to derivate this function {n} times]")

		return self.solveFunction(valueMap, self.derivations[n - 1])
