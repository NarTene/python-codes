
# This program allows to convert your body weight from lbs to kgs
print("***********Welcome to your body weight converter***********")

# Get users weight as a form of float
body_weight_pounds = float(input("Enter your body weight in lbs:\n "))

# Converting pounds into kgs
body_weight_kgs_0 = 0.453592 * body_weight_pounds
body_weight_kgs = round(body_weight_kgs_0, 3)

# Display the body weight in lbs and kgs
print(f"your body weight is: {body_weight_pounds} lbs, and the equivalent in kgs is: {body_weight_kgs} kgs. Thank you!")
