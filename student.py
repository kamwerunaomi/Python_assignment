class Student:
	def __init__(self,first_name,last_name,age,gender):
		self.first_name=first_name
		self.last_name=last_name
		self.age=age
		self.gender=gender
	def show_name(self):
			full_name="{} {}".format(self.first_name, self.last_name)
			return full_name
	def year_of_birth(self):
		year=2017-self.age
		return year
	def show_initiales(self):
		initiales=self.first_name[0],self.last_name[0]
		return initiales
			
