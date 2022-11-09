# This program allows you to print the largest and the smallest values of a list

# creating an empty list
list = []

# get the number of elements for the list
n = int(input("Enter number of elements : "))

# add elements to empty list
for i in range(n):
	element  = int(input(f"Enter the {i+1} element: \n"))
	list.append(element) 

# checking if the list is empty
if len(list)==0:
    print("print the list is empty")
else: 
   # printing largest and smallest elements
    print(f"Your list is: {list} the Largest and Smallest elements of the list are: {max(list)} , {min(list)}")
    # print(f"print the min of my list is: {min(lst)}")