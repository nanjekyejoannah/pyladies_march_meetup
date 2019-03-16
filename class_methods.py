class Animal:

	#specifying instance variables
	def __init__(self, kind):
		self.kind = kind

	#instance method
	def print_kind(self):
		print (self.kind)

	#class method
	@classmethod
	def sound(cls, x):
		print(x)

Animal.sound("woof")