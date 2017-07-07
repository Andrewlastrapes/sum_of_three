

# Write a Python program to calculate the sum of three given numbers, 
# if the values are equal then return thrice of their sum.

def sumofthree():
	number1 = int(input("Please enter a number: "))
	number2 = int(input("Please enter a number: "))
	number3 = int(input("Please enter a number: "))
	if number1 == number2 and number3 == number1:
		return((number1 + number2 + number3) * 3)
	else:
		return(number1 + number2 + number3)

print(sumofthree())

