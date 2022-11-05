# This program allows you to display aws account id from arn.
print("*******Welcome to the account id diplay program*******")

# initiate a variable aws_arn  and print the aws_arn value
aws_arn = "arn:aws:iam::123456789012:user/Development/product_1234/*"
print("The arn is: ", aws_arn)

# slicing the aws_arn to get the account id
account_id = aws_arn[13:25]             

# display the account id
print ("The account id is: ", account_id)

