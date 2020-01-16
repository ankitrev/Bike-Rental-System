from Models.BikeRent import BikeRental
from Models.Customer import Customer

def main():
	shop = BikeRental(100)
	customer = Customer()

	while True:

		choice = input("Enter Choice: ")

		try:

			choice = int(choice)
		except ValueError:
			print("That's not a valid choice!")
			continue

		if choice == 1:
			shop.display_stock()
		elif choice == 2:
			customer.rental_time = shop.rent_bike_on_hourly_basis(customer.request_bike())
			customer.rental_basis = 1
		elif choice == 3:
			customer.rental_time = shop.rent_bike_on_daily_basis(customer.request_bike())
			customer.rental_basis = 2
		elif choice == 4:
			customer.rental_time = shop.rent_bike_on_weekly_basis(customer.request_bike())
			customer.rental_basis = 3
		elif choice == 5:
			customer.bill = shop.return_bike(customer.return_bike())
			customer.rental_basis, customer.rental_time, customer.bikes = 0, 0, 0
		elif choice == 6:
			break
		else:
			print("Invalid input. Please enter number between 1-6 ")
	print("Thank you for using the bike rental system")



if __name__ == '__main__':
	main()