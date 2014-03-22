# A Banking account for the Bank X
# Some algorithms were created just to demonstrate basic methods

Birthday_data = {'David': '03.03.1994', 'George': '12.01.1991', 'Andrey': '09/05/1990'}
SSN = {'David': '23423443', 'George': '343423423', 'Andrey': '34333432'}
Account_Type = {'David': 'Checking', 'George': 'Saving', 'Andrey': 'Checking'}
ERROR = {}

class Account:
	"Banking Account for the Bank X"
	interest = 0.05

	def __init__(self, account_holder, card_number, PIN):
		self.balance = 0
		self.holder = account_holder
		self.card_number = card_number
		self.PIN = PIN

	def day_of_birth(self):
		""" Checks if there is information about the date of birth of the user """
		if self.holder in Birthday_data:
			return Birthday_data[self.holder]
		else:
			return "There is no information about date of birth of this user in database please try again."

	def SSN_check(self):
		"""Chechs if there is information about the SSN Code of the user """
		if self.holder in SSN:
			return SSN[self.holder]
		else:
			return "There is no information about CCN of this user in database please try again."

	def Database_information(self):
		"""Checks if there is any information about the user  - such as day of birth 
		and Social Security Number(SSN)
		"""
		if self.holder in Birthday_data and self.holder in SSN:
			return True
		else:
			if not (self.holder in ERROR):
				ERROR[self.holder] = 'Unknown Entry'

	def CardIsValid(self):
		"""Checks to make sure that the Credit Card Number is Valid by Luhn Algorithm"""
		Cardnum = self.card_number
		sum = 0
		num_digits = len(Cardnum)
		oddeven = num_digits & 1
		for count in range(0, num_digits):
			digit = int(Cardnum[count])
			if not (( count & 1 ) ^ oddeven ):
				digit = digit * 2
			if digit > 9:
				digit = digit - 9
			sum = sum + digit
		return ( (sum % 10) == 0 )

	def PIN_IsValid(self):
		"PIN Generator for this specific bank(Bank X)"
		temporary = []
		if self.CardIsValid():
			indent = ''
			for i in self.card_number:
				temporary.append(i)
			first, sum1 = temporary[0:4], 0
			second, sum2 = temporary[4:8], 0
			third, sum3 = temporary[8:12], 0
			forth, sum4 = temporary[12:16], 0
			for i in first:
				sum1 = sum1 + int(i)
			for j in second:
				sum2 = sum2 + int(j)
			for k in third:
				sum3 = sum3 + int(k)
			for l in forth:
				sum4 = sum4 + int(l)

			# Encoding for the first digit of the PIN
			if sum1>=0 and sum1<4:
				one = 0
			elif sum1>=4 and sum1<9:
				one = 1
			elif sum1>=9 and sum1<14:
				one = 2
			elif sum1>=14 and sum1<18:
				one = 3
			elif sum1>=18 and sum1<21:
				one = 4
			elif sum1>=21 and sum1<23:
				one = 5
			elif sum1>=23 and sum1<27:
				one = 6
			elif sum1>=27 and sum1<30:
				one = 7
			elif sum1>=30 and sum1<33:
				one = 8
			else:
				one = 9

			#Encoding for the second digit of the PIN
			if sum2>=0 and sum2<4:
				two = 0
			elif sum2>=4 and sum2<8:
				two = 1
			elif sum2>=8 and sum2<14:
				two = 2
			elif sum2>=14 and sum2<18:
				two = 3
			elif sum2>=18 and sum2<20:
				two = 4
			elif sum2>=20 and sum2<23:
				two = 5
			elif sum2>=23 and sum2<26:
				two = 6
			elif sum2>=26 and sum2<30:
				two = 7
			elif sum2>=30 and sum2<32:
				two = 8
			else:
				two = 9

			#Encoding for the third digit of the PIN
			if sum3>=0 and sum3<3:
				three = 0
			elif sum3>=3 and sum3<9:
				three = 1
			elif sum3>=9 and sum3<14:
				three = 2
			elif sum3>=14 and sum3<18:
				three = 3
			elif sum3>=18 and sum3<20:
				three = 4
			elif sum3>=20 and sum3<23:
				three = 5
			elif sum3>=23 and sum3<28:
				three = 6
			elif sum3>=28 and sum3<30:
				three = 7
			elif sum3>=30 and sum3<33:
				three = 8
			else:
				three = 9

			# Encoding for the forth digit of the PIN
			if sum4>=0 and sum4<2:
				four = 0
			elif sum4>=2 and sum4<7:
				four = 1
			elif sum4>=7 and sum4<10:
				four = 2
			elif sum4>=10 and sum4<14:
				four = 3
			elif sum4>=14 and sum4<18:
				four = 4
			elif sum4>=18 and sum4<22:
				four = 5
			elif sum4>=22 and sum4<26:
				four = 6
			elif sum4>=26 and sum4<30:
				four = 7
			elif sum4>=30 and sum4<33:
				four = 8
			else:
				four = 9

			answer = 1000 * one + 100 * two + 10 * three + four
			if str(answer) == self.PIN:
				return True
			else:
				return False
		else:
			return False

	def Account_Type_Info(self):
		"""Checks the type of the account"""
		if self.holder in Account_Type:
			return Account_Type[self.holder]
		else:
			print("There is no information about you in current database")
			return False

	def Saving(self, amount):
		"""Imposes a 0.5$ deposit fee"""
		return amount - 0.5

	def Checking(self, amount):
		"""Imposes a 1$ withdrawal fee"""
		return amount - 1

	def Sequrity_Check(self):
		"""Checks if there is a full information about the user in the database"""
		message = 'Dear {0},'.format(self.holder)
		if self.CardIsValid() == True and self.PIN_IsValid() == True and self.Database_information() == True:
			return True
		else:
			print(message)
			print("Trying to verify your account information from the database")
			if self.Database_information() == True:
				print(message)
				print("Your information has been found in the database")
				return True
			else:
				print(message)
				print("There is no information about you in current database")
				return False

	def deposit(self, PIN):
		"""Deposits amount to the account"""
		message = 'Dear {0},'.format(self.holder)
		if self.Sequrity_Check() == True:
			balance = self.balance
			attemp_list = []
			def deposit_try(amount, PIN_attempt):
				nonlocal balance
				if len(attemp_list) == 3:
					print(message)
					return "Your account is locked." 
				if PIN_attempt != self.PIN:
					attemp_list.append(attemp_list)
					print(message)
					return "Incorrect PIN"
				balance = self.Saving (balance + amount)
				self.balance = balance
			return deposit_try
		else:
			print("An error occured during transaction")
			print("You provided incorrect information")
			return

	def withdraw(self, PIN):
		"""Withdrows amount from the account"""
		message = 'Dear {0},'.format(self.holder)
		if self.Sequrity_Check() == True:
			balance = self.balance
			attemp_list = []
			def withdraw(amount, PIN_attempt):
				nonlocal balance
				if len(attemp_list) == 3:
					print(message)
					return "Your account is locked." 
				if PIN_attempt != self.PIN:
					attemp_list.append(attemp_list)
					print(message)
					return "Incorrect PIN"
				if amount > balance:
					print ("Insufficient funds")
					print ("Do you want to apply for loan?")
					print("yes/no")
					variable = input('Your answer!:')
					if variable == 'yes':
						return self.overdrown()
					else:
						return 
				balance = self.Checking(balance - amount)
				self.balance = balance
			return withdraw
		else:
			print("An error occured during transaction")
			print("You provided incorrect information")
			return

	def overdrown(self):
		# a = Account('Rafa', '4815820036130845', '4224')
		balance = self.balance
		bool = False
		""" Makes sure that account balance will not be below 0."""
		message = 'Dear {0},'.format(self.holder)
		print(message)
		print ("Dear User Your Account Balance Can Be Negative")
		print("Indicate the amount you want apply for?")
		print ("1. $250")
		print ("2. $500")
		print ("3. $1000 (Another number will bring to $250) ")
		print ("Choose an option - 1 / 2 / 3")
		# If you will input another arbitrary number it automatically will choose 3.
		option = input()
		if option == '1':
			balance = self.Saving (balance + 250)
			bool = True
		elif option == '2':
			balance = self.Saving (balance + 500)
			bool = True
		else:
			balance = self.Saving (balance + 1000)
			bool = True
		self.balance = balance
		print( self.balance)

		print ("Do you want to calculae the rate? yes/no")
		ans = input()
		interest = 0.0001
		if ans == 'yes':
			print("Indicate the duration of the loan?")
			print ("1. 1 year")
			print ("2. 2 years")
			print ("3. 3 year. (Another number will bring to 3 year) ")
			time = input()
			if time == 1:
				rate = 250 * (0.7+ interest)
			elif time == 2:
				rate = 500 * pow((0.7 + interest), 2)
			else:
				rate = 1000 * pow((0.7 + interest), 3)
			return rate
		else:
			return 






	
