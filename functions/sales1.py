
'''
sales1.py: This code returns items in the grocery cart total price in a receipt.
'''
# create order dictionary
order={'tomato':30, 'Thyme':4.50, 'garlic':7.75, 'onions':4, 'fish':9.99, 'pepper':5}

def sales(grocery_item):
    with open("receipt.txt", "w") as file:
      
        
        # compute total price, Iterate each element in dictionary and add them in variable total
        total = 0
        for price in order:
            total = total + order[price]
        
        # printing items cost
        print("The cost of all items in my grocery cart in $: ", total)

        # writing to receipt.txt
        total= str(total)
        file.write("The cost of all items in my grocery cart in $:\n ")  
        file.write(total)
        
sales("cost")           