# convert if input is in degF
def convertF():
    temp = int(input("enter number to convert\n"))
    newTemp = (temp * 1.8) + 32
    print(temp, "C", "temp is", newTemp, "F")


# convert if input is in degC
def convertC():
    temp = int(input("enter number to convert\n"))
    newTemp = (temp - 32) / 1.8
    print(temp, "F", "temp is", newTemp, "C")

def main():
	convert = input("Enter F or C to convert. Q to Quit\n")
	if convert.upper() == "F":
			convertF()
	elif convert.upper() == "C":
			convertC()
	elif convert.upper() == "Q":
			print("Goodbye")
	else:
			print("Please enter F, C or Q only.")


def look_nice():
	print("Welcome to the temperature converter\n")
	print("*" * 36)
	print()
	main()


# run function
look_nice()
