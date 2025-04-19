# weekly task 07
# write a program that reads a text file and outputs the number of e's it contains.
# program should take a filename from an argument on the command line.
# author: Dave Byrne :)

'''
Research:
https://www.geeksforgeeks.org/how-to-use-sys-argv-in-python/
'''

import sys # importing sys to use for command line arguments

if len(sys.argv) < 2: # check if filename is provided
    print("Please provide a filename as an argument.")
    sys.exit(1) # exit with error code

filename = sys.argv[1]

try:
    with open(filename, 'r') as file: # open file in read mode
        content = file.read() # read file
        count = content.count('e') # count occurrences of 'e'
        print(f"There are {count} e's in '{filename}'.") # print result
except FileNotFoundError:
    print(f"File '{filename}' not found.")
    sys.exit(1)

