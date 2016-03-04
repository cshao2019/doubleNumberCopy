number = raw_input("What number should I double? ")

while number != "":
	try:
#Try block is only for exception causers- if the user messes up, not programmer. Put as little as possbile
		number = float(number)
	except ValueError: #susceptible that there will be an exception- put it under except
		print("Sorry, that is not a number.")
		number = raw_input("Try again: ")

	else:
#This will run in any case
		print("Double that is {}. ".format(number * 2))
		number = ""

#want to use it only when the user will cause an error