word = None


while True:
	word = input("Enter word to see if its a palandrome: ")
	if word == word[::-1]:
		print("This word is a palandrome!")
		again = input("Would you like to try again? (y/n) ")
		if again == "y":
			word = None
		else:
			break
	else:
		print("Please try again. Not a palandrome")
		word = None
