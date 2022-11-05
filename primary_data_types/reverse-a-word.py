
# This program allows a user to enter a word and reverse it.
print("***********Welcome to our program to reverse a word***********")

# enter your word in the keyboard
word = input("please enter your word:\n ")

# spliting the word
word_list = word.split(",")

# reversing the word
word_list = list(reversed(word))

# printing the word
print(word_list, "\n")


# returning the word
print("".join(word_list))




