number = raw_input("What number should I double? ")

notYetConverted = True

while notYetConverted:
	try:
		number = float(number)
		
	except ValueError:
		number = input("Sorry that is not a number, try again. ")
		
	else:
		notYetConverted = False

print("Double that is {}. ".format(number * 2))
