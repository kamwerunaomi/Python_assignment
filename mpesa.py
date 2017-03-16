import datetime
class MPESA:
	def __init__(self):
		self.name=input("Please Enter Your Name")
		self.phone_number=input("Please Enter Your Phone Number")	
		print("Dear {} welcome to MPESA".format(self.name))	
		print("Start by depositing some money")
		self.balance=0
		self.deposits=[]
		self.withdrawals=[]
	def deposit_cash(self, amount):
		if amount < 50:
			print("Thank you for using MPESA  but sorry you cant deposit less than 50 shillings")
		else:
			self.balance+=amount
			print("Thank You for using MPESA your balance is{}".format(self.balance))
			deposits_details={"time":datetime.datetime.now(),"amount":self.balance}
			self.deposits.append(deposits_details)	
	def show_balance(self):
		print("Dear {} your current balance is {}".format(self.name,self.balance))
	def withdraw_cash(self,amount):
		if amount <50:
			print("thank you for using MPESA but you cant withdraw less than 50 shillings")
		elif amount > self.balance:
			print("Thank you for using MPESA but sorry your account balance is insufficient")
		else:
			self.balance-=amount
			print("Thank you {} for using MPESA your balance is {} ".format(self.name, self.balance))
			withdrwals_details={"time":datetime.datetime.now(),"amount":self.balance}
			self.withdrawals.append(withdrwals_details)
	def show_deposits(self):
		for deposit in self.deposits:
			print("Dear {} on {} you deposited {} and your account balance is {}".format(self.name,deposit["time"].strftime("%c"),deposit["amount"],self.balance))
	def show_withdrawals(self):
		for withdrawal in self.withdrawals:
			print("Dear {} on {} you deposited {} and your account balance is {}".format(self.name,deposit["time"].strftime("%c"),deposit["amount"],self.balance))
