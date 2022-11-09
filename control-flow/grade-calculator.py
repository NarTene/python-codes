
# This program allows a student to enter his grades in 5 subjects, calculate the average, and print grade from A - E
print("***********Welcome to our program to compute and print grade***********")

# enter grade for each subject
print ("Please enter your grade number for each subject (enter a number beteween 0-100)")
bio= float(input("enter your grade for Biology:\n"))
math= float(input("enter your grade for Math:\n"))
phys= float(input("enter your grade for Physics:\n"))
chem= float(input("enter your grade for Chemistry:\n"))
eng= float(input("enter your grade for English:\n"))

# compute and print average
average = ( bio + math + phys + chem + eng)/5 
print("Your average is :" + str(average))

# printing grade
grade = average 

if grade > 90:
    print("Your grade is: A")
 
elif grade > 80:
    print("Your grade is: B")
 
elif grade > 70:
    print("Your grade is: C")
 
elif grade > 60:
    print("Your grade is: D")
 
else:
    print("Your grade is: E Failed")

# printing
## printing
#print(f"your sentence is: {word}, and the reverse is: {reverse_word}.")

