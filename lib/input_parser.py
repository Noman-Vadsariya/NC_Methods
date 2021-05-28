class InputParser:
	__instance = None

	# def __init__(self):
	# 	if InputParser.__instance != None:
	# 		return InputParser.__instance

	# 	InputParser.__instance = self

	@staticmethod
	def getInstance():
		if InputParser.__instance is None:
			InputParser()

		return InputParser.__instance

	# bisection, a, b, f(x)
	# false position, a, b, f(x)
	# newton raphson, a, b, f(x)
	# secant, a, b, f(x)

	def getInputStr(self, prompt = None):
		"""Gets function as a string input from user

		Args:
			prompt (str, optional): the prompt for input. Defaults to None.

		Returns:
			str: inputted function
		"""
		if prompt is None or not isinstance(prompt, str):
			inputStr = input()
		else:
			inputStr = input(prompt)

		return inputStr

	def sanitizeInput(self, inputStr = None):
		"""Sanitizes user input, replacing ^ with ** and ax with a*x, the python equivalents.

		This does NOT validate input strings. Expected input should be valid.

		Args:
			inputStr (str, optional): valid input string. Defaults to None.

		Raises:
			Exception: [invalid input expression]

		Returns:
			str: sanitized input string
		"""

		if inputStr is None or not isinstance(inputStr, str):
			raise Exception("[invalid input expression]")

		i = -1

		for char in inputStr:
			if inputStr[i] == "^":
				inputStr = inputStr[0 : i] + "**" + inputStr[(i + 1) :]
				i += 1
			else:
				if char.isalpha() and char in ["x", "y", "z"] and inputStr[i].isnumeric():
					if i > -1:
						inputStr = inputStr[0 : (i + 1)] + "*" + inputStr[(i + 1) :]
						i += 1

			i += 1
		
		return inputStr

	def getNumInput(self, prompt = None):
		"""Take numeric input only

		Args:
			prompt (str, optional): the prompt for input. Defaults to None.

		Raises:
			Exception: only numeric input is accepted

		Returns:
			int|float: number taken as input
		"""

		n = None
		if prompt is None or not isinstance(prompt, str):
			n = input()
		else:
			n = input(prompt)

		# if n.isnumeric() == False:
		# 	raise Exception("[only numeric input is accepted]")

		return float(n)
