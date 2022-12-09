'''
copytor.py: This code copies the contents of a file to a second file using functions.
'''
def write_story(line):
    
    # writing to story.txt
    with open("story.txt", "w") as my_file:
        my_file.write("Note: We've provided you with the first chapter \n")
        my_file.write("of Alice's Adventures in the Wonderland to give you \n")
        my_file.write("some sample text to work with. \n")
        my_file.write("This is also the text used in the tests. \n")

# printing story.txt contents to the console output
    with open("story.txt") as my_file:
        print(my_file.read())

# copying story.txt to story_copy.txt
def copy(file1, file2):
    with open("story.txt", "r") as first, open ("story_copy.txt", "w") as second:
        # read in the first file
        for line in first:
            # write in the second file 
            second.write(line)


# calling write_story function
write_lines = 'cars'
write_story("write_lines")

# calling the copy function
copy("story.txt", "story_copy.txt")
