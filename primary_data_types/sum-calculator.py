
# This program allows you to sum up two numbers
print("***********Welcome to our sum calculator program***********")

# Read users inputs from the keyboard and convert them to float
number1 = float(input('please enter your first number: '))
number2 = float(input('please enter your second number: '))

# Compute the sum of two numbers: number1 and number2
sum = number1 + number2

# Display the sum of the two numbers
print('The sum of {} and {} is:'.format(number1, number2) + ' ' + str(sum))

