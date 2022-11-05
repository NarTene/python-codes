
# This program allows a user to enter a sentence and reverse it.
print("***********Welcome to our program to reverse a sentence***********")

# enter your sentence in the keyboard
word = input("please enter your sentence: ")

#splitting the words into a list using whitespaces or empty characters as separator
word_split = word.split()
print("The splitted sentence is: ", word_split)

# reversing the list 
re_word_split = reversed(word_split)

print("The reversed sentence is: ", list(re_word_split))

# Joining all items of the reversed list into a single string using whitespaces as separator
reverse_word = " ".join(reversed(word_split))

# printing
print(f"your sentence is: {word}, and the reverse is: {reverse_word}.")


