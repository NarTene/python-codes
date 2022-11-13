# This program allows you to print out the last name of the second employee. 

# create a dictionary d with two nested dictionaries: employees, and owners
d = {"employees":[{"firstName":"John", "lastName":"Doe"}, 
                  {"firstName":"Anna", "lastName":"Smith"}, 
                  {"firstName":"Peter", "lastName":"Jones"}],
     "owners":[{"firstName":"Jack", "lastName":"Petter"},
               {"firstName":"Jessy", "lastName":"Petter"}]
}

# traversing the dictionary to get second employee's last name.
last_name = d["employees"][1]["lastName"]

# printing the last name
print(last_name)

