class Age:
	def __init__(self):
		self.name=input("Please enter your name")
		self.age=input("Please enter your age")
		self.year=2017-self.age
		print("Hello {} you were born in {}".format(self.age,self.year))
		