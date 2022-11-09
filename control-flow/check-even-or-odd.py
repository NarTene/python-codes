

# This program allows a user to enter a number and check whether the number is EVEN OR ODD.
print("***********Welcome to your code to check if a number is EVEN or ODD***********")

# enter a number to check
user_number = float(input("enter a number to check whether the number is EVEN or ODD:\n"))

# check if the number is EVEN or ODD
if user_number % 2 == 0:
    print(f"your number {user_number} is EVEN.")
else: 
    print(f"your number {user_number} is ODD.")

# printing
## printing
#print(f"your sentence is: {word}, and the reverse is: {reverse_word}.")