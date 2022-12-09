
'''
 sales.py: This code adds items in your grocery cart and returns total in a receipt.txt
'''
order = {'tomato':30, 'thyme':4.50, 'garlic':7.5, 'rice':10, 'onions':4, 'fish':9.99}

def add_items_values():
    '''
    This function add items' prices in your grocery cart and return the total.
    args: None
    Returns: Float
    
    '''
    return sum(order.values())

def create_receipt(total):

    '''
    This function writes to a file (receipt.txt).
    args: total(float)
    Returns: boolean
    
    '''
    with open("receipt.txt", "w") as file:
          
        file.write("==== Welcome to Walmart !!!! ====\n ")  
        file.write("\n")  
        file.write(f"The cost of all items in your grocery cart in: ${total}")  
    return True
# body of the main
if __name__ == '__main__':

    # compute total price
    try:
        total = str(add_items_values())
        print(f'The cost of all items in your grocery cart is: ${total}')

        # calling create receipt function
        create_receipt(total)
    except TypeError:
        print("Sorry, enter a valid dictionary. ... Try again")
    
    


