
'''
user_credential.py: This Program will first ask a user for a username and password and verify its validity.

'''
# user credential dictionary
user_credential = {"username":"john" ,"password" : "doe123"}

count = 0 
max = 5
state = bool()

while count < max:
  count = count + 1
  
  # ask user to input its username and password
  username= str(input("enter your username\n")).lower()
  password= str(input("enter your passwor\n")).lower()
  
  # verify user's credentials
  if username != user_credential["username"]  or password != user_credential["password"]:
      state = False
         
  elif username == user_credential["username"] and password == user_credential["password"] :
      state = True
      break

# printing the result based on the number of trials
if 0<count<5 and state == False:
  print("Sorry, access denied. Try again")

elif count == 5 and state == False:
  print("You account is locked")

elif 0<count<5 and state ==True:
  print("You have access to the system")

elif count == 5 and state == True:
  print("You have access to the system")