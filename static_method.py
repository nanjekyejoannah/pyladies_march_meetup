class Animal:

	#specifying instance variables
	def __init__(self, kind):
		self.kind = kind

	#instance method
	def print_kind(self):
		print (self.kind)

	#static method
	@staticmethod
	def sound(x):
		print(x)

anim1 = Animal("wild")
anim1.sound("woof")