
INTRODUCTION TO TUPLES AND SETS

Tuple
* Tuples are used to store multiple items in a single variable.
* A tuple is a collection which is ordered and unchangeable.
Tuple Items
* Tuple items are ordered, unchangeable, and allow duplicate values.
* Tuple items are indexed, the first item has index [0], the second item has index [1] etc.
example:
    my_fruit_tuple = ("apple", "banana", "cherry", "apple", "cherry")
    print(my_fruit_tuple)

Tuple Length
* To determine how many items a tuple has, use the len() function:

Example
Print the number of items in the tuple:

fruit = ("apple", "banana", "cherry")
print(len(fruit))

Tuple Items - Data Types
* Tuple items can be of any data type: String, int and boolean data type.
example
fruit1 = ("apple", "banana", "cherry")
num = (1, 5, 7, 9, 3)
boolean_tuple = (True, False, False)
mix_type = ("abc", 34, True, 40, "male")

The tuple() Constructor
* It is also possible to use the tuple() constructor to make a tuple.
Using the tuple() method to make a tuple:
make_fruit = tuple(("apple", "banana", "cherry"))
print(make_fruit)

Access Tuple Items
* You can access tuple items by referring to the index number, inside square brackets:
Print the first item in the tuple:

fruit = ("apple", "banana", "cherry")
print(fruit[0])

Range of Indexes
* You can specify a range of indexes by specifying where to start and where to end the range.
* When specifying a range, the return value will be a new tuple with the specified items.

Return the third, fourth, and fifth item:
fruit = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(fruit[2:5])

