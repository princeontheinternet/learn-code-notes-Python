# Basics Of I/O with files using "with" statement


# The below piece of code rewrites and creates a file if it doesn't exist.
with open('test.txt', 'w') as my_file:
    my_file.write("This is a new file which I created using write method.\nI will append to this file later")

# This will read and print the lines of the file in the o/p
with open('test.txt', 'r') as my_file:
    print(my_file.read())

# This will create a list, which will contain each line as an element. This is the functionality of readlines() method.
with open('test.txt', 'r') as my_file:
    print(my_file.readlines())

"""
Different Modes: 

1. 'r': 
    This is the default mode. 
    It Opens file for reading.
    
2. 'w': 
    This Mode Opens file for writing.
    If file does not exist, it creates a new file.
    If file exists it truncates the file.
    
3. 'x':	
    Creates a new file. If file already exists, the operation fails.

4. 'a':	
    Open file in append mode.
    If file does not exist, it creates a new file.

5. 't':
    This is the default mode. It opens in text mode.

6. 'b':	    
    This opens in binary mode.

7. '+':	
    This will open a file for reading and writing (updating)
"""
