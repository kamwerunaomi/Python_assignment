import datetime
class SavingsAccount:
	def __init__(self):
		self.name=input("Please Enter Your Name")
		self.phone_number=input("Please Enter Your Phone Number")	
		print("Welcome {}.".format(self.name))	
		print("Start by depositing some money")
		self.balance=500
		self.deposits=[]
		self.withdrawals=[]
	def deposit_cash(self, amount):
		if amount < 0:
			print("Invalid Deposit Amount ")
		else:
			self.balance+=amount
			print("Your balance is{}".format(self.balance))
			deposits_details={"time":datetime.datetime.now(),"amount":self.balance}
			self.deposits.append(deposits_details)	
	
