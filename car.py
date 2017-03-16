class Toyota:
	def __init__(self,types,color,year_of_make,mileage,initial_cost,):
		self.type=types
		self.color=color
		self.year_of_make=year_of_make
		self.mileage=mileage
		self.initial_cost=initial_cost
	def year_of_service(self):
			year=2017-self.year_of_make
			return year
	def new_price(self):
			depreciation=5%
			price=depreciation*year*self.initial_cost
			return price




