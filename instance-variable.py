class Animal:

	#specifying instance variables
	def __init__(self, kind):
		self.kind = kind

	#instance method
	def print_kind(self):
		print (self.kind)

animal1 = Animal("domestic")
animal1.print_kind()

animal2 = Animal("Wild")
animal2.print_kind()