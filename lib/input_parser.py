class InputParser:
	__instance = None

	def __init__(self):
		if InputParser.__instance != None:
			raise Exception("[object is singleton]")

		InputParser.__instance = self

	@staticmethod
	def getInstance():
		if InputParser.__instance is None:
			InputParser()

		return InputParser.__instance

	# bisection, a, b, f(x)
	# false position, a, b, f(x)
	# newton raphson, a, b, f(x)
	# secant, a, b, f(x)

	def sanitize_input(self, input_str = None):
		if input_str is None:
			raise Exception("[invalid input expression]")

		i = -1

		for char in input_str:
			if input_str[i] == "^":
				input_str = input_str[0 : i] + "**" + input_str[(i + 1) :]
				i += 1
			else:
				if char.isalpha() and char in ["x", "y", "z"] and input_str[i].isnumeric():
					if i > -1:
						input_str = input_str[0 : (i + 1)] + "*" + input_str[(i + 1) :]
						i += 1

			i += 1
		
		return input_str
