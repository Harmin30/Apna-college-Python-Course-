# ......File input/output.......    
#
# File I/O in Python allows you to read from and write to files.
# You can open a file, read its contents, write to it, and close it when done.      
# The `open()` function is used to open a file, and it returns a file object.
# The file object provides methods to read from and write to the file.
#
#types of file I/O:
#1. Text I/O : .txt files, .csv files,.docx,.log  etc.
#2. Binary I/O : .mp3 files, .jpg files, etc.

f = open("/Users/apple/Desktop/Python full Course/Ch7_File_I/demo.txt","r")
data = f.read()
print(data)  # This will print the contents of the file
f.close()

# Reading a file line by line.

f = open("/Users/apple/Desktop/Python full Course/Ch7_File_I/demo.txt","r")
line1 = f.readline()  # Reads the first line of the file
print(line1)  # This will print the first line of the file

line2 = f.readline()
print(line2)  # This will print the second line of the file

f.close()

# Writing to a file.

f = open("/Users/apple/Desktop/Python full Course/Ch7_File_I/demo.txt","w")

f.write("i want to learn java\n")

f.close()

with open("/Users/apple/Desktop/Python full Course/Ch7_File_I/demo.txt","r") as f:
    data = f.read()
    print(data)  # This will print the contents of the file after writing to it
# Using 'with' statement to handle file I/O automatically closes the file.

with open("/Users/apple/Desktop/Python full Course/Ch7_File_I/demo.txt","w") as f:
    f.write("new data\n")

#  Deleting a file using the os module.

# Module (Like a code library ) is a file written ny another programmer 
# that contains a functions we can use.

import os

os.remove("/Users/apple/Desktop/Python full Course/Ch7_File_I/demo.txt")  # Deletes the file named demo.txt in the current directory
# Note: Make sure to handle exceptions when working with file I/O, 
# such as checking if the file exists before trying to read or write to it.


# Lets Practice : 

#Q1. Create a new file "practice.txt" using python .Add the following data in it :

# Hi everyone 
# This is a practice file.
# i am learning file I/O using java
# i like programming in java.

#WAF that replaces the word "java" with "python" in the file "practice.txt".

# Search if the word "learning" is present in the file "practice.txt".

with open("practice.txt", "w") as f:
    f.write("Hi everyone\n")
    f.write("This is a practice file.\n")
    f.write("I am learning file I/O using java\n")
    f.write("I like programming in java.\n")
    
with open("practice.txt", "r") as f:
    data = f.read()

newdata = data.replace("java", "python")
print(newdata)

# Writing the modified data back to the file

with open("practice.txt", "w") as f:
    f.write(newdata)
# Searching for the word "learning" in the file
with open("practice.txt", "r") as f:
    content = f.read()
    if "learning" in content:
        print("The word 'learning' is present in the file.")
    else:
        print("The word 'learning' is not present in the file.")
# Note: Make sure to handle exceptions when working with file I/O,

#Q2.WAF to find in which line of the file does the word "learning " occurs first time.
#Print -1 if the word is not present in the file.

with open("practice.txt", "r") as f:
    lines = f.readlines()  # Read all lines into a list
    found = False
    for index, line in enumerate(lines):
        if "learning" in line:
            print(f"The word 'learning' occurs first at line {index + 1}.")
            found = True
            break
    if not found:
        print(-1)  # Print -1 if the word is not found in any line

#Q3. From a file containing numbers separated by commas,print the count of even numbers.
with open("numbers.txt", "w") as f:
    f.write("1,2,3,4,5,6,7,8,9,10")

with open("numbers.txt", "r") as f:
    numbers = f.read().split(",")  # Read the file and split by commas
    even_count = sum(1 for num in numbers if int(num) % 2 == 0)  # Count even numbers
    print(f"The count of even numbers is: {even_count}")

# Output:
# The count of even numbers is: 5