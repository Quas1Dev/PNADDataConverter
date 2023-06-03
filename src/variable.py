class Variable:
	def __init__(self, initialPos, size, code, description):
		self.initialPos =initialPos
		self.size = size 
		self.code = code 
		self.description = description
		self.category = []

	def addCategory(self, category):
		self.category.append(category)

	def __str__(self):
		return f"{self.code} - {self.description}"