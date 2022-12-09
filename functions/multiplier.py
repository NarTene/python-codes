'''
multiplier.py: this code returns the product of all even number in a list.
'''
#global 
numbers = [8, 9, 11, 20, 32, 101, 100]

def multiply_even_number(list_integer):

    '''
    This function will return the product of all even numbers in a list.
    args:
    list_integer (list): user provides this list of integer
    Returns:
    product (integer): product of all even numbers in the list
    
    '''
    product = 1
    for num in list_integer:
        if num % 2 == 0:
            product = product * num 
    return product
    
# body of the main
if __name__ == '__main__':

    try:
        # printing the product of all even numbers
        productf = multiply_even_number(numbers)
        print("The product of all even numbers in the list :\n", productf)
    except TypeError: 
        print ("Oops!  That was no a valid list of integer. Please provide a list of type integer and  Try again...")