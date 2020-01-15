class Customer():

	def __init__(self):
		self.bikes = 0;
		self.rental_basis = 0
		self.rental_time = 0
		self.bill = 0

	def request_bike(self):

		bikes = input("How many bikes do you like to rent")
		try:
			bikes = int(bikes)
		except ValueError:
			print("That's not a positive integer!")
			return -1

		if bikes < 1:
			print("Invalid input. Number of bikes should be greater than zero!")
			return -1
		else:
			self.bikes = bikes

		return self.bikes

	def return_bike(self):

		if self.rental_basis and self.rental_time and self.bikes:
			return self.rental_basis, self.rental_time, self.bikes
		else:
			return 0, 0, 0

	


