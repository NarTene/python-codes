
# create a tuple, print its elements
# print the second element of the tuple
# print the lenght
# add an item at the end named school at the end of the tuple
# replace the first item with an item named kiwi

# create a tuple 
my_shopping_bag = ("eggs", "tomatoes", "corn", "sugar", "coffee", "banana", "plantain", "red beans", "milk", "water bottle", "apple juice")

# print tuple's items
print(my_shopping_bag)

# print the second item of the tuple
print(my_shopping_bag[1])

# print the length pf tuple
print(len(my_shopping_bag))

# add an item named school at the end of the tuple 
y = list(my_shopping_bag)
y.append("school")
my_shopping_bag = tuple(y)

print(my_shopping_bag)

# replace the first element with an element named kiwi

z = list(my_shopping_bag)
z[0] = "kiwi"
my_shopping_bag = tuple(z)
print(my_shopping_bag)


