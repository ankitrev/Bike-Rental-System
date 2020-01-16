import datetime

class BikeRental():

	def __init__(self,stock=0):
		self.stock = stock

	def display_stock(self):
		print("We have currently {} bikes available for rent.".format(self.stock))
		return self.stock

	def rent_bike_on_hourly_basis(self,n):

		if n <= 0:
			print("Number of bikes should be positive!")
			return None
		elif n > self.stock:
			print("Sorry we have currently {} bikes to rent.".format(self.stock))
		else:
			now = datetime.datetime.now()
			print("You have rented a {} bike(s) on hourly basis today at {} hours.".format(n,now.hour))
			print("You will be charged Rs. 50 for each hour per bike.")
			print("We hope thate you enjoy our service.")
			self.stock -= n
			return now

	def rent_bike_on_daily_basis(self,n):

		if n <= 0:
			print("Number of bikes should be positive!")
			return None
		elif n > self.stock:
			print("Sorry we have currently {} bikes to rent.".format(self.stock))
		else:
			now = datetime.datetime.now()
			print("You have rented a {} bike(s) on hourly basis today at {} hours.".format(n,now.hour))
			print("You will be charged Rs. 200 for each hour per bike.")
			print("We hope thate you enjoy our service.")
			self.stock -= n
			return now

	def rent_bike_on_weekly_basis(self,n):

		if n <= 0:
			print("Number of bikes should be positive!")
			return None
		elif n > self.stock:
			print("Sorry we have currently {} bikes to rent.".format(self.stock))
		else:
			now = datetime.datetime.now()
			print("You have rented a {} bike(s) on hourly basis today at {} hours.".format(n,now.hour))
			print("You will be charged Rs. 600 for each hour per bike.")
			print("We hope thate you enjoy our service.")
			self.stock -= n
			return now


	def return_bike(self,request):

		rental_basis, rental_time, no_of_bikes = request
		bill = 0

		if rental_time and rental_basis and no_of_bikes:
			self.stock += no_of_bikes
			now = datetime.datetime.now()
			rental_period = now - rental_time

			if rental_basis == 1:
				bill = round(rental_period.seconds/3600) * 50 * no_of_bikes
			elif rental_basis == 2:
				bill = round(rental_period.days) * 200 * no_of_bikes
			elif rental_basis == 3:
				bill = round(rental_period.days/7) * 600 * no_of_bikes

			if (3 <= no_of_bikes <= 5):
				print("You are eligible for family rental promotion of 40% discount.")
				bill = bill * 0.6

			print("Thanks for returning your bike. Hope you enjoyed our service!")
			print("That would be Rs. {}.".format(bill))
			return bill

		else:
			print("Are you sure you rented a bike with us.")
			return None



